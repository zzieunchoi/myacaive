# SQL 추가 사항

## DML, DCL, DDL, TCL

* DML(데이터 조작어)
  * 정의 및 특징
    * 데이터베이스의 데이터를 관리하는데 사용 -> 자동으로 커밋 X
      * 데이터 베이스에 영구적이지 않으므로 롤백 가능
  * select
  * insert
  * update
  * delete
* DDL(데이터 정의어)
  * 정의 및 특징
    * 데이터 베이스 스키마를 정의하거나 조작하기 위해 사용
    * 직접 데이터베이스의 테이블에 영향을 미치기 때문에 DDL 명령어를 입력하는 순간, 작업이 즉시 완료 (AUTO COMMIT)
  * CREATE
  * ALTER
  * DROP
  * RENAME
  * TRUNCATE
* DCL(데이터 제어어)
  * 정의 및 특징
    * 데이터를 제어하는 언어
    * 데이터의 보안, 무결성, 회복, 병행 수행 제어 등을 정의하는데 사용
    * 직접 데이터베이스의 테이블에 영향을 미치기 때문에 DDL 명령어를 입력하는 순간, 작업이 즉시 완료 (AUTO COMMIT)
  * GRANT
  * REVOKE
* TCL(트랜잭션 제어어)
  * 정의 및 특징
    * DCL에서 트랜잭션을 제어하는 명령인 COMMIT과 ROLLBACK만들 따로 분리해서 표현
    * 데이터의 보안, 무결성, 회복, 병행 수행제어 등을 정의하는데 사용
  * COMMIT
    * 트랜잭션의 작업 결과를 반영
  * ROLLBACK
    * 트랜잭션의 작업을 취소 및 원래대로 복구
  * SAVEPOINT



## 옵티마이저 

* 옵티마이저
  * SQL을 수행할 최적의 처리 경로를 생성해주는 DBMS의 핵심 엔진
  * 개발자가 SQL를 작성 -> 옵티마이저에서 쿼리문을 어떻게 실행시킬지 여러가지 실행계획을 세움
  * 그 실행계획에 따라 쿼리를 수행
  * 종류
    * 규칙기반 옵티마이저
      * 사전에 정의된 규칙 기반
    * 비용기반 옵티마이저
      * 최소 비용 계산 실행계획 수립



* 플랜
  * 옵티마이저는 주어진 환경 하에서 최적의 실행계획(플랜)을 제공
    * 그러나 가끔 이 플랜이 성공적이지 않을 수도 있음
      * 따라서 플랜 이해, 비교, 변경 할 수 있어야함



## PK와 UK(유니크 키)

* PK
  * KEY에 해당하는 컬럼
  * 해당 테이블의 식별자 역할을 하는 제약조건으로 테이블에 하나만 설정할 수 있는 키
  * 테이블의 각 레코드를 구별할 수 있는 역할
  * 중복 X(데이터의 유일성 보장)
  * NULL값은 절대로 X
* UK
  * 테이블 내 항상 유일해야하는 값
  * 중복 허용 X
  * 해당 컬럼에 입력되는 데이터가 각각 유일하다는 것을 보장하기 위한 제약조건
  * NULL 값도 허용



## 인덱스

* 인덱스
  * 검색 속도를 높이기 위해 사용하는 하나의 기술
  * FULL SCAN하는게 아니라 색인화 되어있는 인덱스 파일을 검색하여 검색을 빠르게
  * 주의사항
    * 데이터가 순서대로 정렬되어야하는데 INSERT를 사용할 경우 블록에 새로운 데이터가 입력되어야할 경우가 나타남
    * 타 SQL 실행에 악영향
      * 아주 느려질 수 있음



## 트리거

* 트리거

  * 특정 테이블에 insert, delete, update 같은 dml문이 수행됐을 때, 데이터베이스에서 자동으로 동작하도록 작성된 프로그램
  * 사용자가 직접 호출x 
  * 종류
    * 전체 트랜젝션 작업에 대해 발생되는 트리거
    * 각 행에 대해 발생되는 트리거

  ```SQL
  CREATE TRIGGER [트리거명]
  AFTER DELETE
  	ON [테이블명]
  	FOR EACH ROW
  BEGIN
  	조건문
  END
  ```

  

## PARTITION

