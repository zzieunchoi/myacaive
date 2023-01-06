# db 연결

## spring + mybatis

- 의존 모듈(oracle, connection pool, mybatis, spring-mybatis, spring jdbc, spring tx(transaction))을 mvnrepository에서 maven 복사해서
- pom.xml에 dependency 추가!



흐름: 브라우저 -> controller -> 서비스 -> DAO -> **Mybatis** -> DB



* connection pool : db connection 객체를 미리 만들어놓음 -> 담아놓고 나중에 필요할 때 꺼내 씀!
  * 속도 개선을 위해 !
  * 예시) DBCP(db connection pool), HikariCP



* mybatis 버전!
  * 3.0전과 후로 차이가 있음!
  
  * 예전: SqlSessionTemplate 객체를 주입
  
    //chap5/MvcConfig.java
  
    ```java
    package chap5;
    
    import java.io.IOException;
    
    import org.apache.ibatis.session.SqlSessionFactory;
    import org.mybatis.spring.SqlSessionFactoryBean;
    import org.mybatis.spring.SqlSessionTemplate;
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.ComponentScan;
    import org.springframework.context.annotation.Configuration;
    import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
    import org.springframework.web.servlet.config.annotation.DefaultServletHandlerConfigurer;
    import org.springframework.web.servlet.config.annotation.EnableWebMvc;
    import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
    import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    
    @Configuration
    // mvc 활성화 시키는 역할
    @EnableWebMvc
    @ComponentScan(basePackages = {"chap5"})
    public class MvcConfig implements WebMvcConfigurer{
    	
    	@Override
    	public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
    		configurer.enable();
    	}
    	
    	// view resolver 설정
    	@Override
    	public void configureViewResolvers(ViewResolverRegistry registry) {
    		registry.jsp("/WEB-INF/views/", ".jsp");
    	}
    	
    	// HikariCP의 설정
    	@Bean
    	public HikariConfig hikariConfig() {
    		HikariConfig hikariConfig = new HikariConfig();
    		hikariConfig.setDriverClassName("oracle.jdbc.driver.OracleDriver");
    		hikariConfig.setJdbcUrl("jdbc:oracle:thin:@localhost:1521:xe");
    		hikariConfig.setUsername("testuser");
    		hikariConfig.setPassword("test1234");
    		return hikariConfig;
    	}
    	
    	//Datasource 객체
    	@Bean
    	public HikariDataSource dataSource() {
    		HikariDataSource ds = new HikariDataSource(hikariConfig());
    		return ds;
    	}
    	
    	// SqlSessionFactory 객체
    	@Bean
    	public SqlSessionFactory sqlSessionFactory() throws Exception {
    		SqlSessionFactoryBean ssf = new SqlSessionFactoryBean();
    		ssf.setDataSource(dataSource());
    		
    		//SqlSesstionTemplate 방식으로 하는 경우 매퍼(mapper) 파일의 위치 지정
    		PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
    		ssf.setMapperLocations(resolver.getResources("")); // mapper 파일 경로 지정
    		
    		return ssf.getObject();	
    	}
    	
    	//DAO에서 주입받을 객체
    	@Bean
    	public SqlSessionTemplate sqlSessionTemplate() throws Exception {
    		SqlSessionTemplate sst = new SqlSessionTemplate((sqlSessionFactory()));
    		return sst;
        }
    }
    ```
  
    // src/main/resources/mapper/emp.xml
  
    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="">
    
    </mapper>
    ```
  
  * 이후: 매퍼 인터페이스 방식(작업량도 적고 편리)
  
    jdbc, db이후의 작업을 개발자가 할 필요없고 자동적으로 해줌!(로직에만 집중해!)
    
    DAO 가 필요없어지고 대신, 인터페이스를 만들음!
    
    * 매퍼 인터페이스 생성
    * XML이 인터페이스와 동일한 패키지 내에 있어야함
      * xml은 src/main/resources 폴더 안에 넣고 이름만 동일하면 됨!
    * 인터페이스명과 XML 이름이 동일해야함
    * XML의 ID와 동일한 이름으로 추상메서드 정의
    
    ```xml
    <!--chap5/EmpMapper.xml-->
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="chap5.EmpMapper">
    	<select id="all" resultType="chap5.EmpVO">
    		SELECT * FROM emp
    	</select>
    	
    	<insert id="empInsert" parameterType="chap5.EmpVO">
    		INSERT INTO emp (empno,ename,job)
    		VALUES
    		(#{empno}, #{ename}, #{job})
    	</insert>
    </mapper>
    ```
    
    인터페이스: EmpMapper.java
    
    ```java
    package chap5;
    
    import java.util.List;
    import org.apache.ibatis.annotations.Mapper;
    
    @Mapper
    public interface EmpMapper {
    	List<EmpVO> all();
    	int empInsert(EmpVO vo);
    }
    ```
    
    설정 MvcConfig.java
    
    ```java
    package chap5;
    
    import org.apache.ibatis.session.SqlSessionFactory;
    import org.mybatis.spring.SqlSessionFactoryBean;
    import org.mybatis.spring.SqlSessionTemplate;
    import org.mybatis.spring.annotation.MapperScan;
    import org.springframework.context.annotation.Bean;
    import org.springframework.context.annotation.ComponentScan;
    import org.springframework.context.annotation.Configuration;
    import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
    import org.springframework.web.servlet.config.annotation.DefaultServletHandlerConfigurer;
    import org.springframework.web.servlet.config.annotation.EnableWebMvc;
    import org.springframework.web.servlet.config.annotation.ViewResolverRegistry;
    import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
    
    import com.zaxxer.hikari.HikariConfig;
    import com.zaxxer.hikari.HikariDataSource;
    
    @Configuration
    // mvc 활성화 시키는 역할
    @EnableWebMvc
    @ComponentScan(basePackages = {"chap5"})
    @MapperScan(basePackages = {"chap5"})
    public class MvcConfig implements WebMvcConfigurer{
    	
    	@Override
    	public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
    		configurer.enable();
    	}
    	
    	// view resolver 설정
    	@Override
    	public void configureViewResolvers(ViewResolverRegistry registry) {
    		registry.jsp("/WEB-INF/views/", ".jsp");
    	}
    	
    	// HikariCP의 설정
    	@Bean
    	public HikariConfig hikariConfig() {
    		HikariConfig hikariConfig = new HikariConfig();
    		hikariConfig.setDriverClassName("oracle.jdbc.driver.OracleDriver");
    		hikariConfig.setJdbcUrl("jdbc:oracle:thin:@localhost:1521:xe");
    		hikariConfig.setUsername("testuser");
    		hikariConfig.setPassword("test1234");
    		return hikariConfig;
    	}
    	
    	//Datasource 객체
    	@Bean
    	public HikariDataSource dataSource() {
    		HikariDataSource ds = new HikariDataSource(hikariConfig());
    		return ds;
    	}
    	
    	// SqlSessionFactory 객체
    	@Bean
    	public SqlSessionFactory sqlSessionFactory() throws Exception {
    		SqlSessionFactoryBean ssf = new SqlSessionFactoryBean();
    		ssf.setDataSource(dataSource());
    		
    		//SqlSesstionTemplate 방식으로 하는 경우 매퍼(mapper) 파일의 위치 지정
    		PathMatchingResourcePatternResolver resolver = new PathMatchingResourcePatternResolver();
    		ssf.setMapperLocations(resolver.getResources("classpath:/mapper/emp.xml")); // mapper 파일 경로 지정
    		
    		return ssf.getObject();	
    	}
    	
    	//DAO에서 주입받을 객체
    	@Bean
    	public SqlSessionTemplate sqlSessionTemplate() throws Exception {
    		SqlSessionTemplate sst = new SqlSessionTemplate((sqlSessionFactory()));
    		return sst;
    	}
    }
    ```
    
    EmpController.java
    
    ```java
    package chap5;
    
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.PostMapping;
    
    @Controller
    public class EmpController {
    
    	@Autowired	
    	EmpMapper mapper;
    	
    	@GetMapping("/emp/list.ssg")
    	public String list(Model model) {
    		model.addAttribute("list", mapper.all());
    		return "emp/list";
    	}
    	
    	@GetMapping("/emp/write.ssg")
    	public String write() {
    		return "emp/write";
    	}
    	
    	@PostMapping("/emp/write.ssg")
    	public String insert(EmpVO vo, Model model) {
    		int r= mapper.empInsert(vo);
    		if (r> 0) {
    			// 정상 등록
    			model.addAttribute("msg", "정상적으로 등록되었습니다.");
    			model.addAttribute("url", "list.ssg");
    		} else {
    			model.addAttribute("msg", "등록실패");
    			model.addAttribute("url", "write.ssg");
    		}
    		return "emp/insert";
    	}
    }
    ```
    
    
  
* ...Factory, ....Builder : 객체를 생성해주는 것
  * 인터페이스라 직접 생성이 안됨



* jpa
  * 자바 orm 기술에 대한 표준 명세
  * java에서 제공하는 api
  * 자바 어플리케이션에서 관계형 데이터베이스를 사용하는 방식을 정의한 **인터페이스**
  * orm을 사용하기 위해 만든 인터페이스
  * 자바 클래스와 db 테이블 매핑



* ORM (Object Relational Mapper) 과 mapper의 차이
  * orm
    * db 테이블을 자바 객체로 매핑
    * 객체간의 관계를 바탕으로 sql 자동 생성
    * rdb의 관계를 object에 반영하는 것이 목적
  * mapper
    *  sql 명시 must
    * sql을 자바에서 분리(xml)
    * 필드를 매핑시키는 것이 목적



![image-20230105145526282](C:\Users\SSG\Desktop\myacaive\TIL\15_spring\spring\assets\image-20230105145526282.png)



* sql mapper

  * 메서드들

    * selectOne(): 한건 조회
    * selectList(): 여러건 조회
    * insert() : 등록 건수 리턴
    * update() : 업데이트된 건수 리턴
    * delete(): 삭제된 건수 리턴

  * 매개변수

    * "namespace.id", 객체(값)
      * 이때 namespace는 xml의 namespace
      * 예시) 등록: .insert("emp.insert", empvo);

  * 매퍼 안에 있는 sql 태그

    * <select

      * <select id="" parameterType="" resultType="">
            실행될 sql
        </select>

    * <update

    * <insert

    * <delete



## example1 - 조회

* /spring/emp/list.ssg에 들어가면 전체직원 데이터 목록 출력

  * chap5/MvcConfig.java

    ```java
    package chap5;
    
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.PostMapping;
    
    @Controller
    public class EmpController {
    
    	@Autowired
    	EmpDAO dao;
    	
    	@GetMapping("/emp/list.ssg")
    	public String list(Model model) {
    		model.addAttribute("list", dao.all());
    		return "emp/list";
    	}
    }
    ```
    
  * src/main/resources/mapper/emp.xml
  
    ```xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="emp">
    	<select id="all" resultType="chap5.EmpVO">
    		SELECT * FROM emp
    	</select>
    </mapper>
    ```
  
  * EmpVO.java
  
    ```java
    package chap5;
    
    import lombok.Data;
    
    @Data
    public class EmpVO {
    	private int empno;
    	private String ename;
    	private String job;
    }
    ```
  
  * EmpDAO.java
  
    ```java
    package chap5;
    
    import java.util.List;
    
    import org.mybatis.spring.SqlSessionTemplate;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Repository;
    
    @Repository
    public class EmpDAO {
    	
    	// sqlsessiontemplate을 주입이 되야함
    	@Autowired
    	private SqlSessionTemplate sst;
    	
    	public List<EmpVO> all() {
    		return sst.selectList("emp.all");
    	}
    }
    ```
  
  * 나중에 데이터를 처리하거나 하려면 서비스를 만들어야하지만, 지금은 select all이기 때문에 생략
  
  * EmpController.java

    ```java
    package chap5;
    
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.stereotype.Controller;
    import org.springframework.ui.Model;
    import org.springframework.web.bind.annotation.GetMapping;
    
    @Controller
    public class EmpController {
    
    	@Autowired
    	EmpDAO dao;
    	
    	@GetMapping("/emp/list.ssg")
    	public String list(Model model) {
    		model.addAttribute("list", dao.all());
    		return "emp/list";
    	}
    }
    ```
  
  * views/emp/list.jsp
  
    ```jsp
    <%@ page language="java" contentType="text/html; charset=UTF-8"
    	pageEncoding="UTF-8"%>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="UTF-8">
    <title>Insert title here</title>
    </head>
    <body>
    	<h2>직원 목록</h2>
    	<table border="1">
    		<tr>
    			<td>번호</td>
    			<td>이름</td>
    			<td>직책</td>
    		</tr>
    		<c:forEach var="vo" items="${list}">
    			<tr>
    				<td>${vo.empno }</td>
    				<td>${vo.ename }</td>
    				<td>${vo.job }</td>
    			</tr>
    		</c:forEach>
    	</table>
    </body>
    </html>
    ```
  



## example2 - 등록

/spring/emp/write.ssg->입력폼(번호, 직원명, 직책): get 전송

/spring/emp/write.ssg -> 저장 :post전송



* //EmpController.java

  ```java
  package chap5;
  
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Controller;
  import org.springframework.ui.Model;
  import org.springframework.web.bind.annotation.GetMapping;
  import org.springframework.web.bind.annotation.PostMapping;
  
  @Controller
  public class EmpController {
  
  	@Autowired
  	EmpDAO dao;
  	
  	@GetMapping("/emp/list.ssg")
  	public String list(Model model) {
  		model.addAttribute("list", dao.all());
  		return "emp/list";
  	}
  	
  	@GetMapping("/emp/write.ssg")
  	public String write() {
  		return "emp/write";
  	}
  	
  	@PostMapping("/emp/write.ssg")
  	public String insert(EmpVO vo, Model model) {
  		int r= dao.insert(vo);
  		if (r> 0) {
  			// 정상 등록
  			model.addAttribute("msg", "정상적으로 등록되었습니다.");
  			model.addAttribute("url", "list.ssg");
  		} else {
  			model.addAttribute("msg", "등록실패");
  			model.addAttribute("url", "write.ssg");
  		}
  		return "emp/insert";
  	}
  }
  
  ```

* EmpDAO.java

  ```java
  package chap5;
  
  import java.util.List;
  
  import org.mybatis.spring.SqlSessionTemplate;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.stereotype.Repository;
  
  @Repository
  public class EmpDAO {
  	
  	// sqlsessiontemplate을 주입이 되야함
  	@Autowired
  	private SqlSessionTemplate sst;
  	
  	public List<EmpVO> all() {
  		return sst.selectList("emp.all");
  	}
  	
  	// 등록
  	public int insert(EmpVO vo) {
  		return sst.insert("emp.empInsert", vo);
  		
  	}
  }
  
  ```

* write.jsp

  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8"
  	pageEncoding="UTF-8"%>
  <!DOCTYPE html>
  <html>
  <head>
  <meta charset="UTF-8">
  <title>Insert title here</title>
  </head>
  <body>
  	<form action="write.ssg" method="post">
  		<table border="1">
  			<tr>
  				<td>직원번호</td>
  				<td><input type="number" name="empno"></td>
  			</tr>
  			<tr>
  				<td>직원명</td>
  				<td><input type="text" name="ename"></td>
  			</tr>
  			<tr>
  				<td>직책</td>
  				<td><input type="text" name="job"></td>
  			</tr>
  			<tr>
  				<td colspan="2">
  				<input type="submit" value="전송">
  				</td>
  			</tr>
  		</table>
  	</form>
  </body>
  </html>
  ```

* insert.jsp

  ```jsp
  <%@ page language="java" contentType="text/html; charset=UTF-8"
      pageEncoding="UTF-8"%>
  <script>
  alert('${msg}');
  location.href='${url}';
  </script>
  
  ```

* emp.xml

  ```xml
  <?xml version="1.0" encoding="UTF-8" ?>
  <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="emp">
  	<select id="all" resultType="chap5.EmpVO">
  		SELECT * FROM emp
  	</select>
  	
  	<insert id="empInsert" parameterType="chap5.EmpVO">
  		INSERT INTO emp (empno,ename,job)
  		VALUES
  		(#{empno}, #{ename}, #{job})
  	</insert>
  </mapper>
  ```

  