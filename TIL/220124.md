# 데이터 구조

메소드(method) : S.V(): S가 V를 한다 - 메소드는 함수와 비슷하지만 없으면 반환하는 것이 다를 수 있음

ex) list.append(10)

​      string.split()



목차

1. 순서가 있는 데이터 구조: 문자열, 리스트, 튜플
2. 순서가 없는 데이터 구조: 셋, 딕셔너리



## 순서가 있는 데이터구조

### 문자열

- 모든 문자는 str 타입
- '', ""을 활용하여 표기
- immutable 하다: 문자열의 특정부분을 바꿀 수 없음

* 문자열 조회/ 탐색 및 검증 메소드 (is~~ 일 경우에는 True/ False를 반환)

  * s.find(x): x의 **첫번째 위치**를 반환, 없으면 -1을 반환 (첫번째 위치만 반환, 모든 자리의 위치를 알고 싶다면 반복문 사용)

    ``` python
    'apple'.find('p') #1
    'apple'.find('k') #-1
    ```

    

  * s.index(x): x의 첫번째 위치를 반환. 없으면, 오류 발생

    ```python
    'apple'.index('p') #1
    'apple'.index('k') #substring not found
    ```

    

  * s.isalpha(): 알파벳 문자 여부(알파벳만 해당하는 것은 아니고 한글도 가능)

  * s.isupper(): 대문자여부

  * s.islowe(): 소문자여부

  * s.istitle(): 타이틀 형식 여부 , 공백과 ' 뒤에는 대문자로 표현

    ```python
    'Title Title!'.istitle()
    # True
    ```

* 문자열 변경 메소드

  * s.replace(old, new[,count]) : 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

    ```python
    'coone'.replace('o','a') # 'caane'
    'wooooowoo'.replace('o','!',2) # 'w!!ooowoo'
    ```

    

  * s.strip([chars]): 공백이나 특정 문자를 제거

    ``` python
    #문자열을 지정하지 않으면 공백을 제거함
    '     와우!\n'.strip() #'와우!'
    '     와우!\n'.lstrip() #'와우!\n'
    '     와우!\n'.rstrip() #'     와우!'
    '안녕하세요????'.rstrip('?') #'안녕하세요'
    ```

    

  * s.split(sep= None, maxsplit = -1) : 공백이나 특정 문자를 기준으로 분리

    문자열을 특정 단위로 나눠 리스트로 반환

    ```python
    'a,b,c'.split('_') # ['a,b,c']
    'a,b,c'.split(',') # ['a','b','c']
    'a b c'.split() # ['a','b','c']
    ```

    

  * 'separator'.join([iterable]): 구분자로 iterable 합침

    반복가능한 컨테이너 요소들을 구분자로 합쳐 문자열 반환

    반복가능한 컨테이너 요소에 문자열이 아닌 값이 있으면 type error 발생

    ```python
    '!'.join('ssafy') # 's!s!a!f!y'
    ' '.join(['3','5']) # '3 5'
    
    #이건 반복문으로도 가능
    numbers = ['1','2','3']
    for number in numbers:
        print(number, end =' ')
    
    #아니면 join으로 가능
    print(' '.join(numbers))
    
    # 만약 요소가 문자열이 아닌 경우
    numbers = [1,2,3]
    print(' '.join(numbers))
    #type error: sequence item 0: expected str instance, int found -> type error
    #타입에러가 뜬다면
    print(' '.join(map(str, numbers)))
    # 1 2 3 
    ```

  * s.count()
  
  * s.upper() : 모두 대문자
  
  * s.lower():  모두 소문자
  
  * s.swapcase(): 대소문자 변경

### 리스트 메소드 : mutable이기 때문에 리스트 내 요소를 변경 가능

