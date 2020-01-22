X = int(input())
Y = int(input())
soma = 0
if X < Y:
    for count in range(X, Y+1):
        if count % 13 > 0:
            soma = soma + count
elif X > Y:
    for count in range(Y, X+1):
        if count % 13 > 0:
            soma = soma + count
print(soma)