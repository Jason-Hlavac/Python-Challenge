import datetime
years = []

for i in range(1016, 1997, 20):
    years.append(i)

for i in range (len(years)):
    x = datetime.datetime(int(years[i]), 1, 26)
    if(x.strftime("%A") == "Monday"):
        print(x)
