# Tervetuloa Arvaa Bändi -peli sivulle!!!

## Kuvaus
Kyseessä on bändipeli, jossa aloitetaan sanomalla bändi. Seuraavan pelaajan tehtävänä on arvata bändi, joka alkaa edellisen arvauksen viimeisellä kirjaimella. Pelaajalla on kolme yritystä, ennenkuin hän tipahtaa pois. Projekti on kehitysvaiheessa ja yhtyelista ei välttämättä ole vielä erityisen kattava, mutta sitä päivitetään. Peli-idea lähti lapsuuden automatkoista, joilla kyseistä peliä pelattiin ruutuvihkolla tai ihan vaan muistin varassa.

Tämä Python-sovellus on interaktiivinen arvauspeli, jossa pelaajan tulee arvata rockbändien nimiä. Jokaisen arvauksen tulee alkaa edellisen bändin viimeisellä kirjaimella. Peliä voi pelata toistuvasti ja se tarjoaa kolme arvauskertaa per pelikerta.

## Pelin kulku
<img src="pelin virtauskaavio.png" alt="komento" style="">

## Toiminnallisuudet
- Lataa bändien nimet tiedostosta ja muokkaa ne käyttökelpoiseen muotoon.
- Tarkistaa käyttäjän syöttämien bändien nimien kelvollisuuden.
- Hallinnoi pelin kulkua ja käyttäjän syötteitä.


## Käyttö
1. Varmista, että Python on asennettu.
2. Suorita peli komennolla: ```bash python3 arvaa_bandi.py```
    
=======

## Pelin koodi ja selitykset

### Moduulien tuonti
```python
import shutil
import pydoc 
```
### Funktiot

```python
def lataa_bandit(tiedostonimi):
    """
    Lataa bändien nimet tiedostosta, 
    poistaa ylimääräiset välilyönnit 
    ja muuttaa nimet pieniksi kirjaimiksi.
    """
    with open(tiedostonimi, 'r') as tiedosto:
        bandit = [line.strip().lower() for line in tiedosto.readlines()]
    return bandit
```


##### Tämä funktio lataa bändien nimet tiedostosta, poistaa ylimääräiset välilyönnit ja muuttaa kaikki nimet pieniksi kirjaimiksi.

```python
def on_validi_arvaus(bandi, bandit, arvatut_bandit, viimeinen_kirjain):
    """
    Tarkistaa, että arvaus on listalla, 
    ei vielä arvattu ja alkaa oikealla kirjaimella.
    """
    bandi = bandi.lower()
    return (
        bandi in bandit and
        bandi not in arvatut_bandit and
        (bandi[0] == viimeinen_kirjain or viimeinen_kirjain == '')
    )
```
```python
def main():
    # Hallinnoi pelin kulkua ja käyttäjän syötteitä.
    tiedostonimi = 'Bands_List.txt'
    bandit = lataa_bandit(tiedostonimi)
    arvatut_bandit = []
    viimeinen_kirjain = ''
    laskin = 1

    # Pelin ohjeet ja aloitus.
    print("Tervetuloa Arvaa Bändi -peliin!")
    print("Yritä arvata rockbändi. Jokaisen uuden bändin tulee alkaa edellisen bändin viimeisellä kirjaimella.")
    print("Pelissä on kolme yritystä, jonka jälkeen peli päättyy, jos et arvaa oikein.")
    print("Kirjoita 'lopeta' lopettaaksesi pelin.")
    print()

    while True:
        arvaus = input(f"Anna bändi, joka alkaa kirjaimella '{viimeinen_kirjain.upper()}' (tai mikä tahansa, jos ensimmäinen arvaus): ").strip()
        print()

        if on_validi_arvaus(arvaus, bandit, arvatut_bandit, viimeinen_kirjain):
            arvatut_bandit.append(arvaus.lower())
            print(f"Hyvä! {arvaus} on oikein.")
            viimeinen_kirjain = arvaus[-1].lower()
        elif laskin < 3 and arvaus.lower() != 'lopeta':
            laskin += 1
            print(f"Virheellinen arvaus tai on jo arvattu. (Virhe {laskin-1}) Yritä uudelleen.")
        else:
            if laskin == 3:
                print("3 virhettä. Hävisit.")
            print("Kiitos pelaamisesta!")
            break

    # Tulostetaan arvatut bändit keskitettynä
    print("Arvasit seuraavat bändit:".center(shutil.get_terminal_size().columns))
    for bandi in arvatut_bandit:
        padding_width = (shutil.get_terminal_size().columns - max(len(bandi) for bandi in arvatut_bandit)) // 2
        print(' ' * padding_width + bandi.upper())
    print()

def main():
```


