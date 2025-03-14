import sys
sys.stdin = open("input.txt", "r")
'''
완전탐색(재귀)으로 풀기 ----------------------------------------------------------------
'''
def planning(month, cost):
    global min_cost

    if cost > min_cost:
        return

    if month > 12:
        if cost < min_cost:
            min_cost = cost
        return
    
    planning(month+1, cost + D1*days[month])
    planning(month+1, cost + M1)
    planning(month+3, cost + M3)
    planning(13, cost + Y1)



T = int(input())
for tc in range(1, T+1):
    D1, M1, M3, Y1 = map(int, input().split()) # 1일, 1달, 3달, 1년
    days = [0] + [*map(int, input().split())]
    min_cost = float('inf')
    planning(1, 0)
    print(f"#{tc} {min_cost}")
    
    
