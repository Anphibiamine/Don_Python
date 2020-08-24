#ESTO GENERA DOS LISTAS DE CARACTERES UNA EN MAYÚSCULAS Y OTRA EN MINÚSCULAS

nombre = "el anfibio alienígena"
letritas=[nombre[i] for i in range(len(nombre))]
letrotas=[nombre[i].upper() for i in range(len(letritas))]
print(letritas)
print(letrotas)

#EL SIGUIENTE SOLO IMPRIME EN MAYÚSCULAS PERO GUARDA LA LISTA COMO SE ENTREGÓ

nombre = "Nos vA a enSeÑar unos Truquitos"
letritas= [nombre[i] for i in range(len(nombre))]
[print(nombre[i].upper()) for i in range(len(letritas))]
print(letritas)