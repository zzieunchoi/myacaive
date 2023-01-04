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

  * 커맨드객체(ModelAttribute)

  * @PathVariable

  