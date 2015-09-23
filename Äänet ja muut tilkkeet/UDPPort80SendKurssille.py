#!/usr/bin/env python3.3
import socket

Message = 'Saapas'


def getExternalIP():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('google.com', 80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip

ServerIP = getExternalIP()
nelossukka = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
nelossukka.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
nelossukka.bind((ServerIP, 8144))

z = 0
while z < 200:
    nelossukka.sendto(bytes(Message,'utf-8'),(ServerIP,80))
    z += 1
