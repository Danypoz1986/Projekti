import shutil
import pydoc

# Funktio lataa bändien nimet annetusta tiedostosta, poistaa ylimääräiset välilyönnit ja muuttaa nimet pieniksi kirjaimiksi.
def lataa_bandit(tiedostonimi):
    with open(tiedostonimi, 'r') as tiedosto:
        bandit = [line.strip().lower() for line in tiedosto.readlines()]
    return bandit

# Tarkistaa, onko käyttäjän syöttämä arvaus kelvollinen. Arvauksen täytyy olla listalla, ei vielä arvattu ja alkaa oikealla kirjaimella.
def on_validi_arvaus(bandi, bandit, arvatut_bandit, viimeinen_kirjain):
    bandi = bandi.lower()
    return (
        bandi in bandit and
        bandi not in arvatut_bandit and
        (bandi[0] == viimeinen_kirjain or viimeinen_kirjain == '')
    )

# Pääfunktio, joka hallinnoi pelin kulkua
def main():
    tiedostonimi = 'Bands_List.txt'
    bandit = lataa_bandit(tiedostonimi)
    arvatut_bandit = []
    viimeinen_kirjain = ''
    laskin = 1

    print()
    print("Tervetuloa Arvaa Bändi -peliin!")
    print()
    print("Yritä arvata rockbändi. Jokaisen uuden bändin tulee alkaa edellisen bändin viimeisellä kirjaimella.")
    print()
    print("Pelissä on kolme yritystä, jonka jälkeen peli päättyy, jos et arvaa oikein.")
    print()
    print("Kirjoita 'lopeta' lopettaaksesi pelin.")
    print()

    while True:
        arvaus = input(f"Anna bändi, joka alkaa kirjaimella '{viimeinen_kirjain.upper()}' (tai mikä tahansa, jos ensimmäinen arvaus): ").strip()
        print()

        if on_validi_arvaus(arvaus, bandit, arvatut_bandit, viimeinen_kirjain):
            arvatut_bandit.append(arvaus.lower())
            print(f"Hyvä! {arvaus} on oikein.")
            print()
            viimeinen_kirjain = arvaus[-1].lower()
        elif laskin < 3 and arvaus.lower() != 'lopeta':
            laskin += 1
            print(f"Virheellinen arvaus tai on jo arvattu. (Virhe {laskin-1}) Yritä uudelleen.")
            print()
        else:
            if laskin == 3:
                print("3 virhettä. Hävisit.")
                print()
            print("Kiitos pelaamisesta!")
            print()
            break

    # Tulostetaan arvatut bändit keskitettynä
    print("Arvasit seuraavat bändit:".center(shutil.get_terminal_size().columns))
    for bandi in arvatut_bandit:
        padding_width = (shutil.get_terminal_size().columns - max(len(bandi) for bandi in arvatut_bandit)) // 2
        print(' ' * padding_width + bandi.upper())
    print()

if __name__ == "__main__":
    # Pelin toistuva suoritus kunnes käyttäjä päättää lopettaa
    while True:
        main()
        uusi_peli = ''
        while uusi_peli != 'k' and uusi_peli != 'e':
            uusi_peli = input("Haluatko pelata uudelleen? [K]yllä vai [E]i ").lower().strip()
            if uusi_peli != 'k' and uusi_peli != 'e':
                print()
                print("Syötä 'K' jatkaaksesi tai 'E' lopettaaksesi.")
            print()
        if uusi_peli == 'e':
            break
    print("Heippa!!")
    print()
    pydoc.writedoc('Arvaa_Bändi')