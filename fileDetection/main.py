# The OS module in Python provides functions for interacting with the operating system.
# OS comes under Python's standard utility modules. This module provides a portable
# way of using operating system dependent functionality.
# The *os* and *os. path* modules include many functions to interact with the file system

import os

t = "C:\\Users\\fchen\\Desktop\\test.txt"

if os.path.exists(t):
    print("That location exists!")
    if os.path.isfile(t):
        print("That is a file")
    elif os.path.isdir(t):
        print("That is a directory!")
else:
    print("That location doesn't exist!")