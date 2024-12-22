#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
preço = float(input("Qual é o salário do funcionário:R$ "))
multiplicação = preço*15/100
salário = multiplicação+preço
print("Um funcionário que ganhava o salário de R${:.2f}, com o aumento de 15% passa a receber R${:.2f}".format(preço, salário))