nome = str(input('Digite o seu nome completo: ')).strip()
print('O seu nome é : {}\nO seu nome com letra maiuculas : {}\nO seu nome com letras minuculas {}\nQuantas letras tem o seu nome : {}\nSeu primeiro nome tem {}'.format(nome,nome.upper(),nome.lower(),len(nome)-nome.count(' '),nome.find(' ')))

print('Utilizando split()')
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letra'.format(separa[0], len(separa[0])))