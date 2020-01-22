valores = input().split()
valores = list(map(int, valores))
hI, mI, hF, mF = valores

inicio = hI*60 + mI
final = hF*60 + mF
duracao = 0

if hI <= hF:
    duracao = final - inicio
    if duracao == 0:
        print('O JOGO DUROU 24 HORA(S) E {} MINUTO(S)'.format(duracao%60))
    else:
        print('O JOGO DUROU {:.0f} HORA(S) E {} MINUTO(S)'.format((duracao - duracao%60)/60, duracao%60))
else:
    duracao = (24*60 - inicio) + final
    print('O JOGO DUROU {:.0f} HORA(S) E {} MINUTO(S)'.format((duracao - duracao%60)/60, duracao%60))