# chap1

## bean(빈)

bean: 객체

빈 컨테이너 관리 

@Configuration은 자바를 설정하는 파일임을 명시해주는 annotation



chap1/Greet.java 만들기

```java
package chap1;

import lombok.Data;

@Data
public class Greet {
	private String format; // %s님, 안녕하세요
	
	public String greet(String name) {
		return String.format(format, name);
	}
}
```

chap1/Main.java(Greet.java를 실행할 객체 생성)

bean 꺼내기

```java
package chap1;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
public class Main {

	public static void main(String[] args) {
//		Greet g = new Greet();
//		g.setFormat("%s님, 안녕하세요");
//		String msg = g.greet("홍길동");
//		System.out.println(msg);
		
		// java 설정 방식(이 한줄로 AppContext.class bean을 읽어서 컨테이너에 등록)
		AnnotationConfigApplicationContext 
            ctx = new AnnotationConfigApplicationContext(AppContext.class);
        
		Greet g = (Greet)ctx.getBean("greet");
		System.out.println(g.greet("홍길동"));
        //홍길동님, 안녕하세요.
		
		Greet g2 = (Greet)ctx.getBean("greet");
		System.out.println(g == g2);
        //true
        
        Greet g3 = ctx.getBean("hello", Greet.class);
		System.out.println(g2 == g3);
        // true

	}

}

```

chap1/AppContext.java

greet이라는 이름으로 빈을 등록

```java
package chap1;

import org.springframework.context.annotation.Configuration;

@Configuration
public class AppContext {
	@Bean
    //@Scope(value = "prototype") = 이걸 쓴다면 singletone이 아니라서 다른 객체가 생성됨
    // 그렇다면 위에 ==가 모두 false가 됨
	public Greet greet() {
		Greet g = new Greet();
		g.format("%s님, 안녕하세요.")
		return g;		
	}
    
    @Bean
	public Greet hello() {
		return greet();
	}
}
```





xml로 하는 방법

//chap1/Greet.java

```java
package chap1;

import lombok.Data;

@Data
public class Greet {
	private String format; // %s님, 안녕하세요
	
	public String greet(String name) {
		return String.format(format, name);
	}
}
```

//servlet-context.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans
	xmlns="http://www.springframework.org/schema/mvc"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:beans="http://www.springframework.org/schema/beans"
	xmlns:context="http://www.springframework.org/schema/context"
	xsi:schemaLocation="http://www.springframework.org/schema/mvc https://www.springframework.org/schema/mvc/spring-mvc.xsd
		http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
		http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

	<beans:bean id="greet" class="chap1.Greet">
		<beans:property name="format" value="%s님, 안녕하세요" />
	</beans:bean>

</beans:beans>

```

//MainXML.java

```java
package chap1;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainXML {

	public static void main(String[] args) {
		ClassPathXmlApplicationContext 
		ctx = new ClassPathXmlApplicationContext("chap1/servlet-context.xml");
		Greet g = (Greet) ctx.getBean("greet");
		System.out.println(g.greet("홍길동"));
        // 홍길동님, 안녕하세요
        
        Greet g2 = (Greet)ctx.getBean("greet");
		System.out.println(g == g2);
        // true

	}

}

```



# chap2

## 빈 주입

Dependency Injection (의존성 주입): DI

A,B 객체가 있을 때 A에서 B가 필요하면 new B();이렇게 사용함

이 때, B의 이름이 바뀐다면 new B();의 이름을 모두 바꿔줘야함 그렇게 하면 너무 귀찮아짐

따라서, 필요할 때마다 **string이 주체**가 되어 객체를 주입한다 하여 빈 주입이라고 함

```java
MemberDAO.java
package chap2;
import org.springframework.stereotype.Component;

@Component
public class MemberDAO {
	public void insert() {
		// db 등록
		System.out.println("가입");
	}
	public void login() {
		// db 조회
		System.out.println("로그인");
	}
}

```

빈 생성하고 등록하기 위한 @Component

```java
MemberService.java
package chap2;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
@Component
public class MemberService {
	
	@Autowired
	MemberDAO dao;
	
	public boolean regist() {
		dao.insert();
		return true;
	}

	public void login() {
		dao.login();	
	}
	
	// 원래 이렇게 해야함
	//public boolean regist() {
	//	MemberDAO dao = new MemberDAO();
	//	dao.insert();
	//	return true;
	//}

	//public void login() {
	//	MemberDAO dao = new MerberDAO();
	//	dao.login();	
	//}
}
```

```java
MemberController.java
package chap2;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class MemberController {
	@Autowired
	MemberService service;
	
	@RequestMapping("/member/insert.ssg")
	public String insert() {
		service.regist();
		return "home";
	}
}
```





jsp와 연동

```java
MemberController.java
package chap2;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class MemberController {
	@Autowired
	MemberService service;
	
	@RequestMapping("/member/list.ssg")
	public String list() {
		service.regist();
		return "list";
	}
}    
```

```jsp
//list.jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
list
</body>
</html>
```



# chap3

MemberController.java, MemberDAO.java, MemberService.java를 복붙!

servlet.xml에 있는 내용를 java에 넣을거임!

```java
package chap3;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
// mvc 활성화 시키는 역할
@EnableWebMvc
@ComponentScan(basePackages = {"chap3"})
public class MvcConfig implements WebMvcConfigurer{
	
	@Override
	public void configureViewResolvers(ViewResolverRegistry registry) {
		registry.jsp("/WEB-INF/views/", ".jsp");
	}

}
```

```xml
web.xml

<servlet>
		<servlet-name>appServlet</servlet-name>
		<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
		<!-- 자바방식(클래스)으로 할건데 -->
		<init-param>
			<param-name>contextClass</param-name>
			<param-value>org.springframework.web.context.support.AnnotationConfigWebApplicationContext
			</param-value>
		</init-param>
    	<!-- 이클래스로 할꺼야 -->
		<init-param>
			<param-name>contextConfigLocation</param-name>
			<param-value>chap3.MvcConfig</param-value>
		</init-param>
		
		<load-on-startup>1</load-on-startup>
	</servlet>
```

```
이거는 xml 방식
<init-param>
	<param-name>contextConfigLocation</param-name>
	<param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
</init-param>
```

