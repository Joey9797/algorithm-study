import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    info = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    N, num = input().split()
    num = [n for n in num]
    print(f"#{tc}", end=' ')
    for i in num:
        if i in info:
            i = info[i]
            result = ''
            for _ in range(4):
                result += str(i % 2)
                i //= 2
            print(result[::-1], end='')
            
        else:
            i = int(i)
            result = ''
            for _ in range(4):
                result += str(i % 2)
                i //= 2
            print(result[::-1], end='')
    print()