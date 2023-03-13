# 회원관리 예제 - 웹 MVC 개발

## 개념

* MVC 패턴
  * MODEL- VIEW- CONTROLLER 의 약자
  * MODEL
    * 어플리케이션이 무엇을 할건지 정의
    * DB와 연동하여 사용자가 입력한 데이터나 사용자에게 출력할 데이터를 다룸
  * VIEW
    * 사용자에게 시각적으로 보여주는 부분
  * CONTROLLER
    * MODEL이 데이터를 어떻게 처리할지 알려주는 역할
    * VIEW를 반환하기 위해 사용



## 개발

* 기능
  * 홈 화면 추가
  * 등록
  * 조회



HomeController

```java
package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

// 원래는 index.html을 가장 먼저 띄워주는데 다른 설정 사항(return)이 있다면 home.html을 가장 먼저 띄워줌!
@Controller
public class HomeController {
    @GetMapping("/")
    public String home() {
        return "home";
    }
}
```

home.html

회원가입으로 넘어가는 버튼과 회원 목록을 볼 수 있는 버튼을 만들어줌

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<body>

<div class="container">
    <div>
        <h1> Hello Spring</h1>
        <p>회원 기능</p>
        <p>
            <a href="/members/new">회원가입</a>
            <a href="/members">회원목록</a>
        </p>
    </div>
</div>
</body>
</html>
```

MemberController.java

```java
package hello.hellospring.controller;

import hello.hellospring.domain.Member;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class MemberController {
    private final MemberService memberService;

    @Autowired
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    // members/new라는 url로 들어오면 get방식으로 실행 - get은 주로 조회할 때
    @GetMapping("/members/new")
    public String createForm() {
        // 바로 1. members/createMemberForm으로 이동
        return "members/createMemberForm";
    }

    // 5. post방식으로 /members/new로 넘어감 - 데이터를 form 안에 넣어서 가져갈 때 
    @PostMapping("/members/new")
    // MemberForm이라는 인자를 가지고 create 메소드 실행 -> 
    public String create(MemberForm form) {
        Member member = new Member();
        
        // 멤버이름을 가져오고 join 시킴
        member.setName(form.getName());
        memberService.join(member);
        // 다시 첫 페이지로 redirect
        return "redirect:/";
    }
    
    @GetMapping("/members")
    public String List(Model model) {
        List<Member> members = memberService.findMembers();
        // model에 key가 members 로 members를 담아놓음
        model.addAttribute("members", members);
        return "members/memberList";
    }
}
```

templates/members/createMemberForm.html

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">

<body>
<!--2. 이름을 받을 수 있는 인풋 화면-->
<div class="container">
    <!--값을 입력-->
    <!--4. input에서 name이라는 값을 가지고 action url로 post 방식으로 넘어감-->
    <form action="/members/new" method="post">
        <div class="form-group">
            <label for="name">이름</label>
            <!--3. input의 name과 맞는 MemberForm에서 public String name에 해당 이름이 들어감-->
            <input type="text" id="name" name="name" placeholder="이름을 입력하세요">
        </div>
        <button type="submit">등록</button>
    </form>
</div>
</body>
</html>
```

MemberForm.java

```java
package hello.hellospring.controller;

public class MemberForm {
    private String name;

    public String getName() {
        return name;
    }
    
    // input을 통해 들어온 name이 private String name이 아닌 setName으로 인해 name이 들어옴
    public void setName(String name) {
        this.name = name;
    }
}
```

memberList.html

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">

<body>
<div class="container">
    <div>
        <table>
            <thead>
            <tr>
                <th>#</th>
                <th>이름</th>
            </tr>
            </thead>
            <tbody>
            <!--model안에 있는 members를 가져오는것!-->
            <tr th:each="member : ${members}">
                <td th:text="${member.id}"></td>
                <td th:text="${member.name}"></td>
            </tr>
            </tbody>
        </table>
    </div>
</div>
</body>
</html>
```

