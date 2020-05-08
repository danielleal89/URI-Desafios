n = input().split()
total = int(n[0])
for i in range(int(n[1])):
    m = input()
    if m == 'fechou':
        total += 1
    else:
        total -= 1
print(total)