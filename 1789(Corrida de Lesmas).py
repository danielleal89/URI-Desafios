while True:
    maior = 0
    try:
        L = int(input())
        V = input().split(' ')
        for i in range(len(V)):
            if int(V[i]) > maior:
                maior = int(V[i])

        if maior < 10:
            print(1)
        elif maior >= 10 and maior < 20:
            print(2)
        else:
            print(3)
        maior = 0
    except:
        break
