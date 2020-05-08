N = int(input())
p = list(map(int, input().split(' ')))
dois = tres = quatro = cinco = 0
lista = [0, 0, 0, 0]
for i, item in enumerate(p):
    if item % 2 == 0:
        lista[0] += 1
    if item % 4 == 0:
        lista[2] += 1
    if item % 3 == 0:
        lista[1] += 1
    if item % 5 == 0:
        lista[3] += 1
for i in range(4):
    print('{} Multiplo(s) de {}'.format(lista[i], i+2))
