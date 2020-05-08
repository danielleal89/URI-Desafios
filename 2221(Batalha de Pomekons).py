t = int(input())

for i in range(t):
    bonus = int(input())
    dabriel = list(map(int, input().split(' ')))
    guarte = list(map(int, input().split(' ')))
    dCalc = (dabriel[0] + dabriel[1]) / 2
    gCalc = (guarte[0] + guarte[1]) / 2
    if dabriel[2] % 2 == 0:
        dCalc += bonus
    if guarte[2] % 2 == 0:
        gCalc += bonus
    if gCalc > dCalc:
        print('Guarte')
    elif dCalc > gCalc:
        print('Dabriel')
    else:
        print('Empate')