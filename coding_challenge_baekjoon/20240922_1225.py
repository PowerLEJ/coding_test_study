# https://www.acmicpc.net/problem/1225
# 이상한 곱셈
import sys
input = sys.stdin.readline

A, B = list(map(str, input().split()))

A, B = list(map(int, A)), list(map(int, B))

print(sum(A) * sum(B))