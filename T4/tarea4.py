#imgOrigen, imgDestino, archivoLineas, N
# def morph():
#     print("hola")

if __name__ == "__main__":

    #imagen origen
    imgOrigen = 0

    #imagen destino
    imgDestino = 0

    #ruta del archivo que contiene los pares de lineas de ref
    rutaArchivo = "txt/refLines.txt"
    archivo  = open(rutaArchivo, 'r')
    asd = archivo.read().splitlines()
    
    lineas = []
    for linea in asd:
        lst = linea[3:].split(",")
        lineas.append(lst)
    print(lineas)
    

