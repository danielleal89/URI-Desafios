t = int(input())
count = 0

for i in range(1000):
    print('N[{}] = {}'.format(i, count))
    count += 1
    if count == t:
        count = 0
