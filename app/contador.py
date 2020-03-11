import creacion
def resulta(respuestas, resultado, dificultad, tiempo):
    r_buenas=0
    r_malas=0
    for i in range(0,10):
        if respuestas[i] == resultado [i]:
            r_buenas+=1
        else:
            r_malas+=1
    print(f"\u001b[32mTuviste {r_buenas} respuestas correcta \nTuviste {r_malas} respuestas erroneas \nEn total de 10 preguntas")
    nombre = input('Ingresa tu nombre completo para guardar el marcador:')
    marcador = f"Respuestas correctas: {r_buenas} / Respuestas incorrectas: {r_malas} / Dificultad: {dificultad} / Tiempo transcurrido: {tiempo:.2f} segundos"
    creacion.marcadores(nombre, marcador)