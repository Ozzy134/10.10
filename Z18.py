a = [int(s) for s in input().split()]
b = 0
c = 0
for i in range(1, len(a)):
    if a[i] > a[c]:
        c = i
    if a[i] < a[b]:
        b = i
a[b], a[c] = a[c], a[b]
print(' '.join([str(i) for i in a]))