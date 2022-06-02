------

- Trouble Shooting
  - 코드를 보고 결과값 예측
  - 어떤 에러가 날것인지
  - 어떻게하면 에러를 고칠 수 있는지

------

1. Vue의 가장 큰 개발 핵심은?

- SFC ( Single File Component )
  - 하나의 컴포넌트는 .vue 확장자를 가진 하나의 파일 안에서 작성되는 코드의 결과물
  - 화면의 특정 영역에 대한 HTML, CSS, JavaScript 코드를 하나의 파일(.vue) 에서 관리
  - 즉, .vue 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식

------

2. Vue의 특징

- 현대적인 Tool과 다양한 라이브러리를 통해 SPA를 완벽하게 지원
  - SPA ( Single Page Application )
  - 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 App
- SSR & CSR 모두 사용 가능
- Component기반 UI & **프론트엔드 기반**
- CDN 방식 또는 npm을 통한 설치로 사용 가능

------

3. HTML 요소를 다룰 때

- v-bind ( O )
- v-html ( X ) ⇒ XSS 공격에 취약!

------

4. v-on & v-bind의 축약

- v - on
  - 약어 :  @
  - v-on:click  →  @click
- v - bind
  - 약어 : : (콜론)
  - v-bind:href → :href

------

5. img 속성 값중 src속성을 사용하고 싶은 경우

```html
<!-- 둘 다 사용 가능 -->
<img :src= "url">
<img v-bind:src: "url">
```

------

6. vue router 동적인자 사용법

```html
<router-link :to="{ name: 'nameValue'}">path이름</router-link>
```

------

7. Lifecycle Hooks 종류

- created
- mounted
- destroyed

------

8. v-for 사용 방법

- item in items 구문 사용
- item 위치의 변수를 각 요소에서 사용할 수 있음
  - 객체의 경우는  key
- v-for 사용 시 반드시 key  속성을 각 요소에 작성
- v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음
  - 단, 가능하면 동시에 사용하지 말 것!

------

9. vue 실행시 명령어

```bash
$ npm run serve
```

------

10. 양 방향 통신을 하는 방법

- v-model
  - HTML form 요소의 값과 data를 양방향 바인딩

------

11. Vuex의 가장 큰 특징

- 모든 컴포넌트의 데이터를 전역 저장소에 저장하는 것

------

12. Vuex에서 유일하게 State를 조작할 수 있는 방법

- mutations

------

13. Vue Router에서 History Mode의 특징

- HTML History API를 사용해서  router를 구현한 것
- 페이지를 로드하지 않고 URL을 탐색할 수 있음
  - SPA의 단점 중 하나인 "URL이 변경되지 않는다." 를 해결

------

14. Vue.js의 설계 패턴은

- MVVM Pattern
  - Model
  - View
  - View Model

------

15. 컴포넌트는 중첩으로 구현가능한가?

- 가능!

------

16. v-if  &  v-show의 차이점을 서술하시오 ( 서술형 문제 )

- v-if
  - 전달인자가 false인 경우 렌더링이 되지않음
  - 렌더링 자체가 안되기 때문에 렌더링 비용이 낮음
  - 하지만 자주 변경되는 요소의 경우 비용이 증가할 수 있음
- v-show
  - CSS display 속성을 hidden으로 만들어 토글
  - 실제로 렌더링은 되지만 눈에 보이지 않는 것이기 때문에 한 번만 렌더링 되는 경우 v-if에 비해 렌더링 비용이 높음
  - 하지만 자주 변경되는 요소라면 한번 렌더링 된 이후 보여주는지에 대한 여부만 판단하므로 토글비용이 v-if보다 적다

------

17. computed & methods의 차이점을 서술하시오 ( 서술형 문제 )

- computed
  - 종속 대상을 따라 저장됨
  - 즉 종속 대상이 변경되지 않는 한 computed에 작성된 함수를 여러번 호출해도 다시 계산하지 않고 계산되어 있는 결과를 반환
- methods
  - 저장되지않고 methods 호출시 렌더링을 다시 할 때마다 항상 함수를 실행한다.

------

18. Babel을 설명하시오 ( 서술형 문제 ) 한글로 바벨 쓰지말것!!

- Babel 이란

  - 자바스크립트의 이전 버전으로 번역 / 변환해주는 도구
  - 그러므로 최신 문법을 사용해도 이전 브라우저 혹은 환경에서 동작할 수 있다.

  ```jsx
  // 최신 문법 스크립트 : Babel Input
  [1, 2, 3].map((n) => n+1);
  
  // 구 버전 문법 변환 : Babel Output 
  [1, 2, 3].map(function(n) {
  	return n + 1 ;
  });
  ```

------

19. 프록시를 설정하기 위해서 this를 사용해야한다.