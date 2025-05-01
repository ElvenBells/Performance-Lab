n, m = map(int, input().split())
res = ''
pos = 1
while True:
    res = res + str(pos)
    next = (pos + m - 1) % n
    pos = next if next!=0 else n
    if pos == 1:
        break

print(res)