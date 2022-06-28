# 다이나믹 프로그래밍

한번 푼것을 여러번 다시 푸는 비효율적인 알고리즘을 개선시키는 방법



**하나의 문제를 단 한번만 풀도록 하는 알고리즘**



예를들어, 피보나치 수열은

D[15]를 알기 위해서는 D[13], D[14]를 알아야하고

D[14]를 알기 위해서는 D[12], D[13]를 알아야함

재귀적으로 함수를 구현하게 되면 반복적으로 데이터를 계산해야함 

따라서 동일한 데이터를 계속 계산해야함 -> 비효율적



DP는 다음의 가정 하에서 사용가능

1번가정) 큰 문제를 작은 문제로 나눌 수 있음

2번가정) 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일



DP를 사용하지 않은 피보나치 코드

```python
import time

def fibo(x):
    if x == 1 or x == 2:
        return 1

    return fibo(x-1) + fibo(x-2)

for num in range(5, 40, 10):
    start = time.time()
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')
```



DP를 사용한 피보나치 코드

```	python
import time

d = [0] * 50

def fibo(x):
    if x == 1 or x == 2:
        return 1
    # 여기가 중요@
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for num in range(5, 40, 10):
    start = time.time()
    res = fibo(num)
    print(res, '-> 러닝타임:', round(time.time() - start, 2), '초')
```

