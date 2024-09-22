# https://www.acmicpc.net/problem/1434
# 책정리
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = sum(i for i in A)
b = sum(i for i in B)

print(a - b)