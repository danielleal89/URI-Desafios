lista = []
lista = input().split(" ")
A = lista[0]
NN = lista[1:]
soma = 0
for i in NN:
    if int(i) > 0:
        N = int(i)
        N = N - 1
        while N > 0:
            for j in range(0, N+1):
                soma = soma + (int(A) + N)
                N = int(N) - 1
        print(soma)
        exit()