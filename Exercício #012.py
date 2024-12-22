#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
preço = float(input("Qual é o preço do produto?R$ "))
multiplicação = preço*5
divisão = multiplicação/100
preço2 = preço-divisão
print("O produto que custava R${}, na promoção com o desconto de 5%, passa a custar R${:.2f}".format(preço, preço2))
