# jquery 이벤트

* 인라인

  ```javascript
  <script>
      function clickMessage(txt) {
      	alert(txt);
  	}
  </script>
  
  <div onclick="clickMessage("하나");">하나</div>
  ```

* 이벤트 핸들러 연결

  ```java
  <script>
      $(function() {
          $("#div1").click(function() {
              alert($(this).text());
          })
  	});
  </script>
  
  <div id="div1">하나</div>



## 이벤트 전달 제거

.preventDefault(): 기본 이벤트 제거

.stopPropagation(): 이벤트 전달 제거

```javascript
<script>
    $(document).ready(function () {
    	$("#a1").click(function(event) {
            alert("a태그");
            event.preventDefault();
            event.stopPropagation();
        });
    	$("#div1").click(function() {
            alert("div태그");
        });
});

<div id="div1"><a href="http://www.naver.com" id="a1">하나</a></div>
```

