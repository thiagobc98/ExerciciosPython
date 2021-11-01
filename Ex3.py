lista1 = []
lista2 = []
novalista = []
num1 = 0
num2 = 0
while num1 >=0 and num2 >= 0:
    num1 = int(input('Digite os números da lista 1: (NÚMERO NEGATIVO FECHA A LISTA)'))
    num2 = int(input('Digite os números da lista 2: (NÚMERO NEGATIVO FECHA A LISTA)'))
    if num1 >= 0:
        lista1.append(num1)
    if num2 >= 0:
        lista2.append(num2)
for e in lista1:
    novalista.append(e)
for e in lista2:
    if e not in novalista:
        novalista.append(e)
print('lista 1: ', lista1)
print('Lista 2: ', lista2)
print('Nova lista: ', novalista)
