n = float(input())
print('N[{}] = {:.4f}'.format(0, n))

for i in range(1, 100):
    n = n / 2
    print('N[{}] = {:.4f}'.format(i, n))
