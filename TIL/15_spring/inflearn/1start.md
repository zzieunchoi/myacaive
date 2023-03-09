# 처음 시작하기

## 첫 화면 (정적)

src/main/resources/static/index.html 파일을 만들어서 시작하면 서버가 켜질 때 index.html을 최우선적으로 찾아서 파일 실행!



## 첫 화면 (동적)

src/main/hello.hellospring/controller/HelloController.java

```java
package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {
    @GetMapping("hello")
    public String hello(Model model){
        // data라는 값에 hello!를 부여함
        model.addAttribute("data", "hello!!");
        
        // hello.html을 찾아서 return 해줘라! - viewresolver가 화면을 찾아서 처리
        // resources:/templates/+{view_name}+.html이 열림!
        return "hello";
    }
}
```



src/main/resources/templates/hello.html

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Hello</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />

</head>
<body>
<p th:text="'안녕하세요 ' + ${data}"> 안녕하세요 .손님</p>
</body>
</html>
```



![image-20230308110326364](C:\Users\SSG\Desktop\myacaive\TIL\15_spring\inflearn\assets\image-20230308110326364.png)

## 커맨드에서 스프링 켜기

cd hello-spring

gradlew build

cd build\libs

java -jar hello-spring-0.0.1-SNAPSHOT.jar

=> 켜짐!



안되면 `gradlew clean build`하면 build라는 폴더가 사라지고 => 그 후에 다시 build
