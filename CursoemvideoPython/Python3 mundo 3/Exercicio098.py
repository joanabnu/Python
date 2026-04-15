from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de Inicio {inicio} ate {fim} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end=' ', flush=True)
            sleep(0.3)
            cont +=passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end=' ', flush=True)
            sleep(0.3)
            cont -=passo
        print('Fim')




contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizado a contagem! ')
init = int(input('Inicia : '))
final = int(input('Fim : '))
pas = int(input('Passo : '))
contador(init,final,pas)