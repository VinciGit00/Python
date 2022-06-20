
def InsertUrl():
    url = input("Enter the URL for the GET: \n")
    return url
# Params

def InsertParams():

    params = ""
    while True:
        flagParams = input("Would you insert Params? Y/N\n")
        if(flagParams == "Y" or flagParams == "N"):
            if(flagParams == "Y"):
                params = input("Insert the parameters \n")
            break
        else:
            print("You've inserted a not correct value")
    return params
# Header


def insertHeader():
    header = ""
    while True:
        flagHeader = input("Would you insert a header? Y/N\n")
        if(flagHeader == "Y" or flagHeader == "N"):
            if(flagHeader == "Y"):
                header = input("Insert the header \n")
            break
        else:
            print("You've inserted a not correct value")
    return header

# Body


def insertBody():
    body = ""
    while True:
        flagBody = input("Would you insert the body? Y/N\n")
        if(flagBody == "Y" or flagBody == "N"):
            if(flagBody == "Y"):
                body = input("Insert the body \n")
            break
        else:
            print("You've inserted a not correct value")
    return body
