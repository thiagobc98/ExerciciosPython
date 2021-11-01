numeros = ()
num = []
n = 1
i=0
numimpar =0
somanegativos = 0
numpositivos = 0

while n != 0:
    n = int(input('Digite um número: (O ENCERRA)'))
    if n != 0:
        num.append(n)
        i+=1
        if n % 2 != 0:
            numimpar += 1
        if n < 0:
            somanegativos += n
        if n >0:
            numpositivos += 1
''''for p in range(len(num)):
    if num[p] % 2 == 0:
        pos = p
        listapospares = []
        listapospares.append(pos)'''''



numeros = tuple(num)

print(numeros)
print('Tem {} números ímpares.'.format(numimpar))
print("O quadrado da soma dos negativos é {}".format((somanegativos*2)))
print('A média dos números positivos é {}'.format((numpositivos/i)))
