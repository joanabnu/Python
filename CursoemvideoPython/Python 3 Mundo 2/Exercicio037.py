print('1 - binario\n2 - octal \n3 - Hexadecimal')
escolha = int(input('\no Informe a base de conversão :  '))
num = int(input('Escolhar um numero : '))

if escolha == 1:
    print('Numero : {} Convertido para Binario : {}'.format(num,bin(escolha)[2:]))
elif escolha == 2:
    print('Numero : {} Convertido para Octal : {}'.format(num,oct(num)[2:]))
elif escolha == 3:
    print('Numero : {} Convertido para Hexadecimal : {}'.format(num,hex(num)[2:]))
else:
    print('Numero Errado')
