import sys
sys.stdin = open('input.txt', 'r')

# 재료 두 그룹으로 나누기
def pick(i, cnt): # 현재위치 i, 뽑은 개수 cnt
    global result

    if cnt == K:
        food1 = []
        food2 = []
        for i in range(N):
            if bit[i] == 1:
                food1.append(i)
            else:
                food2.append(i)

        food1_sum, food2_sum = sum_score(food1, food2)
        total = abs(food1_sum - food2_sum)
        if total < result:
            result = total
        return 
    
    if i == N:
        return
    
    bit[i] = 1
    pick(i+1, cnt+1)
    bit[i] = 0
    pick(i+1, cnt)

# 각 그룹의 맛(시너지) 합 구하기
def sum_score(lst1, lst2):
    lst1_sum = lst2_sum = 0
    for i in range(K):
        for j in range(K):
            if j == i:
                continue
            lst1_sum += foods[lst1[i]][lst1[j]]
            lst2_sum += foods[lst2[i]][lst2[j]]
    return lst1_sum, lst2_sum    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    K = N//2    # 한 그룹 당 뽑을 음식의 개수
    foods = [[*map(int, input().split())] for _ in range(N)]
    bit = [0]*N
    result = 160000
    pick(0, 0)
    print(f"#{tc} {result}")