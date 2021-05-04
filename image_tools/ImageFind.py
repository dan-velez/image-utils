# image_find.py - Find an image within another image.

import cv2
import numpy as np
import json


def find_image(vstr_image_path, vstr_subimage_path):
    # Return array of all coordinates within image.

    img_rgb = cv2.imread(vstr_image_path)
    template = cv2.imread(vstr_subimage_path)

    print("[* image_find] Big image size: [%s] X [%s]" % (img_rgb.shape[0], img_rgb.shape[1]))
    print("[* image_find] Small image size: [%s] X [%s]" % (template.shape[0], template.shape[1]))

    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    pts = []

    for pt in zip(*loc[::-1]):  # Switch collumns and rows
        #print(pt)
        pt_final = {
            'x1': int(pt[0]),
            'y1': int(pt[1]),
            'x2': int(pt[0] + w),
            'y2': int(pt[1] + h)
        }
        print("LOC: [%s]" % json.dumps(pt_final))
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.imshow('Image', img_rgb)
        cv2.waitKey(0)
        pts.append(pt_final)

    #cv2.imwrite('result.png', img_rgb)

    return pts

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print(
            "[* image_find] Usage: python image_find.py <target_image_path> <image_to_find_path>")
        sys.exit()
    vstr_image_path = sys.argv[1]
    vstr_subimage_path = sys.argv[2]
    print("[* image_fing] Find image in [%s]" % (vstr_image_path))
    find_image(vstr_image_path, vstr_subimage_path)
