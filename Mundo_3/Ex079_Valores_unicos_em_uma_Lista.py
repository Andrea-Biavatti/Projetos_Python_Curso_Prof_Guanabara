# Crie um programa onde o usuário possa digitar vários VALORES NUMÉRICOS e cadastre-os em uma LISTA.
# Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO.
# No final, serão exibidos todos os VALORES ÚNICOS digitados em ORDEM CRESCENTE.


números = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Opção inválida. Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print('-='*30)
números.sort()
print(f'Você digitou os valores {números}')
