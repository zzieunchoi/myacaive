# jsp 스크립트 요소

## 스크립틀릿<% %>

jsp에서 자바코드를 실행할 때 사용하는 자바코드 블록

```jsp
<body>
<%
	int sum =0;
	for(int i =0; i<=10; i++){
		sum += i;
	}
%>
</body>
```



## 표현식<%= %>

어떤 값을 출력 결과에 포함시키고자 할 때 사용

숫자나 문자열, 변수 등의 값을 사용 가능

```jsp
<%@ page import ="java.util.*" %>
<%
	Date now = new Date();
%>

<body>
	<div>현재시간: <%= now %></div>
</body>
```



## 선언부

jsp 스크립틀릿이나 표현식에서 사용할 수 있는 메소드를 작성할 때 사용

```jsp
<%!
	public int multiply(int a, int b){
		int c= a*b;
		return c;
	}
%>

<body>
	10 * 25 = <%= multiply(10,25) %>
</body>
```

