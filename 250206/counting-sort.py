'''
0 <= DATA[i] <= 4
DATA의 원소는 0 이상, k 이하 정수임)
'''

DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)
k = max(DATA)
COUNTS = [0] * k+1  # max(DATA) +1 (인덱스는 0번부터 시작하므로 +1 을 해줘야 한다) 칸 미리 만들어둔 것
TEMP = [0] * N      # 정렬된 결과를 저장하는 배열이므로, N 만큼의 칸을 미리 만들어둔다.

for i in range(N):
    COUNTS[DATA[i]] += 1    # COUNTS의 인덱스 = DATA[i]의 값. +=1 을 통해 COUNTS 리스트에는 해당 값이 몇개 들어있는지가 기록됨

for i in range(1, k+1):         # 0번은 앞 값이 없으므로 1부터 시작한다.
    COUNTS[i] += COUNTS[i-1]    # i번째 값에 i-1번째 값을 더해준다. 이걸 COUNTS[1]부터 끝까지 반복한다.

for i in range(N-1, -1, -1): # 원본 리스트의 마지막 순서부터 첫 순서까지 거꾸로 진행
    COUNTS[DATA[i]] -= 1     # 아직 '번째' 값이므로 -1을 해서 인덱스로 만들어줌
    TEMP[COUNTS[DATA[i]]] = DATA[i] # 만들어준 인덱스를 TEMP에 넣고, 그 값을 DATA[i]라고 한다.

print(COUNTS)