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
2. Suorita peli komennolla: `python3 arvaa_bandi.py`

=======


## Pelin koodi ja selitykset

### Moduulien tuonti

import shutil
import pydoc



