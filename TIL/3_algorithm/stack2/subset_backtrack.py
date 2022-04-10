def backtrack(a, k, input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    # c = [0, 0]
    if k == input:
        process_solution(a,k)
    else:
        k+=1
        ncandidates = construct_candidates(a,k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)


def process_solution(a, k):
    print("(", end = "")
    for i in range(k+1):
        if a[i]:
            print(i, end = " ")
    print(")")

def construct_candidates(a, k , input, c):
    c[0] = True
    c[1] = False
    return 2

MAXCANDIDATES = 100
NMAX = 100
a = [0] * NMAX # a = [0, 0, 0, 0]
backtrack(a, 0, 3)