caso = 1
qtd = pos = 0
while True:
    try:
        um = input()
        dois = input()
        for i in range(len(dois)):
            if um == dois[i:i+len(um)]:
                qtd += 1
                pos = i+1
        print('Caso #{}:'.format(caso))
        caso += 1
        if qtd == 0:
            print('Nao existe subsequencia')
        else:
            print('Qtd.Subsequencias: {}'.format(qtd))
            print('Pos: {}'.format(pos))
        qtd = pos = 0
        print()
    except:
        break
