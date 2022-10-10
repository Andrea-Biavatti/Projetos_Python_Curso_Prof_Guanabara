# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta 
# e mostre sua categoria, de acordo com a idade: 
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER


from datetime import date
atual = date.today().year
nasc = int(input("Qual a data de nascimento do atleta? "))
idade = atual - nasc
print('Esse atleta tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Sua categoria é \033[1;31mMIRIM\033[m.')
elif idade <= 14:
    print('Sua categoria é \033[1;32mINFANTIL\033[m.')
elif idade <= 19:
    print('Sua categoria é \033[1;33mJUNIOR\033[m.')
elif idade <= 25:
    print('Sua categoria é \033[1;34mSÊNIOR\033[m.')
else:
    print('Sua categoria é \033[1;35mMASTER\033[m.')
