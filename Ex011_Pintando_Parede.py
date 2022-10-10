# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

lg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
a = lg * alt
t = a / 2
print('A área a ser pintada é de {:.1f} m². Você precirá de {:.2f} litros de tinta.'.format(a, t))
