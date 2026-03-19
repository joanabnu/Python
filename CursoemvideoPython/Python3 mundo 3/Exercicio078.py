menor =  maior = 0
valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor {cont+1}° : ')))

for c, v in enumerate(valores):

    if  c == 0:
          maior = menor = valores[c]
    
    else:
        if valores[c] > maior:
           maior = valores[c]
           print(f'O menor valor : {v} esta na posicao {c}')
        if valores[c] < menor:
            menor = valores[c]

print(f'Valores digitados foram {valores}') 
print(f'O maior valor digitado : {maior}')  
print(f'O maior valor digitado : {menor}')    
          
