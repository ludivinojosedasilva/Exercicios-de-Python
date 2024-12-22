n= input ('Digite algo: ') # chama se Objeto 
print('O  tipo primitivo desse valor é ', type(n)) #tudo que tem is é chamado de método 
print('Só tem espaços?', n.isspace())
print ('É um número ?', n.isnumeric())
print('É alfabético ?', n.isalpha())
print('São apenas letras maiúsculas ?', n.isupper())
print('Contém números e letras ?', n.isalnum())
print ('São apenas as letras minúsculas ?', n.islower())
print ('Está capitalizada ?', n.istitle())