import customtkinter as ctk
import serial 
import time
#pruebas para la interfaz grafica y conexion a un servo
#hago que mi clase Ventana herede la clase customtkinter.CTk por que es la ventana principal en customtkinter
class Ventana(ctk.CTk):
    def click_boton(self):
        print("se apreto el boton")
        
    def angulo(self,valor):
        anguloDado = str(int(valor))
        if conexionSerial and conexionSerial.is_open:
            conexionSerial.write((anguloDado+'\n').encode())
            print(anguloDado)


    #constructor
    def __init__(self, fg_color =None):
        #llamo al constructor de la clase padre ctk.CTk
        super().__init__(fg_color =fg_color)
        
        self.geometry("800x900")
        self.title("MANO ROBOTICA CONTROLADOR")

        # prueba de botones
        self.button1 =ctk.CTkButton(self, command=self.click_boton, text="Presionar",fg_color="#111429")
        self.button1.grid(row=0,column=0,padx=20,pady=10)
       

        self.slider = ctk.CTkSlider(self, from_=0, to=180, orientation= "horizontal", command=self.angulo)
        self.slider.grid(row=2,column=2,padx=20,pady=10)

    

#puerto serial en mi arduino
puerto = 'com10'
baudRate=9600

try:
    conexionSerial= serial.Serial(puerto,baudRate)
    time.sleep(2)
    print('se conecto al arduino')
except:
    print('no se conecto')


def cerrar():
    app.destroy()
    if conexionSerial and conexionSerial.is_open:
        conexionSerial.close()


app = Ventana(fg_color="#172858")
app.protocol("WM_DELETE_WINDOW",cerrar)
app.mainloop()


""" 
#notas para mi
#self. referencia a la instancia actual de la clase

paletas de colores
AZUL
.color1 {color: #140f07;}
.color2 {color: #111429;}
.color3 {color: #172858;}
.color4 {color: #2c3c89;}
.color5 {color: #4b54bd;}

ROJO
.color1 {color: #810040;}
.color2 {color: #8f002d;}
.color3 {color: #9a3c34;}
.color4 {color: #a06c52;}
.color5 {color: #9f8468;}

.color1 {color: #5c182e;}
.color2 {color: #7b2035;}
.color3 {color: #a73044;}
.color4 {color: #e64754;}
.color5 {color: #ff7875;}

VERDE
.color1 {color: #000005;}
.color2 {color: #051a22;}
.color3 {color: #214449;}
.color4 {color: #3f797d;}
.color5 {color: #55a09e;}
"""
