import network
from time import sleep
import sensor
import socket

def web():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    redes = wifi.scan()

    for red in redes:
        print(red[0].decode())

    ssid = "red2"
    contraseña = "12345678"

    wifi.connect(ssid, contraseña)
    while not wifi.isconnected():
        print(".", end="")
        sleep(1)

    print(wifi.ifconfig())



    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)

    temp, hum =sensor.recibir()

   
    while True:
    
        conn, addr = s.accept()
        print("Got connection from %s" % str(addr))
    
   
        request=conn.recv(1024)
        print("")
        print("Content %s" % str(request))

   
        request = str(request)
    
    
        response ="""<!DOCTYPE HTML>
                <html>
                <head>
                </head>
                <body>
                    <h2>SERVIDOR WEB </h2>
                    <p>Temperatura es """ + str(temp) + """ </p>
                    <p>Humedad es """ + str(hum) + """ </p>
                </body>
                </html>"""
    
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
    
   
        conn.close()
    
    