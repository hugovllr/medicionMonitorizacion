from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import sensor

def proyectar():
# Asignando pines de la pantalla en el ESP32
    i2c = SoftI2C(scl=Pin(22), sda=Pin(21))

    anchoPantalla = 128
    altoPantalla = 64
    oled = ssd1306.SSD1306_I2C(anchoPantalla, altoPantalla, i2c) # Asignando los valores de la resolucion de la pantalla oled

    while True:
        oled.fill(0)
        sleep(1)
        temp, hum =sensor.recibir()
    #encender led si supera humedad
        if hum > 60:
            led = Pin(2, Pin.OUT)
            led.on()
            sleep(0.1)
            led.off()
    # convertir valores en texto
        temp = str(temp) 
        hum = str(hum)
        
    #imprimir en pantalla valores
        oled.text("Temp : " + temp + " C", 20, 8)
        oled.text("Hum  : " + hum + " %", 20, 32)
    
        oled.show()
    