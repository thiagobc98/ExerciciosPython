class Pessoa:
 def __init__(self, nome_pessoa, data_nasc):
  self.nome_pessoa = nome_pessoa
  self.data_nasc = data_nasc

class PessoaFisica(Pessoa):
    def __init__(self, nome_pessoa, data_nasc, cpf):
        self.cpf = cpf
        super().__init__(nome_pessoa, data_nasc)

class PessoaJuridica(Pessoa):
    def __init__(self, nome_pessoa, data_nasc,  cnpj):
        self.cnpj = cnpj
        super().__init__(nome_pessoa, data_nasc)

a = "n"
i =0
dpf = {}
dpj = {}


while a == 'n':
 tipo = input('PJ ou PF ?')
 if tipo == 'PJ':
    p = PessoaJuridica (nome_pessoa=input('Nome: '), data_nasc=input('Data de nascimento:'), cnpj=input('CNPJ: '))
    dpj['Pessoa Jurídica {}:'.format(i)] = p
    i+=1
 elif tipo == 'PF':
     p = PessoaFisica(nome_pessoa=input('Nome: '), data_nasc=input('Data de nascimento:'), cpf=input('CPF: '))
     dpf['Pessoa Física {}:'.format(i)] = p
     i += 1
 a = input('Deseja parar? s/n')


for chave, valor in dpf.items ():
  print ("%s, %s, %s, %s" % (chave, valor.nome_pessoa, valor.data_nasc, valor.cpf))
for chave, valor in dpj.items():
    print('%s %s %s %s' % (chave, valor.nome_pessoa, valor.data_nasc, valor.cnpj))



