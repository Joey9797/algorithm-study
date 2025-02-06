for i1 in range(1, 4): # 1, 2, 3 숫자들의 모든 조합을 만들기. 총 3중 for 문이 생기겠지...
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i1 != i3 and i2 != i3:
                    print(i1, i2, i3)

arr = [2, 3, 7] # 이런 식으로 리스트 내의 숫자를 활용할 수 있다
