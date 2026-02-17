preco = float(input('Informe o valor do produto : R$'))
desconto = preco - (preco * 5 / 100)
print('O valor do produto é : {:.2}\nO produto com desconto é : {:.2} '.format(preco,desconto))