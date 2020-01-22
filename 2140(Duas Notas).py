cont = 0
while True:
    n = input().split()
    troco = int(n[1]) - int(n[0])

    if n[0] == '0' == n[1]:
        break

    for i in range(6):
        if troco - 100 >= 0:
            troco -= 100
            cont += 1
        elif troco - 50 >= 0:
            troco -= 50
            cont += 1
        elif troco - 20 >= 0:
            troco -= 20
            cont += 1
        elif troco - 10 >= 0:
            troco -= 10
            cont += 1
        elif troco - 5 >= 0:
            troco -= 5
            cont += 1
        elif troco - 2 >= 0:
            troco -= 2
            cont += 1

    if cont == 2:
        print('possible')
    else:
        print('impossible')
    cont = 0
