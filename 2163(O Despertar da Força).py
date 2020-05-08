m = input().split()
matriz = []

for i in range(int(m[0])):
    v = input().split()
    matriz.append(v.copy())

for j in range(1, int(m[0]) - 1):
    for k in range(1, int(m[1]) - 1):
        if matriz[j][k] == '42' and k < int(m[1]) - 1:
            if matriz[j][k-1] == matriz[j][k+1] == matriz[j-1][k] == '7':
                if matriz[j+1][k] == matriz[j-1][k-1] == matriz[j-1][k+1] == matriz[j+1][k-1] == matriz[j+1][k+1] == '7':
                    print(j+1, k+1)
                    exit()
print('0 0')
