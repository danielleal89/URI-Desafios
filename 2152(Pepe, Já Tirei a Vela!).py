t = int(input())
for i in range(t):
    entrada = input().split()
    h = int(entrada[0])
    m = int(entrada[1])
    if h < 10:
        h = str(0) + str(entrada[0])
    if m < 10:
        m = str(0) + str(entrada[1])
    print('{}:{} - '.format(h, m), end='')
    if entrada[2] == '1':
        print('A porta abriu!')
    else:
        print('A porta fechou!')