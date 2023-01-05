# controller

- 매핑(url - 메서드)

`get 방식 `				`post 방식`

/test/login.ssg -> /test/process.ssg

get 방식: @GetMapping("/test/get.ssg")

post 방식: @PostMapping("/test/process.ssg")

get방식 post 방식 모두 혼용할 수 있는 것은 @RequestMapping

그렇디만 request mapping은 value와 method를 모두 지정해줘야하기 때문에 불편

=> getmapping, postmapping을 쓰세요!



```java
MvcConfig.java
package chap4;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
// mvc 활성화 시키는 역할
@EnableWebMvc
@ComponentScan(basePackages = {"chap4"})
public class MvcConfig implements WebMvcConfigurer{
	@Override
	public void configureViewResolvers(ViewResolverRegistry registry) {
		registry.jsp("/WEB-INF/views/", ".jsp");
	}
}
```

```java
TestController.java
package chap4;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
// /test가 계속 반복될 때는 @RequestMapping("/test")
public class TestController {
	// get 방식
    // @GetMapping("/get.ssg") 이렇게 반복된 걸 빼고 주소를 넣어주면 됨!
	@GetMapping("/test/get.ssg")
	public String test() {
		// view 
		return "test/get";
	}
	
     // @GetMapping("/login.ssg")
	@GetMapping("/test/login.ssg")
	public String login() {
		return "test/login";
	}
    
     // @PostMapping("/process.ssg")
	@PostMapping("/test/process.ssg")
	public String process() {
//		jsp경로 return  prefix ~ [] ~ suffix 사이의 값
//		redirect 하려면 redirect:
        // 하도 순식간에 지나가서 프린트 !
		System.out.println("여기는 프로세스");
		return "redirect:login.ssg";
	}
}
```

* 이때 login()의 경우 return 이 필요없는 public void login() {}으로 할 수 있는데 
  * 이때처럼 리턴이 없는 경우 url 경로 그대로 jsp로 포워딩 됨
  * /text/login으로 return과 똑같음

```jsp
views/test/get.jsp
<body>
test/get
</body>

views/test/login.jsp
<body>
	<form action="process.ssg" method="post">
		<table>
			<tr>
				<td>아이디</td>
				<td><input type="text" name="id"></td>
			</tr>
			<tr>
				<td>비밀번호</td>
				<td><input type="password" name="pwd"></td>
			</tr>
			<tr>
				<td colspan="2" style="text-align: center;"><input
					type="submit" value="로구인"></td>
			</tr>
		</table>
	</form>
</body>
```



