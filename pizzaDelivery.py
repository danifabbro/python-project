print("Benvenuto al Pizza delivery")
size = input("Che grandezza di pizza desideri? S, M oppure L: ")
pepperoni = input("Vuoi del salame in più sulla pizza? S o N: ")
extra_cheese = input("Vuoi del formaggio extra? S o N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "S":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "S":
    bill += 1


print (f"La tua pizza costa {bill} euro")