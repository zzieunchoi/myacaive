# jquery

모든 브라우저에서 동작하는 자바스크립트 라이브러리



* 다운로드 or cdn 설치

  head 에 넣기!

  `<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>`



`$(document).ready(function () {})`

` $(function() {})` 똑같음!



## 선택자

* 전체 선택자

  `$("*")`

  ```javascript
  <script>
      $(document).ready(function () {
      	$("*").css("color", "red");
  	});
  </script>
  ```

* 요소 선택자

  `$(“element”)`

  ```javascript
  <script>
      $(document).ready(function () {
      	$("h1").css("color", "red");
  	});
  </script>
  ```

* 아이디 선택자

  `$(“#id”)`

  ```javascript
  <script>
      $(document).ready(function () {
      	$("#target").css("color", "red");
  	});
  </script>
  <body>
      <h1 id="target">안녕하세요</h1>
  </body>
  ```

* 클래스 선택자

  `$(“.class”)`

* 다중 선택자

  `$(“selector1, selector2...”)`

* 자식 선택자

  ```javascript
  <script>
      $(document).ready(function () {
      	$("div > ul").css("color", "red");
  	});
  </script>
  <body>
      <div>
      	<ul>
      		<li>사과</li>
  		</ul>
  	</div>
  </body>
  ```

* 후손 선택자

  ```javascript
  <script>
      $(document).ready(function () {
      	$("div li").css("color", "red");
  	});
  </script>
  <body>
      <div>
      	<ul>
      		<li>사과</li>
  		</ul>
  	</div>
  </body>
  ```

* 속성 선택자 (요소 속성 값으로 설정)

  ```javascript
   <script>
      $(document).ready(function () {
      	$("input[type='text']").val("안녕하세요");
   	});
  </script>
  
  <input type="text" />
  ```



## 배열

each()

객체나 배열의 요소를 확인하는 반복문

* $.each(object,function)

  ```javascript
  <script>
      $(document).ready(function () {
      	var arr = [1, 2, 3, 4, 5];
      	$.each(arr, function (idx, val) {
          	console.log(idx + " " + val);
      	});
  	});
  </script>
  /*
  0 1
  1 2
  2 3
  3 4
  4 5
  */
  ```

* $(셀렉터).each(function())

  ```javascript
  <script>
      $(document).ready(function () {
      	var arr = [1, 2, 3, 4, 5];
      	$("h1").each(function(idx, val) {
              console.log(idx+" "+val.innerHTML);
          })
  	});
  </script>
  <body>
      <h1>하나</h1>
      <h1>둘</h1>
  </body>
  
  /*
  0 하나
  1 둘
  */
  ```

  

## val()메서드

 * 파라미터가 있는 경우
   * value 속성 값 입력
 * 파라미터가 없는 경우
   * value 속성 값 리턴

 

## eq

선택한 요소의 인덱스 번호에 해당하는 요소를 찾음

없으면 null반환

```javascript
// div 태그 중 1번 인덱스의 값을 반환
console.log($("div").eq(1))
```