* 리스트 메소드

  * L.append(x) : 리스트 마지막에 항목 x를 추가

    ``` python
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.extend('banapresso')
    print(cafe)
    # ['starbucks','tomntoms','hollys','banapresso']
    ```

    

  * L.insert(i,x) : 리스트 인덱스 i에 항목 x를 삽입

    ``` python
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.insert(0, 'banapresso')
    print(cafe)
    #['banapresso', 'starbucks','tomntoms','hollys']
    
    #리스트 길이보다 큰 i를 집어넣으면 그냥 맨 뒤에다가 추가해줌
    ```

    

  * L.remove(x): 리스트 가장 왼쪽에 있는 항목 x를 제거/ 항목이 존재하기 않을 경우, value error

    ``` python
    numbers = [1,2,3,'hi']
    print(numbers)
    numbers.remove('hi')
    print(numbers)
    #[1,2,3]
    ```

    

  * L.pop(): 리스트 가장 오른쪽에 있는 항목을 반환 후 제거

  * L.pop(i): 리스트의 인데스 i에 있는 항목을 반환 후 제거

    ``` python
    numbers = ['hi',1,2,3]
    print(numbers)
    numbers.pop(0)
    print(numbers)
    #[1,2,3]
    ```

    

  * L.extend(m): 순회형 m의 모든 

    ``` python
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.extend(['coffee'])
    print(cafe)
    # ['starbucks','tomntoms','hollys','coffee']
    
    #만약 append처럼 리스트 형식이 아닌 str으로 넣는다면
    cafe = ['starbucks','tomntoms','hollys']
    print(cafe)
    cafe.extend('coffee')
    print(cafe)
    # ['starbucks','tomntoms','hollys','c','o','f','f','e','e']
    ```

  * L.index(x, start, end): x값을 찾아 해당 index 값 반환/ 없는 경우 value error

    ``` python
    numbers = [1,2,3,4]
    print(numbers)
    print(numbers.index(3))
    # 2
    print(numbers.index(100))
    # value error
    ```

  * L.clear(): 모든 항목 삭제

    ```python
    numbers= [1,2,3]
    print(numbers)
    numbers.clear()
    print(numbers)
    #[]
    ```

    

  * L.count(x): 원하는 값의 개수를 반환

    ```python
    numbers = [1,2,3,1,1]
    numbers.count(1) # 3
    ```

  * L.sort(): 원본 리스트를 정렬함, sorted함수와 비교할 것

    ```python
    a = [100, 10, 1, 5]
    b = [100, 10, 1, 5]
    #1. 메소드 활용 - 리스트.sort()
    print(a.sort()) 
    # None
    print(a) #a.sort 등 메소드를 사용하면 원본 리스트를 정렬하고 none를 return
    # [1, 5, 10, 100]
    
    #2. 함수활용 - sorted(리스트)
    print(sorted(b))
    # [1, 5, 10, 100]
    #원본 리스트는 변경하지 않지만, 정렬된 리스트를 return
    print(b)
    # [100, 10, 1, 5]
    
    #만약 sort를 내림차순으로 해주고 싶다면
    a.sort(reverse = True)
    ```

  * L.reverse(): 순서를 반대로 뒤집음

    ``` python
    numbers = [3,2,5,1]
    result = numbers.reverse()
    print(numbers, result)
    # [1, 5, 2, 3] None
    #numbers를 reverse한거임 result는 none 반환
    ```



### 튜플 메소드 : immutable이기 때문에 튜플 내 요소를 변경 불가능

- 리스트 메소드 중 항목을 변경하는 메소드들을 제외하고 대부분 동일
- 직접 만들어서 쓰는 경우가 x





## 순서가 없는 데이터 구조

### 셋 메소드 : mutable이기 때문에 셋 내 요소를 변경 가능 - 순서 없이, 중복된 값 존재

