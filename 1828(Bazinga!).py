T = int(input())
for i in range(T):
    R = input().split(' ')
    if R[0] == R[1]:
        print('Caso #{}: De novo!'.format(i+1))
    elif R[0] == 'tesoura' and R[1] == 'papel':
        print('Caso #{}: Bazinga!'.format(i+1))
    elif R[0] == 'tesoura' and R[1] == 'lagarto':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif R[0] == 'papel' and R[1] == 'pedra':
        print('Caso #{}: Bazinga!'.format(i+1))
    elif R[0] == 'papel' and R[1] == 'Spock':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif R[0] == 'pedra' and R[1] == 'lagarto':
        print('Caso #{}: Bazinga!'.format(i+1))
    elif R[0] == 'pedra' and R[1] == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif R[0] == 'lagarto' and R[1] == 'Spock':
        print('Caso #{}: Bazinga!'.format(i+1))
    elif R[0] == 'lagarto' and R[1] == 'papel':
        print('Caso #{}: Bazinga!'.format(i + 1))
    elif R[0] == 'Spock' and R[1] == 'tesoura':
        print('Caso #{}: Bazinga!'.format(i+1))
    elif R[0] == 'Spock' and R[1] == 'pedra':
        print('Caso #{}: Bazinga!'.format(i + 1))
    else:
        print('Caso #{}: Raj trapaceou!'.format(i+1))

