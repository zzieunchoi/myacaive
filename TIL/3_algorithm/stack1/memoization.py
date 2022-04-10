# memoization 구현
# 2022-02-24

def fibo1(n):
    global memo
    if n>= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
        print('# {}'.format(memo))
    return memo[n]

memo= [0,1]

print(fibo1(10))
print(memo)