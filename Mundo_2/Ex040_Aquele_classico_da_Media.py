# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('Sua média foi {:.2f}. Você está \33[1;31mREPROVADO\33[m!'.format(média))
elif 7.0 > média >= 5.0:
    print('Sua média foi {:.2f}. Você está \33[1;36mEM RECUPERAÇÃO\33[m!'.format(média))
else:
    print('Sua média foi {:.2f}. Você está \33[1;32mAPROVADO\33[m!'.format(média))
