import csv
import math
def read_data(datos):
    diccionario = {}
    posicion=0
    vacio=False
    a=0
    with open(datos, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            linea=row.split(',')
            for i in linea:
                if i == '':
                    vacio = True
            if linea[0]!='type' and vacio==False:
                nombre="Dato"+str(posicion)
                vino = {
                   'type':linea[0],
                   'fixed acidity':linea[1],
                   'citric acid':linea[2],
                   'residual sugar':linea[3],
                   'chlorides':linea[4],
                   'free sulfur dioxide':linea[5],
                   'total sulfur dioxide':linea[6],
                   'density':linea[7],
                   'pH':linea[8],
                   'sulphates':linea[9],
                   'alcohol':linea[10],
                   'quality':linea[11]
                }
                diccionario[nombre]=vino
                vino.clear()
            posicion= posicion+1
    for j in diccionario:
        a=a+1
    if a>9:
        b="no hay menos de 10 "
    else:
        raise ValueError("existen menos de 10")

    return diccionario
        




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
    
