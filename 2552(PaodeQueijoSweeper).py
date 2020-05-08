lista = []

while True:
    try:
        n = list(map(int, input().split(' ')))
        for i in range(n[0]):
            valor = list(map(int, input().split(' ')))

            # Pega os ao lado
            for i in range(n[1]):
                if valor[i] == 1:
                    valor[i] = 9
                elif i == 0:
                    if valor[i+1] == 1:
                        valor[i] += 1
                elif 0 < i < (n[1] - 1):
                    if valor[i+1] == 1:
                        valor[i] += 1
                    if valor[i-1] == 9:
                        valor[i] += 1
                else:
                    if valor[i-1] == 9:
                        valor[i] += 1
            lista.append(valor)

        # Pega os abaixo
        for j in range(1, len(lista)):
            for k in range(n[1]):
                if lista[j-1][k] != 9:
                    if k < (n[1]):
                        if lista[j][k] == 9:
                            lista[j-1][k] += 1

        # Pega os de cima
        for l in range(len(lista) - 1, 0, -1):
            for m in range(n[1]):
                if lista[l][m] != 9 and m < n[1]:
                    if lista[l-1][m] == 9:
                        lista[l][m] += 1

        # Imprimir
        for i in range(len(lista)):
            for j in range(n[1]):
                print(lista[i][j], end='')
            print()

        lista.clear()
    except:
        break