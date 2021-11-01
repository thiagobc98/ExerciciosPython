num = int(input('Quantos números você deseja? '))
i=0
lista_original = []
lista_par = []
lista_impar = []
while i < num:
    n = int(input('Digite um número: '))
    lista_original.append(n)
    i+=1

for x in lista_original:
    if x%2==0:

        lista_par.append(x)
    else:

        lista_impar.append(x)

print('Lista original: ', lista_original)
print('Lista dos pares: ', lista_par)
print('Lista dos ímpares: ', lista_impar)

