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
    """#Funkce hlavního menu, která poskytuje možnosti pro přidání, zobrazení a odstranění úkolu. 
    Pokud uživatel zadá neplatnou volbu, program ho upozorní a nechá uživatele opakovat znovu."""
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
    """Funkce pro zadání nového úkolu, která ukládá název do seznamu a kontroluje, zda není vstup prázdný.
    Pokud uživatel nic nezadá nebo vloží jen mezeru, program ho vyzve k nápravě a nepustí ho dál."""
    
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
    """Funkce pro přehledné vypsání všech uložených úkolů a jejich popisů do konzole.
    Program spojí názvy úkolů s jejich popisy do slovníku a následně je postupně vytiskne uživateli."""

    if seznam_ukolu:
        print ("Seznam Úkolů:")
        for cislo, (nazev_ukolu, popis_ukolu) in enumerate(seznam_ukolu , start = 1):
            print(f"{cislo}. {nazev_ukolu} - {popis_ukolu}")
    else: 
        print("Seznam úkolů je prazdný")

def odstranit_ukol():
    """Funkce pro současné odstranění názvu i popisu úkolu, která zajišťuje synchronizaci obou seznamů.
    Program kontroluje číselný vstup, validuje rozsah indexů a v případě nesouladu počtu prvků nebo špatného zadání uživatele upozorní."""
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
    print("Konec programu")
    sys.exit()         

def logika_apky():
    """Hlavní řídicí funkce aplikace, která propojuje uživatelské rozhraní s jednotlivými operacemi nad úkoly.
    Program v nekonečné smyčce zpracovává volby uživatele, volá příslušné podfunkce a zajišťuje korektní ukončení celého systému."""
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