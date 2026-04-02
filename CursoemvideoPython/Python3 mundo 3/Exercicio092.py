from datetime import datetime

pessoa = dict()
situacao = 0
pessoa['Nome'] = str(input('Informe o seu nome : '))
pessoa['Nascimento'] = int(input('Informe ano nascimento : '))
pessoa['idade'] = datetime.now().year - pessoa['Nascimento']
pessoa['Carteira'] = int(input('Carteira de trabalho (0 não tem) : '))
    
if pessoa['Carteira'] == 0:
    pessoa[situacao] = 'Carteira inexistente'
    print('=='*25)
    for k, v in pessoa.items():
     
      print(f'{k} tem {v}')
else: 
   pessoa['Ano'] = int(input('Ano de contratação : '))
   pessoa['Salario'] =  float(input('Salario : '))

   pessoa['Aposentadoria'] = (pessoa['idade'] + pessoa['Ano'] + 35 - datetime.now().year)

   for k, v in pessoa.items():

      print(f'{k} tem {v}')

