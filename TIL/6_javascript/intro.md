# javascript

html에서

`<head>`사이에 `<script>`에 저장



## intro

javascript의 필요성

브라우저 화면을 '동적'으로 만들기 위함

브라우저를 조작할 수 있는 유일한 언어



## 브라우저(browser)

* DOM 조작
  * 문서(HTML) 조작
  * 문서가 객체로 구조화되어있으며 key로 접근 가능
  * 문서를 프로그램으로 조작할 수 있다!
  * ![image-20220425134214316](220425.assets/image-20220425134214316.png)
  * DOM 해석
    * 파싱: 구문분석, 해석
    * 브라우저가 문자열을 해석하여 DOM TREE로 만드는 과정
* BOM 조작
  * navigator, screen, location, frames, history, XHR
  * 자바스크립트가 브라우저와 소통하기 위한 모델
  * 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능
* JavaScript Core(ECMA Script)
  * 브라우저를 조작하기 위한 명령어 약속(언어)
  * data structure(object, array), conditional expression, iteration





![image-20220425134103175](220425.assets/image-20220425134103175.png)

자바스크립트는 세미콜론을 선택적으로 사용 가능

세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨



코딩 스타일 가이드

[자바스크립트 코딩 스타일 가이드](https://github.com/airbnb/javascript)



## 변수 

식별자는 변수를 구분할 수 있는 변수명

* 변수명 기술 방법

  * 카멜 케이스(camelCase) - 변수, 객체, 함수에 사용
    * 두번째 단어의 첫글자부터 대문자

  * 파스칼 케이스(PascalCase) - 클래스, 생성자에 사용
    * 모든 단어 첫번쨰 글자 대문자

  * 대문자 스네이크 케이스(SNAKE_CASE) - 상수에 사용
    * 모든 글자 대문자 작성

  * underscore 기법 - 변수
    * 단어마다 underscore 사용
    * my_variable




* 변수명 지정 규칙
  * 식별자는 반드시 문자, 달러 또는 밑줄로 시작(숫자로 시작 x)
  * 대소문자를 구분하며, 클래스명 외에 모두 소문자로 시작
  * 예약어 사용 불가능(for, if, function)
  * 공백 불가



* 자료형
  * 기본형
    * 숫자형, 문자형, 논리형, undefined, null
  * 참조형
    * 배열, 함수, 객체



변수 선언 키워드

* let
  * **재할당 할** 예정인 변수 선언시 사용
  
  * 변수 재선언 불가능
  
  * 블록 스코프
  
    ```javascript
    let foo // 선언
    console.log(foo)
    
    foo = 1 // 할당
    console.log(foo)
    
    let bar = 0 // 선언+ 할당
    console.log(bar)
    ```
  
    ```javascript
    let number = 10
    number = 10
    console.log(number) // 가능
    ```
  
    ```javascript
    let number = 10
    let number = 50 // 불가능
    ```
  
    

* const
  * **재할당 할 예정이 없는** 변수 선언시 사용
  
  * 변수 재선언 불가능
  
  * 블록스코프
  
    ```javascript
    const number = 10
    number = 10 // 불가능
    ```
  
    ```javascript
    const number = 10
    const number = 50 // 불가능
    ```



### 블록 스코프

if, for, 함수 등의 중괄호 내부를 가리킴

블로 스코프를 가진 변수는 블록 바깥에서 접근 불가능

```javascript
let x= 1
if (x===1) {
    let x = 2
    console.log(x) //2
}
console.log(x) //1
```



### 변수 선언 키워드 var

구버전 자바스크립트는 var로 변수를 선언함

문제(hoisting 등)들이 계속해서 나와서 이제는 쓰지않고 지양함



![image-20220425141704998](220425.assets/image-20220425141704998.png)



## 데이터 타입

원시 타입/ 참조 타입으로 분류됨

![image-20220425143134468](220425.assets/image-20220425143134468.png)

원시타입

* 객체가 아닌 기본 타입
* 변수에 해당 타입의 값이 담김
* 다른 변수에 복사할 때 실제 값이 복사됨

1. 숫자(number)타입

   : 정수, 실수 구분 없는 하나의 숫자 타입, 부동소수점 형식을 따름

     NaN(계산 불가능한 경우 반환되는 값

2. 문자열(string)

   : ${expression}  형태로 표현식 삽입 가능

   큰따옴표, 작은따옴표 모두 사용 가능

   `"I'm a boy"`

   `'I\'m a boy` 둘다 사용 가능

3. undefined(값이 없긴 한데 개발자 의도 없어)

   변수의 값이 없음을 나타내는 데이터 타입, 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

4. null(변수의 값이 없는데 의도적으로 표현할 때)

   ```javascript
   lef firstName = null
   console.log(firstName) // null
   typeof null // object
   ```

5. boolean타입

   true, false 표현

   toBoolean Conversions 자동 형변환

![image-20220425144324206](220425.assets/image-20220425144324206.png)



참조타입

* 객체 태입의 자료형
* 변수에 해당 객체의 참조 값이 담김
* 다른 변수에 복사할 때 참조 값이 복사됨

1. 함수

   ```javascript
   function sum(a, b) {
       var s = a+b;
       return s;
   }
   document.write(sum(1, 2));
   
   // 일반적인 함수 지정
   function aaa(name) {
        console.log("안녕하세요 저는 " + name + " 입니다.");
    }
   aaa("최지은");
   
   // 함수 이름 없이 지정 (변수명을 지정해준 것임)
   var bbb = function (name) {
       console.log("안녕하세요 저는 " + name + " 입니다.");
   };
   bbb("최지은");
   
   // 그래서 aaa()는 부를 수 있지만 bbb()는 바로 실행하지 않으면 x
   (function abc() {
       aaa();
       bbb(); //에러 뜸
   })();
   ```

   * 콜백함수

     call(실행) + back(뒤)

     함수를 매개변수로 전달해서 함수 내부에서 실행

     ```javascript
     function ccc() {
         console.log("ccc함수 호출");
     }
     
     function ddd(func) {
         func();
     }
     ddd(ccc);
     
     // 계산기
     function plus(x, y) {
         return x + y;
     }
     
     function calculator(func, x, y) {
         return func(x, y);
     }
     
     var r = calculator(plus, 1, 2);
     console.log(r);
     // 3
     
     // 익명함수도 사용 가능
     var r = calculator(
         function (x, y) {
             console.log(x * y);
         },
         1,
         2
     );
     ```

   * arguments <span style="color:red">함수 선언시 동일하게 맞춰서 코딩해야하기 때문에 더 헷갈림</span>

     파라미터의 정보가 담긴 객체

     배열 형태로 저장

     모든 함수에 무조건 존재

     ```javascript
      function aaa() {
          console.log(typeof arguments);
          console.log(arguments);
          console.log(arguments[2]);
      }
     
     aaa(1, 2, 3, 4, 5);
     ```

2. 배열

3. 객체

   ```javascript
   var obj = {a:1, b:2, c:3};
   document.write(obj.a);
   document.write(obj['a']);
   ```



### 형변환

* 암시적 형변환

  ```javascript
  var a = 1;
  var b = "2";
  var c = a + b;
  document.write(typeof c);
  // string
  
  var d = "1";
  var e = true;
  var f = a + b;
  document.write(typeof f);
  // string
  
  var x = "2";
  var y = 1;
  var z = x - y;
  document.write(typeof z);
  // number
  ```

* 명시적 형변환

  * String()
  * Number()
  * parseInt()

  ```javascript
  var a = 1;
  document.write(typeof(a));
  
  var b = String(a);
  document.write(typeof(b));
  ```

  



## 연산자

1. 할당연산자

   ```javascript
   let x= 0
   x += 10
   console.log(x) //10
   
   x++  // += 연산자와 동일
   console.log(x) //11
   
   x--  // -= 연산자와 동일
   console.log(x) // 10
   ```

   

2. 비교 연산자

   문자열은 유니코드 값을 사용하며 표준 사전 순서를 기반으로 비교

   ```javascript
   const numOne = 1
   const numTwo = 10
   console.log(numOne < numTwo) // true
   
   const charOne = 'a'
   const charTwo = 'z'
   console.log(charOne > charTwo) // false
   ```

3. 동등 비교 연산자(==)

   두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값 반환

   비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교

   두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

   ```javascript
   const a = 1004
   const b = '1004'
   console.log(a==b) //true 

4. 일치 비교 연산자(===)

   두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값 반환

   엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음

   두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

   ```javascript
   const a = 1004
   const b = '1004'
   console.log(a === b) // false
   ```

5. 논리 연산자

   and: $$

   or: ||

   not: !

6. 삼항연산자

   세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자

   가장 왼쪽의 조건식이 참이면 콜론 앞의 값을 사용하고 그렇지 않으면 콜론 뒤의 값을 사용

   ```javascript
   console.log(true ? 1 : 2) //1
   console.log(false ? 1: 2) //2
   
   const result = Math.PI > 4 ? 'Yes' : 'No'
   console.log(result) // NO
   ```

7. 증감 연산자

   전위연산자, 후위 연산자

   ```javascript
   // 전위 연산
   var a = 1;
   var b = ++a;
   document.write("a=" + a + " b=" + b);
   // a=2 b=2
   
   // 후위 연산
   var c = 1;
   var d = c++;
   document.write("c=" + c + " d=" + d);
   // c=2 d=1
   ```



* 참조형 대입 연산은 값 자체가 대입 되는 것이 아님

  메모리 주소 값이 대입되는거라

  새로운 변수에는 주소만 저장되어있으므로 이전 변수 값이 변경되는 경우 새로운 변수도 값이 변경됨

  ```javascript
  var arr1 = [0, 1, 2];
  var arr2 = arr1;
  arr1[0] = 10;
  document.write(arr2[0]);
  ```

  

## 조건/반복

### 조건

if: 조건 표현식의 결과값을 boolean 타입으로 변환 후 참 / 거짓을 판단

```javascript
if (condition) {
    // do something
} else if (condition) {
    // do something
} else {
    // do something
}

const nation = 'Korea'

if (nation === 'Korea') {
    console.log('안녕하세요!')
} else if (nation === 'France') {
    console.log('Bonjour!')
} else {
    console.log('Hello!')
}
```

switch : 조건 표현식의 결과값이 어느 값에 해당하는지 판별

```javascript
switch(expression) {
    case 'first value':{
        // do something
        [break]
    }
    case 'second value':{
        // do something
        [break]
    }
    [default: {
         // do something
    }]
}

const nation = 'Korea'
switch(nation) {
    case 'Korea':{
        console.log('안녕하세요!')
        break
    }
    case 'France':{
        console.log('Bonjour!')
        break
    }
    default: {
         console.log('Hello!')
    }
}
```



### 반복

while

```javascript
let i = 0
while (i<6) {
    console.log(i) // 0, 1, 2, 3, 4, 5
    i +=1
}
// while 문에서 break 문은 선택적으로 작성 가능
```



for

```javascript
for (initialization; condition; expression) {
    //do something
}
// initialization: 최초 반복문 진입 시 1회만 실행되는 부분
// condition: 매 반복 시행 전 평가되는 부분
// expression: 매 반복 시행 이후 평가되는 부분


for (let i = 0; i<6; i++) {
    console.log(i) // 0, 1, 2, 3, 4, 5
}
```



for .. in: 주로 객체(딕셔너리)의 속성(KEY)들을 순회할 때 사용

반복 가능한 객체 순회 뿐만 아니라 객체 순회에도 사용가능, 객체의 속성값 순회에 더유용!

```javascript
for (variable in object) {
    // do something
}

const capitals = {
    korea: 'seoul',
    france: 'paris',
    USA: '워싱텅 디씨'
}
for (let capital in capitals) {
    console.log(capital) // korea, france, USA
}

딕셔너리는 for of 불가능
```



for .. of: 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용

객체 순회에 사용할 수 없으며, 객체의 속성값 순회에 유용한 구문은 for in!

```javascript
for (variable of iterables){
    //do something
}

const fruits = ['딸기','바나나','메론']
for (let fruit of fruits) {
    fruit = fruit + '!'
    console.log(fruit)
}

for (const fruit of fruits) {
    // 재할당 불가능
    console.log(fruit + '!')
}

이때 for of말고 for in을 사용하면 인덱스가 나옴
```



![image-20220426131842399](220425.assets/image-20220426131842399.png)
