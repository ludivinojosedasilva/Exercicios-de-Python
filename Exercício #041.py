#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre 
# sua categoria de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19  anos: Junior
# Até 25 anos: Sênior
# Acima: Master
from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = atual - nascimento
print ("O atleta tem {} anos de idade.".format(idade))
if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JÚNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
