list = [1]
i = 0
curr = ""
for i in range(30):
    j = 0
    k = 1
    while j < len(str(list[i])):
        while(k < len(str(list[i])) and str(list[i])[k] == str(list[i])[j]):
            k+=1
        final += (str(k-j)+ str(list[i])[j])
        j = k
    list.append(final)
    final = ""
        
print(list)
print(len(list[30]))
