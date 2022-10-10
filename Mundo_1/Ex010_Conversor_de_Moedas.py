# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

d = float(input('Quantos reais você possui? R$ '))
dol = d / 3.27
print('Vocé poderá comprar US$ {:.2f} .'.format(dol))
