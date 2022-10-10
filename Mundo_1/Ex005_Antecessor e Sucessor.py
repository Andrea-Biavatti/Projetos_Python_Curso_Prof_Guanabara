# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O número digitado foi {}. O número antecessor é {} e o sucessor é {}'.format(n, a, s))

n = int(input('Digite um número: '))
print('O número digitado foi {}. O número antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
