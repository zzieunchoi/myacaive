# 레이아웃

## 박스 속성

웹 페이지의 레이아웃을 구성할 때 가장 중요한 스타일 속성

width, height, margin, padding, border, box-sizing

![image-20230102121025518](C:\Users\SSG\Desktop\myacaive\TIL\2_web\assets\image-20230102121025518.png)



* width, height
  * 박스 영역의 가로, 세로 크기를 지정
* margin, padding
  * 요소 영역 테두리 외곽 여백/ 요소 영역과 테두리 사이 여백

* border-width

  * thin, medium, thick, 크기값

* border-color

  * top, right, bottom, left 개별 지정 가능
  * none, hidden, dotted, dashed, solid, double .. 

* border-radius

  * top, right, bottom, left 개별 지정 가능

* box-shadow 속성

* box-sizing

  * content-box

    * 기본값으로 width, height 속성으로 나타낸 영역의 크기로 지정

    * 박스 넓이 = width+ (margin + border + padding) *2

    * 박스 높이 = height+ (margin + border + padding) *2

      `box-sizing: content-box`

  * border-box

    * width, height 속성이 테두리까지 포함한 영역의 크기로 지정

    * 박스 넓이 = width + margin *2

    * 박스 높이 = height + margin *2

      `box-sizing: border-box`

* display 속성
  * none: 화면에 보이지 않음
    * visibility와 차이
    * visibility : visible, hidden
    * display:none;과 는 다르게 hidden은 영역이 남아있음
  * block: 블록 태그로 지정
    * 블록태그는 혼자서 한 줄을 차지하는 태그
  * inline: 인라인 태그로 지정
    * 인라인 태그는 줄을 차지하지 않고, 한 줄에 여러 인라인 태그 표시
    * width, height는 적용되지 않으며 margin 속성은 좌우만 적용
  * inline-block: 인라인 -블록 태그로 지정
    * width, height는 모두 적용되며 margin 속성은 좌우상하 모두 적용

* opacity
  * 해당 태그의 투명도 조절 가능 0.0 ~ 1.0
* 위치 속성
  * 절대 위치 좌표
  * 상대 위치 좌표
  * position 속성
    * static: left, top 속성을 사용해서 태그의 위치를 지정할 수 없음
    * relative: 해당 태그가 나와야하는 위치를 기준으로 상대적인 위치
    * absolute: 부모 태그의 위치를 기준으로 left, top 속성을 이용해 원하는 위치에 배치
      * 자식에 absolute를 적용하려면 부모 태그는 position: relative 속성 지정
    * fixed: 절대 좌표 값을 사용해 고정 , 스크롤을 내려도 화면상의 절대값으로 고정
* z-index
  * 숫자가 클수록 화면의 가장 위에 표시

* overflow

  * 부모의 영역을 내부 태그가 벗어날 때 처리여부 지정

    ```html
    <head>
        <style>
          #con {
            position: relative;
            height: 120px;
            border: 1px solid black;
            overflow: scroll;
          }
          #box1 {
            position: absolute;
            background-color: red;
            width: 100px;
            height: 100px;
            z-index: 3;
          }
          #box2 {
            position: absolute;
            background-color: blue;
            left: 50px;
            top: 50px;
            width: 100px;
            height: 100px;
            z-index: 2;
          }
          #box3 {
            position: absolute;
            background-color: orange;
            left: 100px;
            top: 100px;
            width: 100px;
            height: 100px;
            z-index: 1;
          }
        </style>
    </head>
    
    <body>
        <h1>여기는 헤더</h1>
        <div id="con">
          <div id="box1"></div>
          <div id="box2"></div>
          <div id="box3"></div>
        </div>
    </body>
    ```

  * hidden

    * ![image-20230102122908248](C:\Users\SSG\Desktop\myacaive\TIL\2_web\assets\image-20230102122908248.png)

  * scroll

    * ![image-20230102122841045](C:\Users\SSG\Desktop\myacaive\TIL\2_web\assets\image-20230102122841045.png)

* float

  ```html
  <head>
  	<style>
      #box1 {
          background-color: red;
          color: white;
          width: 100px;
          height: 100px;
          text-align: center;
          line-height: 100px;
          float: left;
      }
  	</style>    
  </head>
  
  <body>
      <div id="box1">영역</div>
      <p>
        여기는 문단 여기는 문단 여기는 문단 여기는 문단 여기는 문단 여기는 문단
        여기는 문단 여기는 문단
      </p>
    </body>
  ```

  ![image-20230102123346167](C:\Users\SSG\Desktop\myacaive\TIL\2_web\assets\image-20230102123346167.png)

  영역이 div이지만 태그를 페이지 위에 떠 있도록 지정

  float 속성을 사용하면 그 주변으로 다른 태그가 감싸게 됨. 특정 태그를 나란히 표시할 때 사용