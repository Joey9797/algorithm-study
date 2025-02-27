'''
각 분반은 최소 인원 이상, 최대 인원 이하를 만족해야 함
학생들 점수를 바탕으로 s1, s2를 임의로 나눔
s2 이상 우수 분반, s1이상 s2미만 보통, s1미만 부진 분반
학생이 가장 많은 분반, 적은 분반의 학생 수 차의 최솟값 출력
s1, s2가 없다면, -1 출력'''
'''
5
5 1 4
3 5 5 4 5
6 2 6
5 3 3 5 5 1
7 1 6
3 3 5 2 5 1 2
8 1 7
3 1 1 2 2 5 3 5
10 1 6
4 4 2 4 5 2 5 3 5 5 


답 2 -1 1 2 1'''

'''
1. 일단 s1을 1~98 까지 돌리고, s2를 s1~100까지 돌린다.
2. 0~s1-1([0:s1])까지의 학생 수를 더한다. s1~s2-1([s1:s2])까지의 학생수를 더한다. [s2:101] 까지 더한다.
3. 만약 셋 중에 하나라도 min, max 벗어나면 continue(다음 수 검사)
4. 만족하는게 있으면, 학생수1, 학생수2, 학생수3 의 최대와 최소를 뺀다. 
5. 그 중 가장 작은 값을 출력한다.
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, min_s, max_s = list(map(int, input().split())) # N학생수, min분반별 최소인원, max 분반별 최대인원
#     score = sorted(list(map(int, input().split())))
#     student = []
#     cnt = 1
#     for i in range(N-1):
#         if score[i] == score[i+1]:
#             cnt += 1
#         else:
#             student.append(cnt)
#             cnt = 1
#     student.append(cnt)
    
#     if len(student) == 3:
#         if student[0] < min_s or student[1] < min_s or student[2] < min_s or student[0] > max_s or student[1] > max_s or student[2] > max_s:
#             result = -1
#         else:
#             result = abs(max(student) - min(student))
    
#     if len(student) > 3:
#         avr = round(sum(student) / 3)   # 학생수 기준점 (학생수평균의 반올림값값)
#         print(avr)
#         # for s in student:
