import os
def marcadores(nombre, resultados):
    print("Nuevo registro")
    registro = open('almacen.csv', 'a')
    print(f"Datos capturados: Nombre {nombre}, respuestas {resultados}")
    registro.write('Nombre: ')
    registro.write(nombre)
    registro.write(' / ')
    registro.write(resultados)
    registro.write('\n')
    registro.close()

def Mostrar_Marcadores():
    print(">>Marcadores<<")
    registro = open('almacen.csv')
    print(registro.read())
    input('Presiones enter para continuar (Press enter to continue)')
    os.system('clear')