#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta 
#necessária para pintá-la, sabendo que cada litro de tinta, pinta 2m quadrado.
largura = float(input("Digite a largura de parede: "))
altura = float(input("Digite a altura de parede: "))
área = largura*altura
litro = área / 2
print ("A sua parede tem a dimensão de {} X {}, portanto a área desse parede é de {}m quadrado".format(largura, altura, área))
print ("A quantidade necessária de tinta para pintar essa parede é de {}L".format(litro))
