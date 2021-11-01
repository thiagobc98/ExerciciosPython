print('----------MENU----------')
print('M - Matutino')
print('V - Vespertino')
print('N - Noturno')
turno = input('Qual é o turno que você estuda?')

if(turno == 'M'):
    print('BOM DIA')
elif(turno == 'V'):
    print('BOA TARDE')
elif(turno == 'N'):
    print('BOA NOITE')
else:
    print('VALOR INVÁLIDO')