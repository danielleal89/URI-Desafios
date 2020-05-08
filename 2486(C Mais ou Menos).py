produtos = {'suco':120, 'morango':85, 'mamao':85, 'goiaba':70, 'manga':56, 'laranja':50, 'brocolis':34}
soma = 0

while True:
    t = int(input())
    if t == 0:
        break

    for i in range(t):
        qtd = list(map(str, input().split(' ')))
        b = produtos[qtd[1]]
        soma += int(qtd[0]) * b

    if soma > 130:
        print('Menos {} mg'.format(soma - 130))
    elif soma < 110:
        print('Mais {} mg'.format(110 - soma))
    else:
        print('{} mg'.format(soma))
    soma = 0