a = int(input())
x = list(map(int, input().split()))

num = a * (a + 1) // 2
summy = sum(x)

print(num - summy)
