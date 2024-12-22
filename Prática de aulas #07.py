n1 = int(input("Digite um valor: ")) 
n2 = int(input ("Digite outro valor: "))
s= n1+n2
m= n1-n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("O resultados são: soma {} , multiplicação {}, divisão {}, divisão inteira {} e exponenciação {}".format(s, m, d, di, e))
print ("A divisão inteira é igual a {} e potência é igual a {}". format(di, e))
#{:.3f} isso mostra que só queremos 3 casas decimais depois do ponto, naquele resultado.
#também podemos escrever assim : end= "  " assim tudo vai continuar na mesma linha
Podemos colocar \n para fazer quebra de linha.