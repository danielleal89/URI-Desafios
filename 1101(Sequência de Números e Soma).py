soma = 0

while True:

    M, N = list(map(int, input().split()))

    if M <= 0 or N <= 0:

        break

    elif M > N:

        for c in range(N, M+1, 1):

            print(c, end=' ')

            soma += c

    elif N > M:

        for c in range(M, N+1, 1):

            print(c, end=' ')

            soma += c

    print('Sum={}'.format(soma))

    soma = 0