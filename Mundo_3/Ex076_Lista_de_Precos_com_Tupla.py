# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.


print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for posição in range (0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end='')
    else:
        print(f'R$ {listagem[posição]:>7.2f}')
print('-'*40)
