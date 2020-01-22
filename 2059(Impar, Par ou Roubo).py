p, j1, j2, r, a = input().split()
if r == '0' and a == '0':
    if (int(j1) + int(j2)) % 2 == 0 and p == '1':
        print('Jogador 1 ganha!')
    elif (int(j1) + int(j2)) % 2 != 0 and p == '0':
        print('Jogador 1 ganha!')
    else:
        print('Jogador 2 ganha!')
elif r == '1' and a == '1':
    print('Jogador 2 ganha!')
elif r == '1' and a == '0':
    print('Jogador 1 ganha!')
elif r == '0' and a == '1':
    print('Jogador 1 ganha!')
