op = input()
var = 0
soma = 0
for i in range(12):
    var += 1
    for j in range(12):
        num = float(input())
        if j >= var:
            soma += num
if op in 'Ss':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/66))