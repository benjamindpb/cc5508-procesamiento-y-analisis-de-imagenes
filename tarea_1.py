import argparse
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description = "CC5508 - Procesamiento y Analisis de Imagenes.Tarea 1: Estenografía")
group = parser.add_mutually_exclusive_group()
group.add_argument("--encode", action = "store_true", help = "indica que la tarea es codificar un texto de entrada dentro de una imagen.")
group.add_argument("--decode", action = "store_true", help = "indica que la tarea es decodificar una imagen, mostrando el texto oculto.")
    
parser.add_argument("--image", nargs = 1, type = str, help = "indica la imagen que sera codificada/decodificada.")
parser.add_argument("--text", nargs = 1, type = str, help = "indica el archivo que contiene el texto a codificar.")
parser.add_argument("--nbits", nargs = 1, type = int, choices = range(1,9), help = "indica el numero de bits menos significativos a ser usados.")

args = parser.parse_args()


#python tarea_1.py --encode --image 'images/gray/lion_gray.jpg' --text 'textos/texto1.txt' --nbits 2
if __name__ == '__main__':
    #modo encode
    if args.encode:

        if(8 % args.nbits[0] == 0):
            img_filename = args.image[0]
            image = io.imread(img_filename)
            txt_filename = args.text[0]
            text = open(txt_filename, 'r').read()
            
            lst_txt = []
            for l in text:
                lst_txt.append(l)

            txt_ord = []
            for character in lst_txt:
                txt_ord.append(ord(character))#convierte a codigo ASCII
            
            txt_bin = []
            for num in txt_ord:
                txt_bin.append("{0:{fill}8b}".format(num, fill='0'))#convierte a binario
            
            dimension = np.shape(image)
            filas = dimension[0]
            columnas = dimension[1]
            
            #bin_matrix = np.zeros((filas, columnas))#matriz de ceros

            #creacion de matriz binaria de la imagen original
            bin_matrix = [None] * filas
            for i in range(filas):
                bin_matrix[i] = [None] * columnas

            for n in range(filas):
                for m in range(columnas):
                    bin_matrix[n][m] = "{0:{fill}8b}".format(image[n][m], fill='0')

        
            #ahora debemos considerar los bits menos significativos que nos piden
            bits_sigf = args.nbits[0]#se obtienen los bits significativos que se usaran
            txt_bin_copy = txt_bin.copy()
            txt_bin_copy.reverse()#el ultimo sera el primero

            cortes = int(8/bits_sigf)

            lst_bits_codif = []
            while(txt_bin_copy):
                num_bin = txt_bin_copy.pop()
                ini = 0
                fin = bits_sigf
                for i in range(cortes):
                    lst_bits_codif.append(num_bin[ini:fin])
                    ini += bits_sigf
                    fin += bits_sigf

            
            print("\n")
            i = 0
            for n in range(filas):
                for m in range(columnas):
                    if(i > len(lst_bits_codif) - 1):
                        break
                    if(i > len(lst_bits_codif) - 1):
                        break
                    bin_matrix[n][m] = str(bin_matrix[n][m])[: - bits_sigf] + lst_bits_codif[i]
                    i += 1
                        
            #ahora que tenemos la matriz binaria codificada debemos pasar sus valores a int para convertirla en imagen
            for n in range(filas):
                for m in range(columnas):
                    bin_matrix[n][m] = int(bin_matrix[n][m], 2)

            img = bin_matrix

            plt.imshow(img, cmap = 'gray')
            plt.show()

        else:
            print("La cantidad de bits significativos está limitada a solo ser divisores de 8, prueba con {1,2,4,8} lo siento :(")
    
    #modo decode
    if args.decode:
        print("DECODE")