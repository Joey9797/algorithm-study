# txt = list(input())
# N = len(txt)
# for i in range(N//2):
#     txt[i], txt[N - 1 - i] = txt[N - 1 - i], txt[i]
# print(txt)

# print(int('A', 16))
# print(int('B', 16))
# print(int('Z', 16))

for i in range(1,11): # 1 ~ 10
    print(i)
    if i % 11 == 0:
        print("11의 배수")
        break
    else: # if 가 True 이면 실행 x , if가 False 이면 실행
        print("if-else")
else:
    print("for-else") # for문 안에서 Break가 안됐다면. => for문을 돌면서 전부 다 검사했는데 문제가 없었을 겨우.