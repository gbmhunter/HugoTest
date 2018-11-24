---
author: gbmhunter
date: 2015-11-30 22:30:48+00:00
draft: false
title: Terminal Blocks
type: page
url: /electronics/components/connectors/terminal-blocks
---

# Overview

Terminal blocks are a great easy-to-use connection method for signal from mA right up to 10A+. They make it **easy to connect (and re-arrange)** wires, accept one of the largest ranges of wire sizes, and the standard screw type requires no crimp on the end of the wire. They are also great because they** allow the cable itself to be fed through glands and other small orifices**, as there is no mating connector permanently mounted onto the end of the cable.

There are different types of terminal blocks:

<table ><tbody ><tr >
<td style="width: 100px;" >One piece
</td>
<td >These are your standard terminal blocks that are soldered onto PCBs.
</td></tr><tr >
<td >Feed-through
</td>
<td >Rather than connecting to a PCB, these provide mechanical contacts on both sides of the terminal block, allowing wires to be connected together. Popular with mains (household) wiring.
</td></tr><tr >
<td >Pluggable
</td>
<td >These are like on-piece, except that the PCB part and the wire part are plugged into each other, so that they can be separated.
</td></tr><tr >
<td >Barrier
</td>
<td >These provide electrical isolation.
</td></tr></tbody></table>

You can see the push-in terminal blocks I used to connect up all the solenoids for the [Luxcity Tonic project](http://blog.mbedded.ninja/electronics/projects/luxcity-uv-tonic-control-system) in the image below (the green things with numbered stickers and wires coming out of them).

[caption id="attachment_12746" align="aligncenter" width="1200"][![The Arduino, the relay shields and the relays, set-up for testing.](/images/2015/12/arduino-relay-shields-and-relays.jpg)
](/images/2015/12/arduino-relay-shields-and-relays.jpg) The Arduino, the relay shields and the relays, set-up for testing.[/caption]

However, because they do not enforce a specific wiring configuration, they are prone to wiring errors, especially if someone else than that who designed the circuit is wiring it up.

Common pitches for terminal blocks are:

<table ><tbody ><tr >PitchUse</tr><tr >
<td style="width: 100px;" >2.54mm (100mill)
</td>
<td >Imperial pitch used for small wires (16-30AWG). While this is a very common pitch for other connectors, the design of terminal blocks actually makes this result in very small connections, hence larger pitches are more popular.
</td></tr><tr >
<td >3.5mm
</td>
<td >This is a metric pitch.
</td></tr><tr >
<td >3.84mm (150mill)
</td>
<td >This is a common terminal block imperial pitch
</td></tr><tr >
<td >5.08mm (200mill)
</td>
<td >This is a very common imperial pitch.
</td></tr></tbody></table>

A word of caution: **DO NOT** completely tin the ends of wires that go in the terminal block. Under the pressure of the screw, solder will creep over time, and the connection will become loose, either falling out, or making a high resistance connection. It is acceptable to lightly tin **the very ends** of the wires to keep the individual strands from fraying, but nothing more.

A better way to fix this problem is to use wire ferrules. These are small hollow metal cylinder which just fit over the wire and then crimped onto it, before being inserted into the terminal block. It stops the wires from fraying, and gets rid of the solder creep problem.

[caption id="attachment_12748" align="aligncenter" width="928"][![Wire ferrule are crimped onto wires before they are inserted into a terminal block, preventing fraying and solder creep.](/images/2015/12/wire-ferrules-used-in-terminal-block.jpg)
](/images/2015/12/wire-ferrules-used-in-terminal-block.jpg) Wire ferrule are crimped onto wires before they are inserted into a terminal block, preventing fraying and solder creep.[/caption]

# Connection Type

Terminal blocks have many different connection types:

<table ><tr >
<td style="width: 100px;" >Connection Type
</td>
<td >Image
</td>
<td >Description
</td></tr><tbody ><tr >
<td >Screw
</td>
<td >[caption id="attachment_8743" align="aligncenter" width="181"][![A terminal block with a screw-style connection method.](/images/2011/09/terminal-block-screw-style.jpg)
](/images/2011/09/terminal-block-screw-style.jpg) A terminal block with a screw-style connection method.[/caption]
</td>
<td >The most basic terminal block connection type. I don't particularly like this connection style, especially when clamping bare wires (i.e. no wire ferrule), as the screw can pinch and break the individual wire strands, as well as the screw completely missing some/all of the wire strands if they ride up the sides of the metal enclosure. This problem is exasperated when the gauge of the wire is small compared to the size of the terminal block.
</td></tr><tr >
<td >Rising Cage
</td>
<td >[caption id="attachment_8740" align="aligncenter" width="148"][![A terminal block with a rising-cage style connection method.](/images/2011/09/terminal-block-rising-cage-close-up.jpg)
](/images/2011/09/terminal-block-rising-cage-close-up.jpg) A terminal block with a rising-cage style connection method.[/caption]
</td>
<td >Screw with rising cage clamp is my preferred connection type. This is where the bottom side of a square cage rises up and clamps the wire when you tighten the screw. This does not pinch and break the wire as often as the basic screw connection type terminal block does.
</td></tr><tr >
<td >Spring
</td>
<td > 
</td>
<td > 
</td></tr></tbody></table>

# Terminal Block Covers

You can purchase terminal block covers, which give further protection to the wires after they have been fixed into the contacts.

Commonly, they clip onto the top of the terminal block and shield the terminal block from objects approaching from overhead.

[caption id="attachment_12428" align="aligncenter" width="210"][![A terminal block cover beside the terminal block.](/images/2011/09/terminal-block-cover-beside-block1.jpg)
](/images/2011/09/terminal-block-cover-beside-block1.jpg) A terminal block cover beside the terminal block.[/caption] [caption id="attachment_12429" align="aligncenter" width="445"][![A terminal block cover mounted onto a terminal block.](/images/2011/09/terminal-block-cover-mounted-on-block.jpg)
](/images/2011/09/terminal-block-cover-mounted-on-block.jpg) A terminal block cover mounted onto a terminal block.[/caption]