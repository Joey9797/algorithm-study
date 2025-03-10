'''
0 0 1
1 0 0
0 1 0
0 0 0
'''

import pprint


def fall_bricks(bricks):
    f_bricks = [[0]*10 for _ in range(10)]
    for c in range(10):
        fr = 9
        for r in range(9, -1, -1):
            if bricks[r][c] != 0:
                f_bricks[fr][c] = bricks[r][c]
                fr -= 1
    return f_bricks
# bricks = [list(map(int, input().split())) for _ in range(4)]
# fall_bricks(bricks)
# print(bricks)


bricks = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [1, 1, 0, 0, 1, 2, 2, 2, 2, 1],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
 [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]]


result = fall_bricks(bricks)
pprint.pprint(result)