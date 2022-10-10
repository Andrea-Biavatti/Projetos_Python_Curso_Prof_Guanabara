# Crie um programa onde o usuário possa digitar cinco VALORES NUMÉRICOS e cadastre-os em uma LISTA.
# Já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.


list = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitado em ordem foram {list}')
