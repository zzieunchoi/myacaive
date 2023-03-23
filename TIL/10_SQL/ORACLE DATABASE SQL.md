# ORACLE DATABASE SQL

## CHAPTER 2. SELECT

### BASIC SELEECT STATEMENT

* Basic select 문

  ```sql
  SELECT [DISTINCT] COLUMN EXPRESSION [ALLIAS]
  FROM TABLE
  ```

  * SELECT : 보여질 컬럼들을 명시
  * `* ` : 모든 컬럼들을 선택
  * DISTINCT: 중복을 방지
  * column , expression : 선택할 컬럼의 이름 혹은 표현
  * alias: 선택된 열에 새로운 이름을 부여
  * FROM: 그러한 컬럼들을 보유하고 있는 테이블 이름을 명시



* sql 문을 작성하는 방법
  * SQL 문은 대소문자를 구분하지 않는다.
  * 한 문장 혹은 그 이상의 문장으로 작성 가능
  * keyword는 줄여쓸 수 없고, 여러 줄로 나눠서 작성할 수 없음
  * 한 문장은 다른 줄에 위치
  * 인덴트는 가독성을 높이기 위해 사용
  * 많은 sql 문을 작성할 땐 세미콜론을 사용해서 나눔
  * 모든 sql 문 끝에 세미콜론을 작성해야함



* 기본 헤딩 컬럼
  * 데이트, 문자는 왼쪽 정렬
  * 숫자는 오른쪽 정렬



### ARTIHMETIC EXPRESSIONS AND NULL VALUES IN THE SELECT STATEMENT

* 산수 표현

  * `+ - * /` 

  * ()를 사용해서 산수 순서를 정할 수 있음

    ```sql
    SELECT LAST_NAME, SALARY, SALARY + 300
    FROM EMPLOYEE;
    ```

    

* NULL VALUE

  * zero, 공백과 같은 뜻은 아님

    * zero는 숫자, 공백은 캐릭터임!

  * 만약 한 행이 데이터 값이 부족하다면, 그 값은 null이 되거나 null을 포함한다

  * null은 없는, 부여되지 않은, 모르는, 부적절한 값이다.

  * 어떤 데이터의 속성을 갖고 있던 열은 null을 포함하고 있지만, not null, primary key 등 제한있는 열은 안됨

  * 수식 표현에 null이 있다면, 그 값을 null 됨

    ```sql
    SELECT LAST_NAME, 12 * SALARY * COMMISSION_PCT
    FROM EMPLOYEE;
    
    => SALARY는 값이 있고, COMMISSION_PCT는 NULL 이라면 모든 값이 NULL이 됨
    ```

  * 나눌 때 0으로 나누면 에러가 뜨지만, NULL로 나눈다면 NULL 값이 나옴



### COLUMN ALIASES

* COLUMN ALIAS

  * 열 이름을 바꿈
  * 계산에 유용함
  * AS라는 단축키를 사용할 수도 있음
  * 공백이 있거나, 특수문자를 포함하거나, 대소문자 구별이 명확해야한다면 "" 이 필요함

  ```SQL
  SELECT LAST_NAME "NAME", SALARY* 12 "ANNUAL SALARY", COMMISSION_PCT AS COMM
  FROM EMPLOYEES;
  ```

  

### CONCATENATION OPERATOR, LITERAL CHARACTER STRINGS, ALTERNATIVE QUOTE OPERATOR, THE DISTINCT KEY WORD

* concatenation operator(`||`)

  * 열이나 문자열을 다른 열에 연결시킴
  * 수식 표현, 상수 값을 연결하여 캐릭터 표현으로 만들 수 있음

  ```sql
  SELECT LAST_NAME || JOB_ID AS "EMPLOYEE"
  FROM EMPLOYEES;
  ```



* literal character Strings

  * literal은 select 문에 포함되어있는 캐릭터, 숫자, 날짜이다
  * 날짜와 문자열은 반드시 ' ' 에 감싸져 있어야함

  ```sql
  SELECT LAST_NAME || ' IS A ' || JOB_ID AS "EMPLOYEE DETAILS"
  FROM EMPLOYEE;
  
  => GRANT IS A SA_REP
  ```

  

* alternative quote (q) operator

  * 따옴표 구분 기호 지정 가능
  * 구분 기호 선택
  * 가독성과 사용성을 증가 시킴
  * 중간에 '를 쓸 일이 있을 때 사용하기 편리
  * '[]' 안에 있는 모든 글자를 합쳐줌

  ```sql
  SELECT department_name || q'[ Department's Manager Id : ]' || manager_id AS "department and manager"
  FROM DEPARTMENT;
  ```



* duplicate rows

  * 중복되는 행을 제거함
  * distinct는 모든 선택된 열에 해당되며, 각 열의 중복 제거 조합에 결과로 나타난다

  ```sql
  SELECT DISTINCT department_id
  FROM EMPLOYEE;
  ```

  

### DESCRIBE COMMAND

