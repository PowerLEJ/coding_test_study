# https://www.acmicpc.net/problem/2399
# # 거리의 합
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

result = 0
sum = 0

for i in range(1, n):
    result = (n_list[i] - n_list[i-1]) * i * (n - i)

    # print(n_list[i] - n_list[i-1], ' * ', i, ' * ', n - i, ' = ', result)
    
    # 예시 1 5 3 2 4 일 때
    # 1  *  1  *  4  =  4
    # 1  *  2  *  3  =  6
    # 1  *  3  *  2  =  6
    # 1  *  4  *  1  =  4
    # sum * 2 = 40

    # 예시 9 8 5 2 4 일 때
    # 2 4 5 8 9 로 정렬 하고
    # 4-2=2, 5-4=1, 8-5=3, 9-8=1
    # 차이*본인위치*뒤에서센본인위치
    # 2  *  1  *  4  =  8
    # 1  *  2  *  3  =  6
    # 3  *  3  *  2  =  18
    # 1  *  4  *  1  =  4
    # sum * 2 = 72

    sum += result

print(sum * 2)


# 시간 초과
# for i in range(n):
#     for j in range(i, n):
#         sum += abs(n_list[i] - n_list[j])
# print(sum * 2)

# 시간 초과
# for i in n_list:
#     for j in n_list:
#         sum += abs(i - j)
# print(sum)