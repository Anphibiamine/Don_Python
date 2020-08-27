import random as r

def run():
    mayu = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    minu = [i.lower() for i in mayu]
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbo = ['!','"', '#', '$', '%', '/', '(', ')', '=', '?', '¿','¡' ]
    liscomp = mayu + minu + num + symbo
    contrasenia = [r.choice(liscomp) for i in range(15)]
    contra = ''.join(contrasenia)
    print(contra)
    
    

if __name__ == '__main__':
    run()