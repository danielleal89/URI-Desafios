N = input()
num = int(N)
total = []

while True:
    if num >= 1000:
        total.append('M')
        num -= 1000

    elif '9' in N[0]:
        if num >= 900:
            total.append('CM')
            num -= 900
        elif num >= 90:
            total.append('XC')
            num -= 90
        elif num == 9:
            total.append('IX')
            num -= 9

    elif '4' in N[0]:
        if num >= 400:
            total.append('CD')
            num -= 400
        elif num >= 40:
            total.append('XL')
            num -= 40
        elif num == 4:
            total.append('IV')
            num -= 4

    else:
        if num >= 500:
            total.append('D')
            num -= 500
        elif num >= 100:
            total.append('C')
            num -= 100
        elif num >= 50:
            total.append('L')
            num -= 50
        elif num >= 10:
            total.append('X')
            num -= 10
        elif num >= 5:
            total.append('V')
            num -= 5
        elif num >= 1:
            total.append('I')
            num -= 1
    N = ('{}'.format(num))

    if num == 0:
        print(''.join(total))
        break
