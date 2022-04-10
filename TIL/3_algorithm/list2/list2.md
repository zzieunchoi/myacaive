# list02

## 행렬

2차원 배열: 1차원 list를 묶어놓은 list

2차원 list의 선언: 세로길이(행의 개수), 가로길이(열의 개수)

```python
N= int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
```



## 배열 순회

nxm 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법

1. 행우선순회

``` python
for i in range(n):
    for j in range(m):
        arr[i][j]
```

2. 열우선순회

```python
for i in range(m):
    for j in range(n):
        arr[j][i]
```

3. 지그재그순회

```python
for i in range(n):
    for j in range(m):
        arr[i][j + (m-1-2*j) * (i%2)]
```



### 델타를 이용한 2차 배열 탐색

```python
# arr[i][j]를 이용해서 오른쪽arr[i][j+1] 왼쪽arr[i][j-1] 아래쪽arr[i+1][j] 위쪽arr[i-1][j]을 살펴보자
# arr : NXN 배열 
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for i in range(1, N):
    for j in range(1, N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0<= ni < N and 0 <= nj < N:
                print(arr[ni][nj])
                
# 또 다른 방법
for i in range(1, N):
    for j in range(1, N):
        for di, dj in[(0,1),(1,0), (0,-1), (-1,0)]
            ni = i + di
            nj = j + dj
            if 0<= ni < N and 0 <= nj < N:
                print(arr[ni][nj])

```



### 전치 행렬

```python
for i in range(3):
    for j in range(3):
        if i < j :
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```





## 부분집합

### 부분집합 생성하기

```python
# {1,2,3,4}의 부분집합 생성
A = [1, 2, 3, 4]
bit = [0,0,0,0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                for p in range(4):
                    if bit[p]:
                        print(A[p], end = ' ')
                print()
#4 
#3
#3 4
#2
#2 4
#2 3
#2 3 4
#1
#1 4
#1 3
#1 3 4
#1 2
#1 2 4
#1 2 3
#1 2 3 4
```



### 비트 연산자

&: 비트 단위로 and 연산

|: 비트 단위로 or 연산

<< : 피연산자의 비트 열을 왼쪽으로 이동시킴

'>>': 피연산자의 비트 열을 오른쪽으로 이동시킴

```python
# << 연산자의 경우
1 << n : 2의 n승, 즉, 원소가 n개일 경우의 부분집합
i & (1<<j) : 1 => i에서 j번째 비트가 1인지 아닌지를 리턴함

```



### 비트 연산자를 사용하여 부분집합 간결하게 생성

```python
arr = [3, 6, 7, 1, 5, 4]
n = len(arr)

for i in range(1<<n): # 원소가 n개일 경우의 부분집합을 구할건데
    for j in range(n):  # 모든 n에 대해서
        if i&(1<<j):  # i에서 j번째 비트가 1이라면 
            print(arr[j], end=",") # 그 원소를 내보내줘
    print()
```



## 검색

: 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업 - 목적하는 탐색키를 가진 항목

* 검색의 종류 - 순차 검색, 이진 검색, 인덱싱(해쉬)

  *  순차 검색: 일렬로 되어있는 자료를 순서대로 검색하는 방법 - 순차구조에서 유용

    * 정렬되어있는 자료 / 정렬되어있지 않는 자료의 검색 과정
    * 정렬되지 않았을 때: 첫번째 원소부터 순서대로 검색대상 - 키가 같은 원소가 있는지 비교하여 찾음, 키값이 동일한 원소 찾으면 그 원소의 인덱스  반환

    ```python
    def sequentialSearch(a, n, key):
        i = 0
        while i < n and a[i] != key:
            i= i+1
        if i < n:
            return i
        else:
            return -1 #찾지못함 따로 값이 있는것은 아님
    ```

    * 정렬된 경우: 자료를 순차적으로 검색하면서 키 값을 비교

    ```python
    def sequentialSearch2(a, n , key):
        i = 0
        while i < n and a[i] <key:
            i = i+1
        if i < n and a[i] ==key:
            return i
        else:
            return -1 #찾지못함 따로 값이 있는것은 아님
    ```

  *  이진 검색: 자료의 가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속

    **자료가 정렬된 상태여야함!**

    * 자료의 중앙에 잇는 원소 선택 
    * 목표값< 중앙 원소값: 자료의 왼쪽 반에 대해서 새로 검색 수행
    * 목표값 > 중앙 원소 값: 자료의 오른쪽 반에 대해서 새로 검색 수행

    ```python
    def binarySearch(a, key):
        start = 0
        end = len(a) -1
        while start <= end:
            middle = start + (end -start) //2
            if key == a[middle]:
                return True
            elif key < a[middle]:
                end = middle -1
            else:
                start = middle +1
        return False
    ```

    ``` python
    # 재귀함수 이용하여 이진 검색 구현도 가능
    def binarySearch2(a, low, high, key):
        if low > high:
            return False
        else:
            middle = (low+high)//2
            if key == a[middle]:
                return True
            elif key < a[middle]:
                return binarySearch2(a, low, middle-1, key)
            elif a[middle] < key:
                return binarySearch2(a, middle+1, high, key)
    ```

  * 인덱스



## 정렬

* 셀렉션 알고리즘: 저장되어있는 자료로부터 K번쨰로 큰 혹은 작은 원소를 찾는 방법, 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미

​       셀렉션 선택 과정: 정렬 알고리즘 이용하여 자료 정렬 -> 원하는 순서에 있는 원소 가져오기

``` PYTHON
def select(list,k):
    for i in range(0,k):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[minIndex] > list[j]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list[k-1]
```

* 선택 정렬 의미: 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식, 셀렉션 알고리즘을 전체 자료에 적용한 것

  정렬 과정: 주어진 list 중에서 최소값을 찾고 그 값을 list의 맨 앞에 위치한 값과 교환하고 맨 처음 위치를 제외한 나머지 list를 대상으로 위의 과정 반복

  ```python
  def selectionSort(a):
      for i in range(0, len(a)-1):
          min = i
          for j in range(i+1, len(a)):
              if a[min] > a[j]:
                  min = j
          a[i], a[min] = a[min], a[i]
  ```

  

  버블 정렬과 선택 정렬을 손으로 직접 설명할 수 있는 정도여야함!
