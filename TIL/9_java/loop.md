# for문

for ( 초기화식 ; 조건식 ; 증감식) {

​	실행문;

}

단, 초기화 식에서 선언한 변수는 for문안에서만 사용 가능



```java
int sum = 0;
for ( int i = 1; i <= 100 ; i++) {
    sum = sum + i;
}
System.out.println("1~100의 합: " + sum);
```



변수 2개도 가능

```java
for ( int i = 0; i<= 50 && j >= 50; i++, j --) {
    ...
}
```



증감이 1이 아닐 수 도 있음

```java
int i = 0;
for ( i = 1; i <= 100 ; i+=2) {
    System.out.println(i);
}
```



## 중첩 for 문

```java
for ( int m = 2; m <= 9 ; m++) {
    ...
    for ( int n = 1; n <= 9; n++) {
        ...
    }
}
```



중첩된 for문 안에서 밖의 for문까지 종료시키고 싶을 때

```java
Outter : for (char upper ='A'; upper <='Z'; upper++) {
    for (char lower ='a'; lower<='z'; lower++) {
        System.out.println(upper + "-" + lower);
        if (lower == 'g') {
            break Outter;
        }
    }
}
```

밖의 for문에 이름을 붙이고 안에서 break [for문 이름]; 하면 밖의 for문까지 break;



## while

```java
int i = 1;
while ( i <= 10) {
    System.out.println(i);
    i++;
}
```



```java
Scanner scan = new Scanner (System.in);
boolean run = true;
while (run) {
    System.out.println("입략하세요>");
    String val = scan.next();
    System.out.println("입력란:" + val);
    if ("q".equals(val)) {
        run = false;
        System.out.println("끝~!");
    }
}
```

flag 변수를 이용하여 break 걸기



## 중첩 while 문

```java
int x = 1;
		
while ( x < 10 ) {
    int y = 1;
    System.out.println("\n*** " + x + "단 ***");

    while ( y < 10) {
        System.out.println(x + "x" + y + " = " + (x*y));
        y++;
    }
    x++;
}
```





