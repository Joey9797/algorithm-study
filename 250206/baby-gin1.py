# num = 456789

# 1. 입력을 받는 경우
num = int(input())
c = [0] * 12 # c[10], [11]을 더미로 만든다.

for _ in range(6): # 단순 반복 6회
    c[num%10] += 1
    num //= 10
# print(c)

i = 0
tri = run = 0
while i < 10:   # 카드 번호는 9까지니깐
    if c[i] >= 3:   # triplit 확인
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print('win')
else:
    print('lose')