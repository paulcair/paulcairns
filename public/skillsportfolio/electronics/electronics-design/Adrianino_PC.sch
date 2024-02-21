EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L fab:R R3
U 1 1 6046D332
P 7300 3250
F 0 "R3" V 7093 3250 50  0000 C CNN
F 1 "499" V 7184 3250 50  0000 C CNN
F 2 "fab:R_1206" V 7230 3250 50  0001 C CNN
F 3 "~" H 7300 3250 50  0001 C CNN
	1    7300 3250
	0    1    1    0   
$EndComp
$Comp
L fab:Conn_FTDI_01x06_Male J3
U 1 1 6046E432
P 2650 4150
F 0 "J3" H 2481 4161 50  0000 R CNN
F 1 "FTDI" H 2481 4070 50  0000 R CNN
F 2 "fab:Header_SMD_FTDI_01x06_P2.54mm_Horizontal_Male" H 2650 4150 50  0001 C CNN
F 3 "~" H 2650 4150 50  0001 C CNN
	1    2650 4150
	1    0    0    -1  
$EndComp
$Comp
L fab:BUTTON_B3SN SW1
U 1 1 6046EE52
P 7250 4550
F 0 "SW1" H 7250 4835 50  0000 C CNN
F 1 "BUTTON" H 7250 4744 50  0000 C CNN
F 2 "fab:Button_Omron_B3SN_6x6mm" H 7250 4750 50  0001 C CNN
F 3 "https://omronfs.omron.com/en_US/ecb/products/pdf/en-b3sn.pdf" H 7250 4750 50  0001 C CNN
	1    7250 4550
	1    0    0    -1  
$EndComp
$Comp
L fab:LED D1
U 1 1 6046F703
P 7750 3250
F 0 "D1" H 7743 3466 50  0000 C CNN
F 1 "LED" H 7743 3375 50  0000 C CNN
F 2 "fab:LED_1206" H 7750 3250 50  0001 C CNN
F 3 "https://optoelectronics.liteon.com/upload/download/DS-22-98-0002/LTST-C150CKT.pdf" H 7750 3250 50  0001 C CNN
	1    7750 3250
	-1   0    0    1   
$EndComp
$Comp
L Connector:Conn_01x08_Female J2
U 1 1 60470836
P 7900 5250
F 0 "J2" H 7928 5226 50  0000 L CNN
F 1 "ANALOG" H 7928 5135 50  0000 L CNN
F 2 "fab:fab-1X08SMD" H 7900 5250 50  0001 C CNN
F 3 "~" H 7900 5250 50  0001 C CNN
	1    7900 5250
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x05_Female J5
U 1 1 60471889
P 2700 3400
F 0 "J5" H 2592 3785 50  0000 C CNN
F 1 "I2C" H 2592 3694 50  0000 C CNN
F 2 "fab:fab-1X05SMD" H 2700 3400 50  0001 C CNN
F 3 "~" H 2700 3400 50  0001 C CNN
	1    2700 3400
	-1   0    0    -1  
$EndComp
$Comp
L fab:Regulator_Linear_NCP1117-5.0V-1A U2
U 1 1 60473E21
P 7500 1500
F 0 "U2" H 7500 1742 50  0000 C CNN
F 1 "VREG" H 7500 1651 50  0000 C CNN
F 2 "fab:SOT-223-3_TabPin2" H 7500 1700 50  0001 C CNN
F 3 "https://www.onsemi.com/pub/Collateral/NCP1117-D.PDF" H 7600 1250 50  0001 C CNN
	1    7500 1500
	-1   0    0    -1  
$EndComp
$Comp
L fab:Conn_01x03_Male J4
U 1 1 60474504
P 7700 2700
F 0 "J4" H 7672 2724 50  0000 R CNN
F 1 "UPDI" H 7672 2633 50  0000 R CNN
F 2 "fab:Header_SMD_01x03_P2.54mm_Horizontal_Male" H 7700 2700 50  0001 C CNN
F 3 "~" H 7700 2700 50  0001 C CNN
	1    7700 2700
	-1   0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Female J1
U 1 1 604756AE
P 8100 900
F 0 "J1" H 8128 876 50  0000 L CNN
F 1 "POWER 9V" H 8128 785 50  0000 L CNN
F 2 "fab:fab-1X02SMD" H 8100 900 50  0001 C CNN
F 3 "~" H 8100 900 50  0001 C CNN
	1    8100 900 
	1    0    0    -1  
$EndComp
Wire Wire Line
	7450 3250 7600 3250
Wire Wire Line
	7550 900  7900 900 
Wire Wire Line
	7900 1000 7550 1000
Text Label 7550 900  0    50   ~ 0
VD0
Text Label 7550 1000 0    50   ~ 0
GND
Wire Wire Line
	7200 1500 6950 1500
Text Label 6950 1500 0    50   ~ 0
VCC
Wire Wire Line
	7800 1500 8100 1500
Text Label 8100 1500 0    50   ~ 0
VD0
Wire Wire Line
	7500 1800 7500 2050
