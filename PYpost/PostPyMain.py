import math
import requests
from PYpost.Match import*

while True:
    print("Select the operation you want do")
    print("1: GET")
    print("2: POST")
    print("3: PUT")
    value = input("Enter a number: \n")
    Match(value)
    print("\n")
