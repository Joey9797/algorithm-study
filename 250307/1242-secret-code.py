import pprint
import sys
sys.stdin = open("input.txt", "r")
'''
1. 16진수 2진수로 변환
2. info를 가지고, 두께에 따른 info를 재정의 해야함
3. 2진수 10진수로 변환 (info를 사용하여)
4. 앞에서부터 7까지의 합을 구하고, 검증코드를 구한다.(합 //10 -> +1,  (+1 한 값 * 10) - 합)
5. 검증코드가 맞는지 틀린지 검사한 후, 각각에 맞는 답을 출력한다.
'''


T = int(input())
for tc in range(1, T+1):
    N, M = [*map(int, input().split())] # N 세로길이 M 가로길이
    data = list(set([input() for _ in range(N)]))   # set을 사용하여 0으로만 이루어진 행 제거
    data = sorted(data)[1:] # set후 하나 남은 0으로만 이루어진 행 1개를 마저 제거
    N = len(data)

    code_info = {'211':0, '221':1, '122':2, '411':3, '132':4, 
                 '231':5, '114':6, '312':7, '213':8, '112':9
                }
    hex_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', 
               '4':'0100', '5':'0101', '6':'0110', '7':'0111',
               '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
               'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
               }
    # pprint.pprint(data)
    
    for r in range(N):  # 
        code = ''
        sc = 0
        for c in range(M):
            code += hex_bin[data[r][c]]
        for i in range(len(code)):
            if code[i] != '0':
                sc = i
                break
        code = code[i:]
        # print(code)

        # 첫 숫자의 비율을 구해서, 전체 2진수 암호의 길이를 구한다.
        final_code = []
        sp = 0  # start point
        for _ in range(8):
            cnt_lst = []
            cnt = 1
            while len(cnt_lst) < 3:
                if code[sp] == code[sp+1]:
                    cnt += 1
                    sp += 1
                else:
                    cnt_lst.append(cnt)
                    cnt = 1
                    sp += 1
            min_num = min(cnt_lst) # line 의 두께
            cnt_lst = [i//min_num for i in cnt_lst]
            secret_code = ''.join(map(str, cnt_lst))
            bin_code = code_info[secret_code]
            while code[sp] == '0' and (sp+1) < len(code) :
                sp += 1
            final_code.append(bin_code)
    
        print(final_code)


                

        
        
