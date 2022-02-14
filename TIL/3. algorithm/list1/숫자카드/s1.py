# 4834 숫자카드 풀이
# 2022-02-10

#테스트 케이스 개수 세줘!
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리할게
for t in range(1, T + 1):
    #카드 장수 세줘
    N = int(input())
    #카드 뽑은 거 가져와줘
    cards = int(input())
    # 무슨 카드를 뽑을 건지 리스트로 만들거야 0~9까지의 카드에서 뽑을 거니까 10개의 리스트를 만들어줘
    count_list = [0] * 10
    #뽑은 카드 모든 장 수를 살펴볼거야
    for i in range(N):              
        #뽑은 카드의 숫자에 해당하는 자리에 1을 추가해줘 -> 그래야 그 카드 숫자를 몇개 뽑았는지 알 수 잇어!
        count_list[cards % 10] += 1
        cards //= 10
        
    # 카드 몇번이 가장 많은지 count_list에서 가장 큰 숫자를 골라야돼
    max_count = count_list[0]
    for count in count_list:
        if max_count < count:
            max_count = count
    # 그리고 그 가장 많은 카드의 숫자를 인덱스 활용해서 카드의 숫자를 확인할거야
    for i in range(0, 10):
        if count_list[i] == max_count:
            max_number = i
    # 테스트 케이스가 몇번인지, 가장 많이 뽑힌 카드 숫자, 그리고 그 카드의 장 수를 확인해줘!        
    print('#{} {} {}'.format(t, max_number, max_count))