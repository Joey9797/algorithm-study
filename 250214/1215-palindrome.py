N = int(input())
arr = [input() for _ in range(8)]

mid = N // 2
for r in range(8):
    for c in range(8):
        for i in range(1, mid+1):
            if arr[r][(c+mid) - 1*i] != arr[r][(c+mid) + 1*i]:
                break