#!/usr/bin/python
import cv2


class ImageAutocrop:
    """Find the contours of an image and crop out the portion which falls
    within a range that is input."""

    def autocrop (self, vstr_input, vstr_output):
        image = cv2.imread(vstr_input)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7,7), 0)
        thresh = cv2.threshold(blur, 0, 255, 
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
        dilate = cv2.dilate(thresh, kernel, iterations=4)
        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, 
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        # Store largest contour here.
        vlg = []
        vmax = 0

        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            print(x, y, w, h)
            
            # Test if largest by width.
            if w > vmax: 
                vlg = [x, y, w, h]
                vmax = w

            if ((w > 1900) and (w < 2300)) and ((h > 1300) and (h <1600)):
                print(x, y, w, h)
                cv2.rectangle(image, (x, y), (x+w, y+h), (36,255,12), 2)
                # image = image[y:y+h, x:x+w]
                break

        # Draw rectangle over largest contour.
        cv2.rectangle(image, 
            (vlg[0], vlg[1]), 
            (vlg[0]+vlg[2], vlg[1]+vlg[3]), 
            (36,255,12), 2)

        # Write out new image.
        cv2.imwrite(vstr_output, image)