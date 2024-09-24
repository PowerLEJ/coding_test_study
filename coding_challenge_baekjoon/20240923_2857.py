# https://www.acmicpc.net/problem/2857
# FBI

result = []
for i in range(5):
    N = input()

    if "FBI" in N:
        result.append(i+1)

if len(result) == 0:
    print("HE GOT AWAY!")
else:
    print(*result)