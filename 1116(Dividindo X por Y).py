N = int(input())

count = N

while count > 0:

    count = count - 1;

    lista = input().split(" ")

    X = int(lista[0])

    Y = int(lista[1])

    if Y != 0 :

        div = X / Y

        print('{:.1f}'.format(float(div)))

    else:

        print('divisao impossivel')