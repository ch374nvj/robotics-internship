int in1 = 7;
int in2 = 8;
int in3 = 9;
int in4 = 10;
int ena = 3;
int enb = 5;
char val;
 void setup() {
  pinMode(ena, OUTPUT);
  pinMode(enb, OUTPUT);
  pinMode (in1, OUTPUT);  
  pinMode (in2, OUTPUT);
  pinMode (in3, OUTPUT);
  pinMode (in4, OUTPUT);
}
void loop() {
  while (Serial.available()>0) {
    val=Serial.read();
    Serial.println(val);
}
  analogWrite(ena, 255);
  analogWrite(enb, 255);
  if (val == 'F') {
  digitalWrite (in1, HIGH);
  digitalWrite (in2, LOW);
  digitalWrite (in3, HIGH);
  digitalWrite (in4, LOW);  
  // delay(5000);
  }
  else if (val =='B') {
  digitalWrite (in1, LOW);
  digitalWrite (in2, HIGH);
  digitalWrite (in3, LOW);
  digitalWrite (in4, HIGH);  
  // delay(5000);
  }
  else if (val == 'L') {
  digitalWrite (in1, HIGH);
  digitalWrite (in2, LOW);
  digitalWrite (in3, LOW);
  digitalWrite (in4, HIGH);  
  // delay(5000);
  }
  else if(val == 'R') {
  digitalWrite (in1, LOW);
  digitalWrite (in2, HIGH);
  digitalWrite (in3, HIGH);
  digitalWrite (in4, LOW);  
  // delay(5000);
  }
else {
  digitalWrite (in1, LOW);
  digitalWrite (in2, LOW);
  digitalWrite (in3, LOW);
  digitalWrite (in4, LOW);  
 }
}