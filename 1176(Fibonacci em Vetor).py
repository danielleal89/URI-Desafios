entrada = int(input())

for i in range(entrada):
    n = int(input())
    if n == 0 or n == 1:
        print('Fib({}) = {}'.format(n, n))
    elif n > 1:
        t1 = 0
        t2 = 1
        t3 = 0
        cont = 0
        while n > cont:
            t1 = t2
            t2 = t3
            t3 = t2 + t1
            cont += 1
        print('Fib({}) = {}'.format(n, t3))
