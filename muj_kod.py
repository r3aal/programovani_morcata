import os

def zpracuj_soubor(nazev_souboru):
    with open (nazev_souboru, encoding = "utf-8") as soubor:
        for radek in soubor:
            radek = radek.strip()
            if not radek:
                continue
                
            jmeno, vaha, datum, cena, pohlavi = radek.split(";")

            if pohlavi == "m":
                    pohlavi = "samecek"
                
            else:
                    pohlavi = "samicka"

            cena_se_slevou = float(cena) * 0.9

            print(f"morce je {pohlavi} a jmenuje se {jmeno}")
            print(f"narodilo se {datum} a vazi {vaha}")
            print(f"morce {jmeno} stoji s 10% slevou {cena_se_slevou}")
            print()

if __name__ == "__main__":
    zpracuj_soubor("data/morcata.txt")