import xmlrpc.client

link = xmlrpc.client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print(link)
print(link.system.listMethods())
print(link.system.methodHelp("phone"))
print(link.system.methodSignature("phone"))
link.phone("Bert")
