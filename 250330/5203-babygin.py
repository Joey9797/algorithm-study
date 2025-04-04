import sys
sys.stdin = open('input.txt', 'r')

def find_winner(arr):
    for i in range(len(arr) - 2):
        if arr[i]+1 == arr[i+1] and arr[i+1]+1 == arr[i+2]:
            return True
        if arr[i] == arr[i+1] == arr[i+2]:
            return True

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    p1 = []
    p2 = []
    p1_is_winner = p2_is_winner = False
    winner = 0
    for i in range(6):
        p1.append(arr[2*i])
        p2.append(arr[2*i+1])
        if i >= 2:
            p1 = sorted(p1)
            p1_is_winner = find_winner(p1)
            if p1_is_winner:
                winner = 1
                break
            p2 = sorted(p2)
            p2_is_winner = find_winner(p2)
            if p2_is_winner:
                winner = 2
                break
    print(f"#{tc} {winner}")