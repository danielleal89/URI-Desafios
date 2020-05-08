# -*- encoding: utf-8 -*-
res = []
cont = 0
calculo = 0
listaNomes = []

while True:
    try:
        t = int(input())
        for i in range(t):
            exp = list(map(str, input().split(' ')))
            a = exp[0]
            b = exp[1].split('=')
            res.append([a, b])

        for i in range(t):
            teste = list(map(str, input().split(' ')))
            n = int(teste[1]) - 1

            if teste[2] == '+':
                calculo = (int(res[n][0]) + int(res[n][1][0]))
            elif teste[2] == '-':
                calculo = (int(res[n][0]) - int(res[n][1][0]))
            elif teste[2] == '*':
                calculo = (int(res[n][0]) * int(res[n][1][0]))
            elif teste[2] == 'I':
                c1 = (int(res[n][0]) + int(res[n][1][0]))
                c2 = (int(res[n][0]) - int(res[n][1][0]))
                c3 = (int(res[n][0]) * int(res[n][1][0]))
                if c1 == int(res[n][1][1]) or c2 == int(res[n][1][1]) or c3 == int(res[n][1][1]):
                    listaNomes.append(teste[0])
                    listaNomes.sort()
                else:
                    cont += 1

            if teste[2] == 'I':
                pass
            elif calculo != int(res[n][1][1]):
                listaNomes.append(teste[0])
                listaNomes.sort()
            else:
                cont += 1


        if cont == 0:
            print('None Shall Pass!')
        elif cont == t:
            print('You Shall All Pass!')
        else:
            for i in range(t - cont):
                print(listaNomes[i], end='')
                if i+1 != (t-cont):
                    print(end=' ')
                else:
                    print()

        cont = 0
        listaNomes.clear()
        res.clear()
    except:
        break