* DESCRIBE

  * 테이블의 구조를 보여주기 위해 DESCRIBE 명령어를 작성
  * 연결 구조에 있느 테이블을 선택하고 테이블 구조를 보기 위해 열 탭을 사용
  * 테이블이 보유한 컬럼의 이름, NULL 허용 여부, 데이터 유형이 나타남
    * DESCRIBE의 NULL 탭에 NOT NULL이라고 적혀있는 경우 : 반드시 데이터를 포함하고 있어야함

  ```SQL
  DESCRIBE 테이블 이름;
  
  DESC 테이블 이름;
  ```

  

## CHAPTER 3. SORT

* 쿼리로 검색되는 행들 제한
* 쿼리로 검색되는 행들 정렬
* 실행시간에 출력되는 값들을 정렬하고 제한하기 위한 & 



### LIMIT ROWS 

* where 절

  * 데이터가 충족시켜야하는 조건을 포함함
  * FROM 절 바로 뒤에 따라 붙음
  * 조건이 충족된다면, 해당 행이 보여짐
  * 열 이름, 상수, 비교 연산자로 구성됨
  * 하나 이상의 표현식과 BOOLEAN 연산자의 조합으로 이루어져있음
  * TRUE, FALSE, UNKNOWN의 값을 보여줌

  ```SQL
  SELECT [DISTINCT] COLUMN | EXPRESSION [ALIAS]
  FROM TABLE
  WHERE LOGICAL EXPRESSION(S);
  ```



* CHARACTER STRINGS AND DATES

  * 문자열, 날짜는 ' '로 막혀있음
  * 문자열은 대소문자 구분이 필요하고 날짜는 포맷이 중요함
  * 기본 DATE 포맷은 DD-MON-RR (07-JUL-97) 

  ```SQL
  SELECT LAST_NAME, JOB_ID, DEPARTMENT_ID
  FROM EMPLOYEES
  WHERE LAST_NAME = 'Whalen' and HIRE_DATE = '17-FEB-96';
  ```

  

* COMPARISON OPERATORS

  * = , > , >=, < , <= , <>, BETWEEN .. AND .. , IN(SET) , LIKE, IS NULL
  * WHERE 절 조건식에 넣을 때 사용

  ```SQL
  SELECT LAST_NAME, SALARY
  FROM EMPLOYEES
  WHERE SALARY <= 3000;
  ```



* BETWEEN 연산자를 통한 범위 조건

  * 두 값 사이의 범위에 기초한 행들을 보여줌
  * 최소 제한과 최대 제한이 있음
  * 문자열에도 사용 가능

  ```SQL
  SELECT LAST_NAME, SALARY
  FROM EMPLOYEES
  WHERE SALARY BETWEEN 2500 AND 3500;
  ```



* IN을 활용한 조건
  * 모든 데이터 타입에 전부 사용 가능
    * 문자열에도 사용 가능
  * 값들의 특정 셋 중에서 조건에 맞는 것을 찾고 싶다면 IN을 사용
  * 값의 순서가 중요하지 않음
  * A = VALUE1 OR A = VALUE2 OR A = VALUE3와 같음
  
  ```sql
  SELECT EMPLOYEE_ID, LAST_NAME, SALARY, MANAGER_ID
  FROM EMPLOYEES
  WHERE MANAGET_ID IN (100, 102, 201);
  ```
  
  

* LIKE 연산자

  * 문자열을 검색할 때 와일드카드 서치를 수행하기 위함
    * 와일드카드: 사용된 문자가 들어있는 문자열을 검색해야하는 경우
  * % : 하나도 없거나 많은 문자열
  * _ : 하나의 문자만
  * 이 때 문자열은 대소문자를 구분하므로 대문자 S가 들어있다면 소문자 s는 검색되지 않음

  ```SQL
  SELECT FIRST_NAME
  FROM EMPLOYEES
  WHERE FIRST_NAME LIKE 'S%';
  ```

  * 두 와일드카드를 혼용해서 사용도 가능

  ```sql
  SELECT FIRST_NAME
  FROM EMPLOYEES
  WHERE FIRST_NAME LIKE '_S%' ;
  ```

  * 실제 %, _ 문자를 찾기 위해서 ESCAPE 사용 가능

  ```SQL
  SELECT EMPLOYEE_ID, LAST_NAME, JOB_ID
  FROM EMPLOYEES
  WHERE JOB_ID LIKE '%SA\_%' ESCAPE \
  
  => 무슨 무슨 글자 + SA_ + 무슨 무슨 글자
  ```



* NULL 조건

  * 값이 NULL인 행을 찾음
  * NULL이 아닌 값을 찾으려면 IS NOT NULL
  * 이 때, NULL은 =을 사용할 수 없음
    * 다른 값과 동일하거나 안 동일한지 알 수 없기 떄문

  ```SQL
  SELECT LAST_NAME, MANAGER_ID
  FROM EMPLOYEES
  WHERE MANAGER_ID IS NULL;
  ```



