import dht
from time import sleep
from machine import Pin

def recibir():
    sensor = dht.DHT11(Pin(14)) #Asignando pin del sensor dht11

    sensor.measure() #método de medición
    temp = sensor.temperature() #asignando el valor de la temperatura a la variable "temp"
    hum = sensor.humidity() #asignando el valor de la humedad a la variable "hum"
    return temp, hum