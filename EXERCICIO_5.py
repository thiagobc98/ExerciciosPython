nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if(media >= 7):
    print("APROVADO!!!")
elif (media < 7):
    print('REPROVADO!!!')
elif (media == 10):
    print('APROVADO COM DISTINÇÃO!!!')