# group

그룹핑 한 속성이 아닌 다른 속성을 출력하고자 하면 출력이 안됨
그 이외의 그룹핑 함수는 무한대로 가능

```sql
select count(*) from student group by grade;
select sum(salary* 12 + nvl(bonus, 0)) from professor;
select ceil(avg(salary)), ceil(avg(nvl(bonus, 0))) from professor;
select max(salary), min(salary) from professor;

select major1, count(*) from student group by major1;
select position, count(*) from professor group by position order by count(*) desc;
```



## group by

* group by 로 묶은 것들의 지정한 그룹 함수에 대한 합계를 보여줌

  ```sql
  select deptno, sum(salary) from emp group by rollup(deptno);
  select grade, count(*) from student group by rollup(grade);
  ```



* rollup에 다양한 속성 :  deptno별로 + job별로 합계를 보여줌 마지막에 전체 합계도 보여줌

  grouping sets: 각 속성 별로 별도 합계(전체 합계 x)
  cube; 결합 가능한 모든 그룹핑 ex) deptno가 0일때 job이 이사일 경우... 다양한 조합 결과

  ```sql
  select deptno, job, sum(salary) from emp group by rollup(deptno,job);
  select deptno, job, sum(salary) from emp group by grouping sets(deptno, job);
  select deptno, job, sum(salary) from emp group by cube(deptno, job);
  ```



* having : group by 결과의 조건을 지정할 때 사용 

  group by 로 다 그룹핑 한 다음에 그 결과의 조건으로 사용할 때 사용

  데이터를 그룹핑 하기 전에 조건을 주려면 having x where 절 사용

  ```sql
  select major1, avg(height) from student where height >= 170 group by major1;
  select major1, avg(height) from student group by major1 having avg(height) >= 170;
  select deptno, avg(salary) from professor group by deptno having avg(salary) >= 300;
  ```