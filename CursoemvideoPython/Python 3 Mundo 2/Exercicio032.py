casa = float(input('Informe o valor da casa : '))
salario = float(input('Informe o Salario : '))
anos = int(input('Informe os anos : '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {:.2f} anos'.format(casa,anos))

if prestacao <= minimo:
    print('O emprestimo sera concedido')
else:
    print('Emprestimo Negado')
   