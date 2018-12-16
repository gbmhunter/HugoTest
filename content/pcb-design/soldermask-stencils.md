---
author: gbmhunter
date: 2014-07-23 23:14:49+00:00
draft: false
title: Soldermask Stencils
type: page
url: /pcb-design/soldermask-stencils
---

# Overview

PCB stencils help you apply solder paste and a quick and even manner to a PCB during the reflow soldering process. They are usually made from either a sheet of stainless steel (for large manufacturing runs) or a plastic/wax paper (for cheap one off prototypes).

{{< figure src="/images/2014/07/soldermask-example-stainless-steel-soldermask-dot-com.jpg" width="300px" caption="An example of a stainless steel soldermask stencil. Image from http://www.soldermask.com/."  >}}

The sheet has apertures cut out of it in all places on the PCB in where you want solder paste to be applied. The stencil is placed on the surface of the PCB and solderpaste applied. The thickness of the stencil determines the paste density (how much paste will be applied for a given area).

PCB stencils are usually created from the same design files that are used to manufacture the PCB. If using the [Gerber format](/pcb-design/pcb-data-formats#gerber-files), the Top Paste (.GTP) and Bottom Paste (.GBP) files will be used.

# Etching Processes

## Chemical

Chemically etched stencils are usually produced from an etchable grade of stainless steel. They are cheaper to manufacture than laser cut stencils (when both are made from stainless steel). Since etching is carried out from both sides of the stencil, the process can create a waist within the aperture. This can be removed somewhat by polishing.

The resist openings are made smaller than the final desired aperture size because the chemical **undercuts** the sides of the aperture to some degree. This produces rounded corners which is a characteristic of chemically-etched stencils.

## Laser Cut

Both stainless steel and wax-paper stencils can be laser cut. A tougher grade of stainless steel can be used than with chemical etching.

The aperture wall surface is rougher with laser cut stencils due to the melting effect of the laser.

# Stencil Thickness

Typical thickness include 0.12mm and 0.15mm. 0.10mm thick stainless steel can be quite floppy in unframed A4-sized or larger sheets.

# Aspect Ratio

The aspect ratio of a particular aperture is the ratio beteen the width of an aperture and the thickness of the stencil.

<div>$$ R = \frac{W}{T} $$</div>

For a particular stencil, this ratio should never be smaller than a particular number. This is commonly 1 or 1.5.

# Aperture Size

The rule:

<div>$$ R = \frac{LW}{2(L+W)T} $$</div>

This ratio should always be greater or equal to 0.66.

{{< figure src="/images/2014/07/pcb-stencil-aspect-and-area-ratio-illustration.png" width="877px" caption="Diagram explaining the aspect and area ratios of PCB stencils. Image from http://www.ti.com/lit/an/slua271a/slua271a.pdf."  >}}

# Prices

The price for a single stainless steel stencil for prototype use is normally in the range of US$20 to US$130, depending on the method used to cut the holes.

# Stepped Stencils

Sometimes different paste densities are required for different components. Stencils with varying thickness can be produced by using a combination of chemical and laser etching. These are called **stepped stencils**.

# Art?

What to do with a stencil once you have finished making PCBs with it? Do stencils have the potential to be art pieces? I did attach a back light and diffuser to one and made a wall-mountable piece of art, see the [Backlit PCB Stencil project](/electronics/projects/backlit-pcb-stencil) for more information.