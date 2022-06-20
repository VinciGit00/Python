import requests


def main():
    url = "https://api.github.com"
    payload = {"firstName": "John", "lastName": "Smith"}

    # First method
    request = requests.post(url, headers="", data="", params=payload)

    print(request.status_code)
    print(request.text)

    # Second method
    request2 = requests.request(
        "POST", url, headers="", data="", params=payload)
    print(request2.status_code)
    print(request2.text)


if __name__ == "__main__":
    main()
