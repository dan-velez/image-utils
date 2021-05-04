# image_denoise.py - Remove noise and artifacts from an input file.

import cv2

def denoise_image(vinpath, voutpath):
    "Remove noise from an image."
    image = cv2.imread(vinpath)
    image = cv2.fastNlMeansDenoisingColored(image,None,5,7,21)
    print("Writing: %s" %(voutpath))
    cv2.imwrite(voutpath, image)

if __name__ == "__main__":
    # TODO: CLI
    #denoise_image("denoise_in.png", "denoise_out.png")
    import sys
    if len(sys.argv) < 3:
        print("[* image_denoise] Usage:")
        sys.exit()