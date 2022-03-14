def f(i, N, K): # i 부분집합에 포함될지 결정할 원소의 개수, N 전체원소개수, k 부분집합의 합
    if i == N:  # 한개의 부분집합 완성
        print(bit, end = ' ')
        for j in range(N):
            if bit[j] == 1:
                s += a[j]
                print(a[j], end = ' ')
        if s==K: #부분집합의 합이 k이면 돌아봐라
            for j in range(N):
                if bit[j] == 1:
                    print(a[j], end = ' ')
            print()
    else:
        bit[i] = 1
        f(i+1, N, K)
        bit[i] = 0
        f(i+1, N, K)
    return

a = [1, 2, 3]
N= len(a)
bit = [0] * N
f(0,3,5)

# i== N: # 더이상 고려할 원소가 없으면
# s> t:  # 고려한 원소릐 합 s가 이미 목표를 초과한다면
# return # 하면 함수를 반복하는 횟수가 줄어듦