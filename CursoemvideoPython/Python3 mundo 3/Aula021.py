def contador(i,f,p):

    c = i 
    while c <=f:
        print(f'{c} -', end=' ')
        c+=p
    print('fim')

contador(2,10,2)
help(contador)
print('='*25)
def somar(a=0,b=0,c=0):
    s = a + b + c
    print(f'A soma valle {s}')


somar(5,5,5)
somar(3,2)
print('='*25)
def teste():
    print(f'O valor de {n}')


n=2
print(f'Na função teste {n}')
teste()

print('='*25)

def somar(a=0,b=0,c=0):
    s = a + b + c
    return s


print(somar(3,3,3))

print('='*25)

def fatorial(num=1):
    f=1
    for c in range(num,0,-1):
        f *=c
    return f

n= int(input('Digite um numero : '))
print(f'O fatorial de {n} é igual {fatorial(n)}')