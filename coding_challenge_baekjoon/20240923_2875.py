# https://www.acmicpc.net/problem/2875
# 대회 or 인턴
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

result = 0

while 1:
    N -= 2
    M -= 1

    if N < 0 or M < 0 or (N + M) < K:
        break
    result += 1

print(result)