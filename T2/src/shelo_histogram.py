import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as nd_filters
import basis
import pai_io
import orientation_histograms as oh
import histogram_given_k as ho

def shelo_histogram(image, B, K):
    return 0