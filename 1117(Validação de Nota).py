count = 0

media = 0

while count < 2:

    nota = float(input())

    if nota >= 0 and nota <= 10:

        count = count + 1

        media = float(media + nota)

    else:

        print('nota invalida')

print('media = {:.2f}'.format(media/2))