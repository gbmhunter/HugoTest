---
author: gbmhunter
categories: [ "Electronics", "Circuit Design" ]
date: 2013-08-02
draft: false
tags: [ "button", "debouncing", "hardware", "firmware", "schematic" ]
title: Debouncing
type: page
---

## Overview

Debouncing is the technique of detecting and removing multiple state changes from a hardware device (most commonly a push-button switch) caused when the mechanical contacts touch. Because of tiny imperfections in switch contacts, as the contacts come together and make a conductive circuit, the actual resistance jumps up and down multiple times in quick succession (this is the bouncing). Although the human eye cannot see this when a light is turned on in a house, this bouncing can cause problems for logic which is expecting a single state tradition (e.g. a microcontroller which is counting button presses).

{{< img src="button-press-needs-debouncing.jpg" width="440px" caption="A digitalized output of a button press, which needs debouncing."  >}}

## Hardware Debouncing

A schmitt trigger can be used to avoid "grey areas" of digital logic.

## Firmware Debouncing

Another way to debounce inputs is to use firmware. Assuming the button is connected to the input of a microcontroller, it is normally simpler, cheaper, and easier to do the debouncing in firmware than hardware.

## External Resources

[The Ganssle group, A Guide To Debouncing](http://www.ganssle.com/debouncing.pdf), is an awesome, in-depth investigation into switch debouncing. If you are reading up on this topic, it is a must see!