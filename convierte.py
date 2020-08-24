menu = '''
Elige campión:

1 - Pesos Mexicanos
2 - Pokeyens
3 - Pesetas
'''
opcion = int(input(menu))
if opcion == 1:
    pesosm = float(input("¿Cuánto varo tiene en Pesos Mexicanos?  "))
    dolarvalor = 25.50
    dolarucos = pesosm / dolarvalor
    dolarucos = round(dolarucos, 2)
    print("Usté cuenta con un total de " + str(dolarucos)3 +" dolarucos.")
elif opcion == 2:
    pesosm = float(input("¿Cuánto varo tiene en Pokeyenes?  "))
    dolarvalor = 50
    dolarucos = pesosm / dolarvalor
    dolarucos = round(dolarucos, 2)
    print("Usté cuenta con un total de " +str(dolarucos) +" dolarucos.")
elif opcion == 3:
    pesosm = float(input("¿Cuánto varo tiene en Pesos Argelianos?  "))
    dolarvalor = 2550.20
    dolarucos = pesosm / dolarvalor
    dolarucos = round(dolarucos, 2)
    print("Usté cuenta con un total de " +str(dolarucos) +" dolarucos.")
else:
    print("Ese botón no es parte de las opciones")    