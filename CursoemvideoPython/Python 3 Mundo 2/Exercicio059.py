n1 = int(input('Primeiro valor : '))
n2 = int(input('Segundo valor : '))
opcao = 0
soma = 0
mult = 0
maior = 0
while opcao != 5:
    print('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Nova numeros \n[5] Sair do pragramar')
    opcao = int(input('Qual é sua opção : '))
    if opcao == 1:
         soma = n1 + n2
         print('\033[35mA soma {} entre {} e {} '.format(soma,n1,n2))
    elif opcao == 2:
         mult = n1 * n2
         print('\033[32mO valor da multiplicação : {}'.format(mult))
    elif opcao == 3:
         if n1  > n2:
            maior = n1
            print('\033[34mO maior valor é {}'.format(n1))
         else:
            maior = n2
            print('O maior valor é {}'.format(n2))
    elif opcao == 4:
         print('Informe novos numeros')
         n1 = int(input('Primeiro valor : '))
         n2 = int(input('Segundo valor : '))
         
print('Acabou')
