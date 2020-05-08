# -*- encoding: utf-8 -*-
empate = 'Putz vei, o Leo ta demorando muito pra jogar...'

lista = ["Os atributos dos monstros vao ser inteligencia, sabedoria...",
         "Iron Maiden's gonna get you, no matter how far!",
         "Urano perdeu algo muito precioso..."]

while True:
    try:
        ppt = list(map(str, input().split(' ')))

        if 'papel' in ppt and 'pedra' in ppt and 'tesoura' in ppt:
            print(empate)

        elif ppt.count('papel') == 3 or ppt.count('pedra') == 3 or ppt.count('tesoura') == 3:
            print(empate)

        elif ppt.count('papel') == 2:
            if 'tesoura' in ppt:
                print(lista[ppt.index('tesoura')])
            else:
                print(empate)

        elif ppt.count('pedra') == 2:
            if 'papel' in ppt:
                print(lista[ppt.index('papel')])
            else:
                print(empate)

        elif ppt.count('tesoura') == 2:
            if 'pedra' in ppt:
                print(lista[ppt.index('pedra')])
            else:
                print(empate)

        ppt.clear()

    except:
        break