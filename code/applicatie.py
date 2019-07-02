#In order to use this aplication use cmd with input "python applicatie.py --path <<path of images>> --index <<digit,digit,digit,digit>>"
# for example: python applicatie.py --path images/post --index 3787,3822

from PIL import Image
import pytesseract
import argparse
import os
import time
from algoritme import FindPostcode

def spheropost():
    '''
    This funtion is for use of scanned foto's of letters. It prints adresses where letter should be delivered.

    Parameters:
        URL(string): The url of the chosen letter(s). Write python applicatie.py --path <path> in cmd in order to use this code.In addition you must specify index attribute.
        Index: Index(first four digits) of letters where letters can be delivered. Write python applicatie.py --index <four digits>in cmd in order to use this code.In addition you must specify path attribute.
    '''
    # Providing the CLI and initializing the directory where images are stored, as well as saving the necessary indexes
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--path", required=True,
        help="path of folder with images to be OCR'd, folder should not include another forlders")
    ap.add_argument("-i", "--index", required=True,
        help="first 4 digits of index(es)")
    args = vars(ap.parse_args())
    # Variable initialization
    print("Images will be taken from path:",args["path"]+"/")
    postcoden=args["index"]
    brievenAlsText=[]
    brievenAlsFoto=os.listdir(args["path"]+"/")
    print("Images that are going to be analysed:",str(brievenAlsFoto).strip("[]"))
    #iterate through each photo to process
    for im in brievenAlsFoto:
        img = Image.open(args["path"]+"/"+im)
        #Cropping the picture to the desired size in advance
        size = img.size
        BottomL=(size[0]*3132)/3732
        BottomH=(size[1]*1616)/2616
        TopL=(size[0]*300)/3732
        TopH=(size[1]*500)/2616
        area = (TopL,TopH,BottomL,BottomH)
        img = img.crop(area)
        #adding text recognized by Tesseract algorithm
        brievenAlsText.append(pytesseract.image_to_string(img, lang='eng'))
    #Finding the right addresses among all recognized text
    print(FindPostcode(brievenAlsText,postcoden))
    #The time of the program
    print("It took ",round(time.perf_counter(),2), " sec")
spheropost()