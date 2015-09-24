import socket
#Select on moduuli vastaanottavien sockettien tiedon poimimiseen
import select
import bge

gD = bge.logic.globalDict

vastaanOttaja = gD["VastaanottoTerminaali"]

#Varastoidaan ready-nimiseen muuttujaan, mitä vastaanOttaja on kerännyt 5 millisekunnin
#aikana
ready = select.select([vastaanOttaja], [], [], 0.005)

#Jos ready-muuttujasta löytyy ensimmäinen listan muuttuja
if ready[0]:
    
    #Varastoidaan data-muuttujaan, mitä tulevaa postia vastaanOttaja -socketista löytyy
    #lukemalla 1024 merkkiä
    data = vastaanOttaja.recvfrom(1024)
    print(data)