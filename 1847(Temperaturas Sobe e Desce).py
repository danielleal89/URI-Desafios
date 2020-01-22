temp = input().split(' ')
a = int(temp[0])
b = int(temp[1])
c = int(temp[2])
if a > b and b <= c:
    print(':)')
elif a < b and b >= c:
    print(':(')
elif a < b < c:
    if (c - b) < (b - a):
        print(':(')
    else:
        print(':)') #talvvez aqui
elif a > b > c:
    if (b - c) < (a - b):
        print(':)')
    else:
        print(':(')
elif a == b:
    if b < c:
        print(':)')
    else:
        print(':(')
