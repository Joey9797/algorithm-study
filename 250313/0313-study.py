N = 6
arr = [1, 2, 3, 4, 5, 6]
M = 3
res = []
def roll_dice(cnt, start):
    if cnt == M:
        print(res)
        return
    
    for i in range(start, N):
        res.append(arr[i])
        roll_dice(cnt+1, i)
        res.pop()
roll_dice(0, 0)