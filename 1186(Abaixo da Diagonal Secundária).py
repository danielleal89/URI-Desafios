op = input()
var = 12
soma = 0
for i in range(12):
    for j in range(12):
        num = float(input())
        if j >= var:
            soma += num
    var -= 1
if op in 'Ss':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/66))