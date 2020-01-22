while True:
    cont = 0
    media = 0
    while cont < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            cont += 1
            media += nota
        else:
            print('nota invalida')
    print('media = {:.2f}'.format(media/2))

    teste = 0
    while True:
        print('novo calculo (1-sim 2-nao)')
        teste = int(input())
        if teste == 1 or teste == 2:
            break

    if teste == 2:
        break
