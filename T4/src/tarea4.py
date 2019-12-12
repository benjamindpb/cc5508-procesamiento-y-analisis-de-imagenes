import matplotlib.pyplot as plt
import pai_io
import basis

#imgOrigen, imgDestino, archivoLineas, N
# def morph():
#     print("hola")

if __name__ == "__main__":

    #imagen origen
    imgOrigen = pai_io.imread("../img/hitler_face.jpg")
    #imagen destino
    imgDestino = pai_io.imread("../img/piñera_face.jpg")
    plt.show()

    #ruta del archivo que contiene los pares de lineas de ref
    rutaArchivo = "../txt/refLines.txt"
    archivo  = open(rutaArchivo, 'r')
    asd = archivo.read().splitlines()
    
    lineas = []
    for linea in asd:
        lst = linea[3:].split(",")
        lineas.append(lst)
    #print(lineas)
    

