# 병합 정렬 중 분할과정
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst)//2

    left1 = merge_sort(lst[:middle])
    right1 = merge_sort(lst[middle:])

    return merge(left1, right1)


# 병합 정렬 중 병합과정
def merge(left1, right1):
    global cnt
    result = []
    if left1[-1] > right1[-1]:
        cnt+=1
    while len(left1)>0 or len(right1)>0:
        if len(left1) >0 and len(right1)>0:
            if left1[0] <= right1[0]:
                result.append(left1[0])
                left1 = left1[1:]
            else:
                result.append(right1[0])
                right1 = right1[1:]
        elif len(left1) > 0:
            result.append(left1[0])
            left1 = left1[1:]
        elif len(right1)> 0:
            result.append(right1[0])
            right1 = right1[1:]
        
    return result