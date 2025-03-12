import sys
sys.stdin = open("input.txt", "r")

'''
1. 최댓값과, 최댓값의 위치를 찾는다. 만약 최댓값이 0번에 있지 않다면,
    최댓값이 한개면, 일단 맨 앞자리와 바꾸고 시작한다.
    최댓값이 한개 이상이고, 교환 횟수가 1이면, 역시 맨 앞자리와 바꾸고 시작한다.
    최댓값이 한개 이상이고, 교환 횟수가 2 이상이면,
        앞에서부터 횟수만큼 숫자를 살펴보고, 가장 작은 값과, 가장 오른쪽에 있는 최댓값이랑 바꾼다.
2. 만약 최댓값이 0번에 있다면
    건너뛰고 다음 값들을 본다.
'''

def change_card(change, num_lst):
    global max_p

    if change == M:
        prize = 0
        for n in num_lst:
            prize = prize*10 + n
        max_p = max(prize, max_p)
        return
    
    num = ''.join(map(str, num_lst))
    key = (num, change)
    if key in visited:
        return
    visited[key] = 1
    
    for i in range(N):
        for j in range(i+1, N):
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
            change_card(change+1, num_lst)
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]



T = int(input())
for tc in range(1, T+1):
    num, M = input().split()
    max_p = 0
    num_lst = [int(i) for i in num]
    visited = {}
    M = int(M)
    N = len(num)
    
    change_card(0, num_lst)
    print(f"#{tc} {max_p}")