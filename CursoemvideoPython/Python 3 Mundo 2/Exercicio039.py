from datetime import date 
atual = date.today().year
nascimento = int(input('Ano de nascimento : '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {} '.format(nascimento,idade,atual))

if (idade == 18):
    print('Voce tem que se alistar Imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Voce ainda nao tem 18 anos.Ainda falta {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))