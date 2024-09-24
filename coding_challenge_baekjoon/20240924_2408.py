# https://www.acmicpc.net/problem/2408
# 큰 수 계산
N = int(input())

a = ''
for i in range(2 * N - 1):
    a += input()

a = a.replace('/', '//')

print(eval(a))