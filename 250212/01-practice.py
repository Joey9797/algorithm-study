A = 'XYPV'
B = 'EOGGXYPVSY'

def combine(a, b):
    N = len(A)
    M = len(B)
    ans = ''
    i = j = 0
    while i + j < N + M:
        if i < N:
            ans += A[i]
            i += 1
        if j < M:
            ans += B[j]
            j += 1
    return ans

result = combine(A, B)
print(result)
