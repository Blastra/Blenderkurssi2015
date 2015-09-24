import bge

#Palikan ohjaimen kautta pitää lähteä liikkeelle
cont = bge.logic.getCurrentController()

#Tällä päästään kiinni palikan itsensä ominaisuuksiin
own = cont.owner

#Materiaalit ovat lista, oletusarvoisesti ensimmäinen muoto on se, joka
#näkyy
materiaali = own.meshes[0]

#Materiaaleista ensimmäinen on oletusarvoisesti se, joka näkyy
materiaaliIndeksi = 0

#Jotta kaikki pisteeseen kytketyt vektorit kulkevat mukana,
#napataan yhden vektorin XYZ -koordinaatit
kohdeVektori = materiaali.getVertex(materiaaliIndeksi, 3).getXYZ()

#Käydään kaikki vektorien indeksit läpi
for vektoriIndeksi in range(materiaali.getVertexArrayLength(materiaaliIndeksi)):
    
    #Otetaan vektori, joka on vuorossa
    vektori = materiaali.getVertex(materiaaliIndeksi, vektoriIndeksi)
    
    #Jos vektori johtaa aikaisemmin valitun vektorin kanssa samaan
    #pisteeseen, nostetaan sitä ylöspäin ja päivitetään fysiikat
    if vektori.getXYZ() == kohdeVektori:
        vektori.z += 0.2
        own.reinstancePhysicsMesh()