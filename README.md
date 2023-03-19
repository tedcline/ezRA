# ezRA - Easy Radio Astronomy

<p align="center">
  <img src="/ezRA/ezRA_logo.jpg?raw=true" alt="ezRA_logo"/>
</p>

The ezRA Easy Radio Astronomy set of programs are free PC tools to help folks beginning to explore Radio Astronomy, with 
1420 MHz Galactic hydrogen data collection and analysis.
The open source programs run on the Python3 programming language, on Windows and Linux.

The ezRA set of programs are still in development, but mostly work well.

Interested folks on [GitHub](https://github.com/tedcline/ezRA)
would left-click on the top right Green "Code" button and probably choose "Download ZIP"
(about 30 MBytes, probably as "ezRA-master.zip" into your local "Downloads" directory).

=============================================

ezRA documentation has many images.
Rather than duplicate those image bytes here in an online README.md file,
please see these introductory PDFs from the ezRA directory:

* "Sales Brochure" showing what ezRA can do:<br>
[ezRA_01_Tour.pdf](https://github.com/tedcline/ezRA/blob/master/ezRA/ezRA_01_Tour.pdf)<br>

* Quick overview of programs and documentation:<br>
[ezRA_00_Introduction.pdf](https://github.com/tedcline/ezRA/blob/master/ezRA/ezRA_00_Introduction.pdf)<br>

=============================================

## There are 5 major ezRA programs:

	ezCol - COLlect radio signals into integrated frequency spectrum ezRA .txt data files.

		Or convert previous radio data with ezColBAA, ezColHay, ezColIFAvg,
		ezColSc, etc.

		ezFix - remove or separate samples, combine, edit, and split frequency spectrum
		ezRA .txt data files.

	ezCon - CONdense one or more frequency spectrum data .txt files into
		one .ezb text data file, and perhaps one Galaxy crossing spectra *Gal.npz data file.

	ezPlot - PLOT analysis from one or more .ezb condensed data files.

	ezSky - SKY maps from one or more .ezb condensed data files.

	ezGal - GALaxy plots from one or more spectra *Gal.npz data files (Galaxy rotation,
		Velocity vs Galactic Longitude, Galaxy arm plots?).



## Documentation for ezRA, in the ezRA directory, will eventually include:

    ezRA_00_Introduction.pdf
    ezRA_01_Tour.pdf
    ezRA_05_Demonstration.pdf

    ezRA_10_Hardware_1.pdf
    ezRA_11_Hardware_2.pdf

    ezRA_20a_Software.pdf
    ezRA_20b_Windows_Install.pdf
    ezRA_20c_Linux_Install.pdf
    ezRA_21a_ezCol.pdf
        ezRA_21d_ezColBAA.pdf
        ezRA_21c_ezColHay.pdf
        ezRA_21b_ezColIFAvg.pdf
        ezRA_21e_ezColSC.pdf
        ezRA_21y_ezRename.pdf
        ezRA_21z_ezFix.pdf
    ezRA_22_ezCon.pdf
    ezRA_23_ezPlot.pdf
    ezRA_24_ezSky.pdf
    ezRA_25_ezGal.pdf


## Videos:

* [https://www.youtube.com/@TedCline/videos](https://www.youtube.com/@TedCline/videos)<br>
* [https://www.youtube.com/@radio-astronomy](https://www.youtube.com/@radio-astronomy)<br>

---


## Status:

    ezCon's default "-ezConAstroMath  2" now calculates the   correct   VLSR values.

Known bugs:

    ezCon's "-ezConAstroMath  1" did calculate wrong Right Ascension values.
	Now fixed ?  Does it work for your earth location ?  10x faster !
    ezCon's default still is the slower "-ezConAstroMath  2".

Thanks to Todd Ullery, the  ezColX.py  was an experimental multiple process version of  ezCol.py , to improve dashboard responsiveness.
<br>
Problems ?  Graphic dashboard more responsive ?  Faster ?
<br>
The experiment has completed successfully, ezColX is now named ezCol, and the name ezColX is retired.

These files need lots of cleanup, but should work or be helpful:

    ezColBAA.py
    ezColHay.py
    ezColIFAvg.py
    ezColSc.py

Always need more documentation.

--

Comments are encouraged !

Help improve ezRA.

--

TedClineGit@gmail.com
<br>
Mar-18-2023

---
