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
def first_change():
    global num_lst, can_change_first

    max_num = max(num_lst)
    max_cnt = 0
    max_i = []
    for i in range(N):
        if num_lst[i] == max_num:
            max_cnt += 1
            max_i.append(i)

    if max_cnt == 1:
        num_lst[0], num_lst[i] = num_lst[i], num_lst[0]
        can_change_first = True
        return 1
    else:
        return 0



def change_card(change, num_lst):
    global max_p

    if change == M:
        prize = 0
        for n in num_lst:
            prize = prize*10 + n
        if max_p < prize:
            max_p = prize
        return
    
    num = ''.join(map(str, num_lst))
    key = (num, change)
    if key in visited:
        return
    visited[key] = 1
    
    s = 0
    if can_change_first == True:
        s = 1
    for i in range(N):
        for j in range(i+1, len(num_lst)):
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
            change_card(change+1, num_lst)
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]



T = int(input())
for tc in range(1, T+1):
    num, M = input().split()
    max_p = int(num)
    num_lst = [int(i) for i in num]
    visited = {}
    M = int(M)
    N = len(num)
    can_change_first = False
    
    change_card(first_change(), num_lst)
    print(f"#{tc} {max_p}")