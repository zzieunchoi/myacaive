# Maria DB data processing

데이터베이스 관리를 위해 필요한 데이터 처리에 대해서 과제를 해보자!



우선 heidi sql이라는 것이 MySql 보다는 다운로드도 빠르고 처리하기 쉽다고 들어서 heidi sql을 사용해보려고 한다. 

heidi sql을 사용하기 위해서는 Maria DB를 설치해야한다.

[Maria DB 설치](https://mariadb.org/) -> DOWNLOAD

[Heidi sql 설치](https://www.heidisql.com/download.php) -> DOWNLOAD



신규를 클릭하고 maria db 설치할 때 설정했던 암호를 입력한 후 저장을 하고 열기를 누르면 창이 뜬다!

![image-20220614181244718](Readme.assets/image-20220614181244718.png)



그 이후에 데이터베이스를 생성하고 그 데이터 베이스 안에서 테이블을 생성한다

![image-20220614193009494](Readme.assets/image-20220614193009494.png)



그 후 [도구] - [csv 파일 가져오기] 

![image-20220614193053225](Readme.assets/image-20220614193053225.png)

```
파일명은 바탕화면에서 가져와도 꼬이길래 안전한 로컬 드라이브에서 가져옴!
인코딩은 utf8에서 가져옴
중복 행 처리에서는 중복 무시하고 가져오기로 함!
메서드에서 클라이언트에서 파일 내용 분석을 해야 가져올 수 있었다
필드 종결자는 csv 파일을 txt 파일에서 보면 어떤걸로 구분되는지 확인 가능
줄 종결자는 txt 파일로 열었을 때 csrf 이면 r,n 으로 바꾸고 lf면 n으로만!
목적지는 아까 설정한 데이터베이스와 테이블을 설정하면 되는데 테이블이 없는 상태에서 가져오려먼 <새 테이블>을 클릭하면 된다
가져올 열들을 클릭한 후 가져오기!를 누르면 됨!
```

가져오기!를 하면 완성



이전에 필요한 열들만 뽑아오기 위해 필요없는 열은 삭제!

```sql
ALTER TABLE `sc_clinic`
	DROP COLUMN `기준일`,
	DROP COLUMN `검체채취 가능`,
	DROP COLUMN `신속항원검사(RAT)
실시가능`,
	DROP COLUMN `관할보건소`,
	DROP COLUMN `관할보건소 전화번호`,
	DROP COLUMN `장애인 편의사항`;	
```



그 이후에 

```sql
ALTER TABLE sc_clinic ALTER COLUMN ssafy_nm SET DEFAULT '7기부울경_최지은';
ALTER TABLE sc_clinic ALTER COLUMN reg_dt SET DEFAULT current_timestamp;
```

sql문을 사용해서 원하는 ssafy_nm과 reg_dt 열 추가를 한다

그렇다면 데이터는 완성!(데이터 전처리 완성)



그 이후에 아무 데이터를 선택한 후 우클릭하면 [격자행 내보내기]를 누르면 csv 파일로 내보낼 수 있다!



## 느낀점

```
데이터 전처리 하는 것이 가장 어려웠지만 sql문으로 작성하는 것보다 heidi sql을 사용하면 더 편하게 된다는 것을 알 수 있었다! 그래도 기본적인 sql문을 알아야만 heidi sql을 사용할 수 있었기 때문에 sql문 데이터 전처리하는 것을 더 자세히 알아야 된 것같다!
```

