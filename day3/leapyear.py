year = int(input("Entrez une année:\n"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print(f"{year} est une année bissextile")