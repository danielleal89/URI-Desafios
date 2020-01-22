a = input().split()
P = int(a[0])
N = int(a[1])

b = input().split()

anterior = int(b[0]) + P
proximo = 0
cont = 1

for i in range(1, N):
    proximo = int(b[i]) + P

    if anterior > proximo:
        if anterior - proximo <= P:
           cont += 1
        else:
            print('GAME OVER')
            break

    else:
        if proximo - anterior <= P:
            cont += 1
        else:
            print('GAME OVER')
            break

    if cont == N:
        print('YOU WIN')
        break
    anterior = proximo
