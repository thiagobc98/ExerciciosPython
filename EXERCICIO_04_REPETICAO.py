pais_A = 80000
pais_B = 200000

anos = 0

print("População do País A: ", pais_A)
print("População do País B: ", pais_B)

while(pais_A <= pais_B):
    pais_A = pais_A * 1.030
    pais_B = pais_B * 1.015

    anos = anos + 1

print("Para a população do País A bater ou igualar a do País B vai ser preciso ", anos , " anos ")
