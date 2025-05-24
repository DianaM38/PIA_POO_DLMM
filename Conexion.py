import serial
import time 
#https://pyserial.readthedocs.io/en/latest/shortintro.html
#https://pyserial.readthedocs.io/en/latest/pyserial_api.html 
'''
voy a crear una clase para manejar la conexxion y rl rnvio de mis cadenas a mi arduino 
por el puerto y con esta clase voy a hacer una prueba con unittest en el archivo Utest 
para comprobar la conexion
le estoy enviando un string (M,1,60\n   <-algo asi) a mi arduino en forma de bytes usnado.encode(), 
el codigo de arduino esta en c++ y decidi solo pasar instrucciones atraves del puerto para evitar confuciones y porque
se me hizo mas comodo
'''
class ConexionSerial:
    def __init__(self, puerto='COM10',baudRate=9600):
        #voy a tratar de abirir el puerto
        try:
            #guardo mi objeto de conexion serial (serial.Serial) en self.serial
            self.serial= serial.Serial(puerto,baudRate,timeout=1)
            #espero a que se reinicie el arduino
            time.sleep(2)
            print('arduino conectado')
            #si ocurre un error cancelo todo(None no es valido y entonces no tuve una conexion exitosa)
        except serial.SerialException:
            print(f'no se conecto al arduino')
            self.serial=None
    
    #ahora hare el metodo para enviar lo que quiero que hagan los servo al arduino
    def enviar(self,tipo,pin_servo, angulo):
        #si todo esta en orden (mi conexion fue exitosa) y el puerto esta abierto se va a enviar mi string gracias a .write
        if self.serial and self.serial.is_open:
            instruccion= f'{tipo},{pin_servo},{angulo}\n'
            print(instruccion.strip())
            #envio el comando como bytes
            self.serial.write(instruccion.encode())

    #este es el metodo para cerrar mi conexion con el arduino
    def cerrar(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
            print('se cerro la conexion con el arduino')