Text Label 7500 2050 0    50   ~ 0
GND
Wire Wire Line
	7150 3250 6800 3250
Text Label 6800 3250 0    50   ~ 0
PA1
Wire Wire Line
	7900 3250 8250 3250
Text Label 8250 3250 0    50   ~ 0
GND
Wire Wire Line
	7700 4950 7400 4950
Text Label 7400 4950 0    50   ~ 0
VD0
Wire Wire Line
	7700 5050 7400 5050
Text Label 7400 5050 0    50   ~ 0
GND
Wire Wire Line
	7700 5150 7400 5150
Text Label 7400 5150 0    50   ~ 0
VCC
Wire Wire Line
	7700 5650 7400 5650
Text Label 7400 5650 0    50   ~ 0
GND
Wire Wire Line
	2900 3200 3150 3200
Text Label 3150 3200 0    50   ~ 0
GND
Wire Wire Line
	2900 3300 3150 3300
Text Label 3150 3300 0    50   ~ 0
VCC
Wire Wire Line
	2900 3400 3150 3400
Text Label 3150 3400 0    50   ~ 0
SDA
Wire Wire Line
	2900 3500 3150 3500
Text Label 3150 3500 0    50   ~ 0
SCL
Wire Wire Line
	2900 3600 3150 3600
Text Label 3150 3600 0    50   ~ 0
GND
Wire Wire Line
	4550 3300 4300 3300
Text Label 4300 3300 0    50   ~ 0
SCL
Wire Wire Line
	4550 3400 4300 3400
Text Label 4300 3400 0    50   ~ 0
SDA
Wire Wire Line
	4550 3500 4300 3500
Text Label 4300 3500 0    50   ~ 0
RX
Wire Wire Line
	4550 3600 4300 3600
Text Label 4300 3600 0    50   ~ 0
TX
Wire Wire Line
	7500 2600 7200 2600
Text Label 7200 2600 0    50   ~ 0
UPDI
Wire Wire Line
	7500 2700 7200 2700
Text Label 7200 2700 0    50   ~ 0
GND
Wire Wire Line
	7500 2800 7200 2800
Text Label 7200 2800 0    50   ~ 0
VCC
Wire Wire Line
	5750 3300 6000 3300
Text Label 6000 3300 0    50   ~ 0
UPDI
Wire Wire Line
	5750 3400 6000 3400
Text Label 6000 3400 0    50   ~ 0
PA1
Wire Wire Line
	5750 3500 6000 3500
Text Label 6000 3500 0    50   ~ 0
PA2
Wire Wire Line
	5750 3600 6000 3600
Text Label 6000 3600 0    50   ~ 0
PA3
Wire Wire Line
	7500 3800 7100 3800
Text Label 7100 3800 0    50   ~ 0
PA1
Wire Wire Line
	7500 3900 7100 3900
Text Label 7100 3900 0    50   ~ 0
PA2
Wire Wire Line
	7500 4000 7100 4000
Text Label 7100 4000 0    50   ~ 0
PA3
Wire Wire Line
	7800 3800 8250 3800
Text Label 8250 3800 0    50   ~ 0
GND
Wire Wire Line
	7800 3900 8250 3900
Text Label 8250 3900 0    50   ~ 0
GND
Wire Wire Line
	7800 4000 8250 4000
Text Label 8250 4000 0    50   ~ 0
GND
Wire Wire Line
	7700 5250 7400 5250
Text Label 7400 5250 0    50   ~ 0
PA4
Wire Wire Line
	7700 5350 7400 5350
Text Label 7400 5350 0    50   ~ 0
PA5
Wire Wire Line
	7700 5450 7400 5450
Text Label 7400 5450 0    50   ~ 0
PA6
Wire Wire Line
	7700 5550 7400 5550
Text Label 7400 5550 0    50   ~ 0
PA7
Wire Wire Line
	5750 3700 6000 3700
Text Label 6000 3700 0    50   ~ 0
PA4
Wire Wire Line
	5750 3800 6000 3800
Text Label 6000 3800 0    50   ~ 0
PA5
Wire Wire Line
	5750 3900 6000 3900
Text Label 6000 3900 0    50   ~ 0
PA6
Wire Wire Line
	5750 4000 6000 4000
Text Label 6000 4000 0    50   ~ 0
PA7
$Comp
L fab:R R4
U 1 1 6046D77D
P 7800 4550
F 0 "R4" V 7593 4550 50  0000 C CNN
F 1 "1k" V 7684 4550 50  0000 C CNN
F 2 "fab:R_1206" V 7730 4550 50  0001 C CNN
F 3 "~" H 7800 4550 50  0001 C CNN
	1    7800 4550
	0    1    1    0   
$EndComp
Wire Wire Line
	7050 4550 6800 4550
Text Label 6800 4550 0    50   ~ 0
VCC
Wire Wire Line
	7450 4550 7550 4550
Wire Wire Line
	7950 4550 8250 4550
Text Label 8250 4550 0    50   ~ 0
GND
Wire Wire Line
	7550 4550 7550 4250
