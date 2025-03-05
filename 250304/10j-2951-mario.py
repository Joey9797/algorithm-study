mush = [int(input()) for _ in range(10)]
cnt = 0
for m in mush:
    cnt += m
    if cnt > 100:
        cnt -= m
        
print(cnt)