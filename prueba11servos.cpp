//codigo de prueba para verificar que se mueven los 11 servomotores
#include <Servo.h>
// creo objetos que representen mis servos
Servo pulgar;
Servo p;
Servo i;  
Servo c;
Servo a;
Servo m;
Servo indice;
Servo corazon;
Servo anular;
Servo menique;
Servo muneca;

void setup() {
  //servos mg90s
  muneca.attach(12);
  p.attach(11);
  i.attach(10);
  c.attach(9);
  a.attach(8);
  m.attach(7);
  //servos mg995
  pulgar.attach(6);
  indice.attach(5);
  corazon.attach(4);
  anular.attach(3);
  menique.attach(2);
}

void loop() {
  expa();
  delay(2000);
  
  //exp1x1();
  //delay(2000);
}

void expa() {
//abrir y cerrar la mano
  menique.write(180);
  anular.write(180);
  corazon.write(180);
  indice.write(180);
  pulgar.write(180);
  muneca.write(180);
  p.write(130);
  i.write(130);
  c.write(130);
  a.write(130);
  m.write(130);
  delay(1500);
  
  menique.write(30);
  anular.write(30);
  corazon.write(30);
  indice.write(30);
  pulgar.write(30);
  muneca.write(30); 

  p.write(45);
  i.write(45);
  c.write(45);
  a.write(45);
  m.write(45);
  delay(1500);

  // Expansion for anular
  /*a.write(90);
  delay(1500);
  //a.write(45);
  delay(1500);

  // Expansion for corazon
  //c.write(90);
  delay(1500);
  c.write(80);
  delay(1500);

  // Expansion for indice
  //i.write(90);
  delay(1500);
 // i.write(45);

 */
}
