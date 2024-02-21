#include <TM1637Display.h> //Includes the LED display library
#include <Wire.h> //Includes the I2C library
#define SECOND_ADDR 9 //Defines secondary board Address as 9


const int CLKV = 0;          // clock for voltage (V) readout LED display
const int DIOV = 1;          // DIO for voltage (V) readout LED display
const float Vratio = 5.128;   //ratio of voltage reduction based on experiment
const float VCC = 5.04;       // value of VCC of the board based on measurements
int Voltbits;                // Variable to hold bits received from I2C
int LED = 8;                 //Set LED pin to 8
int BR;                      //Declare Blink Rate variable

//SET UP LED DISPLAYS
    TM1637Display display = TM1637Display(CLKV,DIOV);
    
void setup() {
 
  //Start serial monitor
  Serial.begin(9600);
  
  //Initialize I2C communications as secondary
  Wire.begin(SECOND_ADDR);

  //Initialize name of function that will receive from master
  Wire.onReceive(receiveEvent);

 pinMode(LED, OUTPUT);


}

void receiveEvent(){//Defining the function that receives the date from the master

  Voltbits = Wire.read();
  //GET AND PRINT VOLTAGE
  //calculate voltage and convert from bit reading to voltage value in volts
  
  
}

void loop() {


  float Voltage = VCC*Voltbits*Vratio/255; 
  Serial.println(Voltage);
  

  int BR = map(Voltbits, 1, 255, 1000, 10);

   digitalWrite(LED,HIGH);
   delay(BR);
   digitalWrite(LED,LOW);
   delay(BR);
  

}
