+++
title = "OnShape"
image = "thumbnail.jpg"
weight = 30

[typeScript] 
typeScript1 = "Computer Aided Design: showcasing my OnShape CAD skills" 
typeScript2 = "See the work I've done using OnShape"

[headline]
headline = "Objective: to demonstrate and describe processes used in modelling using OnShape"
+++

The project I will work on using OnShape is a omnidirectional gear that I plan to 3D print using my SLA printer.

# About OnShape

OnShape is an online 3D modelling software that is ideal for collaborating on a project. It is not the most rigorous CAD tool, but there is a free version and it is quite user intuitive. 

{{<image home.png >}}

Furthermore, it has several usefull libraries such as the Beam add-on for quickly creating 8020 extrusions. Its online and open model has enabled a lot of interesting development and add-ons such as this.

{{<image beam-addon.png >}}

It has the ability to model indivdual parts and/or create assemblies. It also has great version control and the ability to import and export files as STEP, STL, 3mf (Fusion 360), and .sldprt (Solidworks), and Rhino. This makes it a great place to store your modelling files on a project where you have multiple designers who use different softwares.

{{<image-matrix-2 version-control.png export.png>}}

I definitely recommend OnShape for a beginner modeller who is looking for a simple user interface and wants to collaborate on a team project. Or as a nice PLM or ECO management for your CAD files for advanced designers who want to collaborate on a team across CAD softwares.

# Modeling Workflow

For this project I am going to create an omnidirectional actuveball mecahnism joint (more commonly known as a "Spherical gear") to print on my SLA printer. I want to make this to test the abilities of this type of joint for motion control. The GIF below demonstrates the functionality of what I will be modelling.

{{<image spherical-gear.gif>}}

I am printing it on my SLA printer so that I can test SLA printing parameters and get an idea for how well it is capable of printing something like this that requires a bit of a smooth surface finish compared to what a FDM printer might be capable of doing in the same amount of print time.

## 1. Create new project folder and file

To begin I created a new project folder because the joint will consist of numerous parts. From a documentation and version control perspective it makes most sense to save all the files in one folder. After thisyou can create a new document. I am calling the folder "omnigear" and the document "driven-sphere".

{{<image project-folder.png>}}

Once you have created your file you will enter into a regular workspace where you can select your plane and begin modelling.

{{<image workspace.png>}}

## 2. Add the spur gear tool

To begin modelling this part I'm actually going to use the spur gear tool offered by OnShape to generate my spur gear sketch and then revolve it around the x-axis and then do a revolved cut around the y-axis to design my part. To add the spur gear tool navigate to the "Search tools" button or press alt-c. Then type gear into the search bar. Click on it and it will generate a gear part.

{{<image gear-tool.png>}}

## 3. Set the gear parameters

Once complete, you can very easily modify the gear specifications, including the depth (thickness of the gear), number of teeth, Pitch circle diameter, the pressure angle, root fillet, and you can even create helical gears and center boards by checking the boxes. For my model I am going to create a 5 cm (50 mm) diameter spherical gear with 35 teeth and a thickness of 5 mm. Once you have modified the given parameters click on the green arrow to generate the part.

{{<image gear-generator.png>}}

## 4. Project the gear onto a new sketch midplane

The Next step is to create a new sketch on the front plane, by selecting it, and clicking the sketch button on the top left. Next. we will click on the "Use" button and select the gear body. This will project the gear onto the midplane. 

{{<image project.png>}}

## 5. Cut half the gear away on the sketch and revolve the gear

The next step is to draw a line across the center of the gear and delete one half of it so we can revolve it around its center axis. 

{{<image-matrix-2 cut.png revolve.png>}}

You should end up with something similar to the below.

{{<image sphere.png>}}

## 6. Copy the spur-gear sketch onto the right plane

The final step is to open the spur-gear sketch that was cut. You can then copy the sketch and create a new sketch on the right plane and paste the sketch features. Next transform the sketch so that it intersects with the revolve tooth. As per the images below.

{{<image-matrix-3 copy.png paste.png transform.png>}}

Next, create a centerpoint arc that goes around the outside of the gear and connect it all to the gears so you will remove the correct material.

{{<image arc.png>}}

## 7. Perform a revolve cut to finish the piece

Use the revolve feature once again and select the "Remove" option to cut away the transformation.

{{<image revolve-cut.png>}}

You should end up with something that looks like the following below.

{{<image final.png>}}

## 8. Export STL to import into your favorite slicer for 3D printing

Export the STL file for your slicer and enjoy.

{{<image-matrix-2 export1.png export2.png>}}







