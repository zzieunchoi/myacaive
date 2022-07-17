# java 기본 및 응용

JVM - java virtual machine

: write once, compile, machine code

운영 체제 종속적이지 않음, 윈도우, 리눅스, 맥오에스 전부 다 사용 가능



자바의 특징 중 하나로 더 이상 사용하지 않는 메모리를 자동으로 정리하는 기능을 무엇이라고 하는가?

- garbage collection



자바의 객체 지향 특징 4가지 

- abstraction
- polymorphism
- inheritance
- encapsulation



타입이란? 자바가 가지고 있는 데이터 타입 

- 기본형(primitive type)
  - 미리 정해진 크기의 memory size로 표현
  - 변수 자체에 값 저장
  - ex
    - 논리형
      - boolean(true/ false)
    - 정수형
      - byte(8), short(16), **int(32)**, long(64)
    - 실수형
      - float(32), double(64)
    - 문자형
      - char(16)
- 참조형(reference type)
  - 크기가 미리 정해질 수 없는 데이터의 표현
  - 변수에는 실제 값을 참조할 수 있는 주소만 저장



* 형변환

  * 묵시적 형변환(작은집 -> 큰집)

    ```java
    byte b = 10;
    int i = (int)b;
    int i2 = b; // 이거는 그냥 넣어도 상관 x
    ```

  * 명시적 형변환( 큰집 -> 작은집)

    ```java
    int i = 300;
    byte b = (byte)i;
    ```

    

```java
public class BP_09 {
  public static void main(String[] args) {
    int i1 = Integer.MAX_VALUE;
    int i2 = i1 + 1;
    System.out.println(i2);

    long l1 = i1 + 1;
    System.out.println(l1);

    long l2 = (long) (i1 + 1);
    System.out.println(l2);

    long l3 = (long) i1 + 1;
    System.out.println(l3);

    int i3 = 1000000 * 1000000 / 100000;
    int i4 = 1000000 / 100000 * 100000;
    System.out.println(i3 + " : " + i4);
  }
}
```



주사위 수 랜덤 뽑기

```java
import java.util.Random;

public class App {
    public static void main(String[] args) {
      int N = 6;

      int num = (int) (Math.random() *N) +1;
      System.out.println(num);

      Random rand =new Random();
      num = rand.nextInt(N)+1;
      System.out.println(num);
    }
  }
```



## 조건문

* if

  * 논리형, 비교식, method call

    ```java
    int a = 20;
    String grade = null;
    
    if (a >= 19) {
        grade = "성인";
    } else if (a >= 13) {
        grade = "청소년";
    } else if (a >= 6) {
        grade = "아동";
    } else {
        grade = "유아";
    }
    ```

    

* switch

  * 정수호환, enum, class object, method call

    ```java
    int month = 3;
    int day = -1;
    switch (month) {
        case 2:
            day = 29; break;
        case 4:
        case 6:
        case 9:
        case 11:
            day = 30; break;
        default:
            day = 31;
    }
    ```



★ 이 때 랜덤 숫자 꺼내오기!

```
import java.util.Random;
int N = 6;
Random rand = new Random();
int num1 = rand.nextInt(N)+1;

현재 이상태에서 rand.nextInt(6)이니까 이건 0~5사이의 랜덤 값을 구하는 것임
따라서 1~6 랜덤 값을 구하기 위해서는 +1을 해줘야함!

boolean nextBoolean()
boolean형 난수 반환

int nextInt()
int형 난수 반환

int nextInt(int n)
0~n 미만의 정수형 난수 반환

long nextLong()
long형 난수 반환

void nextBytes(Byte[] bytes)
-

float nextFloat()
float형 난수 반환

double nextDouble()
double형 난수 반환
```



## 반복문

* for문

  ```
  for ( 변수 초기화; 변수 조건; 변수 증가) {
       break;
  }
  ```

   

  100번 주사위를 던진 결과의 합과 평균값(실수)을 출력하는 코드를 for문을 이용하여 구현

  ```java
  public class App {
      public static void main(String[] args) {
        int sum = 0;
        int cnt = 100;
        double avg = 0;
        Random rand = new Random();
          
        for (int i = 0; i < cnt; i++) {
            sum += rand.nextInt(6)+1;
        }
        avg = 1.0*sum/cnt;
          
        System.out.printf("sum: %d, avg: %f%n", sum, avg);
      }
    }
  ```

* while 문

  ```
  변수 초기화
  while( 반복조건 ) {
      실행문
      증감식
      break;
  }
  ```

   

  100번 주사위를 던진 결과의 합과 평균값(실수)을 출력하는 코드를 while문을 이용하여 구현

  ```java
  public class App {
      public static void main(String[] args) {
        int sum = 0;
        int cnt = 100;
        double avg = 0;
        Random rand = new Random();
        int i = 0;
        
        while (i < cnt) {
            sum += rand.nextInt(6)+1;
            i++;
        }
        avg = 1.0*sum/cnt;
        System.out.printf("sum: %d, avg: %f%n", sum, avg);
      }
    }
  ```



★ 이 때 반복문에 라벨 이름 설정 가능

```java
public static void main(String[] args) {
    outer: for (int i=1; i <10; i++) {
        for (int j= 1; j<10; j++) {
            if (j==5) break outer;
            if (j==3) continue outer;
            
            System.out.print(i*j+" ");
        }
        System.out.println();
    }
}
```





## print

* println: 데이터를 출력한 후 자동으로 다음줄로 넘어감

* print: 줄바꿈을 하지 않음

  ```java
  public class Foo {
    public static void main(String[] args) {
  
      System.out.println("println 은 다음줄로 자동으로 줄바꿈합니다.");
      System.out.println("println 은 다음줄로 자동으로 줄바꿈합니다.");
      System.out.println("println 은 다음줄로 자동으로 줄바꿈합니다.");
  
  
      System.out.println(); // 한 줄의 빈 줄 넣고, 줄바꿈하기
  
  
      System.out.print("print 는 계속 이어서 출력합니다.");
      System.out.print("print 는 계속 이어서 출력합니다.");
      System.out.print("print 는 계속 이어서 출력합니다.");
  
    }
  }
  
  /* println 은 다음줄로 자동으로 줄바꿈합니다.
  println 은 다음줄로 자동으로 줄바꿈합니다.
  println 은 다음줄로 자동으로 줄바꿈합니다.
      
  print 는 계속 이어서 출력합니다.print 는 계속 이어서 출력합니다.print 는 계속 이어서 출력합니다. */
  ```

* printf : 포맷 형식에 따라출력

  ```
  %d	정수형 출력
  %s  문자형 출력
  %f	실수형 출력
  %c	문자열 출력
  %n	줄 바꿈
  %b	boolean 출력
  ```

  ```java
  public class App {
    public static void main(String[] args) {
      int year = 2;
      String area = "서울";
      System.out.printf("줄을 바꿀 수 %n");
      System.out.printf("있다. %n");
  
      System.out.printf("방을 %d년 계약했다. %n", year);
      System.out.printf("나는 %s에 살고 있다", area);
  
    }
  }
  
  /* 줄을 바꿀 수 
  있다. 
  방을 2년 계약했다. 
  나는 서울에 살고 있다 */
  ```

  
