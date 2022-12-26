/* 속성 이름 변경하기 */
alter table member
rename column column1 to age;

/* 테이블 생성하기 */
create table member2 (
    id varchar2(10),
    name varchar2(20),
    age number(5),
    email varchar2(20)
);

/* 테이블 속성 데이터 타입 변경하기
alter table 테이블 명 modify 속성명 바꿀데이터타입(oracle)
alter table 테이블 명 alter column 속성명 바꿀데이터타입(mysql)*/
alter table member modify email varchar2(50);

/* 행삽입하기 
insert into 테이블명 (속성1, 속성2, ...)
values (값1, 값2, ...)*/
/* 속성과 값이 연결이 된다면 상관 x, 순서가 다르게 값을 넣고 싶다면 속성을 집어넣어야함 */
insert into member (id, name, age, email)
values ('hong', '홍길동', 30, 'hong@gmail.com');

insert into member (id, name, age, email)
values ('choi', '최지은', 26, 'zzieun_choi@naver.com');

/* 행수정하기
update 테이블명 set 수정 결과 where 조건*/
update member set age = 20 where id = 'hong';

/* 행 삭제하기
delete from 테이블명 where 조건*/
delete from member where id='hong';

/* 데이터 조회
distinct: 중복제거*/

/* 조건절 */
select ENAME, DEPTNO from EMP where DEPTNO = 20;

insert into member2 (id, name, age, email)
values ('choi', '최지은', 15, 'zzieun_choi');

select rownum from member2;
delete from member2 where rowid = (select rid from (select rownum rn, rowid rid from member2) where rn > 4);
select rownum, m.* from member2 m;

SELECT ename, deptno FROM emp WHERE deptno in (20, 40, 50);

/* % : 0개 이상의 문자
   _ : 1개의 문자 */ 
select * from student where name like '%김%';
select name, tel from student where tel like '02)%';

/* alias 특징
AS(별칭)은 열 이름을 임시로 변경하는 데 사용. 물리적으로 영원히 변경되는 것은 아님.
AS(별칭)은 열 이름 바로 뒤에 사용하며, 열 이름과 별칭 사이에 AS(별칭) 접속사를 넣는다.
AS(별칭) 접속사는 생략할 수 있다.
AS(별칭)에 공백, 특수문자, 대소문자 등 사용하려면 큰따옴표(")로 묶어서 사용.
*/
select ename, salary, salary+100 as "100만원 인상급여" from emp;

/*합집합 그러나 union은 sql을 느려지게 하는 장본인 - 가급적 덜 쓰는게 좋음 */
/*하정환이라는 사람은 202도 해당되고 101도 해당되는데 union all을 하면 두개의 행이 나옴*/
SELECT studno, name, major1, major2
FROM student
WHERE major1 = 202
UNION ALL
SELECT
studno, name, major1, major2
FROM student
WHERE major2 = 101;

/*하정환이라는 사람은 202도 해당되고 101도 해당되는데 union 하면 중복이 제거되어 한개의 행이 나옴*/
SELECT studno, name, major1, major2
FROM student
WHERE major1 = 202
UNION
SELECT studno, name, major1, major2
FROM student
WHERE major2 = 101;

/* null: 값이 없음(0 또는 ''이 아님) - 연산이 되지 않음*/
select * from emp where bonus is null;

/* nvl: bonus가 null이면 0처리를 해라*/
select ename, salary, bonus, salary*12 + nvl(bonus,0) as "real salary" from emp;
/* nvl2: bonus가 null 아니면 앞에 꺼, null이 맞으면 뒤에꺼*/
select salary, bonus, salary + nvl2(bonus, 10, 0) as "real salary" from emp;

/* 함수 */
/* LOWER 소문자로 변경 */
/* UPPER 대문자로 변경 */
select upper(id), lower(id) from student;
/* SUBSTR 문자열 일부 추출 substr(변수, 시작위치, 글자의 개수) */
select name, substr(name, 1, 2) from student;
-- 숫자를 따로 지정하지 않으면 맨 끝까지!
select name, substr(name, 1) from student;
/* REPLACE 문자열 치환 replace(변수, 바꾸고 싶은 단어, 바꿀 단어)*/
select name, replace(name, substr(name, 1, 1), '*') from student; -- 이렇게 하면 이철이 => *철*
select name, concat('*', substr(name, 2)) from student; -- 이렇게 하면 이철이 => *철이
/* CONCAT 문자열 결합 concat(a, b) or a || b 
concat의 인자는 2개뿐! 그래서 concat(a, concat(b, c)) 이렇게 해야함
그러나 ||는 무한대로 결합 가능 */
select ename, job, concat(ename, job) from emp; -- 서민구대표
select ename || ' ' || job from emp; -- 서민구 대표
/* LENGTH 문자열의 길이 */
/* INSTR 문자열 위치 */
select instr(tel,')'), tel from student;
select substr(tel, 1, instr(tel,')')-1) as "지역번호" from student;
/* TRIM 앞 뒤 문자열 제거 */
/* LTRIM 왼쪽 문자열 제거 왼쪽부터 해당 문자열이 나오지 않으면 break */
select url, ltrim(url, 'hw') from professor; -- ://...
/* RTIRM 오른쪽 문자열 제거 */
select url, rtrim(url, '.net') from professor;
select length(rtrim('    홍길동     ', ' ')) from dual; -- 7
select length(replace('    홍길동     ', ' ', '')) from dual; -- 3

/* 숫자 관련 함수 */
/*ROUND 반올림 round(숫자, 소수점 자리수)*/
select round(3.141592, 3) from dual; --3.142
select round(3.141592, 0) from dual; --3
select round(3.141592, -1) from dual; --0
/*TRUNC 버림*/
SELECT ROUND(3.141592,4), TRUNC(3.141592,4) FROM dual; --3.1416, 3.1415
/*CEIL 정수로 올림*/
/*FLOOR 정수로 내림*/
SELECT CEIL(3.1415), FLOOR(3.1415) FROM dual; --4, 3
/*POWER 거듭제곱 a^b*/
/*SQRT 제곱근 루트a*/
SELECT POWER(3,3) , SQRT(100) FROM dual; --27, 10

/*날짜 함수*/
select sysdate from dual;
/* 문자열로 변환: to_char
   날짜로 변환: to_date */
select trunc(sysdate - to_date('2021-01-01')) from dual;
select to_char(sysdate, 'yy/mm/dd') from dual;

/* 1. row_number() : 동점이던 아니던 그냥 점수 매김
   2. rank() : 동점이면 같은 랭킹 그 다음 사람은 동점인 사람 수만큼 밀려남
   3. dense_rank(): 동점이면 같은 랭킹이지만 그 다음 사람은 바로 다음 ranking*/
SELECT salary, ROW_NUMBER() OVER(ORDER BY salary DESC) as rank1, RANK() OVER(ORDER BY salary DESC) as rank2, DENSE_RANK() OVER(ORDER BY salary DESC) as rank3
FROM emp;

/*decode DECODE(컬럼명 , 조건값 , 조건값과 같은 경우 , 조건값과 다른 경우)*/
select grade, decode(grade, 1, '신입생', '재학생') from student;
/*decode 중첩 사용*/
select grade, decode(grade, 1, '신입생', decode(grade, 2, '2학년', decode(grade, 3, '3학년', '4학년'))) as "학년" from student;
select grade, decode(grade, 1, '신입생', substr(grade, 1, 1) || '학년') from student;