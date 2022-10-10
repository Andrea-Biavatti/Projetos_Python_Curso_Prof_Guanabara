# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O número digitado foi {}. O dobro desse número é {}, \no triplo é {} e a raiz quadrada é {:.2f}'.format(n, d, t, rq))

n = int(input('Digite um número: '))
print('O número digitado foi {}. O dobro desse número é {}, \no triplo é {} e a raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), (pow(n, (1/2)))))
