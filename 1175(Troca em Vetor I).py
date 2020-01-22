lista = []
for i in range(20):
    valor = int(input())
    lista.append(valor)
lista.reverse()
for i, y in enumerate(lista):
    print('N[{}] = {}'.format(i, y))
