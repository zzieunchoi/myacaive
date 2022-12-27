# join

  크로스 조인(cross join): 가능한 모든 행 조인
   등가 조인(equi join): 조건이 일치하는 결과
   비등가 조인(non equi join): 조건이 일치하지 않는 결과
   외부 조인(outer join): 양쪽 테이블의 한쪽만 조건이 일치해도 출력
   자체 조인(self join): 자체 테이블에서 조인 



## equi join

테이블 간의 pk를 이용해서 조인

select 테이블명.컬럼1 ,..
from 테이블명1, 테이블명2
where 테이블명1.컬럼명 = 테이블명2.컬렴명 

select 테이블명.컬럼1 ,..
from 테이블명1
join 테이블명2
on 테이블명1.컬럼명 = 테이블명2.컬렴명

```sql
select emp.ename, dept.dname
from emp, dept
where emp.deptno = dept.deptno;

select student.name, major.name
from student, major
where student.major1 = major.code;

select s.name, p.name || ' ' || '교수' as "담당 교수"
from student s, professor p
where s.profno = p.no;
```



## outer join

양쪽 테이블 모두 조건이 만족하지 않아도, 한쪽 테이블의 데이터를 모두 출력해야 하는 경우 사용 

select s.name, p.name
from student s, professor p
where s.profno = p.no(+) 
(+) 붙어있지 않은 쪽이 더 넓은 쪽

select s.name, p.name
from student s
left join professor p
on s.profno = p.no 
left/ right 방향으로 가리키는 테이블이 더 넓은 쪽



```sql
select s.name as "학생 이름", p.name as "교수 이름"
from student s, professor p
where s.profno = p.no(+) 
order by s.name, p.name;

select s.name as "학생 이름", p.name as "교수 이름"
from student s
left join professor p
on s.profno = p.no
order by s.name, p.name;
```