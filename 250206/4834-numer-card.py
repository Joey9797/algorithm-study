'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

3
5
49679
5
08271
10
7797946543
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, list(input())))
    c = [0] * 10

    for i in range(N):
        c[arr[i]] += 1

    max_idx = 0
    for i in range(1, 10):
        if c[i] >= c[max_idx]:
            max_idx = i

    max_cnt = c[max_idx]

    print(f'#{tc} {max_idx} {max_cnt}')