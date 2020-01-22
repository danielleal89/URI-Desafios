count = 0
while count < 1:
    teste = input().split(" ")
    X = int(teste[0])
    Y = int(teste[1])

    if (X > 0) & (Y > 0):
        print('primeiro')
    elif (X < 0) & (Y > 0):
        print('segundo')
    elif (X < 0) & (Y < 0):
        print('terceiro')
    elif (X > 0) & (Y < 0):
        print('quarto')
    else:
       exit()