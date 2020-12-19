#include <Wire.h>

int devices[] = {4,5,1,1,6};
void setup() {
  Wire.begin(3);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
  Serial.begin(9600);           // start serial for output
  Serial.println("lets start...");
  int devicesCount = sizeof(devices);
  for(int i =0; i<devicesCount; i++) {
    pinMode(devices[i], OUTPUT);
  }
}

void loop() {
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
}
