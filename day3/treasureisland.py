print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
print("Bienvenue à l'île au trésor.")
print("Votre mission est de trouver le trésor.")
direction = input("Vous êtes à un croisement. Où voulez-vous aller? Gauche ou Droite?\n").lower()
if direction == "gauche":
  action = input("Vous arrivez à un lac. Il y a une île au milieu du lac. Voulez-vous nager ou attendre? Nager ou Attendre?\n").lower()
  if action == "attendre":
    door = input("Vous arrivez à l'île indemne. Il y a une maison avec 3 portes. Une rouge, une jaune et une bleue. Laquelle choisissez-vous?\n").lower()
    if door == "jaune":
      print("Vous avez trouvé le trésor! Vous gagnez!")
    elif door == "rouge":
      print("Vous êtes brûlé par le feu. Game Over.")
    elif door == "bleue":
      print("Vous êtes mangé par des bêtes. Game Over.")
    else:
      print("Vous avez choisi une porte qui n'existe pas. Game Over.")
  else:
    print("Vous êtes attaqué par un monstre. Game Over.")
else:
    print("Vous tombez dans un trou. Game Over.")