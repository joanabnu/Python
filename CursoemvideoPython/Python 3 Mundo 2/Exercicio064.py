num = 0
cont = 0
soma = 0
print('Digite 999 para sair')
num = int(input('Digite um numero : '))
while num != 999:
    num = int(input('Digite um numero : '))
    cont +=1
    soma = num + num
    
print('Quantidade de numero digitados : {} \nA soma entre eles é {}'.format(cont,soma))