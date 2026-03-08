peso = float(input('Informe o seu peso : '))
altura = float(input('Informe a sua altura : '))

imc = peso / (altura**2)

if imc < 18.5:
    print('Status : Abaixo {:.2f}'.format(imc))
elif imc <=25: 
    print('Status : Ideal {:.2f}'.format(imc))
elif imc <=30:
    print('Status : Sobrepeso {:.2f}'.format(imc))
elif imc <= 40:
    print('Status : Obesidade {:.2f}'.format(imc))
else:
    print('Status : Acima {:.2f}. Obesidade mórbida'.format(imc))