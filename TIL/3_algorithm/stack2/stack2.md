# stack 2

## 계산기

1. 수식을 받아 중위 표기법에서 후위 표기법으로 변환
2. 후위 표기법을 받아 계산하기



#### 1. 수식을 받아 중위 표기법에서 후위표기법으로 변환

1. 수식을 받아온다

2. 숫자를 넣을 string ans 와 연산자를 담을 stack을 만든다

3. 우선순위를 비교할 수 있게 딕셔너리로 만들어준다

4. 연산자라면 스택에 우선순위 비교하여 쌓고 숫자면 string에 넣어준다

   ★ 이때 주의할 사항: 

   스택의 top에 저장되어있는 연산자보다 우선순위가 높으면 스택에 push

   그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop 한후 수식의 연산자 push, top에 연산자가 없으면 push

   `)`이면 스택 top에 왼쪽 괄호가 `(`가 올 때까지 스택에 pop연산을 수행하고 pop한 연산자 출력

ex) (6+5*(2-8)/2) => 6528-`*`2/+

```python
# 수식의 개수 가져오기
N = int(input())
# 수식을 후위표기법으로 변환하기
token = input()

# 수식을 넣을 빈 string 만들기
ans_str = ''
# 빈 스택 만들기
stack = []
# 빈 스택의 마지막 자리인 top을 지정
top = -1

# icp와 isp 우선순위를 지정해주기
icp = {'*':2, '+':1, '(':3, ')': None}
isp = {'*':2, '+':1, '(':0}
# 수식의 모든 연산과 피연산자를 살펴본다
for char in tokens:
    # 만약 연산자라면?
    if char in icp:
        # 만약 닫는 괄호라면?
        if char == ')':
            # 여는 괄호를 만날때까지 
            while stack[top] != '(':
                # 스택의 위에 있는 거를 빼서 ans_str에 하나씩 넣어줘!
                ans_str += stack[top]
                stack.pop()
                top -= 1
                # 여는 괄호를 만나면 뽑아내기 => 즉 끝!
            stack.pop()
            top -= 1
        # 만약 닫는 괄호가 아닌 연산자라면?
        else:
            # 만약 스택이 비어있다면
            if stack == []:
                # 연산자를 스택에 넣어주기
                stack.append(char)
                top += 1
            # 만약 스택이 비어있지 않는다면
            else:
                # 넣으려는 연산자의 icp 우선순위가 스택 가장 위 연산자의 isp 우선순위보다 크다면?
                if isp[stack[top]] < icp[char]:
                    #스택에 넣어줘
                    stack.append(char)
                    top += 1
                #만약 icp우선순위가 isp 우선순위보다 작거나 같다면?
                else:
                    #isp 우선순위가 더 작아질때까지
                    while isp[stack[top]] >= icp[char]:
                        # 스택에서 pop하고 ans_str에 넣음
                        ans_str += stack[top]
                        stack.pop()
                        top -= 1
                    #isp 우선순위가 더 작아진다면 스택에 넣기
                    stack.append(char)
                    top += 1
    # 만약 피연산자라면 그냥 ans_str에 숫자 집어넣기
    else:
        ans_str += char
```



#### 2. 후위 표기법의 수식을 스택을 이용하여 계산

1. 피연산자 만나면 스택에 push

2. 연산자 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산

   연산결과를 다시 스택에 push

3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력

```python
#후위표기법으로 표현된 수식을 계산하기
tokens2 = ans_str
# 후위표기법에 있는 모든 수식을 이용하여
for char2 in tokens2:
    # 피연산자라면
    if char2 not in icp:
        # 스택에 넣기
        stack.append(char2)
        top +=1
    #연산자라면
    else:
        # + 연산자라면
        if char2 == "+":
            # 2개 값 더하기
            oper2 = stack.pop()
            top -= 1
            oper1 = stack.pop()
            top -= 1
            stack.append(int(oper1)+int(oper2))
            top +=1 
        # - 연산자라면
        elif char2 == "-":
            # 2개 값 빼기
            oper2 = stack.pop()
            top -= 1
            oper1 = stack.pop()
            top -= 1
            stack.append(int(oper1)-int(oper2))
        # * 연산자라면
        elif char2 == "*":
            # 2개 값 곱하기
            oper2 = stack.pop()
            top -= 1
            oper1 = stack.pop()
            top -= 1
            stack.append(int(oper1)*int(oper2))
        # / 연산자라면
        elif char2 == "/":
            # 2개 값 나누기
            oper2 = stack.pop()
            top -= 1
            oper1 = stack.pop()
            top -= 1
            stack.append(int(oper1)/int(oper2))
        # 나누기 연산자라면 문제의 조건에 맞춰서 float, int 걸어주기
        
        # 스택의 리스트에는 어차피 답이 하나 밖에 없지만 숫자로 풀어서 쓸 경우 언팩
        print(*stack)
```



## 백트래킹

: 해를 찾는 도중에 막히면 되돌아가서 다시 해를 찾아 가는 기법

깊이우선탐색과는 다르게 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음, 불필요한 경로를 조기에 차단



### 미로 찾기

```python
# 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 길을 찾는 함수 만들기
def my_find(arr, i,j):
    # 4가지 방향에 대하여 
    for k in range(4):
        ni = i
        nj = j
        # 내가 지금까지 지나온 곳은 4로 표시
        arr[ni][nj] = 4
        # 만약 내가 가려고 하는 곳이 3이라면 즉 도착점이라면 경로를 찾은 것이므로 1출력
        if arr[ni + di[k]][nj + dj[k]] == 3:
            return 1
        # 만약 내가 가려고 하는 곳이 0이라면 한칸 진전
        if arr[ni + di[k]][nj + dj[k]] == 0 :
            ni += di[k]
            nj += dj[k]
            # 만약 길을 찾은 곳이 1이라면 1출력
            if my_find(arr, ni, nj) == 1:
                return 1
    return 0


# 테스트케이스
T = int(input())
# 모든 테스트 케이스에대하여 
for t in range(1, T+1):
    # 미로의 개수 받아오기
    N = int(input())
    # 미로 행렬 받아오기 겉은 1로 채워서 빠져나갈 수 없게 만듦
    arr = [[1] + list(map(int, input())) + [1] for _ in range(N)]
    arr = [[1]*(N+2)] + arr + [[1]*(N+2)]
    # 0부터 N+1 행에 대하여 
    for i in range(N+2):
        # 0부터 N+1 열에 대하여 
        for j in range(N+2):
            # 만약 2이라면 즉, 출발점이라면 
            if arr[i][j] == 2:
                #길을 찾는 함수 실행
                print('#{} {}'.format(t, my_find(arr,i,j)))

```



### n-Queen



### map  coloring



### 부분집합의 합 문제 

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    # c = [0, 0]
    if k == input:
        process_solution(a,k)
    else:
        k+=1
        ncandidates = construct_candidates(a,k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def process_solution(a, k):
    print("(", end = "")
    for i in range(k+1):
        if a[i]:
            print(i, end = " ")
    print(")")

def construct_candidates(a, k , input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX 
backtrack(a, 0, 3)
```



### 순열 구하기

```python
def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i] , end = " ")
        print()
    else:
        k+=1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

            
def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX
    
    for i in range(1, k):
        in_perm[a[i]] = True
    ncandidates = 0
    for i in range(1, input+1):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates +=1
    return ncandidates
```

