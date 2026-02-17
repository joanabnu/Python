larg = float(input('Largura da parede : '))
alt = float(input('Altura da parede : '))
area = larg * alt
print('Sua parede tem dimensao de {} X {} e sua area é de  {}m'.format(larg, alt,area))
tinta = area / 2
print('Para pintar essa parede voce precisa de {} de tinta '.format(tinta))