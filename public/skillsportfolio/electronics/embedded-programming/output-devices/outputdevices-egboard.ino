#include <Robojax_AllegroACS_Current_Sensor.h>
#include <DallasTemperature.h>
#include <OneWire.h>
#include <TM1637Display.h>



//DECLARING CONSTANT VARIABLES AND PINS
const float Vratio = 5.128;   //ratio of voltage reduction based on experiment
const float VCC = 5.04;       // value of VCC of the board based on measurements
const int CurrentPin = A0;    // pin where current sensor is conncected
//const int VoltPin = 3;        // pin where voltage sensor is connected
const int TempPin = 3;       // pin where temperature sensor is connected
const int MODEL = 0;          // value of the current sensor model, see below
//const int CLKI = 3;          // clock for current (I) readout LED display 
//const int DIOI = 4;          // DIO for current (I) readout LED display)
const int CLKV = 0;          // clock for voltage (V) readout LED display
const int DIOV = 1;          // DIO for voltage (V) readout LED display 
const int LEDPIN = 7;
const int NUMPIXELS = 8;

// SET UP THE CURRENT SENSOR
  //'robojax' function uses format robojax(MODEL, INPUT-VARIABLE) where the model I am using is model ACS712ELECT-5B 
  //which corresponds to a value of 0 according to https://robojax.com/learn/arduino/?vid=robojax_Alegro_ACS712_curren_sensor
    Robojax_AllegroACS_Current_Sensor robojax(MODEL,CurrentPin);

//SET UP THE TEMPERATURE SENSOR
  //set the pin (TempPin) that the OneWire will communicate through
    OneWire oneWire(TempPin);
  //pass oneWire reference to Dallas Temperature
    DallasTemperature sensors(&oneWire);

//SET UP LED DISPLAYS
 //   TM1637Display displayI = TM1637Display(CLKI, DIOI);
    TM1637Display displayV = TM1637Display(CLKV, DIOV);

//SET UP LED BAR GRAPH
  


void setup() {

  //Start serial monitor
  Serial.begin(9600);

  //Start sensors library for temperature sensor
  sensors.begin(); 

  //Clear LED voltage and current displays
  displayV.clear();
 // displayI.clear();


  //Setup LED bar graph


 
  //Set pin modes
  pinMode(CurrentPin,INPUT);
//  pinMode(VoltPin, INPUT);
  pinMode(TempPin, INPUT);
   
}//end of void setup()

void loop() {

//GET AND PRINT CURRENT
  float Current = robojax.getCurrent();

  Serial.print("Current = ");
  Serial.print(Current,3); //print the current to 3 decimal places
  Serial.print(" A    ");

//GET AND PRINT VOLTAGE
  //calculate voltage and convert from bit reading to voltage value in volts
 // float Voltage = VCC*analogRead(VoltPin)*Vratio/1023; 
  
  Serial.print("Voltage = ");
 // Serial.print(Voltage);
  Serial.print(" V    ");


//GET AND PRINT TEMPERATURE
  sensors.requestTemperatures();
  
  float tempC = sensors.getTempCByIndex(0);
  
    Serial.print("Temperature = ");
    Serial.print(tempC);
    Serial.print(" degC   ");

//PRINT VOLTAGE AND CURRENT ON LED DISPLAYS
//  int voltdisplay = Voltage*100;
  displayV.setBrightness(5); 
  displayV.showNumberDecEx(voltdisplay, 0b01000000, false, 4, 0);// Prints voltage on LED

  int currdisplay = Current *10000;
//  displayI.setBrightness(5);
//  displayI.showNumberDecEx(currdisplay, 0b01000000, false, 4, 1);// Prints voltage on LED
  
//DISPLAY TEMPERATURE ON LED BARGRAPH
  
  int led = 0;
  led = map(tempC, 20, 125, 0, 7);
  Serial.print("LED is :  ");
  Serial.println(led);


 delay(500);

 
}//end of void loop()
