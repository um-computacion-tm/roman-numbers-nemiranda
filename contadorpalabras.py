import unittest

def contadordepalabras(frase):
    palabrassinespacio = frase.lower().split()
    diccionariopalabras = {}
    for palabra in palabrassinespacio:
        if palabra in diccionariopalabras:
            diccionariopalabras[palabra] += 1
        else:
            diccionariopalabras[palabra] = 1
    return diccionariopalabras

if __name__ == '__main__':
    print (contadordepalabras)