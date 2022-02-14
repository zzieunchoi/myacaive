#4835 구간합
#2022-02-10

import sys
sys.stdin = open('input.txt', 'r')

# Test Case 받아오기
T = int(input())

# for문에서 sum 함수를 써야해서 나의 sum으로 미리 구현
def my_sum(a):
    sum = 0
    for num in a:
        sum += num
    return sum

#전체 test case 사용하기
for t in range(1, T+1):
    # N개의 정수와 M개의 부분합을 받아오기
    N, M = map(int, input().split())
    # N개의 숫자 받아오기
    numbers = list(map(int, input().split()))
    
    # sum을 한꺼번에 모아놓을 빈 리스트 구하기
    sum_list = []
    # 예를 들어 10개의 숫자 중에서 3개씩 묶는 것은 총 8개가 나오므로 일반화 시키면 N개의 숫자 중에서 M개씩 묶으면 N-M+1개가 나옴
    for i in range(0, N-M+1):
        # 부분합을 구해서 sum_list에 넣어주라!
        sum_list.append(my_sum(numbers[i: i+M]))
    # 부분합이 모여있는 sum_list에서 최대값 구하기!
    max_value = sum_list[0]
    for sum in sum_list:
        if max_value < sum:
            max_value = sum
    # 부분합이 모여있는 sum_list에서 최소값 구하기!
    min_value = sum_list[0]
    for sum in sum_list:
        if min_value > sum:
            min_value = sum
    # 최대값과 최소값의 차이 구하기
    diff = max_value - min_value
    # 출력 형식에 맞춰 테스트 케이스 숫자와 최대값과 최소값 차이 구하기
    print('#{} {}'.format(t, diff))
