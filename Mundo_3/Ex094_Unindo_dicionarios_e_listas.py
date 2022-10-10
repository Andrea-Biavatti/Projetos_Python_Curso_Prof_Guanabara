# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista.
# No final, mostre:
# a) quantas pessoas foram cadastradas
# b) a média de idade do grupo
# c) uma lista com todas as mulheres
# d) Uma lista com todas as pessoas com idade acima da média.


galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda com apenas S ou N.')
    if resposta == 'N':
        break
print('-='*30)
print(f' A) Ao todo temos {len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f' B) A média de idade é de {média:5.2f} anos.')
print(' C) As mulheres cadastradas foram:')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}')
print()
print(' D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}; ')
        print()
print(' <<< ENCERRADO >>> ')
