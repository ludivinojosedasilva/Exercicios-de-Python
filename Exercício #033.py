#Faça um programa que leia três números e mostre qual delas é maior e qual é menor.
a = int (input("Digite o primeiro valor: "))
b = int (input ("Digite o segundo valor: "))
c = int (input("Digite o terceiro valor: "))
#Verificando o menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando o maior
maior =a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))
#Também podemor fazer em forma de lista ordenada.
n1 = int (input("Digite o primeiro valor: "))
n2 = int (input ("Digite o segundo valor: "))
n3 = int (input("Digite o terceiro valor: "))
lista = [n1, n2, n3]
lista_ordenada = sorted(lista)
print("O menor valor digitado foi {}".format(lista_ordenada[0]))
print("O maior valor digitado foi {}".format(lista_ordenada[2]))