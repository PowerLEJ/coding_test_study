# https://www.acmicpc.net/problem/29751
# 삼각형
import sys
input = sys.stdin.readline

W, H = map(int, input().split())

result = W * H / 2

print(result)