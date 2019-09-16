import matplotlib.pyplot as plt
import numpy as np
import basis
import pai_io
import orientation_histograms as oh

delfin = '/home/nenjamib/Escritorio/Primavera 2019/Procesamiento y Analisis de Imagenes/Tareas/cc5508-tareas/T2/dataset_1/BD_2/dolphin/240003.jpg'

"""
Histrograma de Orientaciones

Esta funcion recibe el path de la imagen y un valor de cuantizacion,
y devuelve el histograma de orientaciones correspondiente (OH)

Parametros
----------
image_path: path de la imagen
K: valor de cuantizacion
"""

def getHistogram(image_path, K):
    image = pai_io.imread(image_path, as_gray = True)
    print(image)
    # hA = oh.compute_orientation_histogram(image, K)
    # plt.bar(range(K), height = hA)
    # plt.show()

getHistogram(delfin, 36)