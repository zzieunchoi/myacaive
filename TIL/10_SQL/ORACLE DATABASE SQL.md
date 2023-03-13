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

    
