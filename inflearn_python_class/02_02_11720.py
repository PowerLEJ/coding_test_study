# https://www.acmicpc.net/problem/11720
# [배열과 리스트 실전 문제] 숫자의 합 구하기

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)