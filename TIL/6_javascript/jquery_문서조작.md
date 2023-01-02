# 문서 조작

## 클래스 추가

```javascript
<style>
    .redColor {
        color:red;
    }
</style>
<script>
    $(document).ready(function() {
    $("h1").addClass("redColor");
});
</script>

<h1>하나</h1>
```



## 클래스 제거

```javascript
<style>
    .redColor {
        color:red;
    }
</style>
<script>
    $(document).ready(function() {
    $("h1").removeClass("redColor");
});
</script>

<h1 class="redColor">하나</h1>
```

* toggleClass("클래스명") : 있으면 제거, 없으면 추가



## 속성확인

```javascript
<script>
    $(document).ready(function() {
        console.log($("#img1").attr("src"))
});
</script>

<img id="img1" src="http://    ....">
```



## 속성추가

* .attr("속성명", "값");
* .attr("속성명", function(index, attr){});
* .attr(object);

```javascript
<script>
    $(document).ready(function() {
        $("#img1").attr("width", 200);
	});
</script>

<img id="img1" src="http://    ....">
```

```
배열로 줘도 가능
$("img1").attr({
 	width: 200,
 	height: 200
 })
```



## 속성 제거

removeAttr ; 속성 자체를 삭제

removeClass : 클래스 속성 중 선택적으로 제거

```javascript
<script>
    $(document).ready(function() {
        $("#img1").removeAttr("width");
	});
</script>

<img id="img1" width="200" src="http://    ....">
```



## 스타일 확인

.css("속성명")

```javascript
<script>
    $(document).ready(function() {
        console.log($("h1").css("color"));
	});
</script>
```



## 스타일 추가

.css("속성명", "값");

.css("속성명", function(index){});

.css(object);



## 객체내부 확인

.html();

.text();

```javascript
$(document).ready(function() {
    var a = $("h1").html();
    var b = $("h1").text();
})
```



## 객체 내부 추가

.html("내용")

.text("내용")

`$("div").text("<h1>하나</h1>")`



## 객체 제거

.remove(): 문서 객체를 제거

.empty(): 문서 객체의 후손을 모두 제거

```javascript
$(document).ready(function() {
    $("#first").remove();
})
```

```javascript
$("body").empty();
```



## 객체 생성

```javascript
$(document).ready(function() {
    $("<h1></h1>");
})
```



## 객체 삽입

* $(A).appendTo(b)
  * a를 b의 뒤로 추가
* $(A).append(b)
  * b를 a의 뒤에 추가
* $(A).prependTo(b)
  * a를 b의 앞에로 추가
* $(A).prepend(b)
  * b를 a의 앞에 추가
* $(A).insertAfter(b)
  * a를 b의 뒤에 추가
* $(A).insertBefore(b)
  * a를 b의 앞에 추가
* $(A).after(b)
  * b를 a의 뒤에 추가
* $(A).before(b)
  * b를 a의 앞에 추가

```javascript
<script>
    $(document).ready(function() {
    $("<h1>새로운</h1>").appendTo('#first');
});
</script>


<div id="first">하나</div>
```

