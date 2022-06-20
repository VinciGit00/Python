from urllib import response
from Parameters import *
from RequestFunction import *
import requests
# Function for get procedures


def GETfunction():

    url = InsertUrl()
    header = insertHeader()
    body = insertBody()
    params = InsertParams()

    response = Requests("GET", url, header, body, params)
    printResponse(response)
   