# https://www.acmicpc.net/problem/2386
# 도비의 영어공부
import sys
input = sys.stdin.readline

while 1:
    ary = list(map(str, input().split()))

    find = ary[0]
    target = ary[1:]

    if '#' == find:
        break

    cnt = 0
    cnt = str(target).lower().count(find)

    print(find, cnt)