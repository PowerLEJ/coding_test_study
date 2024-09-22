# https://www.acmicpc.net/problem/2139
# 나는 너가 살아온 날을 알고 있다
import sys
input = sys.stdin.readline

while 1:

    d, m, y = map(int, input().split())
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0

    if 0 == d and 0 == m and 0 == y:
        break

    if 0 == y % 4:
        day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # print('윤년')
        if 0 == y % 100:
            day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            # print('윤년 아님')
        if 0 == y % 400:
            day_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            # print('다시 윤년임')

    result = sum(day_list[:m-1]) + d

    print(result)