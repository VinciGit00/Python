import requests


def Requests(operation, url, header, body, params):
    response = requests.request(
        operation, url, headers=header, data=body, params=params)
    return response


def printResponse(res):
    print("Status code: "+str(res.status_code))
    print("Response: ")
    print(res.text)
