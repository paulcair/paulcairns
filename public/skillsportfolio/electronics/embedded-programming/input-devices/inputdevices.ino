#include <Robojax_AllegroACS_Current_Sensor.h>
#include <DallasTemperature.h>
#include <OneWire.h>

//DECLARING CONSTANT VARIABLES AND PINS
const float Vratio = 5.128;   //ratio of voltage reduction based on experiment
const float VCC = 5.04;       // value of VCC of the board based on measurements
const int CurrentPin = 0;    // pin where current sensor is conncected
const int VoltPin = 1;        // pin where voltage sensor is connected
const int TempPin = 3;       // pin where temperature sensor is connected
const int MODEL = 0;          // value of the current sensor model, see below

// SET UP THE CURRENT SENSOR
  //'robojax' function uses format robojax(MODEL, INPUT-VARIABLE) where the model I am using is model ACS712ELECT-5B 
  //which corresponds to a value of 0 according to https://robojax.com/learn/arduino/?vid=robojax_Alegro_ACS712_curren_sensor
    Robojax_AllegroACS_Current_Sensor robojax(MODEL,CurrentPin);

//SET UP THE TEMPERATURE SENSOR
  //set the pin (TempPin) that the OneWire will communicate through
    OneWire oneWire(TempPin);
  //pass oneWire reference to Dallas Temperature
    DallasTemperature sensors(&oneWire);

void setup() {

  //Start serial monitor
  Serial.begin(9600);

  //Start sensors library for temperature sensor
  sensors.begin(); 

  //Set pin modes
  pinMode(CurrentPin,INPUT);
  pinMode(VoltPin, INPUT);
  pinMode(TempPin, INPUT);

}//end of void setup()

void loop() {

//GET AND PRINT CURRENT
  Serial.print("Current = ");
  Serial.print(robojax.getCurrent(),3); //print the current to 3 decimal places
  Serial.print(" A    ");

//GET AND PRINT VOLTAGE
  //calculate voltage and convert from bit reading to voltage value in volts
  float Voltage = VCC*analogRead(VoltPin)*Vratio/1023; 
  
  Serial.print("Voltage = ");
  Serial.print(Voltage);
  Serial.print(" V    ");


//GET AND PRINT TEMPERATURE
  float tempC = sensors.getTempCByIndex(0);
  
  if(tempC != DEVICE_DISCONNECTED_C)
  {
    Serial.print("Temperature = ");
    Serial.print(tempC);
    Serial.println(" degC   ");
  }
  else
  {
    Serial.println("Temperature = Could not read data");
  }//end of if/else statement

 delay(1500);
 
}//end of void loop()
