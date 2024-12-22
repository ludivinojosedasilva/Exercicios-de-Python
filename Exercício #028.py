#Escreva um programa que faça o computador "PENSAR" em um número inteiro entre 0 a 5 e peça o usuário
#tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
import emoji
n= random.randint(0, 5)
print("-=-="*20)
print("Vou pensar em um número entre 0 a 5. Tente adivinhar...")
print("-=-="*20)
n1 = int(input("Em que número você pensou: "))
if  n1>5:
    print("Digite o número válido")
print("-=-="*20)
if n1<=5:
    print("PROCESSANDO...")
sleep(3)
print("O número que o computador escolheu é {}".format(n))
print("O número que você escolheu é {}".format(n1))
print("Venceu 🤑🎉"if n == n1 else "Perdeu 😭😭")
