#define IN1 10
#define IN2 11
#define IN3 12
#define IN4 13
#define EN_A 9
#define EN_B 3
#define LOOK_LEFT 0
#define LOOK_FRONT 90
#define LOOK_RIGHT 180
#define SERVO_PIN 2
#define TRIGGER_PIN  5
#define ECHO_PIN     6
#define MAX_DISTANCE 150
#define TURN_DELAY 600
#define MOTOR_SPEED 200
#define THRESHOLD 5

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
  Serial.begin(9600);
}
void loop() {
  delay(50);
  left = 0;
  right = 0;
  front = 0;
  analogWrite(EN_A, 255);
  analogWrite(EN_B, 180);
  Serial.println(sonar.ping_cm());
  if(sonar.ping_cm()<=THRESHOLD)
    pos = sonarResponse();
  
  switch(pos) {
    case 0:
      moveFwd();
      // delay(200);
      break;
    case 1:
      moveLeft();
      // delay(TURN_DELAY);
      stop();
      break;
    case 2:
      moveRight();
      // delay(TURN_DELAY);
      stop();
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
  analogWrite(EN_A, 180);
  analogWrite(EN_B, 100);
  digitalWrite (IN1, HIGH);
  digitalWrite (IN2, LOW);
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, HIGH);
  delay(TURN_DELAY);
}

void moveRight() {
  analogWrite(EN_A, 100);
  analogWrite(EN_B, 255);
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, HIGH);
  digitalWrite (IN3, HIGH);
  digitalWrite (IN4, LOW);  
  delay(TURN_DELAY);
}

void stop() {
  digitalWrite (IN1, LOW);
  digitalWrite (IN2, LOW);
  digitalWrite (IN3, LOW);
  digitalWrite (IN4, LOW);                                                                                                                                                                                                                                                                        
}

int sonarResponse() {
    stop();
    // if (sonar.ping_cm()<=THRESHOLD&& sonar.ping_cm()!=0) 
    // {
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
    // }
    if (front >= THRESHOLD)
      return 0;
    else if (left >= THRESHOLD)
      return 1;
    else if (right >= THRESHOLD)
      return 2;
    else
      return 3;
  // return val;
}
