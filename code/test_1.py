from PIL import Image
import pytesseract
import argparse
import os
import time



ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", default="post",
	help="path of folder with images to be OCR'd, folder should not include another forlders")
args = vars(ap.parse_args())
path=args["path"]+"/"
print(path)
postcoden=["3705"]
brievenAlsText=[]
brievenAlsFoto=os.listdir(path)
print(brievenAlsFoto)
counter=0
for im in brievenAlsFoto:
    img = Image.open(path+im)
    size = img.size
    BottomL=(size[0]*3132)/3732
    BottomH=(size[1]*1616)/2616
    TopL=(size[0]*300)/3732
    TopH=(size[1]*500)/2616
    area = (TopL,TopH,BottomL,BottomH)
    # img = img.crop(area)
    if counter > 2:
        img.show()
    brievenAlsText.append(pytesseract.image_to_string(img, lang='eng'))
    counter+=1

a=0
found=0
postcode=""
adres=[]
print(brievenAlsText[-2])
print(brievenAlsText[-1])
for text in brievenAlsText:
    voriglen=len(adres)
    dublicate=0
    for letter in text:
        try:
            if type(eval(letter))==int:
                a+=1
                postcode+=letter
                if a == 4 and postcode in postcoden:
                    found=1
                    if dublicate == 2:
                        found=0
                        adres.pop(-1)
                        adres.append("skip")
                        break
                    dublicate+=1
                    continue
        except:
            a=0
            if found==0:
                postcode=""
            if found <=3 and found!=0:
                postcode+=letter
                found+=1
                if found==4:
                    text = text.split(postcode)
                    text[0] = text[0].strip(" ")
                    text[0] = text[0].split(" ")
                    huisnummer = text[0][-1]
                    adres.append(postcode + " " + huisnummer)
                    text=text[1]
                    postcode=""
                    found = 0
                    dublicate+=1
                    continue
    if len(adres)==voriglen:
        adres.append("skip")

for i in range(len(adres)):
    adres[i]=adres[i].strip("\n")
    if "\n" in adres[i]:
        adres[i]=adres[i].split("\n")
        adres[i]=adres[i][0]

print(adres)
print(round(time.perf_counter(),2))
