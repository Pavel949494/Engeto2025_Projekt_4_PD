"""
projekt_4.py: Čtvrtý projekt do Engeto Online Python Akademie

author: Pavel Dostalík
email: pavel.dostalík94@gmail.com
"""


import sys

polozky_menu = ["Správce úkolů - Hlavní menu", 
                "1. Přidat nový úkol", 
                "2. Zobrazit všechny úkoly", 
                "3. Odstranit úkol", 
                "4. Konec programu"]

seznam_ukolu = []

def hlavni_menu():
    """Zobrazuje uživatelské rozhraní s dostupnými akcemi a zajišťuje navigaci v programu. 
    V cyklu vypisuje položky menu a čeká na uživatelskou volbu, dokud není proces ukončen."""

    vyber_polozky_menu = True 
    while vyber_polozky_menu:
        for polozka in polozky_menu:
            print(polozka)
        
        zadana_volba = (input("Vyberte možnost:  "))
        if zadana_volba.isnumeric() and int(zadana_volba) in range (1, len(polozky_menu)):
            vyber_polozky_menu = False
        else:
            print("Zadejte číselnou hodnotu")
    
    return(zadana_volba)

def pridat_ukol():
    """Zajišťuje zadání platného názvu úkolu pomocí nekonečného cyklu. 
    Pokud uživatel zadá prázdný řetězec nebo mezeru, program ho vyzve k novému zadání."""
    
    validace_nazvu_ukolu = True
    while validace_nazvu_ukolu:
        novy_ukol = input("Zadejte název úkolu:  ")
        if novy_ukol == " " or  novy_ukol == "":
            print("Vyplňte znovu název úkolu")
        else:
            validace_nazvu_ukolu = False

    validace_popisu_ukolu = True       
    while validace_popisu_ukolu:
        popis_noveho_ukolu = input("Zadejte popis úkolu:  ")
        if popis_noveho_ukolu == " " or  popis_noveho_ukolu == "":
            print("Vyplňte znovu popis úkolu")
        else:
            validace_popisu_ukolu = False
    
    seznam_ukolu.append([novy_ukol, popis_noveho_ukolu]) 
    return seznam_ukolu

def zobrazit_ukoly():
    """Vypisuje přehled všech uložených úkolů s jejich pořadovým číslem a popisem. 
    V případě, že je seznam prázdný, informuje uživatele o tom, že nemá žádné úkoly k zobrazení."""

    if seznam_ukolu:
        print ("Seznam Úkolů:")
        for cislo, (nazev_ukolu, popis_ukolu) in enumerate(seznam_ukolu , start = 1):
            print(f"{cislo}. {nazev_ukolu} - {popis_ukolu}")
    else: 
        print("Seznam úkolů je prazdný")

def odstranit_ukol():
    """Zajišťuje bezpečné odstranění úkolu ze seznamu podle jeho pořadového čísla. 
    Program kontroluje, zda je vstupem číslo a zda se daný úkol v seznamu skutečně nachází, 
    přičemž při neplatném zadání vyzve uživatele k opakování."""

    index_smazaneho_ukolu = True 
    while index_smazaneho_ukolu: 
        odebrat_ukol = (input("Zadejte číslo úkolu, který chcete odstranit: "))
        if odebrat_ukol.isnumeric():
            index_ukolu = int(odebrat_ukol) - 1
            pocet_ukolu = len(seznam_ukolu) 
            if index_ukolu in range(pocet_ukolu):
                seznam_ukolu.pop(index_ukolu)
                index_smazaneho_ukolu = False
            else:
                print("Špatná hodnota čísla úkolu, zadejte znovu")
        else:
            print("Zadejte číselnou hodnotu")
    return(seznam_ukolu)

def konec_programu():
    """Ukončí běh aplikace a vypíše potvrzovací zprávu do konzole. 
    Pomocí systémového volání zajistí okamžité a čisté zavření celého skriptu."""

    print("Konec programu")
    sys.exit()         

def logika_apky():
    """Hlavní nekonečný cyklus aplikace, který propojuje volbu uživatele s konkrétními funkcemi. 
    Na základě vstupu z menu spouští přidávání, prohlížení, mazání úkolů nebo ukončení celého programu."""

    Task_Manager = True
    while Task_Manager: 
        zadana_volba = hlavni_menu()
        if zadana_volba == "1":
            pridat_ukol()   
        elif zadana_volba == "2":
            zobrazit_ukoly()
        elif zadana_volba == "3":
            odstranit_ukol()
        elif zadana_volba == "4":
            konec_programu()


if __name__ == "__main__":
    logika_apky()
