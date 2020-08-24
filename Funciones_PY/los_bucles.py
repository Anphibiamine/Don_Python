def potencias(cual_num, que_potencia):
    POTENCIA = int(que_potencia)
    BASE =  int(cual_num)
    cunt = 0
    while cunt < POTENCIA:
        print(str(BASE) + " Elevado a la " + str(cunt) + " Es igual a " + str(BASE**cunt))
        cunt = cunt +1
    return (cunt)



# cunt=0
# cual_num= 3
#     #while cunt <= que_potencia:
# print(str(cual_num) + " Elevado a la " +str(cunt) + " es igual a: "+str(cual_num**cunt))
# cunt =cunt +1
#     #else:
# print("Yaca Beeeee")
    

