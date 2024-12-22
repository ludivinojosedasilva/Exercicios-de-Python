#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A pretação mensal, não pode exceder 30% do salário ou então o emprestimo será negado.
casa = int(input("Qual é o valor da casa?R$ "))
salário = int(input("Qual é o seu salário?R$ "))
anos = int(input("Em quantos anos você quer pagar? "))
prestação = casa / (anos * 12)
mínimo = (salário * 30) / 100
if prestação > mínimo:
    print("Emprestimo negado!")
else:
    print("Emprestimo Aceitado! ")
print("Para pagar uma casa de R${} em {} anos. ".format(casa, anos))
print("A prestação será de R${}.".format(prestação))
