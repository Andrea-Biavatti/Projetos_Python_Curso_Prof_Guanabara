# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temp = float(input('Informe a temperatura em C: '))
f = ((9 * temp) / 5) + 32
print('A temperatua de {} C corresponde a {} F!'.format(temp, f))
