a = int(input('Primeiro valor : '))
b = int(input('Segundo valor : '))
c = int(input('Terceiro valor : '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor valor digitador é : {}'.format(menor))