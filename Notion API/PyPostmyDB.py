from email import header
from urllib import response
from xxlimited import new
import requests
import json

token = 'secret_OqxCkOUHuIbghFlcay5ex7lcCbyfYQA7kP0T59CIDfo'

databaseId = 'a24c2332602a40dd924ac97be03ac946'

header = {
    "Authorization": "Bearer "+token,
    "Notion-Version": "2022-02-22"
}

header2 = {
    "Authorization": "Bearer secret_OqxCkOUHuIbghFlcay5ex7lcCbyfYQA7kP0T59CIDfo",
    "Content-Type": "application/json",
    "Notion-Version": "2022-02-22"
}


def readDataBase(databaseId, header):
    readURL = f"https://api.notion.com/v1/databases/{databaseId}"

    res = requests.request("GET", readURL, headers=header)
    print(res.status_code)
    print(res.text)


def CreatePage(databaseId, header):
    createURL = f"https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": "gabriele"
                        }
                    }
                ]
            },
            "Category": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Franco"
                        }
                    }
                ]
            },
            "Price": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Giuseppe"
                        }
                    }
                ]
            },
            "Date": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Giuseppe"
                        }
                    }
                ]
            }
        },

    }

    data = json.dumps(newPageData)

    res = requests.request("POST", createURL, headers=header, data=data)

    print(res.status_code)
    print(res.text)


def updatePage(databaseId, header):
    updateURL = f"https://api.notion.com/v1/pages/{databaseId}"

    updateData = {
        "properties": {
            "Value": {
                "rich_text": [
                    {
                        "text": {
                            "content": "Oggetto cambiato"
                        }
                    }
                ]
            },
        }
    }

    data = json.dumps(updateData)

    response = requests.request(
        "PATCH", updateURL, headers=header, data=data)

    print(response.status_code)
    print(response.text)


if __name__ == '__main__':
    # Call read
    #readDataBase(databaseId, header)

    # Call create
    CreatePage(databaseId, header2)

    # This is the Id of the single line
    # call update
    # Each line has a unique ID
    #pageId = "7d508a3f-2d6d-433c-88ff-c5b64c8e2507"
    #updatePage(pageId, header2)
