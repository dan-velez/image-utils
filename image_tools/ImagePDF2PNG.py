# image_pdf2png.py - Convert a pdf to a png image. 

import os
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

CDPI = 300

def convert(vstr_pdf_path, vdpi):
    CDPI = vdpi
    try:
        # Get file metadata.
        vout_dir = os.path.sep.join(vstr_pdf_path.split(os.path.sep)[0:-1])
        vfname = ".".join(vstr_pdf_path.split(os.path.sep)[-1].split(".")[0:-1])

        # Make conversion.
        vimages = convert_from_path(
            vstr_pdf_path,
            output_file=vfname+"_", 
            output_folder=vout_dir, 
            fmt='png', 
            dpi=CDPI)

        print("[* image_pdf2png] Converted PDFs [%s] [%s] images to directory [%s]" % (
            vfname, str(len(vimages)), vout_dir))
        return vout_dir + "\\" + vfname+"_0001-1.png"
    except Exception as e:
        print("[* image_pdf2png] Could not convert PDF. " + str(e))
        return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("[* image_pdf2png] Usage: python image_pdf2png.py <vstr_pdf_path> <DPI>")
        sys.exit()
    vpdf_path = sys.argv[1]
    vdpi = sys.argv[2]
    print("[* image_pdf2png] Converting PDF: [%s]" % sys.argv[1])
    convert(sys.argv[1], vdpi)