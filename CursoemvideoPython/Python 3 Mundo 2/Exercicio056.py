mediaIdade = 0
maiorIdade = 0
totalF = 0
maioridadehomen = 0
nomeVelho = ''
for c in range(1,4):
    print('-------- {}° Pessoa --------'.format(c,))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('[M/F\nSexo:')).upper()
    mediaIdade = (idade +idade ) / 4
    if c == 1 and sexo in 'M':
        maioridadehomen = idade
        nomeVelho = nome
    if sexo in 'M' and idade > maioridadehomen:
        maioridadehomen = idade
        nomeVelho = nome
    if sexo == 'F' and idade > 20:
        totalF += 1

print('Media de idade é {} \nTotal de mulheres : {}'.format(mediaIdade,totalF))
print('O homen mais velho tem {} anos e se chama {}.'.format(maioridadehomen,nomeVelho))

  

