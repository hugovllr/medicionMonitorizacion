import pantalla
import webserver

print("Para iniciar digite w para accceder al servidor web, de lo contrario digite p para visualizar los datos en la pantalla Oled ")
dato =input()

while dato != "w" and dato != "p":
    print("Digite la letra correcta")
    dato =input()
    
if dato == "w":
    webserver.web()
elif dato == "p":
    pantalla.proyectar()
    print("Visualizando en pantalla Oled")



