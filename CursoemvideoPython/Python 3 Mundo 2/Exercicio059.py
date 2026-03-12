print('{:=^40}'.format('Informando Valores'))
n1 = int(input('Primeiro valor : '))
n2 = int(input('Segundo valor : '))

opcao = 0
soma = 0
mult = 0
maior = 0
while opcao != 5:
    print('{:=^40}'.format('Menu'))
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Nova numeros \n[5] Sair do pragramar')
    print('{:=^40}'.format('Informe a Opção'))
    opcao = int(input('Qual é sua opção : '))
    if opcao == 1:
         soma = n1 + n2
         print('\033[1;35;46mA soma {} entre {} e {} '.format(soma,n1,n2))
    elif opcao == 2:
         mult = n1 * n2
         print('\033[1;36;43mO valor da multiplicação : {}'.format(mult))
    elif opcao == 3:
         if n1  > n2:
            maior = n1
            print('\033[1;32;46mO maior valor é {}'.format(n1))
         else:
            maior = n2
            print('O maior valor é {}'.format(n2))
    elif opcao == 4:
         print('{:=^40}'.format('Digite novamente'))
         n1 = int(input('Primeiro valor : '))
         n2 = int(input('Segundo valor : '))
         
print('Acabou')
