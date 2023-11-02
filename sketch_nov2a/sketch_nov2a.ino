#define IN1 10
#define IN2 11
#define IN3 12
#define IN4 13
#define EN_A 8
#define EN_B 9
#define LOOK_LEFT 0
#define LOOK_FRONT 90
#define LOOK_RIGHT 180
#define SERVO_PIN 2
#define TRIGGER_PIN  12 
#define ECHO_PIN     11 
#define MAX_DISTANCE 150
#define TURN_DELAY 2000


#include<Servo.h>
#include<NewPing.h>
Servo myservo;
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);


int left = 0;
int right = 0;
int front = 0;
int pos = 0;
int dist = 0;
int val;
void setup() {
  pinMode(EN_A, OUTPUT);
  pinMode(EN_B, OUTPUT);
  pinMode(IN1, OUTPUT);  
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  myservo.attach(SERVO_PIN);
}
void loop() {
  delay(50);
  analogWrite(EN_A, 255);
  analogWrite(EN_B, 255);
  
  pos = sonarResponse();
  
  switch(pos) {
    case 0:
      moveFwd();
      delay(200);
      break;
    case 1:
      moveLeft();
      delay(TURN_DELAY);
      break;
    case 2:
      moveRight();
      delay(TURN_DELAY);
      break;
    default:
      stop();
  }
}

void moveFwd(){
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);
}

void moveLeft() {
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);
}

void moveRight() {
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);  
}

void stop() {
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);                                                                                                                                                                                                                                                                        
}

int sonarResponse() {
    if (sonar.ping_cm()<=10 && sonar.ping_cm()!=0) 
    {
      myservo.write(LOOK_LEFT);
      left = sonar.ping_cm();
      delay(700);
      myservo.write(LOOK_FRONT);
      delay(100);
      front = sonar.ping_cm();
      delay(700);
      myservo.write(LOOK_RIGHT);
      delay(100);
      right = sonar.ping_cm();
      delay(700);
      myservo.write(LOOK_FRONT);
      
      Serial.println("Left: ");
      Serial.print(left);
      Serial.println("Front: ");
      Serial.print(front);
      Serial.println("right: ");
      Serial.print(right);
    }
    if (front >= 10)
      return 0;
    else if (left >= 10)
      return 1;
    else if (right >= 10)
      return 2;
    else
      return 3;
  // return val;
}
