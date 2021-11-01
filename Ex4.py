lista1 = []
lista2 = []
novalista = []
num1=0
num2=0
while num1 >= 0 and num2 >= 0:
    num1 = int(input('Digite um número para a lista 1: (NEGATIVO TERMINA)'))
    if num1 >= 0:
        lista1.append(num1)
    num2 = int(input('Digite um número para a lista 2: (NEGATIVO TERMINA)'))
    if num2 >= 0:
        lista2.append(num2)
for e in lista1:
    for e in lista2:
        if e in lista1 and lista2:
            novalista.append(e)
print('Lista 1: ', lista1)
print('Lista 2: ', lista2)
print('Nova lista: ', novalista)
