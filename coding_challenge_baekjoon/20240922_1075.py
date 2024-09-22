# https://www.acmicpc.net/problem/1075
# 나누기
N = int(input())
F = int(input())
temp = (N // 100) * 100

while 1:
    if 0 == temp % F:
        break
        
    temp += 1
    
print(str(temp)[-2:])