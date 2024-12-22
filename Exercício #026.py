#Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
#Em que posição ela aparece pela primeira vez.
#Em que posição ela aparece a última vez.
frase = str (input("Digite uma frase: ")).upper().strip()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A letra A apareceu pela primeira vez na posição {}.".format(frase.find("A")+1))
print("A letra A apareceu pela última vez na posição {}.".format(frase.rfind("A")+1))
