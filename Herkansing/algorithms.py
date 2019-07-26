from PIL import Image
from Sosfunctions import check_whether_int

def crop_image(img, oppervlakte=(23, 19)):
    '''
    
    This funtion finds coordinates of rectangle with specified parameters on foto.
    After, coordinates are passed to crop function.
    Before using you must be sure that foto is processed same way as foto that is used in the example.
    
    Parameters:
        img binary:  Image that are going to be processed. It can be obtained by using PIL module.
        oppervalkte(optionally) tuple: Tuple that consist 2 arguments: width and hight of rectangle in %.
    
    '''
    
    # Resizes image and loads pixels of it.
    im = img.resize((img.size[0] // 30,img.size[1] // 30), Image.NEAREST)
    pix = im.load()
    
    # Initialisation
    WIDTH = 1.19*oppervlakte[0]
    HIGHT = 0.83*oppervlakte[1]
    left_top_corner = 0
    grenz = 0
    rect = 0

    # Iteration through each pixel.
    for y in range(im.size[1]):
        if rect:
            break
        for x in range(im.size[0]):
            
            # if left top corner of rectangle is found
            if left_top_corner and x < left_top_corner[0]:
                continue
            #Check if pixel is black colour.
            if pix[x, y] < 200:
                #safe coordinates of first black pixel that can be potential left top corner of rectangle
                if left_top_corner == 0:
                    left_top_corner = x, y
            else:
                # if corner wasn't found.
                if left_top_corner == 0:
                    continue
                # First safe of length of rectangle
                if grenz == 0:
                    if x - left_top_corner[0] >= WIDTH:
                        grenz = x
                        break
                    else:
                        #
                        left_top_corner = 0
                        continue
                # if grenz 
                if x < grenz:
                    #
                    if y - left_top_corner[1] >= HIGHT:
                        rect = left_top_corner, (grenz - 1, y - 1)
                        break
                    #
                    else:
                        left_top_corner = 0
                        grenz = 0
                        continue
                #
                else:
                    break
    #найден ли
    if type(rect) != int:
        area = rect[0][0] * 30, rect[0][1] * 30,\
               rect[1][0] * 30, rect[1][1] * 30
        return img.crop(area)
    else:
        return None


def find(text, mode, to_find=""):

    if mode == "adr":
        text = text.split("\n")
        if len(text) > 1 and \
                check_whether_int_in_the_row\
                (text[-2] + ", " + text[-1], 4) == (4, 4):
            return text[-2] + ", " + text[-1]
        else:
            return -1

    elif mode == "F" and len(to_find) :
        print(len(to_find))
        text = text.split(to_find)
        if len(text) > 1:
            loc=[]
            amount = len(text) - 1
            location = len(text[0]) + len(to_find)
            for i in range(len(text) - 1):
                if i:
                    location += len(text[i]) + len(to_find)
                    loc.append(location)
                else:
                    loc.append(len(text[i]))
            return amount, loc
        else:
            return -1


def check_whether_int_in_the_row(text, number_in_the_row):
    digits = 0
    for symbol in text:
        if check_whether_int(symbol):
            digits += 1
        else:
            if digits >= number_in_the_row:
                return number_in_the_row, digits
            else:
                digits = 0
    return -1
# print(checkWhetherIntInTheRow('Panweg 6, NL-3705 GD ZEIST',4))
