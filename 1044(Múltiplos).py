lista = input().split()
A = int(lista[0])
B = int(lista[1])
if (A / B)%2 == 0 or (B / A)%2 == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')