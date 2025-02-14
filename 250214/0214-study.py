## ------------------------------------------------------------------------------------------
## fibo memoization
def fibo1(n) :
    global cnt
    # cnt += 1
    if n >= 2 and memo[n] == 0 :    # memo[0]은 0, memo[1]은 1이 들어있는 상태
        # memo[0]과 memo[1]은 리
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]

n = 10
# cnt = 0                 # 호출 횟수 기록
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo1(n))



## ------------------------------------------------------------------------------------------
## fibo DP
def fibo2(n) :
    f = [0] * (n + 1)   # 일단 배열을 만들어둔다.
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1) :
        f[i] = f[i-1] + f[i-2]  # 배열에 fibo 값을 저장하고, for문을 돌린다.

    return f[n] # n번째 값(피보나치 방식으로 더한 최종 값) 을 리턴한다.

print(fibo2(10))
