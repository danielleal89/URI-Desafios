X = int(input())
Y = int(input())
if X < Y:
    for c in range(X+1, Y, 1):
        if c%5 == 2 or c%5 == 3:
            print(c)
elif Y < X:
    for c in range(Y+1, X, 1):
        if c%5 == 2 or c%5 == 3:
            print(c)