import cv2


class ImageScale:
    """Use CV2 to scale an image by a factor.""" 

    def image_scale (self, vstr_inpath, vstr_outpath, vint_scale):
        """Scale an image by an input factor."""
        oriimg = cv2.imread(vstr_inpath)
        height, width, depth = oriimg.shape
        newX,newY = oriimg.shape[1]*vint_scale, oriimg.shape[0]*vint_scale
        newimg = cv2.resize(oriimg,(int(newX),int(newY)))
        cv2.imwrite(vstr_outpath, newimg)