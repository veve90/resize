#!/usr/bin/env python
import PIL
from PIL import Image
import os
import sys

mywidth = 300

def resize_images(directoryIn, directoryOut):
    for filename in os.listdir(directoryIn):
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            # image path
            imagPath = os.path.join(directoryIn, filename)
            print("Input image: " + imagPath)
            outputImagPath = os.path.join(directoryOut, filename)

            # resize image
            img = Image.open(imagPath)
            wpercent = (mywidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((mywidth,hsize), PIL.Image.ANTIALIAS)
            img.save(outputImagPath)
            print("Ouput image: " + outputImagPath)
       