import sys
sys.stdin = open("input.txt", "r")


def change_card(change, num_lst):
    global max_p

    # num_l = num_lst[:]
    if change == M:
        prize = 0
        for n in num_lst:
            prize = prize*10 + n
        if max_p < prize:
            max_p = prize
        return
    
    N = len(num_lst)
    for i in range(N):
        for j in range(i+1, len(num_lst)):
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]
            change_card(change+1, num_lst)
            num_lst[i], num_lst[j] = num_lst[j], num_lst[i]



T = int(input())
for tc in range(1, T+1):
    max_p, M = map(int, input().split())
    num_lst = [int(i) for i in str(max_p)]
    change_card(0, num_lst)
    print(f"#{tc} {max_p}")
