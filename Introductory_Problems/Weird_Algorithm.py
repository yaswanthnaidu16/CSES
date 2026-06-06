a = int(input())
c = a

ans = [a]

while c != 1:
    if c % 2 == 0:
        c //= 2
    else:
        c = c * 3 + 1

    ans.append(c)

print(*ans)
