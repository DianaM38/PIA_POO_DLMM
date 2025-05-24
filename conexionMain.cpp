//liberria para controlar mis servomotores
#include <Servo.h>
//defino una clase para representar un servo

class ServoControl{
  //no quiero que se modifique el pin entonces por eso lo puse en private
  private:
  //pin al que va conectado mi servo
  byte pin;
  Servo servo;

  public:
  //mi constructor
  ServoControl(){

  }
  //mi metodo para vincular los servos con los pines
  void attach(byte p){
    pin=p;
    //conecto mi servo a ese pin 
    servo.attach(pin);
  }
  //mi metodo para mover el servo al angulo 
  void mover(int angulo){
    servo.write(angulo);
  }
};

//creo un arreglo de objetos de mi clase para mis servos
ServoControl servos[13];
//declaro las variables para recibir los datos

// va a almacenar los caracteres que se envien por el puerto serial (tipo,pin,valor\n)
String datoString="";
// cuando encuentre \n cabia a true por que entonces ya termine de recibir mi instrruccion**
bool datoCompleto =false;

void setup() {
  //inicio la comunicacion serial entre el puerto y mi laptop 
  //transimito a velocidad de 9600 bautios (bits/segundo)
  Serial.begin(9600);

  //muñeca 
  servos[1].attach(12);
  //
  servos[2].attach(2);
  servos[3].attach(3);
  servos[4].attach(4);
  servos[5].attach(5);
  servos[6].attach(6);
  //
  servos[7].attach(7);
  servos[8].attach(8);
  servos[9].attach(9);
  servos[10].attach(10);
  servos[11].attach(11);

  //IMPORTANTE, debo de reservar memoria para la cadena que mande de python 
  datoString.reserve(30);
}

void loop() {
   eventoSerial();
   if(datoCompleto){
    //divido la cadena por las comas y guardo su posicion 
    int c1= datoString.indexOf(',');
    int c2= datoString.indexOf(',',c1+1);
    //confirmo que si mande las comas (si es -1 mande mal mi instruccion)
    if(c1!=-1 && c2!=-1){
      String tipo= datoString.substring(0,c1);
      int pinServo= datoString.substring(c1+1,c2).toInt();
      int angulo=datoString.substring(c2+1).toInt();

      //valido que mande un pin valido
      if(pinServo>=1 && pinServo<=12){
        servos[pinServo].mover(angulo);
      }

    }

    
    //limpio la cadena para mi siguiente instruccion
    datoString="";
    datoCompleto=false;
  }

}

void eventoSerial(){
  //mientras haya datos disponibles en mi puerto voy a leer 
  // los caracteres que haya hasta el salto de linea
  while(Serial.available()){
    //convierto el caracter que read me devuelva a char y lo agrego a mi instruccion
    char enCar= (char)Serial.read();
    datoString+=enCar;
    if(enCar=='\n'){
      datoCompleto=true;
    }
  }
}