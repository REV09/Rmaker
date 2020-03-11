import repositorio
import contador
import aleartorios
import creacion
import random
import os
from time import time
operaciones = []
resultados = []
resultados_usuario= []
while True:
    print(repositorio.cadena.center(80, "="))
    print(repositorio.presentacion1.center(10, "="))
    print(repositorio.presentacion2.center(10, "="))
    print(repositorio.presentacion3.center(10, "="))
    print(repositorio.presentacion4.center(10, "="))
    input('Presiona enter para continuar (Press enter to continue)')
    os.system('clear')
    break
while True:
    print(repositorio.presentacion5.center(40, "+"))
    print(repositorio.presentacion6.center(40, "+"))
    print(repositorio.presentacion7.center(40, "+"))
    print(repositorio.presentacion8.center(40, "+"))
    print(repositorio.presentacion9.center(40, "+"))
    input('Presiona enter para continuar (Press enter to continue)')
    os.system('clear')
    confirmacion = input("\u001b[32m¿Todo claro todo hasta aquí? \nEn caso de 'si' escribe tu confirmacion ('si' o una 's',o confirmar en ingles) \nEn caso de 'no' aplica de la misma forma ('no' o 'n'):")
    confirmacion = confirmacion.upper()
    if confirmacion == 'S' or confirmacion == 'SI' or confirmacion == 'YES' or confirmacion == 'Y':
        print("Perfecto entonces comenzemos")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
        break
    elif confirmacion == 'N' or confirmacion == 'NO':
        print("Ok lo repetire para que quede claro")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
    else:
        print("Opcion tecleada incorrecta vuelve a intentarlo")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
while True:
    dificultad = input("\u001b[37mEscoge el nivel de dificultad (elige tecleando el nombre en ingles o español, por la primera letra o numero de opcion) \n1)Facil \n2)Normal \n3)Dificil \n4)Experto \n5)Marcadores \n>")
    dificultad = dificultad.upper()
    os.system('clear')
    if dificultad == '1' or dificultad ==  'FACIL' or dificultad ==  'EASY' or dificultad ==  'F' or dificultad ==  'E' or dificultad == 'UNO' or dificultad == 'ONE':
        print(f"Dificultad {dificultad}: Facil seleccionada")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
        aleartorios.generador_facil()
        break
    elif dificultad == '2' or dificultad ==  'NORMAL' or dificultad ==  'N' or dificultad == 'DOS' or dificultad=='TWO':
        print(f"Dificultad {dificultad}: Normal seleccionada")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
        aleartorios.generador_normal()
        break
    elif dificultad == '3' or dificultad ==  'HARD' or dificultad ==  'DIFICIL' or dificultad ==  'H' or dificultad ==  'D' or dificultad == 'TRES' or dificultad == 'THREE':
        print(f"Dificultad {dificultad}: Dificil seleccionada")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
        aleartorios.generador_dificil()
        break
    elif dificultad == '4' or dificultad == 'EXPERTO' or dificultad ==  'EXPERT' or dificultad ==  'E' or dificultad == 'CUATRO' or dificultad == 'FOUR':
        print(f"Dificultad {dificultad}: Experto seleccionada. Buena suerte")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')
        aleartorios.generador_experto()
        break
    elif dificultad == '5':
        creacion.Mostrar_Marcadores()
    else:
        print("No se ha seleccionado ninguna opcion valida intente de nuevo")
        input('Presiona enter para continuar (Press enter to continue)')
        os.system('clear')