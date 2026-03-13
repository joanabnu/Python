quantValor = soma = 0
while True:
   print('=='*20)
   print('LOJA SUPER BARATÃO')
   print('=='*20)
   produto = str(input('Nome do produto : '))
   valor = float(input('Preço : '))
   if valor >= 1000:
      quantValor +=1
   soma += valor
   prosseguir = str(input('S/N \nQuer prosseguir : ')).strip().upper()[0]
   if prosseguir != 'S':
      break
print(f'Total da comprar : {soma} \nProduto custando mais R$1.000 \n Quantidade : {quantValor}')