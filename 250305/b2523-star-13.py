N = int(input())

for i in range(1, N*2):
    if i <= N:
        print('*'*i)
    else:
        print('*'*(N*2-i))
    