* 셋 메소드

  * s.copy()

  * s.add(x)

    ```python
    a = {'사과', '바나나', '수박'}
    a.add('딸기')
    print(a)
    # {'사과', '바나나', '딸기','수박'}
    ```

  * s.update

    ``` python
    a = {'사과', '바나나', '수박'}
    a.update(['딸기', '바나나', '참외'])
    print(a)
    # {'바나나', '사과', '참외', '수박', '딸기'}
    ```

    
  
  * s.pop(): 임의의 원소를 제거해 반환

    ``` python
    a = {'사과', '바나나', '수박'}
    a.pop()
    print(a)
    # {'바나나', '수박'}
    ```
  
    
  
  * s.remove(elem): 셋에서 삭제하고, 없으면 key error
  
    ``` python
    a = {'사과', '바나나', '수박'}
    a.remove('사과')
    # {'바나나', '수박'}
    a.remove('메론')
    # keyerror
    ```
  
  * s.discard(elem): 셋에서 삭제하고 없어도 에러가 발생하지 않음
  
    ``` python
    a = {'사과', '바나나', '수박'}
    a.discard('사과')
    # {'바나나', '수박'}
    a.remove('메론')
    # {'바나나', '수박'}
    ```
  
    



### 딕셔너리 메소드

* d.keys(): 딕셔너리의 모든 키를 담은 뷰를 반환

* d.values() : 딕셔너리의 모든 값을 담은 뷰를 반환

* d.items(): 딕셔너리의 모든 키 - 값의 쌍을 담은 뷰를 반환

* d.get(k) : 키의 값을 반환하는데, 키가 딕셔너리에 없을 경우 none 반환

  ``` python
  my_dict = {'apple':'사과', 'banana' :'바나나'}
  print(my_dict.get('pineapple')) #None
  print(my_dict.get('pineapple',0)) #0
  
  d.get(k,v): 키의 값을 반환하는데, 키가 딕셔너리에 없을 경우 v 반환
  ```

* d.pop(k): key가 딕셔너리에 있으면 제거하고 해당 값을 반환/ 그렇지 않으면 default 반환/ default 값이 없으면 key error

  ``` python
  my_dict = {'apple':'사과', 'banana':'바나나'}
  data = my_dict.pop('pineapple',0)
  print(data, my_dict)
  
  d.pop(k,v): 키값을 반환하고 키인 항목을 딕셔너리에서 삭제하는데, 키가 딕셔너리에 없을 경우 v반환
  ```

* d.update([other]): 값을 제공하는 key, value로 덮어씀

  ``` python
  my_dict = {'apple':'사', 'banana':'바나나'}
  my_dict.update(apple = '사과')
  print(my_dict)
  #{'apple':'사과', 'banana':'바나나'}
  ```

  



### ★ pop(list: 마지막 or index / set: 랜덤(임의의), dictionary: key)

