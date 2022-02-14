#txt파일을 들고 위해 모듈 설치
import sys
# 이번 케이스는 test case가 따로 주어지지 않으므로 text case의 총 개수를 미리 입력함
T = 10
#input.txt파일을 불러오기
sys.stdin = open('input.txt', 'r')  
# 모든 test case를 진행하기 위해 총 10번 for문 실행
for t in range(T):
    #가로 길이 입력하기
    N = int(input())
    # 빌딩의 개수 입력하기
    bds = list(map(int, input().split()))
    
    # 최소한의 view를 알려줄 min_view와 답을 알려줄 count_view 변수 초기화
    min_view = 0
    count_view = 0
    
    #i-2와 i+2의 인덱스 에러를 커버하기 위해 범위를 2부터 N-2까지로 지정 - 모든 가로의 길이의 빌딩 수를 이용하여 
    for i in range(2, N-2):
        #i열에 있는 빌딩이 조망이 좋기 위해서는 i+1, i-1, i-2, i+2의 빌딩의 높이가 i열에 있는 빌딩의 높이보다 낮아야함
        if bds[i] > bds[i-1] and bds[i] > bds[i-2] and bds[i] > bds[i+1] and bds[i] > bds[i+2]:
            # i와 i+1, i-1, i+2, i-2와의 빌딩 높이의 차
            view1 = bds[i] - bds[i-1]
            view2 = bds[i] - bds[i-2]
            view3 = bds[i] - bds[i+1]
            view4 = bds[i] - bds[i+2]
            
            # 빌딩 높이의 차 중에서 위의 조건에 모두 해당되어야 하므로 view1~4중의 최소값을 구해야함
            min_view = view1
            # view1~4까지 최솟값을 구하기
            for view in [view1, view2, view3, view4]:
                if view < min_view:
                    min_view = view
            count_view += min_view
    #각 테스트 케이스마다 테스트케이스 번호와, 조망권이 확보된 세대의 수 출력
    print('#{} {}'.format(t+1, count_view))