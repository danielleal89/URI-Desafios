while True:
    try:
        a = input().split(':')
        calc = ((int(a[0]) * 60) + int(a[1])) + 60
        if calc <= 480:
            print('Atraso maximo: 0')
        else:
            print('Atraso maximo: {}'.format(calc-480))
    except:
        break