더 많고 자세한 메소드 : [파이썬 자습서 - 자료구조](https://docs.python.org/ko/3/tutorial/datastructures.html)

개발자의 수준 분류 - [d2 - naver](https://d2.naver.com/news/3435170)



## 얕은 복사와 깊은 복사

복사 방법: 할당(assignment), 

* 할당

  * 대입 연산자 (=)

    ```python
    original_list = [1,2,3]
    copy_list = original_list
    copy_list[0] = 'hello'
    print(original_list, copy_list)
    # ['hello', 2, 3], ['hello', 2, 3]
    # ???? original_list와 copy_list는 같은 객체를 참조하기 때문에 copy_list를 바꿔도 original_list도 바뀜!
    
    #같은 객체를 참조하지 않도록 하려면 어떻게 해야할까? 얕은 복사
    original_list = [1,2,3]
    copy_list = original_list[:] #리스트 슬라이싱, 0부터 끝까지 슬라이싱 해서 변수에 넣기 때문에 다른 객체를 참조하게 됨
    copy_list[0] = 'hello'
    print(original_list, copy_list)
    # [1, 2, 3] ['hello', 2, 3]
    
    #또는
    original_list = [1,2,3]
    copy_list = list(original_list)
    copy_list[0] = 'hello'
    print(original_list, copy_list)
    # [1, 2, 3] ['hello', 2, 3]
    ```

    

* 얕은 복사 주의사항: [:]등 방법을 통해서 얕은 복사를 했지만 주소가 참조 된 주의사항 

  * 1차원일 때는 얕은 복사만 충분

  * 복사하는 리스트의 원소가 주소를 참조하는 경우

    ``` python
    a = [1, 2, ['a','b']]
    b = a[:]
    print(a, b)
    b[2][0] = 0
    print(a, b)
    # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
    ```

  * 그러나 2차원일 때는 깊은 복사가 필요



* 깊은 복사(deep copy) 

  ```python
  import copy
  a = [1, 2, ['a', 'b']]
  b = copy.deepcopy(a)
  print(a,b)
  b[2][0] = 0
  print(a,b)
  # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
  ```





# 디버깅

조건과 반복, 함수에서 가장 많은 제어가 필요!

조건문에서 중점적으로 봐야하는 것은 내가 작성한 조건문이 모든 조건을 커버하는지! and 조건을 잘 판단하고 있는지!



### 문법 에러(syntax error)

- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 때 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿 기호(^) 표시
- invalid syntax: 유효하지 않은 문법
- assign to literal: 특정 고유한 값들에 해당할 수 없어
- EOL(End Of Line)/ EOF(End Of File)



### 예외

- 문장이나 표현식이 문법적으로 올바르더라도 실행 도중 예상치 못한 상황을 맞이하면 발생
- zerodivision error: 0으로 나눌라함
- name error: namespace상에 이름이 없는 경우(이름 오타, 잘못된 명령)
- type error: 타입 불일치 ex) str + int, round('str')
- argument 누락
- IndexError - 인덱스가 존재하지 않거나 범위를 벗어나는 경우
- KeyError - 해당 키가 존재하지 않는 경우
- ModuleNotFoundError - 존재하지 않는 모듈을 import하는 경우
- ImportError - Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우



### 예외처리 (수정)

* try문: 오류가 발생할 가능성이 있는 코드를 실행/ 예외가 발생되지 않으면, except 없이 실행 종료

  ```python
  try: #예외없는 정상종료
      try 명령문
  except 예외그룹-1 as 변수-1: #예외처리 할경우 
      예외처리 명령문 1
  except 예외그룹-2 as 변수-2:
      예외처리 명령문 2
  finally: # 예외처리 하지 못한경우 
      finally 명령문
      
  try:
      num = input('숫자입력 :')
      print(int(num))
  except ValueError:
      print('숫자가 입력되지 않았습니다.')
  ```

  

* as 예외처리

  ``` python
  try:
      empty_list = []
      print(empty_list[-1])
  except ValueError as e:
      print(f'{e}, 오류가 발생했습니다.')
  ```

  

* 복수의 예외 처리 실습

  ``` python
  try:
      num = input('100으로 나눌 값을 입력하시오: ')
      100/int(num)
  except(ValueError, ZeroDivisionError):
      print("똑바로 입력해줘!")
  
  try:
      num = input('값을 입력하시오: ')
      100/int(num)
  except ValueError:
      print('숫자를 넣어주세요.')
  except ZeroDivisionError:
      print('0으로 나눌 수 없습니다.')
  except:
      print('에러는 모르지만 에러가 발생하였습니다.')
  ```
  
  

if, else와 똑같은거 아닌가요??

if, else는 오류가 발생하면 멈추지만 try, except는 예외를 발생시키지 않고 처리할 수 있도록 도와줌!





### 예외 발생시키기

* raise statement : 실제 프로덕션 코드에서 활용(파이썬을 만들어낼 때)

  : raise <표현식>(메시지)

  ```python
  raise ValueError('값 에러 발생')
  ```

  

* assert : 특정 조건이 거짓이면 발생, 디버깅 및 테스트에서 활용

​       : assert <표현식>, <메시지> #false인 경우 assertion error

``` python
assert len([1,2]) == 1, '길이가 1이 아닙니다'
```

