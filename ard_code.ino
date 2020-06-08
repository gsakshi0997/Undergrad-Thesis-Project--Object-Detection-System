#include <Servo.h>
#include<avr/io.h>
Servo sh,el,grp,base;
int pos_el = 120; // Stores the position (angle) of the servo. Range is [0, 180].
int pos_sh=30;
int pos_grp = 0; // Stores the position (angle) of the servo. Range is [0, 180].
int data;
int count0=0;
int count1=0;
int count2=0;
int count3=0;
void setup()
{
 Serial.begin(9600);
 el.attach(9); // Attaches the servo on pin 9 to the servo object.
 el.write(120);
 sh.attach(10);
 sh.write(30);// Resets the position.
 grp.attach(11);
 grp.write(0);
base.attach(12);
 base.write(0);
 //Serial.end();

}
void loop()
{

 while(Serial.available())
 {
 data = Serial.read();


 // Serial.println("dataaa");
 }
 if(data == '0')
 {
 // Serial.println("dataaa");
 while(count0<1)
 {
 count0++;
 grp.write(150);
 delay(2000);
 prop();
 delay(4000);
 base.write(40);
 delay(2000);
 prop();
 delay(2000);
 base.write(0);
 
 //Serial.end();
 }
 }
 if(data == '1')
 {
 //Serial.println("dataaa");

 while(count1<1)
 {
 count1++;
 grp.write(150);
 delay(2000);
 prop();
 // base.write(40);
 delay(4000);
 base.write(80);
 delay(3000);
 prop();
 delay(4000);
 // base.write(40);
 base.write(0);
 el.write(120);
 sh.write(30);// Resets the position.
 grp.write(0);
 base.write(0);
 //Serial.end();
 }
 }

 if(data == '2')
 {
 while(count2<1)
 {

 count2++;
 grp.write(150);
 delay(2000);
 //Serial.println("dataaa");
 prop();
 delay(4000);
 base.write(120);
 delay(3000);
 prop();
 delay(4000);
 base.write(0);
 //Serial.end();
 }
 }
 if(data == '3')
 {
 while(count3<1)
 {
 count3++;
 grp.write(150);
 delay(2000);
 // Serial.println("dataaa");
 prop();
 delay(4000);
 base.write(160);
 delay(3000);
 prop();
 delay(4000);
 base.write(0);
 //Serial.end();
 }
 }
 //Serial.end();


}
void prop()
{
/* grp.write(120);
 delay(2000);
 grp.write(0);
 delay(1000);*/
 delay(2000);
 el.write(90);
 sh.write(45);
 delay(2000);
 el.write(75);
 sh.write(60);
 delay(2000);
// el.write(60);
// sh.write(75);
 delay(2000);
 grp.write(150);
 delay(2000);
 grp.write(0);
 delay(2000);
 //el.write(75);
// sh.write(60);
 delay(2000);
 el.write(90);
 sh.write(45);
 delay(2000);
 el.write(120);
 sh.write(30);
 delay(4000);

}