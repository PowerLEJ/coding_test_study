# https://www.acmicpc.net/problem/1267
# 핸드폰 요금
import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
y_charge = 0
m_charge = 0

# Y
y_charge = sum((i // 30 + 1) * 10 for i in m)

# M
m_charge = sum((i // 60 + 1) * 15 for i in m)

if y_charge < m_charge:
    print(f"Y {y_charge}")
elif m_charge < y_charge:
    print(f"M {m_charge}")
else:
    print(f"Y M {y_charge}")

# import sys
# input = sys.stdin.readline

# n = int(input())
# m = list(map(int, input().split()))
# y_charge = 0
# m_charge = 0

# # Y
# for i in range(n):
#     y_charge = y_charge + (m[i] // 30 + 1) * 10

# # M
# for i in range(n):
#     m_charge = m_charge + (m[i] // 60 + 1) * 15

# if y_charge < m_charge:
#     print('Y', y_charge, end=' ')
# elif m_charge < y_charge:
#     print('M', m_charge, end=' ')
# else:
#     print('Y M', y_charge, end=' ')