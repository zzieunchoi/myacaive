# 연습문제3 풀이
# 2022-03-30


# 전위순회
def preorder(node):
    global Tree, preans
    # 부모
    preans.append(node)
    # 왼쪽 자식
    if len(Tree[node]) >=1:
        preorder(Tree[node][0])
    # 오른쪽 자식
    if len(Tree[node]) ==2:
        preorder(Tree[node][1])
    return


# 중위순회
def inorder(node):
    global Tree, inans
    # 왼쪽 자식
    if len(Tree[node]) >= 1:
        inorder(Tree[node][0])
    # 부모
    inans.append(node)
    # 오른쪽 자식
    if len(Tree[node]) ==2:
        inorder(Tree[node][1])
    return


# 후위순회
def postorder(node):
    global Tree, postans
    # 왼쪽 자식
    if len(Tree[node]) >= 1:
        postorder(Tree[node][0])
    # 오른쪽 자식
    if len(Tree[node]) ==2:
        postorder(Tree[node][1])
    # 부모
    postans.append(node)
    return


E = 12
line = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4,7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

# 트리 만들기
Tree = [[] for _ in range(E+2)]
for i in range(0, len(line), 2):
    Tree[line[i]].append(line[i+1])

# 전위 순회 하기
preans = []
preorder(1)
print(preans)

# 중위 순회 가기
inans = []
inorder(1)
print(inans)

# 후위 순회 가기
postans = []
postorder(1)
print(postans)
