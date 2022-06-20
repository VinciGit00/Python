import requests
import json


def main():
    url = "https://api.github.com"
    response = requests.get(url)
    print("Response code: "+str(response.status_code))

    print(json.dumps(response.text))
    print("----------------------------------------------------------------------------------")
    # This one looks bettere
    print(response.text)
    print("----------------------------------------------------------------------------------")

    # Alternatively for GET requests:
    # In params you have to insert the payload
    res = requests.request("GET", url, headers="", data="", params="")
    print("Response code: "+str(res.status_code))

    print(res.text)


if __name__ == "__main__":
    main()
