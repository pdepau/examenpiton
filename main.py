from functions import *

diccionario = read_data('winequality.csv')
diccionarioWhite,diccionarioRed = split(diccionario)
listaAlcoholWhite = reduce(diccionarioWhite,'alcohol')
listaAlcoholRed= reduce(diccionarioRed,'alcohol')
coeficiente = silhouette(listaAlcoholWhite,listaAlcoholRed)
