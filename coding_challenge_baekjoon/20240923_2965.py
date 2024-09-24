# https://www.acmicpc.net/problem/2965
# 캥거루 세마리
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

result = max(B - A, C - B) - 1

print(result)