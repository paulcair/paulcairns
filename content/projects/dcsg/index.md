+++
title = "High Pressure Oxy-fired Combustion Development"
video = "dcsg.mp4"
weight = 30

[lead]
lead = "HiPrOx DCSG - A method to produce high pressure steam using "

[typeScript] 
typeScript1 = "High Pressure Oxy-fired Direct Contact Steam Generation (HiPrOx/DCSG)" 
typeScript2 = "An efficient method to produce steam for Carbon Capture and Sequestration"

[headline]
headline = "I worked on this project as a Research Mechanical Engineer to start out my carreer. Over the course of 6 years on the project, I saw it from techno-economic feasibility through mechanical completion of the pilot demonstration plant. Below are details about my contributions to the project."
+++

# 1. Background Information

A more detailed video about the project is included below.

{{<youtube-responsive mannAO6f70c>}}



## Aspects of the project

This project was very much a 6 year entire research program, as such there were very many aspects of it that I was involved with. Below is list of them. I will cover each in detail in Section 2.

- Techno-econmic feasibility study
- Process simulations
- Fuel reactivity PTGA bench-scale testing
- Integrated Emissions Control bench-scale testing
- 15 barg pilot plant retrofit and test campaign (OSLI)
- 100 barg pilot plant design and construction (mechanical)
- Theoretical design of 100 MWth HiPrOx power plant

## Confidentiality 

Much about this project was privileged confidential as we were working with a client, therefore I can only share photos and videos that have been made publicly available either on the NRCan Website, Youtube channel, or Scientific Publication. Furthemore, any description of work on the project will aim to exclude design details and will focus more on engineering methodology and processes used.

# 2. My Personal Contributions

## Techno-economic feasibility study

## Process Simulations

## Fuel reactivity PTGA bench-scale testing

## Integrated Emissions Control bench-scale testing

## 15 barg pilot plant retrofit and test campaign (OSLI)

### Updating P&IDs

### HAZOP

### Burner design construction and testing

One of the major objectives of the 15 barg pilot testing campaign was to test various burner configurations using CO2 as moderator and steam as moderator. Furthermore we wanted to test different fuel feed types including slurried solid fuels, liquid fuels, and gas fuel (methane gas). This led to discussion of the various atomization techniques for the different fuels. We settled on two designs to test:

1. A gas-swirl atomizer
2. An external atomizer

The gas-swirl atomizer was the primary choice as it would work very well with both the liquid-gas, and gas-gas feeds. One issue with the gas-swirl atomizer is the pintle is subject to wear from erosion, which becomes an issue when you have a slurried solid fuel as the fuel particles will erode the pintle over time. This is why we chose to explore the external atomizer. Next I will walk through the steps taken to design and construct the burner for this specific test campaign.

Below is an image of the gas-swirl atomizer that was included in a [publication](../../publications/scientific-papers/hiprox/hiprox-publication.pdf) I authored. 

{{<image burner.png>}}

Note that this image excludes specific design details due to confidentiality.

#### 1. Process simulations to determine feed rates

The first step in the process was to perform process simulations using AspenTech HYSYS to determine the required feed rates. 

- We started by defining the thermal energy requirement (1 mmBTU/hr or 293 kWth).
- This set the fuel flow rate based on the heat value of the fuel
- If the fuel was a solid slurry we would look at the slurry viscosity stress-strain curve and determine the water composition based on the pump characteristics, this would set our water flow rate 
- Next we defined the oxygen flow rate based on the desired excess oxygen in the flue gas
- Finally, we added any additional moderator (CO2 or water) to ensure a flame temperature below 2000 C. This would set the moderator flow rate.

Once the feed flow rates were defined we 

#### 2. Momentum balance to determine orifice sizes

The next step in the process was to determine the orifice and channel sizes so that the burner face could be specified and manufactured in our shop. 

Given the feed rates from the step above, we had to select the cross-sectional diameter that would be required to properly impinge (external atomizer), or swirl (gas-swirl atomizer) the fluid to ensure proper atomization. The following steps were taken to perform the momentum balance and size the orifices.

- Determine the momentum differences required for proper atomization based on heuristics and atomizer type. For example, for an externally atomized gas/liquid burner, would be characterized as 2:1 or 1.5:1, etc.
- The diameter of the inner tube would be set based on the flow rate of the fuel, the desired Reynolds number (as close to turbulent flow as possible while remaining laminar, so 3000-3500) and then double checking minimum velocity required to avoid settling in the case of a slurry.  This would set the momentum of the fuel jet (inner). 
- Given the diamater of the fuel tube, the momentum can be calculated using (where rho is  density of fuel, D is diamater of pipe, and W is mass flow rate)









### Internals design construction and testing

### Pilot plant operation

### Pilot plant maintenance and turnover

### Data analysis

### Final Report

## 100 barg pilot plant design and construction (mechanical)

### Process simulation and Design Basis

### Version control and system design

Defining the blocks, systems, numbering, and version control

### P&IDs

### HAZOP

### Line Lists and Equipment Lists

### Unit operations process design

### Equipment design
#### Internals
#### Pressure destaging
#### Bottom Flange Lift Mechanism
#### Equipment frames


### Purchasing

### Construction and Assembly


## Theoretical design of 100 MWth HiPrOx power plant

### Thermodynamic layout of steam cycle

### Tube-side heat exchanger sizing

### Mechanical layout of steam cycle

### Cad models