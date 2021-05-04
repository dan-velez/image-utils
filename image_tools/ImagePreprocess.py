# preprocessor.py - Preprocess an image for OCR.

try:
    from PIL import Image
except ImportError:
    import Image
import cv2
import numpy as np
from typing import Tuple
from deskew import determine_skew
import math

def rotate(image, angle, background):
    old_width, old_height = image.shape[:2]
    angle_radian = math.radians(angle)
    width = abs(np.sin(angle_radian) * old_height) + abs(np.cos(angle_radian) * old_width)
    height = abs(np.sin(angle_radian) * old_width) + abs(np.cos(angle_radian) * old_height)

    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    rot_mat[1, 2] += (width - old_width) / 2
    rot_mat[0, 2] += (height - old_height) / 2
    return cv2.warpAffine(image, rot_mat, (int(round(height)), int(round(width))), borderValue=background)

def deskew_image(vinput, voutput):
    image = cv2.imread(vinput)
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    angle = determine_skew(grayscale)
    rotated = rotate(image, angle, (255, 255, 255))
    cv2.imwrite(voutput, rotated)

def debug_show_image(image_tmp_path):
    image = cv2.imread(image_tmp_path)
    cv2.imshow('image', image)
    cv2.waitKey(0)

def invert_colors(vinput_path, name):
    "Read in image and invert. Output to path."
    imagem = cv2.imread(vinput_path)
    imagem = (255-imagem)
    cv2.imwrite(name, imagem)

def preprocess_1099(vstr_path, vstr_out_path):
    "This is the function used in the 1044 extractor. TODO: add deskew."
    # Deskew
    deskew_image(vstr_path, vstr_path)

    # Read image
    img = cv2.imread(vstr_path)

    # Normalize image
    vnormalized = np.zeros((2475, 3203))
    img = cv2.resize(img, (2475, 3203))
    img = cv2.normalize(img,  img, 0, 255, cv2.NORM_MINMAX)

    # Crop
    # img = img[115:1700, 100:2400]
    img = autocrop(img)

    # Equalize
    img_final = cv2.imread(vstr_path)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv2.THRESH_BINARY_INV

    # Write
    cv2.imwrite(vstr_out_path, new_img)

    # Invert
    # invert_colors(vstr_out_path, vstr_out_path)

    return "Processed and Wrote image succesfully."


def denoise_image(vinpath, voutpath):
    "Remove noise from an image."
    image = cv2.imread(vinpath)
    image = cv2.fastNlMeansDenoisingColored(image,None,5,7,21)
    cv2.imwrite(voutpath, image)