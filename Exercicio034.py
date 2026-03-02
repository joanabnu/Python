salario = float(input('Informe o seu salario : '))
if salario <= 1250:
  ajuste = salario + ( salario * 15 / 100)
else:
  ajuste = salario +(salario * 10)/ 100
print('O seu salario anterior : \033[0;33;44m{}\033[m \nAjuste salario : {} '.format(salario,ajuste))
