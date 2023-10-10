n = int(input())

st = 0
k = 1

while k <= n // 2:
    st += 1
    k *= 2
print(st, k)