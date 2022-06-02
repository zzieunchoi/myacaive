import sys
sys.stdin = open('input.txt','r')

N= int(input())
for _ in range(N):
    sentence = list(map(str, input().split()))
    sentence_reverse = []
    for i in range(len(sentence)):
        sentence_reverse.append("".join(reversed(sentence[i][::1])))
    print(" ".join(sentence_reverse))