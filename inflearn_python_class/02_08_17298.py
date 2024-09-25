# https://www.acmicpc.net/problem/17298
# 오큰수 구하기 [스택과 큐 실전 문제]
n = int(input())
A = list(map(int, input().split()))
ans = [0] * n # 오큰수 저장하는 정답 배열
myStack = [] # A 배열의 index가 append 되고, pop되는 것 기록하는 배열

for i in range(n):
    while myStack and A[myStack[-1]] < A[i]: # 오큰수 조건
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수 저장
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ''
for i in range(n):
    result += str(ans[i]) + " "

print(result)