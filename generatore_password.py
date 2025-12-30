import random
lettere = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeri = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simboli = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Benvenuto nel mio generatore di password!")

nr_lettere = int(input("Quante lettere vuoi nella tua password?/n"))
nr_numeri = int(input("Quanti numeri vuoi nella tua password?/n"))
nr_simboli = int(input("Quanti simboli vuoi nella tua password?/n"))

password_array = []

for car in range(0,nr_lettere):
    password_array.append(random.choice(lettere))

for car in range(0,nr_numeri):
    password_array.append(random.choice(numeri))

for car in range(0,nr_simboli):
    password_array.append(random.choice(simboli))

random.shuffle(password_array)

password_official = ""

for car in password_array:
    password_official += car

print("La tua password è: " + password_official)