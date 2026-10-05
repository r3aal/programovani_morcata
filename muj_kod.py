import os

def zpracuj_soubor(nazev_souboru):
    with open (os.sep.join([nazev_souboru]), encoding = "utf-8") as soubor:
        for radek in soubor:
            radek = radek.strip()
            if not radek:
                continue

                jmeno, vaha, datum, cena, pohlavi = radek.split(";")

                if pohlavi == m:
                    pohlavi = "samecek"
                
                else
                    pohlavi = "samicka"

                cena_se_slevou = float(cena) * 0.9