* 논리 연산자를 사용해서 조건 정의

  * AND : 두 조건이 참이라면 참을 반환
  * OR : 두 조건 중 하나만 참이라도 참 반환
    * NULL OR TRUE : TRUE
    * NULL OR FALSE : NULL
    * NULL OR NULL : NULL
  * NOT : 조건이 거짓이라면 TRUE 반환
    * NULL의 NOT은 NULL
    * 다른 연산자들과 함께 사용 가능
      * BETWEEN: WHERE SALARY NOT BETWEEN 1000 AND 5000
      * IN : WHERE SALARY NOT IN (500, 1000)
      * LIKE : WHERE LAST_NAME NOT LIKE '%A%'
      * NULL : WHERE COMMISSION_PCT IS NOT NULL

  ```SQL
  /* AND */
  SELECT ..
  FROM ..
  WHERE SALARY >= 10000 AND JOB_ID LIKE '%MAN%';
  
  /* OR */
  SELECT ..
  FROM ..
  WHERE SALARY >= 10000 OR JOB_ID LIKE '%MAN%';
  
  /* NOT */
  SALARY ..
  FROM ..
  WHERE JOB_ID NOT IN ('IT_PROG', 'ST_CLERK', 'SA_REP')
  ```

  

### RULES OF PRECEDENCE FOR OPERATORS IN AN EXPRESSION(연산자 우선순위)

* 우선순위
  * 숫자 표현
  * 연결 연산자
  * 비교 조건
  * IS [NOT] NULL, LIKE, [NOT] IN 
  * [NOT] BETWEEN
  * NOT EQUAL TO
  * NOT logical condition
  * AND logical condition
  * OR logical condition



### SORTING ROWS USING THE ORDER BY CLAUSE

* ORDER BY 를 통한 정렬

  * 주어진 행이 보여지는 순서를 세분화함
  * ASC: 오름차순
  * DESC: 내림차순
  * SELECT문에서는 ORDER BY 가 가장 마지막에 나옴
  * 숫자는 가장 작은 값부터 나옴
  * 날자짜는 이른 값부터 나옴
  * 문자는 알파벳 순서로 나옴
  * NULL 값은 오름차순에서 마지막에 나오고, 내림차순에서 가장 먼저 나옴
  * SELECT 에 있는 열 외의 열로도 정렬 가능

  ```SQL
  SELECT ..
  FROM ..
  ORDER BY HIRE_DATE;
  
  /* 정렬하려는 해당 열에 alias를 썼다면 alias로 정렬해야함 */
  SELECT .., SALARY*12 ANNSAL
  FROM EMPLOYEES
  ORDER BY ANNSAL;
  ```



* ORDER BY 특이 사항

  * 열의 숫자 위치에 따라 사용 가능

    ```SQL
    SELECT LAST_NAME, JOB_ID, DEPARTMENT_ID, HIRE_DATE
    FROM EMPLOYEES
    ORDER BY 3;
    
    => DEPARTMENT_ID 가 SELECT 문에서 3번째에 있으므로, 이 열을 기준으로 SORTING
    ```

  * 많은 열들을 기준으로 SORTING 가능

    ```SQL
    SELECT LAST_NAME, DEPARTMENT_ID, SALARY
    FROM EMPLOYEES
    ORDER BY DEPARTMENT_ID, SALARY DESC;
    ```

    

### SUBSTITUTION VARIABLES

* & 치환 변수(단일 치환 변수)

  * 변수 앞에 &를 붙이면 유저가 값을 입력하도록 할 수 있음
  * 문자 및 날짜 값을 치환 변수로 지정할 때에는 작은 따옴표로 묶어야 됨
  * 조건 절 뿐만 아니라 SELECT, ORDERBY, 열 표현, 테이블 이름, 모든 SELECT 문에서도 사용 가능

  ```SQL
  SELECT ENAME 이름, DEPTNO 부서
  FROM EMP
  WHERE DEPTNO = &DEP AND HIREDATE = '&DATE';
  ```

  ```SQL
  SELECT ENEMA 이름, DEPTNO 부서, &COL_NAME 연봉
  FROM EMP
  WHERE &CONDITION
  ORDER BY &ORDER_COL;
  ```



* && 치환 변수(이중 치환 변수)

  * 변수 값을 재사용하는 경우 사용
  * 이중 치환 변수는 단일 치환 변수보다 앞쪽에

  ```SQL
  SELECT ENAME 이름, &&DEP 부서
  FROM EMP 
  ORDER BY &DEP;
  
  => 부서에 대해 입력값을 받고 그 입력값에 대해 ORDER BY
  ```

  * 사용 후에는 UNDEFINE 명령을 사용하여 일시적으로 저장된 값 삭제

  ```SQL
  UNDEFINE DEP;
  ```

  

### DEFINE AND VERIFY COMMANDS

