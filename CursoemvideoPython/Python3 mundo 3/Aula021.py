def contador(i,f,p):

    c = i 
    while c <=f:
        print(f'{c} -', end=' ')
        c+=p
    print('fim')

contador(2,10,2)
help(contador)

def somar(a,b,c=0):
    s = a + b + c
    print(f'A soma valle {s}')


somar(5,5,5)
somar(3,2)