# https://www.acmicpc.net/problem/10986
# [구간 합 실전 문제] 나머지 합 구하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * n
C = [0] * n
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        answer += C[i] * (C[i] - 1) // 2

print(answer)