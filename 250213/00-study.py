## ------------------------------------------------------------------------------------------
## STACK push
def push(item, size):
    global top
    if top == size-1:   # stack이 '꽉찬 상태'인지 확인 필수!
        print('꽉 찼어요!')
    else:
        top += 1
        stack[top] = item
size = 10
stack = [0] * size
top = -1

push(10, size)

# 아래 코드가 강사님 코든데, 뭔가 헷갈림. 혹시 몰라서 일단 써둔다.
def push(item, size):
    global top
    top += 1
    if top == size:
        print('꽉 찼어요!')
    else:
        stack[top] = item


## ------------------------------------------------------------------------------------------
## STACK pop
def pop():
    global top
    if top == -1:
        return 0
    else:
        top -= 1
        return stack[top + 1]


## ------------------------------------------------------------------------------------------
## STACK push,pop 으로 괄호 검사하기
txt = input()

top = -1
stack = [0] * len(txt)

for x in txt:
    if x == '(':    # 괄호가 여러 종류고, 중간에 글자도 들어있다면 if x in '{[(<' 로 바꾸면 됨.
        top += 1
        stack[top] = x
    elif x == ')':  # 여러종류면 if x in '}])>' 로 바꾸면 됨.
        if top == -1:   # 스택이 비어있는 경우
            print('짝이 맞지 않아요')
            break # for x in txt 중단. 아예 걍 끝.
        else:
            top -= 1
            # if # 소괄호로만 이루어진 txt이므로, 비교 작업 생략
if top > -1:    # 스택에 괄호가 남아있는 경우
    print('짝이 맞지 않아요')