* PARTITION BY

  * 분석함수를 사용할 때 그룹으로 묶어서 연산 가능
  * GROUP BY 절을 사용하지 않고, 조회된 각 행에 그룹으로 집계된 값을 표시할 때 OVER 절과 함께 PARTITION BY 절 사용!\
  * 데이터가 변형되지 않음

  ```SQL
  분석함수([컬럼]) OVER(PARTITION BY 칼럼1, 칼럼2... [ORDER BY 절][WINDOWING 절])
  
  SELECT RANK() OVER(PARTITION BY JOB ORDER BY SAL) AS RNK
  ```

  

## 프로시저

* 특정한 로직을 처리하고 결과 값을 반환하지 않는 서브 프로그램

* 테이블에서 데이터를 추출해 조작하고 그 결과를 다른 테이블에 다시 저장하거나 갱신하는 일련의 처리할 때 사용

```SQL
CREATE OR REPLACE PROCEDURE 프로시저명
	(매개변수명1 [IN| OUT | IN OUT] 데이터타입 [:= 디폴트값]
    ,매개변수명2 [IN| OUT | IN OUT] 데이터타입 [:= 디폴트값]
    ...
    )
    
IS[AS]
	변수, 상수 등 선언
BEGIN
	실행부
	
[EXCEPTION
	예외처리부]
END [프로시저명];
```

```SQL
EXEC(EXECUTE) 프로시저명(매개변수1값, 매개변수2값, ...);
```



## Number(p, s)

* p: 최대 유효 십진 자릿수 
* s: 소수점에서 최하위 유효 자릿수까지의 자릿수 
* ex)
  * 123.74 => Number(3) => 124(세자리가 유효함)
  * 123.74 => Number(3, 2) => 3자리가 유효한데 소수점이 2째까지 있어야되므로 불가능 에러!
  * 123.74 => Number(7, 1) => 7자리가 유효 소수점은 첫번째까지 가능하기 때문에 둘째자리에서 반올림 => 123.7



## 토드 F4 버튼

테이블 정보 상세 보기

TABLE, VIEW, PROC, FUNCT, PACKAGE를 DESCRIBE

테이블 명 위에 커서를 두고 F4키



## COMMENT

추가 참조를 위해 오브젝트(테이블, 뷰) 정보르 제공할 수 있음 

* 테이블에 COMMENT 설정
  * `COMMENT ON TABLE [테이블명] IS 'TABLE_COMMENT'`
* 컬럼에 COMMENT 설정
  * `COMMENT ON COLUMN[테이블명.컬럼명] IS 'COLUMN_COMMNET'
* COMMENT 삭제
  * `COMMENT ON TABLE [테이블명] IS ''`
* COMMENT 수정
  * `COMMENT ON TABLE [테이블명] IS '수정문자열'`



## JOIN

* INNER JOIN

  * 메인테이블과 조인 테이블에 조인 칼럼의 값이 동시에 존재해야 조회 가능

  ```SQL
  SELECT A.EMPNO, A.ENAME, A.DEPTNO, B.DNAME
  FROM EMP A, DEPT B
  WHERE A.JOB = 'MANAGER'
  AND A.DEPTNO = B.DEPTNO
  ```

* LEFT OUTER JOIN

  * 왼쪽 테이블이 메인 테이블이 됨
  * 조인 테이블의 값이 존재하지 않아도 메인 테이블의 데이터가 조회
  * 조인 테이블의 값을 가져오지 못하면 NULL로 표시

  ```SQL
  SELECT A.EMPNO, A.ENAME, A.DEPTNO, B.DNAME
  FROM EMP A, DEPT B
  WHERE A.JOB = 'MANAGER'
  AND A.DEPTNO = B.DEPTNO(+)
  ```

* RIGHT OUTER JOIN

  * LEFT OUTER JOIN과 비슷하지만 오른쪽 테이블이 메인 테이블이 됨

  ```SQL
  SELECT A.EMPNO, A.ENAME, A.DEPTNO, B.DEPTNO, B.DNAME
  FROM EMP A, DEPT B
  WHERE A.DEPTNO(+) = B.DEPTNO
  AND (A.JOB = 'MANAGER' OR A.JOB IS NULL)
  ```

  

## 앰퍼센드 문자열

문자열에서 날짜열로 전환



앰퍼센드 문자열 - : 문자열과 동일



