import matplotlib.pyplot as plt
import numpy as np
import glob
import pai_io
import basis
import cv2
""" 
Morphing de Imágenes

CC5508 - Procesamiento y Analisis de Imagenes 

Autor: Benjamin del Pino B.

"""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""
Esta funcion esta encargada de leer las imagenes de entrada y 
el archivo de texto que contiene las coordenadas de las 
lineas para posteriormente aplicar el algoritmo de Beier-Neely

rutaImgOrigen: str
    ruta de la imagen de origen

rutaImgDestino: str
    ruta de la imagen de destino

rutaArchivoLineas: str
    ruta del archivo de texto que contiene las lineas

N: int
    cantidad de imagenes intermedias a generar

Author: Benjamin del Pino B.

"""
def morph(rutaImgOrigen, rutaImgDestino, rutaArchivoLineas, N):
    #ruta del archivo que contiene los pares de lineas de ref
    rutaArchivoDeLineas = "../txt/refLines.txt"
    archivoDeLineas  = open(rutaArchivoDeLineas, 'r')
    lineas = archivoDeLineas.read().splitlines()
    #imagen origen
    imgOrigen = pai_io.imread(rutaImgOrigen)
    #imagen destino
    imgDestino = pai_io.imread(rutaImgDestino)
    #dimensiones de la imagen que se obtendrá
    largo, ancho, dim = imgDestino.shape
    imageB = np.zeros((imgDestino.shape), np.uint8)

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

    warp(img)
    
    

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
"""
Funcion encargada de calcular las nuevas
coordenadas de la transformacion

x: int
    coordenada x del pixel
y: int
    coordenada y del pixel
arrayPuntos: list
    las listas de los pares de puntos
"""
def transform(x, y, arrayPuntos):
    x = np.array([x, y])
    #coordenadas de los puntos que forman la linea
    pa, qa, pb, qb = arrayPuntos
    #pares de puntos que conforman la linea(---->)
    px = x - pa
    pq_a = qa - pa
    pq_b = qb - pb
    #norma de las lineas
    pq_a_norm = np.linalg.norm(pq_a)
    pq_b_norm = np.linalg.norm(pq_b)

    u_a = pq_a / pq_a_norm
    v_a = np.array([-u_a[1], u_a[0]])
    u_b = pq_b / pq_b_norm
    v_b = np.array([-u_b[1], u_b[0]])
    
    a = u_a @ px
    b = v_a @ px
    
    C = (pq_b_norm * a * u_b) / pq_a_norm
    D = b * v_b
    X = pb + C + D
    return X

"""
Esta funcion realiza la deformacion de una imagen

imageA:
"""  
def warp(imageA, arrayPuntos):
    imageB = np.zeros((imageA.shape), np.uint8)
    #print(imageB.shape)
    return imageB[2][4]
""" 
image:
    imagen que será interpolada
X:
    punto 
    
"""    
def interpolacion_bilineal(image, X):
    
    return
if __name__ == "__main__":
    morph("../img/pinochet_face.jpg", "../img/hitler_face.jpg", "txt/refLines.txt", 4)

