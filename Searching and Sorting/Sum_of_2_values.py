n, x = map(int, input().split())
a = list(map(int, input().split()))

d = {}

for i in range(n):
    need = x - a[i]
    if need in d:
        print(d[need] + 1, i + 1)
        break
    d[a[i]] = i
    else:
        print("IMPOSSIBLE")
