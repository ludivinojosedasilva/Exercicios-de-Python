#Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo nome: "))
n3 = str(input("Terceiro nome: "))
n4 = str(input("Quarto nome: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))