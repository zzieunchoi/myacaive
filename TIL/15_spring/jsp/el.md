## EL

expression language

저장소에 있는 값을 출력

간결하게 사용 가능

null처리 불필요

* 값 일때

  ```jsp
  //index.jsp
  <% 
  request.setAttribute("nickname", "hong");
  %>
  
  <body>
  닉네임: ${requestScope.nickname }, ${nickname}
  </body>
  
  // 닉네임: 홍홍, 홍홍
  ```

* 객체 시

  ```java
  package jsp.member;
  
  public class MemberVo {
  	private String id;
  	private String name;
  	private String email;
  	public String getId() {
  		return id;
  	}
  	public void setId(String id) {
  		this.id = id;
  	}
  	public String getName() {
  		return name;
  	}
  	
  	public String getName2() {
  		return name+"님";
  	}
  	public void setName(String name) {
  		this.name = name;
  	}
  	public String getEmail() {
  		return email;
  	}
  	public void setEmail(String email) {
  		this.email = email;
  	}
  
  }
  ```

  ```jsp
  <% 
  request.setAttribute("nickname", "홍홍");
  MemberVo vo = new MemberVo();
  vo.setId("hong");
  vo.setName("홍길동");
  vo.setEmail("zzieun_choi@naver.com");
  
  // 세션에저장
  session.setAttribute("member", vo);
  
  // 이렇게 해도 되지만 너무 귀찮아!
  //MemberVo m = (MemberVo) session.getAttribute("member");
  //m.getId();
  
  %>
  
  <body>
  	닉네임: ${requestScope.nickname } <br>
      <!--바로 객체.속성으로 출력 가능-->
  	세션에 있는 값 :  ${member.id}, ${member.name} , ${member.email }
  </body>
  ```

  이 때 출력되는 것은 getter메소드를 출력하는 것임

  ```java
  // MemberVo.java에
  public String getName2() {
      return name+"님";
  }
  ```

  이라고 추가해서

  ```jsp
  <body>
  	${member.name2}
  </body> 
  ```

  라고 하면 홍길동님이라고 출력됨!

  

* param 객체

  `http://localhost:8081/jsp/el/index.jsp?no=10`

  no=??라고 파라미터를 보내면

  ```jsp
  파라미터:  ${param.no }
  <!-- 10이 출력 -->
  ```

  



