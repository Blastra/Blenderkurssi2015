import bge
import socket

gD = bge.logic.globalDict

#Määritellään, mitä haluamme lähettää Internetin läpi
Viesti = 'Saapas'

#Lähetetään viesti kaiken valmistelun jälkeen
gD["HeittoTerminaali"].sendto(bytes(Viesti,'utf-8'),(gD["OmaPuh"],80))
