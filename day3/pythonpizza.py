print("Merci d'qvoir choisi Python Pizza")
size = input("Quelle taille de pizza voulez-vous? S, M, L\n")
add_pepperoni = input("Voulez-vous du pepperoni? Y, N\n")
extra_cheese = input("Voulez-vous du fromage supplémentaire? Y, N\n")
bill = 0
if size == "S":
  bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Votre facture est de: {bill}€")
