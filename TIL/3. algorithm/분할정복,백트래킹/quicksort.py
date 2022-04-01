# 퀵정렬 첫번째 방법
def quicksort(lst, l, r):
    if l < r:
        s = partition(lst, l, r)
        quicksort(lst, l, s-1)
        quicksort(lst, s+1, r)
    
# 피봇 정하기
def partition(lst, l, r):
    # 맨왼쪽을 피봇으로 정함
    pivot = lst[l]
    i = l
    j = r
    while i <= j:
        while i <= j and lst[i] <= pivot:
            i+=1
        while i <= j and lst[j] >= pivot:
            j -=1
        if i<j:
            lst[i] , lst[j] = lst[j], lst[i]
    # 피봇과 j서로 바꾸기
    lst[l], lst[j] = lst[j], lst[l]
    return j 


# 퀵 정렬 두번쨰 방법
def partition(target_list, pivot, right):
    x = target_list[right]
    i = pivot - 1
    for j in range(pivot, right):
        if target_list[j] <= x:
            i += 1
            target_list[i], target_list[j] = target_list[j], target_list[i]
    target_list[i+1], target_list[right] = target_list[right], target_list[i+1]
    return i + 1


def quick_sort(target_list, left, right):
    if left < right:
        s = partition(target_list, left, right)
        quick_sort(target_list, left, s - 1)
        quick_sort(target_list, s+1, right)


T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, len(arr)-1)
    print('#{}'.format(t))
    print(arr)