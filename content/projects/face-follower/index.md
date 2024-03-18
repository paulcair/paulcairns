+++
title = "Face Follower - An AI and hardware fusion"
video = "demo.mp4"
weight = 30

[lead]
lead = "The Face Follower - A 3D printed hardware mechanism to find and point to faces"

[typeScript] 
typeScript1 = "The Face Follower" 
typeScript2 = "A 3D printed hardware using Arduino controller and python based face-detection AI."

[headline]
headline = "The Face Follower is a little project that combines AI face-detection python programming, with 3D printed hardware and Arduino based micro-controller with servo motion control. "
+++

{{<video demo.mp4>}}

# Background and Inspiration

I came across this video on social media and got inspired to see if I could replicate it by dusting off an old face detection app I made that uses OpenCV.

The video of the project that inspired this is below:

{{<youtube-responsive f2TUxoaKIsA>}}

As part of the challenge, I wanted to avoid looking at any documentation that the project included and just try to design the project from scratch using only the video as guidance and to see how I might be able to improve upon the hardware.

Once I completed the project, I finally opened the github repository for his project to see our difference in approach. In the end the overall approach was very similar, one major difference, which I think made his solution more elegant, was that he uses the python program to control the Arduino directly, whereas I have programmed the Arduino seperately and am sending the coordinates to the arduino from my laptop over the USB Serial, which results in a minor delay in the reactivity of the servo, compared to his project.

Either way, it was a really fun project and experience. I will share the methodology and details of my approach to the problem below.

## Python AI face detection App

Here is a video of the python program in action:

{{<video coord.mp4 >}}

Below is the python code:

