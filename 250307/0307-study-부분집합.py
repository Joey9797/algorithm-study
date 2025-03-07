# --------------- bit 연산 응용
# 1. 부분집합의 수를 바로 구할 수 있다.
arr = [1, 2, 3, 4]  # 16개

print(f'부분 집합의 수 : {1 << len(arr)}')

for i in range(1 << len(arr)):
    for idx in range(len(arr)):
        # (1 << idx)
        #   ob1, 0b10, 0b100, 0b1000
        # i 의 idx 번째 bit 가 1인 지 확인(부분 집합에 포함 되어 있는 지 확인)
        if i & (1 << idx):
            print(arr[idx], end=" ")
    print()


# 2. 합이 10인 부분 집합만 출력해라
arr = [1, 2, 3, 4, 5, 6]
for i in range(1 << len(arr)):
    subset = []
    total = 0
    for idx in range(len(arr)):
        if i & (1 << idx):
            subset.append(arr[idx])
            total += arr[idx]
    if total == 10:
        print(f'합이 10인 부분집합: {subset}')