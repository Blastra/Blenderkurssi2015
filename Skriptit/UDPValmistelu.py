#Socket-kirjasto on yksi tietokoneiden välisen kommunikoinnin moduuli
import socket
import bge

#Otetaan käyttöön taas Blenderin sisäinen kirjasto, jonne voi tallentaa
#ja josta voi hakea tallennettua tavaraa
gD = bge.logic.globalDict

#Lähetysosa

#Haetaan tietokoneen IP-osoite eli "puhelinnumero" pienellä ohjelmalla
#käyttäen googlen sivuja 
def getExternalIP():
    
    #Luodaan socket-objekti kommunikointia varten ja tallennetaan se nimeen sock
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    #Yhdistetään googlen sivuihin portin 80 kautta.
    sock.connect(('google.com', 80))
    
    #Kerätään sockin "tekninen nimi" talteen nimeen ip
    ip = sock.getsockname()[0]
    
    #Suljetaan sock
    sock.close()
    
    #Tuodaan ip esille sille, joka käytti pientä ohjelmaamme
    return ip

#Hankitaan pienellä ohjelmallamme oma IP-osoitteemme
OmaIP = getExternalIP()

#Luodaan socket-objekti, joka on Internetkäytössä ja lähettää Datagrammeja
lahetysHeitin = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Asetetaan lähetysHeitin-socketin tyyppi SOL_SOCKET ja portti uudelleenkäytettäväksi,
#vaikka se olisikin vielä auki 
lahetysHeitin.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

#Sidotaan socket-objekti porttiin 8144
lahetysHeitin.bind((OmaIP, 8144))

#Varastoidaan oma IP:mme myöhempää käyttöä varten
gD["OmaPuh"] = OmaIP

#Varastoidaan lähetysHeitin, sillä toiset kirjoittamamme skriptit eivät
#muista sen olemassaoloa, jos emme kutsu sitä globalDictin sisältä
gD["HeittoTerminaali"] = lahetysHeitin

#Vastaanotto-osa

#Hankitaan taas oma IP:mme
PuheluIP = getExternalIP()

vastaanOttaja = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
vastaanOttaja.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

#Kaikki muu tehdään samoin, mutta vastaanottava skriptimme kuuntelee porttia 80
vastaanOttaja.bind((PuheluIP, 80))

#Varastoidaan myös vastaanottava socket myöhempää käyttöä varten 
gD["VastaanottoTerminaali"] = vastaanOttaja
