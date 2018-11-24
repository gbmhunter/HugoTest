---
author: gbmhunter
date: 2013-09-05 22:19:08+00:00
draft: false
title: How To Route A PSoC Microcontroller
type: page
url: /programming/microcontrollers/psoc/how-to-route-a-psoc-microcontroller
---

# SIO Pins

SIO pins can:  * Act as digital I/O  * Can handle up to 5.5V on SIO pins, regardless of the microcontrollers maximum supply voltage (this is due to no top ESD diode).  * Sink/source more current than GPIO  * Can have programmable drive voltage levels

SIO pins cannot:  * Act as analogue I/O. This means you cannot connect them up things like the ADC, VDAC, IDAC, e.t.c.  * Cannot act as LCD I/O.

Some SIO pins also have fixed-hardware I2C peripherals connected to them. In my experience, SIO pins also tend to use a little more power than GPIO, it seems that their input buffers consume more current.

[caption id="attachment_5144" align="aligncenter" width="631"][![Information on the SIO pins from a PSoC datasheet.](/images/2013/09/additional-features-only-provided-on-sio-pins.png)
](/images/2013/09/additional-features-only-provided-on-sio-pins.png) Information on the SIO pins from a PSoC datasheet.[/caption]