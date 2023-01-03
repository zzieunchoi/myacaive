# servlet

spring에서 controller가 servlet

controller는 요청을 받는 역할



src/main/java - [오른쪽 마우스] - [new] - [others] - [servlet] 검색

```java
jsp/src/main/java/jsp/HelloServlet.java
package jsp;


import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/HelloServlet")
public class HelloServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public HelloServlet() {
        super();
    }

    @Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    	// request저장소에 저장
    	request.setAttribute("name", "최지은");
    	
    	//servlet hello.jsp로 forwarding
    	RequestDispatcher rd = request.getRequestDispatcher("/servlet/hello.jsp");
    	rd.forward(request, response);
	}
    
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}

```

```jsp
hello.jsp
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

${name }
</body>
</html>
```

```xml
web.xml
<web-app>
	<welcome-file-list>
        ...
	</welcome-file-list>
	<servlet>
        <servlet-name>helloServlet</servlet-name>
		<servlet-class>jsp.HelloServlet</servlet-class>
	</servlet>
  
    <servlet-mapping>
        <servlet-name>helloServlet</servlet-name>
        <url-pattern>/hello.ssg</url-pattern>
    </servlet-mapping>
</web-app>
```



HttpServlet을 상속받아 정의

web.xml에서 서블릿 설정, 매핑 설정



jsp 포워딩

printwriter 객체로 출력(jsp 없이)



web.xml 설정 없이 @webservlet

@WebServlet("/test.ssg")
