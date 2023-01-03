# JSTL

JSTL+ EL

JavaServer Pages Standard Tag Library 

라이브러리 이므로 다운 받아야함 

* [jstl 설치](https://mvnrepository.com/artifact/javax.servlet/jstl)
* web-inf 폴더 안에 복붙

`<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>`



| <c:set>       | 변수명에 값을 할당                                   |
| ------------- | ---------------------------------------------------- |
| <c:out>       | 값을 출력                                            |
| <c:if>        | 조건식에 해당하는 블럭과 사용될 scope설정            |
| <c:choose>    | 다른 언어의 switch와 비슷                            |
| <c:when>      | switch문의 case에 해당                               |
| <c:otherwise> | switch문의 default에 해당                            |
| <c:forEach>   | 다른언어의 loop문 items 속성에 배열을 할당할 수 있음 |



* c:set

  * var = 변수명
  * value= 할당할 값

  ```jsp
  <c:set var="tel" value="010" ></c:set>
  
  <body>
      ${tel}
  </body>
  ```

* c:out

  * value=출력할 값

  ```jsp
  <c:out value="${tel}" /><br>
  ```

* c:if

  ```jsp
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
  <c:set var="tel" value="010" ></c:set>
  
  <body>
  	<c:if test="${param.id == 'admin' }">
  	관리자님 안녕하세요
  	</c:if>
  	<c:if test="${param.id != 'admin' }">
  	관리자만 접속 가능합니다.
  	</c:if>
  </body>
  ```

  c:if는 else가 안되기 때문에 if(조건)을 모두 써야함 ㅠㅠ

  ```jsp
  // 로그인 시
  <c:if test="${!empty member} }">
      ${member.name}님, 안녕하세요
  </c:if>
  <c:if test="${empty member} }">
      로그인해주세요.
  </c:if>
  ```

* c:forEach

  * var=for문안에서 쓸 이름
  * items= for문 돌 객체 이름
    * 이때 items="${}"에
    * request.setAttribute("memberlist", list)에서 memberlist를 담아야함!
    * setAttribute에 담긴 이름을 el로 적어야함

  ```jsp
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
  <%@ page import="java.util.*"%>
  <body>
  	<%
  	// MemberVo객체를 arraylist 객체에 담고
  	MemberVo vo = new MemberVo();
  	List<MemberVo> list = new ArrayList<MemberVo>();
  	vo.setId("son");
  	vo.setName("손종례");
  	list.add(vo);
  
  	vo = new MemberVo();
  	vo.setId("choi");
  	vo.setName("최지은");
  	list.add(vo);
  
  	vo = new MemberVo();
  	vo.setId("kwon");
  	vo.setName("권도건");
  	list.add(vo);
  	
  	// arraylist 객체를 request 객체에 담음
  	request.setAttribute("memberlist", list);
  	%>
  	<jsp:forward page="list.jsp"/>
  
  </body>
  ```

  ```jsp
  //list.jsp
  <%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
  
  <body>
  	<c:forEach var="vo" items="${ memberlist}">
  		${vo.id } ${vo.name }<br>
  	</c:forEach>
  </body>
  ```

  **/el/list.jsp url로 가면 안나오는 이유**

  list.jsp는 memberlist가 비어있음 따라서 list.jsp에서는 for를 돌것이 없는 거임!

  만약 forward가 아니고 redirect였다면 새로운 요청이 2번 들어가기 때문에 안될 것임

  그러나 forward이므로 한번의 요청만 들어가서 list.jsp에 넘긴거임 list.jsp가 아닌 jstl.jsp에서 출력되는 것임

  

  

