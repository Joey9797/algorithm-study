"""
i+1 박수중 = i 박수중 + i+1 일어난 + i 추가할
i 추가할(hire) = i 와 i 박수중 비교. i <= 박수중 이면, i 추가할 에 + 1 한다.
i 박수중(clap) = i 일어난(stand) + i-1 박수중(clap)

1 박수중 = 1 일어난 + 0 박수중 + 0 추가할
i 추가할(hire) = i 와 i 박수중 비교. i <= 박수중 이면, i 추가할 에 + 1 한다.
"""
info = list(map(int, input()))
hire = 0
clap = 0
for i in range(len(info)):
    stand = info[i]
    if clap < i:
        hire += 1
        clap += 1
    clap += stand
print(hire)














# T = int(input())
# for tc in range(1, T+1):
#     info = list(map(int, input()))
#     hire = [0]
#     clap = []
#     for i in range(len(info)):
#         if i == 0:
#             stand = info[0]
#             clap.append(stand)
#             if i >= clap[0]:
#                 hire[0] = 1
#         else:
#             stand = info[i]
#             clap.append(stand + clap[i-1] + hire[-1])
#             if i >= clap[i]:
#                 hire.append(1)
#     print(f'#{tc} {sum(hire)}')


