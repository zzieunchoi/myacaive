# java와 oracle 연결

 DB 작업 순서
		 *  1. 드라이버 클래스 로드
	2. DB에 연결
	3. SQL 실행할 객체를 준비
	4. SQL 실행
	5. 실행 결과 처리
	6. 자원 해제

```java
public static void main(String[] args) {
   
    // 0. 변수 선언
    Connection conn = null;
    Statement stmt = null; //bins가 아닌 sql : sql 실행하는 갹채
    ResultSet rs = null; // 실행결과

    try {
        // 1. 드라이버 로드(클래스를 메모리로 로드해라)
        Class.forName("oracle.jdbc.OracleDriver");
        // 2. db에 연결
        // url: "jdbc:oracle:thin:@호스트이름:포트번호:서비스이름
        String url = "jdbc:oracle:thin:@localhost:1521:xe";
        String username = "testuser";
        String pwd = "test1234" ;

        conn = DriverManager.getConnection(url, username, pwd);
        // 연결이 안되었다면 error처리 돼서 아래 프린트가 되지 않음
        System.out.println("DB 연결 성공");

        // 3. sql 실행할 객체준비
        stmt = conn.createStatement();

        // 4. sql 실행(sql을 문자열로 실행)
        // select는 executeQuery
        // insert/update/delete: executeUpdate();
        rs = stmt.executeQuery("select * from emp");

        // 5. 해당하는 열 출력 & 처리
        while (rs.next()) {
            System.out.println(rs.getString("salary"));
        }

    } catch (Exception e ) {
        System.out.println(e.toString());
    }

}
```



* Statement
* preparedstatement
  * 장점
    * "/' 가 수월해짐
      * 변수를 받아와서 sql 처리를 해야할 때 ?로 사용완료!
      * select * from emp where deptno = ?
    * 속도가 빠름(statement보다)
    * 보안 유리(statement의 경우 '`admin' --`' 이라고 보내면 뒤에가 주석 처리 돼서 해킹이 쉬움) => 개인 정보를 사용하는 페이지의 경우 보안을 위해서는 무조건 preparedstatement 사용해야함