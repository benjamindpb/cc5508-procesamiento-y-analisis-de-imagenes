import argparse
from skimage import io


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
    
    img_filename = args.image[0]
    image = io.imread(img_filename)

    txt_filename = args.text[0]
    text = open(txt_filename, 'r').read()
    
    lst_txt = []
    for word in text:
        lst_txt.append(word)

    lst_ord = []
    for character in lst_txt:
        lst_ord.append(ord(character))#convierte a codigo ASCII
    
    lst_bin = []
    for num in lst_ord:
        lst_bin.append("{0:{fill}8b}".format(num, fill='0'))#convierte a binario
    
    print(lst_txt)
    print(lst_bin)


    #modo encode
    if args.encode:
        print("ENCODE")#print(image.shape)  ##tengo la imagen como una matriz de 250x250 (LION)
        

    #modo decode
    if args.decode:
        print("DECODE")