* DEFINE: 변수에 값을 부여하거나 만들기 위한 명령어

  ```SQL
  DEFINE EMPLOYEE_NUM = 200
  SELECT EMPLOYEE_ID, LAST_NAME, SALARY, DEPARTMENT_ID
  FROM EMPL
  WHERE EMPLOYEES_ID = &EMPLOYEE_NUM
  ```

  

* UNDEFINE: 변수의 값을 제거하기 위한 명령어



* VERIFY 

  * 스크립트 출력 탭에서 치환 변수를 값으로 바꾸기 전, 후의 명령문을 확인 가능

  ```SQL
  SET VERIFY ON
  SELECT ENAME 이름, DEPTNO 부서
  FROM EMP
  WHERE DEPTNO = &DEP;
  ```

  => DEP에 대한 값 입력 후 

  ```
  이전: SELECT ENAME 이름, DEPTNO 부서FROM EMP WHERE DEPTNO = &DEP;
  신규: SELECT ENAME 이름, DEPTNO 부서FROM EMP WHERE DEPTNO = 30;
  ```

  이라는 명령문을 확인가능



## CHAPTER 4. USING SINGLE ROW FUNCTIONS TO CUSTOMIZE OUTPUT

* SQL에서 가능한 함수의 다양한 타입
* SELECT 문에서 문자열, 숫자, 날짜 함수 사용 가능



* 함수들의 특징
  * SQL 함수는 인자를 갖을 수도 있고, 결과는 반드시 출력한다
  * 데이터의 계산을 수행
  * 각각 개별의 데이터 아이템을 수정
  * 행들의 그룹의 출력을 조작
  * 보여지기위한 날짜와 숫자의 포맷
  * 열의 데이터 타입을 변환



### SINGLE -ROW SQL FUNCTIONS

* SINGLE-ROW 함수
  * 데이터 아이템을 조작
  * 인자를 받고 하나의 값을 리턴함
  * 리턴된 각 행들 하나씩 수행
  * 한 행당 하나의 결과 반환
  * 데이터 타입을 수정 가능
  * 중첩될 수 있음
  * 열 혹은 표현인 인자들도 받을 수 있음



### CHARACTER FUNCTIONS

* 대소문자 변경 함수
  * LOWER
  * UPPER
  * INITCAP : 매개변수로 들어오는 CHAR의 첫문자는 대문자로, 나머지는 소문자로 반환
    * 공백이나 알파벳이 아닌 문자를 만나 후 다음 첫 알파벳 문자를 대문자로 변환
* 문자열 조작 함수
  * CONCAT
  * SUBSTR : 부분문자열 반환
  * LENGTH
  * INSTR: 해당하는 문자의 위치를 반환
  * LPAD | RPAD
  * TRIM
  * REPLACE



### NUMBER FUNCTIONS

* round: 특정 소수점으로 반올림
  * 인자가 2이면 -> 소수 셋째 자리에서 반올림
* trunc: 특정 소수점으로 내림
* mod: 나누고 난 나머지
* dual이라는 테이블: 계산, 함수로부터 결과를 살펴보기 위한 테이블



### WORKING WITH DATES

* sysdate: date, time을 반환 해주는 함수

  ```sql
  select sysdate
  from dual;
  ```

* 날짜로 숫자를 더하거나 뺄 수 있음

  * date + number
  * date - number

* 날짜들 사이의 일수를 날짜 뺌으로써 알 수 있음

  * date - date

* 날짜에 시간을 더할 수 있음

  * date + number/24

  ```sql
  SELECT LAST_NAME, (SYSDATE-HIRE_DATE) / 7 AS WEEKS
  FROM EMPLOYEES
  WHERE DEPARTMENT_ID = 90;
  ```

  

### DATE FUNCTIONS

* DATE-MANIPULATION FUNCTIONS
  * MONTHS_BETWEEN(date1, date2)
  * ADD_MONTHS(date, n)
  * NEXT_DAY(date, 'char')
    * next_day(date, 'friday') : 이 date이 후에 첫 금요일
  * LAST_DAY(date)
    * 그 달의 마지막 날
  * ROUND
    * round(sysdate, 'month') : 한 달 단위로 반올림
  * TRUNC



## CHAPTER 5. USING CONVERSION FUNCTIONS AND CONDITIONAL EXPRESSIONS

* TO_CHAR, TO_NUMBER, TO_DATE
* SELECT 문에 조건절 적용하기



### IMPLICIT AND EXPLICIT DATA TYPE CONVERSION(절대적인 형변환)

* implicit data type conversion(절대적인 데이터 형변환)
  * varchar2 or char <=> number
  * varchar2 or char <=> date



* explicit data type conversion(명확한 데이터 형변환)
  * number -> character: to_char
  * character -> date : to_date
  * character -> number : to_number
  * date -> character: to_char



### TO_CHAR, TO_DATE, TO_NUMBER FUNCTIONS

