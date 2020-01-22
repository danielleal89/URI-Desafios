x = {}

for i in range(0, 10):
    a = int(input())
    if a <= 0:
        x[i] = 1
        print('X[{}] = {}'.format(i, x[i]))
    else:
        x[i] = a
        print('X[{}] = {}'.format(i, x[i]))
