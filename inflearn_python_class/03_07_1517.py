# https://www.acmicpc.net/problem/1517
# 버블 소트 [병합 정렬 실전 문제]
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)
tmp = [0] * (N + 1)

result = 0

def merge_sort(s, e):

    global result
    
    if e - s < 1: return

    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)

    for i in range(s, e + 1):
        tmp[i] = A[i]

    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k # swap 값 카운트
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
        
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1

    while index2 <= m:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

merge_sort(1, N)

print(result)