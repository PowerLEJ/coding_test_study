# https://www.acmicpc.net/problem/2292
# 벌집
n = int(input())

cnt = 1 # 벌집 갯수
floor = 1 # 벌집 층수

while cnt < n:
    cnt += 6 * floor
    floor += 1

print(floor)