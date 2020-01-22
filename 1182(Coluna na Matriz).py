C = int(input())
T = input()
soma = 0

for i in range(144):
    ler = float(input())
    if i == C:
        soma += ler
        C += 12
if T == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma / 12))