* to_char

  * to_char(date,'format_model')

  * 포맷 모델의 특징
    * ' '로 감싸져있어야함
    * 대소문자 구분필수
    * 유효한 날짜 포맷 요소를 표현할 수 있음
    * 공백은 자동적으로 사라짐
    * 이 때 중간에 글자를 넣고 싶다면 쌍따옴표로 감싸야함
    * fm표기법 존재
      * 숫자 -> 문자 시, 첫 번째 자리에 0이있을 때 0생략되어 표출되는 경우가 많음
      * fm: 좌우 공백 제거
      * 9: 가변적인 값으로 0이거나 숫자가 없을 시 값을 버린다
      * 0: 고정적인 값으로 변환된 숫자의 길이를 맞추고 싶으면 원하는 길이만큼 0으로 채워줌
      * ex)
        * TO_CHAR(0.123, 'FM999.9999') => .123
        * TO_CHAR(0.123,' FM000.000') => 000.123
        * TO_CHAR(0.1230, 'FM000.000') => 000.123
    
  * TO_CHAR를 날짜에 적용할 떄 

     ```SQL
     SELECT EMPLOYEE_ID, TO_CHAR(HIRE_DATE, 'MM/YY') MONTH_HIRED
     FROM EMPLOYEES
     WHERE LAST_NAME = 'Higgins';
     
     SELECT LAST_NAME, TO_CHAR(HIRE_DATE, 'fmDdepth "of" Month YYYY fmHH:MI:SS AM') HIRE_DATE
     FROM EMPLOYEES;
     ```

  * TO_CHAR를 숫자에 적용할 떄 

    ``` SQL
    SELECT TO_CHAR(SALARY, '$99,999.00') SALARY
    FROM EMPLOYEES
    WHERE LAST_NAME = 'Ernsr';
    ```

    * 9: 가변적인 값 -> 있으면 쓰는거고 없으면 없는것임
    * 0: 고정적인 값 -> 없더라고 무조건 표기
    * $: 달러 표시

* TO_NUMBER AND TO_DATE

  * fx modifier
    * 포맷이 날짜의 포맷과 정확히 일치하는지 체크
    * update 문에서 to_date를 사용하여 데이터를 갱신할 때 기존의 데이터포맷과 동일성여부를 체크
      * -> 일치하는 경우에만 데이터 갱신 가능
      * 데이터의 일관성에 유용

  ```SQL
  SELECT LAST_NAME, HIRE_DATE
  FROM EMPLOYEES
  WHERE HIRE_DATE = TO_DATE('May 24, 1999', 'fxMonth DD, YYYY')
  ```
  
  

### NESTING FUNCTIONS

중첩되어있는 함수들은 가장 안쪽부터 최근 단계까지 올라와서 계산됨

```SQL
SELECT LAST_NAME, UPPER(CONCAT(SUBSTR(LAST_NAME, 1, 8), '_US'))
FROM EMPLOYEES
WHERE DEPARTMENT_ID = 60;
```



### GENERAL FUNCTIONS

* NVL(expr1, expr2)

  * null을 실제값으로 변경

  ```sql
  SELECT LAST_NAME, (SALARY * 12) + (SALARY * 12 * NVL(COMMISION_PCT, 0)) AN_SAL
  FROM EMPLOYEES;
  ```

  

* NLV2(expr1, expr2, expr3)

  * expr1이 null 이 아니면 expr2가 되고
  * null이면 expr3

  ```SQL
  SELECT LAST_NAME, SALARY, NVL2(COMMISION_PCT, 'SAL+COMM', 'SAL') INCOME
  FROM EMPLOYEES;
  ```

  

* NULLIF(expr1, expr2)

  * 두 expr을 비교해서 같으면 null, 같지 않으면 expr1

  ```SQL
  SELECT NULLIF(LENGTH(FIRTS_NAME), LENGTH(LAST_NAME)) 
  FROM EMPLOYEES;
  ```

  

* COALESCE(expr1, expr2, ..., exprn)

  * expr들 중에 처음으로 null이 아닌 값을 반환

  ```SQL
  SELECT LAST_NAME, EMPLOYEE_ID, COALESCE(TO_CHAR(COMMISSION_PCT), TO_CHAR(MANAGER_ID), 'NO')
  FROM EMPLOYEES;
  ```

  

### CONDITIONAL EXPRESSIONS

* CASE 

  * CASE WHEN .. THEN

    ​		  WHEN .. THEN

    ​          ELSE

    END

  * ```SQL
    SELECT CASE JOB_ID WHEN 'IT_PROG' THEN 1.10*SALARY
    				   WHEN 'ST_CLERK' THEN 1.15*SALARY
    	   ELSE SALARY
    	   END
    FROM EMPLOYEES;
    ```

    

* DECODE

  * IF- THEN -ELSE와 유사한 구문

  * decode(해당 변수명, 해당 변수명이 그 값이라면, expr1, 해당 변수명이 이 값이라면, expr2)

  * ```SQL
    SELECT DECODE(JOB_ID, 'IT_PROG', 1.10*SALARY,
                 		  'ST_CLERK'. 1.15*SALARY,
                 SALARY)
    FROM EMPLOYEES
    ```

    

