T = int(input())
for tc in range(1, 1+T):
    txt = input()
    stack = [0] * len(txt)
    top = -1
    result = 1
    for t in txt:
        if t not in '{()}':
            continue
        elif t in '{(':
            top += 1
            stack[top] = t
        elif t in ')}':
            if top == -1:
                result = 0
            elif t == '}' and stack[top] == '{':
                top -= 1
            elif t == ')' and stack[top] == '(':
                top -= 1
            else: 
                result = 0
    if top > -1:
        result = 0

    print(f'#{tc} {result}')
