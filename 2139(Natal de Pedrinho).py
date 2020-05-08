from datetime import datetime
while True:
    try:
        n = input().split()
        mes = int(n[0])
        dia = int(n[1])
        if mes == 12 and dia == 25:
            print('E natal!')
        elif mes == 12 and dia == 24:
            print('E vespera de natal!')
        elif mes == 12 and dia > 25:
            print('Ja passou!')
        else:
            d2 = datetime.strptime('2016-12-25', '%Y-%m-%d')
            d1 = datetime.strptime('2016-{}-{}'.format(mes, dia), '%Y-%m-%d')
            x = abs((d2 - d1).days)
            print('Faltam {} dias para o natal!'.format(x))
    except:
        break