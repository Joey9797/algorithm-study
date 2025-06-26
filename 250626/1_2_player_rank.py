# 진짜 등수 찾기가 아님. 
# 그냥 배열 내에서 내가 찾고자 하는 등수(index+1)의 점수가 뭐고, 그 점수로 묶인 구간을 찾는 것임.
# 즉, 특정 점수 구간의 첫 번째 인덱스와 마지막 인덱스를 찾는 것.
# 근데 이 문제는 내가 원하는 점수의 시작점(가장 높은 등수) 만 찾은 후에, 
#   그거보다 하나 앞선 등수보다 1점 낮고, target 점수 이상인 구간만 찾으면 됨
 
arr = [225, 220, 160, 160, 160, 100]

def find_range(target_rank):
    target_score = arr[target_rank-1]
    s = 0
    e = 5
    rank = 0

    while s <= e:
        mid = (s+e)//2
        if target_score >= arr[mid]:
            rank = mid
            e = mid - 1
        else:
            s = mid + 1
    
    print(f'{target_rank}등 = {arr[target_rank-1]} ~ {arr[rank - 1] - 1}')

find_range(3)
find_range(4)
find_range(5)
find_range(6)