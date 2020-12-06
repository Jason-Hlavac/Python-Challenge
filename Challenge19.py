import gzip, difflib

data = gzip.open("deltas.gz")
d1, d2 = [], []
for line in data:
    d1.append(line[:53].decode()+"\n")
    d2.append(line[56:].decode())


compare = difflib.Differ().compare(d1, d2)

link = open("f.png", "wb")
username = open("f1.png", "wb")
password = open("f2.png", "wb")

for line in compare:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == '+':
        username.write(bs)
    elif line[0] == '-':
        password.write(bs)
    else:
        link.write(bs)

link.close()
username.close()
password.close()
