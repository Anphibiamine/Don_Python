numero = input("Escribe un númaero entero campeon!!!  ")
n = int(numero)
for i in range(2, n):
    if n % i != 0:
        print("no lo dividie el "+ str (i))
        if i == n-1 :
            print("esto es un numero primo")
    elif n % i == 0 :
        print("no es primo por que lo divide el "+ str(i))
        break

# numero = input("Escribe un númaero entero campeon!!!  ")
# n = int(numero)
# for i in range(2, n):
#     if n % i != 0:
#         print("no lo dividie el "+ str (i))
#     elif n % i == 0 :
#         print("no es primo por que lo divide el "+ str(i))
#         break

# def es_prim(numb):
#     cunt = 0
#     for i in range(1,numb+1):
#         if i == 1 or i == numb :
#             continue
#         if numb % i == 0 :
#             cunt += 1
#     if cunt == 0:
#         return True
#     else:
#         return False

# def run():


#     minum = int(input("Escriba un número entero campeon!!!  "))
#     if es_prim(minum):
#         print("Eso es un número primo")
#     else:
#         print ("No es un número primo :(")


# if __name__=='__main__':
#     run()