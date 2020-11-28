import math

string = input("Enter your String: ")
dictionary = {}
for i in range(len(string)):
    if string[i] not in dictionary:
        dictionary[string[i]] = 1
    else:
        dictionary[string[i]] += 1
print (dictionary)
