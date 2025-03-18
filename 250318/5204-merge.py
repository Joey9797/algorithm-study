import sys
sys.stdin = open('input.txt', 'r')

def merge(left, right):
    global cnt

    result = [0] * (len(left) + len(right))
    i = j = 0
    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result[i+j] = left[i]
            i += 1
        else:
            result[i+j] = right[j]
            j += 1

    while i < len(left):
        result[i+j] = left[i]
        i += 1

    while j < len(right):
        result[i+j] = right[j]
        j += 1

    return result


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
   
    left_lst = merge_sort(left)
    right_lst = merge_sort(right)

    result = merge(left_lst, right_lst)
    return result
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [*map(int, input().split())]
    cnt = 0
    result = merge_sort(arr)
    print(f"#{tc} {result[N//2]} {cnt}")