## CHAPTER 6. REPORTING AGGREGATED DATA USING THE GROUP FUNCTIONS

* GROUP  함수
* HAVING 절



### GROUP FUNCTIONS

* group 힘수: 한 그룹 당 하나의 결과를 주기 위해 행의 세트를 작동한다
  * 그룹 함수의 종류
    * avg, count, max, min, stddev, sum, variance
    *  null 값은 모두 무시



* syntax

  ```sql
  SELECT GROUP_FUNCTION(COLUMN), ..
  FROM TABLE
  [WHERE CONDITION];
  ```

  

* DISTINCT

  * 중복을 없앤 값들만을 대상으로 GROUP BY 함수 실행

    ```SQL
    SELECT COUNT(DISTINCT DEPARTMENT_ID)
    FROM EMPLOYEES;
    ```

* NVL

  * NVL과 같이 NULL을 포함한 값을 핸들링할 수 있는 함수를 사용할 수도 있음

    ```SQL
    SELECT AVG(NVL(COMMISION_PCT, 0))
    FROM EMPLOYEES;
    ```

    

### GROUPING ROWS

이전까지는 하나의 큰 테이블로 생각했다면, GROUP BY  함수를 사용한다면 작은 그룹으로 나눌 수 있음



```SQL
SELECT COLUMN, GROUP_FUNCTION(COLUMN)
FROM TABLE
[WHERE CONDITION]
[GROUP BY GROUP_BY_EXPRESSION]
[ORDER BY COLUMN];
```



* illegal queries using group functions

  * group 함수를 쓰려면 group by가 반드시 있어야함

    ```sql
    SELECT DEPARTMENT_ID, COUNT(LAST_NAME)
    FROM EMPLOYEES;
    
    => 에러!
    ```

  * GROUP_BY 로 설정한 변수 외에 다른 컬럼을 SELECT 절에 놓으면 안됨

    ```SQL
    SELECT DEPARTMENT_ID, JOB_ID, COUNT(LAST_NAME)
    FROM EMPLOYEES
    GROUP BY DEPARTMENT_ID;
    
    => 에러!
    ```



* 하면 안되는 SQL 문!
  * 그룹을 제한하기 위해서는 WHERE 절을 쓸수 없다
  * 대신, HAVING 절을 사용할 수 있다
  * WHERE 절에 GROUP 함수를 쓸수 없다 EX) AVG, SUM, ...



* having 절

  * 행이 그룹핑 되어있고
  * 그룹 함수가 적용되고
  * having에 맞는 그룹들이 보여짐

  ```sql
  SELECT DEPARTMENT_ID, MAX(SALARY)
  FROM EMPLOYEE
  WHERE CONDITION
  GROUP BY GROUP_BY_EXPRESSION
  HAVING MAX(SALARY) > 10000;
  ORDER BY COLUMN;
  ```

  

### NESTING GROUP FUNCTIONS

중첩된 그룹 함수는 GROUP BY 가 필수적임

```SQL
SELECT MAX(AVG(SALARY))
FROM EMPLOYEES
GROUP BY DEPARTMENT_ID;
```



## CHAPTER 7. DISPLAYING DATA FROM MULTIPLE TABLES USING JOINS

### TYPES OF JOINS AND ITS SYNTAX

* 두 개이상의 테이블에서 데이터를 얻기 위해서는 JOIN을 써야함

* 두 개이상의 테이블에 있는 열 이름들의 권한을 주기 위해서 테이블 명명을 사용해야함
* table 명이 아닌 alias를 사용
* 다른 테이블에 같은 이름이 있을 때는 column alias를 사용



### NATURAL JOIN

두개의 테이블 사이에 같은 열의 이름이 있는 모든 열을 기준으로 병합

```sql
SELECT DEPARTMENT_ID, DEPARTMENT_NAME, LOCATION_ID, CITY
FROM DEPARTMENTS
NATURAL JOIN LOCATIONS;
```

WHERE절로 다른 제약 조건을 추가할 수 있음



### JOIN WITH THE USING CLAUSE

natural join과 상호 배타적인 절

만약 몇몇개의 열이 같은 이름을 갖고 있지만 데이터 타입이 다르다면, 조인을 위해 열들을 구체화하는 using 절을 사용

```SQL
SELECT EMPLOYEE_ID, LAST_NAME, LOCATION_ID, DEPARTMENT_ID
FROM EMPLOYEES JOIN DEPARTMENTS
USING (DEPARTMENT_ID);
```

DEPARTMENT_ID가 두테이블에 있어서 그 열을 기준으로 병합



using 절에 사용되는 컬럼에는 alias를 하면 안됨

```SQL
SELECT L.CITY, D.DEPARTMENT_NAME
FROM LOCATIONS L
JOIN DEPARTMENTS D
USING (LOCATION_ID)
WHERE D.LOCATION_ID = 1400;

=> 에러!
```



