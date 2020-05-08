n = int(input())

for i in range(n):
    nome = input()
    grau = float(input())
    notas = list(map(float, input().split(' ')))

    a = sorted(notas)
    del(a[0])
    del(a[-1])

    print('{} {:.2f}'.format(nome, (sum(a) * grau)))