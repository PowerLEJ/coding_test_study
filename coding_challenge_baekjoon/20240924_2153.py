# https://www.acmicpc.net/problem/2153
# 소수 단어
word = list(str(input()))
total = 0
cnt = 0

for i in word:
    if i.islower():
        total += ord(i) - 96
    else:
        total += ord(i) - 38

if 1 == total:
    cnt = 1

for i in range(2, total + 1):
    if total % i == 0:
        # total = total // i
        cnt += 1
        
if 1 == cnt:
    print("It is a prime word.")
else:
    print("It is not a prime word.")