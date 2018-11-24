---
author: gbmhunter
date: 2016-06-28 05:59:45+00:00
draft: false
title: Off-line Switchers
type: page
url: /electronics/components/power-regulators/off-line-switchers
---

# Overview

Off-line switchers convert a usually high AC input voltage (e.g. 240VAC mains supply) down to a IC level DC voltage (e.g. 5V). Their design is based on a _flyback regulator_ circuit. 

# Terminology

The term "_off-line switchers_" comes from the fact that the DC output voltage is derived straight from the AC input (the DC voltage comes straight "off" the line (AC)). 

IMHO, this was a **bad name choice**, as many people would assume it is related to being offline (disconnected), rather than online. Remember back to when dot-matrix printers had a "online" LED?

# Isolation

Both isolated and non-isolated off-line switchers exist on the market.

[caption id="attachment_13624" align="aligncenter" width="651"][![Schematic of a isolated off-line switcher by TI. Image from http://www.ti.com.](/images/2016/06/offline-switcher-complete-isolated-flyback-switching-supply-schematic-ti.png)
](/images/2016/06/offline-switcher-complete-isolated-flyback-switching-supply-schematic-ti.png) Schematic of a isolated off-line switcher by TI. Image from http://www.ti.com.[/caption]

And here is an example of a non-isolated version:

[caption id="attachment_13625" align="aligncenter" width="625"][![A typical application schematic for the LinkSwitch-TN family of non-isolated off-line switchers by Power Integrations. Image from www.power.com.](/images/2016/06/offline-switcher-linkswitch-tn-typical-application-schematic.pdf.png)
](/images/2016/06/offline-switcher-linkswitch-tn-typical-application-schematic.pdf.png) A typical application schematic for the LinkSwitch-TN family of non-isolated off-line switchers by Power Integrations. Image from www.power.com.[/caption]