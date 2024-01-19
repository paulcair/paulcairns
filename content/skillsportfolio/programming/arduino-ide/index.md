+++
title = "Arduino IDE"
image = "thumbnail.jpg"
weight = 30

[typeScript] 
typeScript1 = "Embedded Programming using Arduino IDE" 
typeScript2 = "See the work embedded programming I have done using Arduino IDE"

[headline]
headline = "Objective: to learn how to program the microcontroller chip on the circuit board we designed in Week 7."
+++
---

On this page, the objective was to showcase how to program a microcontroller chip on a circuit board that was designed during my [Fab Academy week 7 "electronics design" assignment](https://fabacademy.org/2021/labs/vancouver/students/paul-cairns/assignments/9-embedded-programming/). As usual, the assignment had a group and individual element. Below are the details.

**Group assignment:**

-   Compare the performance and development workflows for different microcontroller families
-   Document your work (in a group or individually)

**Individual assignment:**

-   Read the datasheet for the microcontroller you are programming
-   Program the board you have made to do something, with as many different programming languages and programming environments as possible.

**Learning outcomes:**

-   Identify relevant information in a microcontroller datasheet.
-   Implement programming protocols.
-   Document what you learned from reading a microcontroller datasheet.
-   Program your board
-   Described the programming process/es you used
-   Include your source code
-   Include a short ‘hero video’ of your board

As usual, we will start with the group assignment documentation and then present the individual assignment documentation.

# Individual Assignment

The individual assignment consisted of two tasks. The first was to read and understand that data shee for the microcontroller you are programming, and the second is to program the board. We will begin by discussing that datasheet.

## AT-Tiny 1614 data sheet

For my electronics design project, I designed a version of the [Adrianino](http://fabacademy.org/2020/labs/leon/students/adrian-torres/adrianino.html). The Afrianino uses the AT-Tiny 1614 microcontroller. The datasheet for which [can be found here](../7-electronics-design/ATtiny.pdf).

### Introduction

The ATtiny1614 is a memberare members of the tinyAVR®
 1-series of microcontrollers, using the AVR®
 8-bit processor with hardware multiplier, running at up to 20 MHz and with 16 KB Flash, 2 KB of SRAM, and
256 bytes of EEPROM in a 14-pin package. Below are some of the specifications:

-   **CPU:** AVR 8-bit CPU running at up to 20 MHz
-   **Memories:** 16 KB in systemp self-programmable flash memory
    -   256 bytes EEPROM
    -   2 KB SRAM
    -   Write/erase flash 10,000 cycles, EEPROM 100,000 cycles
-   **System:** Power-on reset
    -   Brown out detection
    -   Internal and external clock optionn
    -   16/20 MHz lower-power RC oscillater
    -   Single pin programming and debugging interface (UPDI)
    
    further details regarding the introduciton and system specificaitons can be found on page 1 and 2 of the document.

### Block diagram

One of the first and most critical diagrams in the spec sheet is the block diagram. This diagram gives an overiew of the chip internals, system details, peripherals, and provides an idea of the I/O of the chip. The image below is presents the block diagram for the AT-tiny 1614. (p. 13, Figure 3-1)

{{<image-responsive blockdiagram.jpg>}}

### Pinout

The next diagram of importance in the spec sheet is the pinout. The pinout describes the which peripherals and I/O types are available at each pin. The image below presents the pinout. (p.14, Figure 4.1)

{{<image-responsive pinout.jpg>}}

The important pins to consider for the AT-tiny are the VDD (pin 1), the GND (pin 14), and the UPDI (pin 10). Other important pins to pay attention to are:

-   Pins 2-5, 8,9 11, 12: Digital/analog functions to read or output to peripherals
-   Pins 6 and 7: GPIO and clock
-   Pin 13 GPIO/Clock/Analalog function

### Memory map and flash

The ATtiny1614 conatains a 16 KB on-chip in-system reprogrammable flash memory for program storage.(p.17,18, Figures 6-1, 6-2, respectively)  

{{<image-matrix-2 memorymap.jpg flash.jpg>}}

Important things to note from the images that there is 256 bytes of EEPROM memory and 16 KB of flash memory.

The ATtiny1614 has 256 bytes of EEPROM data memory, see Memory Map section. The EEPROM
memory supports single byte read and write. The EEPROM is controlled by the Nonvolatile Memory
Controller (NVMCTRL). (Page 18, Section 6.5)

The ATtiny1614 contains 16 KB on-chip in-system reprogrammable Flash memory for program storage. (Page 17, Section 6.3)
Since all AVR instructions are 16 or 32 bits wide, the Flash is organized as 4K x 16. For write protection,
the Flash program memory space can be divided into three sections:

-   Bootloader section, 
-   application code section, 
-   application data section, 

with restricted access rights
among them.


###  Peripherals and Architecture

The ATtiny 1614 has numerous peripherals with various addresses below is a list of the types of peripherals it contains:

-   Virtual Ports (A/B)
-   I/O registers
-   CPU
-   Reset controller
-   Sleep controller
-   Clock Controller
-   Brown-out detector
-   Voltage reference
-   Port configuration
-   Analog comparators
-   Digital-to-Analog converters
-   Universal Synchronous Asynchronous Receiver Transmitter
-   Serial Peripheral interface
-   Timer/counter
-   System configuration

This information can all be found in the peripherals section (p. 42, Section 7) and is all neatly summarized in Table 7-1 as illustrated below.

{{<image-responsive peripherals.jpg>}}

Details of each peripheral are given in the chapters that follow. We will not discuss them in detail here. The last two things we will discuss before moving ahead to programming the board will be the CPU and the UPDI.

### AVR CPU

The AVR CPU uses 8-bit AVR CPU. The CPU is able to access memories, perform calculations, control peripherals, and execute instructions in the progrm memory. This CPU uses a **HARVARD Architecture** with seperate buses for program and data. Instruction in the program memory are executed with single-level pipelining. While one instruction is being ecuted, the net instruction is prefetched from the program memory, which enables instruction to be executed on every clock cycle. (p.48, Sections 8.1-8.3). The features of this AVR CPU are:

-   8-Bit, High-Performance AVR RISC CPU
-   135 instructions
-   Hardware multiplier
-   32 8-Bit Registers Directly Connected to the Arithmetic Logic Unit (ALU)
-   Stack in RAM
-   Stack Pointer Accessible in I/O Memory Space
-   Direct Addressing of up to 64 KB of Unified Memory:
-   Entire Flash accessible with all LD/ST instructions
-   True 16/24-Bit Access to 16/24-Bit I/O Registers
-   Efficient Support for 8-, 16-, and 32-Bit Arithmetic
-   Configuration Change Protection for System Critical Features

A block diamgram that illustrates the architecture is shown below:

{{<image-responsive cpuarchitecture.jpg>}}

Last topic of discussion will be the Unified Program and Debug Interface (UPDI)

### UPDI - Unified Program and Debug Interface

The UPDI is an interface for external programming and on-chip debugging of a device. The UPDI supports programming of nonvolatile memory (NVN) spalce; FLASH, EEPROM, ukbi and the user row. Furthermore, the UPDI can access the entire I/O and data space of the device. Programming and debugging are done the the UPDI Physical interface (UPDI PHY), which is a 1-wire interface that uses the RESET pin. The UPDI access layer grants access to the bus matrix, with memory mapped access to system blocks such as NVM, and peripherals. (p.516, Section 33.2). The fueature of the Unified Program and Debug Interface are as follows (p.516, Section 33.1):

**Programming:**
-   External programming through UPDI 1-wire (1W) interface
-   Enable programming by 12V or fuse
-   Uses the RESET pin of the device for programming
-    No GPIO pins occupied during operation
-   Asynchronous Half-Duplex UART protocol towards the programmer

**Debugging:**
-   Memory mapped access to device address space (NVM, RAM, I/O)
-   No limitation on device clock frequency
-   Unlimited number of user program breakpoints
-   Two hardware breakpoints
-   Run-time readout of CPU Program Counter (PC), Stack Pointer (SP), and Status register
(SREG) for code profiling
-   Program flow control -> Go, Stop, Reset, Step Into
-   Non-intrusive run-time chip monitoring without accessing system registers -> Monitor CRC status and sleep status

**Unified Programming and Debug Interface (UPDI):*
-   Built-in error detection with error signature readout
-   requency measurement of internal oscillators using the Event System

A block diagram of the UPDI system is shown in the image below (p.517, Figure 33-1):

{{<image-responsive updi.jpg>}}





## Programming Blink onto the ATtiny 

The circuit board that was constructed was designed to be compatible with Arduino IDE and thus reprogrammable based on the functions that you want it to perform. In this section we will discuss how to program the standard "blink" sketch onto our AT-Tiny board. The steps are as follows:

i)      Install Arduino IDE
ii)     Download and install the AT-Tiny board library
iii)    Configure Ubuntu for pyudpi (linux only)
iv)     Install dependecies (linux only)
v)      Set the board configuration and port
vi)     Upload the blink sketch using Arduino
vii)    Program the board using python (linux only)

