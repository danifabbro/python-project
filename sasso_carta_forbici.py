import random
roccia = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

carta = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

forbici = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
elementi = [roccia,carta,forbici]
scelta_pc = random.choice(elementi)
scelta_giocatore = input("Benvenuto al gioco SASSO CARTA E FORBICI!!! Seleziona 1 per ROCCIA, 2 per CARTA, 3 per FORBICI!!\n")



if scelta_giocatore == "1":
    if scelta_pc == roccia:
        print("la tua scelta:\n" + roccia + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto ROCCIA e il computer ROCCIA. Pareggio!!\n")
    elif scelta_pc == carta:
        print("la tua scelta:\n" + roccia + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto ROCCIA e il computer CARTA. Hai perso! :(\n")
    else:
        print("la tua scelta:\n" + roccia + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto ROCCIA e il computer FORBICI. Hai vintoooo!!! Congratulazioni!!\n")
elif scelta_giocatore == "2":
    if scelta_pc == roccia:
        print("la tua scelta:\n" + carta + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto CARTA e il computer ROCCIA. Hai vintoooo!!! Congratulazioni!!\n")
    elif scelta_pc == carta:
        print("la tua scelta:\n" + carta + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto CARTA e il computer CARTA. Pareggio!!\n")
    else:
        print("la tua scelta:\n" + carta + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto CARTA e il computer FORBICI. Hai perso! :(\n")
elif scelta_giocatore == "3":
    if scelta_pc == roccia:
        print("la tua scelta:\n" + forbici + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto FORBICI e il computer ROCCIA. Hai perso! :(\n")
    elif scelta_pc == carta:
        print("la tua scelta:\n" + forbici + "\n")
        print("Scelta del computer\n" + scelta_pc + "\n")
        print("Hai scelto FORBICI e il computer CARTA. Hai vintoooo!!! Congratulazioni!!\n")
    else:
        print("Hai scelto FORBICI e il computer FORBICI. Pareggio!!\n")