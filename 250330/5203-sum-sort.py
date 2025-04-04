import sys
sys.stdin = open('input.txt', 'r')

def split(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_arr = split(left)
    right_arr = split(right)

    result = merge(left_arr, right_arr)
    return result


def merge(left, right):
    global cnt

    if left[-1] > right[-1]:
        cnt += 1
        
    L, R = len(left), len(right)
    result = [0]*L + [0]*R

    l = r = 0
    while l < L and r < R:
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l+r] = right[r]
            r += 1

    while l < L:
        result[l+r] = left[l]
        # if left[l] > right[r-1]:
        #     cnt += 1
        #     print(cnt, result)
        l += 1

    while r < R:
        result[l+r] = right[r]
        r += 1
    
    return result


T =  int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    result = split(lst)
    print(f"#{tc} {result[N//2]} {cnt}")