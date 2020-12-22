#include <Wire.h>

int devices[] = {11,10,9,3,12,8,7,6,5,4};
void setup() {
  // To fetch i2c address from header
  pinMode(A0, INPUT_PULLUP);
  pinMode(A1, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);
  
  Wire.begin(getSlaveAddress());                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output
  Serial.print("Listening at - ");
  Serial.println(getSlaveAddress());
  int devicesCount = sizeof(devices);
  for(int i =0; i<devicesCount; i++) {
    pinMode(devices[i], OUTPUT);
  }
}

void loop() {
//  delay(100);
}

void receiveEvent(int howMany) {
    int deviceIndex = Wire.read();
    Wire.read();
    int state = Wire.read();
//    Serial.print("dev ");
//    Serial.print(deviceIndex);
//    Serial.print("\tstate ");
//    Serial.println(state);

      if (state) {
        digitalWrite(devices[deviceIndex -1], HIGH);
        }
        else {
          digitalWrite(devices[deviceIndex -1], LOW);
          }
      Serial.println("delayed");
}

int getSlaveAddress() {
  int pa0 = !(digitalRead(A0));
  int pa1 = !(digitalRead(A1));
  int pa2 = !(digitalRead(A2));
  int addr = pa0*1 + pa1*2 + pa2*4;
  return(addr);
}
