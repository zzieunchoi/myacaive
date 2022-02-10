# 6자리 숫자를 받아줘 단, 494335 이런식으로 받아야함
num = int(input()) 
# while-if 문에서 인덱스 에러를 해결하기 위해 list를 10개보다 2개 더 큰 12개짜리 리스트를
blank_list = [0] * 12
# 숫자 6개를 받을건데 그 숫자의 개수를 카운팅해줄거야
for i in range(6):               # 6자리 숫자의 모든 숫자들을 살펴볼게
    # 맨 뒤에 있는 숫자를 받고 리스트의 그 숫자 자리에 1을 추가해줘. 숫자의 개수를 셀거야
    blank_list[num % 10] += 1
    # 그리고 그 숫자는 없애줘 그 숫자를 없애준 후 아직 남아있는 숫자의 마지막 숫자를 이용할게
    num //= 10                   # 얘는 num = num // 10과 같은 수식

# 변수 생성및 초기화
i = 0 
triplet = 0
run = 0

# 총 10번을 진행할거야
while i < 10:
    # * triplet일 경우 구하기
    # 만약 같은 숫자, 즉 숫자의 개수가 3개 이상인 경우
    if blank_list[i] >= 3:
        # triplet 하나 세줬으니까 나머지 숫자들을 살펴볼거야 방금 나온 triplet 제거해
        blank_list[i] -= 3
        # triplet은 하나 추가해줘!
        triplet +=1 

    # * run일 경우 구하기
    # 만약 연속된 숫자, 즉 i번째 i+1번째 i+2번째 숫자 모두 1개 이상인 경우
    if blank_list[i] >=1 and blank_list[i+1] >=1 and blank_list[i+2] >=1:
        # run 하나 세줬으니까 나머지 숫자들을 살펴볼거야 방금 나온 run 제거해
        blank_list[i] -= 1
        blank_list[i+1] -= 1
        blank_list[i+2] -= 1
        # run 하나 세줘야지!
        run +=1
    #10번 초과하면 while문 빠져나가게 한번 할 때마다 i에 1씩 추가해줘
    i += 1

#run과 triplet으로 이루어져있으면 baby_gin 아니면 lose 출력
if run + triplet == 2:
    print('baby_gin')
else:
    print('lose')
