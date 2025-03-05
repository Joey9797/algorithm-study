N = int(input())
seats = input()
cnt = 0
i = 0
while i < N:
    if seats[i] == 'L' and i < N:
        i += 1
    cnt += 1
    i += 1
if 'L' in seats:
    cnt += 1
print(cnt)