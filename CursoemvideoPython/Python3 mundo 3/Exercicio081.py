lista = []

while True:
    n = int(input('Digite um valor na lista : '))
    lista.append(n)
    contin = str(input('sim/Não \nInforme se gostaria de prosseguir  : ')).upper().strip() 
    if contin =='N':
        break
print(f'O valores digitados : {lista}')
print(f'Quantidade de valores {len(lista)}')
lista.sort(reverse=True)
print(f'{lista}')
if 5 in lista:
   print('Foi encontrado o numero 5 ')
else:
    print('Não há numero 5 ')