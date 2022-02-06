# font awesome과 bootstrap 쓰기



## bootstrap과 font awesome을 쓰기 전에

bootstrap에는 웹사이트를 쉽게 만들 수 있게 도와주는 HTML, CSS, JS프레임워크이다.

원하는 기능이 있을 때 붓 스트랩 들어가서 도움을 받을 수 있음!



font awesome은 다양한 아이콘을 쓸 수 있음. 원하는 아이콘을 쓰기 위해서는 폰트 어썸을 들어가면 됨!



사용하기 위해서는 <head>에

bootstrap 사용 시

``` html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
```

을 붙이고

font awesome 사용시

``` html
<script src="https://kit.fontawesome.com/29a158db2d.js" crossorigin="anonymous"></script>
```

붙이면 됨. 중간에 29a~는 각자가 font awesome에서 발급받는 개인 코드!



오늘은 카드를 만들어 볼거에요~

그렇다면 bootstrap - docs 에 card를 검색해서 원하는 카드 이미지를 선택하고 코드를 복사하면 됨!

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
  </div>
</div>
```

이거를 복사해서 body에 붙여넣기!



그리고 원하는 이미지를

```html
<img src="./1.png" class="card-img-top" alt="내남자의비즈니스">
```

이렇게 첨부!



``` html
<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
```

여기에는 원하는 텍스트 작성 가능!



### row

 행 별로 정렬할 거기 때문에 class에 row를 넣어줘야함

``` html
<div class = "row">
```





### flex

: 레이아웃, 할당, 그리드 혈의 사이즈 조정, 네비게이션, 구성 요소 등을 쉽게 조절할 수 있는 방법!

bootstrap에 flex 검색하면 나옴

d-flex를 사용하면 레이아웃 편하게 조정 가능

```html
<div class="d-flex justify-content-start">...</div>   <!--맨처음부터 정렬 -->
<div class="d-flex justify-content-end">...</div>     <!--맨끝에 쪽에 정렬 -->
<div class="d-flex justify-content-center">...</div>  <!--중간에 쏠리게 정렬 -->
<div class="d-flex justify-content-between">...</div> <!--처음, 중간, 끝에 정렬 -->
<div class="d-flex justify-content-around">...</div>  
<!--세가지 카드를 넣는다면 12칸을 3개로 나눈 후 그 중간에 정렬 -->
<div class="d-flex justify-content-evenly">...</div>  <!--띄어있는 칸이 똑같게끔 정렬 -->
```

```html
<!--행 으로 정렬하겠다는 row class 뒤에 d-flex~ 작성 -->
<div class = "row d-flex justify-content-center">
```

** class가 두 개 있을 경우 두개 다 참조 가능



### col-n

웹페이지에서는 한 줄을 12개의 칸으로 봄!

|      |      |      |      |      |      |      |      |      |      |      |      |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      |      |      |      |      |      |      |      |      |      |      |

하나의 칸에 한장의 사진씩 넣으면 된다고 생각!

따라서 내가 카드를 12장을 넣고 싶다 = col을 1개씩 차지

내가 카드 사진을 5장 넣고 싶다 = col을 2개씩 차지 -- 나머지 2개는 버리는 자리

``` html
<div class="card col-2">
    
</div>
```

이렇게 작성하고 안에 넣고 싶은 카드를 작성하면 됨



### font awesome

원하는 이모티콘 넣기!

만약 ❤️ 안녕하세요 지은입니다. 라고 작성하고 싶다면

``` html
<p>
    안녕하세요 지은입니다.
</p>
```

'안녕~' 앞에 커서를 넣은 후

font awesome에 원하는 이모티콘을 클릭 한 후 사이트 안에 들어가서 <i ~>를 복사

나는 하트를 하고 싶으니까

``` html
<i class = "fas fa-heart"></i>
```

를 복사한 다음에 붙여넣기!



색깔 지정 및 다른 스타일링도 가능!

```html
<i class="fas fa-heart" style="color: red">
```

이렇게 색깔을 지정해주면 이모티콘의 색상 및 스타일링 변경 가능!



# 최종본

``` html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://kit.fontawesome.com/29a158db2d.js" crossorigin="anonymous"></script>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <link rel = "stylesheet" href="0206.css">
  <title>sunday morning</title>
</head>
<body>
  <div class = "container">
    <div class = "row d-flex justify-content-center">
      <div class="card col-2">
        <img src="./1.jfif" class="card-img-top" alt="진">
        <div class="card-body">
          <p class="card-text"><i class="fas fa-heart" style="color: red"></i>안녕하세요. 진입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./2.jfif" class="card-img-top" alt="뷔">
        <div class="card-body">
          <p class="card-text"><i class="far fa-heart" style="color: blue"></i>안녕하세요. 뷔입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./3.jfif" class="card-img-top" alt="구교환">
        <div class="card-body">
          <p class="card-text">안녕하세요. 구교환입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./4.png" class="card-img-top" alt="현빈">
        <div class="card-body">
          <p class="card-text">안녕하세요. 현빈입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./5.jpg" class="card-img-top" alt="차은우">
        <div class="card-body">
          <p class="card-text">안녕하세요. 차은우입니다.</p>
        </div>
      </div>
    </div>

        <!-- 2 -->
    <div class = "row d-flex justify-content-between mt-5">
      <div class="card col-2">
        <img src="./1.jfif" class="card-img-top" alt="진">
        <div class="card-body">
          <p class="card-text">안녕하세요. 진입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./2.jfif" class="card-img-top" alt="뷔">
        <div class="card-body">
          <p class="card-text"><i class="fas fa-heart"  style="color: red"></i>안녕하세요. 뷔입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./3.jfif" class="card-img-top" alt="구교환">
        <div class="card-body">
          <p class="card-text">안녕하세요. 구교환입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./4.png" class="card-img-top" alt="현빈">
        <div class="card-body">
          <p class="card-text">안녕하세요. 현빈입니다</p>
        </div>
      </div>
      <div class="card col-2">
        <img src="./5.jpg" class="card-img-top" alt="차은우">
        <div class="card-body">
          <p class="card-text">안녕하세요. 차은우입니다.</p>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
```

