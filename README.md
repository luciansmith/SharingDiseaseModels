Sharing Disease Models
=======================
This repository consist of several files implementing very simple disease models to show sharing capabilities of disease models. The models are implemented in  PharmML, The MIcroSumlation Tool (MIST), and the SBML tools Tellurium using antimony and Rule Bender using BioNetGen.
These examples are supporting the SummerSim 2016 paper titled: "Disease Model Sharing Formats".


FILES:
------
* README.md - is the file you are reading now
* License.txt - GPL version 3 license file

### Representations of Example 1 - Simple Markov Model in paper section 2.2
* categorical_MARKOV1.xml: PharmML format
* Example1.bngl: Rule Bender using BioNetGen implementation 
* Example1.py: Tellurium using antimony implementation 
* Example1.xml: SBML XML file
* Example1.zip: MIST implementation 

### Representations of Example 2 - Three State Markov Model in paper section 2.3
* categorical_MARKOV2.xml: PharmML format
* Example2.bngl: Rule Bender using BioNetGen implementation 
* Example2.py: Tellurium using antimony implementation 
* Example2.xml: SBML XML file
* Example2.zip: MIST implementation 

### Representations of Example 3 - Stratified Markov Model in paper section 2.4
* categorical_MARKOV3.xml: PharmML format
* Example3.bngl: Rule Bender using BioNetGen implementation 
* Example3.py: Tellurium using antimony implementation 
* Example3.xml: SBML XML file
* Example3.zip: MIST implementation 


USAGE:
------
Each file uses a different system and format. To run some of the files to reproduce paper results specific tools are required:
The following tools and versions were used to generate the results in this paper on a Windows 7 (64 bit) machine:
* MIST Version 0.92.0.0 using Python 2.7.11 | Anaconda 2.4.1 (64-bit)  - Install from: https://github.com/Jacob-Barhak/MIST
* RuleBender-2.0.382r3-win32 using BioNetGen-2.2.6 - Install from: http://bionetgen.org/index.php/Download
* Tellurium Version:  1.2.4, RoadRunner version: 1.4.0; Compiler: Microsoft Visual Studio 2013, C++ version: 199711; JIT Compiler: LLVM-3.5; Date: Oct  6 2015, 17:30:09, Antimony version: v2.8.0 - Install from: http://tellurium.analogmachine.org/stuff/



VERSION HISTORY:
----------------
Development started after discussion on 22-Sep-2015.
Uploaded to Github on 8-March-2016 - no version number assigned
Modifed on 16-March-2016 after paper review by Richard Smith? by Lucian and Jacob to get nicer plots


DEVELOPER CONTACT INFO:
-----------------------

Please pass questions according to format to:

### SBML
Lucian Smith
lpsmith@uw.edu

### PharmML
Maciej J. Swat
maciej.swat@gmail.com

### MIST
Jacob Barhak Ph.D.
Email: jacob.barhak@gmail.com
http://sites.google.com/site/jacobbarhak/



ACKNOWLEDGEMENTS:
-----------------
Thanks to discussers in the SBML and DDMoRe discussion lists: Robert Phair, Lukas Endler, Gareth Smith, Nicolas Le Novere, Jose Juan Tapia, Jim Sluka, Leonard Harris, Fengkai Zhang, Nick Holford, Mike K Smith, Sarah Keating, Herbert Sauro, Michael Hucka, Kyle Medley.
This work used the MIcro Simulation Tool (MIST) that is based on IEST. The IEST GPL disease modeling framework was initially supported by the Biostatistics and Economic Modeling Core of the MDRTC (P60DK020572) and by the Methods and Measurement Core of the MCDTR (P30DK092926), both funded by the National Institute of Diabetes and Digestive and Kidney Diseases. The modeling framework was initially defined as GPL and was funded by Chronic Disease Modeling for Clinical Research Innovations grant (R21DK075077) from the same institute. MIST, however, was developed without financial support.
Additional thanks to Richard Smith? for his review: https://groups.google.com/forum/#!topic/public-scientific-reviews/8SCxed6KhlU




LICENSE
-------

Copyright (C) 2015 Jacob Barhak, Maciej J. Swat, Lucian Smith
 
This file is part of "Sharing Disease Models". "Sharing Disease Models" is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

"Sharing Disease Models" is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
