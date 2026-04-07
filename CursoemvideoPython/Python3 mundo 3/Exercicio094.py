Agrupamento = list()
pessoa = dict()
soma = 0


while True:
        pessoa.clear()
        pessoa['Nome'] = str(input('Nome : ')).upper()[0]
        while True:
           pessoa['Sexo'] = str(input('Sexo : (M/F) : ')).upper()[0]
           if pessoa['Sexo'] in 'MF':
            break
           print('Erro! Por favor, digite apenas M ou F.')
       
        pessoa['idade'] = int(input('Idade : '))
        soma += pessoa['idade']

        Agrupamento.append(pessoa.copy())
        while True:
            resposta = str(input('Quer continuar S/N : ')).upper()[0]
            if resposta in 'SN':
              break
            print('Erro! Resposda apaenas S ou N')
        if resposta == 'N':
            break
print(Agrupamento)
media = soma / len(Agrupamento)
print(f'Media {media:5.2f}')
print('As mulheres cadastradas foram ',end='')
for p in Agrupamento:
    
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} e ', end='')

