#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. 
#Faça um programa que leia o nome dos quatros alunos e mostre a ordem sorteada.
import random
a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")
lista = [a, b, c, d]
escolhido =random.shuffle(lista)
print("Essa é a ordem escolhida para apresentação: {}".format(lista))
