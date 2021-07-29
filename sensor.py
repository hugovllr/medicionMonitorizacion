import dht
from time import sleep
from machine import Pin

def recibir():
    """Recibir los datos del sensor y almacenarlos en varriables"""
    #Asignando pin del sensor dht11
    sensor = dht.DHT11(Pin(14))
    
    #método de medición
    sensor.measure()
    #asignando el valor de la temperatura a la variable "temp"
    temp = sensor.temperature()
    #asignando el valor de la humedad a la variable "hum"
    hum = sensor.humidity() 
    return temp, hum