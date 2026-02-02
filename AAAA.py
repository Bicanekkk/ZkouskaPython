with open("test.txt","r") as f:
    pole=f.readlines()


with open("text.txt","w") as f:
    for i in f:
        rad=rad.strip()
        rad=rad.upper()
        f.write(rad+"\n")