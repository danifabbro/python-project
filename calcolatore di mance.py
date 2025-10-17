print("Benvenuti nel mio calcolatore di mance! \n")
total_bill = input("Qual'è la spesa totale? ")
tip_quantity = input("Quanta mancia in percentuale rispetto al totale vuoi dare? ")
people_payment = input("In quanti avete mangiato? ")

percentual_by_total = round(float(total_bill), 2) / 100 * round(float(tip_quantity))

total = (round(float(total_bill)) + round(percentual_by_total)) / int(people_payment)

print(f"Ognuno di voi dovrà pagare ciascuno: {total} euro")
