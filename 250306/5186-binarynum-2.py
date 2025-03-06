import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    num = 0
    result = [0]*12
    for i in range(1, 13):
        if num + 2**(-i) <= N:
            result[i-1] = 1
            num += 2**(-i)
        else:
            result[i-1] = 0
        
        if num == N:
            result = ''.join(map(str, result[:i]))
            print(f"#{tc} {result}")
            break
    else:
        print(f"#{tc} overflow")