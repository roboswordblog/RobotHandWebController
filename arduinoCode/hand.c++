#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

bool downOrUp = false;
void setup() {
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);
 // servo5.attach(10);
  
  servo3.write(-90);
  servo2.write(-90);
  servo5.write(150);
  servo1.write(-45);
  servo4.write(45);
  
}
void lunge() {
  servo3.write(90);
  servo2.write(90);
}
void down(int d) {
  downOrUp = true;
  if (d <= 0) {
    d = 60;
  }
  servo3.write(-90);
  servo2.write(60);
}

void moveAngleEntire(int angle) { servo5.write(angle); }

void twistClaw(int angle) { servo4.write(angle); }
void claw() {}

void loop() {
  delay(2000);

}
