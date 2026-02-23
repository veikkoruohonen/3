ALAMITTA = 37

pituus = float(input("Anna kuhan pituus (cm): "))

if pituus < ALAMITTA:
    puuttuu = ALAMITTA - pituus
    print("Kuha on alamittainen. Laske se takaisin järveen.")
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallitun mittainen.")