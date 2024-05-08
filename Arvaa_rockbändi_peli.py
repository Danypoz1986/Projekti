def lataa_bandit(tiedostonimi):
    with open(tiedostonimi, 'r') as tiedosto:
        bandit=[line.strip().lower() for line in tiedosto.readlines()]
    return bandit
    
def on_validi_arvaus(bandi, bandit, arvatut_bandit, viimeinen_kirjain):
    bandi=bandi.lower()
    return (bandi in bandit and
            bandi not in arvatut_bandit and
            (bandi[0]==viimeinen_kirjain or viimeinen_kirjain=='') 
            )
    
def main():
    tiedostonimi = 'Rock_Bands_List.txt'
    bandit=lataa_bandit(tiedostonimi)
    arvatut_bandit=[]
    viimeinen_kirjain=''
    
    print("Tervetuloa Arvaa Rockbändi -peliin!")
    print("Yritä arvata rockbändi. Jokaisen uuden bändin tulee alkaa edellisen bändin viimeisellä kirjaimella.")
    print("Kirjoita 'lopeta' lopettaaksesi pelin.")
    
    while True:
        arvaus=input(f"Anna rockbändi, joka alkaa kirjaimella '{viimeinen_kirjain}' (tai mikä tahansa, jos ensimmäinen arvaus): ").strip()
        
        if arvaus.lower()=='lopeta':
            print("Kiitos pelaamisesta")
            break
            
        if on_validi_arvaus(arvaus, bandit, arvatut_bandit, viimeinen_kirjain):
            print(f"Hyvä! {arvaus} on oikein.")
            viimeinen_kirjain=arvaus[-1].lower()
            arvatut_bandit.append(arvaus.lower())
        else:
            print("Virheellinen arvaus tai on jo arvattu. Yritä uudelleen.")
            
    print(f"Arvasit seuraavat bändit:")
    for bandi in arvatut_bandit:
        print(bandi)
               
if __name__ == "__main__":
    main()
