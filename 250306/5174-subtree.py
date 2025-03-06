import sys
sys.stdin = open("input.txt", "r")

def cnt_node(n):
    global cnt

    if cl[n]:
        cnt += 1
        cnt_node(cl[n])
    if cr[n]:
        cnt += 1
        cnt_node(cr[n])

T = int(input())
for tc in range(1, T+1):
    E, N = list(map(int, input().split()))  # 간선의 개수 E, 노드 N을 루트로 하는 서브 트리
    info = list(map(int, input().split()))
    cl = [0] * (E+2)
    cr = [0] * (E+2)
    for i in range(0, E*2, 2):
        p = info[i]
        c = info[i+1]
        if not cl[p]:
            cl[p] = c
        else:
            cr[p] = c
    cnt = 1
    cnt_node(N)
    print(f"#{tc} {cnt}")
