"""
Hold functions and code temporarily while refactoring.
"""

try:
    from PIL import Image
except ImportError:
    import Image
import PIL.ImageOps
import numpy as np
from skimage import io
from skimage.transform import rotate
from skimage.color import rgb2gray
from deskew import determine_skew


def preprocess_1099(vstr_path, vstr_out_path):
    "This is the function used in the 1044 extractor."
    # Deskew
    # deskew_image(vstr_path, vstr_path)

    # Read image
    img = cv2.imread(vstr_path)

    # Normalize image
    #vnormalized = np.zeros((2475, 3203))
    #img = cv2.resize(img, (2475, 3203))
    #img = cv2.normalize(img,  img, 0, 255, cv2.NORM_MINMAX)

    # Crop
    # img = img[115:1700, 100:2400] # TODO: Auto detect crop
    # img = img[50:2400, 50:3000] # TODO: Auto detect crop
    
    # Equalize
    img_final = cv2.imread(vstr_path)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  
    # for black text , cv2.THRESH_BINARY_INV

    cv2.imwrite(vstr_out_path, new_img)
    return "Processed and Wrote image succesfully."