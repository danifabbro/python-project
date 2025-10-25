print("Benvenuto nell'isola surreale!")
print("La tua missione e' sopravvivere.")
munizioni = 3
left_right = input('Ti sei risvegliato in un bosco fitto e buio, \n'
                   'il battito del cuore accellera\n'
                   ' per la paura, correndo ti imbatti in un bivio dove vai\n: digita "Destra" o "sinistra" \n').lower()

if left_right == "destra":
    swim_wait = input("Sei sulla riva di un fiume: Nuoti o aspetti? \n").lower()
    if swim_wait == "aspetto":
        cannibale = input(' Ti viene incontro un uomo che ti rincorre velocemente\n '
                          'con aria buia e lugubre, hai 3 colpi in canna per sparargli\n'
                          'cosa fai?: digita "ricarico" o "non ricarico" \n').lower()
        if cannibale == "ricarico":
            munizioni += 3
            munizioni_rimaste = munizioni - 5
            ucciso = input(f'Hai ricaricato la pistola hai usato 5 colpi\n, '
                           f'preso in testa Hai {munizioni_rimaste} pallottole\n. '
                           f'Sei sopravvissuto! Prendi il telefono del cannibale\n '
                           f'ma non c\'è campo, ti dirigi fino a 3 porte, quale scegli?\n '
                           f'la "1","2" o "3"? \n').lower()
            if ucciso == "1":
                print('La porta che hai scelto è \n'
                      'finta e ha attivato un meccanismo\n'
                      ' che ti scaglia addosso delle frecce!\n '
                      'Morto come uno spiedino!\n')
            elif ucciso == "2":
                print('La porta che hai scelto è corretta,\n'
                      ' il telefono prende e chiami la \n'
                      'sicurezza!')
            elif ucciso == "3":
                print("La porta è sbagliata, all\'interno\n "
                      "della stanza c'è un orso che ti\n "
                      "sbrana, morto e spolpato!\n")
            else:
                print("Hai scelto una porta inesistente, Game over")
        else:
            print('Hai usato tutti e 3 i colpi senza\n '
                  'successo, piatto succulento per il\n '
                  'cannibale sei morto sbranato!\n')
    else:
        print('Sei stato sbranato vivo da un\n '
              'coccodrillo. Sei morto e hai\n'
              ' riempito la sua panza.\n ')
else:
    print('Sei caduto in un dirupo rotolando\n '
          'senza sosta, sbatti la testa e muori.\n '
          ' Game over')