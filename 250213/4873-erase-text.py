T = int(input())
for tc in range(1, 1+T):
    txt = input()
    N = len(txt)
    stack = []

    for i in range(N):
        if txt[i] not in stack:
            stack.append(txt[i])
        elif txt[i] == stack[-1]:
            stack.pop()
        elif txt[i] != txt[i - 1] and i > 1:
            stack.append(txt[i])

    print(f'#{tc} {len(stack)}')

# txt = input()
# N = len(txt)
# stack = [0] * N
# xadd = []
# top = 0
# for t in txt:
#     if t not in stack:
#         stack[top] = t
#         top += 1
#     elif t == stack[top-1]:
#         top -= 1
#         xadd.append(stack[top-1])
#     if -2 <= top <= -1:
#         top = 0

#------------------------------------------------------------------------------
# 지우 코드
# T = int(input())
# for tc in range(1, T+1):
#     S = input()
#     k = len(S)
#     arr = [0]*(k+1)
#     top = 0
#     arr[top]=0
#     for s in S:
#         top+=1
#         arr[top]=s
#         if arr[top]==arr[top-1]:
#             top-=2
#     result = arr[1:top+1]
#     print(f'#{tc} {len(result)}')
