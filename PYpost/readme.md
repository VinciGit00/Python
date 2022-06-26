# PostPy

## Introduction

PostPy is a python script that allows to do POST, GET and PUT exactly like postman but in python terminal.

Why should you use PostPy even if there is a better developed app like Postman that do the same things? Because python is cute and you can do the same things only from terminal.
No data is stored and your privacy is safe.

## Requirements

The library required is requests for Python.

You can install it opening your virtual environment and run:

```python
pip install requests
#Otherwise if you have conda you can install it using conda

conda install requests
```

The documentation of the library is the following: [https://requests.readthedocs.io/en/latest/](https://requests.readthedocs.io/en/latest/)

## General info

The app does not do any data storage and does not use any database.

The script starts with a loop and after any HTTP request you can see the result with his status code.

## Instructions to run PostPy on your PC

First you have to install the library required and after you have to open the directory with terminal and run:

```python
python3 PostPy.py
```

Otherwise you can run the script from any IDE, like VSC or Atom.
