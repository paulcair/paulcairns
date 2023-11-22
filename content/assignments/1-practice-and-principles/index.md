+++
title = "01 - Principles and Practices"
image = "PowerStoveDiagram.JPG"
weight = 30

[typeScript] 
typeScript1 = "Assignment 1: Principles and Practices" 
typeScript2 = "See the work I did for this weeks' assignment"

[headline]
headline = "Objective: to plan and sketch a final project idea and build a personal site describing it."
+++

The assignment for the first week of the FabAcademy is based on the assessments for ([Principles and Practices](http://fabacademy.org/2021/docs/assessment/principles_and_practices.html)). The tasks for this assignment include:

-  Plan and sketch a potential final project
-  Build a personal site describing you and your final project.

We will be evaluated on whether we:

- 	Read the Fab Charter
-   Sketched your final project idea/s
- 	Described what it will do and who will use it 
- 	Signed and uploaded the Student Agreement


## Final Project Assessment Criteria

Before beginning, it is important to understand what is expected of a final project. To do this it is important to look at the assessment criteria. The final project will be assessed based on the following learning outcomes:

-	Create your own integrated design
- 	Demonstrate 2D & 3D modelling capabilities applied to your own    designs
-	Select and apply appropriate additive and subtractive techniques
-	Demonstrate competence in design, fabrication and programming of your own fabbed microcontroller PCB, including an input & output device

Further details regarding the assesment of the Final project ([can be found here](http://fabacademy.org/2021/docs/assessment/project_requirements.html))

# Project Idea: A stove that generates electricity

The idea for the final project that I would like to construct throughout the FabAcademy is a powered stove similar to the PowerStove or the BioLite. 

PowerStove

{{<image PowerStove.jpg>}}


BioLite

{{<image BioLite.jpg>}}

## Background

55% of rural Africans across the continent have little to no access to electricity as they try to cook in the nighttime . The PowerStove will immediately provide electricity for these families with a short payback period compared to buying a conventional stove and small solar panel.  PowerStove provides a solution much more elegant than cooking without the benefit of creating electricity and/or the complexity of having to buy additional equipment 

The PowerStove is designed for user’s with no training required. Simply fill the stove with biopellets, ignite them and you’re ready to cook while powering your electronic device through the USB port.

This two in one solution replaces your conventional charcoal stove and comes with the added bonus of electric power. No need to buy a solar panel, this stove powers while you cook. A similar stove has proven successful in Nigeria with little to know user training necessary.

## What it Does

The Powered Stove converts heat from cooking into Direct Current Electricity using Thermoelectric Generators (TEGs). TEGs are thermo-electric component that take advante of the ([Seebeck Effect](https://en.wikipedia.org/wiki/Thermoelectric_effect))

The electricity is used to power a USB terminal suitable to charge a phone. Critical to the Seebeck effect is the requirement of a thermal differential. As such, a heat sink and fan are required on one side of the TEG to appropriately cool the TEG. The photo below provides a general overview of what it does.

{{<image PowerStoveOverview.JPG>}}

## How it works

There are three main sub assemblies involved in this stove. 

1 - The combustion chamber assembly

2 - The electric generator assembly

3 - The electronics assembly

Below is a concept illustrating the sub-assemblies. Using this as reference we will provide detailed sketches of each aspect in each sub-section below.

{{<image PowerStoveDiagram.JPG>}}

### Combustion chamber assembly

The combustion chamber assembly mates with the electric generator assembly. The sketch below illustrates the concept for how it will be constructed for this prototype

{{<image PowerStoveSketch1.JPG>}}

{{<image PowerStoveSketch2.JPG>}}

### Electric generator assembly

The eletric generator assembly contains the TEGs and the cooling fan and heat sink. The sketch below illustrates the concept:

{{<image PowerStoveSketch3.JPG>}}

{{<image PowerStoveWiringDiagram.JPG>}}

### Electronic Assembly

The last assembly includes the wiring for the LiOn batteries, charge controller, voltage regulator and USB port. The first spiral used soldered wires and the next spiral will use a circuit board and will add temperature sensing as well as an LED bar graph.

{{<image PowerStoveWiringDiagram2.JPG>}}

{{<image ElectronicsFirstSpiral.jpg>}}

# Project Plan

In this section I will discuss the history of my work on this concept,the over all development goals (spiral developments), and the objectives for this course.

## History of my work on this concept

To date, I have built a very first prototype of this concept as a way to learn the main subassemblies and where to improve the development. Below is a video of the first prototype:

{{<youtube-time zda-0qfy3CU>}}

In the first prototype, I proved the concept of using heat to produce suffient amount of electricity to power the fan and cool the back side of the TEGs. 

## Overall development goals (spiral developments)

In the first prototype, I experimented with using the TEGs to produce sufficient electricity to power a 5V fan. Although successful. There were many improvements that could be made. Below is a list of the improvements to be made. 

### Improvements required

- 	Construction of a better heat sink
- 	Construction of a better TEG
- 	Creating a circuit board rather than using wires and solder
- 	Adding a temperature sensor with an LED bargraph similar to the 	 biolite
-	Creating a more aesthetic housing for the electronics assembly

### Spirals

Using the improvements listed above, below is an idea of the spirals that could be followed over the evolution of the project

1 - Completed prototype as is (TEGs that power fan)

2 - Addition of a heat sensor and led bargraph

3 - Refinement of heatsink assembly

4 - Custom build of the TEG

## Objectives for this course

### Primary objective

In this course I intent to focus in on Spiral Step 2: Addition of a heatsensor and led bargraph. The objective is to build a heat sensor system and not focus so much on the combustion chamber. The BioLite video below illustrates the objective

{{<youtube-time YF6dR8fSGvU>}}

### Secondary objectives

The secondary objetives would be to successfully attach this electronics sensing assembly to an existing stove configuration and power it using off the shelf TEGs and heat sinks.

### Moonshot

The moonshot would be to make my own custom heat sink and TEGs
