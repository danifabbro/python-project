print("Benvenuto al Pizza delivery")
size = input("Che grandezza di pizza desideri? S, M oppure L: ")
pepperoni = input("Vuoi del salame in più sulla pizza? S o N: ")
extra_cheese = input("Vuoi del formaggio extra? S o N: ")

bill = 0

if size == "S": #pizza piccola
    bill = 15
    if pepperoni == "S": #dico si al salame in più
        bill += 2
        if extra_cheese == "S":  #dico si al formaggio extra
            bill += 1
elif size == "M":  #pizza media
    bill = 20
    if pepperoni == "S": #dico si al salame in più
        bill += 3
elif size == "L":    #pizza grande
    bill = 25
    if pepperoni == "S": #dico si al salame in più
        bill += 3
        if extra_cheese == "S": #dico si al formaggio extra
            bill += 1
else:
    print("Hai digitato male la misura")

print(f"La pizza costa {bill} euro")