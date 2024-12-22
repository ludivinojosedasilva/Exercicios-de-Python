#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro número é maior
# O segundo número é maior
# Não existe valor maior, os dois são iguais.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
print("Analisando os dois números...")
if n1 > n2:
    print ("O primeiro valor é maior de que o segundo valor.")
elif n2 > n1:
    print("O segundo valor é maior de que o primeiro valor")
elif n1 == n2:
    print("Ambos os valores são iguais.")
