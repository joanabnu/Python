quantValor = menor = soma = barato = cont = 0
while True:
   print('=='*20)
   print('LOJA SUPER BARATÃO')
   print('=='*20)
   produto = str(input('Nome do produto : '))
   valor = float(input('Preço : '))
   cont+=1
   if cont == 1:
      menor = valor
   else:
      if valor < menor:
         menor = valor
         barato = produto
   if valor >= 1000:
      quantValor +=1     
   soma += valor
   prosseguir = str(input('S/N \nQuer prosseguir : ')).strip().upper()[0]
   if prosseguir != 'S':
      break
print('=='*20)
print('fim')
print('=='*20)
print(f'Total da comprar : {soma} \nProduto custando mais R$1.000 \nQuantidade : {quantValor} \nO produto mais barata \nNome : {barato} Valor : {menor}')