cont = 0
media = 0
maior = 0
menor = 0
soma =0
prosseguir ='S'
while prosseguir == 'S':
    num = int(input('Digite um numero : '))
    cont +=1
    soma += num
 
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
           maior = num
        if num < menor:
           menor = num
    
    prosseguir = str(input('Gostaria de proseguir S/N : ')).upper().strip()[0]
media = soma / cont
print('Maior valor : {} \nMenor valor : {} \nMedia : {} \nQuantidade {}'.format(maior,menor,media,cont))
    

