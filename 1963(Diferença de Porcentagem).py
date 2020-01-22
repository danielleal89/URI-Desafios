N = input().split()
antigo = float(N[0])
novo = float(N[1])

calc = ((novo/antigo) * 100) - 100

print('{:.2f}%'.format(calc))