Connection ~ 7550 4550
Wire Wire Line
	7550 4550 7650 4550
Text Label 7550 4250 0    50   ~ 0
PA3
Text Label 3500 2400 0    50   ~ 0
SDA
Wire Wire Line
	3500 2150 3500 2400
Text Label 3950 2400 0    50   ~ 0
SCL
Wire Wire Line
	3950 2150 3950 2400
Text Label 3950 1600 0    50   ~ 0
VCC
Wire Wire Line
	3950 1850 3950 1600
Text Label 3500 1600 0    50   ~ 0
VCC
Wire Wire Line
	3500 1850 3500 1600
$Comp
L fab:R R2
U 1 1 6046CF98
P 3950 2000
F 0 "R2" H 4020 2046 50  0000 L CNN
F 1 "4.99k" H 4020 1955 50  0000 L CNN
F 2 "fab:R_1206" V 3880 2000 50  0001 C CNN
F 3 "~" H 3950 2000 50  0001 C CNN
	1    3950 2000
	1    0    0    -1  
$EndComp
$Comp
L fab:R R1
U 1 1 6046CBC8
P 3500 2000
F 0 "R1" H 3570 2046 50  0000 L CNN
F 1 "4.99k" H 3570 1955 50  0000 L CNN
F 2 "fab:R_1206" V 3430 2000 50  0001 C CNN
F 3 "~" H 3500 2000 50  0001 C CNN
	1    3500 2000
	1    0    0    -1  
$EndComp
$Comp
L fab:C C1
U 1 1 6046DD35
P 5450 1950
F 0 "C1" H 5565 1996 50  0000 L CNN
F 1 "1uF" H 5565 1905 50  0000 L CNN
F 2 "fab:C_1206" H 5488 1800 50  0001 C CNN
F 3 "" H 5450 1950 50  0001 C CNN
	1    5450 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5450 1800 5450 1550
Text Label 5450 1550 0    50   ~ 0
VCC
Wire Wire Line
	5450 2100 5450 2350
Text Label 5450 2350 0    50   ~ 0
GND
Wire Wire Line
	5150 3000 5150 2700
Text Label 5150 2700 0    50   ~ 0
VCC
Wire Wire Line
	5150 4400 5150 4700
Text Label 5150 4700 0    50   ~ 0
GND
Wire Wire Line
	2850 3950 2950 3950
Text Label 3150 3950 0    50   ~ 0
GND
Wire Wire Line
	2850 4150 3000 4150
Text Label 3150 4150 0    50   ~ 0
VCC
Wire Wire Line
	2850 4250 3150 4250
Text Label 3150 4250 0    50   ~ 0
TX
Wire Wire Line
	2850 4350 3150 4350
Text Label 3150 4350 0    50   ~ 0
RX
$Comp
L Power:PWR_FLAG #FLG0101
U 1 1 6068B2E8
P 2950 3950
F 0 "#FLG0101" H 2950 4025 50  0001 C CNN
F 1 "PWR_FLAG" H 2950 4123 50  0000 C CNN
F 2 "" H 2950 3950 50  0001 C CNN
F 3 "~" H 2950 3950 50  0001 C CNN
	1    2950 3950
	1    0    0    -1  
$EndComp
Connection ~ 2950 3950
Wire Wire Line
	2950 3950 3150 3950
$Comp
L Power:PWR_FLAG #FLG0102
U 1 1 6068CE18
P 3000 4150
F 0 "#FLG0102" H 3000 4225 50  0001 C CNN
F 1 "PWR_FLAG" H 3000 4323 50  0000 C CNN
F 2 "" H 3000 4150 50  0001 C CNN
F 3 "~" H 3000 4150 50  0001 C CNN
	1    3000 4150
	1    0    0    -1  
$EndComp
Connection ~ 3000 4150
Wire Wire Line
	3000 4150 3150 4150
$Comp
L Adrianino-eagle-import:CONN_03X2-PINHEAD-SMD J6
U 1 1 6046FEF2
P 7600 3900
F 0 "J6" H 7650 4286 59  0000 C CNN
F 1 "DIGITAL" H 7650 4181 59  0000 C CNN
F 2 "fab:fab-2X03SMD" H 7600 3900 50  0001 C CNN
F 3 "" H 7600 3900 50  0001 C CNN
	1    7600 3900
	1    0    0    -1  
$EndComp
$Comp
L MCU:ATtiny1614-SS U1
U 1 1 6046BDCE
P 5150 3700
F 0 "U1" H 5150 4581 50  0000 C CNN
F 1 "ATtiny1614-SS" H 5150 4490 50  0000 C CNN
F 2 "fab:SOIC-14_3.9x8.7mm_P1.27mm" H 5150 3700 50  0001 C CIN
F 3 "http://ww1.microchip.com/downloads/en/DeviceDoc/ATtiny1614-data-sheet-40001995A.pdf" H 5150 3700 50  0001 C CNN
	1    5150 3700
	1    0    0    -1  
$EndComp
$EndSCHEMATC
