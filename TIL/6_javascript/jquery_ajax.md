# ajax

특정 언어나 프로그램이 아닌 비동기로 서버와 통신하는 방식



json 형태로 통신

```javascript
<script>
    $(function () {
    	$("#btn").click(function () {
        	$.ajax({
            	url: "text.html",
            	cache: false,
            	dataType: "HTML",
            	success: function (data) {
                	var r = data.trim();
                	$("#div1").html(r);
            	},
            	error: function (res) {
                	console.log(res);
            	},
        	});
    	});
	});
</script>
```

<span style="color:red">서버에서 실행필요</span>



```javascript
<script>
      $(function () {
        $("#btn").click(function () {
          $.ajax({
            url: "ajax.html",
            data: { name: "test" },
            cache: false,
            dataType: "JSON",
            success: function (data) {
                // each로 json parsing 해서 data함!
              $.each(data, function (key, val) {
                $("div1").append(
                  "<tr><td>" +
                    val.no +
                    "</td><td>" +
                    val.title +
                    "</td><td>" +
                    val.name +
                    "</td><td>" +
                    val.date +
                    "</td>"
                );
              });
            },
            error: function (res) {
              console.log(res);
            },
          });
        });
      });
    </script>
```

```javascript
<body>
    <table id="div1" border="1" style="width: 500px; border-collapse: collapse">
      <tr>
        <td>번호</td>
        <td>제목</td>
        <td>작성자</td>
        <td>작성일</td>
      </tr>
    </table>
    <input type="button" value="ajax 불러오기" id="btn" />
</body>
```

