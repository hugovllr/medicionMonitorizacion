import network
from time import sleep



def conectar():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    redes = wifi.scan()



    for red in redes:
        print(red[0].decode())

    ssid = "BATMAN"
    contraseña = "BATSH8213gh"

    wifi.connect(ssid, contraseña)
    while not wifi.isconnected():
        print(".", end="")
        sleep(1)

    print(wifi.ifconfig())
    
