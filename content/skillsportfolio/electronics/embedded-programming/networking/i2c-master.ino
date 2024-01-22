#include <Wire.h> // Includes the I2C library
#define SECOND_ADDR 9 //defines the address of the secondary board

//DECLARING CONSTANT VARIABLES AND PINS
const float Vratio = 5.128;   //ratio of voltage reduction based on experiment
const float VCC = 5.04;       // value of VCC of the board based on measurements
const int VoltPin = 0;        // pin where voltage sensor is connected
int Voltbits;                  // Name of variable that will be passed to secondary board

void setup() {
  // put your setup code here, to run once:
 //Start serial monitor
  Serial.begin(9600);

  //Initialize I2C communications on Master
  Wire.begin();

  //DefinePins
  pinMode(VoltPin, INPUT);

}

void loop() {

  //Read the voltage from the volt sensor
  int Volts = analogRead(VoltPin);
  
  //Map the voltage to a value that can be sent via I2C
  Voltbits = map(Volts,0,1023,1,255); 

  //Write and charter to the secondary
  Wire.beginTransmission(SECOND_ADDR);
  Wire.write(Voltbits);
  Wire.endTransmission();


  //GET AND PRINT VOLTAGE
  //calculate voltage and convert from bit reading to voltage value in volts
  float Voltage = VCC*Volts*Vratio/1023; 
  
  Serial.print("Voltage = ");
  Serial.println(Voltage);
  Serial.print(" V    ");

  delay(500);
}
