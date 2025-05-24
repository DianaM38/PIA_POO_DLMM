#como ya lo dije en el documento profe, tkinter parece que es de 2010 y por eso opte por customtkinter (mejora a tkinter), pero aprendi cosas de diseño
#https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/
#https://customtkinter.tomschimansky.com/documentation/widgets/slider  voy a usar slider para controlar mis servos
import customtkinter as ctk
'''https://customtkinter.tomschimansky.com/tutorial/grid-system/
espero dejar bien la documentacio
pude haber usado pack() pero me gusto mas grid(), lit es mas facil dividirlo en columanas y filas en mi opinion'''

#hago la clase para controlar mis servos con sliders
class ServoControles:
    def __init__(self, contenedor, nombre,pinServo,tipo,minV,maxV,comando,fila,columna):
        #atributos
        self.contenedor=contenedor
        self.nombre=nombre
        self.pinServo=pinServo
        self.tipo=tipo
        self.comando=comando

        #etiquetas con el nombre de mi servo
        self.etiqueta= ctk.CTkLabel(contenedor,text=nombre)
        #lo alineo a la izquierda
        self.etiqueta.grid(row=fila,column=columna,padx=10,pady=10,sticky='w')

        #mis sliders para controlar los servos, (valor que pueden tomar mis servos)
        self.control= ctk.CTkSlider(contenedor,from_=minV, to=maxV,orientation='horizontal',command=self.cambiar_angulo)
        #hago que la posicion inicial de mis controles esten en 0
        self.control.set(0)
        #ew para que se extienda horizontalmente 
        self.control.grid(row=fila+1,column=columna,padx=10,pady=10,sticky='ew')

    #hago un metdo para  modficar la posicion de mi control manualmente para mis botones en el main
    def colocar(self,angulo):
        self.control.set(angulo)
        

    #mi metodo para mover automaticamente el slider
    def cambiar_angulo(self,angulo):
        self.comando(self.tipo,self.pinServo,int(angulo))
        
        