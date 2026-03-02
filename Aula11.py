# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# style 0 = none - 1 = bold -  4 = Uderline -  7 = negativo
# text 30 =  branco - 31 = vermelho - 32 = verde - 34 = azul - 35 = lilas - 36 =  azul claro - 37 = cinza
#  back 40 = branco - 41 = vermelho - 42 =  verde - 43 = amarelho - 44 = azul escuro -  45 = lilas - 46 = azul claro - 47 - cinza

# print('\033[31mOlá mundo')
#  print('\033[1;31;43mOlá a todos')
#  print('--'*30)
print('\033[4;30;45mOlá de novo!\033[m')