# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 인큐(삽입)
rear += 1
queue[rear] = 1

rear += 1
queue[rear] = 2

rear += 1
queue[rear] = 3

# 1, 2, 3 디큐(반환)
front += 1  #프론트를 한 칸 옮기고 (-1 => 0)
print(queue[front]) # 꺼내기 # 1 (리턴하거나, 연산하거나. 지금은 그냥 프린트했음)

front += 1  # 2
print(queue[front])

front += 1  # 3
print(queue[front])



## ------------------------------------------------------------------------------------------
## enQueue 함수로 구현
queue = [0] * 3
front = rear = -1

def enqueue(item):
    global rear
    if rear == len(queue) - 1:
        print('꽉 찼어요!')
    else:
        rear += 1
        queue[rear] = item




## ------------------------------------------------------------------------------------------
## while 문으로 큐에서 디큐하기
while front != rear:    # 큐에 원소가 남아있으면
    front += 1  # 디큐
    t = queue[front]
    print(t)


## ------------------------------------------------------------------------------------------
## .append, .pop으로 큐에서 인큐 디큐하기 (연산이 느리므로, 사용 지양)
q = []
q.append(1) # 1 삽입
q.append(2)
q.append(3)
q.pop(0)    # 맨 앞 요소 pop
q.pop(0)
q.pop(0)