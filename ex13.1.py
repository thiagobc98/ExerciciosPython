class Pessoa:
 def __init__(self, nome_pessoa, data_nasc):
  self.nome_pessoa = nome_pessoa
  self.data_nasc = data_nasc

a = "n"
i =0
dicionario = {}

while a == 'n':
 p = Pessoa (nome_pessoa=input('Nome: '), data_nasc=input('Data de nascimento:'))
 dicionario['Pessoa {}:' .format(i)] = p

 i += 1
 a = input('Deseja parar? s/n')

for chave, valor in dicionario.items ():
  print ("%s, %s, %s" % (chave, valor.nome_pessoa, valor.data_nasc))




