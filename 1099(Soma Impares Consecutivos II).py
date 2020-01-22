N = int(input())
count = 0
soma = 0
while count < N:
    count = count + 1
    teste = input().split(" ")
    X = int(teste[0])
    Y = int(teste[1])
    if X < Y:
        for pos in range(X+1, Y):
            if pos % 2 == 1:
                soma += pos
        print(soma)
    else:
        for pos in range(X-1, Y, -1):
            if pos % 2 == 1:
                soma += pos
        print(soma)
    soma = 0