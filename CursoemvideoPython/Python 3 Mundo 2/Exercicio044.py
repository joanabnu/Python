print('==' * 10, 'MERCADINHO', '==' *10)
compra = float(input('Preço da Compras : '))
opcao = int(input('[1] à vista dinheiro\n[2] à cartao a vista \n[3] 2X no cartao de credito \n[4] 3x ou mais no cartão \nQual é a opção ? '))

if opcao == 1:
    desconto = compra - (compra * 10 / 100)
    print('O valor da sua comprar: {} \nO desconto : {} '.format(compra,desconto))
elif opcao == 2:
   desconto = compra - (compra * 5 / 100)
   print('O valor da compra : {} \nO valor do desconto : {}'.format(compra,desconto))
elif opcao == 3:
    desconto = compra +(compra *5 /100)
    print('O valor da sua compra : {} \nO valor do desconto : {}'.format(compra,desconto))
elif opcao == 4:
    
    desconto = compra +(compra * 10 /100)
    print('O valor da sua compra : {} \nO valor do desconto : {}'.format(compra,desconto))
else:
    print('Incorreto! ')
print('{:=^40}'.format('MERCADINHO'))
