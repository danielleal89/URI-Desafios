alcool = 0
gasolina = 0
diesel = 0
count = 0
while count != 4:
    count = int(input())
    if count == 1:
        alcool += 1
    if count == 2:
        gasolina += 1
    if count == 3:
        diesel += 1
 #   elif count == 4:
print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcool))
print('Gasolina: {}'.format(gasolina))
print('Diesel: {}'.format(diesel))