```
import cv2
import os
import time
import serial
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#Get the path of the current script
script_path=os.path.abspath(__file__)

# Get the directory containing the script
script_directory = os.path.dirname(script_path)

# Concatenate the script directory with the face XML file name
cascade_face_path = os.path.join(script_directory, 'haarcascade_frontalface_default.xml')

# Concatenate the script directory with the Smile XML file name
cascade_smile_path = os.path.join(script_directory, 'haarcascade_smile.xml')

# Open a connection to the serial port (adjust the port and baud rate as needed)
# ser = serial.Serial('/dev/ttyACM0', 115200)

# Create an App class called FaceDetect
class FaceDetect(App):

    #Build a window named self and set the columns
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5 }
    
        # Add widgets to the window

        # Create a lable widget with a greeting
        self.greeting = Label(
                        text = "Welcome to Paul's Facial Recognition App",
                        font_size = 32,
                        color = '#00FFCE'
                        )
        self.window.add_widget(self.greeting)

        # Create a label widget with a prompt
        self.prompt = Label(
                      text = "Please select the functionality",
                      font_size = 16
                      )
        self.window.add_widget(self.prompt)

        # Create a button widget with face detector only
        self.face = Button(
                      text = "Track face only",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = '#00FFCE'
                      )
        self.face.bind(on_press = self.track_face)
        self.window.add_widget(self.face)

        # Create a button widget with face and smile detector
        self.face_smile = Button(
                      text = "Track face and smile",
                      size_hint = (1,0.5),
                      bold = True,
                      background_color = '#00FFCE'
                      )
        self.face_smile.bind(on_press = self.track_face_smile)
        self.window.add_widget(self.face_smile)
     
        return self.window
        
    #Function that launches face tracker on button press
    def track_face(self, instance):

        # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
        trained_face_data = cv2.CascadeClassifier(cascade_face_path)

        # Choose an image to detect faces in
        #img = cv2.imread('paulface.jpg')

        # Capture video from webcam
        webcam = cv2.VideoCapture(0)

        while True:
            #Read the current frame
            succesful_frame_read, frame = webcam.read()

            # Convert the image to greyscale
            img_greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            face_coordinates = trained_face_data.detectMultiScale(img_greyscale)

            # Initialize empty variables to find the bigest face 
            biggest_face_width = 0
            biggest_face = None
            # last_biggest_face = (320,240,0,0)

            # Find the biggest face in the face_coordinates array
            for (x,y,w,h) in face_coordinates:
                if w > biggest_face_width:
                    biggest_face_width = w
                    biggest_face = (x,y,w,h)
            
                cv2.rectangle(frame,(x, y),(x+w, y+h),(0,255,0), 3)

            # If a face is detected, send face coordinates to Arduino via serial port
            if biggest_face is not None:
                # last_biggest_face = biggest_face
                x, y, w, h = biggest_face

                cv2.rectangle(frame,(x, y),(x+w, y+h),(0,0, 255), 3)

                coordinates_string = f"{x},{y},{w},{h}\n"
                # ser.write(coordinates_string.encode('utf-8'))
                print(coordinates_string)
            # else:
            #     x, y, w, h = last_biggest_face
            #     none_detected = f"{x},{y},{w},{h}\n"
            #     ser.write(none_detected.encode('utf-8'))
            #     print(none_detected)

            #Flip the frame horizontally
            mirrored_frame = cv2.flip(frame, 1)      

            #Add Label with prompt to press ESC to exit
            cv2.putText(mirrored_frame, 'PRESS ESC TO EXIT PROGRAM', (40 ,40), fontScale = 2, fontFace = cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

            # Display the image with boxes around the detected faces
            
            cv2.imshow('Clever Programmer Face Detector Grey', mirrored_frame)
            key = cv2.waitKey(1)

            #Exit the program if Q key is pressed
            if key == 27:
                break
            
        
        #Realease the webcam
        webcam.release()
        cv2.destroyAllWindows()
 
    # Function that launches face and smile tracker on button press
    def track_face_smile(self, instance):

        # Load some pre-trained data on face frontals and smiles from opencv (haar cascade algorithm)
        trained_face_data = cv2.CascadeClassifier(cascade_face_path)
        trained_smile_data = cv2.CascadeClassifier(cascade_smile_path)

        # Capture video from webcam
        webcam = cv2.VideoCapture(0)

        while True:
            #Read the current frame
            succesful_frame_read, frame = webcam.read()

            # Convert the image to greyscale
            img_greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces
            face_coordinates = trained_face_data.detectMultiScale(img_greyscale, minNeighbors = 10)

            # Create rectangles around the detected faces and create a different color box around each one
            for (x,y,w,h) in face_coordinates:

                #Draw a rectangle around the face
                cv2.rectangle(frame,(x, y),(x+w, y+h),(0,255,0), 3)

                # Send face coordinates to Arduino via serial port
                coordinates_string = f"{x},{y},{w},{h}\n"
                ser.write(coordinates_string.encode('utf-8'))

                # Create image the size of each face box
                the_face = frame[y:y+h, x:x+w]

                #Change facebox subset to greuscale
                face_greyscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

                # Search for smiles within each face box
                smiles = trained_smile_data.detectMultiScale(face_greyscale, scaleFactor = 1.3, minNeighbors = 12)
                
                # Run smile detection within each of the faces
                for (a,b,c,d) in smiles:
                    
                    #Draw a rectangle around each detected smile within the face
                    cv2.rectangle(the_face, (a, b), (a+c, b+d),(0,0,255),3)

                #Label this face as smiling
                if len(smiles) > 0:
                    cv2.putText(frame, 'SMILING', (x ,y+h+40), fontScale = 2, fontFace = cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

            #Add Label with prompt to press ESC to exit
            cv2.putText(frame, 'PRESS ESC TO EXIT PROGRAM', (40 ,40), fontScale = 2, fontFace = cv2.FONT_HERSHEY_PLAIN, color=(255, 255, 255))

            # Display the image with boxes around the detected faces
            cv2.imshow('Clever Programmer Face and Smile Detector', frame)
            key = cv2.waitKey(1)

            
            #Exit the program if Q key is pressed
            if key == 27:
                break
            

        #Release the webcam
        webcam.release()
        cv2.destroyAllWindows()
         
# Run the App called FaceDetect   
if __name__ == "__main__":
    FaceDetect().run()
```

## Hardware Design

I designed the hardware for the face-follower using Solidworks. I cover details of the design on a seperate solidworks page. You can find it [here](../../skillsportfolio/computer-aided-design/solidworks/)

### CAD

I have included some of the Solidworks images and videos below:

{{<image face-follower-assembly.PNG>}}

{{<video face-follower-assembly.mp4>}}

### 3D printing

I 3D printed the parts using a Prusa 3D printer with PLA. I chose draft print settings. Unfortunately I didn't take any photos of the printing process. But I do have a photo of the end result.



