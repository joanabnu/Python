# def lin():
#     print('='*30)


def mensagem(msg):
    print(msg)


mensagem(' => Aprendendo Python <= ')


def  soma(a,b):
   s = a + b
   print(f'Os valores foram : A = {a} e B = {b}')
   print(f'A soma :  {s}')


soma(a=4,b=5)
soma(b=8,a=9)
soma(a=2,b=1)
print('='*30)
def contador(* num):
    a = len(num)
    print(f' são ao todo \n {a}° : {num}',end=' ')
    

contador(2,7,9)
contador(4,9,6,9)
contador(2,5,4,9,8)

