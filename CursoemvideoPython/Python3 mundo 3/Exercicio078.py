menor =  maior = 0
valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor {cont}° : ')))

for c, v in enumerate(valores):

    if  c == 0:
          maior = menor = valores[c]
    
    else:
        if valores[c] > maior:
           maior = valores[c]
          
        if valores[c] < menor:
            menor = valores[c]

print(f'Valores digitados foram {valores} ')
print('--'*30)
for i, v in enumerate(valores):
    if v == maior: 
       print(f'O maior valor digitado : {maior} nas posicao {i}...') 


for i, v in enumerate(valores):
    if v == menor:
       print(f'O menor valor digitado : {menor} na posicao {i}...')    

          
