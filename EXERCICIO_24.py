num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

print('---------- MENU -------------')
print('1. SOMA')
print('2. SUBTRAÇÃO')
print('3. MULTIPLICAÇÃO')
print("4. DIVISÃO")
print("-----------------------------")
op = int(input('Qual operação você deseja fazer?'))
 
if(op == '1'):
    resultado = num1 + num2
    if (resultado % 2== 0):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e positivo')
        else:
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e negativo')    
    elif (resultado % 2 == 1):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e negativo')
        else: 
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e positivo')

            
elif(op == '2'):
    resultado = num1 - num2
    if (resultado % 2== 0):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e positivo')
        else:
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e negativo')    
    elif (resultado % 2 == 1):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e negativo')
        else: 
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e positivo')

elif(op == '3'):
    resultado = num1 * num2
    if (resultado % 2== 0):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e positivo')
        else:
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e negativo')    
    elif (resultado % 2 == 1):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e negativo')
        else: 
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e positivo')

elif(op == '4'):
    resultado = num1 / num2
    if (resultado % 2== 0):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e positivo')
        else:
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é par e negativo')    
    elif (resultado % 2 == 1):
        if(resultado < 0):
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e negativo')
        else: 
            print("A SOMA DOS DOIS NÚMEROS É IGUAL A ", resultado, ' e ele é ímpar e positivo')



