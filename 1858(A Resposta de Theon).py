n = int(input())
p = input().split(' ')
cont = 100
pos = 0
for i in range(len(p)):
    if int(p[i]) < cont:
        cont = int(p[i])
        pos = i+1
print(pos)
