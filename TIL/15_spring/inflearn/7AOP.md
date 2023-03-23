# AOP(Aspect Oriented Programming)

## AOP가 필요한 상황

모든 메소드의 호출 시간을 측정하고 싶을 때 

매 메소드(메소드가 너무 많아지면 오또케 ;;)에 호출 시간을 print 해줘야함

```java
public Long join(Member member) {
    long start = System.currentTimeMillis();
    
    try {
        validateDuplicateMember(member);
        memberRepository.save(member);
        return member.getId();
    } finally {
        long finsh = System.currentTimeMillis();
        long timeMs = finish - start;
        System.out.println("join = " + timeMs + "ms");
    }
}
```



주요 기능(core concern)이 아닌 사항을 공통 관심 사항(cross-cutting concern)이라고 함

ex) 회원가입에 시간을 측정하는 기능



시간 측정 로직을 만들어놓고 원하는 기능에 공통관심사항을 적용함 

매 메소드마다 만드는게 아니고!



```java
package hello.hellospring.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Aspect;

@Aspect
// @Component: 아래처럼 직접 등록안하고 이렇게 해도 됨!
public class TimeTraceAop {
    
    @Around("execution(* hello.hellospring..*(..))")
    public Object execute(ProceedingJoinPoint joinPoint) throws Throwable {
        long start = System.currentTimeMillis();
        System.out.println("START : " +joinPoint.toString());
        try {
            Object result = joinPoint.proceed();
            return result;
        } finally {
            long finish = System.currentTimeMillis();
            long timeMs = finish - start;
            System.out.println("END : " +joinPoint.toString() + " " + timeMs + "ms");
        }
    }
}
```

springConfig

```java
@Configuration
public class SpringConfig {
    
    //aop는 configuration에 등록해주는게 더 좋음
    @Bean
    public TimeTraceAop timeTraceAop() {
        return new TimeTraceAop();
    }
}
```



* Around
  * 공통 관심사를 타게팅하는 것



=> 결론

* 회원가입, 회원 조회 등 핵심 관심사항과 공통 관심사를 분리

* 핵심 관심 사항을 깔끔하게 유지
* 변경이 필요하면 aop만 변경 가능
* 원하는 적용 대상을 around를 통해 선택 가능