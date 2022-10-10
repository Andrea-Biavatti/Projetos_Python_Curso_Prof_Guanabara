# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores PARES e os valores IMPARES digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.


números = []
pares = []
impares = []
while True:
    números.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Opção inválida. Por favor, informe se deseja continuar. [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for i, v in enumerate(números):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {números}')
pares.sort()
print(f'A lista de pares é {pares}')
impares.sort()
print(f'A lista de ímpares é {impares}')
