def run():
    pob_paises = {
        'méxico':'un montón',
        'argentina':44938712,
        'mundo pokemon':982,
    }
    [print(i) for i in pob_paises.keys()]
    [print(i) for i in pob_paises.values()]
    [print ("La población de "+ str(i)+ " es "+ str(pob_paises[i])) for i in pob_paises.keys()]
    [print("La población de " + i + " es de " + str(j) +" de habitantes.") for i, j in pob_paises.items()]



if __name__=='__main__':
    run()