# Crie um programa que faça o computador jogar Jokenpô com você.


from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-='*20)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}.'.format(itens[jogador]))
print('-='*20)
if computador == 0: # computador jogou pedra
    if jogador == 0: # jogador jogou pedra
        print('EMPATE')
    elif jogador == 1: # jogador jogou papel
        print('O JOGADOR VENCEU!')
    elif jogador == 2: # jogador jogou tesoura
        print('O COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou papel
    if jogador == 0:  # jogador jogou pedra
        print('O COMPUTADOR VENCEU')
    elif jogador == 1:  # jogador jogou papel
        print('EMPATE!')
    elif jogador == 2:  # jogador jogou tesoura
        print('O JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA!')
else: # computador jogou tesoura
    if jogador == 0:  # jogador jogou pedra
        print('O JOGADOR VENCEU')
    elif jogador == 1:  # jogador jogou papel
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:  # jogador jogou tesoura
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')
