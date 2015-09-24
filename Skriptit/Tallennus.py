#Otetaan käyttöön kirjasto bge, joka sisältää työkalut maailman 
#muutteluun pelimoottorin ollessa käynnissä
import bge

#cont-nimiseen muuttujaan säilötään nykyinen controlleri, eli H:hon kytketty
#Python-ohjain, johon valittiin Tallennus.py
cont = bge.logic.getCurrentController()

#sce-nimiseen muuttujaan säilötään koko pelin sisältävä maailma
sce = bge.logic.getCurrentScene()

#own-nimiseen muuttujaan säilötään cont-muuttujan omistaja, eli peliobjekti, jonka
#sisällä se on, tässä tapauksessa kuutiomme
own = cont.owner

#Tarkistetaan, onko tallennus jo käynnissä. Jos ei ole, toteutetaan sisennetty osa
#(Game Propertyihin pääsee käsiksi tyylillä   palikka["ominaisuus"]   , kuten alla)
if own["Saving"] == False:
    
    #Muutetaan Saving-booleanin arvo todeksi
    own["Saving"] = True
    
    #Objektit, jotka jätetään välistä, kun luodaan tallennustiedostoa
    välKap = ["__default__cam__","Camera","MenuKeskus"]
    
    #Luodaan tyhjä lista nimeltä peliKappaleet
    peliKappaleet = []    
    
    #Käydään kaikki sce-maailman peliobjektit läpi
    for kappale in sce.objects:
        
        #Jos kappale ei ole vältettävien kappaleiden listalla
        if str(kappale) not in välKap:
            
            #Kappaleen nimi lisätään listaan ja tehdään rivinvaihto
            peliKappaleet.append(str(kappale)+"\n")
            #Kappaleen paikka lisätään listaan ja tehdään rivinvaihto
            peliKappaleet.append(str(kappale.worldPosition)+"\n")
            #Kappaleen kääntökulmatiedot lisätään listaan ja tehdään rivinvaihto
            peliKappaleet.append((str(kappale.worldOrientation.to_euler()).replace("\n",""))+"\n")
    
    #Avataan uusi tiedosto kirjoitusoikeuksilla
    tTiedosto = open("TallennusTiedosto.txt","w")
    #Kirjoitetaan listan sisältö tiedostoon
    tTiedosto.writelines(peliKappaleet)
    #Suljetaan tiedosto, että vältytään hankaluuksilta
    tTiedosto.close()