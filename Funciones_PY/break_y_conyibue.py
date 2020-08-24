lista_1 = [i for i in range(1, 1001)]
#print(lista_1)
lista_2 = [i for i in range(1, 1001) if i % 2 != 0]
#print(lista_2)
lista_3 = [i for i in range(1, 1001) if i % 2 == 0 ]
#print(lista_3)

## ESTE QUITA LOS ESPACIOS
# frase_comp = input("Escriba una frase  ")
# loco = [frase_comp[i] for i in range(len(frase_comp)) if frase_comp[i] != " "]
# print("La primer palabra es: \n" )
# print(loco)

##este quiero que separe palabras
frase_comp = input("Escriba una frase  ")
for i in frase_comp:
    if frase_comp[i] == " ":
        FIN1 = i
        FIN2 = 
fin1 = 5
fin2 = 8
fin3 = 15
pal_1 = frase_comp[0:fin1]
pal_2 = frase_comp[fin1 +1 : fin2]
pal_3 = frase_comp[fin2 +1 : fin3]
print(pal_1)
print(pal_2)
print(pal_3)

# loco = [frase_comp[i] for i in range(len(frase_comp)) if frase_comp[i] != " "]
# print("La primer palabra es: \n" )
# print(loco)
