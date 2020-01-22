entrada = int(input())
x = 0
for i in range(entrada):
    v = int(input())
    for j in range(0, v):
        if j % 2 == 0:
            x += 1
        else:
            x -= 1
    print(x)
    x = 0
