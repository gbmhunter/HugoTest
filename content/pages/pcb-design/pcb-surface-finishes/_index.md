---
author: gbmhunter
date: 2015-10-06 03:35:21+00:00
draft: false
title: PCB Surface Finishes
type: page
url: /pcb-design/pcb-surface-finishes
---

# Overview

The following surface finishes are listed in order of increasing price/performance.

# Hot Air Solder Leveled (HASL)

HASL is one of the most widely used surface finishes. It involves dipping the circuit board into a pot of molten solder, taking it out, and then removing the excess solder with a set of "air knives".

[caption id="attachment_12112" align="aligncenter" width="463"][![An example of a PCB with a HASL surface finish. Image from http://www.pcbsourcing.com/.](/images/2015/10/hasl-pcb-surface-finish-example.jpg)
](/images/2015/10/hasl-pcb-surface-finish-example.jpg) An example of a PCB with a HASL surface finish. Image from http://www.pcbsourcing.com/.[/caption]

**Pros:**  * Cheap  * Tough  * Re-workable

**Cons:**  * Uneven surface  * Thermally shocks the PCB (decreased reliability)  * Plugs (or partially plugs) plated through-holes

HASL used to be the de-facto surface finish for most PCB's. As component footprint has shrunk, the limitations of HASL have begun to cause serious issues.

The major issue is the uneven surface that HASL provides. With 0.5-0.8mm pitch QFN and BGA components, this irregular solder deposit can bridge pads and create shorts.

The thermal shock from dipping the PCB into a pool of molten solder can damage tiny vias and tracks, even causing a via to crack. This may result in the board working fine at room temperatures, but failing at -10°C as the metal in the via contracts.

# Immersion Tin (ISn)

Immersion tin is

[caption id="attachment_12115" align="aligncenter" width="890"][![Example of an immersion tin (ISn) PCB surface finish. Image from http://www.standardpcb.com/.](/images/2015/10/example-of-immersion-tin-surface-finish-on-pcb.jpg)
](/images/2015/10/example-of-immersion-tin-surface-finish-on-pcb.jpg) Example of an immersion tin (ISn) PCB surface finish. Image from http://www.standardpcb.com/.[/caption]

**Pros**  * Relatively cheap, but more expensive than HASL  * Flat surface  * No lead (RoHS compliant)  * Re-workable

**Cons**  * Short shelf-life (3-6 months)

The biggest issue with ISn is that the copper and tin layers slowly diffuse into one another over time. This creates "tin wiskers", and limits the shelf-life of ISn PCB's (before soldering) to about 3-6 months.

# Immersion Silver (IAg)

Immersion silver is good alternative to ENIG.

[caption id="attachment_12110" align="aligncenter" width="600"][![Example of an immersion silver (IAg) PCB finish. Image from http://www.rlcinnovation.com/.](/images/2015/10/pcb-surface-finish-immersion-silver.jpg)
](/images/2015/10/pcb-surface-finish-immersion-silver.jpg) Example of an immersion silver (IAg) PCB finish. Image from http://www.rlcinnovation.com/.[/caption]

**Pros**  * Precise  * Only requires one plating procedure (compared to ENIG)

**Cons**  * Moderately expensive  * Finger-grease and solvents can cause wetting problems  * Gets attacked in acidic and sulphur environments

PCB's plated with IAg must not be handled directly or cleaned with a solvent prior to soldering, as finger-grease and solvents can cause wetting problems.

# Electroless Nickel Immersion Gold (ENIG)

ENIG is becoming more and more popular as component package pitch sizes drop, and RoHS regulation becomes more common place.

[caption id="attachment_12116" align="aligncenter" width="1557"][![Example of an immersion gold PCB surface finish. Image from http://www.standardpcb.com/.](/images/2015/10/example-of-immersion-gold-pcb-surface-finish.jpg)
](/images/2015/10/example-of-immersion-gold-pcb-surface-finish.jpg) Example of an immersion gold PCB surface finish. Image from http://www.standardpcb.com/.[/caption]

**Pros**  * Very high shelf-life  * Good for PCB fingers  * Good for RF shield connections

**Cons**  * More expensive than immersion silver  * Requires to plating procedures (nickel, then gold)

# Immersion vs. Electro-less Platings

Immersion platings rely on a chemical displacement reaction of the surface of the PCB copper with a more noble metal that is in solution. Remember back to school chemistry in where iron nails where placed in a copper sulphate solution, and after a while the nail would be covered in copper?

Immersion platings are very thin (once the surface is covered, the reaction stops), and don't have great adhesion.

Electro-less platings use auto-catalytic platings.