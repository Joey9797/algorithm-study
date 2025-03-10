def black(i):
    global max_v
    if i == 3:
        sum_cards = sum(picked)
        if sum_cards > M:
            return
        max_v = max(max_v, sum_cards)
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                picked[i] = cards[j]
                visited[j] = 1
                black(i+1)
                visited[j] = 0
            
N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
picked = [0] * 3
visited = [0] * N
max_v = 0
black(0)
print(max_v)

#-----------------------------------------------------------
def black(i, num):
    global max_v
    if i == 3:
        sum_cards = sum(picked)
        if sum_cards > M:
            return
        max_v = max(max_v, sum_cards)
        return
    else:
        for j in range(num + 1, N):
            picked[i] = cards[j]
            black(i+1, j)
            
N, M = list(map(int, input().split()))
cards = list(map(int, input().split()))
picked = [0] * 3
# visited = [0] * N
max_v = 0
black(0, -1)
print(max_v)
