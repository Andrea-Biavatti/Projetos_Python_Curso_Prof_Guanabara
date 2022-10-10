# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
if num1 > num2:
    print('O \33[34mprimeiro\33[m valor é maior')
elif num1 < num2:
    print('O \33[35msegundo\33[m valor é maior')
else:
    print('Os dois números são \33[36miguais\33[m')
