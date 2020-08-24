import random as ra

def run ():
    al_num = ra.randint( 0, 100)
    num_usr = int(input("Adivina adivinador.. ¿qué número pienso yo?  "))
    while num_usr != al_num:
        if num_usr < al_num :
            print("El número que buscas es mas grande")
        elif num_usr > al_num :
            print("El número que buscas es más pequeño")
        num_usr = int(input("Elige otro número mi chavo  "))
    print("Haz superao el juego!!!")


if __name__=='__main__':
    run()