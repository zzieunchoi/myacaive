# 재귀

마이클잭슨 해보기

```python
def gogo(n):
    if n== 17:
        print()
        return
    
    if n != 13:
        print(n, end = ' ')
    gogo(n+2)
    if n != 13:
        print(n, end = ' ')
gogo(3)

# 3 5 7 9 11 15 
# 15 11 9 7 5 3 
```



트리 형태 그려보기

```python
def gogo(n):
    print(n, end = ' ')
    if n== 2:
        return 
    for i in range(2):
        gogo(n+1)
gogo(0)

# 0 1 2 2 1 2 2
```



트리 중간에 print 넣고 출력결과 예상해서 맞추기

```python
def gogo(n):
    if n== 2:
        print(n, end = ' ')
        return 
    for i in range(2):
        gogo(n+1)
gogo(0)

# 2 2 2 2 
```



path 배열(마지막 도착할 때 마다 path 배열 출력)

```python
path = [0]*4
def gogo(lev):
    if lev ==2 :
        for i in range(lev):
            print(path[i], end = ' ')
        print()
        return 
    for i in range(2):
        path[lev] = i
        gogo(lev+1)
        path[lev]= 0

gogo(0)

# 0 0 
# 0 1 
# 1 0
# 1 1        
```



브랜치, 레벨로 원하는 모양으로 출력하기

````
1111
1112
1113
1121
1122
1123
1131
....
3332
3333

으로 출력하기 위해서는 branch, level 각각 몇으로 해야되나?
답: branch : 3, level : 4
````

```python
path = [0]*4
def gogo(lev):
    if lev == 4 :
        for i in range(lev):
            print(path[i], end = '')
        print()
        return 
    for i in range(3):
        path[lev] = i+1
        gogo(lev+1)
        path[lev]= 0

gogo(0)
```



그 이후에 argument 넣는 법 배우기

```python
path = [0] * 10
n = 5

def bbq(lev, sum):
    global path, n
    
    if lev == n:
        for i in range(lev):
            print(path[i], end = ' ')
        print(" = " + str(sum))
        return
    
    for i in range(6):
        path[lev] = i+1
        bbq(lev+1, sum +i +1)
        path[lev] = 0
bbq(0, 0)

# ....
# 6 6 6 5 5  = 28
# 6 6 6 5 6  = 29
# 6 6 6 6 1  = 25
# 6 6 6 6 2  = 26
# 6 6 6 6 3  = 27
# 6 6 6 6 4  = 28
# 6 6 6 6 5  = 29
# 6 6 6 6 6  = 30
```



가지치기

```python
path = [0] * 10
n = 5

def bbq(lev, sum):
    global path, n
    # sum이 7이하만 출력
    if sum > 7:
        return
    if lev == n:
        for i in range(lev):
            print(path[i], end = ' ')
        print(" = " + str(sum))
        return
    
    for i in range(6):
        path[lev] = i+1
        bbq(lev+1, sum +i +1)
        path[lev] = 0
bbq(0, 0)
```



