 int x=0;

void setup(){

  size(500,400);
  
}  

void draw() {
  
  
  background(216,255,149);
   
  text("Voltage is:",0,195);
  text(x,65,195);
   
   
  stroke(0);
  fill(255,0,0);
  
    if(x<450){
    rect(0, 200, x, 200);
      x = x+1;
      }
      
     else {
     x=0;
     }
  
  }
