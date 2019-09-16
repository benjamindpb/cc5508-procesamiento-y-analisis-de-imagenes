import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as nd_filters
import basis
import pai_io
import orientation_histograms as oh

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

def helo_histogram(image_path, B, K):
    image = pai_io.imread(image_path)
    L_x = np.zeros(B)
    L_y = np.zeros(B)
    kernel_x = np.array([[-1,0,1], [-2,0,2],[-1,0,1]])
    g_x = nd_filters.convolve(image_path.astype(np.float32), kernel_x, mode = 'constant', cval = 0)
    kernel_y = np.transpose(kernel_x)
    g_y = nd_filters.convolve(image_path.astype(np.float32), kernel_y, mode = 'constant', cval = 0)

