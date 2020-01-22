v = {}
for i in range(100):
    valor = float(input())
    if valor <= 10:
        v[i] = valor
    else:
        v[i] = 11
for j in range(len(v)):
    if v[j] <= 10:
        print('A[{}] = {}'.format(j, v[j]))
