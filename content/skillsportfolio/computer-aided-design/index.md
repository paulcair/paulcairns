+++
title = "Computer Aided Design"
image = "thumbnail.jpg"
weight = 30

[typeScript] 
typeScript1 = "Computer Aided Design: showcasing my CAD skills" 
typeScript2 = "See the work I did using FreeCAD"

[headline]
headline = "Objective: to evaluate 2D and 3D software, demonstrate and describe processes used in modelling, and model a possible project"
+++



This week I worked on defining my final project idea and started to get used to the documentation process. The learning objectives for the assignment this week are:

a. Evaluate and select 2D and 3D software

b. Demonstrate and describe processes used in modelling with 2D and 3D software    

c. Model experimental objects/part of a possible project in 2D and 3D software   

d. Show how I did it with words/images/screenshots 

e. Include my original design files


## a. Evaluate and select 2D and 3D software

Since I am working to build out a node in Togo, Africa, and cost constraints with regards to sofware are an issue faced by Africans. I will opt to work with the open source softwares. As a result, I elected to use the following softwares:

-   2D Modelling - Inkscape

-   3D Modelling - FreeCAD  

{{<image-matrix-2 InkscapeLogo.jpg FreeCadLogo.jpg>}}

## b. Demonstrate and select 2D and 3D software

For my project I have elected to create a stove that generates electricity for cell phone appliances and other low voltage DC electronics. An expoded view of the final 3D model is shown below

{{<image-matrix-2 thumbnail.jpg AssemblyExploded.jpg>}}

 
To create this model various computer aided design skills were needed both in Inkscape, and in FreeCAD. In this section i will link to the video tutorials I used to learn each of these skills. I will also embed some of the videos below. Here is a list of the skills that were required

### 2D Inkscape skills

Below is a list of the Inkscape skills that were used to make the model for my project including links to the Youtube videos that were used for each skill. For further inkscape tutorials you can also visi ther tutorial webpage here: (https://inkscape.org/learn/tutorials/)


- ([Intro to inscape](https://www.youtube.com/watch?v=8f011wdiW7g)
- ([Shape tools and option](https://www.youtube.com/watch?v=LEjlKhVnJgU))
- ([Groups, levels, and object selection](https://youtu.be/D_53Cb9aR0c)) 
- ([Difference, union, intersection, combine](https://youtu.be/jxhR9aT6crU))
- ([Importing a logo/image and converting to svg](https://www.youtube.com/watch?v=KsCwsOqBLtg))
- ([Saving svg to import into FreeCad](https://www.youtube.com/watch?v=6LedIN5S2so))


{{<youtube-matrix-2 8f011wdiW7g LEjlKhVnJgU>}}

{{<youtube-matrix-2 D_53Cb9aR0c jxhR9aT6crU>}}
  

### 3D FreeCAD skills

Below is a list of the FreeCAD Skills that were used to make the model for my project including links to the YouTube videos that were used. The workbench that was required to use each feature is also identified. For further FreeCAD tutorials you can also visit their tutorial webpage here: (https://wiki.freecadweb.org/Tutorials)

#### Sketcher

- ([Making a sketch and constraining it](https://youtu.be/lI3KDep2TxE))
- ([Creating a datum plane](https://youtu.be/zY3dzk1Q554))
- ([Parameterising a sketch - includes Spreadsheet Workbench discussion](https://www.youtube.com/watch?v=fXoRAYv1wHQ))
- ([Creating a shapestring]( https://www.youtube.com/watch?v=_D5WJqd1SSE&t=614s))
- ([Making a sketch and transforming it onto a surface - includes Surface Workbench](https://www.youtube.com/watch?v=iU0GxYs39oI))

#### Part Design Workbench

- ([Pad and Pocket (Extrude and Cut)](https://youtu.be/3LiKwUFSbAw))
- ([Sweep](https://youtu.be/P-qQSuMxjtI)
- ([Multi Transform - linear and polar](https://youtu.be/NJsUTG4TSzk))
    
#### Part Workbench

- ([Make a union between two bodies](https://youtu.be/hA9xpfzrbFE))
- Make a cut between two bodies (same link as above)

#### Draft Workbench

- ([Linear array](https://youtu.be/NjEWcvLH9Uc))
- Polar array (same as above)   

#### Sheetmetal workbench

- ([Bend](https://youtu.be/qsj8-ZnQrs0))
- Flatten (same as above)

#### Surface Workbench

- ([How to make surfaces](https://www.youtube.com/watch?v=Mi_r4mgBGeg))

#### Assembly Workbench

- ([Creating an assembly](https://www.youtube.com/watch?v=6vlkd27fgf0))
- ([Mating parts](https://youtu.be/lfinO3EGXeo))
   
#### Exporting and Rendering

- ([Meshing and exporting your CAD file as a .OBJ for 3D printing or Rendering](https://www.youtube.com/watch?v=7cT_O1KnBJA))
- ([Rendering Your Assembly using Blender](https://www.youtube.com/watch?v=tMiGNJbPaPY))
- ([Rendering using CadRays](https://www.youtube.com/watch?v=1H5LD5mxWsE))

{{<youtube-matrix-3 NJsUTG4TSzk hA9xpfzrbFE NjEWcvLH9Uc>}}

{{<youtube-matrix-3 qsj8-ZnQrs0 Mi_r4mgBGeg lfinO3EGXeo>}}


## c. Model experimental objects/part of a possible project in 2D and 3D software

In this section I will provide a video of the final 3D model with a walk through of all the parts and features. See the video below for details

{{<youtube HbZEdt0Rnaw>}}


## d. Show how I did it with words/images/screenshots

In this section I will show in detail how I constructed each body and sketch using FreeCAD or Inkscape as well as how I was able to parameterise the design.

### Inkscape walkthrough

In these videos I demonstrate the work that was done on Inkscape to make the louvre slits and also how to I imported the sketch into FreeCAD. Note that the SVG file is included below. You can also see a screenshot. The videos require too much space therefore they are linked to youtube.

{{<youtube-matrix-2 TqHoiDLZckM 4c8Wsj422Cw>}}

Here is a photo of the inkscape file

{{<image-responsive louvres.jpg>}}

You can see on the screen that I used a circle and then used the subtract feature of the three squares. Lastly, I merged all the objects into one path.


### FreeCAD Walkthrough

In these videos I perform a walkthrough of the FreeCAD functions and methods used to create my 3D models. I also exported the results into an STL format with the files shown below. Again, the videos were very large and as a result they had to be posted on YouTube. 

{{<youtube KnSy1IqwT4g>}}

Below are photos of the STL versions of what was created. Note many functions in FreeCAD were used such as pad, pocket, loft, sweep, rotate, and more.

{{<image-matrix-2 assembly.jpg tegcover.jpg>}}


### Parameterisation walkthrough

In this section I discuss how to parametrize the file and the parameterization that was done for this assembly.

As is discussed in the video (file too large to upload) I use the spreadsheet function to determine the dimensions and then label all dimensions as a function of those defined in the spreadsheet. This way you can see and change any parameter to reconfigure the entire assembly.

{{<youtube DMSvgu0MzhI>}}
   
In the image below I demonstrate how the spreadsheet looks in FreeCAD and illustrated the variables that were used.

{{<image-responsive parameters.jpg>}}

## e. Include my original design files

1. [Louvreslits.svg](LouvreSlits.svg)
2. [StoveAssembly.stl](EGTechStoveAssembly.stl)
3. [TEGCover.stl](TEGCoverSubtract.stl)
4. [StoveAssemblyFreeCAD.zip](StoveAssemblyFC.zip)




