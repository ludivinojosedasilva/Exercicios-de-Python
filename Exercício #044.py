#Elabore um programa que calcule o valor a ser pago por um produto,
#considerando o seu preço normal e condição de pagamento:
# Á vista dinheiro / cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de Juros
print ( "{:=^40}".format(" LOJAS LUDIVINO "))
preço = float(input("Digite o preço de Compras: R$ "))
print(""" Formas de  PAGAMENTO 
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
opção = int(input("Qual é a opcão? "))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print("A sua compra de R${} parcelada em 2x vai custar R${:.2f} para cada parcela".format(preço, parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input("Quantas parcelas? "))
    parcela = total / totparc
    print("A sua compra de R${} parcelada em {}x vai custar R${:.2f} para cada parcela".format(preço, totparc, parcela))
else:
    total = preço
    print("\033[4;33;41m OPÇÃO INVÁLIDA DE PAGAMENTO. TENTE NOVAMENTE!\033[m")
print("Sua Compra de R${:.2f} vai custar R${:.2f} no final.".format(preço, total))
