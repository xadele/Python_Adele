import random  # Importē random moduli, kas nepieciešams, lai izvēlētos nejaušu elementu no saraksta

# Galvenā vārdnīca ar galvenajām atslēgām un to vērtībām
main_dictionary = {
    "leduslācis": {  
        "galvena_vertiba": "Lielākais sauszemes plēsējs, baltas, biezs kažoks.",  
        "Antarktīda": {  
            "subkey1": "Izolēta un attāla cilvēku neapdzīvota vieta.",  
            "subkey2": "Viena no sausākajām un vēsākajām vietām."  
        }
    },
   "zilonis": {  
        "galvena_vertiba": "Vislielākais uz sauszemes dzīvojošais zīdītājs, veido ģimeņu grupas.",  
        "Āfrika": {  
            "subkey1": "Daudzveidīga ar savu ainavu: savannām, džungļiem, kalni un ūdeņi.",  
            "subkey2": "Viena no visvairāk saulainajām vietām ar sausu klimatu."  
        }
    },
   "panda": {  
        "galvena_vertiba": "Apspalvojums ir biezs, silts un sargā to no aukstā kalnu klimata ir lāču dzimtā.",  
        "Ķīna": {  
            "subkey1": "Bagāta ar vēsturi un tradīcijām, tai skaitā ar lielajiem mūriem un senajiem tempļiem.",  
            "subkey2": "Augsti kalni, plakanas ielejas, skaisti ezeri un upes, piemēram, Huanghe."  
        }
    },
   "grizlilācis": {  
        "galvena_vertiba": "Katras spalvas gals ir gaišs, gandrīz balts, un tas izskatās sudrabots.",  
        "Ziemeļamerika": {  
            "subkey1": "Tur ir vairāki lielākie un vissvarīgākie pasaules pilsētu centri.",  
            "subkey2": "Daudz dažādu klimata zonu, sākot no polāra klimata ziemeļos līdz tropu klimata dienvidos."  
        }
    },
   "gepards": {  
        "galvena_vertiba": "Slavens ar savu ātrumu, to uzskata par mazāko starp lielajiem kaķiem.",  
        "Āfrika": {  
            "subkey1": "Slavena ar savu bagāto kultūru un tradīcijām, kas ietver dažādas mūzikas, dejotāju formas u.c.",  
            "subkey2": "Pārsvarā visu gadu turās nemainīgi augsta temperatūra."  
        }
    },
   "lauva": {  
        "galvena_vertiba": "Liels un veikls dzīvnieks. Tas ir otrs lielākais kaķu dzimtas dzīvnieks.",  
        "Āfrika": {  
            "subkey1": "Ļoti silts klimats un daudz saulainu dienu.",  
            "subkey2": "Daudzveidīga ar savu ainavu: savannām, džungļiem, kalniem un ūdeņiem."  
        }
    },
   "ķengurs": {  
        "galvena_vertiba": "Vislielākie somaiņi, tiem ir lielas, spēcīgas pakaļkājas un gara muskuļta aste.",  
        "Austrālija": {  
            "subkey1": "Pazīstama ar savu unikālo dzīvnieku pasauli.",  
            "subkey2": "Šis kontinents ir arī slavens ar savu daudzveidīgo ainavu."  
        }
    },
   "ronis": {  
        "galvena_vertiba": "Gludi, pludlīniju formās veidoti ķermeņi, vienā vidē lempīgs un lēns, otrā ātrs un veikls.",  
        "Okeāns": {  
            "subkey1": "Lieli H2O platības, kas pazīstamas ar savu dziļumu un bagātīgu bioloģisko daudzveidību.",  
            "subkey2": "Svarīgs elements pasaules klimata sistēmā."  
        }
    },
   "koala": {  
        "galvena_vertiba": "Somaiņu zīdītājs, vienīgā mūsdienās dzīvojošā suga no tās ģints, biezs kažoks un lielas ausis.",  
        "Austrālija": {  
            "subkey1": "Mājvieta dažādām kultūrām un tradīcijām, sākot no senajiem aborigēniem.",  
            "subkey2": "Ir vairākas no pasaules skaistākajām un slavenākajām pilsētām."  
        }
    },
   "pingvīns": {  
        "galvena_vertiba": "Viņiem ir īpaša ķermeņa plūdlīnijas forma, kas tiem ideāli noder, vidējais ātrums ir 8 km/h,",  
        "Antarktīda": {  
            "subkey1": "Pārsvarā aug sporaugi (aļģes, ķērpji, sūnas).",  
            "subkey2": "Vieno no neapdzīvotākajām vietām, pārsvarā dzīvo tikai zinātniskie pētnieki."  
        }
    }
}

