# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Qual o preço do produto R$ '))
pgto = print('''Qual a opção de pagamento desejada? 
[ 1 ] À vista, com dinheiro ou cheque
[ 2 ] À vista no cartão
[ 3 ] Parcelado em até 2x no cartão
[ 4 ] Parcelado em 3x ou mais no cartão''')
opção = int(input('Qual a opção escolhida? '))
if opção == 1:
    valor = preço - (preço * 10 / 100)
    print('O valor a ser pago será de R$ {:.2f}'.format(valor))
elif opção == 2:
    valor = preço - (preço * 5 / 100)
    print('O valor a ser pago será de R$ {:.2f}'.format(valor))
elif opção == 3:
    print('O valor a ser pago será de R$ {:.2f}, dividido em 2 parcelas de R$ {:.2f} cada uma.'.format(preço, (preço / 2)))
elif opção == 4:
    parc = int(input('Em quantas parcelas você deseja efetuar o pagamento? '))
    valor = preço + (preço * 20 / 100)
    print('O valor a ser pago será de R$ {:.2f}, dividido em {} parcelas de R$ {:.2f} cada uma.'.format(valor, parc, (valor / parc)))
else:
    print('Opção inexistente. Tente novamente.')
