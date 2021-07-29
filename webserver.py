import network
from time import sleep
import sensor
import socket
import wifi
import urequests
def web():
    """Servidor web para mostrar los datos de los sensores de manera local"""
    wifi.conectar()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 80))
    s.listen(5)
   
    while True:
        
        #Recibir datos del sensor dht11
        temp, hum =sensor.recibir()
        sleep(2)
        
        #Enviar dato del sensor de temperatura a la api de thingspeak
        apiTemp="https://api.thingspeak.com/update?api_key=38YCW8L4OCXQGK6H&field1="
        apiTemp = apiTemp + str(temp)
        r1 = urequests.get(apiTemp)
        print(r1.json())
        
        #Enviar dato del sensor de humedad a la api de thingspeak
        apiHum="https://api.thingspeak.com/update?api_key=ORDLJDO3MN6OX9Q6&field1="
        apiHum = apiHum + str(hum)
        r2 = urequests.get(apiHum)
        print(r2.json())
             
        #guardar la conexión y dirección del dispositivo 
        conn, addr = s.accept()
        print("Nueva conexión desde %s" % str(addr))
    
        request=conn.recv(1024)
        print("")
        print("Solicitud %s" % str(request))

        request = str(request)
        
        #condiciones de temperatura si sobrepasan el rango requerido
        if (temp < 15 or temp > 20):
            t = "Está fuera del rango"
        else:
            t = "Está dentro del rango"
        
        if (hum < 45 or hum > 60):
            h = "Está fuera del rango"
        else:
            h = "Está dentro del rango"
        
        #Pagina web para mostrar los datos de los sensores y thingspeak
        pagina ="""<!DOCTYPE HTML>
                <html>
                <head>
                    <meta charset="utf-8">
                </head>
                  <body style="background-color:#BCDCF1;">
                          
                    <center>
                    <h1>Medición y monitorización </h1>
                    <iframe src="https://thingspeak.com/channels/1456301/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15" height="260" width="460" title="Temperatura"></iframe>
                    <h2 style="color: #6F40A8;">Temperatura es """ + str(temp) +""" </h2>  
                    <h2>"""+t+"""</h2>
                    
                    <br>
                    <iframe src="https://thingspeak.com/channels/1456302/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15" height="260" width="460" title="Humedad"></iframe>
                    <h2 style="color: #6F40A8;">Humedad es """ + str(hum) + """ </h2>
                    <h2>"""+h+"""</h2>
                     </center>
                      </body>
                </html>"""
        #mostramos pagina web y cerramos la pagina web
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(pagina)
        conn.close()
        