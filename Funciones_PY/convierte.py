def mesj(num, cambio):
    pesosm = input("¿Cuánto varo tiene en " + num + "?  ")
    pesosm = float(pesosm)
    dolarvalor= float(cambio)
    dolarucos = pesosm / dolarvalor
    dolarucos = str(round(dolarucos, 2))
    print("Usté cuenta con $" + dolarucos + " dolarucos.")


menu = '''
Elige campión:

1 - Pesos Mexicanos
2 - Pokeyens
3 - Pesetas
'''
opcion = int(input(menu))
if opcion == 1:
    mesj("pezones mexicanos", 25)
elif opcion == 2:
    mesj("poke Yenes", 10)
elif opcion == 3:
    mesj("pezones argelianos", 250)
else:
    print("Ese botón no es parte de las opciones")