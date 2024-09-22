# https://www.acmicpc.net/problem/2028
# 자기복제수
T = int(input())

for i in range(T):
    N = int(input())
    temp = N ** 2

    n_str = str(N)

    cnt = 0
    for j in n_str:
        cnt += n_str.count(j)

    temp_str = str(temp)

    if temp_str[-cnt:] == n_str:
        print('YES')
    else:
        print('NO')