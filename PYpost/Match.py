
from POST import *
from PUT import *
from GET import *

# Switch case for the application


def Match(value):
    a = "3"
    if(value == "1"):
        GETfunction()
    elif(value == "1"):
        PUTFunction()
    if(value == "1"):
        POSTFunction()
    else:
        print("You have not selected a valid option")
