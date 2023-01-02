# background image

1. 백그라운드 이미지 속성

   - 배경이미지 지정

     ```html
     <head>
         <style>
             body {
                 background-image: url("bg-img1.png");
             }
         </style>
     </head>
     ```

     

2. background-repeat 속성

   * repeat: 태그에 가득 찰 때까지 가로, 세로 반복

   * repeat-x : 태그의 너비와 같아질 때까지 가로 반복

   * repeat-y: 태그의 높이와 같아질때까지 세로 반복

   * no-repeat

     ```html
     body {
     	background-image: url("bg-img1.png");
     	background-repeat: repeat-y;
     }
     ```

     

3. background-position 속성

   ```html
   <style>
       div {
           ..
           background-position: right bottom;
       }
   </style>
   ```



4. background-attachment 속성

   스크롤을 내려도 배경 이미지를 고정 가능

   ```html
   <style>
       body {
           background-attachment: fixed;
       }
   </style>
   ```

   

**위의 속성들을 하나의 속성으로 줄여서 사용 가능**

`background: url("html5.png") no-repeat right bottom fixed`