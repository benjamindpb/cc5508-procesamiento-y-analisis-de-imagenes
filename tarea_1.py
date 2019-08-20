import argparse
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description = "CC5508 - Procesamiento y Analisis de Imagenes.Tarea 1: Estenografía")
group = parser.add_mutually_exclusive_group()
group.add_argument("--encode", action = "store_true", help = "indica que la tarea es codificar un texto de entrada dentro de una imagen.")
group.add_argument("--decode", action = "store_true", help = "indica que la tarea es decodificar una imagen, mostrando el texto oculto.")
    
parser.add_argument("--image", type = str, help = "indica la imagen que sera codificada/decodificada.")
parser.add_argument("--text", type = str,  help = "indica el archivo que contiene el texto a codificar.", required = False)
parser.add_argument("--nbits", type = int, help = "indica el numero de bits menos significativos a ser usados.", required = False, choices = [1,2,4,8])

args = parser.parse_args()

#python tarea_1.py --encode --image 'images/gray/lenna_gray.png' --text 'textos/texto1.txt' --nbits 1
#python tarea_1.py --decode --image 'img_out/lenna_gray_out.png'
if __name__ == '__main__':
    img_filename = args.image
    image = io.imread(img_filename)
    eof_fila = 0
    eof_colm = 0

    #modo encode
    if args.encode:
        txt_filename = args.text
        text = open(txt_filename, 'r').read()
        #imagen en escala de grises
        if(len(image.shape) == 2):
            dimension = np.shape(image)
            filas = dimension[0]
            columnas = dimension[1]
            
            if(8 % args.nbits == 0):
                lst_txt = []
                for l in text:
                    lst_txt.append(l)

                txt_ord = []
                for character in lst_txt:
                    txt_ord.append(ord(character))#convierte a codigo ASCII
                
                txt_bin = []
                for num in txt_ord:
                    txt_bin.append("{0:{fill}8b}".format(num, fill='0'))#convierte a binario

                #creacion de matriz binaria de la imagen original
                bin_matrix = [None] * filas
                for i in range(filas):
                    bin_matrix[i] = [None] * columnas

                for n in range(filas):
                    for m in range(columnas):
                        bin_matrix[n][m] = "{0:{fill}8b}".format(image[n][m], fill='0')

                #ahora debemos considerar los bits menos significativos que nos piden
                bits_sigf = args.nbits #se obtienen los bits significativos que se usaran
                txt_bin_copy = txt_bin.copy()
                txt_bin_copy.reverse()#el ultimo sera el primero

                cortes = int(8/bits_sigf)#cantidad de divisiones del numero binario

                #esta lista almacenará los substrings
                lst_bits_codif = []
                while(txt_bin_copy):
                    num_bin = txt_bin_copy.pop()
                    ini = 0
                    fin = bits_sigf
                    for i in range(cortes):
                        lst_bits_codif.append(num_bin[ini:fin])
                        ini += bits_sigf
                        fin += bits_sigf
                
                """el valor de los bits menos significativos nbits sera guardado
                en el pixel ubicado en la ultima posicion de las filas y las columnas,
                este será guardado en binario"""
                if(bits_sigf == 1):
                    bin_matrix[filas - 1][columnas - 1] = str(bin_matrix[filas - 1][columnas - 1])[:-4] + "0001"
                if(bits_sigf == 2):
                    bin_matrix[filas - 1][columnas - 1] = str(bin_matrix[filas - 1][columnas - 1])[:-4] + "0010"
                if(bits_sigf == 4):
                    bin_matrix[filas - 1][columnas - 1] = str(bin_matrix[filas - 1][columnas - 1])[:-4] + "0100"
                if(bits_sigf == 8):
                    bin_matrix[filas - 1][columnas - 1] = str(bin_matrix[filas - 1][columnas - 1])[:-4] + "1000"

                #modificacion de la matriz de la imagen
                i = 0
                for n in range(filas):
                    if(i > len(lst_bits_codif) - 1):
                        break
                    for m in range(columnas): 
                        if(i > len(lst_bits_codif) - 1):
                            break
                        bin_matrix[n][m] = str(bin_matrix[n][m])[: - bits_sigf] + lst_bits_codif[i]
                        i += 1
                pixeles = len(lst_bits_codif)
                
                #se guarda la cantidad de pixeles que se van a usar
                bin_matrix[filas - 2][columnas - 2] = "{0:{fill}8b}".format(pixeles, fill='0')
                
                #ahora que tenemos la matriz binaria codificada debemos pasar sus valores a int para convertirla en imagen
                for n in range(filas):
                    for m in range(columnas):
                        bin_matrix[n][m] = int(bin_matrix[n][m], 2)

                img = bin_matrix.copy()
                img_numpy = np.array(img, dtype=np.uint8)
                file = io.imsave("img_out/" + img_filename[11:-4] + "_out.png", img_numpy)

            else:
                print("La cantidad de bits significativos está limitada a solo ser divisores de 8, prueba con {1,2,4,8} lo siento :(")
            
        #imagen a color
        elif(len(image.shape) == 3):
            pass
    
    #modo decode
    if args.decode:
        dimension = np.shape(image)
        filas = dimension[0]
        columnas = dimension[1]
        
        #imagen en escala de grises
        if(len(image.shape) == 2):
            num_a_codificar=[]

            #se extrae el numero de los bits menos significativos
            nbits = int("{0:{fill}8b}".format(image[filas - 1][columnas - 1], fill='0')[4:], 2)
            #nro de pixeles que se van a usar
            pixeles = image[filas - 2][columnas - 2]

            n_pix = 0
            for n in range(filas):
                for m in range(columnas):
                    if(n_pix == pixeles):
                        break
                    else:
                        num_a_codificar.append(image[n][m])
                        n_pix += 1
                break

            if(nbits == 8):#8
                decode = ''
                for elem in num_a_codificar:
                    caracter = chr(elem)
                    decode += caracter
                print(decode)

            else:
                txt_codificado_bin =[]
                j = 0
                i = 0
                while(i < len(num_a_codificar)):
                    A = ''
                    while(j < int(8 / nbits) and i < len(num_a_codificar)):
                        letra_en_binario = "{0:{fill}8b}".format(num_a_codificar[i], fill='0')[-nbits:]
                        A += letra_en_binario
                        i += 1
                        j += 1
                    txt_codificado_bin.append(A)
                    j = 0

                msj_final = ''
                for elem in txt_codificado_bin:
                    caracter_num = int(elem, 2)
                    to_char = chr(caracter_num)
                    msj_final += to_char
                print(msj_final)          

        #imagen a color
        elif(len(image.shape) == 3):
            pass
        
        

        #bits_significativos = image[]