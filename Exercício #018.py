#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
num = float(input("Digite o ângulo que você deseja: "))
n = math.radians(num)
sen = math.sin(n)
cos = math.cos(n)
tan = math.tan(n)
print("O seno desse ângulo é {:.2f} \n O cosseno desse ângulo é {:.2f} \n o tangente desse ângulo é {:.2f}".format(sen, cos, tan))