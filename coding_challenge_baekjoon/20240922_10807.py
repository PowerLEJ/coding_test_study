# https://www.acmicpc.net/source/84162606
# 개수 세기
import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
l = int(input())
cnt = 0

for i in range(n):
    if m[i] == l:
        cnt += 1

print(cnt)