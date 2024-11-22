import re

# ruta del libro y de los documentos a generar como lo son la opcion 1 y la opcion 4 
ruta_archivo = 'C:\\Users\\pipe0\\Desktop\\principito.txt'
ruta_resultado_frecuencia = 'C:\\Users\\pipe0\\Desktop\\resultado_frecuencia.txt'
ruta_resultado_repetidas = 'C:\\Users\\pipe0\\Desktop\\resultado_repetidas.txt'

with open(ruta_archivo, 'r', encoding='utf-8') as file:  # abrir archivo del libro de principito .txt
    texto = file.read()  # leer el libro y guarda todo en la variable texto

texto = re.sub(r'[^a-zA-Z\s]', '', texto).lower()  # eliminar caracteres especiales, comas, tildres, espacios en blancos y convertir a minuscula todo
palabras = texto.split()  # separar el texto en una lista de palabras usando split

frecuencia_palabras = {}  # crear un diccionario vacío para almacenar la frecuencia de las palabras
for palabra in palabras:  # iteramos
    if palabra in frecuencia_palabras:  # si la palabra ya existe en el diccionario entonces
        frecuencia_palabras[palabra] += 1  # si existe entonces aumenta el valor en el conteo de esa palabra
    else:  # si no
        frecuencia_palabras[palabra] = 1  # solo se guarda con valor 1

def mostrar_frecuencia(archivo):  # frecuencia de palabras en orden alfabético, se crea la funcion para mejor profesionalismo
    archivo.write("\nFrecuencia de todas las palabras por orden alfabético:\n")  # creamos el archivo a imprimir al final en la ruta establecida al inicio
    for palabra, frecuencia in sorted(frecuencia_palabras.items()):  # iteramos sobre el diccionario organizado alfabéticamente
        archivo.write(f"'{palabra}': {frecuencia} veces\n")  # escribimos todas las palabras con el valor de repetición de cada palabra

def mostrar_palabras_repetidas(archivo):  # palabras que se repiten más de tres veces, ordenadas por frecuencia
    archivo.write("\nPalabras que se repiten más de tres veces, listado organizado por mayor a menor frecuencia:\n")  # texto para el documento
    palabras_frecuentes = {palabra: frecuencia for palabra, frecuencia in frecuencia_palabras.items() if frecuencia > 3}  # filtramos las palabras repetidas más de 3 veces
    for palabra, frecuencia in sorted(palabras_frecuentes.items(), key=lambda x: x[1], reverse=True):  # ordenamos las palabras filtradas por frecuencia de mayor a menor para que se vea ordenado y claro
        archivo.write(f"'{palabra}': {frecuencia} veces\n")  # escribimos las palabras y su frecuencia en el archivo y se guarda en la ruta establecida

# un buen ciclo para una mejor usabilidad por el usuario, además es infinito no termina hasta hacerlo terminar
while True:
    print("""
    \n\tUniversidad Del Quindío
    \tPrograma de Física
    \tCurso de Programación
    \tSALOME TORRES
    \tSALOMEDEPERUUUUUGMIAL.COM

    \tSelecciona una opción:

    1. Consultar la frecuencia de todas las palabras 
    2. Consultar la palabra más frecuente
    3. Consultar el número total de palabras únicas
    4. Consultar las palabras que se repiten más de tres veces
    5. Salir
    """)
 
    opcion = input("Ingresa una opción válida  ")  # valor ingresado por el usuario

    if opcion == "1":
        with open(ruta_resultado_frecuencia, 'w', encoding='utf-8') as archivo:  # Abrir archivo para escribir los resultados
            mostrar_frecuencia(archivo)  # Mostrar la frecuencia de todas las palabras ordenadas alfabéticamente
        print("Por favor abrir el archivo 'resultado_frecuencia.txt' para consultar el resultado.")
    
    elif opcion == "2":  # palabra más frecuente
        top_palabras = sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True)[:5]  # filtramos y mostramos las 5 más frecuentes 
        palabra_frecuente, max_frecuencia = top_palabras[0]
        print(f"\nLa palabra más frecuente es '{palabra_frecuente}' con {max_frecuencia} apariciones.")
        print("\nLas 5 palabras más frecuentes:")
        for palabra, frecuencia in top_palabras:
            print(f"'{palabra}': {frecuencia} veces")

    elif opcion == "3":  # listado de palabras únicas ordenado alfabéticamente
        palabras_unicas = sorted({palabra for palabra, frecuencia in frecuencia_palabras.items() if frecuencia == 1})
        print(f"\nNúmero total de palabras únicas: {len(palabras_unicas)}")
        print("Listado de palabras únicas (orden alfabético):")
        for palabra in palabras_unicas:
            print(palabra)

    elif opcion == "4":  # palabras repetidas más de tres veces
        with open(ruta_resultado_repetidas, 'w', encoding='utf-8') as archivo:
            mostrar_palabras_repetidas(archivo)
        print("Los resultados han sido guardados en 'resultado_repetidas.txt'.")
    
    elif opcion == "5":  # terminar programa 
        print("Saliendo del programa.")
        break

    else:  # opción por si meten cosas no permitidas
        print("¡AMIGO! Ingresa un número del 1 al 5.")

