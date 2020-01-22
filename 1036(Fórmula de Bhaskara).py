import math
lista = input().split(" ")
A = float(lista[0])
B = float(lista[1])
C = float(lista[2])
D = ((B*B) - (4* A * C))

if D >= 0 and A != 0:
    R1 = (((-B) + math.sqrt(D)) / (2 * A))
    R2 = (((-B) - math.sqrt(D)) / (2 * A))
    print('R1 = {:.5f}'.format(R1))
    print('R2 = {:.5f}'.format(R2))
else:
    print("Impossivel calcular")