# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:


# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:

import csv 

with open('pisadata.csv', 'r' ) as f:
    _1 = f.read()
    print(_1)
    


# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:


# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:


# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:


# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:

#meny
def meny():
  """Skriver ut en meny med alternativ och returnerar användarens val."""
  print('1. Läs in CSV-filen')
  print('2. Bästa respektive sämsta resultat år 2018')
  print('3. Matematikkunskaper i Norden år 2003 - 2018')
  print('4. Kontinuerligt förbättrat resp. försämrat år 2003 - 2018')
  print('5. Kvinnor presterar bättre än män under åren 2003-2018.')
  print('6. Avsluta programmet.')
  val = input(f'Gör ett val 1-6: ')
  return val

def main():
  """Kör programmet."""
  while True:
    val = meny()
    if val == '1':
      # Läs in CSV-filen
      pass
    elif val == '2':
      # Visa bästa och sämsta resultat år 2018
      pass
    elif val == '3':
      # Visa matematikkunskaper i Norden år 2003 - 2018
      pass
    elif val == '4':
      # Visa kontinuerligt förbättrat resp. försämrat år 2003 - 2018
      pass
    elif val == '5':
      # Visa om kvinnor presterar bättre än män under åren 2003-2018
      pass
    elif val == '6':
      # Avsluta programmet
      break
    else:
      print('Felaktigt val. Välj ett nummer mellan 1 och 6.')

if __name__ == '__main__':
  main()
