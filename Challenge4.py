import urllib.request
import re

find = ("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+")
string = input("Enter the string to search: ")
re.findall(find, string)
