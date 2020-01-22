inicio = input().split(' ')
i = input().split(':')
fim = input().split(' ')
f = input().split(':')

# DIAS --------------------------------------
dias = int(fim[1]) - int(inicio[1])

# HORAS -------------------------------------
if int(i[0]) > int(f[0]):
    horas = 24 - (int(i[0]) - int(f[0]))
    dias -= 1
else:
    horas = int(f[0]) - int(i[0])

# MINUTOS -----------------------------------
if int(i[1]) > int(f[1]):
    minutos = 60 - (int(i[1]) - int(f[1]))
    horas -= 1
else:
    minutos = int(f[1]) - int(i[1])

# SEGUNDOS ----------------------------------
if int(i[2]) > int(f[2]):
    segundos = 60 - (int(i[2]) - int(f[2]))
    minutos -= 1
else:
    segundos = int(f[2]) - int(i[2])

if dias == 0 and horas == 0 and minutos == 0:
    exit()
print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(minutos))
print('{} segundo(s)'.format(segundos))
