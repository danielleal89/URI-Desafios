n = int(input())
for i in range(n):
    j1 = input()
    j2 = input()
    if j1 == 'ataque' == j2:
        print('Aniquilacao mutua')
    elif j1 == 'pedra' == j2:
        print('Sem ganhador')
    elif j1 == 'papel' == j2:
        print('Ambos venceram')
    elif j1 == 'ataque' or j2 == 'ataque':
        if j1 == 'ataque':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
    else:
        if j1 == 'pedra':
            print('Jogador 1 venceu')
        else:
            print('Jogador 2 venceu')
