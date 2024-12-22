#Desenvolva um programa que pergunte a distância de uma viagem me Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas. 
n = float(input("Digite a distância da sua viagem: "))
print("Você está prestes a começar uma viagem de {}km ".format(n))
if n<=200:
    valor1= n*0.50
    print("A sua passagem custa R${:.2f}".format(valor1))
else:
    valor2= n*0.45
    print("A sua passagem custa R${:.2f}".format(valor2))