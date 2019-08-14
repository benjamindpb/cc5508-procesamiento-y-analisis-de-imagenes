import argparse

parser = argparse.ArgumentParser(description = "Estenografía")
group = parser.add_mutually_exclusive_group()
group.add_argument("--encode", action = "store_true")
group.add_argument("--decode", action = "store_true")
    
parser.add_argument("--image", nargs = 1, type = str)
parser.add_argument("--text", nargs = 1, type = str)
parser.add_argument("--nbits", nargs = 1, type = int)

args = parser.parse_args()


#si es el script principal
if __name__ == '__main__':
    if args.encode:
        print("EnCODE")
    if args.decode:
        print("DECODE")