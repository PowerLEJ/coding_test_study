# https://www.acmicpc.net/problem/1592
# 영식이와 친구들
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())

n_list = [0] * N
cnt = 0 # 공 던진 총 횟수
i = 0 # 몇 번째 사람

while 1:
    n_list[i] += 1 # i번째 사람의 공 받은 횟수 축적

    if M == n_list[i]:
        print(cnt)
        break

    elif 0 != n_list[i] % 2:
        i = (i + L) % N
    else:
        i = (i - L + N) % N

    cnt += 1