marcos = []
leonardo = []

while True:
    try:
        n = int(input())
        m_l = list(map(int, input().split(' ')))
        for i in range(m_l[0]):
            var = list(map(int, input().split(' ')))
            marcos.append(var)

        for i in range(m_l[1]):
            var = list(map(int, input().split(' ')))
            leonardo.append(var)

        cartas = list(map(int, input().split(' ')))
        atributo = int(input())

        m = marcos[cartas[0]-1][atributo-1]
        l = leonardo[cartas[1]-1][atributo-1]

        if m > l:
            print('Marcos')
        elif l > m:
            print('Leonardo')
        else:
            print('Empate')

        marcos.clear()
        leonardo.clear()
    except:
        break