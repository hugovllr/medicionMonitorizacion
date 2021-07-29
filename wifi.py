import network
from time import sleep


def conectar():
        """Conectar a la red wifi"""
        wifi = network.WLAN(network.STA_IF)
        ssid = "red2"
        contraseña = "12345678"
        ssid2 = "BATMAN"
        contraseña2 = "BATSH8213gh"
        
      #Si no hay conexión, activar wifi y conectar con el nombre de la red y su contraseña
        if not wifi.isconnected():
            wifi.active(True)
            wifi.connect(ssid, contraseña)
            while not wifi.isconnected():
                print(".", end="")
                sleep(1)
        print("Conexión establecida con " + ssid)    
        print(wifi.ifconfig())
