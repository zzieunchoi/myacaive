# 1. 변수 생성 및 input 값을 받을 변수 생성
# 방의 가로길이를 받아줘
N= int(input())
# 쌓여 있는 상자의 개수를 받아줘 단, 7 4 2 0 0 6 0 7 0 이런식으로 받아야됨
numbers = list(map(int, input().split()))
# 낙차의 크기가 가장 큰 것을 받아줄 변수를 생성
max_value = 0

# 2. 가장 큰 낙차를 구해보자
for i in range(0, N):                # 전체 방의 모든 열마다 둘러보자
    cnt = 0                          # 낙차의 크기를 하나씩 추가
    # 왼쪽 상자가 90도 회전했을 때 떨어지기 위해서는 오른쪽 상자가 가로 막고 있으면 안되니까 
    # 왼쪽 상자의 크기와 오른쪽 상자의 크기 비교가 필수!
    for j in range(i+1, N):          
        if numbers[i] > numbers[j]:  # 만약 왼쪽 상자의 개수가 오른쪽 상자의 개수보다 크다면
            cnt +=1                  # 떨어지는 낙차 크기에 1 추가

# 3. 모든 열을 실행한 후에 그 중 가장 큰 낙차의 값을 구하기
    if cnt > max_value:
        max_value = cnt

# 4. answer
print(max_value)