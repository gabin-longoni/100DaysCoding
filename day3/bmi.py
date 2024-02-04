userWeight = int(input("Entrez votre poids (en kg):\n"))
userHeight = float(input("Entrez votre taille (en m):\n"))
bmi = userWeight / (userHeight * userHeight)
if (bmi <= 18.5):
  print(f"Vous êtes en sous poids ({bmi})")
elif (bmi < 25 and bmi > 18.5):
  print(f"Vous êtes à un poids normal ({bmi})")
elif (bmi > 25 and bmi < 30):
  print(f"Vous êtes en surpoids ({bmi})")
elif (bmi > 30 and bmi < 35):
  print(f"Vous êtes obèse ({bmi})")
elif (bmi > 35):
  print(f"Vous êtes obèse clinique (Lilith) ({bmi})")

  