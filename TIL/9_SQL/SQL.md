# SQL

## SUM, MAX, MIN

* 최솟값 구하기

  동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

  ```SQL
  SELECT MIN(DATETIME) AS "시간" FROM ANIMAL_INS
  ```

  표에 MIN(DATETIME)이라고 뜨지 않게 하기 위해서는

  `MIN(DATETIME) AS "시간"`

* 중복값 제거하기

  동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

  ```SQL
  SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL
  ```



## GROUP BY

* 고양이와 개는 몇마리 있을까

  동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

  ```SQL
  SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE
  ```

* 동명 동물 수 찾기

  동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

  `WHERE 절은 FROM으로부터 불러들여진 데이터에서 필요한 데이터만 뽑는다면,
  having 은 group by 로 묶여진 그룹에 대해 필요한 데이터만 뽑는 구문입니다. `

  ```sql
  SELECT NAME, COUNT(NAME) AS "COUNT" FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME
  ```

* 입양 시각 구하기(1)

  보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

  ```SQL
  SELECT HOUR(DATETIME), COUNT(ANIMAL_ID) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) BETWEEN 9 AND 20 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME) ASC
  ```

  ```
  GROUP BY, WHERE, HAVING
  - 컬럼 그룹화
  	SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼;
  - 컬럼 그룹화 후에 조건 처리
  	SELECT 컬럼 FROM 테이블 GROUP BY 그룹화할 컬럼 HAVING 조건식;
  - 조건 처리 후에 컬럼 그룹화
  	SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼;
  - 조건 처리 후에 컬럼 그룹화 후에 조건 처리
  	SELECT 컬럼 FROM 테이블 WHERE 조건식 GROUP BY 그룹화할 컬럼 HAVING 조건식;
  - ORDER BY는 GROUP BY, HAVING 후에!
  	SELECT 컬럼 FROM 테이블 [WHERE 조건식] GROUP BY [그룹화할 컬럼] HAVING [조건식] ORDER BY 컬럼1 [, 컬럼2, 컬럼3 ...];
  ```

* 입양 시각 구하기(2)

  보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.

  ```SQL
  # 재귀테이블 만들기
  WITH RECURSIVE HOUR_A AS (
  SELECT 0 AS H
  UNION ALL
  SELECT H+1 
  FROM HOUR_A
  WHERE H <23
  )
  
  SELECT A.H,
  	CASE WHEN B.CNT IS NULL THEN 0
  	ELSE B.CNT
  	END AS COUNT
  FROM HOUR_A AS A
  LEFT JOIN (SELECT HOUR(DATETIME) AS HOUR_B, COUNT(ANIMAL_ID) AS CNT 
             FROM ANIMAL_OUTS 
             GROUP BY HOUR(DATETIME)) AS B 
  ON A.H = B.HOUR_B
  ```

  ```SQL
  # 재귀테이블 만들기
  WITH RECURSIVE 테이블명 AS
  (
  SELECT 초기값 AS 컬럼명
  UNION ALL
  SELECT 컬럼명 재귀 조건
  FROM 테이블명
  WHERE 제어문
  )
  ```

  ```SQL
  # CASE WHEN 사용하기
  CASE WHEN 조건식 THEN 반환값
       WHEN 조건식2 THEN 반환값2
       ELSE 조건에 만족하지 않을 경우 반환값
  END [AS 컬럼 이름]
  ```

  ```SQL
  # LEFT JOIN = 합집합
  SELECT column_name(s) FROM table1 LEFT JOIN table2
  ON table1.column_name=table2.column_name;
  
  # INNER JOIN = 교집합
  SELECT column_name(s) FROM table1 INNER JOIN table2
  ON table1.column_name=table2.column_name;
  ```



## IS NULL

* 이름이 없는 동물의 아이디

  동물 보호소에 들어온 동물 중, 이름이 없는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

  ```SQL
  SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NULL
  ```

* 이름이 있는 동물의 아이디

  동물 보호소에 들어온 동물 중, 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

  ```SQL
  SELECT ANIMAL_ID FROM ANIMAL_INS WHERE NAME IS NOT NULL ORDER BY ANIMAL_ID ASC
  ```

* NULL 처리하기

  동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

  ```SQL
  SELECT ANIMAL_TYPE, 
  	   CASE WHEN NAME IS NULL THEN "No name"
  	   ELSE NAME
  	   END AS NAME,
         SEX_UPON_INTAKE 
  FROM ANIMAL_INS  
  ```

  

## JOIN

* 없어진 기록 찾기

  천재지변으로 인해 일부 데이터가 유실되었습니다. 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.

  ```SQL
  # NOT IN
  SELECT ANIMAL_ID, NAME FROM ANIMAL_OUTS
  WHERE NAME NOT IN (SELECT NAME FROM ANIMAL_INS)
  ORDER BY ANIMAL_ID;
  ```

  ```SQL
  # LEFT JOIN
  SELECT O.ANIMAL_ID, O.NAME
  FROM ANIMAL_OUTS O LEFT JOIN ANIMAL_INS I 
      ON (O.ANIMAL_ID = I.ANIMAL_ID)
  WHERE I.ANIMAL_ID IS NULL
  ORDER BY O.ANIMAL_ID
  ```

  

  



## STRING, DATE

