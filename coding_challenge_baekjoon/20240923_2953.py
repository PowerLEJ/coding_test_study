# https://www.acmicpc.net/problem/2953
# 나는 요리사다
import sys
input = sys.stdin.readline

B = []

for i in range(5):
    A = list(map(int, input().split()))
    B.append(sum(A))

for i in range(5):
    if max(B) == B[i]:
        print(i + 1, max(B))
        break