## Ardiuino Program

Below is the Arduino program. Note that I took a few different approaches, and have some of the other approaches commented out in the code.

```
#include <Servo.h>

// y Servo can go from 0 to 60 degrees
// X Servo can go from 0 to 180 degrees with forward being at 90 degrees althought it might be better to go from 90 +- 45 (45 to 135) 

int xPrevious;
int yPrevious;
int wPrevious;
int hPrevious;
int counter = 0;
int counts = 7;


const float smoothingFactor = 0.1;
float smoothedAngleX = 90.0;       
float smoothedAngleY = 0.0;  

Servo xServo;
Servo yServo;

void setup() {
  
  Serial.begin(115200);
  xServo.attach(8);
  yServo.attach(9);
  xServo.write(90);
  yServo.write(0);
}

void loop() {

  //// Code to test the servos and their positions. Uncomment this code and comment all of the code below "Servo Testing" to run the servo test program
  // for(int i=3; i<=9; i++){
  //   int j = i*15; // for x go at increments of 15 degrees from 45 to 135 degrees
  //   int k = (i-3)*10; // for y go at increments of 10 degrees 
  //   Serial.println(j);
  //   xServo.write(j);
  //   yServo.write(k);
  //   delay(1000);
  // }
  // Serial.println("Servo Testing")
  
  // If the Serial is available, read it
  if(Serial.available()>0){
    String coordinates = Serial.readStringUntil('\n');

    // Parse the coordinates printed on the serial into integers
    int x,y,w,h;
    sscanf(coordinates.c_str(), "%d,%d,%d,%d", &x,&y,&w,&h);
    
    // If we are returned a strange value, set x, y, w, or h to what they were previously
    if(x>640){
      x = xPrevious;
    }else{
      xPrevious = x;
    }   

    if(y>640){
      y = yPrevious;
    }else{
      yPrevious = y;
    } 

    if(w>640){
      w = wPrevious;
    }else{
      wPrevious = w;
    }  

    if(h>640){
      h = hPrevious;
    }else{
      hPrevious = h;
    }  

    // Find the center of the box
    float xCenter = (x+(w/2)); // Account for the fact that xPosition zero is at center of screen
    float yCenter = y+(h/2);

  
    // Method 1: Take the image and convert it to cm and calculate an angle based on the geometry

    // Convert the center value of the box into a distance in cm knowing that the window frame height is 480 px and at a distance of 1m from the camera this corelates to 75cm in y and 100 cm wide
    // float xPosition = (xCenter/640)*100;
    // float yPosition = (yCenter/480)*75;

    // // Convert the x and y positions into radians
    // float xAngleRadians = atan2(xPosition, 100);
    // float yAngleRadians = atan2(yPosition, 100);

    // // Convert the x and y radians to degrees subtract from 135 and 60 degrees which are motor positions to aim at (0,0)
    // int xDegrees = 135-degrees(xAngleRadians);
    // int yDegrees = 60-degrees(yAngleRadians);//Add 90 degrees because of the way the servo arm is set up (need to correct this)
 
    // xServo.write(xDegrees);
    // yServo.write(yDegrees);
    

    // Method 2 (simpler method): Convert the x and y position coordinates into a % of the range in degrees (135 to 45 for x) and (60 to 0) for y 
    
    int xDegrees = 135-(xCenter/640)*90;
    int yDegrees = 60-(yCenter/480)*60;

    // Round to the nearest 10 degrees
    int xDegreesRounded = round(xDegrees/5.0)*5;
    int yDegreesRounded = round(yDegrees/5.0)*5;

    // Smooth out the motion
    // smoothedAngleX = smoothingFactor * xDegrees + (1 - smoothingFactor) * smoothedAngleX;
    // smoothedAngleY = smoothingFactor * yDegrees + (1 - smoothingFactor) * smoothedAngleY;
    if(counter == counts){
    xServo.write(xDegreesRounded);
    yServo.write(yDegreesRounded);

    }

    counter++;
    if(counter == counts+1){
      counter = 0;
    }
  } 
      
}
```

## Links

- [github repository for python and arduino code](https://github.com/paulcair/face-detector)
- [CAD Files Zip folder](cad.zip)
- [Gcode Files Zip folder](gcode.zip)