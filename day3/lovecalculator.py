print("L O V E  C A L C U L A T O R")
name1 = input("Entrez votre nom:\n")
name2 = input("Entrez le nom de votre partenaire:\n")
combined_name = name1 + name2
lower_combined_name = combined_name.lower()
t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")
l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")
true = t + r + u + e
love = l + o + v + e
love_score = int(str(true) + str(love))
print(f"Votre score d'amour est de: {love_score}")