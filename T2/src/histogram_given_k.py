import matplotlib.pyplot as plt
import numpy as np
import basis
import pai_io
import orientation_histograms as oh

delfin = '/home/nenjamib/Escritorio/Primavera 2019/Procesamiento y Analisis de Imagenes/Tareas/cc5508-tareas/T2/dataset_1/BD_2/dolphin/240003.jpg'
# print(type(delfin))
delfin2 = pai_io.imread(delfin, as_gray = True)
# print(type(delfin2))
# print(type(delfin2) == np.ndarray)

"""
Histrograma de Orientaciones

Esta funcion recibe el path o la matriz correspondiente a la imagen y un valor de cuantizacion, y devuelve el histograma de orientaciones correspondiente (HO)

Parametros
----------
image_path: path o matriz de la imagen
K: valor de cuantizacion
"""

def getHistogram(image, K):
    if(type(image) == np.ndarray):
        hA = oh.compute_orientation_histogram(image, K)
        plt.bar(range(K), height = hA)
        plt.show()
    else:
        img = pai_io.imread(image, as_gray = True)
        hA = oh.compute_orientation_histogram(img, K)
        plt.bar(range(K), height = hA)
        plt.show()