from random import shuffle
n1 = str(input('Primeiro Aluno : '))
n2 = str(input('Segunda Aluno : '))
n3 = str(input('Terceiro Aluno : '))
n4 = str(input('Quarta Aluna : '))
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação sera : ')
print(lista)