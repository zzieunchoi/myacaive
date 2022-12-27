# null

## null이란

값이 없음(0 또는 ''이 아님) - 연산이 되지 않음

```sql
select * from emp where bonus is null;
```



## nvl, nvl2

### nvl

bonus가 null이면 0처리를 해라

```sql
select ename, salary, bonus, salary*12 + nvl(bonus,0) as "real salary" from emp;
```

### nvl2

bonus가 null 아니면 앞에 꺼, null이 맞으면 뒤에꺼

```sql
select salary, bonus, salary + nvl2(bonus, 10, 0) as "real salary" from emp;
```

