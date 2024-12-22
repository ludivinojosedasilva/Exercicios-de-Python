#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
#custa R$60 por dia e R$0,15 por km rodado.
dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km rodados? "))
preço1 = 60*dias
preço2 = 0.15*km
pagamento = preço1+preço2
print("Você deve pagar R${} ".format(pagamento))