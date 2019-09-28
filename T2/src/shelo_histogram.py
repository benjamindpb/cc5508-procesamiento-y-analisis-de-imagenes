import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as nd_filters
import basis
import pai_io
import orientation_histograms as oh
import histogram_given_k as ho

delfin = '/home/nenjamib/Escritorio/Primavera 2019/Procesamiento y Analisis de Imagenes/Tareas/cc5508-tareas/T2/dataset_1/BD_2/dolphin/240003.jpg'

def shelo_histogram(image, B, K):
    img = pai_io.imread(image, as_gray=True)

    filas = np.shape(img)[0]
    columnas = np.shape(img)[1]

    L_x = np.zeros((B,B)) #conjunto de gradientes locales c/r a x
    L_y = np.zeros((B,B)) #conjunto de gradientes locales c/r a y
    ang = np.zeros((B,B))

    kernel_x = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
    kernel_y = np.transpose(kernel_x)

    g_x = nd_filters.convolve(image, kernel_x, mode = 'constant', cval = 0.0)
    g_y = nd_filters.convolve(image, kernel_y, mode = 'constant', cval = 0.0)

    for i in range(filas):
        for j in range(columnas):
            return 0
