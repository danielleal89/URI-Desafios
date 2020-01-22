X = int(input())
Y = int(input())
soma = 0
if X > Y:
    t = X
    X = Y
    Y = t
if X%2 != 0:
    X += 2
    while X < Y:
       if X%2 != 0:
           soma += X
       X += 1
else:
    X += 1
    while X < Y:
        if X%2 != 0:
            soma += X
        X += 1
print(soma)