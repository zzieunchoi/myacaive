# css 선택자

## 전체 선택자

전체 선택

```html
<head>
    <style>
        * {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>
        제목 테스트
    </h1>
    <p>
        본문 테스트
    </p>
</body>
```



## 태그 선택자

특정 종류의 모든 태그에 스타일 적용

```html
<head>
    <style>
        p {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>
        제목 테스트
    </h1>
    <p>
        본문 테스트
    </p>
</body>
```



## 아이디 선택자

문서 내의 아이디 속성값으로 접근

아이디명은 문서내에서 중복되지 않아야함

`#아이디명`

```html
<head>
    <style>
        #p2 {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>
        제목 테스트
    </h1>
    <p id="p2">
        본문 테스트
    </p>
</body>
```



## 클래스 선택자

문서 내의 클래스 속성값으로 접근

`.클래스명`

```html
<head>
    <style>
        .p2 {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>
        제목 테스트
    </h1>
    <p class="p2">
        본문 테스트
    </p>
</body>
```



## 속성 선택자

특정 속성을 가진 태그를 선택 가능

`선택자[속성=값]`

```html
<head>
    <style>
        input[type="text"] {
            background: black;
        }
    </style>
</head>
<body>
    <h1>
        제목 테스트
    </h1>
    <input type="text">
</body>
```



## 선택자 우선순위 

좀 더 좁은 범위로 지정된 선택자가 우선 적용됨

```html
<head>
    <style>
        p#p2 {
            color: blue;
        }
    </style>
</head>
<body>
    <p id="p2">
        본문 테스트
    </p>
</body>
```

p#p2 선택자: p태그이면서 아이디가 p2인 선택자



## 다중 선택자

여러개의 선택자 스타일 일괄 지정

```html
<head>
    <style>
        p, h1, div {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>
        제목 테스트
    </h1>
    <p>
        본문 테스트
    </p>
    <div >
        여기는 div
    </div>
</body>
```



## 자식/ 자손 선택자

* 자식 선택자
  * 특정 태그 바로 아래 선택
* 자손 선택자
  * 특정 태그의 자식, 손자.. 등 모든 후손 태그들 포함

```html
<head>
    <style>
        /*자식 선택자*/
        #first > div {
            color: red;
        }
        /*자손 선택자*/
        #first a {
            color: red;
        }
    </style>
</head>
<body>
    <div id="first">
        <div>
            first 아이디 태그 밑에 div
        </div>
        <span>
        	first 아이디 태그 밑에 span
            <div>
                <a href="">여기1</a>
            </div>
            <div>
                <a href="">여기2</a>
            </div>
        </span>
    </div>
</body>
```



## 형제(인접, 동위) 선택자

* 선택자a+선택자b
  * 선택자 a 바로 뒤에 위치하는 선택자 b
* 선택자 a~ 선택자b
  * 선택자 a 뒤에 위치하는 선택자 b 모두

```html
<head>
    <style>
        h1 + h2 {
            color:red;
        }
        h1 ~ h2 {
            background: orange;
        }
    </style>
</head>
<body>
    <h1>h1</h1>
    <h2>h2</h2>
    <h2>h2</h2>
    <h2>h2</h2>
</body>
```



## 가상 클래스 선택자

특정 상황에 따라 가상의 선택자 지정

* link 선택자
  * a 태그의 텍스트 링크 스타일 지정
  * `a:link {color: red;}`

* visited 선택자
  * 한번 이상 방문한 링크의 스타일 지정
  * `a: visited {color: red;}`
* active 선택자
  * 해당 태그의 링크를 클릭하는 순간 스타일 지정
  * `a:visited {color: red;}`
* hover 선택자
  * 해당 태그 위로 마우스 포인터를 올려놓았을 때 스타일
  * `a:hover {color: red;}`
* focus 선택자
  * 해당 태그에 포커스가 맞춰졌을 때 스타일
  * `input[type='text']:focus {color: red;}`
* root 선택자
  * html 문서에서 루트요소는 htm
* first-child 선택자
  * 첫번째 자식 태그
  * `li:first-child {color: red;}`

* last-child 선택자
  * 마지막 자식 태그
  * `li:last-child {color: red;}`
* nth-child(n)
  * 앞에서 n번째 있는 자식 태그
  * `li:nth-child(2n) {color: red;}`
* nth-last-child(n)
  * 뒤에서 n번째 있는 자식 태그
  * `li:nth-last-child(2n) {color: red;}`

* first-of-type
  * 동일한 타입의 요소 중 첫번째 자식 태그
* last-of-type
  * 동일한 타입의 요소 중 마지막 자식 태그
* nth-of-type(n)
  * 동일한 타입의 요소 중 앞에서 n번째 있는 자식 태그
* nth-last-of-type(n)
  * 동일한 타입의 요소 중 뒤에서 n번째 있는 자식 태그

* :not(선택자)
  * 부정 선택자
  * `div:not(.a) {color: red;}` div인데 class가 a가 아닌 태그에 적용