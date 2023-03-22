import csv
import math
def read_data(datos):
    diccionario = {}
    posicion=0
    vacio=False
    with open(datos, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            linea=row.split(',')
            for i in linea:
                if i == '':
                    vacio = True
            if linea[0]!='type' and vacio==False:
                nombre="Dato"+str(posicion)
                nombre{
                    
                }




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
    
