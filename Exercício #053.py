# Crie um programa que leia uma frase qualquer e diga se ela é políndromo, desconsiderando os espaços.
# APOS A SOPA     A SACADA DA CASA     A TORRE DA DERROTA   O LOBO AMO O BOLO      ANOTARAM A DATA DA MARATONA.
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
"""#tambem podemos fazer assim: 
inverso = ""
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]"""
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("Temos um PALÍNDROMO!")
else:
    print("A frase NÃO É UM PALÍNDROMO!")
    print(junto, inverso)
