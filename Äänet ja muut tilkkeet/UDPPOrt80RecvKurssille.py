#!/usr/bin/env python3.3
import socket
import select

def getExternalIP():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('google.com', 80))
    ip = sock.getsockname()[0]
    sock.close()
    return ip

ServerIP = getExternalIP()
kolmossukka = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
kolmossukka.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
kolmossukka.bind((ServerIP, 80))

h = 0
while 1:
    kolmossukka = kolmossukka
    kolmossukka.setblocking(0)
    ready = select.select([kolmossukka], [], [], 0.005)
    # TAKE NOTICE: These actions must be generalised and individualized to
    # work on all player objects.

    if ready[0]:            
        data = kolmossukka.recvfrom(1024)
        print(data)
    h += 1
