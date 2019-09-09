import sys
sys.path.append('../aux_functions')
import matplotlib.pyplot as plt
import numpy as np
import basis
import pai_io
import orientation_histograms as oh

def getHistogram(K):
    filenameA = '../dataset_1/BD_2/chair/180016.jpg'
    imageA = pai_io.imread(filenameA, as_gray = True)
    hA = oh.compute_orientation_histogram(imageA, K)

    plt.bar(range(K), height = hA)
    plt.show()

getHistogram(100)