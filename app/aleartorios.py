import contador
import random
import os
import creacion
from time import time
vector = []
resultados = []
respuesta = []

def generador_facil():
    for i in range(0,20,1):
        vector.append(random.randint(1,100))
    inicio =time()
    for i in range(0,20,2):
        auxiliar = int(input(f"\u001b[36mCuanto es {vector[i]} + {vector[i+1]}?\n>"))
        resultados.append(vector[i] + vector[i+1])
        respuesta.append(auxiliar)
        if auxiliar == vector[i] + vector[i+1]:
            print("\u001b[32m¡¡Correcto muy bien!!")
        else:
            print("\u001b[31; Respuesta equivocada")
        print(f"\u001b[36mLa respuesta correcta es: {vector[i]+vector[i+1]}")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
    fin = time()
    tiempo = fin - inicio
    print(f"\u001b[36mResultados de las operaciones: {resultados}")
    print(f"\u001b[36mResultados que dictaste: {respuesta}")
    contador.resulta(respuesta,resultados,'Facil',tiempo)

def generador_normal():
    for i in range(0,30,1):
        vector.append(random.randint(1,300))
    inicio =time()
    for i in range(0,30,3):
        auxiliar = int(input(f"\u001b[36mCuanto es {vector[i]}+{vector[i+1]}-{vector[i+2]}?\n>"))
        resultados.append(vector[i]+vector[i+1]-vector[i+2])
        respuesta.append(auxiliar)
        if auxiliar == vector[i]+vector[i+1]-vector[i+2]:
            print("\u001b[32m¡¡Correcto muy bien!!")
        else:
            print("\u001b[31; Respuesta equivocada")
        print(f"\u001b[36mLa respuesta correcta es: {vector[i]+vector[i+1]-vector[i+2]}")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
    fin = time()
    tiempo = fin - inicio
    print(f"\u001b[36mResultados de las operaciones {resultados}")
    print(f"\u001b[36mResultados que dictaste: {respuesta}")
    contador.resulta(respuesta,resultados,'Normal',tiempo)

def generador_dificil():
    for i in range(0,40,1):
        vector.append(random.randint(1,200))
    inicio =time()
    for i in range(0,40,4):
        auxiliar = int(input(f"\u001b[36mCuanto es {vector[i]}+{vector[i+1]}-{vector[i+2]}-{vector[i+3]}?\n>"))
        resultados.append(vector[i]+vector[i+1]-vector[i+2]-vector[i+3])
        respuesta.append(auxiliar)
        if auxiliar == vector[i]+vector[i+1]-vector[i+2]-vector[i+3]:
            print("\u001b[32m¡¡Correcto muy bien!!")
        else:
            print("\u001b[31; Respuesta equivocada")
        print(f"\u001b[36mLa respuesta correcta es: {vector[i]+vector[i+1]-vector[i+2]-vector[i+3]}")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
    fin = time()
    tiempo = fin - inicio
    print(f"\u001b[36mResultados de las operaciones: {resultados}")
    print(f"\u001b[36mResultados que dictaste: {respuesta}")
    contador.resulta(respuesta,resultados,'Dificil',tiempo)

def generador_experto():
    for i in range(0,30,1):
        vector.append(random.randint(1,20))
    inicio =time()
    for i in range(0,30,3):
        auxiliar = int(input(f"\u001b[36mCuanto es {vector[i]}+{vector[i+1]}X{vector[i+2]}?\n>"))
        resultados.append(vector[i]+vector[i+1]*vector[i+2])
        respuesta.append(auxiliar)
        if auxiliar == vector[i]+vector[i+1]*vector[i+2]:
            print("\u001b[32m¡¡Correcto muy bien!!")
        else:
            print("\u001b[31; Respuesta equivocada")
        print(f"\u001b[36mLa respuesta correcta es: {vector[i]+vector[i+1]*vector[i+2]}")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
    fin = time()
    tiempo = fin - inicio
    print(f"\u001b[36mResultados de las operaciones {resultados}")
    print(f"\u001b[36mResultados que dictaste: {respuesta}")
    contador.resulta(respuesta,resultados,'Experto',tiempo)