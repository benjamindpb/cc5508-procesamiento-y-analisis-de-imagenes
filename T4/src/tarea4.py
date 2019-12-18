import matplotlib.pyplot as plt
import numpy as np
import glob
import pai_io
import basis
import cv2

#imgOrigen, imgDestino, archivoLineas, N
def morph(rutaImgOrigen, rutaImgDestino, rutaArchivoLineas, N):

    #ruta del archivo que contiene los pares de lineas de ref
    rutaArchivoDeLineas = "../txt/refLines.txt"
    archivoDeLineas  = open(rutaArchivoDeLineas, 'r')
    lineas = archivoDeLineas.read().splitlines()
    
    paresDeLineas = []
    for par in lineas:
        L = par[3:].split(",")
        for i in range(len(L)):
            L[i] = int(L[i])
        paresDeLineas.append(L)

    listaPuntos=[]
    for lineas in paresDeLineas:
        for i in range(len(lineas)):
            if i%2 == 0:
                P=[]
                P.append(lineas[i])
            else:
                P.append(lineas[i])
                listaPuntos.append(P)

    listaPuntos = np.array(listaPuntos)
    print(listaPuntos)

    #imagen origen
    imgOrigen = pai_io.imread(rutaImgOrigen)
    #imagen destino
    imgDestino = pai_io.imread(rutaImgDestino)

    largo, ancho, dim = imgDestino.shape

########################################################################
    # plt.figure()

    # plt.subplot(1, 2, 1)
    # plt.imshow(imgOrigen)
    # plt.axis('off')
    # plt.title("Piñera")

    # plt.subplot(1, 2, 2)
    # plt.imshow(imgDestino)
    # plt.axis('off')
    # plt.title("Hitler")

    # plt.show()
    #hola()
########################################################################
    
    for i in range(largo):
        for j in range(ancho):
            
    

if __name__ == "__main__":
    morph("../img/pinochet_face.jpg", "../img/hitler_face.jpg", "txt/refLines.txt", 4)
    

