# DML, DDL

## 속성 이름 변경하기

```SQL
alter table member
rename column column1 to age;
```



## 테이블 생성하기

```SQL
create table member2 (
    id varchar2(10),
    name varchar2(20),
    age number(5),
    email varchar2(20)
);
```



## 테이블 속성 데이터 타입 변경하기

```SQL
alter table 테이블 명 modify 속성명 바꿀데이터타입(oracle)
alter table 테이블 명 alter column 속성명 바꿀데이터타입(mysql)*/
alter table member modify email varchar2(50);
```



## 행 삽입하기

insert into 테이블명 (속성1, 속성2, ...)
values (값1, 값2, ...)

`속성과 값이 연결이 된다면 상관 x, 순서가 다르게 값을 넣고 싶다면 속성을 집어넣어야함`

```SQL
insert into member (id, name, age, email)
values ('hong', '홍길동', 30, 'hong@gmail.com');

insert into member (id, name, age, email)
values ('choi', '최지은', 26, 'zzieun_choi@naver.com');
```



## 행 수정하기

update 테이블명 set 수정 결과 where 조건

```SQL
update member set age = 20 where id = 'hong';
```



## 행 삭제하기

delete from 테이블명 where 조건

```SQL
delete from member where id='hong';
```



## 데이터 조회

distinct: 중복제거



## 조건절

```SQL
select ENAME, DEPTNO from EMP where DEPTNO = 20;

insert into member2 (id, name, age, email)
values ('choi', '최지은', 15, 'zzieun_choi');

select rownum from member2;
delete from member2 where rowid = (select rid from (select rownum rn, rowid rid from member2) where rn > 4);
select rownum, m.* from member2 m;

SELECT ename, deptno FROM emp WHERE deptno in (20, 40, 50);
```



## LIKE

 % : 0개 이상의 문자
  _ : 1개의 문자

```SQL
select * from student where name like '%김%';
select name, tel from student where tel like '02)%';
```



## ALIAS

AS(별칭)은 열 이름을 임시로 변경하는 데 사용. 물리적으로 영원히 변경되는 것은 아님.
AS(별칭)은 열 이름 바로 뒤에 사용하며, 열 이름과 별칭 사이에 AS(별칭) 접속사를 넣는다.
AS(별칭) 접속사는 생략할 수 있다.
AS(별칭)에 공백, 특수문자, 대소문자 등 사용하려면 큰따옴표(")로 묶어서 사용.

```SQL
select ename, salary, salary+100 as "100만원 인상급여" from emp;
```



## 합집합

union은 sql을 느려지게 하는 장본인 - 가급적 덜 쓰는게 좋음

### union all

하정환이라는 사람은 202도 해당되고 101도 해당되는데 union all을 하면 두개의 행이 나옴

```sql
SELECT studno, name, major1, major2
FROM student
WHERE major1 = 202
UNION ALL
SELECT
studno, name, major1, major2
FROM student
WHERE major2 = 101;
```



### union

하정환이라는 사람은 202도 해당되고 101도 해당되는데 union 하면 중복이 제거되어 한개의 행이 나옴

```sql
SELECT studno, name, major1, major2
FROM student
WHERE major1 = 202
UNION
SELECT studno, name, major1, major2
FROM student
WHERE major2 = 101;
```