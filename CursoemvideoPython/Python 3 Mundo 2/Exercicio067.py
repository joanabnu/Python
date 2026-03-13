n = cont = tabu= 0

while True:
    print('=='*15)
    n = int(input('Quer ver a tabuada de qual valor : '))
    print('=='*15)
    if n < 0:
        break
    cont = 0
    while cont <=10:

        print('{} X {} = {}'.format(n,cont,n*cont))
        cont+=1
  
print('Tabuada encerrada, Volte sempre')