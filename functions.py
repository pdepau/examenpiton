import csv
import math
def read_data(datos):
    with open(datos, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
        row.split()

def split(diccionario):
    diccionarioWhite={}
    diccionarioRed={}
    for i in diccionario:
        diccionarioTemporal=diccionario[i]
        tipo=diccionarioTemporal['type']
        if tipo == 'white':
            vinoWhite = {
                'fixed acidity':diccionarioTemporal['fixed acidity'],
                'volatile acidity':diccionarioTemporal['volatile acidity'],
                'citric acid':diccionarioTemporal['citric acid'],
                'residual sugar':diccionarioTemporal['residual sugar'],
                'chlorides':diccionarioTemporal['chlorides'],
                'free sulfur dioxide':diccionarioTemporal['free sulfur dioxide'],
                'total sulfur dioxide':diccionarioTemporal['total sulfur dioxide'],
                'density':diccionarioTemporal['density'],
                'pH':diccionarioTemporal['pH'],
                'sulphates':diccionarioTemporal['sulphates'],
                'alcohol':diccionarioTemporal['alcohol'],
                'quality':diccionarioTemporal['quality']
            }
            diccionarioWhite[i]=vinoWhite
            vinoWhite.clear()
        if tipo == 'red':
            vinoRed = {
                'fixed acidity':diccionarioTemporal['fixed acidity'],
                'volatile acidity':diccionarioTemporal['volatile acidity'],
                'citric acid':diccionarioTemporal['citric acid'],
                'residual sugar':diccionarioTemporal['residual sugar'],
                'chlorides':diccionarioTemporal['chlorides'],
                'free sulfur dioxide':diccionarioTemporal['free sulfur dioxide'],
                'total sulfur dioxide':diccionarioTemporal['total sulfur dioxide'],
                'density':diccionarioTemporal['density'],
                'pH':diccionarioTemporal['pH'],
                'sulphates':diccionarioTemporal['sulphates'],
                'alcohol':diccionarioTemporal['alcohol'],
                'quality':diccionarioTemporal['quality']
            }
            diccionarioRed[i]=vinoRed
            vinoRed.clear()
    return vinoWhite,vinoRed


def reduce(diccionario,atributo):
    listaFinal=[]
    for i in diccionario:
        diccionarioTemporal=diccionario[i]
        listaFinal.append(diccionarioTemporal[atributo])
    return listaFinal

def silhouette(lista1,lista2):
    
