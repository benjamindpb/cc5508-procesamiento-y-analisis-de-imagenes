import matplotlib.pyplot as plt
import pai_io
import basis

#imgOrigen, imgDestino, archivoLineas, N
# def morph():
#     print("hola")

if __name__ == "__main__":

    #imagen origen
    imgOrigen = pai_io.imread("../img/piñera_face.jpg")
    #imagen destino
    imgDestino = pai_io.imread("../img/hitler_face.jpg")

########################################################################
    plt.figure()

    plt.subplot(1, 2, 1)
    plt.imshow(imgOrigen)
    plt.axis('off')
    plt.title("Piñera")

    plt.subplot(1, 2, 2)
    plt.imshow(imgDestino)
    plt.axis('off')
    plt.title("Hitler")

    plt.show()
########################################################################

    #ruta del archivo que contiene los pares de lineas de ref
    rutaArchivo = "../txt/refLines.txt"
    archivo  = open(rutaArchivo, 'r')
    asd = archivo.read().splitlines()
    
    lineas = []
    for linea in asd:
        lst = linea[3:].split(",")
        lineas.append(lst)
    #print(lineas)
    

