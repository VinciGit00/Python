
import requests
from urllib import response
from Parameters import *
from RequestFunction import *


def PUTFunction():
    url = InsertUrl()
    header = insertHeader()
    body = insertBody()
    params = InsertParams()

    response = Requests("POST", url, header, body, params)
    printResponse(response)
