caso = 0
while True:
    try:
        n = int(input())
        lista = [0]
        caso += 1
        for i in range(n + 1):
            for j in range(i):
                lista.append(i)
        print('Caso {}: {} numero'.format(caso, len(lista)), end='')
        if n != 0:
            print('s', end='')
        print()
        for k in range(len(lista)):
            print('{}'.format(lista[k]), end='')
            if k != len(lista)-1:
                print(' ', end='')
            else:
                print()
        print()

    except EOFError:
        break
