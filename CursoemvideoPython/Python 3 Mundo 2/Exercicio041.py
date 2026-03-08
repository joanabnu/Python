from datetime import date 
atual = date.today().year
nasc = int(input('Informe seu ano de nascimento : '))
idade = atual - nasc

if idade <= 9:
    print('Categoria : Mirim')
elif idade <= 14:
    print('Categoria : Infantil')
elif idade <= 19:
    print('Categoria : Junior')
elif idade <= 25:
    print('Categoria : Sênior')
elif idade > 25:
    print('Categoria : Master')
print('O atleta tem {} anos'.format(idade))
