from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de Inicio {inicio} ate {fim} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.2)
            cont +=passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end=' ', flush=True)
            sleep(0.2)
            cont -=passo
        print('Fim')




contador(1,10,1)
contador(10,0,2)