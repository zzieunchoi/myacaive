#4828 min_max 풀이
#2022-02-10

#input.txt 데이터 가져오기
import sys
sys.stdin = open('input.txt', 'r')

#전체 테스트 케이스 가져와바라
T = int(input()) # Test Case

#모든 테스트 케이스 전체를 둘러볼게~
for t in range(1, T+1):
    # 숫자의 개수를 불러와줘!
    N = int(input())
    # 각 테스트 케이스의 숫자들을 불러와줘
    numbers = list(map(int, input().split()))
    
    #min_value를 살펴볼거야 숫자 중에 가장 작은 숫자를 알려줘
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    
    #max_value를 살펴볼거야 숫자 중에 가장 큰 숫자를 알려줘
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    
    #min_value와 #max_value의 차이를 알려줄 변수를 지정하고 그 변수에 값을 넣어줘
    diff = max_value - min_value
    
    #출력할 양식에 맞게 출력할게!
    print('#{} {}'.format(t, diff))