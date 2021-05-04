# image_invert.py - Invert image colors. 

import cv2

def invert_colors(vinput_path, voutput_path):
    "Read in image and invert. Output to path."
    imagem = cv2.imread(vinput_path)
    imagem = (255-imagem)
    cv2.imwrite(voutput_path, imagem)

if __name__ == "__main__":
    import sys
    import os

    if len(sys.argv) < 3:
        print("Usage: image_invert <input path> <output path>")
        exit()

    vinput_path = os.path.abspath(sys.argv[1])
    voutput_path = os.path.abspath(sys.argv[2])

    print("Invert image [%s] to [%s]" % (vinput_path, voutput_path))

    invert_colors(vinput_path, voutput_path)