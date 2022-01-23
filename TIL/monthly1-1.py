# #json 파일을 python으로 가져오는 과정
# problem01 = open('problem01_data.json', encoding = 'utf-8')
# problem_dict = json.load(problem01)

exam_score = dict(python = 50, html = 71, javascript = 83, project = 48)
print(exam_score)

# def max_score(dict):
#     max = 0
#     for i in dict:
#         for j in dict:
#             if dict[j] > dict[i]:
#                 max = dict[j]
#     return max

# print(f'전체 점수 중 최고점: {max_score(exam_score)}')

def over(dict):
    cnt = 0 
    for i in dict:
        if dict[i] >= 60:
            cnt += 1
    return cnt

print(f'전체 점수 중 60점 이상인 과목의 개수: {over(exam_score)}')

