for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        check_lst = buildings[i-2:i] + buildings[i+1:i+3]
        max_building = max(check_lst)
        if buildings[i] > max_building:
            view = buildings[i] - max_building
            cnt += view
    print(f'#{tc} {cnt}')
