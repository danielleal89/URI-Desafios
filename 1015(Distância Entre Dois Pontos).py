L1 = input().split(" ")
L2 = input().split(" ")
x1 = float(L1[0])
y1 = float(L1[1])
x2 = float(L2[0])
y2 = float(L2[1])
a = (x2 - x1)**2
b = (y2 - y1)**2
distancia = ((a + b)**(1/2))
print('{:.4f}'.format(distancia))