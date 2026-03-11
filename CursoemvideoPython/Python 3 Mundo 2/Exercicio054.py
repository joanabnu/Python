from datetime import date 
atual = date.today().year
idade = 0
menor = 0
maior = 0
ano = 0
for c in range(1,8):
  ano = int(input('Informe o ano de nascimento : '))
  print('Pessoa {} \nAno de nascimento : {}'.format(c,ano))
  idade = ano - atual
  if idade < 18:
   menor +=1
  elif idade > 18:
   maior +=1
print('Quantidade de pessoa maior de idade é : {} \nQuantidae de pessoa menor de idade é : {}'.format(menor, maior))
  
   