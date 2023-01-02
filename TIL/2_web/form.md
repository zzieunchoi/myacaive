# form

## form 태그 속성

* action
  * 입력 데이터를 전송할 경로
* method
  * 입력 데이터 전송 방식
  * get/post
    * get: `index.html?id=a&pwd=b`
      * 데이터만 가져오는 간단한 데이터 처리 때는 get 방식 사용!
    * post: `index.html`
      * 개인 정보, 보안관련된 로그인 같은 상황에서는 무조건 post!
      * 파일 업로드 시
* name 
  * form의 이름
* target
  * action 속성에 지정한 경로를 현재창이 아닌 다른 대상으로 지정

```html
<body>
    <h1>form 입력방식</h1>
    <form action="index.html">
        <input type="text" name="id" />
        <input type="password" name="pwd" />
        <input type="submit" value="전송" />
    </form>
    
    <!--이렇게 get방식으로 보낼 수도 있음!-->
    <a href="index.html?a=b&c=d">이동</a>
</body>
```

