# css

스타일 시트: 속성을 이용해서 웹 문서의 디자인적인 요소를 제어하는 기능

웹 문서의 내용과 디자인을 분리 (내용 - html/ 디자인 - css)



* `<head>`안에 css 넣기

  ```html
  <head>
      <style>
      	h1 {
      		color: red;
      	}
      </style>
  </head>
  ```

* 외부 css 파일에서 가져오기

  ```html
  <head>
      <link href="test.css" rel="stylesheet" type="text/css">
  </head>
  ```

  

## 상속

부모태그의 속성을 자식태그 속성으로 전달되는 것을 상속

```html
<head>
   <style>
      body {
        background-color: black;
        color: white;
      }
      ul {
        color: red;
      }
    </style>
</head>
<body>
    <h1>테스트</h1>
    <p>본문 테스트</p>
    <ul>
      <li>목록1</li>
      <li>목록2</li>
    </ul>
</body>
```

![image-20230102104210484](C:\Users\SSG\Desktop\myacaive\TIL\2_web\assets\image-20230102104210484.png)

ul 태그에다 red로 해놨어도 li에서도 속성이 상속됨



## important

```html
<style>
    p {
        color: red;
    }
    p {
        color: blue !important;
    }
</style>
```

red, blue 둘다 값이 있지만 important가 먼저 우선순위!

![image-20230102104405839](C:\Users\SSG\Desktop\myacaive\TIL\2_web\assets\image-20230102104405839.png)