cont = 1
X = int(input())
while True:
    num = int(input())
    if num > X:
        Z = num
        soma = X
        break
for i in range(X+1, Z, 1):
    soma += i
    cont += 1
    if soma > Z:
        print(cont)
        break