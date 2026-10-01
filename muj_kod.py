import os

def zpracuj_soubor(nazev_souboru):
    with open (os.sep.join([nazev_souboru]), encoding = "utf-8") as soubor:
        for radek in soubor:
            radek = radek.strip()
            if not radek:
                continue