# 페이징 처리

```sql
select * 
from (select rownum as rnum, a.*
    from ( select * from student order by grade desc) a) b
where b.rnum between 1 and 10;
```

