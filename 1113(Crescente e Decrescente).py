import sys

count = 1

while count > 0:

    lista = input().split(" ")

    X = int(lista[0])

    Y = int(lista[1])

    if X > Y:

        print('Decrescente')

    elif Y > X:

        print('Crescente')

    elif X == Y:

        sys.exit()