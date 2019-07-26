#In order to use this aplication use cmd with input
# "python applicatie.py --path <<path of images>>

import time
import pytesseract
import argparse
import os
from PIL import Image
from algorithms import find
from algorithms import crop_image


def spheropost():

    '''

    This funtion is for use of scanned foto's of letters.  It prints adresses where letter should be delivered.
    Parameters:
        URL(string):  The url of the chosen letter(s).  Write python applicatie.py --path <path> in cmd in order to use this code.

    '''

    # Providing the CLI and initializing the directory
    # where images are stored, as well as saving the necessary indexes

    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required = True,
        help = "path of folder with images to be OCR'd,"
               " folder should not include another forlders")
    args = vars(ap.parse_args())

    # Variable initialization
    print("Images will be taken from path:", args["path"] + "/")
    brieven_als_text = []
    brieven_als_foto = os.listdir(args["path"] + "/")
    print("Images that are going to be analysed:",
          str(brieven_als_foto).strip("[]"))

    #iterate through each photo to process
    for img in brieven_als_foto:
        img = Image.open(args["path"] + "/" + img)

        #Cropping the picture to the desired size
        # in advance before using OCR algorithm
        img = crop_image(img)

        if img == None:
            return -1
        # img.show()

        #adding text recognized by Tesseract algorithm
        brieven_als_text.append(pytesseract.image_to_string(img, lang = 'eng'))

    #Finding the right addresses among all recognized text
    for i,text in enumerate(brieven_als_text):
        print(i,find(text,"adr"))

    #The time of the program
    print("It took ", round(time.perf_counter(), 2), " sec")
spheropost()