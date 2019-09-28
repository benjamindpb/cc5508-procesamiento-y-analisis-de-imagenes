import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as nd_filters
import basis
import pai_io
import orientation_histograms as oh
import histogram_given_k as ho

"""
Histograma de Orientaciones Locales

Esta funcion recibe una imagen, la cantidad de bloques y un valor de cuantizacion
para devolver el histograma de orientaciones locales correspondiente

Parametros
----------
image_path: path de la imagen
B: cantidad de bloques en los que se dividirá la imagen
K: valor de cuantizacion
"""

delfin = '/home/nenjamib/Escritorio/Primavera 2019/Procesamiento y Analisis de Imagenes/Tareas/cc5508-tareas/T2/dataset_1/BD_2/dolphin/240003.jpg'

def helo_histogram(image_path, B, K):
    image = pai_io.imread(image_path, as_gray = True) #matriz que representa la imagen

    L_x = np.zeros((B,B)) #conjunto de gradientes locales c/r a x
    L_y = np.zeros((B,B)) #conjunto de gradientes locales c/r a y
    ang = np.zeros((B,B))

    kernel_x = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
    kernel_y = np.transpose(kernel_x)

    g_x = nd_filters.convolve(image, kernel_x, mode = 'constant', cval = 0.0)
    g_y = nd_filters.convolve(image, kernel_y, mode = 'constant', cval = 0.0)
    
    height = np.shape(image)[0] #nro de pixeles de largo
    width = np.shape(image)[1] #nro de pixeles de ancho
    
    for i in range(height):
        for j in range(width):
            r = round((i/height) * (B - 1))
            s = round((j/width) * (B - 1))
            #print(i, j)
            L_x[r][s] += (g_x[i][j])**2 - (g_y[i][j])**2
            L_y[r][s] += 2 * (g_x[i][j]) * (g_y[i][j])

    for r in range(B):
        for s in range(B):
            ang[r,s] = np.arctan2(L_y[r,s], L_x[r,s]) * 0.5 - np.pi * 0.5

    ho.getHistogram(ang, K)

#def helo_lines(image, B, K):
    
#helo_histogram(delfin, 25, 36)
    



