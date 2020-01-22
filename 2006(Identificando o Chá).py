tipo = int(input())
nota = input().split()
cont = 0
for i in nota:
    if int(i) == tipo:
        cont += 1
print(cont)
