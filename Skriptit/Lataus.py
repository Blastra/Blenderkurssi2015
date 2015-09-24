import bge

#cont-nimiseen muuttujaan säilötään nykyinen controlleri, eli H:hon kytketty
#Python-ohjain, johon valittiin Tallennus.py
cont = bge.logic.getCurrentController()

#sce-nimiseen muuttujaan säilötään koko pelin sisältävä maailma
sce = bge.logic.getCurrentScene()

#own-nimiseen muuttujaan säilötään cont-muuttujan omistaja, eli peliobjekti, jonka
#sisällä se on, tässä tapauksessa MenuKeskus
own = cont.owner

if own["Loading"] == False:
    
    #Muutetaan Loading-booleanin arvo todeksi
    own["Loading"] = True
    
    #Avataan pelin tilannetiedot sisältävä tekstitiedosto lukuoikeuksilla
    latausTiedosto = open("TallennusTiedosto.txt","r")
    
    #Luetaan teksti tiedoston sisältä ja varastoidaan se tekstiKasaan
    tekstiKasa = latausTiedosto.readlines()
    
    #Suljetaan tekstitiedosto
    latausTiedosto.close()
    
    #Luetteloidaan merkit, jotka pitää poistaa, jotta jäljelle
    #jäävät vain numerot ja kappaleiden nimet
    roippeet = [", order='XYZ'","<",">","Euler "," ","x=","y=","z=","Vector","\n"]
    
    #Luodaan tyhjä lista niitä objekteja varten, joihin ei pidä koskea
    säilytettävät = []

    #Lisätään säilytettävien joukkoon peruskamera (Blender kaatuu, jos tämä
    #objekti poistetaan, kun näkymä on sen sisällä.)
    säilytettävät.append(sce.objects["__default__cam__"])

    #Menukeskus pitää sisällään käynnissä olevan skriptin, joten sen 
    #poistaminen todnäk. kaataisi Blenderin
    säilytettävät.append(sce.objects["MenuKeskus"])
    
    #Käydään kaikki kappaleet läpi
    for kappale in sce.objects:
        
        #Jos kappale ei löydy säilytettävien listalta, se poistetaan
        #ladattavan tilanteen tieltä
        if kappale not in säilytettävät:
            kappale.endObject()

    #Luodaan muokatuille kirjainjoukoille lista, joka ottaa niistä kopin
    lopullistenKasa = []

    #Käydään läpi jokainen rivi, mitä tekstitiedostosta on löytynyt
    #ja käytetään rivin nimenä i:tä
    for i in tekstiKasa:
        
        #Kopioidaan lopullinen-muuttujaan i 
        lopullinen = i
        
        #Käydään kaikki roippeet läpi...
        for roipe in roippeet:
            #...ja poistetaan ne kirjainjonosta
            lopullinen = lopullinen.replace(roipe,"")
        
        #Lisätään muunnokset läpikäynyt lopullinen lopullistenKasa -listaan
        lopullistenKasa.append(lopullinen)
    
    #Käydään läpi numerot, joita on yhtä paljon kuin läpi
    #käytäviä kappaleita    
    for indeksi in range(int(len(lopullistenKasa)/3)):
        
        #Paikkatiedot löytyvät aina seuraavalta riviltä
        #Ne tarvitsevat hieman muokkausta ja muuttamisen listaksi pilkkujen kohdalta (split)
        paikkaTiedot = lopullistenKasa[indeksi*3+1].replace("(","").replace(")","").split(",")
        
        #Luodaan koordinaattikasa -niminen lista (toimii myös tyhjennyksenä)
        koordinaattiKasa = []
        
        #Käydään paikkatiedot läpi ja nimetään yhtä läpikäytävää nimellä xyz
        for xyz in paikkaTiedot:
            
            #Lisätään koordinaattiKasan perään liukulukuversio (float, hieman kuin desimaali) 
            #xyz:stä
            koordinaattiKasa.append(float(xyz))
        
        #Siirretään MenuKeskus oikeaan paikkaan luomaan kappaletta
        sce.objects["MenuKeskus"].worldPosition = koordinaattiKasa
        
        #Haetaan kääntötiedot kohdasta indeksi+2 ja tehdään niistä lista
        kääntöTiedot = lopullistenKasa[indeksi*3+2].replace("(","").replace(")","").split(",")
        
        #Luodaan kääntöön tarvittaville luvuille oma lista (toimii myös tyhjennyksenä)
        kääntöKasa = []

        #Käydään kaikki kääntöTiedot -listan jäsenet läpi
        for xyz in kääntöTiedot:
            
            #Lisätään liukuluku kääntöKasa -listaan
            kääntöKasa.append(float(xyz))                
        
        #Käännetään MenuKeskus oikeaan kulmaan avaruudessa    
        sce.objects["MenuKeskus"].worldOrientation = kääntöKasa
        
        #Lisätään MenuKeskus -objektin kohtaan kappale, jonka nimi löytyy
        #lopullistenKasa -listasta kohdalta indeksi kerrottuna kolmella
        sce.addObject(lopullistenKasa[indeksi*3],"MenuKeskus")
    
    #Käännetään lataustoiminto pois päältä, että voidaan ladata uudestaan
    own["Loading"] = False