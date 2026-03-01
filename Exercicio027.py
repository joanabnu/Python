nome = str(input('Digite seu nome completo : ')).strip()
n = nome.split()
print('O seu primeiro nome é : {} '.format(n[0]))
print('Seu ultimo nome é : {}'.format(n[len(n)-1]))
