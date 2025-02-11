T = int(input())
for tc in range(1, T+1):
    txt = input()
    # print(txt)
    # print(txt[::-1])
    if txt == txt[::-1]:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')
'''
3
level
samsung
eye
'''