```SQL
SELECT L.CITY, D.DEPARTMENT_NAME
FROM LOCATIONS L
JOIN DEPARTMENTS D
USING (LOCATION_ID)
WHERE LOCATION_ID = 1400;

=> 정상
```



### JOIN WITH THE ON CLAUSE

조인 조건을 명확하게 하기 위해 on 절을 사용. 

where 절에 있는 조건들과 명확하게 구분할 수 있음!



```SQL
SELECT E.EMPLOYEE_ID, E.LAST_NAME, E.DEPARTMENT_ID, D.DEPARTMENT_ID, D.LOCATION_ID
FROM EMPLOYEES E
JOIN DEPARTMENTS D
ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID);
```



3개 테이블을 JOIN할 수 있음

```SQL
SELECT EMPLOYEE_ID, CITY, DEPARTMENT_NAME
FROM EMPLOYEES E
JOIN DEPARTMENT D
ON D.DEPARTMENT_ID = E.DEPARTMENT_ID
JOIN LOCATIONS L
ON D.LOCATION_ID = L.LOCATION_ID;
```

E와 D 먼저 JOIN => E, D와 L 순차적으로 JOIN



다른 조건을 또 부여할 수 있음 - AND, WHERE 조건 등(AND과 WHERE 조건 모두 결과는 동일하게 나옴)

```SQL
SELECT E.EMPLOYEE_ID, E.LAST_NAME, E.DEPARTMENT_ID, D.DEPARTMENT_ID, D.LOCATION_ID
FROM EMPLOYEES E
JOIN DEPARTMENTS D
ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID)
WHERE E.MANAGER_ID = 149;
```



### SELF JOIN

* ON 절을 사용한 SELF JOINS

  ```SQL
  SELECT WORKER.LAST_NAME EMP, MANAGER.LAST_NAME MGR
  FROM EMPLOYEES WORKER JOIN EMPLOYEES MANAGER
  ON (WORKER.MANAGER_ID = MANAGER.EMPLOYEE_ID);
  ```

  괄호는 사용하고 싶으면 사용해도 되고, 생략도 가능!



### NONEQUIJOINS

두 개의 테이블 간에 칼럼 값들이 서로 정확하게 일치하지 않는 경우에 사용

```SQL
SELECT E.LAST_NAME, E.SALARY, J.GRADE_LEVEL
FROM EMPLOYEES E
JOIN JOB_GRADES J
ON E.SALARY BETWEEN J.LOWEST_SAL AND J.HIGHEST_SAL;
```

J 테이블의 LOWEST_SAL, HIGHEST_SAL 사이에 있는 값들을 기준으로 병합



### OUTER JOIN

* INNER JOINS VS OUTER JOINS
  * INNER JOINS
    * 두 테이블 간에 맞는 행만을 반환하는 것
  * OUTER JOINS
    * INNER JOINS의 결과도 반환하면서 왼쪽 (OR 오른쪽) 테이블에서 MATCH되지 않은 행을 반환하는 것이 왼(오) OUTER JOIN이라고함
    * 왼쪽 오른쪽 모든 테이블의 값을 반환하는 것이 FULL OUTER JOIN 



* LEFT OUTER JOIN

  ```SQL
  SELECT E.LAST_NAME, E.DEPARTMENT_ID, D.DEPARTMENT_NAME
  FROM EMPLOYEES E
  LEFT OUTER JOIN DEPARMTMENTS D
  ON (E.DERPARTMENT_ID = D.DEPARTMENT_ID);
  ```

  LEFT TABLE이 EMPLOYEES인데 EMPLOYEES 테이블에 있는 모든 행이 나옴!

  DEPARTMENTS 테이블에 맞지 않더라도!



* RIGHT OUTER JOIN

  ```SQL
  SEELECT E.LAST_NAME, D.DEPARTMENT_ID, D.DEPARTMENT_NAME
  FROM EMPLOYEES E
  RIGTH OUTER JOIN DEPARTMENTS D
  ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID);
  ```

  오른쪽 테이블인 DEPARTMENTS 테이블의 모든 행이 다 나옴



* FULL OUTER JOIN

  ```SQL
  SELECT E.LAST_NAME, D.DEPARTMENT_ID, D.DEPARTMENT_NAME
  FROM EMPLOYEES E
  FULL OUTER JOIN DEPARTMENTS D
  ON (E.DEPARTMENT_ID = D.DEPARTMENT_ID);
  ```

  서로 각자의 테이블이 매치되는 행이 없더라도 EMPLOYEES, DEPARTMENTS의 모든 행이 다 나옴!



### CARTESIAN PRODUCT(카티션곱)

CROSS JOIN = CARTESIAN PRODUCT



조인 조건절을 적지 않는 경우 해당 테이블에 대한 모든 데이터를 가져오는 현상

즉, 조인 쿼리 중에 WHERE 절 혹은 JOIN 조건절이 잘못 기술되었거나 아예 없을 때 발생/ WHERE 절에 조인 조건을 주지 않을 수도 있음!