* 파라미터를 받는 방법(***중요***)

  * request 객체를 통해서 받을 수 있음(request.getparameter(..))

    HttpServletRequest
  
    getParameter()
  
    getParameterValues()
  
    ```java
    @GetMapping("/param.ssg")
    public String param(HttpServletRequest req) {
        String id = req.getParameter("id");
        System.out.println("id : " + id);
        
        //서블릿 처리
        PrintWriter out = res.getWriter();
        out.print("id는 " + id);
        
        return null;
    }
    ```

  * @RequestParam
  
    * 개별 처리 (하나씩)
    * name 속성: 파라미터명 지정
    * required = "false"를 하면 꼭 지정한 name이 아니더라도 에러가 나지 않음
    * 그러나 기본 자료형은 required="false"로 하면 안됨 => defaultValue를 지정해야함
  
    ```java
    @GetMapping("/param2.ssg")
    public void param2(@RequestParam(name="idx") String id) {
        System.out.println("id: "+ id);
    }
    ```
  
  * 커맨드객체(ModelAttribute)
  
    알아서 객체에 만들어줌!
  
    ```java
    package chap4;
    
    import lombok.Data;
    
    @Data
    public class MemberVo {
    	private String id;
    	private int number;
    	private String pwd;
    	private String name;
    }
    ```
  
    ```java
    @GetMapping("/param3.ssg")
    public void param3(MemberVo vo) {
        System.out.println("id : " + vo.getId());
        System.out.println("number : "+ vo.getNumber());
        System.out.println("name : " + vo.getName());
    }
    ```
  
    원래는 나중에 jsp에서 보여주려면
  
    ```java
    @GetMapping("/param3.ssg")
    public void param3(HttpServletRequest req, MemberVo vo) {
        System.out.println("id : " + vo.getId());
        System.out.println("number : "+ vo.getNumber());
        System.out.println("name : " + vo.getName());
        req.setAttribute("vo", vo);
    }
    ```
  
    ```jsp
    <body>
    	아이디 : ${vo.id}<br>
    	number: ${vo.number}<br>
    	name: ${vo.name }
    </body>
    ```
  
    이렇게 해야하는데 커맨드 객체는 자동으로 할당해줌
  
    이때 불러올 때는 클래스 이름에서 첫 글자만 소문자로 바꿔준 이름으로 담아줌!
  
    ```jsp
    <body>
        아이디 : ${requestScope.memberVo.id}
    </body>
    ```
  
    * 객체 이름을 따로 만들고 싶지 않다면
  
      ```java
      @GetMapping("/param3_1.ssg")
      	public void param3_1(HttpServletRequest req, 
      			@RequestParam Map param) {
      		System.out.println("id : " + param.get("id"));
      		System.out.println("number : " + param.get("number"));
      		System.out.println("name : " + param.get("name"));	
          }
      ```
  
    * 이름을 변경하고 싶다면
  
      ```java
      @GetMapping("/param3.ssg")
      public void param3(@ModelAttribute("vo") MemberVo vo) {
          System.out.println("id : " + vo.getId());
          System.out.println("number : "+ vo.getNumber());
          System.out.println("name : " + vo.getName());
      }
      ```
  
      ```jsp
      <body>
          아이디 : ${vo.id} <br>
      	number: ${vo.number}<br>
      	name: ${vo.name }
      </body>
      ```
  
  * @PathVariable
  
    * uri 대신 경로가 변수되는 것
    * ex) 공지 사항 게시판 1페이지 : /board/notice/1
  
    ```java
    @GetMapping("/param4/{id}/{page}")
    public void param4(@PathVariable String id,
                       @PathVariable int page) {
        System.out.println("id :"+ id);
        System.out.println(("page : "+page));
    }
    ```



* 데이터를 뷰에서 처리하기 위한 방법

  * request 객체에 저장

    ```java
    @GetMapping("/res.ssg")
    public String res(@RequestParam(required=false) String type,
                      HttpServletRequest req) {
        String message = "" ;
        if ( "1".equals(type)) {
            message = "정상적으로 저장되었습니다.";
        } else {
            message = "저장 실패";
        }
        req.setAttribute("msg", message);
        return "test/response";
    }
    ```

  * session 객체에 저장

    ```java
    @GetMapping("/res.ssg")
    public String res(@RequestParam(required=false) String type,
                      HttpServletRequest req,
                      HttpSession sess) {
        String message = "" ;
        if ( "1".equals(type)) {
            message = "정상적으로 저장되었습니다.";
        } else {
            message = "저장 실패";
        }
        //	HttpSession sess = req.getSession();
        sess.setAttribute("msg", message);
    
        return "test/response";
    }
    ```

  * 모델에 저장

    ```java
    @GetMapping("/res.ssg")
    public String res(@RequestParam(required=false) String type,
                      HttpServletRequest req,
                      Model model) {
        String message = "" ;
        if ( "1".equals(type)) {
            message = "정상적으로 저장되었습니다.";
        } else {
            message = "저장 실패";
        }
        // model에 저장
        model.addAttribute("id", "hong");
        return "test/response";
    }
    ```



* 리턴 종류

  * String리턴: ViewResolver에 prefix와 suffix 사이

  * void: uri(경로)와 동일한 jsp 위치

  * ModelAndView

    * ```java
      @GetMapping("/mav.ssg")
      public ModelAndView mav() {
          ModelAndView mav = new ModelAndView();
          mav.addObject("msg", "안녕하세요");
          mav.setViewName("test/response");
          return mav;
      }
      ```

    * ```jsp
      <body>
          ${msg}
      </body>
      ```

      

