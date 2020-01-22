par = []
impar = []

for i in range(15):
    valor = int(input())
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    if len(par) == 5:
        for p, v in enumerate(par):
            print('par[{}] = {}'.format(p, v))
        par.clear()
    elif len(impar) == 5:
        for p, v in enumerate(impar):
            print('impar[{}] = {}'.format(p, v))
        impar.clear()

for p, v in enumerate(impar):
    print('impar[{}] = {}'.format(p, v))

for p, v in enumerate(par):
    print('par[{}] = {}'.format(p, v))
