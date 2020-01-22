cont = 0
soma = 0
while True:
    e = str(input())
    if e == 'caw caw':
        cont += 1
        print(soma)
        soma = 0
        if cont == 3:
            break
    else:
        if e == '--*':
            soma += 1
        elif e == '-*-':
            soma += 2
        elif e == '-**':
            soma += 3
        elif e == '*--':
            soma += 4
        elif e == '*-*':
            soma += 5
        elif e == '**-':
            soma += 6
        elif e == '***':
            soma += 7
