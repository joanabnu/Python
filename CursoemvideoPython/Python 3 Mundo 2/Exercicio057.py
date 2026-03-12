sexo = str(input('Informe o seu sexo : ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe o seu sexo : ')).strip().upper()[0]
print('Sexo registrado com sucesso : {}'.format(sexo))