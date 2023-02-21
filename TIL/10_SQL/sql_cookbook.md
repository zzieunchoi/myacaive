# SQL



## varchar(n)의 의미

```sql
/* 테이블 생성 */
create table tb_test_1 
(
    co varchar(4)
);

/* 값 넣기 */
insert into tb_test_1 values('가');
insert into tb_test_1 values('가나');
```

* ORACLE은 한번에 여러 데이터 입력 X
  * `insert into emp_table(ename, sal, comm) values ('지은', 500, 600)` x 로우 수

* varchar(4)는 oracle에서 4byte로 인식하기 때문에 '가'는 3byte 라 '가나'는 에러

  `value too large for column "SQL_WKENABGKLLLXSMFVBRAICWPJG"."TB_TEST_1"."CO" (actual: 6, maximum: 4)`

* mysql은 varchar(4)의 숫자 = 입력 가능한 문자 길이 4개로 인식

  * oracle도 이렇게 하려면 varchar(4char)



## null을 포함한 정렬 (null을 마지막으로)

```sql
/* 테이블 생성 */
create table emp_table 
(
    ENAME varchar(20),
    SAL int,
    COMM int
);

/* 값 넣기 */
insert into emp_table values('지은', 500, 600);
insert into emp_table values('지현', 500, null);
insert into emp_table values('신세계', 500, 0);

/* NULL을 포함한 정렬(NULL을 마지막으로)*/
select * from emp_table order by COMM DESC NULLS LAST;

/* NULL을 포함한 정렬(NULL을 처음으로)*/
select * from emp_table order by COMM NULLS FIRST;
```



## 여러 테이블에서 누락된 데이터 반환

조인할 때 한 컬럼을 기준으로 잡는다면 그 기준을 바탕으로 연결된 테이블이 null이더라도 다 조인!

```sql
select d.deptno, d.dname, e.ename
from dept d full outer join emp e
on (d.deptno = e.deptno);
```



## 한번에 여러 테이블에 데이터 입력

oracle만 가능! mysql을 불가능

```sql
/* 테이블 생성 */
create table dept_east
(
    deptno int,
    dname varchar(20),
    loc varchar(20)
);

create table dept_mid
(
    deptno int,
    dname varchar(20),
    loc varchar(20)
);

create table dept_west
(
    deptno int,
    dname varchar(20),
    loc varchar(20)
);

create table dept 
(
    deptno int,
    dname varchar(20),
    loc varchar(20)
);

insert into dept values(1, '부서1', 'NEW YORK');
insert into dept values(1, '부서2', 'CHICAGO');
insert into dept values(1, '부서3', 'DALLAS');
insert into dept values(1, '부서4', 'BOSTON');

insert all 
	when loc in ('NEW YORK', 'BOSTON') then
		into dept_east (deptno, dname, loc) values (deptno, dname, loc)
    when loc in ('CHICAGO') then
    	into dept_mid (deptno, dname, loc) values (deptno, dname, loc)
    when loc in ('DALLAS') then
    	into dept_west (deptno, dname, loc) values (deptno, dname, loc)
    select deptno, dname, loc
    from dept;
    
select * from dept_east;
select * from dept_mid;
select * from dept_west;
```



## 중복 데이터 삭제하기

```sql
create table dupes 
(
    id int,
    name varchar(20)
);

insert into dupes values(1, 'a');
insert into dupes values(2, 'b');
insert into dupes values(3, 'b');
insert into dupes values(4, 'c');
insert into dupes values(5, 'c');
insert into dupes values(6, 'c');
insert into dupes values(7, 'c');

select * from dupes;

delete from dupes
where id not in (select min(id) from dupes group by name);

select * from dupes;
```



________________

## 다른 테이블 값으로 업데이트하기

new_sal 테이블 값을 이용해서 emp 테이블 업데이트 하는 쿼리

```sql
update emp e set (e.sal, e.comm) = 
(select ns.sal, ns.sal/2
 from new_sal ns
 where ns.deptno = e.deptno)
 where exists (select *
               from new_sal ns
               where ns.deptno = e.deptno);
```



* exists
  * in과 유사한 개념
  * in의 괄호 () 사이에는 특정값 혹은 서브 쿼리가 올 수 있음
  * exists의 괄호 () 사이에는 서브쿼리만 가능
  * 그러나 서브쿼리를 사용할 떄는 exists 쓰는 것이 더 효율적!

 

## 데이터 병합하기

*  merge 구문

```
merge into TableA
using TableB
on (병합 조건절)
when matched then
update set 업데이트 내용
delete where 조건
when not matched then
insert values(컬럼이름);
```



