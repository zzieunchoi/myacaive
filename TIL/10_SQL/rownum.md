rownum은 동적생성되어 rownum이 1 이상인 것은 조회할 수 없음
-> 행번호가 3번인 행만 가져온다면 조회 결과는 1건이 되고 행번호는 다시 1이 되어
행번호 3인 자료는 가져올 수 없음

1. rowid는 가능? x
2. delete from table 1 where rowid = (select rid from (select rownum rn, rowid rid from table1) where rn = 3)
   이건 됨

하지만 2개 이상일 경우 single-row subquery returns more than one row 라는 에러가 떠서  단일 행 하위 질의에
2개 이상의 행이 리턴되었다는 것을 보여준다