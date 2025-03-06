'''
4
5
....o
...o.
..o..
.o...
o.... 
5
...o.
ooooo
...o.
...o.
.....
5
.o.oo
oo.oo
.oo..
.o...
.o...
5
.o.o.
o.o.o
.o.o.
o.o.o
.o.o.
'''
def omok(arr, N):
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for om_r, om_c in [[0, 1], [1, 1], [1, 0], [1, -1]]:
                    for i in range(1, 5):
                        nr = r + om_r * i
                        nc = c + om_c * i
                        if nr < 0 or nr >= N or nc < 0 or nc >= N or arr[nr][nc] == '.':
                            break
                    else:
                        return 'YES'
    return 'NO'
                    
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 오목판 크기 N
    arr = [input() for _ in range(N)]
    result = omok(arr, N)
    print(f"#{tc} {result}")
                    
