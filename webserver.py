import network
from time import sleep
import sensor
import socket
import wifi

def web():
    
    wifi.conectar()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
   
    while True:
        
        temp, hum =sensor.recibir()
        
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
    
    