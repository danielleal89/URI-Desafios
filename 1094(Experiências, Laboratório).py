import sys
N = int(input())
count = 0
R = 0
S = 0
C = 0
total = 0
while count < N:
    count = count + 1
    Quantia = input().split(" ")

    if Quantia[1] == 'R':
        R = R + int(Quantia[0])
        total = total + int(Quantia[0])
    elif Quantia[1] == 'S':
        S = S + int(Quantia[0])
        total = total + int(Quantia[0])
    elif Quantia[1] == 'C':
        C = C + int(Quantia[0])
        total = total + int(Quantia[0])

    while count == N:
        print('Total: {} cobaias'.format(total))
        print('Total de coelhos: {}'.format(C))
        print('Total de ratos: {}'.format(R))
        print('Total de sapos: {}'.format(S))
        print('Percentual de coelhos: {:.2f} %'.format((C/total)*100))
        print('Percentual de ratos: {:.2f} %'.format((R/total)*100))
        print('Percentual de sapos: {:.2f} %'.format((S/total)*100))
        sys.exit()