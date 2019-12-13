import matplotlib.pyplot as plt
import numpy as np
import glob
import pai_io
import basis
import cv2

#imgOrigen, imgDestino, archivoLineas, N
def morph(rutaImgOrigen, rutaImgDestino, rutaArchivoLineas, N):
    images = []
    #imagen origen
    imgOrigen = pai_io.imread(rutaImgOrigen)
    print(imgOrigen.shape)
    #imagen destino
    imgDestino = pai_io.imread(rutaImgDestino)
    print(imgDestino.shape)

    images.append(imgOrigen)
    images.append(imgDestino)

    alto, ancho , capas = images.shape
    size = (ancho, alto)

    out = cv2.VideoWriter("morphing.avi", cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(images)):
        out.write(images[i])
    out.release()

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
    
    #print(paresDeLineas)

    listaPuntos=[]
    for lineas in paresDeLineas:
        for i in range(len(lineas)):
            if i%2 == 0:
                P=[]
                P.append(lineas[i])
            else:
                P.append(lineas[i])
                listaPuntos.append(P)
    print(listaPuntos)
    

if __name__ == "__main__":
    morph("../img/pinochet_face.jpg", "../img/hitler_face.jpg", "txt/refLines.txt", 4)
    

