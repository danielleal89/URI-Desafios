par = 0
while True:
    X = int(input())
    if X == 0:
        break
    elif X%2 == 0:
        for c in range(X, X+10):
            if c%2 == 0:
                par = par + c
    elif X%2 != 0:
        for c in range(X, X+11):
            if c%2 == 0:
                par = par + c
    print(par)
    par = 0