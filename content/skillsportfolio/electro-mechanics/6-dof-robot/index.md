+++
title = "6 Degree of Freedom Robot Arm"
image = "leArm.png"
weight = 30

[section]
path = "/6-dof-robot"
subTitle = "6 Degree of Freedom Robot Arm"

[typeScript] 
typeScript1 = "Electro-mechanical design: Showcasing my 6 DOF robot arm design skills" 
typeScript2 = "See the work I did to characterize the motion and control of a 6 DOF robot arm."

[headline]
headline = "Objective: to characterize the motion of and program a 6 DOF robot arm to be used as a pick and place (PnP) machine using computer vision."
+++
             
# Background information                      
The objective of this project was to learn how to program a 6 DOF robot arm to be used as a pick and place (PnP) machine using computer vision. To do this, I used an off the shelf 6DOF robotic arm that I bought on Amazon called, "LeArm". I started by assembling and learning the hardware/mechanics. Next, I had to learn some background information about how to kinematicly define and program the robot arm.

The following sections will go over the specifications of LeArm, and provide background about Denavit-Hartenberg frames and coordinate systems.

## Specifications of LeArm

For this project I used LeArm 6 DOF robot kit as an off the shelf robot arm. It is programmable and controllable. I would like to tie it with a computer vision AI program to recognize little cubes, calculate their coordinates, move to that position to grab the cube, and then place the cube in a little basket.

Below are the details and specifications for LeArm.

ADD DETAILS HERE

## Denavit-Hartenberg Frames and Coordinate Systems

To begin, the first thing is to understand and learn D-H frames and coordinate systems for mechanisms.

Below is text taken from automaticaddison describing D-H coordinate systems and their rules. You can find the full article [here](https://automaticaddison.com/how-to-assign-denavit-hartenberg-frames-to-robotic-arms/). I suggest you read take a look as it is very detailed, and valuable information to know.

>Denavit-Hartenberg (D-H) frames help us to derive the equations that enable us to control a robotic arm. 
>
>The D-H frames of a particular robotic arm can be classified as follows:
>- Global coordinate frame: This coordinate frame can have many names…world frame, base frame, etc. [...]
>- Joint frames: We need a coordinate frame for each joint.
>- End-effector frame: We need a coordinate frame for the end effector of the robot (i.e. the gripper, hand, etc….that piece of the robot that has a direct effect on the world).   

The other important information to know about D-H coordinate frames are the four rules for defining the D-H convention in a mechanical system and kinematic drawing. These rules are important to ensure that a 6 DOF robot is properly defined and easily programmable. Again the following text is taken directly from the [automaticaddison.com](https://automaticaddison.com/how-to-assign-denavit-hartenberg-frames-to-robotic-arms/) article. 

>Here are the four rules that guide the drawing of the D-H coordinate frames:
>
>1. The z-axis is the axis of rotation for a revolute joint. 
>2. The x-axis must be perpendicular to both the current z-axis and the previous z-axis.
>3. The y-axis is determined from the x-axis and z-axis by using the right-hand coordinate system.
>4. The x-axis must intersect the previous z-axis (rule does not apply to frame 0).

Below is an example for how to draw the D-H frames for a 3 linkage mechanism with revolute joints.

{{<image dhcoords.jpg>}}

Next step is to draw and define the D-H frames for LeArm so that we can begin to program and manipulate it.

<!-- Link to guide for how to program the coordinates -->

I followed this guide at the following link: [ulitmate guide to 6DOf robot](https://automaticaddison.com/the-ultimate-guide-to-inverse-kinematics-for-6dof-robot-arms/)

# Programming Workflow

In this section I will go over the workflow that I used to program the robot arm. I will go over the steps I took to define the coordinate frames, and then how to program the robot arm to move to a desired position. After that I will go into the details of the computer vision program that I used to recognize the cubes and calculate their coordinates. Lastly, I will demonstrate how these two programs work together to pick up and place the cubes. All of the code for this project can be found on my [Github](https://github.com/paulcair/picknplace).

The workflow for the entire project can be broken down into the following steps:

1. Define the coordinate frames
2. Program the robot arm to move to a desired position
3. Program the computer vision to recognize the cubes and calculate their coordinates
4. Combine the two programs to pick up and place the cubes

## Step 1: Define the Coordinate Frames

Defining the coordinate frames requires a number of steps, and can be done either analytically or numerically. Although the analytical approach is more complex, I opted to use it over the numerical approach so I could learn more about the mechanics of the robot arm and go through the exercise of defining the coordinate frames myself. At the end of this step I will share some numerical approaches that can be used. To define the coordinate frames analytically, I followed the following steps:

1. Draw the kinematic diagram for LeArm
2. Fill the D-H parameters table
3. Use the D-H parameters to derive the transformation matrices
4. Find the forward transformation matrix
5. Write a python function to calculate the forward transformation matrix

I next drew the kinematic diagram for LeArm.