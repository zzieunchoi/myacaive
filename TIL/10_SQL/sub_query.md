# sub query

서브쿼리의 결과가 1개인 경우/ 2개 이상인 경우가 존재
서브쿼리는 where, 컬럼, having, from 구문에서 사용 가능



```sql
select ename, salary
from emp
where salary > (select salary from emp where ename='양준혁');

select name, grade, height
from student
where height in (select height from student where grade = 1) and grade = 2;
```



## 다중행 서브쿼리 any

어떤 키든 그 키보다 크면 출력

```sql
select name, grade, height
from student
where height >= (select min(height) from student where grade = 2) and grade =2;

select name, grade, height
from student
where height >= any (select height from student where grade = 2) and grade =2;
```



## 다중행 서브쿼리 all

모든 키보다 크면 출력

```sql
select name, grade, height
from student
where height >= (select max(height) from student where grade = 2) and grade =2;

select name, grade, height
from student
where height >= all (select height from student where grade = 2) and grade =2;
```



## 스칼라 서브쿼리

컬럼 자리에 서브쿼리가 들어가는 경우

```sql
select ename, d.deptno, dname
from emp e 
join dept d
on e.deptno = d.deptno;

select ename, deptno, 
    (select dname from dept where deptno = emp.deptno)
from emp;
```



## inline view

가상의 테이블을 만드는 쿼리

```sql
select ename, e.deptno, e.salary, v.s
from emp e
join (select deptno, avg(salary) s from emp group by deptno) v
on e.deptno = v.deptno;
```

