# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date
atual = date.today().year
print('-=-'*20)
print('ALISTAMENTO MILITAR')
print('-=-'*20)
sexo = print('''Escolha uma das opções:
[ 1 ] sexo MASCULINO
[ 2 ] sexo FEMININO''')
opção = int(input('Sua opção: '))
if opção == 1:
    nasc = int(input('Ano de nascimento: '))
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Você tem que se alistar imediatamente!')
    elif idade < 18:
        saldo = 18 - idade
        print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))
    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}.'.format(ano))
elif opção == 2:
    print('Você não precisa realizar alistamento militar.')
else:
    print("Opção errada. Tente novamente.")
