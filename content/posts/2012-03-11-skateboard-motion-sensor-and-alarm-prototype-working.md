---
author: gbmhunter
date: 2012-03-11 04:18:09+00:00
draft: false
title: Skateboard Motion Sensor And Alarm Prototype Working
type: post
url: /electronics/electronics-electric-skateboard/skateboard-motion-sensor-and-alarm-prototype-working
categories:
- Electric Skateboard
tags:
- alarm
- bjt
- electric skateboard
- full-bridge
- motion sensor
- psoc
---

[singlepic id=508 w=250 h=240 float=right]

The motion sensor and alarm is now working! This would of had to been the easiest part of the circuits to get working. Everything just worked, first time (so did the software, and big part due to the PSoC's easy to use drag'n'drop hardware blocks and configurations tools.



I found this cool little motion sensor, the MS24 on Element14 for less than NZ$10. It's heaps better than most tilt sensors since it is sensitive to motion in all orientations, unlike tilt sensors which tend to only change state at a specific angle from the horizontal.

[singlepic id=513 w=250 h=240 float=right]

The sensor is normally closed, but when a small amount of motion disturbs it, it momentarily goes into the open state. All you need is a resistor and capacitor to interface this into a microcontrollers interrupt pin. The combination of the resistor and capacitor control the sensitivity.



I made a simple BJT full-bridge to control a speaker (or peizo) at 12V from the microcontrollers PWM outputs (the PSoC allows you to configure one PWM module to have two outputs, each the inverse of the other, all in the GUI!).

For the prototype, the motion sensor triggers an interrupt on the micro, which then enables the PWM, changing the frequency every 500ms to create an alarm sound.

[singlepic id=515 w=250 h=240 float=right]

Here's a little video showing how it works. Note that I had the motion sensor on maximum sensitivity (aka no capacitor), hence how a little table vibration sets it off, which is quite impressive!

[youtube=http://www.youtube.com/watch?v=cKx7CbwUe6E]