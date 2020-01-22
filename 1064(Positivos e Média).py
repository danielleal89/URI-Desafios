a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
contador = 0
num = 0
if a >= 0:
    contador = contador + 1
    num = num + a
if b >= 0:
    contador = contador + 1
    num = num + b
if c >= 0:
    contador = contador + 1
    num = num + c
if d >= 0:
    contador = contador + 1
    num = num + d
if e >= 0:
    contador = contador + 1
    num = num + e
if f >= 0:
    contador = contador + 1
    num = num + f
print('{} valores positivos'.format(contador))
print('{:.1f}'.format(num/contador))