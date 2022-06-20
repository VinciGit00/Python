
from PYpost.GET import *
from PYpost.POST import *
from PYpost.PUT import *

# Switch for the application


def Match(value):
    match value:
        case "1":
            GETfunction()
        case "2":
            PUTFunction()
        case "3":
            POSTFunction()
        case _:
            print("You have not selected a valid option")
