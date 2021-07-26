import network
from time import sleep


def conectar():
    
        wifi = network.WLAN(network.STA_IF)
        ssid = "red2"
        contraseña = "12345678"
        ssid2 = "BATMAN"
        contraseña2 = "BATSH8213gh"
        
        
        if not wifi.isconnected():
            wifi.active(True)
            wifi.connect(ssid2, contraseña2)
            while not wifi.isconnected():
                print(".", end="")
                sleep(1)
            
        print(wifi.ifconfig())
