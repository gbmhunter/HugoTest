---
author: gbmhunter
date: 2012-03-15 01:04:38+00:00
draft: false
title: LEDs
type: page
url: /electronics/components/diodes/leds
---

[mathjax]

# Overview

There is a neat little [LED Wizard](http://led.linear1.org/led.wiz) from [LED Centre](http://led.linear1.org/) for working out what parallel/series combination of LED's you should use given a certain input voltage and number of LEDs you want in your array.

[caption id="attachment_13722" align="aligncenter" width="242"][![A diffused-lens, red, 5mm through-hole LED.](/images/2012/03/red-led-5mm-th-diffused.jpg)
](/images/2012/03/red-led-5mm-th-diffused.jpg) A diffused-lens, red, 5mm through-hole LED.[/caption]

# Important Parameters

<table border="0" ><tbody ><tr >
<td >**Name**
</td>
<td >**Parameter Symbol**
</td>
<td >**Units**
</td>
<td >**Description**
</td></tr><tr >
<td >Forward Current
</td>
<td >\(I_F\)
</td>
<td >mA
</td>
<td > 
</td></tr><tr >
<td >Forward Surge Current
</td>
<td >\(I_{FM}\)
</td>
<td >mA
</td>
<td >Normally rated at a fixed temperature, duty cycle, and pulse length.
</td></tr><tr >
<td >Forward Voltage
</td>
<td >\(V_F\)
</td>
<td >V
</td>
<td >Rated at a fixed forward current.
</td></tr><tr >
<td >Reverse Voltage
</td>
<td >\(V_R\)
</td>
<td >V
</td>
<td > 
</td></tr><tr >
<td >Dominant Wavelength
</td>
<td >\(\lambda_{dom}\)
</td>
<td >nm
</td>
<td >This is the wavelength which determines the "colour" you see.
</td></tr></tbody></table>

# Limiting The LED Current

A common mistake when working out the value of a current limiting LED resistor is to forget to include the forward voltage drop of the diode into the equations. This has a bigger effect when running the LED at lower voltages. The equation for working out the resistance needed to limit the current in an LED is:

$$R = \frac{V_{dd} - V_{led,f}}{I_{led}}$$

where:  
\(R\) = resistance required in series of LED to limit current,  
\(V_{dd}\) = supply voltage driving the LED (typ. 3.3, 5, 12V)  
\(V_{led,f}\) = forward voltage drop of the led (typ. 2.0V)  
\(I_{led}\) = required current through the led (typ. 5-20mA)

# Reverse Mounting

Reverse mounting LED's are SMD LEDs which have the light source emitting in the reverse direction, e.g. toward the PCB they are mounted on. A hole is drilled in the PCB to let the light through to the other side. They are useful when using a PCB as a user interface panel, or when you want to use light guides (since the light guides can be mounted up against flat PCB).

Note: Be careful when soldering reverse-mount LEDs by hand, it is very easy to push too hard on the LED body and bend the legs!

[caption id="attachment_12653" align="aligncenter" width="440"][![An Osram reverse-mount LED (P47K series).](/images/2012/03/osram-ls-p47k-reverse-mount-led-photo.png)
](/images/2012/03/osram-ls-p47k-reverse-mount-led-photo.png) An Osram reverse-mount LED (P47K series).[/caption]

As of Dec 2015, it is fairly hard to find multi-colour (e.g. bi-colour or RGB) reverse-mount LEDs.

# Multiplexing

Multiplexing is a way of connecting LED's in an arrangement so that it minimises the number of microcontroller pins required to drive them. There is also a even greater pin-saving method, known as Charlieplexing.

Multiplexing is normally done in a row/column configuration, where the LED's are connected in a grid-like fashion, and one microcontroller output pin is used for each row and column. This gives the following equation linking the number of pins used and the number of LEDs:

$$y = (\frac{x}{2})^2$$

where:  
\(y\) = number of LEDs  
\(x\) = number of microcontroller pins

# Charlieplexing

Charlieplexing is a more efficient (in terms of number of drive signals used) way of driving LEDs, compared to multiplexing.

The following equation is given linking the number of pins used and the number of LEDs:

$$y = x^2 - x$$

# ESD

Even though all LEDs are susceptible to ESD damage, it is the GaN based LEDs (blue, white and some green colors) that are more sensitive to surge voltages caused by ESD.

The susceptibility for LEDs to ESD is low enough that no extra ESD protection measures (aside from the current-limiting resistor which acts somewhat as a ESD suppressor also) are taken for LEDs used for general purposes.

# Light Detection With A LED

A little known fact about LEDs is that they can be used for light detection. Although not as sensitive as purpose-built photo-diodes, with a few external components, can be interfaced with a microcontroller and be used to detect variations in the light level.

The schematic below shows how to connect an LED up to a general microcontroller for light detection. The LED and resistor are connected up to GPIO pins.

[caption id="attachment_12654" align="aligncenter" width="502"][![Schematic showing how to connect an LED to a general microcontroller for light detection. The LED and resistor are connected to GPIO pins.](/images/2012/03/led-connected-to-micro-for-light-detection-schematic.png)
](/images/2012/03/led-connected-to-micro-for-light-detection-schematic.png) Schematic showing how to connect an LED to a general microcontroller for light detection. The LED and resistor are connected to GPIO pins.[/caption]

The photocurrent of an LED is about 10-100 times smaller that that of a purpose-built photo-diode. The wavelength of peak sensitivity is usually a little less than the peak wavelength that it emits light at.

# RGB LEDs

RGB LEDs are LED's which have three diodes inside them, one red, one green, and one blue. Whats cool with these is, when controlled correctly, they can produce almost any visible colour (remember primary colours in science class?).

RGB's usually have at least four pins, one each for one side of the red, green, and blue diodes (either all anode or all cathode), and a common which connects all three of the other sides of the diodes. They are more complicated to control than a normal LED, normally requiring 3 different PWM signals, and a bit of firmware to calculate the appropriate duty cycles.

You can get RGD LEDs which already have the control and drive circuitry (e.g. the constant current source) for the LEDs inside them. These are normally connected to a microcontroller via a digital communication bus (e.g. [SPI](http://blog.mbedded.ninja/electronics/circuit-design/communication-protocols/spi-protocol), or sometimes a custom protocol).

One popular example, the WS8211, uses it's own custom communications protocol running at 800kHz.

[caption id="attachment_12655" align="aligncenter" width="498"][![The WS2811, a popular RGD LED, with integrated controller and drive circuitry (constant current supply). Communicates via a custom 800kHz protocol to a microcontroller.](/images/2012/03/ws2811-rgb-led-front-and-back-photo.png)
](/images/2012/03/ws2811-rgb-led-front-and-back-photo.png) The WS2811, a popular RGD LED, with integrated controller and drive circuitry (constant current supply). Communicates via a custom 800kHz protocol to a microcontroller.[/caption]

# LED Controllers

LED controllers are ICs designed specifically to make driving LEDs easier, by providing the correct current for the LEDs to operate and off-loading the processing power which would otherwise have to be done on a microcontroller. They normally allow you to control both the current and the PWM rate for each LED (to control both the brightness and colour). Some are specially designed for RGB LEDs.

Some feature logarithmic current output levels to best match up with what the human eye perceives.

## PWM vs Current Control

There are two main ways to dim an LED, either by changing the current or with PWM. Since PWM only varies how long the LED is on for, and keeps the current through the LED the same, it does not really affect the colour of the LED, while the current-changing method does (the colour depends on the forward current).

## Examples

 

The [PCA9634 8-Channel 25mA I2C LED Controller by NXP](http://www.nxp.com/products/power_management/lighting_driver_and_controller_ics/i2c_led_display_control/series/PCA9634.html) is a simple LED driver for up to 8 single low-power (20mA) LEDs.

# Lens Shapes

LEDs come with a variety of lens shapes. The major thing that the len shapes influences is the **radiant intensity or radiation pattern of the light**. Some lens shapes focus the light around a small angle (e.g. 10°), while others spread the light over nearly 180°.

Most standard LEDs used on circuit boards are either encapsulated or hemispherical.

Hemispherical lens concentrates the light into a tight beam, while the flat and encapsulated lens types spread the light more evenly than an LED with no lens at all.

# Laser Diodes

Laser diodes are LEDs which emits 'lasered' light using a similar method to standard-light LEDs.

Some laser diodes have integrated switching FETs and capacitors for high-speed, high-power applications (such as laser range finding).

[caption id="attachment_12658" align="aligncenter" width="473"][![A laser diode with an integrated FET and capacitor for high-seed, high-power switching.](/images/2012/03/lazer-diode-with-integrated-fet-and-cap.png)
](/images/2012/03/lazer-diode-with-integrated-fet-and-cap.png) A laser diode with an integrated FET and capacitor for high-seed, high-power switching.[/caption]

# Pulse-Width Extending

A common use for an LED is to connect it to a digital output pin of a microcontroller/IC which goes active upon a certain event (say the microcontroller receives a packet of data).

The problem with this is that the length of time that the output pin is active for can be a really short amount of time, e.g. microseconds or even nanoseconds. It the events are rare enough, this may make it impossible to see the LED flicker.

One way to fix this with hardware to to use a simple pulse-width extender circuit as shown below:

[caption id="attachment_12673" align="aligncenter" width="645"][![The schematic for a LED pulse width extending circuit. It converts a short pulse that would not be seen into a longer pulse which is visible.](/images/2012/03/led-pulse-extending-circuit-schematic-annotated-rc-mosfet.png)
](/images/2012/03/led-pulse-extending-circuit-schematic-annotated-rc-mosfet.png) The schematic for a LED pulse width extending circuit. It converts a short pulse that would not be seen into a longer pulse which is visible.[/caption]

This circuit uses an RC network to form a time delay. When the short pulse arrives, the MOSFET is turned on almost immediately, and the LED lights up. When the pulse stops, the diode prevents the capacitor from discharging immediately, and instead has to discharge slowly through the resistor. The MOSFET/LED remain on until the voltage on the capacitor drops below the MOSFET's gate-source threshold voltage (or something close to that).

# Peak vs. Dominant Wavelength

LEDs are usually given with two different quantifiers regarding their wavelength, both the _peak wavelength_ and the _dominant wavelength_.

Most LEDs emit a **narrow spectrum of light** (as opposed to filament-style bulbs, which emit a broad spectrum of light). The **spectral shape is approximately Gaussian** (a.k.a. the normal distribution).

[caption id="attachment_13355" align="aligncenter" width="665"][![A graph of the relative intensity vs. wavelength for a 0603 green LED (LTST-C190KGKT). It has a peak wavelength of 574nm and a dominant wavelength of 571nm.](/images/2012/03/green-led-relative-intensity-vs-wavelength-ltst-c190kgkt.png)
](/images/2012/03/green-led-relative-intensity-vs-wavelength-ltst-c190kgkt.png) A graph of the relative intensity vs. wavelength for a 0603 green LED (LTST-C190KGKT). It has a peak wavelength of 574nm and a dominant wavelength of 571nm.[/caption]

The peak wavelength is the wavelength at the peak of the spectral density curve. The dominant wavelength is a _colorimetric_ quantity that describes the perceived colour of the LED with respect to the human eye. The human eye essentially sees a weighted average of all the wavelengths emitted by the LED, and perceives a single colour based on this averaging.

The dominant wavelength is important for user interface designers as it determines the "colour" the user perceives.

# Packaging

You can get LED's in a variety of SMD packages. Common SMD LED packages include the 0603 on 0402 chip packages.

[caption id="attachment_12652" align="aligncenter" width="1200"][![A picture of a 0603 LED up close on a PCB. You can see the filament running into the middle of the pad (the part which emits the light).](/images/2012/03/0603-led-up-close.jpg)
](/images/2012/03/0603-led-up-close.jpg) A picture of a 0603 LED up close on a PCB. You can see the filament running into the middle of the pad (the part which emits the light).[/caption]