lista = []
for n in range(2, 101):
  lista.append(1/n)
  soma = sum(lista)
  s = 1 + soma
print("%.2f" %s)