As a note, the directions used for programming this board were based very closely on the guidance given by Adrian Torres on his [Adrianino Fab Academy Website](http://fabacademy.org/2020/labs/leon/students/adrian-torres/adrianino.html#outputs).

There is also a good YouTube video that describes how to install the TinyMegaCore package onto Aurduino IDE below.

{{<youtube-responsive AL9vK_xMt4E>}}

Before we begin, we will want to connect our board to our computer. we do this by connecting our FTDI chip with our UPDI chip and slip that into the UPDI slot of our board. The image below illustrates how to connect the hardware:

{{<image-matrix-2 PlugIn1.jpg PlugIn2.jpg>}}

**i) Install Arduino IDE:**The first step was to install the arduino IDE, on windows this can be done at the [arduino website](https://www.arduino.cc/en/software), for linux this can be done using the Ubuntu software manager. 

**ii) Download and install the AT-Tiny board library:** The next step is to download the AT-Tiny board library by Spence Konde [it can be found here](http://drazzy.com/package_drazzy.com_index.json). If you need further assistance you can follow the [Spence Konde Tutorial here](https://github.com/SpenceKonde/megaTinyCore/blob/master/Installation.md) as well. For simplicity you can just copy the Mega Tiny Core URL into the Arduino IDE boards library by clicking: ***File > Preferences***

URL: http://drazzy.com/package_drazzy.com_index.json

the image below shows where to paste the link.

{{<image-responsive ArdURL.jpg>}}

The next step is to install it in the boards manager by clicking: ***Tools > Board > Board Manager*** scrolling down to the "MegaTinycore" library and clicking ***install*** there is a **VERY IMPORTANT NOTE: YOU MUST INSTALL VERSION 2.2.1** we were unable to get the sketh to upload successfully using any of the newer versions. Below is an image of the installation process

{{<image-responsive ArdInstMega221.jpg>}}

If you are using Ubuntu or linux based software you will want to continue with the following steps. **If you are using Windows, you can proceed to step v).**

