#1208 flatten풀이
#2022-02-10 

import sys
sys.stdin = open('input.txt', 'r')

#전체 테스트 개수 가져오기 이때는 테스트 개수가 따로 지정되지 않아서 10으로 입력
T = 10
#모든 테스트에 대해서
for t in range(1, T+1):
    #dump 횟수를 받고 
    dump = int(input())
    #boxes의 개수를 입력 받음
    boxes = list(map(int, input().split()))
    
    #dump의 개수를 한번 돌릴때마다
    while dump>0:
        #박스의 최대값, 최대값일때의 자리, 최소값, 최소값일 때의 자리를 구하기 위해 변수 초기화
        max_box = boxes[0]
        max_idx = 0
        min_box = boxes[0]
        min_idx = 0
        
        #100개의 자리에 대해서 
        for i in range(0, 100):
            #enumerate를 쓰지 않겠다는 나의 발악
            box = boxes[i]
            #박스의 개수가 최대일 때의 박스의 개수와 그때의 자리
            if box > max_box:
                max_box = box
                max_idx = i
            #박스의 개수가 최소일 떄의 박스의 개수와 그때의 자리
            elif box < min_box:
                min_box = box
                min_idx = i
        
        #최대일 때는 그 때의 박스의 개수를 하나 빼고, 그 상자를 최소인 자리에 넣어줌
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        #그리고 dump한번 했으니까 차감한다~
        dump -=1
    
    # 정답을 내기 위해 최대, 최소 박스의 값을 구하기 위해 변수 초기화 
    max_value = boxes[0]
    min_value = boxes[0]

    # box_list 를 순회하며 최대값과 최소값을 찾음
    for box in boxes:
        if box > max_value:
            max_value = box
        elif box < min_value:
            min_value = box
    
    #최대값의 최소값의 차이 구하기
    diff = max_value - min_value
    
    # 결과값 출력
    print('#{0} {1}'.format (t, diff))