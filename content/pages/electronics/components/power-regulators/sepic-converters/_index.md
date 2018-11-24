---
author: gbmhunter
date: 2015-03-24 19:31:39+00:00
draft: false
title: SEPIC Converters
type: page
url: /electronics/components/power-regulators/sepic-converters
---

[mathjax]

# Overview

SEPIC (single-ended primary inductance converter) is a switch-mode power supply (SMPS) which can both up and down-convert, similar to a buck/boost. It can be viewed as a boost converter followed by a buck-boost converter.

[caption id="attachment_11556" align="aligncenter" width="698"][![The basic components of a SEPIC style buck-boost converter.](/images/2015/03/smps-buck-boost-converter-sepic-basic-components.png)
](/images/2015/03/smps-buck-boost-converter-sepic-basic-components.png) The basic components of a SEPIC style buck-boost converter.[/caption]

It is normally recognised both in schematics and on PCBs because of it's use of two inductors. It's advantages over a buck-boost alone is that is has a non-inverted output voltage, DC decouplement from input to out (through a series power-transferring capacitor), which makes it easier to handle things such as short circuits on the output, and true turnoff of the output (when the switch is off, the output truly goes to 0V).

Like other SMPS, the SEPIC converter uses a switching element of control the output. The power transferring capacitor between input and output is sometimes called the **AC capacitor**.

# Output Voltage

In continuous-conduction mode (CCM), the equation linking the input and output voltage of a SEPIC is:

$$ D = \frac{V_{OUT}}{V_{OUT} + V_{IN}} $$

# Inductor(s)

The SEPIC is usually identified by it's two inductors, rather than as most other power converters which use only one. They can either be wound on separate cores and not share any magnetic field (uncoupled inductors), or be wound on the same core and share a magnetic field (a coupled dual-winding inductor). Using a coupled dual-winding inductor has the advantages of reducing the component count, and lowering the total inductance requirements, but can be hard to find for high-power requirements. Coupled inductors used in a SEPIC also benefit from some leakage inductance, which reduces the AC losses.

The equations are different for coupled and un-coupled inductor designs. For a coupled inductor, the equation is:

$$ L = \frac{V_{IN}^2 d_{min}^2}{2f_s P_{OUT(min)}(1 + d_{min}\frac{1 - n}{n})} $$

And for two uncoupled inductors:

$$ L_1 = \frac{d_{min} V_{IN(max)}^2 n}{2f_s P_{OUT(min)}} $$

$$ L_2 = \frac{(1 - d_{min}) V_{OUT}^2}{2f_s P_{OUT(min)}} $$

The above equations determines the minimum inductance required for CCM operation at maximum input voltage and minimum load (the worst-case scenario for a SEPIC).

Even though the equations above show this, it is still worth pointing out that in an decoupled design, the inductances **do not have to be the same value**. This is a common misconception, this rule only applies to the coupled SEPIC design.

# Capacitor

Sometimes the AC capacitor needs a series RC snubber circuit to make the SEPIC stable. A low resistance between 1-10R and a large capacitance between 50-1000uF can sometimes fix this.

# Examples

The LT from Linear Technology can be used in a SEPIC configuration to control a series of high-power LEDs.