**iii) Configure Ubuntu for pyudpi (linux only):** The next step is to configure python UPDI. You can do so by cloning the following git repository to your computer using the terminal.

URL: https://github.com/mraardvark/pyupdi

{{<image-responsive GitClone.jpg>}}

**iv) Install dependencies (linux only):** In this step you will want to run the following command in your command line to install the python dependencies.

```
    pip3 install intelhex pylint pyserial
```


**v) Set the board configuration and port:** In this step you will return to the Arduino IDE and load your sketch as you normally would. You will next want to set the board configuration as follows ***Tools > Boards > MegaTinyCore > ATtiny 1614***
and you will want to set the programmer to Serial Port and 4.7k (pyupdi style) under ***Tools > programmer > Serial Port and 4.7k***. Other settings to consider are the clock. To set it at 20 MHz. The image below demonstrates these steps.

{{<image-responsive ArdSetBoard.jpg>}}

**vi) Upload the blink sketch:** By navigating to ***File > Examples > 01 Basics > blink*** you can open the blink sketch. For this board change the pin number to Pin 8, which is the pin that the LED is wired to. You can do this by replacing ***LED_BUILTIN*** in the code with ***8***. Once finished click upload. The following video demonstrated that it worked.

{{<video-responsive blink-13s.mp4>}}

The final step, if you are using linux, is to program the board using python. This will be necessary if the Arduino IDE does not upload properly to your board. Details about this will be discussed in the following step.

**vii) Program the board using python (linux only):** When the Arduino finishes compiling you will want to find the ***.hex*** file in the temporary folder. lastly open the command line and run the following code 

```
sudo python3 pyupdi.py -d tiny1614 -c /dev/ttyUSB0 -b 115200 -f Blink.ino.hex -v
```

being sure to replace ***/dev/ttyUSB0*** with the directory that you put your ***.hex*** file.

## Programming hello.t1614.echo.ino onto the ATtiny using Arduino IDE

Now that we have configured the Arduino IDE on both Windows and Linux, we are going to try uploadinging another program that uses the Serial Monitor. The program we will be uploading onto the chip is the hello.t1614.echo.ino by Neil Gershenfeld (link to file in the Files section below). For this we will be repeating step (vi) above but uploading a different file. 

***IMPORTANT STEP: once you have uploaded the files using the FTDI and the UPDI programmerr you must REMOVE THE PROGRAMMER in order to talk to the chip and have the serial monitor work*** 

{{<image-responsive programmerremoved.jpg>}}

### hello.t1614.echo.ino Windows

Here is a video of the hello.echo program uploaded onto the chip. Note that the Serial Monitor was set to 9600 in the program and was also seleted in the "baud" at the bottom of the serial monitor.

{{<video-responsive helloecho-ino.mp4>}}

Picture of final result:

{{<image-responsive helloechoresult.jpg>}}

Next. I repeated the same process using linux. Below are the results from using Arduino IDE for linux.

{{<video-responsive helloecho-inolinux.mp4>}}

Picture of final result:

{{<image-responsive helloechoinolinux.jpg>}}

The results were good!

### hello.world.ino for Windows

Lastly, I wanted to test a program that I wrote myself. In this program I simply printed "hello world" to the serial monitor without any user input or prompt. I ran this program simply on windows. Here is the result.

{{<video-responsive hello-world-ino.mp4>}}

## Programming hello.1614.echo.ino using VSCode and Python on Linux

After obtaining a solid confidence with the Arduino IDE on both Windows and Linux, I attempted to upload and program the ATtiny using VS Code and python. used the hello.1614.py code created by Neil Gershenfeld.

I was succesful in using VS Code to run and compile the python code but was unsucessful in uploading the code to the chip as well as not sure how to monitor the results. I believe further learning and investigation and perhaps a different IDE will be necessary.

# Files

-   [ATtiny Spec Sheet](../7-electronics-design/ATtiny.pdf)
-   [hello.1614.echo.ino](Helloecho-ino.ino)
-   [hello.world.ino](Helloechopc-ino.ino)
-   [hello.1614.echo.py](helloecho.py)
