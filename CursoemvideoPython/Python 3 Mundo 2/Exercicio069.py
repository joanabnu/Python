idadecont = 0
Hcont = 0
fcont = 0
while True:
    print('=='*20)
    print('CADASTRE UMA PESSOA')
    print('=='*20)
    idade = int(input('idade : '))
    sexo = str(input('Sexo : ')).strip().upper()[0]
    
    if idade >= 18:
           idadecont +=1
    if sexo == 'M':
           Hcont +=1
    if sexo == 'F' and idade < 18:
           fcont +=1
    prosseguir = str(input('S/N \nQuer continuar ? ')).strip().upper()[0]
    if prosseguir != 'S':
        break
print(f'Total de pessoas com mais de 18 anos \nQuatidade: {idadecont} \nTotal de homens \nQuantidade {Hcont} \nTotal de mulheres menores de 18 anos \nQuantidade : {fcont}')
print('Acabou')
