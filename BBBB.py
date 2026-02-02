soucet=0
pocet=0
with open("cisla.txt", "r") as f:
    for rad in f:
        rad=rad.strip()
        cs=int(rad)
        soucet=soucet+cs
        pocet=pocet+1
print(soucet/pocet)