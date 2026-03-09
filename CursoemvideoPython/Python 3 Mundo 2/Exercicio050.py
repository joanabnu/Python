soma = 0
cont = 1
for c in range(1,7):
    num = int(input('Digite um valor : '))
    if num % 2 == 0:
      soma += num
      cont += 1
print('Quantidade de Numero: {}\n Numeros {}\nA soma : {}'.format(cont,num,soma))