from math import pow, sqrt
lista = []
num=0
media =0
i=0
somadp =0
while (num >= 0):
    num = float(input('Número: (NÚMERO NEGATIVO ENCERRA)'))
    if num >= 0:
        lista.append(num)
        i+= 1
for x in lista:
    media += x
media = media / i
for x in lista:
   somadp =pow(x - media, 2)
   somadp  +=somadp
dp = sqrt(somadp/i)

print('Lista: ', lista)
print('Média:{:.2f} '.format(media))
print('Desvio Padrão: {:.4f}'.format(dp))
