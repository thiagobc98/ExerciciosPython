sal = float(input("Quanto que você ganha por hora?"))
horas = int(input("Número de horas trabalhadas por mês: "))
salBruto = sal * horas
impostoRenda = (salBruto/100)*11
inss = (salBruto/100) *8
sindicato = (salBruto/100)*5
salLiquido = salBruto - inss - impostoRenda - sindicato
print("Salário Bruto: R$ ", salBruto)
print("INSS: R$ ", inss)
print("Sindicato: R$ ", sindicato)
print("Sálario Líquido: R$ ", salLiquido)
