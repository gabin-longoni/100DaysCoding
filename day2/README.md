# Tip Calculator

Ce script Python simple calcule combien chaque personne devrait payer en incluant le pourboire.

## Comment utiliser

1. Exécutez le script.
2. Lorsqu'on vous le demande, entrez le montant total de la facture.
3. Ensuite, entrez le pourcentage de pourboire que vous souhaitez donner (10, 12, ou 15).
4. Enfin, entrez le nombre de personnes entre lesquelles la facture sera divisée.
5. Le script calculera et affichera combien chaque personne devrait payer.

## Code

Voici la partie principale du script :

```python
print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill ? \n $"))
percentage_tip = int(input("What percentage tip would you like to give ? 10, 12, or 15\n"))
people = int(input("How many people to split the bill ?\n"))

formula = (total_bill + (total_bill * (percentage_tip/100))) / people

print(f"Each person should pay: ${formula}")