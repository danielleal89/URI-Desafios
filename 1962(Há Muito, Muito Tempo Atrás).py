N = int(input())

for i in range(N):
    ano = int(input())

    if ano >= 0 and ano < 2015:
        calc = 2015 - ano
        print('{} D.C.'.format(calc))
    else:
        calc = ano - 2014
        print('{} A.C.'.format(calc))
