# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
me = (n1 + n2) / 2
print('A primeira nota do aluno foi {:.1f} e a segunda nota foi {:.1f}. A média final é {:.1f}.'.format(n1, n2, me))
