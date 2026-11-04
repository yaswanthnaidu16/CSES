s = input()

maxy = 1
summy = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        summy += 1
    else:
        summy = 1

    maxy = max(maxy, summy)

print(maxy)
