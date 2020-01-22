lista = input().split(" ")

ini = int(lista[0])

fim = int(lista[1])

if ini > fim:
    tempo = (24 - ini) + fim
    print('O JOGO DUROU {} HORA(S)'.format(tempo))

elif ini == fim:
    print('O JOGO DUROU 24 HORA(S)')

else:
    tempo = fim - ini
    print('O JOGO DUROU {} HORA(S)'.format(tempo))