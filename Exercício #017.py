#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retânglo
#calcule e mostre o comprimento da hipotenusa.
import math
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
s = math.hypot(co, ca)
print("A hipotenusa vai medir {:.2f}".format(s))