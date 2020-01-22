N = int(input())
qtd1 = input().split(' ')
qtd = list(map(int, qtd1))
passou = 0

while True:
    for i in range(N):
        if qtd[i] % 2 != 0:
            passou += 1
            qtd[i] -= 1
        else:
            passou += 1
            qtd[i] -= 1
            for k in range(i-1, -1, -1):
                if qtd[k] == 0:
                    break
                else:
                    qtd[k] -= 1
            break
    break
print('{} {}'.format(passou, sum(qtd)))
