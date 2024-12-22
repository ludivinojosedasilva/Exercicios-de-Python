#Refaça o desafio #035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno: todos os lados diferentes.
n1 = int(input("Digite o valor do primeiro lado: "))
n2 = int(input("Digite o valor do segundo lado: "))
n3 = int(input("Digite o valor do terceiro lado: "))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print("Os valores PODEM FORMAR UM TRIÂNGULO.")
    if n1 == n2 == n3:
        print("O triângulo que podem formar é o TRIÂNGULO EQUILÁTERO")
    elif n1 != n2 != n3 != n1:
        print("O triângulo que podem formar é o TRIÂNGULO ESCALENO")
    else:
        print("O triângulo que podem formar é o TRIÂNGULO ISÓSCELES")
else:
    print("Os valores NÃO PODEM FORMAR UM TRIÂNGULO.")
    