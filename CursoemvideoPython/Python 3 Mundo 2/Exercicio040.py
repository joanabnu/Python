primeiraNota = float(input('Digite a 1° Nota : '))
segundaNota = float(input('Digite a 2° Nota : '))
media = (primeiraNota + segundaNota) /2

if media > 7:
    print('Parabens voce passou!!')
elif media >= 5 and media < 7: 
    print('Recuperaçaõ')
elif media < 5:
    print('Reprovado')
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.f}}'.format(primeiraNota,segundaNota,media))