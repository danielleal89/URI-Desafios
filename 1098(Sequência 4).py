i = float(-0.2)
j = float(0.8)

while (i < 1.8):
    i = i + 0.2
    j = j + 0.2
    if i == 0.0 or i == 1.0 or i == 1.9999999999999998:
        print('I={:.0f} J={:.0f}'.format(i, j))
        print('I={:.0f} J={:.0f}'.format(i, j + 1))
        print('I={:.0f} J={:.0f}'.format(i, j + 2))
    else:
        i = i
        print('I={:.1f} J={:.1f}'.format(i,j))
        print('I={:.1f} J={:.1f}'.format(i,j+1))
        print('I={:.1f} J={:.1f}'.format(i,j+2))