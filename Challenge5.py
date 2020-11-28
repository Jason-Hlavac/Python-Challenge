from bs4 import BeautifulSoup
import requests

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"

for i in range(400):
    page=requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    if(str(soup).find("the next nothing is ")!= -1):
        nothing = str(soup)[str(soup).find("the next nothing is ")+20:]
        print(nothing)
    elif(str(soup).find("Divide") != -1):
        nothing = int(nothing)/2
    else:
        break
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(str(int(nothing)))
