import argparse

def hola():
    print("hola chavales")
    
parser = argparse.ArgumentParser()
parser.add_argument("--image", type = str, help = "indica la imagen sobre la que se trabajará", action = "store_true")
parser.add_argument("--text", type = str, help = "indica el archivo que contiene el texto a codificar", action = "store_true")

group = parser.add_mutually_exclusive_group()
group.add_argument("--encode", help = "encodifica", action = "store_true")
group.add_argument("--decode", help = "decodifica", action = "store_true")

args = parser.parse_args()

#si es el script principal
if __name__ == '__main__':
    if args.encode and args.image and args.text:
        print(args)
    if args.decode:
        print("D")