dictionary1 = {
    "leduslācis": "Antarktīda",
    "zilonis": "Āfrika",
    "panda": "Ķīna",
    "grizlilācis": "Ziemeļamerika",
    "gepards": "Āfrika",
    "lauva": "Āfrika",
    "ķengurs": "Austrālija",
    "ronis": "Okeāns",
    "koala": "Austrālija",
    "pingvīns": "Antarktīda"
}


# Izvada sākotnējo ziņojumu par spēli
print("Šajā spēlē jūsu uzdevums ir mēģināt atminēt sākumā nejauši izvēlēto elementu (dzīvnieku/putnu). Ja tu neuzmini izvēlēto elementu uzreiz, tad tiks uzdots jautājums, kur tas ir izplatīts.")
print("Jautājuma atbildēšanai būs doti divi mēģinājumi.")
print("Ja tu gribi pārtraukt spēlēt spēli, tad raksti 'stop'.")

chosen_key = None

def main():
    global chosen_key  # Norāda, ka tiek izmantots ārpus funkcijas definētais chosen_key
    # Galvenā programma
    while True:  # Nebeidzami atkārtojiet, kamēr lietotājs neizlemj nesākt spēli
        start_game = input("Vai tu gribi sākt? (Jā vai Nē): ").lower()  # Lietotāja jautājums par spēles sākumu
        if start_game != "nē":  # Pārbauda, vai lietotājs nav izvēlējies nesākt spēli
            break  # Izkļūst no cikla, ja lietotājs izvēlas sākt spēli
    print("Sākotnējais jautājums:")  # Izvada paziņojumu par sākotnējo jautājumu
    play_game()  # Izsaukums spēles funkcijai

def main1():
    global chosen_key  # Norāda, ka tiek izmantots ārpus funkcijas definētais chosen_key
    # Galvenā programma
    while True:  # Nebeidzami atkārtojiet, kamēr lietotājs neizlemj nesākt spēli
        start_game = input("Vai tu gribi turpināt? (Jā vai Nē): ").lower()  # Lietotāja jautājums par spēles sākumu
        if start_game != "nē":  # Pārbauda, vai lietotājs nav izvēlējies nesākt spēli
            break  # Izkļūst no cikla, ja lietotājs izvēlas sākt spēli
    print("Sākotnējais jautājums:")  # Izvada paziņojumu par sākotnējo jautājumu
    play_game()  # Izsaukums spēles funkcijai

