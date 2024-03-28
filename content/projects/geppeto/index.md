+++
title = "Geppeto the benchtop CNC"
video = "geppeto.mp4"
weight = 30

[lead]
lead = "Geppeto - the benchtop CNC. A 3D linear axis CNC machine machine made for milling wax molds and other small parts"

[typeScript] 
typeScript1 = "Geppeto: The benchtop CNC" 
typeScript2 = "See the work I did to develop a bencthtop CNC."

[headline]
headline = "Objective: to design and build a machine that has a mechanical and electronic component that can be actuated and automated to perform a certain task."
+++

## Overview

Geppeto was the first in-house machine that I built at EnergyLab Lome. It is a 3-axis CNC machine with a frame made of 3D printed parts, combined with off the shelf rods and lead screws. The motors are 1.5 A nema 17, and it is all controlled using an arduino with CNC shield and grbl controller.

It was a great project, that took a while to master and many contributors. I would like to personally thank Hadnane OURO-AGBE, Matt STEDMA, and Edward YAKUBU, for their contributions to the project over time and for helping bring it to life.

IMPORTANT NOTE: this is one of the first projects that set me off on my machine building and electro-mechanical design journey, as such, I had not mastered the concept of properly documenting my work. Therefore the images and videos are sparse and limited.


## Equipment Details

Geppeto is a custom built desktop CNC designed for medium builds for machining wax and wood for assignments such as moulding and casting. Gepetto's body is a combination of 3D printed and extruded alluminum, with Nema 17 motors and an Arduino CNC sheild as hardware and a GRBL controller for firmware. It was made from an open source machine available on [Thingiverse](https://www.thingiverse.com/thing:3004773). A photo of the original design and the specifications are included below.

{{<image desktop-cnc.jpg>}}

{{<table "table table-striped table-bordered table-dark">}}
|Custom DIY Dremel CNC||
|--------|--------|
| Machine Type | 3030 Single Head CNC Router Woodworking Machine |
| Table Size| 300 x 500 mm|
| Work Plan|300 x 300 x 100 mm|
| Number of Axes| Three |
| Maximum Empty Travel Speed|4800 mm/min|
| Working Speed|4800 mm/min|
| Operation type | Linear bearings with lead screw (all axes)|
| Spindle Power|500 W  airc cooled spindle|
| Spindle Speed|0-12000 rmp|
| Motor |Nema 17|
|Operating Voltage|AC220V, 50HZ|
| Run Command|G Code|
| Operating System|UGS platform|
| Support Software|FreeCAD, Inkscape, Mods|
{{</table>}}


## Construction

Geppeto was the first machine that we ever built at EnergyLab. We built it to fill the need of being able to mill wood pieces and wax for lost wax casting.

We opted for an open source design that could make use of predesinged 3D printed parts that can be found in the youtube video below.

{{<youtube-responsive Njs0FU6PfPg>}}

We followed this design and tutorial pretty closely for the first version that we made. There were some design flaws which we corrected in the second version.

It was the first machine built in the lab. As such,  I didn't do a great job of properly documenting its construction. So photos are limited. There were two versions that we made. The first was 3D printed in organge filament, which had some design flaws and eventually failed.

### Version 1

Below is an image of the first version while under construction.

{{<image construct.jpg>}}

The first version had some major flaws were related to the y-axis holders. The top bracket above the guide rods was a little thin and would crack with the vibration. This would make the holes that secured them loose and so the bars would slide and fall out of position during a cut. Below is an image showing where the problem lie.

{{<image issuev1.jpg>}}

### Version 2

The second version was black, and had some fixes to the design flaws of the first. The first was a fix to the y-axis holders. We added some y-axis mount covers. Below is a photo of the fix.

{{<image fix.jpg>}}

## Commissioning

Another issue that was encountered was that the bed was not level and so when we would run the router the machine would cut too deep and drag to miss a few steps. This resulted in the coordinates being offset and would ruin a cut. To fix this, I used a surfacing router simlar to the image below to level the bed.

{{<image router.jpg>}}

Lastly, I commisioned and mad sure it was working well by testing with a pencil. You can see a photo of the first sketch that was created below.

{{<image commission.jpg>}}


## End Use

Once commissioned we were able to use the machine to do milling of wax for molding and casting. See the photos and videos below for results.

{{<video geppeto.mp4 >}}

{{<image pacome.jpeg>}}




