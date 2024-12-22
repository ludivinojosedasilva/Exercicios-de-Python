# Crie um programa que faça o computador jogar JOKENPÔ com você.
from emoji import emojize
from random import randint
from time import sleep
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input("Qual é a sua Jogada? "))
print("JO 🤜🤛")
sleep(1)
print("KEN 🤜🤛")
sleep(1)
print("PÔ! ")
print("-="*14)
print("O computador escolheu {}".format(itens[computador]))
print("O jogador escolheu {}".format(itens[jogador]))
print("-="*14)
if computador == 0: #Computador jogou PEDRA
    if jogador == 0:
        print("EMPATE 🤝")
    elif jogador == 1:
        print("JOGADOR VENCEU 😎🥳🎉")
    elif jogador == 2:
        print("COMPUTADOR VENCEU 😂")
    else:
        print("JOGADA INVÁLIDA")

elif computador == 1: #Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCEU 😂")
    elif jogador == 1:
        print("EMPATE 🤝")
    elif jogador == 2:
        print("JOGADOR VENCEU 😎🥳🎉")
    else:
        print("JOGADA INVÁLIDA")

elif computador == 2: #Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCEU 😎🥳🎉")
    elif jogador == 1:
        print("COMPUTADOR VENCEU 😂")
    elif jogador == 2:
        print("EMPATE 🤝")
    else:
        print("JOGADA INVÁLIDA")


