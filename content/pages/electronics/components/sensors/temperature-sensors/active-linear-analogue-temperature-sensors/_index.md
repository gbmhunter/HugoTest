---
author: gbmhunter
date: 2016-04-19 05:21:18+00:00
draft: false
title: Active Linear Analogue Temperature Sensors
type: page
url: /electronics/components/sensors/temperature-sensors/active-linear-analogue-temperature-sensors
---

# Overview

Linear active temperature sensors output a analogue voltage which is proportional (linear) to the temperature, and require a voltage supply to run.

[caption id="attachment_8831" align="aligncenter" width="279"][![A photo of the common TMP36 analogue temperature sensor in the TO-92 package. Image from https://www.sparkfun.com/products/10988.](/images/2012/11/temp-sensor-tmp36-to-92-photo.jpg)
](/images/2012/11/temp-sensor-tmp36-to-92-photo.jpg) A photo of the common TMP36 analogue temperature sensor in the TO-92 package. Image from https://www.sparkfun.com/products/10988.[/caption]

They require contact with the medium that is to be measured. They usually require three connections (power, ground, and Vout), but can be purchased in packages with more pins. They use an internal diode to measure the temperature, surrounded by circuitry which linearises the output, provides an offset, and makes the reading insensitive to other parameter changes.

[caption id="attachment_8828" align="aligncenter" width="502"][![Graph of the voltage output vs. temperature for a Microchip TC1046 analogue temperature sensor. Image from http://ww1.microchip.com/downloads/en/DeviceDoc/21496C.pdf.](/images/2012/11/temp-sensor-tc1046-graph-output-voltage-vs-temp.png)
](/images/2012/11/temp-sensor-tc1046-graph-output-voltage-vs-temp.png) Graph of the voltage output vs. temperature for a Microchip TC1046 analogue temperature sensor. Image from http://ww1.microchip.com/downloads/en/DeviceDoc/21496C.pdf.[/caption]

Being encapsulated in a standard through-hole or surface mount component package, **these temperature sensors are designed to measure the temperature at the location at which they are soldered onto the circuit board**. This is called _local_ temperature sensing. This makes them somewhat unsuitable if you want to measure the temperature of an off-PCB location (_remote_ temperature sensing), although you can mount the through-hole versions onto pretty much anything you want and then attach it to the PCB via a cable. The [Texas Instruments LM35DT temperature sensor](http://www.ti.com/lit/ds/symlink/lm35.pdf) is one of the last commonly available sensors in a TO-220 package.

**This type of temperature sensor is one of the easiest to interface with a microcontroller in an embedded system**, since the output can be directly connected to an ADC input, voltage read, and then converted into a temperature by a simple linear equation.  They usually output a change of 10 or 19.5mV per degree Celsius, which provides 1bit per degree on a 8-bit ADC with a reference voltage of either 2.5V or 5.0V respectively.

**DESIGN TIP:** When looking at the accuracy, be careful, as they usually advertise the typical accuracy, but it is normally the worst case accuracy that is more important to the PCB designer. Sometimes the stated accuracy is only achievable after calibration.