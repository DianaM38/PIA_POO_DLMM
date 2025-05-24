#importo las librerias que hice y custontkinter para mi gui
import customtkinter as ctk
from controles import*
from Conexion import*

#hago que mi clase principal herede la clase customtkinter.CTk por que es la ventana principal 
#  y asi dice en la  doc si loquiero hacer con clases
class ControlesMano(ctk.CTk):
    
    def __init__(self, fg_color=None):
        #llamo al constructor de la clase padre ctk.CTk
        super().__init__(fg_color=fg_color)
        
        #esto es para el tamaño y titulo de mi ventana
        self.geometry("800x900")
        self.title("CONTROLES DE MI MANNO ROBOTICA")

        #para manejar mi comunicacion serial creo una instancia de mi clase conexionSerial
        self.serial=ConexionSerial()

        #esta lista tendra todos los controles de mis servomotores (sliders)
        self.controles=[]

        # etiquetas para identificar mejor que controlan grado de libertad estoy controlando
        self.etiquetaH=ctk.CTkLabel(self,text="\nSERVOS DIRECCION\n HORIZONTAL")
        self.etiquetaH.grid(row=0,column=0,padx=5,pady=5)
        #vertical
        self.etiquetaV=ctk.CTkLabel(self,text="\nSERVOS DIRECCION\n VERTICAL")
        self.etiquetaV.grid(row=0,column=1,padx=5,pady=5)


        #hago los controles para mis servos verticales y horizontales, 
        # tipo=h,(mi grado de libertad, me va a ayudar como identificador), 
        # paso desde que pin se va asociar cada dedos, (desde el 7(osea 7,8,9,10,11)) 
        # y los grados que se pueden mover mis servos y la columna en mi gui en el que van a estar
        self.crear_dedos('H',['meñique','anular','corazon','indice','pulgar'],7,0,30,0)
        self.crear_dedos('V',['meñique','anular','corazon','indice','pulgar'],2,0,180,1)
        #creo el control para mi muñeca y botones para mis movimientos preguardados
        self.crear_muñeca()
        self.crear_botones()
    

    
        # metodo que envia la instruccion al arduino cuando se mueve un slider
    def enviar_comando(self,tipo,pinServo,angulo):
        #llamo al metodo enviar de la clase controles y le paso los parametros
        self.serial.enviar(tipo,pinServo,angulo)  


        #creo los controles de mis dedos y los añado a mi lista de controles
    def crear_dedos(self,tipo,nombres,pinDeInicio,minV,maxV,columna):
        for i,nombre in enumerate(nombres):
             # cada control ocupa 2 filas por su etiqueta y slider 
            fila = i*2+1 
            s=ServoControles(self,nombre,i+pinDeInicio,tipo,minV,maxV,self.enviar_comando,fila,columna)
            self.controles.append(s)

    # creo el control de mi muñeca
    def crear_muñeca(self):
        #el pin va a ser el 1 pero lo conecte al 12 en el arduino por que los pines 1 y 0 son pines reservados
        # el tipo es M como identificador y va dede 10 hasta 60 grados
        s = ServoControles(self,['muñeca'],1,"M",10,60,self.enviar_comando,6,2) 
        self.controles.append(s)
    
    # aqui estan las rutinas para abrir,cerrar,amor y paz, y hacer el simobolo de yeah
    def abrir_mano(self):
        for s in self.controles:
            if s.tipo=='V': 
                s.colocar(0)
                self.enviar_comando(s.tipo,s.pinServo,0)
            elif s.tipo=='H': 
                s.colocar(0)
                self.enviar_comando(s.tipo,s.pinServo,0)
            elif s.tipo=='M':
                s.colocar(10)
                self.enviar_comando(s.tipo,s.pinServo,10)
    
    def amor_paz(self):
        self.cerrar_mano()
        for s in self.controles:
            if s.tipo =='M': 
                s.colocar(60)
                self.enviar_comando(s.tipo,s.pinServo,60)
            elif s.pinServo ==5: 
                s.colocar(0)
                self.enviar_comando(s.tipo,s.pinServo,0)
            elif s.pinServo ==4:
                s.colocar(0)
                self.enviar_comando(s.tipo,s.pinServo,0)
        
    
    def yeah(self):
        self.abrir_mano()
        for s in self.controles:
            if s.tipo=='M':
                s.colocar(60)
                self.enviar_comando(s.tipo,s.pinServo,60)
            elif s.pinServo ==4:  
                s.colocar(180)
                self.enviar_comando(s.tipo,s.pinServo,180)
            elif s.pinServo ==3: 
                s.colocar(180)
                self.enviar_comando(s.tipo,s.pinServo,180)


    # Método para cerrar todos los dedos y muñeca a su posición "cerrada"
    def cerrar_mano(self):
        for s in self.controles:
            if s.tipo=='M':
                s.colocar(60)
                self.enviar_comando(s.tipo,s.pinServo,60)       
            elif s.tipo=='H':
                s.colocar(0)
                self.enviar_comando(s.tipo,s.pinServo,0)
            elif s.tipo=='V': 
                s.colocar(180)
                self.enviar_comando(s.tipo,s.pinServo,180)



    def crear_botones(self):
        ctk.CTkButton(self,text="Abrir Mano",command=self.abrir_mano,fg_color="#4b54bd").grid(row=1,column=2,padx=10,pady=5,sticky="ew")
        ctk.CTkButton(self,text="Cerrar Mano",command=self.cerrar_mano,fg_color="#4b54bd").grid(row=2,column=2,padx=10,pady=5,sticky="ew")
        ctk.CTkButton(self,text="Amor y paz",command=self.amor_paz,fg_color="#4b54bd").grid(row=3,column=2,padx=10,pady=5,sticky="ew")
        ctk.CTkButton(self,text="yeah",command=self.yeah,fg_color="#4b54bd").grid(row=4,column=2,padx=10,pady=5,sticky="ew")


    #metodo para cerrar mi puerto y gui 
    def cerrar(self):
        self.serial.cerrar()
        self.destroy()



if  __name__=='__main__':
    #creo una instancia de mi clase principal 
    app = ControlesMano(fg_color="#172858")
    #vinculo el metodo cerrar de mi clase principal para cerrar la conxion al ´puerto 
    # y cerrar la ventana
    app.protocol("WM_DELETE_WINDOW",app.cerrar)
    #esto se tiene que poner siempre por que inicia el bucle prinpcipal de mi gui y solo se pone uno profe
    app.mainloop()


