# https://www.acmicpc.net/problem/11003
# [슬라이딩 윈도우 실전 문제] 최솟값 찾기

from collections import deque
import sys

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 1. 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i], i))

    # 2. 슬라이딩 윈도우 벗어난 데이터 삭제하기
    if mydeque[0][1] <= i - L: # 윈도우 범위를 벗어나면
        mydeque.popleft()
    print(mydeque[0][0], end=' ')