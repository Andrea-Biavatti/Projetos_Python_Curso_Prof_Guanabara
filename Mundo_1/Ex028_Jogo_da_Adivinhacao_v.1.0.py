# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e # peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.


from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'* 20)
jogador = int(input('Em qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Ganhei, eu pensei no número \033[1;32m{}\033[m e não no \033[1;31m{}\033[m!'.format(computador, jogador))
