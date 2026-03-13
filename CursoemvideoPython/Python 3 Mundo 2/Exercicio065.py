cont = 1
media = 0
maior = 0
menor = 0
num = int(input('Digite um numero : '))
prosseguir = str(input('Gostaria de proseguir S/N')).upper()
while prosseguir == 'S':
    num = int(input('Digite um numero : '))
    prosseguir = str(input('Gostaria de proseguir S/N')).upper().strip()[0]
    cont +=1
    media = (num + num) / cont
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print('Maior valor : {} \nMenor valor : {} \nMedia : {} \nQuantidade {}'.format(maior,menor,media,cont))
    

