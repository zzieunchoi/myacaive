# api

pom.xml

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.14.1</version>
</dependency>
```



com.shinsegae.board/ BoardApiController.java

```java
package com.shinsegae.board;

import java.util.Map;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController // api를 위한 컨트롤러
public class BoardApiController {

	@GetMapping(value="/get", produces="text/plain;charset=utf-8")
	public String get() {
		return "안녕";
	}
	
	@PostMapping("/post")
	public void post(@RequestBody Map<String, String> map) {
		Set<String> keys = map.keySet();
		for (String key : keys) {
			System.out.println(key + ": " + map.get(key));
		}
	}
	
	// post 방식으로 json 데이터를 requestbody를 통해서 boardvo에 저장
	// db에 저장
	@Autowired
	BoardMapper mapper;
	
	@PostMapping("/post2")
	public void post2(@RequestBody BoardVO vo) {
		System.out.println("title:" + vo.getTitle());
		System.out.println("content: "+ vo.getContent());
		mapper.boardInsert(vo);
	}
	
	// 한건 응답(json 객체)
	@GetMapping("/api/board/{no}")
	public BoardVO getBoard(@PathVariable int no) {
		return mapper.selectOne(no);
		
	}
	
	// 여러 건 응답(json 배열)
	@GetMapping("/api/board/all")
	public List<BoardVO> getAll() {
		return mapper.selectList();
	}
}
```



talend api 확장 프로그램으로 이용

![image-20230106161450611](C:\Users\SSG\Desktop\myacaive\TIL\15_spring\spring\assets\image-20230106161450611.png)

BoardMapper.xml

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.shinsegae.board.BoardMapper">
	<insert id="boardInsert"
		parameterType="com.shinsegae.board.BoardVO">
		INSERT INTO board
		(no, title, content, regdate, member_no)
		VALUES (
        <!--sequence 쓰는 방법!-->
        <!--lombok data가 있기 때문에 getter,setter가 만들어져서 이게 가능한 거임-->
		BOARD_SEQ.NEXTVAL, #{title}, #{content}, SYSDATE, #{member_no})
        <!--위를 시행하고 아래를 시행하게 되는데 no에 set을 해서 현재 번호를 담아줌
        즉, 위에서 nextval은 2이지만 밑에 currval도 2가되는 것임
		insert를 하기 전에 값을 알려고 시행하는 것임!-->
        <selectKey keyProperty="no" order="AFTER" resultType="int">
        	SELECT BOARD_SEQ.CURRVAL FROM dual 
        </selectKey>
	</insert>
	
	<select id="selectOne" parameterType="int" resultType="com.shinsegae.board.BoardVO">
		SELECT * FROM board WHERE no = #{no}
	</select>
	
	<select id="selectList" resultType="com.shinsegae.board.BoardVO">
		SELECT * FROM board
	</select>
</mapper>
```

BoardMapper.java

```java
package com.shinsegae.board;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface BoardMapper {
	 int boardInsert(BoardVO param);
	 
	 // result 메소드 이름 파라미터
	 BoardVO selectOne(int no);
	 List<BoardVO> selectList();
}

```

