#Criar Conversor de Moedas- Reais R$, Euro €, Dólar Americano U$$ e Franco CFA
n= float(input("Quanto de dinheiro você tem na sua carteira ? R$ "))
e= n*0.1784
d= n*0.1935
f= n*117.0381
print("Fazendo câmbio de {}R$, teremos: \n{:.3f}€ \n{:.3f}U$$ \n{:.3f}CFA".format(n, e, d, f))
