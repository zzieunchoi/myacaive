# event

이벤트(**특정 이벤트가 발생하면, 할일을 등록한다)**

네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체



## Event Listener

마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생 가능

특정 메서드를 호출 하여 프로그래밍적으로도 만들어 낼 수 있음

```javascript
<head>
    <script>
    window.onload = function () {
    var btn = document.getElementById("btn");

    function whenClick() {
        alert("click!");
    }
    btn.onclick = whenClick;
	};
	</script>
</head>

<body>
    <input type="button" value="버튼" id="btn" />
</body>
```

btn: 객체 / onClick: 이벤트 속성/ whenClick: 이벤트 핸들러



## 이벤트 종류

* 마우스 이벤트

  * click

  * dbclick

  * mousedown

  * mouseup

  * mouseover

  * mouseout

  * mousemove

* 키보드이벤트
  * keydown
  * keyup
  * keypress
* 폼 이벤트
  * submit
  * reset
  * change
  * focus
  * blur

* 문서 이벤트
  * load: 문서를 모두 불러왔을 때
  * resize: 창의 크기 변경
  * scroll: 스크롤 되었을 때
  * unload: 페이지가 닫힐 때



## event handler 

* 인라인 방식

  ```javascript
  <head>
      <script>
      function message() {
      alert("인라인 방식");
  	}
  	</script>
  </head>
  <body>
      <input type="button" value="메시지" onclick="message()" />
  </body>
  ```

  

* addEventListener()

  지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정

  이벤트를 지원하는 모든 객체를 대상으로 지정 가능

  target.addEventLister(type, listener[, options])

  * type : 반응 할 이벤트 유형(대소문자 구문 문자열)
  * listener: 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
    *  eventListener 인터페이스 혹은 js function 객체여야함

  ```javascript
  <head>
      <script>
        window.onload = function () {
          var btn = document.getElementById("btn");
  
          var message = function () {
            alert("리스너 방식");
          };
          btn.addEventListener("click", message);
        };
      </script>
  </head>
  <body>
      <input type="button" value="메시지" id="btn" />
  </body>
  ```
  
  
  
  ```javascript
  const btn = document.querySelector('button')
  btn.addEventListener('click', function (event) {
      alert('버튼이 클릭되어있습니다.')
      console.log(event)
  })
  ```
  
  ```javascript
  <button onclick = "alertMessage()">나를 눌러봐!</button>
  const alertMessage = function () {
      alert('메롱!!!')
  }
  
  <button id = "my-button">나를 눌러봐!</button>
  const myButton = document.querySelector('#my-button')
  myButton.addEventListener('click', alertMessage)
  ```
  
  입력한 내용을 그대로 보여주기
  
  ```javascript
  <p id = "my-paragraph"></p>
  <form action = "#">
      <label for = "my-text-input">내용을 입력하세요.</label>
      <input id = "my-text-input" type = "text">
  </form>
  
  const myTextInput = document.querySelector('#my-text-input')
  
  const ifInputIsComing = function (event) {
      const myPtag = document.querySelector('#my-paragraph')
      myPtag.innerText = event.target.value
  }
  
  myTextInput.addEventListener('input', ifInputIsComing)
  
  // 이렇게 한번에 쓰는 것도 가능!
  myTextInput.addEventListener('input', function (event) {
      const myPtag = document.querySelector('#my-paragraph')
      myPtag.innerText = event.target.value
  })
  ```
  
  input 이벤트: 키보드를 치는 행위

  event.target  // `<input id = "my-text-input" type = "text">`
  
  
  
  입력한 내용 그대로 색깔 바꾸기
  
  ```javascript
  <h2>Change My color</h2>
  <label for = "change-color-input">원하는 색상을 영어로 입력하세요.</label>
  <input id = 'change-color-input'></input>
  <hr>
      
  const colorInput = document.querySelector('#change-color-input')
  const changeColor = function (event) {
      const h2Tag = document.querySelector('h2')
      h2Tag.style.color = event.target.value
  }
  colorInput.addEventListener('input',changeColor)
  ```
  
  

## event 취소

event.preventDefault()

현재 이벤트의 기본 동작 중단

HTML 요소의 기본 동작을 작동하지 않게 막음

이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소

체크 박스 못해!

```javascript
<input type = "checkbox" id = "my-checkbox">
    
const checkBox = document.querySelector('#my-checkbox')
checkBox.addEventListener('click', function (event) {
    event.preventDefault()
    console.log(event)
})
```

제출하는데 넘어가지 않아!

```javascript
<form action = "/articles/" id = "my-form">
    <input type = "text">
    <input type = "submit" value = "제출!">
</form>

const formTag = document.querySelector('#my-form')
formTag.addEventListener('submit', function (event) {
    console.log(event)
    event.preventDefault()
    event.target.reset()
})

// 이때 event.target은 그 함수의 주어 formTag임!
```

링크 눌러도 못들어가게

```javascript
<a href = "https://google.com/" target = "_blank" id = "my-link">Google</a>

const aTag = document.querySelector('#my-link')
aTag.addEventListener('click', function (event) {
    console.log(event)
    event.preventDefault()
})
```

스크롤 못해!

```javascript
document.addEventListener('scroll',function (event) {
    console.log(event)
    event.preventDefault()
})
```

취소할 수 없는 이벤트도 존재!

event.cancelable을 사용해 확인 가능



## 팝업 띄우기

```javascript
<script>
    window.onload = function() {
    	var btn = document.getElementById("popupBtn");
    
    	function popup() {
            window.open("pop.html", "popup", "height=500, width=500");
        }
    
    	btn.onclick = popup;
}
</script>
<button id="popupBtn">팝업</button>
```



## 실습

```javascript
<head>
    <script>
    window.onload = function () {
    	var btn1 = document.getElementById("btn1");
    	var btn2 = document.getElementById("btn2");

    	function btnClick1() {
       		console.log("클릭됨");
        	document.getElementById("cnt1").innerHTML =
            Number(document.getElementById("cnt1").innerHTML) + 1;
    	}

    	function btnClick2() {
        	console.log("클릭됨");
        	document.getElementById("cnt2").innerHTML =
            Number(document.getElementById("cnt2").innerHTML) + 1;
    	}

    	btn1.onclick = btnClick1;
    	btn2.onclick = btnClick2;
	};
	</script>
</head>
<body>
    <button id="btn1">버튼1</button>
	<button id="btn2">버튼2</button>
	<h1>버튼 1 클릭횟수: <span id="cnt1">0</span></h1>
    <h1>버튼 2 클릭횟수: <span id="cnt2">0</span></h1>
</body>
```

