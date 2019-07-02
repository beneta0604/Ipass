def addtolist(data):
    '''
    This function adds parameter to list and returns it. If parameter was list type, it will do nothing.

    Parameters:
        string, integer, list: any string or integer in order to force function something do.
    Returns:
        output: It will return parameter within list if parameter was of type integer or string
    '''
    if type(data) != list:
        data=data.split(",")
        return(data)
    else:
        return(data)

def checkWhetherInt(symbol):
    '''
    This function checks whether parameter is of integer type.

    Parameters:
        character(string):Any symbol of string type.
    Returns:
        output: It returns asnwer in boolean type whether parameter is integer type.
    '''
    try:
        type(eval(symbol)) == int
        return True
    except:
        return False

