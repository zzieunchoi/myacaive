# 텍스트

## 폰트 사용하기

구글 웹폰트 사용

```html
<head>
    <style>
      @import url("https://fonts.googleapis.com/css?family=Nanum+Gothic");
      p {
        font-family: "Nanum Gothic";
      }
    </style>
</head>
<body>
    <p>
        하잉
    </p>
</body>
```



## 폰트 속성

* font-size
* font-style
  * normal
  * italic
  * olbique
* font-variant
  * normal
  * small-caps
* font-weight
  * normal
  * bold
  * lighter
  * bolder
  * 100~900 사이의 수

**한 줄로 작성 가능**

`font: noraml normal bold 20px/20px 'Nanum Gothic';`

* direction

  텍스트 방향 지정

  * ltr: 왼쪽에서 오른쪽
  * rtl: 오른쪽에서 왼쪽

* text alight

  * left
  * right
  * center
  * justify

* text-shadow

* text-overflow

  영역보다 텍스트의 길이가 길고 줄을 바꾸지 못하는 경우 지정

  * clip: 넘치는 텍스트 잘라냄
  * ellipsis: 넘치는 텍스트 대신 "... " 표시

* text-decoration

  * none
  * underline
  * overline
  * line-through

* text-indent

  텍스트 들여쓰기, 문단의 첫 글자를 얼마나 들여쓸지 지정

* text-transform

  텍스트 대소문자 변환

  * capitalize : 시작하는 첫번째 글자 대문자로
  * uppercase : 모든 글자 대문자로
  * lowercase : 모든 글자 소문자로
  * none : 변환 없음

* letter-spacing, word-spacing

  * letter: 글자와 글자 사이의 간격
  * word: 단어와 단어 사이의 간격

* line-height : 줄간격
* list-style-type: 대부분 none처리
* list-style-position

* empty-cells 

  * show: 빈셀 표시(기본값)
  * hide: 미표시

* text-align

  셀 안의 수평 정렬

  * left
  * center
  * right

* vertical-align

  셀 안의 수직 정렬

  * top
  * middle
  * bottom