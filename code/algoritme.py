from SosFunctions import addtolist
from SosFunctions import checkWhetherInt
def FindPostcode(brievenAlsText,postcoden):
    '''
    This function is used to extract address(es) that is(are) corresponding to the specified index(ces) from given text.
    If in the text there will be found the indices for which the first four digits match or the indices will not be found at all to corresponding text will be given label "skip"


    Parameters:
        texts within list or one list as string type: Text must include indices or in output to text will be given label "skip"
        index(ces)string or integer type: Hier must be specified first four digits of indices that you want to be find among given text.
    Returns:
        output: It returns adresses within list that are corresponding to texts within list.
    '''

    # preparing the variables to be used throughout the next iteration
    addtolist(brievenAlsText)
    addtolist(postcoden)
    cijfer=0
    gevonden=0
    postcode=""
    adres=[]

    # Iterate through all available texts.
    for text in brievenAlsText:
        # initialization of variables necessary for label skipping
        voriglen=len(adres)
        dublicate=0
        # finding the address in this text
        for symbol in text:
            # checking whether a character is an int type
            if checkWhetherInt(symbol):
                #  put all characters following each other in 1 string
                cijfer+=1
                postcode+=symbol
                # If accumulated 4 characters in a row (index has found)
                if cijfer == 4 and postcode in postcoden:
                    gevonden=1
                    # check whether the string consisting of 4 characters is not identical to the previous one
                    if dublicate == 2:
                        # This text will be given a label to skip and the iteration will go to the next text
                        adres.pop(-1)
                        adres.append("skip")
                        break
                    dublicate+=1
                    continue
            else:
                # the case if 4 numbers did not meet in a row
                cijfer=0
                if gevonden==0:
                    postcode=""
                # assignment of two letters to an already specified index
                if gevonden <=3 and gevonden!=0:
                    postcode+=symbol
                    gevonden+=1
                    # preparation of the final address
                    if gevonden==4:
                        # finding the house number
                        text = text.split(postcode)
                        text[0] = text[0].strip(" ")
                        text[0] = text[0].split(" ")
                        huisnummer = text[0][-1]
                        # add the full address and bring all variables to the initial state for the remaining text
                        adres.append(postcode + " " + huisnummer)
                        text=text[1]
                        postcode=""
                        gevonden = 0
                        dublicate+=1
                        continue
        # check whether any address was found
        if len(adres)==voriglen:
            adres.append("skip")

    # getting rid of unnecessary data between the index and the house number
    for i in range(len(adres)):
        adres[i]=adres[i].strip("\n")
        if "\n" in adres[i]:
            adres[i]=adres[i].split("\n")
            adres[i]=adres[i][0]
    return(adres)

