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
    
def transform(x_i, x_j, arrayPuntos):
    x = np.array([x_i, x_j])
    pa, qa, pb, qb = arrayPuntos
    
    px = x - pa
    pq_a = qa - pa
    pq_b = qb - pb

    pq_a_norm = np.linalg.norm(pq_a)
    pq_b_norm = np.linalg.norm(pq_b)

    u_a = pq_a / pq_a_norm
    v_a = np.array([-u_a[1], u_a[0]])
    u_b = pq_b / pq_b_norm
    v_b = np.array([-u_b[1], u_b[0]])

    a = u_a @ px
    b = v_a @ px
    C = ((pq_b_norm * a * u_b) / pq_a_norm)
    D = (b * v_b)

    X = pb + C + D
    return X


    print("hola")
    

if __name__ == "__main__":
    #morph("../img/pinochet_face.jpg", "../img/hitler_face.jpg", "txt/refLines.txt", 4)
    A = transform(4,5,np.array([[2, 2], [2, 6], [3, 3], [7, 7]]))
    print(A)

