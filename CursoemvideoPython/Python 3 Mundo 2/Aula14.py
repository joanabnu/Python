c = 1
while c < 11:
    print(c)
    c +=1
par = 0
impar = 0
n = 1
while n != 0:
    n = int(input('Digite um valor : '))
    if n % 2 == 0:
        par += 1
    else: 
        impar += 1
print('Numero par: {} \nNumero impar {}'.format(par,impar))

print('Fim')