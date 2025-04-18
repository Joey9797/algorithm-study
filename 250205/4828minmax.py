'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

[입력]
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 50 )
각 케이스의 첫 줄에 양수의 개수 N이 주어진다. ( 5 ≤ N ≤ 1000 )
다음 줄에 N개의 양수 ai가 주어진다. ( 1 ≤ ai≤ 1000000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
T = int(input())

def max_min_val(T):
    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))

        max_val = arr[0]
        min_val = arr[0]

        # 최댓값,최솟값 구하기
        for i in range(1, N):
            if max_val < arr[i]:
                max_val = arr[i]
            if min_val > arr[i]:
                min_val = arr[i]
        print(f'#{tc} {max_val - min_val}')

max_min_val(T)

'''
입력
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]

    for i in range(1, N):
        if max_v < arr[i]:
            max_v = arr[i]
        if min_v > arr[i]:
            min_v = arr[i]

    print(f'#{tc} {max_v - min_v}')
'''

