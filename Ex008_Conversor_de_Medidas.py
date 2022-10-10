# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite a metragem: '))
c = n * 100
m = n * 1000
print('A metragem digitada foi {}. Isso equivale a {} centímetros ou {} milímetros.'.format(n, c, m))