=> 두 테이블 간의 관계에서의 모든 경우의 수를 합쳐 테이블로 출력!



* 카티션 곱 후의 튜플(행)의 수 = 각 테이블의 곱
* 카티션 곱 후의 속성(컬럼)의 수 = 각 테이블의 속성들을 더한 것

```SQL
SELECT LAST_NAME, DEPARTMENT_NAME
FROM EMPLOYEES
CROSS JOIN DEPARTMENTS;
```



## CHAPTER 8. USING SUBQUERIES TO SOLVE QUERIES

### SUBQUERY: TYPES, SYNTAX, AND GUIDELINES

A의 월급보다 더 월급을 많이 받는 사람은 누구냐 는 것에 대해 찾아볼 때 

1. A의 월급을 찾아봐야하고
2. 그보다 많은 월급을 받는 사람을 찾는 것!

다른 쿼리 안에 한 쿼리를 위치시켜야 하므로!



서브 쿼리(이너 쿼리)는 메인 쿼리(아우터 쿼리) 이후에 실행

서브쿼리의 결과는 메인 쿼리에 의해 사용됨



* 서브 쿼리가 사용될 수 있는 곳
  *  WHERE절
  * HAVING 절
  * FROM 절



```SQL
SELECT LAST_NAME, SALARY
FROM EMPLOYEES
WHERE SALARY > (SELECT SALARY FROM EMPLOYEES WHERE LAST_NAME = 'A');
```



* 서브 쿼리 사용 방법
  *  서브 쿼리를 괄호로 감싸야함
  * 가독성을 위해 비교 조건 오른쪽에 서브 쿼리를 두어야함
  * 단일 행 서브쿼리에는 단일 행 연산자를 사용할 수 있고 멀티 행 서브쿼리에는 멀티 행 연산자 사용 가능



### SINGLE-ROW SUBQUERIES

* 한 행만 반환함

  * = > >= < <= <> 의 단일 행 비교 연산자 사용

  ```SQL
  SELECT LAST_NAME, JOB_ID, SALARY
  FROM EMPLOYEES
  WHERE JOB_ID = (SELECT JOB_ID FROM EMPLOYEES WHERE LAST_NAME='TAYLOR')
  AND SALARY > (SELECT SALARY FROM EMPLOYEES WHERE LAST_NAME='TAYLOR');
  ```

  

* 그룹 함수도 사용 가능

  ```SQL
  SELECT LAST_NAME, JOB_ID, SALARY
  FROM EMPLOYEES
  WHERE SALARY = (SELECT MIN(SALARY) FROM EMPLOYEES);
  ```

  

* 서브쿼리에 HAVING 절 쓰기

  ```SQL
  SELECT DEPARTMENT_ID, MIN(SALARY)
  FROM EMPLOYEES
  GROUP BY DEPARTMENT_ID
  HAVING MIN(SALARY) > (SELECT MIN(SALARY) FROM EMPLOYEES WHERE DEPARTMENT_ID = 50) ;
  ```

   

* 주의할 점!

  * 서브쿼리가 단일인지 멀티 행인지 알아보고 그 타입에 따라 연산자를 사용하는 것이 중요!

    ```SQL
    SELECT EMPLOYEE_ID, LAST_NAME
    FROM EMPLOYEES
    WHERE SALARY = (SELECT MIN(SALARY) FROM EMPLOYEES GROUP BY DEPARTMENT_ID);
    ```

    이 때 잘 썼다고 생각했는데 서브쿼리에 의해서 두 행 이상이 출력된다면 한 행 연산자인 = 이 성립되지 않아 에러가 뜸!

  * INNER 쿼리에 의해 행이 반환되지 않을수도 있음



### MULTIPLE-ROW SUBQUERIES

한 개 이상의 행을 반환함

이 때는 multiple-row 비교 연산자를 사용 : in, all, any

```SQL
SELECT LAST_NAME, SALARY, DEPARMENT_ID
FROM EMPLOYEES
WHERE SALARY IN (SELECT MIN(SALARY) FROM EMPLOYEES GROUP BY DEPARTMENT_ID);
```



### USING THE EXISTS OPERATOR

```SQL
SELECT EMPLOYEE_ID, SALARY, LAST_NAME
FROM EMPLOYEES M
WHERE EXISTS (SELECT EMPLOYEE_ID FROM EMPLOYEES W WHERE (조건));
```

 MULTIPLE 행 서브쿼리에 많은 값이 반환된다면 EXIST 사용가능



### NULL VALUES IN A SUBQUERY

**주의사항**

NULL과 비교하는 것은 항상 NULL만 나옴!

그래서 NULL 값이 있는 서브쿼리에서 NOT  IN을 쓰면 NULL 값이 나와서 아무 값도 나오지 않음

```SQL
SELECT LAST_NAME
FROM EMPLOYEE
WHERE EMPLOYEE_ID
NOT IN (SELECT MANAGER_ID FROM EMPLOYEES WHERE MANAGER_ID IS NOT NULL);
```

