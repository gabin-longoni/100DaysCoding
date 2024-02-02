# Band Name Generator

Ce script Python simple génère un nom de groupe basé sur les entrées de l'utilisateur.

## Comment utiliser

1. Exécutez le script.
2. Lorsqu'on vous le demande, entrez le nom de la ville où vous avez grandi.
3. Ensuite, entrez le nom de votre animal de compagnie.
4. Le script générera alors et imprimera le nom de votre groupe, qui est une combinaison du nom de la ville et du nom de l'animal.

## Code

Voici la partie principale du script :

```python
print("Welcome to the Band Generator")
cityName = input("What's the name of the city you grew up in ?\n")
petName = input("What's the name of your personal pet ?\n")
print("Your band name is: " + cityName + " " + petName)