#Crie um programa que leia duas notas do aluno e calcule a sua média,
#mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
n1 = float (input("Primeira nota: "))
n2 = float (input("Segunda nota: "))
média = (n1 + n2) / 2
print("O aluno que teve a primeira nota de {:.1f} valores e a segunda de {:.1f} valores, a sua média é de {:.1f} valores.".format(n1, n2, média))
if média >=5 and média <7: # tamém podemos escrever essa fórmula assim: 7 > média >=5:
     print("O aluno está em \033[1;33m RECUPERAÇÃO \033[m.")
elif média < 5:
     print("O aluno está \033[1;31m REPROVADO\033[m.")
elif média >=7:
    print("O aluno está \033[1;32m APROVADO \033[m.")
