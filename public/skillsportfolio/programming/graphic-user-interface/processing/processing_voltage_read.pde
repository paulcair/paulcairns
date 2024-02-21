import processing.serial.*; //imports  the serial library
Serial myPort;             // initialize a variable named "myPort"
float Voltage;              // declare variable to receive the Voltage value
float x;                    // variable that maps the Voltage to bits

void setup(){

  size(500,400);
  myPort = new Serial (this, "/dev/ttyUSB0", 9600);
  myPort.bufferUntil( '\n' );
}  

void serialEvent (Serial myPort){
  
  Voltage = float(myPort.readStringUntil( '\n'));
  
  x = map(Voltage, 0,20,0,500);
}

void draw() {
  
  
  background(216,255,149);
   
  text("Voltage is:",0,195);
  text(Voltage,65,195);
   
   
  stroke(0);
  fill(255,0,0);
  rect(0, 200, x, 200);
  }
