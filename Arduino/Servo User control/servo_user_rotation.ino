/*
    Team: Top-Gun
*/

#include <Servo.h>
Servo servo1;
int pos = 0;
void setup() {
  // put your setup code here, to run once:
Serial.begin (9600);

servo1.attach(9);
}

void loop() {
  // put your main code here, to run repeatedly
Serial.println("Enter pos:");
while(Serial.available() == 0);
pos = Serial.readString().toInt();
delay(1000);
// Serial.println(pos);
if (pos<=180 && pos>=0)
  servo1.write(pos);
else
  Serial.println("Error");
}
