'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    def special_sort(N, arr):
        for i in range(N - 1):
            if i % 2 == 0:
                max_idx = i
                for j in range(i+1, N):
                    if arr[max_idx] < arr[j]:
                        max_idx = j
                arr[i], arr[max_idx] = arr[max_idx], arr[i]
            elif i % 2 == 1:
                min_idx = i
                for j in range(i+1, N):
                    if arr[min_idx] > arr[j]:
                        min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    result = ' '.join(map(str, special_sort(N, arr)[:10]))
    print(f"#{tc} {result}")
