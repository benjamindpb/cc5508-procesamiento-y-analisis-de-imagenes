import sys
import matplotlib.pyplot as plt
import numpy as np
import basis
import pai_io
import orientation_histograms as oh

silla = '/home/nenjamib/Escritorio/Primavera 2019/Procesamiento y Analisis de Imagenes/Tareas/cc5508-tareas/T2/dataset_1/BD_2/chair/180016.jpg'

def getHistogram(image_path, K):
    imageA = pai_io.imread(image_path, as_gray = True)
    hA = oh.compute_orientation_histogram(imageA, K)
    plt.bar(range(K), height = hA)
    plt.show()

getHistogram(silla, 100)