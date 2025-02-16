arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)
k = max(arr)
cnt = [0] * (k+1)
ans = [0] * N

for i in range(N):
    cnt[arr[i]] += 1

for i in range(1, k+1):
    cnt[i] += cnt[i-1]

for i in range(N-1, -1, -1):
    cnt[arr[i]] -= 1
    ans[cnt[arr[i]]] = arr[i]
print(ans)


# for i in range(k+1):
#     for j in range(N):
#         if i == arr[j]:
#             cnt[i] += 1
# print(cnt)
# for i in range(1, k+1):
#     cnt[i] += cnt[i-1]
#
# for i in range(N-1, -1, -1):
#     cnt[arr[i]] -= 1
#     ans[cnt[arr[i]]] = arr[i]
# print(ans)