def play_game(repeat=False, repeat_attempt=False):
    global chosen_key  # Norāda, ka tiek izmantots ārpus funkcijas definētais chosen_key

    if chosen_key is None:  # Ja chosen_key vēl nav izvēlēts, izvēlas nejaušu elementu
        chosen_key = random.choice(list(main_dictionary.keys()))
    initial_chosen_key = chosen_key  # Saglabā sākotnējo chosen_key vērtību
    guessed_elements = 0  

    while True:  # Nebeidzami atkārtojiet, kamēr spēlētājs izvēlas pārtraukt spēli
        print(f"Kas tas ir? {main_dictionary[initial_chosen_key]["galvena_vertiba"]}")  # Izvada galveno vērtību izvēlētajam elementam
        user_guess = input("Pamēģini atminēt: ").lower()  # Lietotāja ievade, mēģinot atminēt elementu

        if user_guess == "stop":  # Pārbauda, vai lietotājs nav izvēlējies pārtraukt spēli
            break  # Izkļūst no cikla, ja lietotājs izvēlas pārtraukt spēli
        if user_guess == initial_chosen_key:  # Pārbauda, vai lietotāja ievade sakrīt ar izvēlēto elementu
            print("Pareizi! Jūs atminējāt.")  # Izvada paziņojumu, ka lietotājs ir pareizi atminējis elementu
            guessed_elements += 1 # Palielina pareizi atminēto elementu skaitu par 1
            chosen_key = None
            break  # Izkļūst no cikla, ja lietotājs ir pareizi atminējis elementu
        
                 # Norāda, ka spēle turpināsies vai nav beigusies
        else:  # Ja lietotāja ievade neatbilst izvēlētajam elementam
            if repeat_attempt:  # Ja funkcija tiek atkārtoti izsaukta un tika sniegta nepareiza atbilde
                print(f"Tu nevari atminēt. Pareizā atbilde ir: {initial_chosen_key}")
                print("Turpinām spēlēt spēli!╰(*°▽°*)╯")
                main1()
                
            else:  # Ja funkcija netiek atkārtoti izsaukta vai netika sniegta nepareiza atbilde
                print("Diemžēl nepareizi. Tagad tev būs jāatbild uz jautājumu.")
                

                main2(initial_chosen_key)

    # Pārbaude, vai lietotājs vēlas turpināt vai pārtraukt spēli
    next_game = input("Vai turpināt? (Jā vai Nē): ").lower()  # Lietotāja ievade par spēles turpināšanu
    if next_game != "jā":  # Pārbauda, vai lietotājs nav izvēlējies turpināt spēli
        print(f"Tu atminēji {guessed_elements} elementus.")  # Izvada paziņojumu par pareizi atminēto elementu skaitu
        restart_game = input("Vai tu gribi sākt spēli no jauna? (Jā vai Nē): ").lower()  # Lietotāja ievade par spēles sākumu no jauna
        if restart_game == "jā":  # Pārbauda, vai lietotājs ir izvēlējies sākt spēli no jauna
            chosen_key = None
            main()  # Izsaukums spēles funkcijai
        else:  # Ja lietotājs nav izvēlējies sākt spēli no jauna
            print("Paldies par spēlēšanu!(●'◡'●)") # Izvada paziņojumu par pateicību par spēlēšanu
            
    else:  
        play_game() 
            
    
    
def main2(initial_chosen_key, repeat_attempt=False):
    # Papildus funkcija, kas uzdod jautājumu par elementa dzīves vietu
    attempts = 0  # Inicializē mainīgo, kas glabās mēģinājumu skaitu
    subkeys = dictionary1.keys()
    for key, value in dictionary1.items():
          # Iegūst apakšvērtību, kas saistīta ar atslēgu "subkey1"
        if key == initial_chosen_key:
           subkey = value



    if subkeys:  # Pārbauda, vai ir atrastas apakšvērtības
        while attempts < 2:  # Nebeidzami atkārtojiet, kamēr mēģinājumu skaits ir mazāks par 2
            guess = input(f"Kur viņš dzīvo? {main_dictionary[initial_chosen_key][subkey]['subkey1']} (Vai 'stop', lai pārtrauktu): ").lower()  # Lietotāja ievade par elementa dzīves vietu
            
            if guess == "stop":  # Pārbauda, vai lietotājs nav izvēlējies pārtraukt spēli
                break  # Izkļūst no cikla, ja lietotājs izvēlas pārtraukt spēli

            if guess == subkey.lower():  # Pārbauda, vai lietotāja ievade sakrīt ar izvēlēto elementu
                print("Pareizi!")
                print("Tagad tev būs vieglāk atminēt izvēlēto elementu.(❁´◡`❁)")# Izvada paziņojumu, ka lietotājs ir atminējis pareizi
                play_game(repeat_attempt=True)
                return  # Beidz funkcijas izpildi
            
                
            else:  # Ja lietotāja ievade neatbilst izvēlētajam elementam
                attempts += 1  # Palielina mēģinājumu skaitu par 1
                print("Nepareizi. Tev atlikuši", 2 - attempts, "mēģinājumi.")  # Izvada paziņojumu par atlikušo mēģinājumu skaitu

                if attempts == 1:  # Pārbauda, vai ir pirmais mēģinājums
                    #print(main_dictionary[chosen_key].get(f"subkey2", ""))  # Izvada apakšvērtību, kas saistīta ar atslēgu "subkey2"
                    print(main_dictionary[initial_chosen_key][subkey][f"subkey{attempts + 1}"])
            # Ja mēģinājumu skaits ir sasniedzis 2
        if attempts == 2:
            print("Tomēr nesanāca(┬┬﹏┬┬), tagad tu mēģināsi minēt sākumā izvēlēto elementu.(✿◡‿◡)")   
           
    play_game(repeat_attempt=True)

    
if __name__ == "__main__":
    main()  # Izsaukums galvenajai funkcijai