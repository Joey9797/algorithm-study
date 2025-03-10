# c가 겹치면 안됨
# c에 들어갈 수 있는 애들(r)은 각각 3개씩 있음
# 즉, r도 겹치면 안되고, c도 겹치면 안됨
'''
1
3
9 4 7
8 6 5
5 3 7'''
def min_sum(r, lst):
    if r == N:
         return
    else:
        if r_visited[r] == 0: # c에 집어넣을 애(r) 하나 고름
            r_stack.append(r)
            r_visited[r] = 1
            for c in range(r, N):
                if c_visited[c] == 0: # c 중 하나 고름
                    c_stack.append(c)
                    c_visited[c] = 1
                    lst.append(arr[r][c])
                    min_sum(r+1, lst)                     
                    v = c_stack.pop()
                    c_visited[v] = 0
            # else:
            #     w = r_stack.pop()
            #     r_visited[w] = 0

T = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
r_stack = []
r_visited = [0] * N
c_stack = []
c_visited = [0] * N
ans = 0
value = []
min_sum(0, value)
if len(value) == N:
    s = sum(value)
if ans > s:
    ans = s
print(ans)

