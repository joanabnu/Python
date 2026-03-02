n1 = float(input('Digite a primeira nota : '))
n2 = float(input('Digite a primeira nota : '))
media = (n1 + n2) / 2
print('A sua media foi {:.1f} '.format(media))
if media >= 6.0:
    print('Sua media é : {} Parabens!! '. format(media))
else:
    print('Sua nota : {} \nSua media foi ruim! Estude mais!'.format(media))