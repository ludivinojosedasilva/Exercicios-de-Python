#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.
velocidade = float(input("Digite a velocidade atual do seu carro: "))
if velocidade <= 80:
  print("Boa Viagem! Dirija com segurança!")
else:
  print("Multado! Você excedeu o limite permitido que é de 80Km/h")
  multa = (velocidade - 80)*7
  print("Você deve pagar uma multa no valor de R${:.2f}!".format(multa))