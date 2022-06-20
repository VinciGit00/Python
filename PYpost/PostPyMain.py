import math
import requests
from Match import *


def main():
    while True:
        print("Select the operation you want do")
        print("1: GET")
        print("2: POST")
        print("3: PUT")
        value = input("Enter a number: \n")
        Match(value)
        print("\n")


if __name__ == "__main__":
    main()
