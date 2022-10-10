# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de Quilômetros percorridos: '))
dias = float(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
pago = (km * 0.15) + (dias * 60)
print("O valor total a ser pago será de R$ {:.2f}".format(pago))
