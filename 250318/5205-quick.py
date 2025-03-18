import sys
sys.stdin = open('input.txt', 'r')

def partition(left, right):
    global arr

    pivot = arr[left]
    i = left + 1
    j = right
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    return j


def sort(left, right):
    if left < right:
        pivot = partition(left, right)

        sort(left, pivot-1)
        sort(pivot+1, right)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [*map(int, input().split())]
    sort(0, N-1)
    print(f"#{tc} {arr[N//2]}")

