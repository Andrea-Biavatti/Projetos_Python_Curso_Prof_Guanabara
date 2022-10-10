# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um número: '))
unid = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
milhar = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(unid))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(milhar))