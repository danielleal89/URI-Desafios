op = input()
var = 0
var_sec = 11
soma = 0
for i in range(12):
    for j in range(12):
        num = float(input())
        if j > var and j < var_sec:
            soma += num
    var += 1
    var_sec -= 1
if op in 'Ss':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/30))