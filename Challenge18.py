from urllib.request import Request, urlopen
from urllib.parse import quote_plus

url = "http://www.pythonchallenge.com/pc/stuff/violin.php"
message = "the flowers are on their way"

req = Request(url, headers = { "Cookie": "info=" + quote_plus(message)})

print(urlopen(req).read())
