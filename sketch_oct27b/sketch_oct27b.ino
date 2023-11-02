int l = 0;
int r = 0;
int f = 0;
int b = 0;

void setup () {
  // put your setup code here, to run once:
Serial.begin (9600);
pinMode(10,INPUT);
pinMode(11,INPUT);
pinMode(12,INPUT);
pinMode(13,INPUT);

pinMode(2,OUTPUT);
pinMode(3,OUTPUT);
pinMode(4,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
l = digitalRead(12);
r = digitalRead(13);
f = digitalRead(10);
b = digitalRead(11);
if(f) {
  Serial.println("Forward");
  digitalWrite(2,HIGH);
  delay(2000);
  digitalWrite(2,LOW);
}
else if(l) {
  Serial.println("Left");
  digitalWrite(3,HIGH);
  delay(2000);
  digitalWrite(3,LOW);
}
else if(r) {
  Serial.println("Right");
  digitalWrite(4,HIGH);
  delay(2000);
  digitalWrite(4,LOW);
}
else if(b) {
  Serial.println("Backward");
  digitalWrite(3,HIGH);
  digitalWrite(4,HIGH);
  delay(2000);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
}

delay(500);
}