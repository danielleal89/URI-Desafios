op = input()
var = 0
soma = 0
for i in range(12):
    for j in range(12):
        num = float(input())
        if 0 < i < 6:
            if j < i:
                soma += num
        elif i == 6:
            var = 5
            if j < (i-1):
                soma += num
        elif i > 6:
            if j < var:
                soma += num
    var -= 1
if op in 'Ss':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/30))