*  병합 조건절에 해당하는 데이터가 있다면 update / 조건에 해당하지 않는 데이터들은 insert



```sql
merge into emp_comission ec
using (select * from emp) emp
on (ec.empno = emp.empno)
when matched then 
	update set ec.comm = 1000
	delete where (sal < 2000)
when not matched then
	insert (ec.empno, ec.ename, ec.deptno, ec.comm)
	values (emp.empno, emp.ename, emp.deptno, emp.comm);
```



## 메타 데이터 조회 (테이블, 인덱스)



## 메타 데이터 조회 (제약조건)



## 문자열에서 원하지 않는 문자 제거

```sql
select ename, replace(translate(ename, 'AEIOU', 'aaaaa'), 'a', '') as ename_2, sal, 		   replace(cast(sal as char(4)), '0', '') as sal_2
from emp;
```



* replace

  * replace(' 문자열' or 열 이름, '바꾸려는 문자열', '바뀔 문자열')

* translate

  * translate('문자열', '대상문자', '변환문자')

  * 대상문자와 변환 문자는 1:1로 변환 -> 대상문자에는 있는데 변환 문자에는 없으면 해당 문자는 제거!

  * replace는 제거하고 싶으면 변환 문자에 ''을 사용하면 되지만, translate함수에는 변환 문자에 '' 사용 불가능

    ```sql
    select translate('1234abcd', 'abcd', 'ABC') from dual 
    
    /* 1234ABC */
    ```

* cast

  * 데이터 형식을 다른 데이터 형식으로 변환하는 역할
  *  cast('[변환하고자 하는 데이터]' as [데이터 형식])



## ip 주소 파싱하기

* substr()
  * substr([문장], 시작위치[number], 자르고 싶은 길이[number])
  * 시작부터 0이 아니고 위치는 1!
  * 만약 substr('abcdef', 3) 이면 왼쪽을 기준으로 3번째부터 전부 추출

* instr()
  * instr('문자열', '찾고 싶은 문자열', 시작위치, 발견 인덱스)
  * 입력된 문자열이 일치하면 그 첫번쨰 인덱스 값을 반환
  * instr('abcdefff', 'f', 3, 2) => 7



```sql
select ip, 
	   substr(ip, 1, instr(ip, '.')-1), 
	   substr(ip, instr(ip,'.')+1, instr(ip,'.', 1,2)-instr(ip,'.')-1), ]
	   substr(ip, instr(ip,'.', 1, 2)+1, inst(ip,'.', 1, 3)- instr(ip, '.', 1, 2) -1),
	   substr(ip, instr(ip,'.', 1, 3) +1)
from (select '12.111.34.55' as ip from t1)
```

=> 12.111.34.55, 12, 111, 34, 55



___________

## 최빈값 계산

* keep 키워드

  * 한번의 쿼리문으로 최저 또는 최고에 해당하는 행의 값을 쉽게 가져올 수 있음

  * group by / over 절과 함께 사용!

  * dense_rank 함수와 rank 차이

    * dense_rank는 중복이 된다면 순차적으로 다음 순위값 표시
    * rank는 중복이 된다면 중복 순위 개수만큼 다음 순위 값을 증가
    * keep은 dense_rank만 사용 가능!

  * keep (dense_rank last) 

    * 그룹내 최대값

  * keep (dense_rank first)

    * 그룹내 최소값

    ```sql
    create table employ (
        job varchar(20),
        sal int, 
        ename varchar(20)
    );
    
    insert into employ values ('manager', 5000, 'jonesa');
    insert into employ values ('manager', 1500, 'jonesb');
    insert into employ values ('manager', 2000, 'jonesc');
    insert into employ values ('salesman', 1500, 'jonesd');
    insert into employ values ('salesman', 1500, 'jonese');
    insert into employ values ('salesman', 3000, 'jonesf');
    
    select job, max(sal) keep(dense_rank last order by sal) as sal_last,
    max(ename) keep(dense_rank last order by sal) as ename_last
    from employ
    where job in ('manager', 'salesman')
    group by job;
    ```

    

```sql
select max(sal) keep(dense_rank first order by cnt desc) sal
from (
    select sal, count(*) cnt
    from employ
    group by sal
);
```

최빈값: 1500



## 최댓값과 최솟값을 배제한 평균 계산



## 일, 월, 연도 가감하기



## 두 날짜 사이의 일수 알아내기



## 두 날짜 사이의 영업일 수 알아내기



## 두 날짜 사이의 시, 분, 초 알아내기



## 특정 월의 마지막 날 조회





```sql
select max(sal) keep(dense_rank first order by cnt desc) sal
from (
    select sal, count(*) cnt
    from employ
    group by sal
)
```

