/*notas
Servo.h no es una clase en sí misma, sino un archivo de cabecera 
que define la clase Servo en el contexto de Arduino para controlar servomotores
la clase Servo se utiliza luego para crear objetos que representen 
los servomotores que se controlan. 
*/
#include <Servo.h>
// instancio un objeto de la clase servo
Servo servo1;
////declaro las variables para recibir los datos
// va a almacenar los caracteres que se envien por el puerto serial
String datoString="";
// cuando encuentre \n cabia a true por que entonces ya termine de recibir todos los datos
bool datoCompleto =false;
// convierto datoString a entero y este sera el angulo
int dato=0;


void setup(){

  //inicio la comunicacion serial entre el puerto y mi laptop 
  //transimito a velocidad de 9600 bautios (bits/segundo)
  Serial.begin(9600);
  //mi servo esta en el pin 3 de mi arduino, los 11 servos iran de 2 a 12
  servo1.attach(3);
}

void loop(){
  //veo si hay datos disponibles
  eventoSerial();
  if(datoCompleto){
    dato= datoString.toInt();
    if(dato>=0&& dato<=180){
      servo1.write(dato);
    }
    //reinicio las variables para el siguiete dato
    datoString="";
    datoCompleto=false;
  }
}

void eventoSerial(){
  //mientras haya datos disponibles en mi puerto voy a leer 
  // los caracteres que haya hasta el salto de linea
  while(Serial.available()){
    char enCar= (char)Serial.read();
    if(enCar=='\n'){
      datoCompleto=true;

    }else{
      //si no hay salto de linea, agrego lo que tenga datoString
      datoString+=enCar;
      
    }
  }

}

