n = int(input())
total = 0
for i in range(n):
    p = list(map(int, input().split(' ')))
    if p[0] == 1001:
        total += 1.5 * p[1]
    elif p[0] == 1002:
        total += 2.5 * p[1]
    elif p[0] == 1003:
        total += 3.5 * p[1]
    elif p[0] == 1004:
        total += 4.5 * p[1]
    elif p[0] == 1005:
        total += 5.5 * p[1]

print('{:.2f}'.format(total))
