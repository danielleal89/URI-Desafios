soma = 0
cont = 0
while True:
    idade = int(input())
    if idade >= 0:
        soma += idade
        cont += 1
    else:
        break
print('{:.2f}'.format(soma/cont))
