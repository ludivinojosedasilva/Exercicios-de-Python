#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre
# seu status de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
peso = float (input("Qual é o seu peso? (Kg) "))
altura = float (input("Qual é a sua altura? (m) "))
imc = peso / (altura ** 2) #IMC - significa Índice de Massa Corporal
print("O IMC dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5:
    print("Você está ABAIXO DO PESO NORMAL")
elif 18.5 <= imc < 25:
    print("PARABÉNS! Você está na faixa de PESO NORMAL")
elif 25 <= imc <30:
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("você está em OBESIDADE!")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, CUIDADO!")
    