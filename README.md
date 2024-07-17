# ezRA - Easy Radio Astronomy

<p align="center">
  <img src="/ezRA/doc/ezRA_logo.jpg?raw=true" alt="ezRA_logo"/>
</p>

The ezRA Easy Radio Astronomy set of programs are free PC tools to help folks beginning to explore Radio Astronomy, with 
1420 MHz Galactic hydrogen data collection and analysis.
The open source programs run on the Python3 programming language, on Windows and Linux.

The ezRA set of programs are still in development, but mostly work well.

Interested folks on [GitHub](https://github.com/tedcline/ezRA)
would left-click on the top right Green "Code" button and probably choose "Download ZIP"
(about 30 MBytes, probably as "ezRA-master.zip" into your local "Downloads" directory).
Then start exploring the many PDF files in your  ezRA/doc  directory.
Also the videos listed below.

=============================================

ezRA documentation has many images.
Rather than duplicate those image bytes here in an online README.md file,
please see these introductory PDFs from the ezRA directory:

* "System Tour" showing what ezRA can do:<br>
[ezRA_01_Tour.pdf](https://github.com/tedcline/ezRA/blob/master/ezRA/doc/ezRA_01_Tour.pdf)<br>

* Quick overview of programs and documentation:<br>
[ezRA_00_Introduction.pdf](https://github.com/tedcline/ezRA/blob/master/ezRA/doc/ezRA_00_Introduction.pdf)<br>

Or perhaps start with these 2 introductory videos (from the longer list of videos below):

* [ezRA - Simple Overview (13 minutes)](https://youtu.be/kHgwEbWKhzs)<br>
* [ezRA - PZT Antenna Tests (31 minutes)](https://youtu.be/VZrd2-VFiPE)

=============================================

## There are 6 major ezRA programs:

* ezCol - COLlect radio signals into integrated frequency spectrum ezRA .txt data files.

  * Or convert previous radio data with ezColBAA, ezColHay, ezColIFAvg, ezColSc, etc.

  * ezFix - remove or separate samples, combine, edit, and split frequency spectrum ezRA .txt data files.

* ezCon - CONdense one or more frequency spectrum data .txt files into one .ezb text data file, and perhaps one Galaxy crossing spectra *Gal.npz data file.

* ezPlot - PLOT analysis from one or more .ezb condensed data files.

* ezSky - SKY maps from one or more .ezb condensed data files.

* ezGal - GALaxy plots from one or more spectra *Gal.npz data files (centered on one Galactic Latitude: Galaxy rotation, Galaxy mass,
Velocity vs Galactic Longitude, Galaxy arm plots).

* ezGLon - Galaxy LONgitude plots from one or more spectra *GLon.npz data files (centered on one Galactic Longitude: Galaxy arm cross-section plots).

## Videos:

[https://www.youtube.com/@TedCline/videos](https://www.youtube.com/@TedCline/videos)<br>

  * [ezRA - Simple Overview  (13 minutes)](https://youtu.be/kHgwEbWKhzs)<br>
  * [ezRA - PZT Antenna Tests  (31 minutes)](https://youtu.be/VZrd2-VFiPE)

<br>

  * [Pablo 1 - ezRA Installation on Windows](https://www.youtube.com/watch?v=2DbS5A42OJQ)<br>
  * [Pablo 2 - ezCol with USB Relay Control of LNA Resistor](https://www.youtube.com/watch?v=N1TRyJ9w0As)<br>
  * [Pablo 3 - ezCon Plot Tour](https://www.youtube.com/watch?v=8EUmCQAIBLg)<br>
  * [Pablo 4 - ezCol Data Collecting Software in Action](https://www.youtube.com/watch?v=15Q6_OCDTs0)
<br>

  * [ezRA Analysis 1 - Introduction, Data Collectors](https://youtu.be/2TWXiAUpgCc)<br>
  * [ezRA Analysis 2 - Spreadsheet Analysis](https://youtu.be/9vKaob-jweM)<br>
  * [ezRA Analysis 3 - Signal Progression](https://youtu.be/7c-0rbNOOV4)<br>
  * [ezRA Analysis 4 - More Plots and .ezb File](https://youtu.be/bpU1wYJJrO4)<br>
  * [ezRA Analysis 5 - Interference Filters](https://youtu.be/XAitkAerXjM)<br>
  * [ezRA Analysis 6 - ezSky](https://youtu.be/dj3_jikH59Y)<br>
  * [ezRA Analysis 7 - AntXTVT and VLSR](https://youtu.be/038Apm0yAjY)<br>
  * [ezRA Analysis 8 - ezGal](https://youtu.be/YXuPDJVRbd0)

Society of Amateur Radio Astronomers (SARA) [https://www.youtube.com/@radio-astronomy](https://www.youtube.com/@radio-astronomy)<br>

## Documentation for ezRA, in the ezRA/doc directory, will eventually include:

  * ezRA_00_Introduction.pdf
  * ezRA_01_Tour.pdf
  * ezRA_05_Demonstration.pdf<br><br>
  * ezRA_10_Hardware_1.pdf
  * ezRA_11_Hardware_2.pdf<br><br>
  * ezRA_20a_Software.pdf
  * ezRA_20b_Windows_Install.pdf
  * ezRA_20c_Linux_Install.pdf
  * ezRA_21a_ezCol.pdf
    * ezRA_21d_ezColBAA.pdf
    * ezRA_21c_ezColHay.pdf
    * ezRA_21b_ezColIFAvg.pdf
    * ezRA_21e_ezColSC.pdf
    * ezRA_21y_ezRename.pdf
    * ezRA_21z_ezFix.pdf
  * ezRA_22_ezCon.pdf
  * ezRA_23_ezPlot.pdf
  * ezRA_24_ezSky.pdf
  * ezRA_25_ezGal.pdf
  * ezRA_26_ezGLon.pdf

---

## Status:

  * ezSky's ezSkyXYLimL allows zoomed interpolated plots of the sky.
  * ezCol and ezCon now support RaDec and Galactic sky tracking (but no motor control).
  * ezCon's default is now the faster "-ezConAstroMath  1".

Thanks to Todd Ullery, the  ezColX.py  was an experimental multiple process version of  ezCol.py , to improve dashboard responsiveness.
<br>
The experiment has completed successfully, ezColX is now named ezCol, and the name ezColX is retired.

These data converter programs need lots of cleanup, but should work or be helpful:

  * ezColBAA.py
  * ezColHay.py
  * ezColIFAvg.py
  * ezColSc.py

Always need more documentation.

--

Did ezRA work for you ?

<p align="center">
  <img src="/ezRA/doc/ezRA_users240616.png?raw=true" alt="ezRA_users240616"/>
</p>

Comments are encouraged !

Help improve ezRA.

--

TedClineGit@gmail.com
<br>
Jul-16-2024

(World Map by juicy_fish on Freepik.com)

---
