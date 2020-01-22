maior = 0
codigo = 0

qtd = int(input())
for i in range(qtd):
    cod, nota = input().split()
    if float(nota) > maior:
        maior = float(nota)
        codigo = cod
if float(maior) >= 8:
    print(codigo)
else:
    print('Minimum note not reached')
