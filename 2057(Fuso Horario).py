a, b, c = input().split()
calculo = int(a) + int(b) + int(c)
if calculo < 0:
    print(24 + calculo)
elif calculo > 24:
    print(calculo - 24)
else:
    print(calculo)
