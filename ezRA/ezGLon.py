programName = 'ezGLon241207a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezGLon single Galactic LONgitude explorer program,
#   to read ezCon constant GLon format *GLon.npz condensed data file(s),
#   and optionally create .png plot files.
# https://github.com/tedcline/ezRA

# Copyright (c) 2024, Ted Cline   TedClineGit@gmail.com

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

# TTD:
#       remove many global in main() ?????????
#       plotCountdown, 'plotting' lines only if plotting

# ezGLon241207a, 2 ezGLon580 X,Y,Z extremes to control X,Y,Z autoscaling to value 0.0
# ezGLon241118a, in ezGLon570 and ezGLon571 moved plt.colorbar() to later in case no data to plot
# ezGLon241024a, -ezGLon580CsvFrac
# ezGLon241023b, 'for GLon' into status line
# ezGLon241023a,
# ezGLon241020ax, -ezGLon580Csv and -ezGLon582Csv
#   to create CSV files for 3d colored-dot plots with rinearn.com/en-us/graph3d
# ezGLon231012a, for ezGLon571 and ezGLon581 and ezGLon582 limit GLat plotted to -18 to +19,
#   removed ezGLon582 vertical thin white line
# ezGLon230930a.py, ezGLon510
# ezGLon230824a.py, print ezGlonPlotRangeL in printGoodbye()
# ezGLon230818a.py, ezGlon571galArmsSunMag5 and ezGLon581galArmsSunIMag5
# ezGLon230810ca.py, ezGLon580galArmsSunI with Magnified gLat angle test
# ezGLon230810c.py, ezGLon580galArmsSunI
# ezGLon230810a.py, ezGLon580galArmsSunI
# ezGLon230804a,py, ezGLon510 back to vertical thin lines
# ezGLon230803a,py, ezGLon570 back to ax.set_facecolor("black")
# ezGLon230802b.py, plot grid before data on ezGLon510
# ezGLon230802a.py, plot grid before data on ezGLon510
# ezGLon230701a.py,
# ezGLon230630c.py, remove -ezGLonGalCrossingGLonSpanL,
#   back to -ezGLonGalCrossingGLonCenter and -ezGLonGalCrossingGLonNear
# ezGLon230630b.py, 570 works ?
# ezGLon230630a.py, remove -ezGLonGalCrossingGLonCenter and -ezGLonGalCrossingGLonNear
#   use -ezGLonGalCrossingGLonSpanL,
#   ezGLon510velGLat and ezGLon511velGLatCount work ?
# ezGLon230628a.py, display if GLon.npz file's ezConGalCrossingGLonCenter == ezGLonGalCrossingGLonCenter
# ezGLon230627a.py, require all *GLon.npz files have same
#   ezConGalCrossingGLonNear and ezConGalCrossingGLonCenter
# ezGLon230624a.py, 
# ezGLon230623a.py, 
# ezGLon230608a.py, renamed from ezGalC
# --------------------
# ezGalC230607a.py, renamed to plotEzGalC580galArmsSunI(),
#   Mxxx or Pxxx to titleS and ezGalC510 ezGalC511 and ezGalC580 plot file names 
# ezGalC230604b.py, plotEzGalC510velGLat(), plotEzGalC511velGLatCount(), and plotEzGalC580galArmsSun() work?
# ezGalC230603a.py,
# ezGalC230602a.py,
# ezGalC230601a.py, read many GalC.npz files and plot vertical Galactic Latitude radar for 2 opposite Galactic Longitudes
#   (facing toward one perpendicular Galactic Longitude (0-180), plot "ears" of Sun)
# ------------------
# ezGal230530a.py, create one GalC.npz Combined velocity file like data/2021_333_00p00.0GalC.npz,
#   with multiple GalC.npz files to be read by ezGalC.py
# ezGal230528b.py, remove 'Galaxy plane'
# ezGal230528a.py,
# ezGal230521a.py, renamed highGLonMin to gLonSpurMax
# ezGal230514a.py, 'Sofue 2017 says 1e+11' to plotEzGal560galMass()
# ezGal230512a.py, 'Possible Galactic Atomic Hydrogen', '"Keplerian Rotation"'
# ezGal230511a.py, plotEzGal559planetRot()
# ezGal230509a.py, 
# ezGal230508c.py, changed -ezGalVelGLonEdgeLevelL to velGLonLevel, highGLonMin, velGLonUEdge[gLon=0],
#   findVelGLonEdges() input with -ezGal540edgesUFile and -ezGal540edgesLFile,
#   findVelGLonEdges() writes ezGal540edgesUFileOut.txt and ezGal540edgesLFileOut.txt,
#   due to https://en.wikipedia.org/wiki/Sun, changing 230 km/sec to 220
# ezGal230508b.py, cleanup
# ezGal230508a.py, cleanup, plotEzGal516velGLonAvg() and plotEzGal517velGLonMax(),
#   plotEzGal550galRot() and plotEzGal560galMass() to kiloparsecs
# ezGal230506c.py, improved plotEzGal61XgLonSpectraCascade()
# ezGal230506b.py, comment cleanup
# ezGal230506a.py, cleanup
# ezGal230504b.py, cleanup into plotEzGal570galArmsSun() and plotEzGal580galArmsGC()
#   plotEzGal690gLonDegP180_nnnByFreqBinAvg() to plotEzGal710gLonDegP180_nnnByFreqBinAvg(),
#   plotEzGal520velGLonPolar()  to plotEzGal520velGLonPolarI(),
#       ezGal520velGLonPolarB() to plotEzGal521velGLonPolarD(),
#   plotEzGal521velGLonPolarCount() to plotEzGal525velGLonPolarCount()
# ezGal230504a.py, plotEzGal570galArms1() ezGal580galArms00e.png working
# ezGal230503c.py, plotEzGal570galArms1()
# ezGal230503b.py, plotEzGal570galArms1()
# ezGal230503a.py, plotEzGal570galArms1() ezGal570galArms00d.png working, odd colorbar values
# ezGal230502d.py, plotEzGal570galArms1()
# ezGal230502c.py, plotEzGal570galArms1()
# ezGal230502b.py, plotEzGal570galArms1() ezGal570galArms00d.png closer, with polar
# ezGal230502a.py, plotEzGal570galArms1() ezGal570galArms00d.png closer, but not polar
# ezGal230501a.py, plotEzGal570galArms1()
#   for each of 0-180 degrees, ignore velGLonUEdge[], but using p54 Eq3:
#        galGasRadiusKm = galSunRadiusKm * 230. * np.sin(np.radians(np.arange(91))) \
#            / (230. * np.sin(np.radians(np.arange(91))) + velGLonUEdge[180:180 + 91])   # in km
#   calc p54 Eq4 for each velocityBin[], and plot (with the proper color)
# ezGal230424a.py, plotEzGal570galArms1()
# ezGal230423a.py, plotEzGal570galArms1()
# ezGal230422a.py, plotEzGal570galArms1()
# ezGal230420a.py, plotEzGal570galArms1()
# ezGal230419b.py, plotEzGal570galArms1()
# ezGal230419a.py, plotEzGal570galArms1()
# ezGal230418a.py, plotEzGal570galArms1()
# ezGal230417b.py, plotEzGal570galArms1()
# ezGal230417a.py, plotEzGal570galArms1()
# ezGal230416c.py, plotEzGal570galArms1()
# ezGal230416b.py, plotEzGal570galArms1()
# ezGal230416a.py, plotEzGal570galArms1()
# ezGal230415b.py, plotEzGal570galArms1()
# ezGal230415ax.py, plotEzGal570galArms1()
# ezGal230414a.py, plotEzGal570galArms1(), hide bad velGLonUEdge
# ezGal230413b.py, plotEzGal570galArms1()
# ezGal230413a.py, Quadrant text to ezGalVel520 and ezGalVel521
# ezGal230412a.py, ezGalVelGLonEdgeLevelL
# ezGal230403b.py, ezGal610 with all 4 quadrants
# ezGal230402a.py, fixed plotCountdown
# ezGal230401b.py, 4 quadrants: plotEzGal61XgLonSpectraCascade() 611, 612, 613, 614
# ezGal230401a.py, 4 quadrants: plotEzGal60XgLonSpectra() 601, 602, 603, 604
# ezGal230331a.py, 4 quadrants: plotEzGal70XgLonSpectrums() 701, 702, 703, 704
# ezGal230330a.py, more quadrants - no success
# ezGal230329a.py, more quadrants
# ezGal230328a.py, more quadrants
# ezGal230327a.py, rewrote ezGal540, ezGal541, ezGal550, and ezGal560
# ezGal230325a.py, plotEzGal560galMass()
# ezGal230324a.py, plotEzGal560galMass()
# ezGal230316a.py, -eX, cmdLineArg
# ezGal230311a.py, oops ezGal516 ezGal516 ezGal516 were not finished, commented them out,
#   for ezGal520velGLonPolar.png and ezGal521velGLonPolarCount.png,
#   "MatplotlibDeprecationWarning: Auto-removal of grids by pcolor() and
#   pcolormesh() is deprecated since 3.5 and will be removed two minor releases later;
#   please call grid(False) first.", so put "plt.grid(0)" in front of each "im = plt.pcolormesh(",
#   `scipy.ndimage` not deprecated `scipy.ndimage.filters`,
#   plotCountdown tuning
# ezGal230308a.py, cleanup
# ezGal230305a.py, boilerplate from ezSky
# ezGal230217a.py, add ezGal516velGLonAvg, ezGal517velGLonMax
# ezGal221123a.py, to ezGal690, and to X axis using -byFreqBinX
# ezGal221117a.py, "Galaxy Crossing" to "Galaxy Plane"
# ezGal221117a.py,
#   ezGal530velDecGLon.png to ezGal530galDecGLon.png,
#   ezGal550velGRot_*.png to ezGal550galRot_*.png,
#   ezGal690GLonDegP180_*ByFreqBinAvg.png to ezGal590gLonDegP180_*ByFreqBinAvg.png
# ezGal221017a.py, polishing
# ezGal221016a.py, polishing
# ezGal221013a.py, polishing
# ezGal221012a.py, polishing
# Jul-28-2022a, ezGal10z05b.py,
#   removed warning for missing ezDefaults.txt, ezCon to ezGal, ezVel to ezGal,
#   galGLon to velGLon, velDecP90GLonP180Count to galDecP90GLonP180Count
# ezGal10z05a.py, first try with *Gal.npz input, Jul-15-2022a  N0RQV
#   from "ezVelV7 (2).py"
#   Vel.npz changed to Gal.npz,
#   in ezVel512velGLonPolar plt.pcolormesh() gets shading='auto'
#   in ezVel513velGLonCountPolar plt.pcolormesh() gets shading='auto'
# May- 6-2021a  N0RQV
# ezVelV7.py, added fileObsName to loaded Vel.npz file format for plot titles,
#   fileObsName can be overwritten by optional ezRAObsName argument,
#   commented out unused arguments


import seaborn as sb

import os                       # used to grab all files in the current directory

import sys                

import time
import datetime

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#plt.rcParams['agg.path.chunksize'] = 20000    # to support my many data points

from astropy import units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation
from astropy.coordinates import SkyCoord

import numpy as np

from scipy.interpolate import griddata

import math



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezGLon.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezGLon.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezGLon single Galactic LONgitude explorer program,')
    print('  to read ezCon constant GLon format *GLon.npz condensed data file(s),')
    print('  and optionally create .png plot files.')
    print()
    print('  "radioDataFileDirectories" may be one or more *Gal.npz condensed data text files:')
    print('         py  ezGLon.py  bigDish_N10Gal.npz')
    print('         py  ezGLon.py  bigDish_N10Gal.npz bigDish_P10Gal.npz')
    print('         py  ezGLon.py  bigDish_*Gal.npz')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezGLon.py  .')
    print('         py  ezGLon.py  bigDish2203')
    print('         py  ezGLon.py  bigDish2203 bigDish2204')
    print('         py  ezGLon.py  bigDish22*')
    print('  "radioDataFileDirectories" may be a mix of *Gal.npz condensed data files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezGLon program,')
    print("  then in order from the ezDefaults.txt in the ezGLon.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('    -ezRAObsName         bigDish    (observatory name for plot titles)')
    print()
    print('    -ezGLonPlotRangeL     0  500    (save only this range of ezGLon plots to file, to save time)')
    print('    -ezGLonDispGrid          1      (turn on graphical display plot grids)')
    print()
    print('    -ezGLonGalCrossingGLonCenter   71')
    print('         (center of Galactic Longitude, in degrees)')
    print('    -ezGLonGalCrossingGLonCenterL  70  80  11')
    print('         (adds centers of Galactic Longitude np.linspace(70.0, 80.0, num=11) in degrees)')
    print('    -ezGLonGalCrossingGLonNear     2.1')
    print('         (defines nearness of Galactic Longitude, in degrees, from ezGLonGalCrossingGLonCenter)')
    #print()
    #print('    -ezGLon61XGain           150    (maximum height in ezGLon61XgLonCascade plots)')
    print()
    print('    -ezGLon580Csv             1.3    (create CSV file of ezGLon580 values equal or greater than 1.3,')
    print('                                      for 3d colored-dot plots with rinearn.com/en-us/graph3d)')
    print('    -ezGLon580CsvFrac         0.45   (set ezGLon580Csv as Fraction 0.45 between ezGLon580 colorbar extreme values,')
    print('                                      overrules ezGLon580Csv input, -9999.0 to disable)')
    print('    -ezGLon582Csv             1.3    (create CSV file of ezGLon582 values equal or greater than 1.3,')
    print('                                      for 3d colored-dot plots with rinearn.com/en-us/graph3d)')
    print()
    print('    -ezDefaultsFile ../bigDish8.txt (additional file of ezRA arguments)')
    print()
    print('    -eXXXXXXXXXXXXXXzIgonoreThisWholeOneWord')
    print('         (any one word starting with -eX is ignored, handy for long command line editing)')
    print()
    print()
    print(' programRevision =', programRevision)
    print()
    print()
    print()
    print()
    print()
    print('       The Society of Amateur Radio Astronomers (SARA)')
    print('                    radio-astronomy.org')
    print()
    print()
    print()
    print()
    print()
    print('##############################################################################################')
    print()

    exit()



def printHello():

    global programRevision          # string
    global commandString            # string

    print()
    print('         For help, run')
    print('            ezGLon.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezGLonArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsName                      # string

    global ezGLonDispGrid                   # integer

    global ezGLonGalCrossingGLonCenterL     # float list
    global ezGLonGalCrossingGLonNear        # float

    #global ezGLon61XGain                    # float
    global ezGLon580Csv                     # float
    global ezGLon580CsvFrac                 # float
    global ezGLon582Csv                     # float

    global ezGLonPlotRangeL                 # integer list


    print()
    print('   ezGLonArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileNameInput, 'r')

        # process each line in ezDefaultsFileNameInput
        
        print('      success opening ' + ezDefaultsFileNameInput)

        while 1:
            fileLine = fileDefaults.readline()

            # LF always present: 0=EOF  1=LF  2=1Character
            if not fileLine:              # if end of file
                break                     # get out of while loop

            thisLine = fileLine.split()
            if not thisLine:              # if line all whitespace
                continue                  # skip to next line

            if thisLine[0][0] == '#':    # ignoring whitespace, if first character of first word
                continue                  # it is a comment, skip to next line


            thisLine0Lower = thisLine[0].lower()

            # ezRA arguments used by multiple programs:
            if thisLine0Lower == '-ezRAObsName'.lower():
                ezRAObsName = thisLine[1]
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])


            # integer arguments:
            elif thisLine0Lower == '-ezGLonDispGrid'.lower():
                ezGLonDispGrid = int(thisLine[1])


            # float arguments:
            elif thisLine0Lower == '-ezGLon580Csv'.lower():
                ezGLon580Csv += [float(thisLine[1])]

            elif thisLine0Lower == '-ezGLon580CsvFrac'.lower():
                ezGLon580CsvFrac += [float(thisLine[1])]

            elif thisLine0Lower == '-ezGLon582Csv'.lower():
                ezGLon582Csv += [float(thisLine[1])]

            elif thisLine0Lower == '-ezGLonGalCrossingGLonCenter'.lower():
                ezGLonGalCrossingGLonCenterL += [float(thisLine[1])]

            elif thisLine0Lower == '-ezGLonGalCrossingGLonCenterL'.lower():
                ezGLonGalCrossingGLonCenterL += np.linspace(float(thisLine[1]), float(thisLine[2]), num=int(thisLine[3])).tolist()

            elif thisLine0Lower == '-ezGLonGalCrossingGLonNear'.lower():
                ezGLonGalCrossingGLonNear = float(thisLine[1])


            # string arguments:

            # list arguments:
            elif thisLine0Lower == '-ezGLonPlotRangeL'.lower():
                ezGLonPlotRangeL = [int(thisLine[1]), int(thisLine[2])]


            # string arguments:

            # list arguments:

            elif 6 <= len(thisLine0Lower) and thisLine0Lower[:6] == '-ezGLon'.lower():
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Defaults file ( ' + ezDefaultsFileNameInput + ' )')
                print(" has this line's unrecognized first word:")
                print(fileLine)
                print()
                print()
                print()
                print()
                exit()


            else:
                pass    # unrecognized first word, but no error

    except (FileNotFoundError, IOError):
        #print ()
        #print ()
        #print ()
        #print ()
        #print ('   Warning: Error in opening file or reading ' + ezDefaultsFileName + ' file.')
        ##print ('   ... Using defaults ...')
        #print ()
        #print ()
        #print ()
        #print ()
        pass

    else:
        fileDefaults.close()       #   then have processed all available lines in this Defaults file



def ezGLonArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsName                      # string

    global ezGLonDispGrid                   # integer

    global ezGLonGalCrossingGLonCenterL     # float list
    global ezGLonGalCrossingGLonNear        # float

    #global ezGLon61XGain                    # float
    global ezGLon580Csv                     # float
    global ezGLon580CsvFrac                 # float
    global ezGLon582Csv                     # float

    global ezGLonPlotRangeL                 # integer list

    global cmdDirectoryS                    # string            creation


    print()
    print('   ezGLonArgumentsCommandLine ===============')

    cmdLineSplit = commandString.split()
    cmdLineSplitLen = len(cmdLineSplit)
        
    if cmdLineSplitLen < 2:
        # need at least one data directory or file
        printUsage()

    cmdLineSplitIndex = 1
    cmdDirectoryS = ''

    while cmdLineSplitIndex < cmdLineSplitLen:
        #print(' cmdLineSplit[cmdLineSplitIndex] =', cmdLineSplit[cmdLineSplitIndex])
        if cmdLineSplit[cmdLineSplitIndex][0] != '-':
            # ignoring whitespace, first character of cmdLineSplit word is not '-'
            if cmdLineSplit[cmdLineSplitIndex][0] == '#':
                # rest of cmdLineSplit is a comment, get out of while loop
                break
            else:
                # must be a data directory or file, remember it
                cmdDirectoryS = cmdDirectoryS + cmdLineSplit[cmdLineSplitIndex] + ' '

        else:
            # Ignoring whitespace, first character of cmdLineSplit word is '-'.
            # Must be an option.
            # Remove '-'
            cmdLineArg = cmdLineSplit[cmdLineSplitIndex][1:]
            # ignoring whitespace, first character of cmdLineSplit word was '-', now removed
            if cmdLineArg[0] == '-':
                cmdLineArg = cmdLineArg[1:]
                # ignoring whitespace, first 2 characters of cmdLineSplit word were '--', now removed

            cmdLineArgLower = cmdLineArg.lower()
            cmdLineSplitIndex += 1      # point to first option value


            if cmdLineArgLower == 'help':
                printUsage()

            elif cmdLineArgLower == 'h':
                printUsage()


            # ezRA arguments used by multiple programs:
            elif cmdLineArgLower == 'ezRAObsName'.lower():
                ezRAObsName = cmdLineSplit[cmdLineSplitIndex]   # cmd line allows only one ezRAObsName word
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])


            # integer arguments:
            elif cmdLineArgLower == 'ezGLonDispGrid'.lower():
                ezGalDispGrid = int(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:
            elif cmdLineArgLower == 'ezGLon61XGain'.lower():
                ezGal61XGain = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezGLon580Csv'.lower():
                ezGLon580Csv = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezGLon580CsvFrac'.lower():
                ezGLon580CsvFrac = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezGLon582Csv'.lower():
                ezGLon582Csv = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezGLonGalCrossingGLonCenter'.lower():
                ezGLonGalCrossingGLonCenterL += [float(cmdLineSplit[cmdLineSplitIndex])]

            elif cmdLineArgLower == 'ezGLonGalCrossingGLonCenterL'.lower():
                ezGLonGalCrossingGLonCenterL0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGLonGalCrossingGLonCenterL1 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGLonGalCrossingGLonCenterL2 = int(cmdLineSplit[cmdLineSplitIndex])
                ezGLonGalCrossingGLonCenterL += np.linspace(ezGLonGalCrossingGLonCenterL0, ezGLonGalCrossingGLonCenterL1, num=ezGLonGalCrossingGLonCenterL2).tolist()

            elif cmdLineArgLower == 'ezGLonGalCrossingGLonNear'.lower():
                ezGLonGalCrossingGLonNear = float(cmdLineSplit[cmdLineSplitIndex])


            # string arguments:


            # list arguments:
            elif cmdLineArgLower == 'ezGLonPlotRangeL'.lower():
                ezGLonPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGLonPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezDefaultsFile'.lower():
                ezGLonArgumentsFile(cmdLineSplit[cmdLineSplitIndex])


            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 2 <= len(cmdLineArgLower) and cmdLineArgLower[:2] == 'ex':
                cmdLineSplitIndex -= 1
                #pass

            # before -eX, old spelling:
            # ignore silly -ezez* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            elif 4 <= len(cmdLineArgLower) and cmdLineArgLower[:4] == 'ezez':
                cmdLineSplitIndex -= 1
                #pass


            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized first word:')
                print('-' + cmdLineArg)
                print()
                print()
                print()
                print()
                exit()
                
        cmdLineSplitIndex += 1



def ezGLonArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global ezRAObsName                      # string

    global ezGLonGalCrossingGLonCenterL     # float list
    global ezGLonGalCrossingGLonNear        # float

    #global ezGLon61XGain                    # float
    global ezGLon580Csv                     # float
    global ezGLon580CsvFrac                 # float
    global ezGLon582Csv                     # float

    global ezGLonPlotRangeL                 # integer list
    global plotCountdown                    # integer
    global ezGLonDispGrid                   # integer


    # defaults
    #ezRAObsName = 'LebanonKS'
    #ezRAObsName = 'defaultKS'
    ezRAObsName = ''                # overwritten by optional argument

    ezGLonGalCrossingGLonCenterL = []
    ezGLonGalCrossingGLonNear = 5.

    #ezGLon61XGain = 120.            # maximum height in ezGLon61XgLonSpectraCascade plots
    ezGLon580Csv     = -9999.        # silly value to disable
    ezGLon580CsvFrac = -9999.        # silly value to disable
    ezGLon582Csv     = -9999.        # silly value to disable

    ezGLonPlotRangeL = [0, 9999]    # save this range of plots to file
    plotCountdown = 25              # number of plots still to print + 1
    ezGLonDispGrid = 0

    # process arguments from ezDefaults.txt file in the same directory as this ezGLon program
    ezGLonArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezGLonArgumentsFile('ezDefaults.txt')

    ezGLonArgumentsCommandLine()    # process arguments from command line
    
    # sanity tests

    if not len(ezGLonGalCrossingGLonCenterL):
        print()
        print()
        print(' ========== FATAL ERROR: must supply -ezGLonGalCrossingGLonCenterL values')
        print()
        print()
        print()
        exit()

    # print status
    print()
    print('   ezRAObsName =', ezRAObsName)
    print()
    print('   ezGLonGalCrossingGLonCenterL =', ezGLonGalCrossingGLonCenterL)
    print('   ezGLonGalCrossingGLonNear    =', ezGLonGalCrossingGLonNear)
    print()
    #print('   ezGLon61XGain    =', ezGLon61XGain)
    print('   ezGLon580Csv     =', ezGLon580Csv)
    print('   ezGLon580CsvFrac =', ezGLon580CsvFrac)
    print('   ezGLon582Csv     =', ezGLon582Csv)
    print()
    print('   ezGLonPlotRangeL =', ezGLonPlotRangeL)
    print('   ezGLonDispGrid   =', ezGLonDispGrid)



def readDataDir():
    # Open each data file in directory and read data

    global ezRAObsName                      # string
    global fileObsName                      # string                            creation
    global fileFreqMin                      # float                             creation
    global fileFreqMax                      # float                             creation
    global fileFreqBinQty                   # integer                           creation

    global velGLatP90                       # float 2d array                    creation
    global velGLatP90Count                  # integer array                     creation
    global velGLatP90CountSum               # integer                           creation
    global antXTVTName                      # string                            creation
    global ezGLonGalCrossingGLonCenter      # float
    global ezGLonGalCrossingGLonNear        # float
    global fileNameLast                     # string                            creation

    print()
    print('   readDataDir ===============')

    ezConGalCrossingGLonMax = -9999     # silly value
    ezConGalCrossingGLonMin =  9999     # silly value

    #directoryList = sorted(cmdDirectoryS.split())           # sorted needed on Linux
    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)

    gLonNpz_Qty = 0
    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]

        # if arguments are GLon.npz filenames,
        # pass each of them through together as a mini directory list of GLon.npz files.
        # Allows one GLon.npz file from a directory of GLon.npz files.
        if directory.endswith('GLon.npz'):
            fileList = [directory]
            directory = '.'
        else:
            fileList = sorted(os.listdir(directory))        # sorted needed on Linux
        fileListLen = len(fileList)
        for fileCounter in range(fileListLen):
            fileReadName = fileList[fileCounter]
            #print('\r file =', fileCounter + 1, ' of', fileListLen,
            #    ' in dir', directoryCounter + 1, ' of', directoryListLen,
            #    ' =', directory + os.path.sep + fileReadName, '                                      ',
            #    end='')   # allow append to line
            #print(f'\r {gLonNpz_Qty + 1}  file = {fileCounter + 1} of {fileListLen}',
            #    f' in dir {directoryCounter + 1} of {directoryListLen} =',
            #    directory + os.path.sep + fileReadName, '                                      ',
            #    end='')   # allow append to line
            print(f'\r {gLonNpz_Qty + 1} for GLon {ezGLonGalCrossingGLonCenter},',
                f' in dir {directoryCounter + 1} of {directoryListLen}',
                f' file = {fileCounter + 1} of {fileListLen} =',
                directory + os.path.sep + fileReadName, '                                      ',
                end='')   # allow append to line

            if not fileReadName.endswith('GLon.npz'):
                continue                                # skip to next file

            npzfile = np.load(fileReadName)
            #print(npzfile.files)

            # ezCon230629a.py says
            #   np.savez_compressed(fileGLonWriteName,
            #       fileObsName=np.array(ezRAObsName),
            #       fileFreqMin=np.array(fileFreqMin), 
            #       fileFreqMax=np.array(fileFreqMax),
            #       fileFreqBinQty=np.array(fileFreqBinQty),
            #       velGLatP90=velGLatP90,
            #       velGLatP90Count=velGLatP90Count,
            #       antXTVTName=antXNameL[1]+'TVT',
            #       ezConGalCrossingGLonCenter=ezConGalCrossingGLonCenter,
            #       ezConGalCrossingGLonNear=ezConGalCrossingGLonNear)

            ezConGalCrossingGLonCenter = npzfile['ezConGalCrossingGLonCenter']
            #print(" ezConGalCrossingGLonCenter =", ezConGalCrossingGLonCenter)

            if ezConGalCrossingGLonCenter < ezGLonGalCrossingGLonCenter - ezGLonGalCrossingGLonNear \
                or ezGLonGalCrossingGLonCenter + ezGLonGalCrossingGLonNear < ezConGalCrossingGLonCenter:
                    continue                            # skip to next file

            if not gLonNpz_Qty:
                # first *GLon.npz file
                # These are defined by the first *GLon.npz file:
                #   fileObsName
                #   fileFreqMin
                #   fileFreqMax
                #   fileFreqBinQty
                #   antXTVTName
                #   ezConGalCrossingGLonCenter
                #   ezConGalCrossingGLonNear
                fileObsName    = npzfile['fileObsName'].tolist()
                if ezRAObsName:
                    fileObsName = ezRAObsName       # overwrite fileObsName with argument
                fileFreqMin    = float(npzfile['fileFreqMin'])
                fileFreqMax    = float(npzfile['fileFreqMax'])
                fileFreqBinQty = int(npzfile['fileFreqBinQty'])

                # Velocity by Galactic Latitude (gLat) grid.
                # gLat is -90thru+90, adding 90, gives gLatP90 as 0thru180 which is more convenient.
                # velGLatP90 is fileFreqBinQty by 0thru180 gLatP90
                #velGLatP90 = np.zeros([fileFreqBinQty, 181], dtype = float)
                velGLatP90 = npzfile['velGLatP90']

                # incoming velGLatP90 is now still the summed antXTVT frequency spectra, with decending frequency.
                # For each spectrum, velGLatP90Count[gLatP90] recorded the quantity summed.

                # velGLatP90Count is count of saved spectra in velGLatP90
                #velGLatP90Count = np.zeros([181], dtype = int)
                velGLatP90Count = npzfile['velGLatP90Count']
                #print(npzfile.files)
                #print('antXTVTName' in npzfile.files)
                antXTVTName = npzfile['antXTVTName']
                #ezConGalCrossingGLonCenter = npzfile['ezConGalCrossingGLonCenter']
                ezConGalCrossingGLonNear = npzfile['ezConGalCrossingGLonNear']

            else:
                # not first *GLon.npz file
                velGLatP90            += npzfile['velGLatP90']
                velGLatP90Count       += npzfile['velGLatP90Count']

            if 0:
                # blur to make new data wider
                #velGLatP90[:, 2:]  = velGLatP90[:, :-2] + npzfile['velGLatP90'][:, :-2]
                velGLatP90[:, 1:]  = velGLatP90[:, :-1] + npzfile['velGLatP90'][:, :-1]
                velGLatP90[:, :-1] = velGLatP90[:, 1:]  + npzfile['velGLatP90'][:, 1:]
                #velGLatP90[:, :-2] = velGLatP90[:, 2:]  + npzfile['velGLatP90'][:, 2:]

                #velGLatP90Count[2:]  = velGLatP90Count[:-2] + npzfile['velGLatP90Count'][:-2]
                velGLatP90Count[1:]  = velGLatP90Count[:-1] + npzfile['velGLatP90Count'][:-1]
                velGLatP90Count[:-1] = velGLatP90Count[1:]  + npzfile['velGLatP90Count'][1:]
                #velGLatP90Count[:-2] = velGLatP90Count[2:]  + npzfile['velGLatP90Count'][2:]

            gLonNpz_Qty += 1
            fileNameLast = fileReadName
            ezConGalCrossingGLonMax = max(ezConGalCrossingGLonMax, ezConGalCrossingGLonCenter + ezConGalCrossingGLonNear)
            ezConGalCrossingGLonMin = min(ezConGalCrossingGLonMin, ezConGalCrossingGLonCenter - ezConGalCrossingGLonNear)
            print()

            #if gLonNpz_Qty:
            #    break                       # got one GLon.npz file, get out of for loop

    # have now read all GLon.npz files

    # maybe blank out the last filename
    if not fileReadName.endswith('GLon.npz'):
        print('\r                                                                              ' \
            + '                                                                                ')
    else:
        print()
    
    if not gLonNpz_Qty:                      # if no first *GLon.npz file
        print()
        print()
        print(' ========== FATAL ERROR: no data file loaded')
        print()
        print()
        print()
        exit()


    print(' fileNameLast =', fileNameLast)
    print(' gLonNpz_Qty  =', gLonNpz_Qty)
    print()
    print(' fileObsName = ', fileObsName)
    print(' fileFreqMin = ', fileFreqMin)
    print(' fileFreqMax = ', fileFreqMax)
    print(' fileFreqBinQty = ', fileFreqBinQty)
    print()
    print(' velGLatP90.shape = ', velGLatP90.shape)
    print(' velGLatP90Count.shape = ', velGLatP90Count.shape)
    print()
    print(' antXTVTName =', antXTVTName)
    print(' ezConGalCrossingGLon possible Max = ', ezConGalCrossingGLonMax)
    print(' ezConGalCrossingGLon possible Min = ', ezConGalCrossingGLonMin)
    print(' Requested ezGLonGalCrossingGLonCenter =', ezGLonGalCrossingGLonCenter)
    print(' Requested ezGLonGalCrossingGLonNear   =', ezGLonGalCrossingGLonNear)
    print()
    velGLatP90CountSum = velGLatP90Count.sum()
    print(' velGLatP90CountSum =', velGLatP90CountSum)

    if not velGLatP90CountSum:       # if nothing in velGLatP90 to save or plot
        print()
        print()
        print(' ========== FATAL ERROR: no data loaded')
        print()
        print()
        print()
        exit()


    # Prepare velGLatP90 for later plots.
    # velGLatP90 has been filled with sums of samples.  Now for each column, convert to sum's average.
    for gLatP90 in range(181):
        if velGLatP90Count[gLatP90]:
            velGLatP90[:, gLatP90] /= velGLatP90Count[gLatP90]

    # mask low values with Not-A-Number (np.nan) to not plot
    #maskOffBelowThis = 0.975    # N0RQVHC
    #maskOffBelowThis = 0.9      # WA6RSV
    maskOffBelowThis = 1.0      # LTO15HC
    print('      maskOffBelowThis = ', maskOffBelowThis)
    maskThisOff = (velGLatP90 < maskOffBelowThis)
    #velGLatP90[maskThisOff] = np.nan                   # maskOffBelowThis is the do not plot
    velGLatP90[maskThisOff] = maskOffBelowThis         # maskOffBelowThis is the minumum everywhere



def plotPrep():
    # creates titleS, velocitySpanMax, velocityBin

    global fileObsName              # string
    global fileFreqMin              # float
    global fileFreqMax              # float
    global fileFreqBinQty           # integer

    global freqStep                 # float                 creation
    global freqCenter               # float                 creation

    global velocitySpanMax          # float                 creation
    global velocityBin              # float array           creation

    global titleS                   # string                creation

    print()
    print('   plotPrep ===============')

    print('                         fileFreqMin =', fileFreqMin)
    print('                         fileFreqMax =', fileFreqMax)

    #freqStep = 0.00234375           # 2.4 MHz / 1024 = 0.00234375 MHz
    # fileFreqMin = 1419.205         #0000      -1.2 Doppler
    #                                #0512       0.0 Doppler
    # fileFreqMax = 1421.60265625    #1023       1.2 Doppler
    # (1421.60265625 - 1419.205 ) * 512 / 1023 = 1.2
    # 1.2  + 1419.205 = 1420.405 ------- yup
    #freqStep = (fileFreqMax - fileFreqMin) / (freqBinQtyPre + fileFreqBinQty - 1)
    freqStep = (fileFreqMax - fileFreqMin) / (fileFreqBinQty - 1)
    print('                         freqStep =', freqStep)
    dopplerSpanD2 = (fileFreqMax - fileFreqMin) / 2.        # Doppler spans -dopplerSpanD2 thru +dopplerSpanD2
    print('                         dopplerSpanD2 =', dopplerSpanD2)
    freqCenter = (fileFreqMin + fileFreqMax) / 2.
    print('                         freqCenter =', freqCenter)

    #titleS = '  ' + fileNameLast.split('\\')[-1] + u'           N\u00D8RQV          (' + programName + ')'
    #titleS = '  ' + fileNameLast.split('\\')[-1] + u'           WA6RSV          (' + programName + ')'
    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + u'           ' + fileObsName \
        + '          (' + programName + ')'

    #if 0 <= ezGLonGalCrossingGLonCenter:
    #    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + u'      ' + fileObsName \
    #        + f'P{ezGLonGalCrossingGLonCenter:03d}      (' + programName + ')'
    #else:
    #    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + u'      ' + fileObsName \
    #        + f'M{-ezGLonGalCrossingGLonCenter:03d}      (' + programName + ')'

    velocitySpanMax = dopplerSpanD2 * (299792458. / freqCenter) / 1000.  # = 253.273324388 km/s
    print('                         velocitySpanMax =', velocitySpanMax)
    velocityBin = np.linspace(-velocitySpanMax, velocitySpanMax, fileFreqBinQty)
    #print('                         velocityBin =', velocityBin)
    print('                         len(velocityBin) =', len(velocityBin))



def plotEzGLon510velGLat():

    global plotCountdown            # integer
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer

    global ezGLonGalCrossingGLonCenter      # float
    global ezGLonGalCrossingGLonNear        # float

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGLonDispGrid           # integer
    global ezGLonPlotRangeL         # integer list

    plotCountdown -= 1

    # if anything in velGLatP90 to save or plot
    if ezGLonPlotRangeL[0] <= 510 and 510 <= ezGLonPlotRangeL[1] and velGLatP90CountSum:

        #plotName = 'ezGLon510velGLat.png'
        #plotName = 'ezGLon510velGLatXxxx.xXxxx.x.png'
        if 0 <= ezGLonGalCrossingGLonCenter:
            plotName = f'ezGLon510velGLatP{ezGLonGalCrossingGLonCenter:05.1f}'
        else:
            plotName = f'ezGLon510velGLatN{ezGLonGalCrossingGLonCenter:05.1f}'
        if 0 <= ezGLonGalCrossingGLonNear:
            plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
        else:
            plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

        plt.clf()

        # if any Galactic plane crossings, velGLatP90 has been (partially?) filled with averages
        velGLatP90CountNonzero = np.count_nonzero(velGLatP90Count)
        print('                         velGLatP90CountNonzero =', velGLatP90CountNonzero, 'of', len(velGLatP90Count) )
        print()

        xi = np.arange(-90, +91, 1)           # +90 thru -90 degrees in degrees, galaxy plane centered
        #yi = np.arange(0, fileFreqBinQty, 1)    # 0 to fileFreqBinQty in freqBins
        # speed of light = 299,792,458 meters per second
        #    rawPlotPrep ===============
        #       fileFreqMin = 1419.2
        #       fileFreqMax = 1421.6
        #       freqStep = 0.009411764705881818
        #       dopplerSpanD2 = 1.1999999999999318
        #       freqCenter = 1420.4
        # velocity = (fileFreqBin doppler MHz) * (299792458. m/s / 1420.406 MHz) / 1000. = km/s
        # velocity spans = -dopplerSpanD2 * (299792458. / freqCenter) thru
        #                  +dopplerSpanD2 * (299792458. / freqCenter)
        #velocitySpanMax = +1.1999999999999318 * (299792458. / 1420.406) / 1000.  # = 253.273324388 km/s
        #velocitySpanMax = +dopplerSpanD2 * (299792458. / freqCenter) / 1000.  # = 253.273324388 km/s
        #yi = np.linspace(-velocitySpanMax, velocitySpanMax, fileFreqBinQty)
        yi = velocityBin + 0.

        xi, yi = np.meshgrid(xi, yi)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        if 1:
            #gridColor = 'black'
            gridColor = 'white'
            # horizonal thin black line
            plt.axhline(y =   0, linewidth=0.5, color=gridColor)

        if 1:
            # vertical thin lines
            plt.axvline(x = -45, linewidth=0.5, color=gridColor)
            plt.axvline(x =   0, linewidth=0.5, color=gridColor)
            plt.axvline(x =  45, linewidth=0.5, color=gridColor)

        print('                         np.nanmax(velGLatP90) =', np.nanmax(velGLatP90))
        #print('                         np.mean(velGLatP90[~np.isnan(velGLatP90)]) =',
        #    np.mean(velGLatP90[~np.isnan(velGLatP90)]))
        print('                         np.mean(velGLatP90) =', np.mean(velGLatP90))
        print('                         np.nanmin(velGLatP90) =', np.nanmin(velGLatP90))
        #pts = plt.contourf(xi, yi, velGLatP90, 100, cmap=plt.get_cmap('gnuplot'), vmin=1.025, vmax=1.21)
        pts = plt.contourf(xi, yi, velGLatP90, 100, cmap=plt.get_cmap('gnuplot'))

        cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

        plt.title(titleS)
        #plt.grid(ezGLonDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Latitude (degrees)')
        plt.xlim(-90, 90)        # in degrees
        plt.xticks([ -90,   -45,   0,   45,   90],
                   ['-90', '-45', '0', '45', '90'])

        plt.ylim(-velocitySpanMax, velocitySpanMax)        # in velocity

        #    plt.ylabel('Interpolated Velocity (km/s) by Galactic Latitude' \
        #        + f'\n\nVelocity Count Sum = {velGLatP90CountSum}' \
        #        + f'\n\nVelocity Count Nonzero = {velGLatP90CountNonzero}' \
        #        + f' of {len(velGLatP90Count)}',
        #        rotation=90, verticalalignment='bottom')
        plt.ylabel('Interpolated Velocity (km/s) by Galactic Latitude' \
            + f'\nVelocity Count: Sum={velGLatP90CountSum:,}'
            + f' Nonzero={velGLatP90CountNonzero} of {len(velGLatP90Count)}',
            rotation=90, verticalalignment='bottom')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzGLon511velGLatCount():

    global plotCountdown            # integer
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global ezGLonGalCrossingGLonCenter      # float
    global ezGLonGalCrossingGLonNear        # float

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGLonPlotRangeL         # integer list

    plotCountdown -= 1

    # if anything in velGLatP90 to plot
    if ezGLonPlotRangeL[0] <= 511 and 511 <= ezGLonPlotRangeL[1] and velGLatP90CountSum:

        #plotName = 'ezGLon511velGLatCount.png'
        #plotName = 'ezGLon511velGLatCountXxxx.xXxxx.x.png'
        if 0 <= ezGLonGalCrossingGLonCenter:
            plotName = f'ezGLon511velGLatCountP{ezGLonGalCrossingGLonCenter:05.1f}'
        else:
            plotName = f'ezGLon511velGLatCountN{ezGLonGalCrossingGLonCenter:05.1f}'
        if 0 <= ezGLonGalCrossingGLonNear:
            plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
        else:
            plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

        plt.clf()
        plt.plot(np.arange(-90, +91, 1), velGLatP90Count)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Latitude (degrees)')
        plt.xlim(-92, 92)        # in degrees
        plt.xticks([ -90,   -45,   0,   45,   90],
                   ['-90', '-45', '0', '45', '90'])

        # if any Galactic plane crossings, velGLatP90 has been (partially?) filled with averages
        velGLatP90CountNonzero = np.count_nonzero(velGLatP90Count)
        print('                         velGLatP90CountNonzero =', velGLatP90CountNonzero, 'of', len(velGLatP90Count) )
        print()

        plt.ylabel('Velocity Data Counts by Galactic Latitude' \
            + f'\nVelocity Count: Sum={velGLatP90CountSum:,}' \
            + f' Nonzero = {velGLatP90CountNonzero} of {len(velGLatP90Count)}')
        #    rotation=90, verticalalignment='bottom')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')


        if 0:
            # print out velGLonCount status
            fileWriteGLonName = 'ezGLon511velGLatCount.txt'
            fileWriteGLon = open(fileWriteGLonName, 'w')
            if not (fileWriteGLon.mode == 'w'):
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Can not open ')
                print(' ' + fileWriteGLonName)
                print(' file to write out velGLatCount data')
                print()
                print()
                print()
                print()
                exit()


            fileWriteGLonHashS = '########################################' \
                + '########################################'                        # 40 + 40 = 80 '#'

            fileWriteGLon.write('\ngLonDeg (-180thru180)   velGLonCount   gLonDegForHaystackSrt.cmd '\
                + '(180thru359to0thru180)       (RtoL)\n\n')

            for gLonP180 in range(180):                               # for every column, RtoL, 0 thru 179
                fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLatP90Count[gLonP180]:5d}  {gLonP180 + 180:4d}  ' \
                    + fileWriteGLonHashS[:velGLatP90Count[gLonP180]] + '\n'
                fileWriteGLon.write(fileWriteGLonS)

            fileWriteGLonS = f'0000  {velGLatP90Count[180]:5d}  0000  ' \
                + fileWriteGLonHashS[:velGLatP90Count[180]] + '\n'
            fileWriteGLon.write(fileWriteGLonS)

            for gLonP180 in range(181, 361):                          # for every column, RtoL, 181 thru 360
                fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLatP90Count[gLonP180]:5d}  {gLonP180 - 180:4d}  ' \
                    + fileWriteGLonHashS[:velGLatP90Count[gLonP180]] + '\n'
                fileWriteGLon.write(fileWriteGLonS)


            # print out velGLonCount Things-To-Do for Haystack srt.cmd command file
            velGLonCountTrigger = 15
            fileWriteGLon.write( \
                '\n\n\n\n\n* velGLonCount Things-To-Do for Haystack srt.cmd command file    (RtoL)')
            fileWriteGLon.write('\n* velGLonCountTrigger = ' + str(velGLonCountTrigger))
            fileWriteGLon.write('\n\n:5              * short pause of 5 seconds')
            fileWriteGLon.write('\n: record')
            fileWriteGLon.write('\n* later, do not forget at the end,       : roff\n\n')
            fileWriteGLon.write( \
                '\n* 600 + 240 + 060 = 900 seconds = 10 + 4 + 1 minutes = 15 min data collection\n\n')

            for gLonP180 in range(180):                               # for every column, RtoL, 0 thru 179
                if velGLatP90Count[gLonP180] <= velGLonCountTrigger:
                    fileWriteGLon.write(f': G{gLonP180 + 180:03d}    * have {velGLatP90Count[gLonP180]:5d}\n')
                    fileWriteGLon.write(':600\n')
                    fileWriteGLon.write(':240\n')
                    fileWriteGLon.write(':060\n')
                    fileWriteGLon.write('*\n')
            for gLonP180 in range(180, 361):                          # for every column, RtoL, 180 thru 360
                if velGLatP90Count[gLonP180] <= velGLonCountTrigger:
                    fileWriteGLon.write(f': G{gLonP180 - 180:03d}    * have {velGLatP90Count[gLonP180]:5d}\n')
                    fileWriteGLon.write(':600\n')
                    fileWriteGLon.write(':240\n')
                    fileWriteGLon.write(':060\n')
                    fileWriteGLon.write('*\n')

            fileWriteGLon.close()   



def plotEzGlon570galArmsSun():
    # plot Galactic Arms with Sun in center

    global plotCountdown            # integer
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global ezGLonGalCrossingGLonCenter      # float 
    global ezGLonGalCrossingGLonNear        # float

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGLonDispGrid           # integer
    global ezGLonPlotRangeL         # integer list

    global fileFreqBinQty           # integer
    global velocityBin              # float array

    plotCountdown -= 1

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 570 and 570 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    #plotName = 'ezGLon570galArmsSun.png'
    #plotName = 'ezGLon570galArmsSunXxxx.xXxxx.x.png'
    if 0 <= ezGLonGalCrossingGLonCenter:
        plotName = f'ezGLon570galArmsSunP{ezGLonGalCrossingGLonCenter:05.1f}'
    else:
        plotName = f'ezGLon570galArmsSunN{ezGLonGalCrossingGLonCenter:05.1f}'
    if 0 <= ezGLonGalCrossingGLonNear:
        plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
    else:
        plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

    plt.clf()

    if velGLatP90CountSum:         # if anything in velGLatP90 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusPlotLimit = galSunRadiusKm * 3.

        gLonDeg = ezGLonGalCrossingGLonCenter
        #gLonDegRad = gLonDeg * np.pi / 180.
        gLonDegRad = gLonDeg * 0.01745329251
        #gLonDegRadMany = np.full(fileFreqBinQty, gLonDegRad)

        # JJ's p54 Eq3
        #   R = R0*V0*sin(l) / ( V0*sin(l) + Vr )
        galGasVelRadiusKm = galSunRadiusKm * 220. * np.sin(gLonDegRad) \
            / (220. * np.sin(gLonDegRad) + velocityBin)   # in km
        # shape(galGasVelRadiusKm) = (256,)
        # but that denominator was often near zero, so trim +/- large galGasVelRadiusKm
        ##############galGasVelRadiusKm[galSunRadiusPlotLimit  < galGasVelRadiusKm] = np.nan
        ##############galGasVelRadiusKm[galGasVelRadiusKm < -galSunRadiusPlotLimit] = np.nan
        # trim negative galGasVelRadiusKm
        galGasVelRadiusKm[galGasVelRadiusKm < 0.] = np.nan

        # JJ's p54 Eq4
        #   r = +-sqrt( R*R     - R0*R0*sin(l)*sin(l) ) + R0*cos(l)
        #   r = +-sqrt( addend1 + addend2             ) + addend3
        #   but negative values of r are ignored because they have no physical reality
        addend1 = galGasVelRadiusKm * galGasVelRadiusKm     # = np.multiply()
        addend2 = -galSunRadiusKm2 * math.sin(gLonDegRad) * math.sin(gLonDegRad)
        addend3 = galSunRadiusKm * math.cos(gLonDegRad)
        addend1p2 = addend1 + addend2
        # trim negative addend1p2 before sqrt()
        addend1p2[addend1p2 < 0.] = np.nan

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        # use positive sqrt()
        addend12 = np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3)
        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        #print('============== velGLatP90Count =', velGLatP90Count)

        for gLatDeg in range(-90, 91):
            #gLatDeg += 45
            gLatDegP90 = gLatDeg + 90
            if 180 <= gLatDegP90:
                gLatDegP90 -= 180

            if velGLatP90Count[gLatDegP90] > 0:       # if column used
                print('============== gLatDeg =', gLatDeg)
                #gLatDegRad = gLatDeg * np.pi / 180.
                gLatDegRad = gLatDeg * 0.01745329251
                #gLatDegRad = gLatDeg * 0.01745329251 + .1
                gLatDegRadMany = np.full(fileFreqBinQty, -gLatDegRad)

                #print('============== plotRadii =', plotRadii)
                print('============== np.nanmax(plotRadii) =', np.nanmax(plotRadii))
                polarPlot = ax.scatter(gLatDegRadMany, plotRadii,
                    c=velGLatP90[:,gLatDegP90], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        # use negative sqrt()
        addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3)
        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        #        print('============== plotRadii =', plotRadii)
        #        polarPlot = ax.scatter(gLatDegRadMany, plotRadii,
        #            c=velGLatP90[:,gLatDegP90], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        for gLatDeg in range(-90, 91):
            #gLatDeg += 45
            gLatDegP90 = gLatDeg + 90
            if 180 <= gLatDegP90:
                gLatDegP90 -= 180

            if velGLatP90Count[gLatDegP90] > 0:       # if column used
                print('============== gLatDeg =', gLatDeg)
                #gLatDegRad = gLatDeg * np.pi / 180.
                gLatDegRad = gLatDeg * 0.01745329251
                #gLatDegRad = gLatDeg * 0.01745329251 + .1
                gLatDegRadMany = np.full(fileFreqBinQty, -gLatDegRad)

                #print('============== plotRadii =', plotRadii)
                print('============== np.nanmax(plotRadii) =', np.nanmax(plotRadii))
                polarPlot = ax.scatter(gLatDegRadMany, plotRadii,
                    c=velGLatP90[:,gLatDegP90], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        # Plot yellow Sun at center
        polarPlot = ax.scatter(0., 0., c='black', s=120, alpha=0.75)
        polarPlot = ax.scatter(0., 0., c='yellow', s=100, alpha=1.)

        # Add a color bar which maps values to colors.
        plt.colorbar(polarPlot, pad=0.1)

        plt.title(titleS)

        ax.set_rgrids((galSunRadiusPlotLimit,), ('',))
        ax.set_theta_zero_location('W', offset=0.0)
        #ax.set_thetagrids((0, 90, 180, 270), ('0', '90', '                               180 and -180 Galactic Longitude', '-90'))
        #ax.set_thetagrids((0, 90, 180, 270), ('0', '-90 Galactic Latitude', '', '90'))
        if 1:
            ax.set_thetagrids((0, 90, 180, 270), ('0', '                           -90 Galactic Latitude', '', '90'))
        if 0:
            ax.set_thetagrids((90, 180, 270), ('                           -90 Galactic Latitude', '', '90'))
        ax.set_rmax(galSunRadiusPlotLimit)
        ax.set_facecolor("black")

        #radiusTextQuadrant = galSunRadiusPlotLimit * 1.4
        #ax.text( 0.9,  radiusTextQuadrant, 'Quadrant 1', color='red', verticalalignment='center')
        #ax.text( 2.25, radiusTextQuadrant, 'Quadrant 2', color='red', verticalalignment='center')
        #ax.text(-2.25, radiusTextQuadrant, 'Quadrant 3', color='red', verticalalignment='center', horizontalalignment='right')
        #ax.text(-0.9,  radiusTextQuadrant, 'Quadrant 4', color='red', verticalalignment='center', horizontalalignment='right')

        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nSun = Yellow Dot\n\n')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzGlon571galArmsSunMag5():
    # plot Galactic Arms with Sun in center with Magnified x5 gLat angles

    global plotCountdown            # integer
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global ezGLonGalCrossingGLonCenter      # float 
    global ezGLonGalCrossingGLonNear        # float

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGLonDispGrid           # integer
    global ezGLonPlotRangeL         # integer list

    global fileFreqBinQty           # integer
    global velocityBin              # float array

    plotCountdown -= 1

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 571 and 571 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    #plotName = 'ezGLon571galArmsSunMag5.png'
    #plotName = 'ezGLon571galArmsSunMag5Xxxx.xXxxx.x.png'
    if 0 <= ezGLonGalCrossingGLonCenter:
        plotName = f'ezGLon571galArmsSunMag5P{ezGLonGalCrossingGLonCenter:05.1f}'
    else:
        plotName = f'ezGLon571galArmsSunMag5N{ezGLonGalCrossingGLonCenter:05.1f}'
    if 0 <= ezGLonGalCrossingGLonNear:
        plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
    else:
        plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

    plt.clf()

    if velGLatP90CountSum:         # if anything in velGLatP90 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusPlotLimit = galSunRadiusKm * 3.

        gLonDeg = ezGLonGalCrossingGLonCenter
        #gLonDegRad = gLonDeg * np.pi / 180.
        gLonDegRad = gLonDeg * 0.01745329251
        #gLonDegRadMany = np.full(fileFreqBinQty, gLonDegRad)

        # JJ's p54 Eq3
        #   R = R0*V0*sin(l) / ( V0*sin(l) + Vr )
        galGasVelRadiusKm = galSunRadiusKm * 220. * np.sin(gLonDegRad) \
            / (220. * np.sin(gLonDegRad) + velocityBin)   # in km
        # shape(galGasVelRadiusKm) = (256,)
        # but that denominator was often near zero, so trim +/- large galGasVelRadiusKm
        ##############galGasVelRadiusKm[galSunRadiusPlotLimit  < galGasVelRadiusKm] = np.nan
        ##############galGasVelRadiusKm[galGasVelRadiusKm < -galSunRadiusPlotLimit] = np.nan
        # trim negative galGasVelRadiusKm
        galGasVelRadiusKm[galGasVelRadiusKm < 0.] = np.nan

        # JJ's p54 Eq4
        #   r = +-sqrt( R*R     - R0*R0*sin(l)*sin(l) ) + R0*cos(l)
        #   r = +-sqrt( addend1 + addend2             ) + addend3
        #   but negative values of r are ignored because they have no physical reality
        addend1 = galGasVelRadiusKm * galGasVelRadiusKm     # = np.multiply()
        addend2 = -galSunRadiusKm2 * math.sin(gLonDegRad) * math.sin(gLonDegRad)
        addend3 = galSunRadiusKm * math.cos(gLonDegRad)
        addend1p2 = addend1 + addend2
        # trim negative addend1p2 before sqrt()
        addend1p2[addend1p2 < 0.] = np.nan

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        # use positive sqrt()
        addend12 = np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3)
        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        #print('============== velGLatP90Count =', velGLatP90Count)

        #for gLatDeg in range(-90, 91):
        for gLatDeg in range(-18, 19):
            #gLatDeg += 45
            gLatDegP90 = gLatDeg + 90
            if 180 <= gLatDegP90:
                gLatDegP90 -= 180

            if velGLatP90Count[gLatDegP90] > 0:       # if column used
                print('============== gLatDeg =', gLatDeg)
                #gLatDegRad = gLatDeg * np.pi / 180.
                ##gLatDegRad = gLatDeg * 0.01745329251
                #gLatDegRad = gLatDeg * 0.01745329251 + .1
                gLatDegRad = gLatDeg * 0.01745329251 * 5.   # Mag5
                gLatDegRadMany = np.full(fileFreqBinQty, -gLatDegRad)

                #print('============== plotRadii =', plotRadii)
                print('============== np.nanmax(plotRadii) =', np.nanmax(plotRadii))
                polarPlot = ax.scatter(gLatDegRadMany, plotRadii,
                    c=velGLatP90[:,gLatDegP90], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        # use negative sqrt()
        addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3)
        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        #        print('============== plotRadii =', plotRadii)
        #        polarPlot = ax.scatter(gLatDegRadMany, plotRadii,
        #            c=velGLatP90[:,gLatDegP90], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        #for gLatDeg in range(-90, 91):
        for gLatDeg in range(-18, 19):
            #gLatDeg += 45
            gLatDegP90 = gLatDeg + 90
            if 180 <= gLatDegP90:
                gLatDegP90 -= 180

            if velGLatP90Count[gLatDegP90] > 0:       # if column used
                print('============== gLatDeg =', gLatDeg)
                #gLatDegRad = gLatDeg * np.pi / 180.
                ##gLatDegRad = gLatDeg * 0.01745329251
                #gLatDegRad = gLatDeg * 0.01745329251 + .1
                gLatDegRad = gLatDeg * 0.01745329251 * 5.   # Mag5
                gLatDegRadMany = np.full(fileFreqBinQty, -gLatDegRad)

                #print('============== plotRadii =', plotRadii)
                print('============== np.nanmax(plotRadii) =', np.nanmax(plotRadii))
                polarPlot = ax.scatter(gLatDegRadMany, plotRadii,
                    c=velGLatP90[:,gLatDegP90], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        # Plot yellow Sun at center
        polarPlot = ax.scatter(0., 0., c='black', s=120, alpha=0.75)
        polarPlot = ax.scatter(0., 0., c='yellow', s=100, alpha=1.)

        # Add a color bar which maps values to colors.
        plt.colorbar(polarPlot, pad=0.1)

        plt.title(titleS)

        ax.set_rgrids((galSunRadiusPlotLimit,), ('',))
        ax.set_theta_zero_location('W', offset=0.0)
        #ax.set_thetagrids((0, 90, 180, 270), ('0', '90', '                               180 and -180 Galactic Longitude', '-90'))
        #ax.set_thetagrids((0, 90, 180, 270), ('0', '-90 Galactic Latitude', '', '90'))
        if 1:
            ax.set_thetagrids((0, 90, 180, 270), ('0', '                           -18 Galactic Latitude', '', '18'))
        if 0:
            ax.set_thetagrids((90, 180, 270), ('                           -90 Galactic Latitude', '', '90'))
        ax.set_rmax(galSunRadiusPlotLimit)
        ax.set_facecolor("black")

        #radiusTextQuadrant = galSunRadiusPlotLimit * 1.4
        #ax.text( 0.9,  radiusTextQuadrant, 'Quadrant 1', color='red', verticalalignment='center')
        #ax.text( 2.25, radiusTextQuadrant, 'Quadrant 2', color='red', verticalalignment='center')
        #ax.text(-2.25, radiusTextQuadrant, 'Quadrant 3', color='red', verticalalignment='center', horizontalalignment='right')
        #ax.text(-0.9,  radiusTextQuadrant, 'Quadrant 4', color='red', verticalalignment='center', horizontalalignment='right')

        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nSun = Yellow Dot, GLat Magnification = 5\n\n')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')






#def plotEzGal580galArmsGC():
def plotEzGLon580galArmsSunI():
    # plot Interpolated Galactic Arms with Sun in center

    global plotCountdown            # integer
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global ezGLon580Csv                     # float
    global ezGLon580CsvFrac                 # float
    global ezGLonGalCrossingGLonCenter      # float 
    global ezGLonGalCrossingGLonNear        # float

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGLonDispGrid           # integer
    global ezGLonPlotRangeL         # integer list

    global fileFreqBinQty           # integer
    global velocityBin              # float array





#    global velGLonP180              # float 2d array
#    global velGLonP180Count         # integer array
#    global velGLonP180CountSum      # integer

    plotCountdown -= 1

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 580 and 580 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    #plotName = 'ezGLon580galArmsSunI.png'
    #plotName = 'ezGLon580galArmsSunIXxxx.xXxxx.x.png'
    if 0 <= ezGLonGalCrossingGLonCenter:
        plotName = f'ezGLon580galArmsSunIP{ezGLonGalCrossingGLonCenter:05.1f}'
    else:
        plotName = f'ezGLon580galArmsSunIN{ezGLonGalCrossingGLonCenter:05.1f}'
    if 0 <= ezGLonGalCrossingGLonNear:
        plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
    else:
        plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

    plt.clf()

    if velGLatP90CountSum:         # if anything in velGLatP90 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusKpc = galSunRadiusKm * 3.24078e-17      # in kiloparsecs
        galSunRadiusPlotLimit = galSunRadiusKm * 4.

        x = []
        y = []
        z = []

        # longest plotRadii needed, to draw edge toward top right corner, at
        #   sqrt(20*20 + 30*30) is 36.06
        plotRadiiEdgeMany = np.linspace(0., 37., 371)       # each tenth of kiloparsec
        velGLatP90MinMany = np.full_like(plotRadiiEdgeMany, velGLatP90.min())

        # ezGLonGalCrossingGLonCenter is used to create plotRadii 
        #gLonDegRad = ezGLonGalCrossingGLonCenter * np.pi / 180.
        gLonDegRad = ezGLonGalCrossingGLonCenter * 0.01745329251

        cosGLonDegRad = math.cos(gLonDegRad)
        sinGLonDegRad = math.sin(gLonDegRad)

        # JJ's p54 Eq3
        #   R = R0*V0*sin(l) / ( V0*sin(l) + Vr )
        galGasVelRadiusKm = galSunRadiusKm * 220. * np.sin(gLonDegRad) \
            / (220. * np.sin(gLonDegRad) + velocityBin)   # in km
        # shape(galGasVelRadiusKm) = (256,)
        # but that denominator was often near zero, so trim +/- large galGasVelRadiusKm
        galGasVelRadiusKm[galSunRadiusPlotLimit  < galGasVelRadiusKm] = np.nan
        galGasVelRadiusKm[galGasVelRadiusKm < -galSunRadiusPlotLimit] = np.nan
        # trim negative galGasVelRadiusKm
        galGasVelRadiusKm[galGasVelRadiusKm < 0.] = np.nan

        # JJ's p54 Eq4
        #   r = +-sqrt( R*R     - R0*R0*sin(l)*sin(l) ) + R0*cos(l)
        #   r = +-sqrt( addend1 + addend2             ) + addend3
        #   but negative values of r are ignored because they have no physical reality
        addend1 = galGasVelRadiusKm * galGasVelRadiusKm     # = np.multiply()
        addend2 = -galSunRadiusKm2 * sinGLonDegRad * sinGLonDegRad
        addend3 = galSunRadiusKm * cosGLonDegRad
        addend1p2 = addend1 + addend2
        # trim negative addend1p2 before sqrt()
        addend1p2[addend1p2 < 0.] = np.nan

        # use positive sqrt()
        addend12 = np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        notIsNanPlotRadiiPos = np.logical_not(np.isnan(plotRadii))
        notIsNanPlotRadiiPosAny = notIsNanPlotRadiiPos.any()

        if notIsNanPlotRadiiPosAny:
            for gLatDeg in range(-90, 91):
                gLatDegP90 = gLatDeg + 90

                if velGLatP90Count[gLatDegP90] > 0:       # if column used
                    #gLatDegRad = gLatDeg * np.pi / 180.
                    gLatDegRad = gLatDeg * 0.01745329251
                    #gLatDegRad = gLatDeg * 0.01745329251 * 4.

                    cosGLatDegRad = math.cos(gLatDegRad)
                    sinGLatDegRad = math.sin(gLatDegRad)

                    # plot a radius, but not an edge
                    gLatDegRadMany = np.full(fileFreqBinQty, gLatDegRad)

                    # append only those x values where corresponding plotRadii is not a nan
                    #x = plotRadii * cos(gLatDeg - 90.)
                    #x = plotRadii * sin(gLatDegRad)
                    #x = plotRadii * sinGLatDegRad
                    x += (-plotRadii[notIsNanPlotRadiiPos] * sinGLatDegRad).tolist()

                    # append only those y values where corresponding plotRadii is not a nan
                    #y = plotRadii * sin(gLatDeg - 90.)
                    #y = plotRadii * -cos(gLatDegRad)
                    #y = plotRadii * -cosGLatDegRad
                    #y += (-plotRadii[notIsNanPlotRadiiPos] * -cosGLatDegRad - galSunRadiusKpc).tolist()
                    y += (-plotRadii[notIsNanPlotRadiiPos] * -cosGLatDegRad).tolist()

                    # append only those z values where corresponding plotRadii is not a nan
                    z += velGLatP90[:,gLatDegP90][notIsNanPlotRadiiPos].tolist()

        # use negative sqrt()
        addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        notIsNanPlotRadiiNeg = np.logical_not(np.isnan(plotRadii))
        
        if notIsNanPlotRadiiNeg.any():
            for gLatDeg in range(-90, 91):
                gLatDegP90 = gLatDeg + 90

                if velGLatP90Count[gLatDegP90] > 0:       # if column used
                    #gLatDegRad = gLatDeg * np.pi / 180.
                    gLatDegRad = gLatDeg * 0.01745329251

                    cosGLatDegRad = math.cos(gLatDegRad)
                    sinGLatDegRad = math.sin(gLatDegRad)

                    # plot a radius, but not an edge
                    gLatDegRadMany = np.full(fileFreqBinQty, gLatDegRad)

                    # append only those x values where corresponding plotRadii is not a nan
                    # append only those x values where corresponding plotRadii is not a nan
                    #x = plotRadii * cos(gLatDeg - 90.)
                    #x = plotRadii * sin(gLatDegRad)
                    #x = plotRadii * sinGLatDegRad
                    x += (-plotRadii[notIsNanPlotRadiiNeg] * sinGLatDegRad).tolist()

                    # append only those y values where corresponding plotRadii is not a nan
                    #y = plotRadii * sin(gLatDeg - 90.)
                    #y = plotRadii * -cos(gLatDegRad)
                    #y = plotRadii * -cosGLatDegRad
                    #y += (-plotRadii[notIsNanPlotRadiiNeg] * -cosGLatDegRad - galSunRadiusKpc).tolist()
                    y += (-plotRadii[notIsNanPlotRadiiNeg] * -cosGLatDegRad).tolist()

                    # append only those z values where corresponding plotRadii is not a nan
                    z += velGLatP90[:,gLatDegP90][notIsNanPlotRadiiNeg].tolist()

        elif not notIsNanPlotRadiiPosAny:
            # if not notIsNanPlotRadiiNeg.any() and not notIsNanPlotRadiiPosAny:
            # plot an edge radius, all as velGLatP90.min()
            for gLatDeg in range(-90, 91):
                gLatDegP90 = gLatDeg + 90

                #gLatDegRad = gLatDeg * np.pi / 180.
                gLatDegRad = gLatDeg * 0.01745329251

                cosGLatDegRad = math.cos(gLatDegRad)
                sinGLatDegRad = math.sin(gLatDegRad)

                # plot an edge radius, all as velGLatP90.min()
                x += (-plotRadiiEdgeMany * sinGLatDegRad).tolist()
                #y += (-plotRadiiEdgeMany * -cosGLatDegRad - galSunRadiusKpc).tolist()
                y += (-plotRadiiEdgeMany * -cosGLatDegRad).tolist()
                z += velGLatP90MinMany.tolist()

        #xi = np.linspace(-20., 20., 401)   # in kiloparsec
        #yi = np.linspace(20., -20., 401)   # in kiloparsec
        xi = np.linspace(20., -20., 401)   # in kiloparsec
        yi = np.linspace(-20., 20., 401)   # in kiloparsec
        xi, yi = np.meshgrid(xi, yi)
        ##zi = griddata((x, y), z, (xi, yi), method='linear')
        #x = -x
        #y = -y
        zi = griddata((y, x), z, (xi, yi), method='linear')
        # free memory
        x = []
        y = []
        z = []

        ###zi = gaussian_filter(zi, 9.)

        fig = plt.figure()
        ax = fig.add_subplot()

        img = plt.imshow(zi, aspect='auto', cmap=plt.get_cmap('gnuplot'))
        # Add a color bar which maps values to colors.
        plt.colorbar(img, orientation='vertical', pad=0.1)

        #polarPlot = ax.plot[[[0., 200], [400., 200.]], 'white')
        # horizonal thin white line
        plt.axhline(y = 200., linewidth=0.5, color='white')
        # vertical thin white line
        plt.axvline(x = 200., linewidth=0.5, color='white')

        # Plot yellow Sun at center
        polarPlot = ax.scatter(200., 200., c='black', s=120, alpha=1.)
        polarPlot = ax.scatter(200., 200., c='yellow', s=100, alpha=1.)

        plt.title(titleS)
        plt.xticks(range(0, 401, 50),
            ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        plt.yticks(range(400, -1, -50),
            ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        ax.set_facecolor("black")

        ax.set_xlabel('Distance (kiloparsecs)')
        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nSun = Yellow Dot')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')

        print('================== ezGLon580CsvFrac =', ezGLon580CsvFrac, '     ezGLon580Csv =', ezGLon580Csv)
        print('================== np.nanmax(zi) =', np.nanmax(zi))
        print('================== np.nanmin(zi) =', np.nanmin(zi))
        if -9999. < ezGLon580CsvFrac:
            ziNanmin = np.nanmin(zi)
            ezGLon580Csv = ezGLon580CsvFrac * (np.nanmax(zi) - ziNanmin) + ziNanmin


        print('================== ezGLon580CsvFrac =', ezGLon580CsvFrac, '     ezGLon580Csv =', ezGLon580Csv)
        if -9999. < ezGLon580Csv:
            plotNameCsv = plotName[:-3] + 'csv'
            #ziWhere = np.argwhere(ezGLon580Csv <= zi)
            ziEqualGreater = ezGLon580Csv <= zi
            #ziEqualGreaterX, ziEqualGreaterY = np.nonzero(ezGLon580Csv <= zi)
            ziEqualGreaterX, ziEqualGreaterY = np.nonzero(ziEqualGreater)
            #zi = zi[ezGLon580Csv <= zi]
            #row_indices, col_indices = np.indices(np.transpose(zi).shape)
            #ziCsv = np.column_stack((row_indices.ravel()[::-1], col_indices.ravel(), np.transpose(zi).ravel()))
            # following 3 parameters =
            #   radius in Galactic plane from Galactic Center,
            #   height above Galactic plane from Galactic Center,
            #   Galactic hydrogen density value
            #ziCsv = np.column_stack((np.max(ziEqualGreaterY) - ziEqualGreaterY, np.max(ziEqualGreaterX) / 2. - ziEqualGreaterX, \
            #    zi[ezGLon580Csv <= zi].ravel()))
            #ziCsv = np.column_stack((20. - ziEqualGreaterY, -ziEqualGreaterX, zi[ezGLon580Csv <= zi].ravel()))
            #ziCsv = np.column_stack((200. - ziEqualGreaterY, 200. - ziEqualGreaterX, zi[ezGLon580Csv <= zi].ravel()))
            # ezGLonGalCrossingGLonCenter

            ############################################ tedd
            piD180 = np.pi / 180.
            # map to galacticX and galacticY and galacticZ, with galacticZ perpendicular to Galactic plane, all centered on Sun
            # galacticX is kpc from Galactic Center, in Galactic plane, in direction of GLon 270 degrees
            # galacticX is (-(200. - ziEqualGreaterY)) * sin(ezGLonGalCrossingGLonCenter * 2. * np.pi() / 360.)
            # galacticX is (  ziEqualGreaterY - 200. ) * sin(ezGLonGalCrossingGLonCenter * np.pi() / 180.)
            # galacticX is (  ziEqualGreaterY - 200. ) * sin(ezGLonGalCrossingGLonCenter * piD180)
            #
            # galacticY is kpc from Galactic Center, in Galactic plane, in direction of GLon 0 degrees
            # galacticY is much like galacticX, but with cos() and a sign change
            # galacticY is (+(200. - ziEqualGreaterY)) * cos(ezGLonGalCrossingGLonCenter * 2. * np.pi() / 360.)
            # galacticY is (  200. - ziEqualGreaterY ) * cos(ezGLonGalCrossingGLonCenter * np.pi() / 180.)
            # galacticY is (  200. - ziEqualGreaterY ) * cos(ezGLonGalCrossingGLonCenter * piD180)
            #
            # galacticZ is kpc from Galactic Center, perpendicular to Galactic plane
            # galacticZ is 200. - ziEqualGreaterX
            #
            # dot color is Galactic hydrogen density value

            # define 2 X,Y,Z extremes to control X,Y,Z autoscaling, with minimal value normalized to 0.0
            #ziCsv = np.array([ [200, 200, 200, ezGLon580Csv], [-200, -200, -200, ezGLon580Csv] ])
            ziCsv = np.array([ [200., 200., 200., 0.], [-200., -200., -200., 0.] ])
            # concatenate data
            #print(ziCsv)
            #print(np.column_stack(( \
            #    (ziEqualGreaterY - 200.) * np.sin(ezGLonGalCrossingGLonCenter * piD180),
            #    (200. - ziEqualGreaterY) * np.cos(ezGLonGalCrossingGLonCenter * piD180),
            #    200. - ziEqualGreaterX,
            #    np.transpose(zi[ziEqualGreater]).ravel() )) )
            # from ezGal241024a,
            # galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
            # galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
            # galSunRadiusKpc = galSunRadiusKm * 3.24078e-17      # 7.971022488, in kiloparsecs
            # print('                         galSunRadiusKpc =', galSunRadiusKpc)

            # ziValues = zi thinned and normalized to 0.0 to 1.0
            #print('======================== zi =', zi)
            ziValues = zi[ziEqualGreater]
            ziValuesNanmin = np.nanmin(ziValues)
            ziValues = (ziValues - ziValuesNanmin) / (np.nanmax(ziValues) - ziValuesNanmin)
            #print('======================== ziValues =', ziValues)

            ziCsv = np.concatenate([ziCsv, np.column_stack(( \
                (ziEqualGreaterY - 200.) * np.sin(ezGLonGalCrossingGLonCenter * piD180),
                (200. - ziEqualGreaterY) * np.cos(ezGLonGalCrossingGLonCenter * piD180),
                200. - ziEqualGreaterX,
                np.transpose(ziValues).ravel() )) ])
            #    (200. - ziEqualGreaterY) * np.cos(ezGLonGalCrossingGLonCenter * piD180 - 10.),
            #    (200. - ziEqualGreaterY) * np.cos(ezGLonGalCrossingGLonCenter * piD180 - 7.971022488),
            #    np.transpose(zi[ziEqualGreater]).ravel() )) ])
            #print('======================== ziCsv =', ziCsv)

            # map to galacticX and galacticY and galacticZ, with galacticZ perpendicular to Galactic plane, all centered on Galactic center

            np.savetxt(plotNameCsv, ziCsv, delimiter=",")



def plotEzGLon581galArmsSunIMag5():
    # plot Interpolated Galactic Arms with Sun in center with Magnified x5 gLat angles

    global plotCountdown            # integer
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global ezGLonGalCrossingGLonCenter      # float 
    global ezGLonGalCrossingGLonNear        # float

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGLonDispGrid           # integer
    global ezGLonPlotRangeL         # integer list

    global fileFreqBinQty           # integer
    global velocityBin              # float array





#    global velGLonP180              # float 2d array
#    global velGLonP180Count         # integer array
#    global velGLonP180CountSum      # integer

    plotCountdown -= 1

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 581 and 581 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    #plotName = 'ezGLon581galArmsSunIMag5.png'
    #plotName = 'ezGLon581galArmsSunIMag5Xxxx.xXxxx.x.png'
    if 0 <= ezGLonGalCrossingGLonCenter:
        plotName = f'ezGLon581galArmsSunIMag5P{ezGLonGalCrossingGLonCenter:05.1f}'
    else:
        plotName = f'ezGLon581galArmsSunIMag5N{ezGLonGalCrossingGLonCenter:05.1f}'
    if 0 <= ezGLonGalCrossingGLonNear:
        plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
    else:
        plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

    plt.clf()

    if velGLatP90CountSum:         # if anything in velGLatP90 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusKpc = galSunRadiusKm * 3.24078e-17      # in kiloparsecs
        galSunRadiusPlotLimit = galSunRadiusKm * 4.

        x = []
        y = []
        z = []

        # longest plotRadii needed, to draw edge toward top right corner, at
        #   sqrt(20*20 + 30*30) is 36.06
        plotRadiiEdgeMany = np.linspace(0., 37., 371)       # each tenth of kiloparsec
        velGLatP90MinMany = np.full_like(plotRadiiEdgeMany, velGLatP90.min())

        # ezGLonGalCrossingGLonCenter is used to create plotRadii 
        #gLonDegRad = ezGLonGalCrossingGLonCenter * np.pi / 180.
        gLonDegRad = ezGLonGalCrossingGLonCenter * 0.01745329251

        cosGLonDegRad = math.cos(gLonDegRad)
        sinGLonDegRad = math.sin(gLonDegRad)

        # JJ's p54 Eq3
        #   R = R0*V0*sin(l) / ( V0*sin(l) + Vr )
        galGasVelRadiusKm = galSunRadiusKm * 220. * np.sin(gLonDegRad) \
            / (220. * np.sin(gLonDegRad) + velocityBin)   # in km
        # shape(galGasVelRadiusKm) = (256,)
        # but that denominator was often near zero, so trim +/- large galGasVelRadiusKm
        galGasVelRadiusKm[galSunRadiusPlotLimit  < galGasVelRadiusKm] = np.nan
        galGasVelRadiusKm[galGasVelRadiusKm < -galSunRadiusPlotLimit] = np.nan
        # trim negative galGasVelRadiusKm
        galGasVelRadiusKm[galGasVelRadiusKm < 0.] = np.nan

        # JJ's p54 Eq4
        #   r = +-sqrt( R*R     - R0*R0*sin(l)*sin(l) ) + R0*cos(l)
        #   r = +-sqrt( addend1 + addend2             ) + addend3
        #   but negative values of r are ignored because they have no physical reality
        addend1 = galGasVelRadiusKm * galGasVelRadiusKm     # = np.multiply()
        addend2 = -galSunRadiusKm2 * sinGLonDegRad * sinGLonDegRad
        addend3 = galSunRadiusKm * cosGLonDegRad
        addend1p2 = addend1 + addend2
        # trim negative addend1p2 before sqrt()
        addend1p2[addend1p2 < 0.] = np.nan

        # use positive sqrt()
        addend12 = np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        notIsNanPlotRadiiPos = np.logical_not(np.isnan(plotRadii))
        notIsNanPlotRadiiPosAny = notIsNanPlotRadiiPos.any()

        if notIsNanPlotRadiiPosAny:
            #for gLatDeg in range(-90, 91):
            for gLatDeg in range(-18, 19):
                gLatDegP90 = gLatDeg + 90

                if velGLatP90Count[gLatDegP90] > 0:       # if column used
                    #gLatDegRad = gLatDeg * np.pi / 180.
                    #gLatDegRad = gLatDeg * 0.01745329251
                    gLatDegRad = gLatDeg * 0.01745329251 * 5.   # Mag5

                    cosGLatDegRad = math.cos(gLatDegRad)
                    sinGLatDegRad = math.sin(gLatDegRad)

                    # plot a radius, but not an edge
                    gLatDegRadMany = np.full(fileFreqBinQty, gLatDegRad)

                    # append only those x values where corresponding plotRadii is not a nan
                    #x = plotRadii * cos(gLatDeg - 90.)
                    #x = plotRadii * sin(gLatDegRad)
                    #x = plotRadii * sinGLatDegRad
                    x += (-plotRadii[notIsNanPlotRadiiPos] * sinGLatDegRad).tolist()

                    # append only those y values where corresponding plotRadii is not a nan
                    #y = plotRadii * sin(gLatDeg - 90.)
                    #y = plotRadii * -cos(gLatDegRad)
                    #y = plotRadii * -cosGLatDegRad
                    #y += (-plotRadii[notIsNanPlotRadiiPos] * -cosGLatDegRad - galSunRadiusKpc).tolist()
                    y += (-plotRadii[notIsNanPlotRadiiPos] * -cosGLatDegRad).tolist()

                    # append only those z values where corresponding plotRadii is not a nan
                    z += velGLatP90[:,gLatDegP90][notIsNanPlotRadiiPos].tolist()

        # use negative sqrt()
        addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        notIsNanPlotRadiiNeg = np.logical_not(np.isnan(plotRadii))
        
        if notIsNanPlotRadiiNeg.any():
            #for gLatDeg in range(-90, 91):
            for gLatDeg in range(-18, 19):
                gLatDegP90 = gLatDeg + 90

                if velGLatP90Count[gLatDegP90] > 0:       # if column used
                    #gLatDegRad = gLatDeg * np.pi / 180.
                    gLatDegRad = gLatDeg * 0.01745329251

                    cosGLatDegRad = math.cos(gLatDegRad)
                    sinGLatDegRad = math.sin(gLatDegRad)

                    # plot a radius, but not an edge
                    gLatDegRadMany = np.full(fileFreqBinQty, gLatDegRad)

                    # append only those x values where corresponding plotRadii is not a nan
                    # append only those x values where corresponding plotRadii is not a nan
                    #x = plotRadii * cos(gLatDeg - 90.)
                    #x = plotRadii * sin(gLatDegRad)
                    #x = plotRadii * sinGLatDegRad
                    x += (-plotRadii[notIsNanPlotRadiiNeg] * sinGLatDegRad).tolist()

                    # append only those y values where corresponding plotRadii is not a nan
                    #y = plotRadii * sin(gLatDeg - 90.)
                    #y = plotRadii * -cos(gLatDegRad)
                    #y = plotRadii * -cosGLatDegRad
                    #y += (-plotRadii[notIsNanPlotRadiiNeg] * -cosGLatDegRad - galSunRadiusKpc).tolist()
                    y += (-plotRadii[notIsNanPlotRadiiNeg] * -cosGLatDegRad).tolist()

                    # append only those z values where corresponding plotRadii is not a nan
                    z += velGLatP90[:,gLatDegP90][notIsNanPlotRadiiNeg].tolist()

        elif not notIsNanPlotRadiiPosAny:
            # if not notIsNanPlotRadiiNeg.any() and not notIsNanPlotRadiiPosAny:
            # plot an edge radius, all as velGLatP90.min()
            #for gLatDeg in range(-90, 91):
            for gLatDeg in range(-18, 19):
                gLatDegP90 = gLatDeg + 90

                #gLatDegRad = gLatDeg * np.pi / 180.
                gLatDegRad = gLatDeg * 0.01745329251

                cosGLatDegRad = math.cos(gLatDegRad)
                sinGLatDegRad = math.sin(gLatDegRad)

                # plot an edge radius, all as velGLatP90.min()
                x += (-plotRadiiEdgeMany * sinGLatDegRad).tolist()
                #y += (-plotRadiiEdgeMany * -cosGLatDegRad - galSunRadiusKpc).tolist()
                y += (-plotRadiiEdgeMany * -cosGLatDegRad).tolist()
                z += velGLatP90MinMany.tolist()

        #xi = np.linspace(-20., 20., 401)   # in kiloparsec
        #yi = np.linspace(20., -20., 401)   # in kiloparsec
        xi = np.linspace(20., -20., 401)   # in kiloparsec
        yi = np.linspace(-20., 20., 401)   # in kiloparsec
        xi, yi = np.meshgrid(xi, yi)
        ##zi = griddata((x, y), z, (xi, yi), method='linear')
        #x = -x
        #y = -y
        zi = griddata((y, x), z, (xi, yi), method='linear')

        # free memory
        x = []
        y = []
        z = []
        xi = []
        yi = []

        ###zi = gaussian_filter(zi, 9.)

        fig = plt.figure()
        ax = fig.add_subplot()

        img = plt.imshow(zi, aspect='auto', cmap=plt.get_cmap('gnuplot'))
        # Add a color bar which maps values to colors.
        plt.colorbar(img, orientation='vertical', pad=0.1)

        #polarPlot = ax.plot[[[0., 200], [400., 200.]], 'white')
        # horizonal thin white line
        plt.axhline(y = 200., linewidth=0.5, color='white')
        # vertical thin white line
        plt.axvline(x = 200., linewidth=0.5, color='white')

        # Plot yellow Sun at center
        polarPlot = ax.scatter(200., 200., c='black', s=120, alpha=1.)
        polarPlot = ax.scatter(200., 200., c='yellow', s=100, alpha=1.)

        plt.title(titleS)
        plt.xticks(range(0, 401, 50),
            ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        plt.yticks(range(400, -1, -50),
            ['  -4', '-3', '-2', '-1', '0', '1', '2', '3', '4'])
        #    ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        ax.set_facecolor("black")

        ax.set_xlabel('Distance (kiloparsecs)')
        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nSun = Yellow Dot, GLat Magnification = 5')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzGLon582galArmsSunRIMag5():
    # plot Interpolated Galactic Arms with Sun at right with Magnified x5 gLat angles

    global plotCountdown            # integer
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global ezGLon582Csv                     # float
    global ezGLonGalCrossingGLonCenter      # float 
    global ezGLonGalCrossingGLonNear        # float

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGLonDispGrid           # integer
    global ezGLonPlotRangeL         # integer list

    global fileFreqBinQty           # integer
    global velocityBin              # float array





#    global velGLonP180              # float 2d array
#    global velGLonP180Count         # integer array
#    global velGLonP180CountSum      # integer

    plotCountdown -= 1

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 582 and 582 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    #plotName = 'ezGLon582galArmsSunRIMag5.png'
    #plotName = 'ezGLon582galArmsSunRIMag5Xxxx.xXxxx.x.png'
    if 0 <= ezGLonGalCrossingGLonCenter:
        plotName = f'ezGLon582galArmsSunRIMag5P{ezGLonGalCrossingGLonCenter:05.1f}'
    else:
        plotName = f'ezGLon582galArmsSunRIMag5N{ezGLonGalCrossingGLonCenter:05.1f}'
    if 0 <= ezGLonGalCrossingGLonNear:
        plotName += f'P{ezGLonGalCrossingGLonNear:05.1f}.png'
    else:
        plotName += f'N{ezGLonGalCrossingGLonNear:05.1f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ================================')

    plt.clf()

    if velGLatP90CountSum:         # if anything in velGLatP90 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusKpc = galSunRadiusKm * 3.24078e-17      # in kiloparsecs
        galSunRadiusPlotLimit = galSunRadiusKm * 4.

        x = []
        y = []
        z = []

        # longest plotRadii needed, to draw edge toward top right corner, at
        #   sqrt(20*20 + 30*30) is 36.06
        plotRadiiEdgeMany = np.linspace(0., 37., 371)       # each tenth of kiloparsec
        velGLatP90MinMany = np.full_like(plotRadiiEdgeMany, velGLatP90.min())

        # ezGLonGalCrossingGLonCenter is used to create plotRadii 
        #gLonDegRad = ezGLonGalCrossingGLonCenter * np.pi / 180.
        gLonDegRad = ezGLonGalCrossingGLonCenter * 0.01745329251

        cosGLonDegRad = math.cos(gLonDegRad)
        sinGLonDegRad = math.sin(gLonDegRad)

        # JJ's p54 Eq3
        #   R = R0*V0*sin(l) / ( V0*sin(l) + Vr )
        galGasVelRadiusKm = galSunRadiusKm * 220. * np.sin(gLonDegRad) \
            / (220. * np.sin(gLonDegRad) + velocityBin)   # in km
        # shape(galGasVelRadiusKm) = (256,)
        # but that denominator was often near zero, so trim +/- large galGasVelRadiusKm
        galGasVelRadiusKm[galSunRadiusPlotLimit  < galGasVelRadiusKm] = np.nan
        galGasVelRadiusKm[galGasVelRadiusKm < -galSunRadiusPlotLimit] = np.nan
        # trim negative galGasVelRadiusKm
        galGasVelRadiusKm[galGasVelRadiusKm < 0.] = np.nan

        # JJ's p54 Eq4
        #   r = +-sqrt( R*R     - R0*R0*sin(l)*sin(l) ) + R0*cos(l)
        #   r = +-sqrt( addend1 + addend2             ) + addend3
        #   but negative values of r are ignored because they have no physical reality
        addend1 = galGasVelRadiusKm * galGasVelRadiusKm     # = np.multiply()
        addend2 = -galSunRadiusKm2 * sinGLonDegRad * sinGLonDegRad
        addend3 = galSunRadiusKm * cosGLonDegRad
        addend1p2 = addend1 + addend2
        # trim negative addend1p2 before sqrt()
        addend1p2[addend1p2 < 0.] = np.nan

        # use positive sqrt()
        addend12 = np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        notIsNanPlotRadiiPos = np.logical_not(np.isnan(plotRadii))
        notIsNanPlotRadiiPosAny = notIsNanPlotRadiiPos.any()

        if notIsNanPlotRadiiPosAny:
            #for gLatDeg in range(-90, 91):
            for gLatDeg in range(-18, 19):
                gLatDegP90 = gLatDeg + 90

                if velGLatP90Count[gLatDegP90] > 0:       # if column used
                    #gLatDegRad = gLatDeg * np.pi / 180.
                    #gLatDegRad = gLatDeg * 0.01745329251
                    gLatDegRad = gLatDeg * 0.01745329251 * 5.   # Mag5

                    cosGLatDegRad = math.cos(gLatDegRad)
                    sinGLatDegRad = math.sin(gLatDegRad)

                    # plot a radius, but not an edge
                    gLatDegRadMany = np.full(fileFreqBinQty, gLatDegRad)

                    # append only those x values where corresponding plotRadii is not a nan
                    #x = plotRadii * cos(gLatDeg - 90.)
                    #x = plotRadii * sin(gLatDegRad)
                    #x = plotRadii * sinGLatDegRad
                    x += (-plotRadii[notIsNanPlotRadiiPos] * sinGLatDegRad).tolist()

                    # append only those y values where corresponding plotRadii is not a nan
                    #y = plotRadii * sin(gLatDeg - 90.)
                    #y = plotRadii * -cos(gLatDegRad)
                    #y = plotRadii * -cosGLatDegRad
                    #y += (-plotRadii[notIsNanPlotRadiiPos] * -cosGLatDegRad - galSunRadiusKpc).tolist()
                    y += (-plotRadii[notIsNanPlotRadiiPos] * -cosGLatDegRad).tolist()

                    # append only those z values where corresponding plotRadii is not a nan
                    z += velGLatP90[:,gLatDegP90][notIsNanPlotRadiiPos].tolist()

        # use negative sqrt()
        addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
        plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

        # trim negative plotRadii
        plotRadii[plotRadii < 0.] = np.nan

        notIsNanPlotRadiiNeg = np.logical_not(np.isnan(plotRadii))
        
        if notIsNanPlotRadiiNeg.any():
            for gLatDeg in range(-90, 91):
                gLatDegP90 = gLatDeg + 90

                if velGLatP90Count[gLatDegP90] > 0:       # if column used
                    #gLatDegRad = gLatDeg * np.pi / 180.
                    gLatDegRad = gLatDeg * 0.01745329251

                    cosGLatDegRad = math.cos(gLatDegRad)
                    sinGLatDegRad = math.sin(gLatDegRad)

                    # plot a radius, but not an edge
                    gLatDegRadMany = np.full(fileFreqBinQty, gLatDegRad)

                    # append only those x values where corresponding plotRadii is not a nan
                    # append only those x values where corresponding plotRadii is not a nan
                    #x = plotRadii * cos(gLatDeg - 90.)
                    #x = plotRadii * sin(gLatDegRad)
                    #x = plotRadii * sinGLatDegRad
                    x += (-plotRadii[notIsNanPlotRadiiNeg] * sinGLatDegRad).tolist()

                    # append only those y values where corresponding plotRadii is not a nan
                    #y = plotRadii * sin(gLatDeg - 90.)
                    #y = plotRadii * -cos(gLatDegRad)
                    #y = plotRadii * -cosGLatDegRad
                    #y += (-plotRadii[notIsNanPlotRadiiNeg] * -cosGLatDegRad - galSunRadiusKpc).tolist()
                    y += (-plotRadii[notIsNanPlotRadiiNeg] * -cosGLatDegRad).tolist()

                    # append only those z values where corresponding plotRadii is not a nan
                    z += velGLatP90[:,gLatDegP90][notIsNanPlotRadiiNeg].tolist()

        elif not notIsNanPlotRadiiPosAny:
            # if not notIsNanPlotRadiiNeg.any() and not notIsNanPlotRadiiPosAny:
            # plot an edge radius, all as velGLatP90.min()
            for gLatDeg in range(-90, 91):
                gLatDegP90 = gLatDeg + 90

                #gLatDegRad = gLatDeg * np.pi / 180.
                gLatDegRad = gLatDeg * 0.01745329251

                cosGLatDegRad = math.cos(gLatDegRad)
                sinGLatDegRad = math.sin(gLatDegRad)

                # plot an edge radius, all as velGLatP90.min()
                x += (-plotRadiiEdgeMany * sinGLatDegRad).tolist()
                #y += (-plotRadiiEdgeMany * -cosGLatDegRad - galSunRadiusKpc).tolist()
                y += (-plotRadiiEdgeMany * -cosGLatDegRad).tolist()
                z += velGLatP90MinMany.tolist()

        #xi = np.linspace(-20., 20., 401)   # in kiloparsec
        #yi = np.linspace(20., -20., 401)   # in kiloparsec
        #xi = np.linspace(20., -20., 401)   # in kiloparsec
        xi = np.linspace(40., 0., 401)   # in kiloparsec, Sun to the right
        yi = np.linspace(-20., 20., 401)   # in kiloparsec
        xi, yi = np.meshgrid(xi, yi)
        ##zi = griddata((x, y), z, (xi, yi), method='linear')
        #x = -x
        #y = -y
        zi = griddata((y, x), z, (xi, yi), method='linear')
        # free memory
        x = []
        y = []
        z = []
        xi = []
        yi = []

        ###zi = gaussian_filter(zi, 9.)

        fig = plt.figure()
        ax = fig.add_subplot()

        img = plt.imshow(zi, aspect='auto', cmap=plt.get_cmap('gnuplot'))
        # Add a color bar which maps values to colors.
        plt.colorbar(img, orientation='vertical', pad=0.1)

        #polarPlot = ax.plot[[[0., 200], [400., 200.]], 'white')
        # horizonal thin white line
        plt.axhline(y = 200., linewidth=0.5, color='white')
        # vertical thin white line
        #plt.axvline(x = 200., linewidth=0.5, color='white')

        # Plot yellow Sun at the right
        polarPlot = ax.scatter(400., 200., c='black', s=120, alpha=1.)
        polarPlot = ax.scatter(400., 200., c='yellow', s=100, alpha=1.)

        plt.title(titleS)
        plt.xticks(range(0, 401, 50),
            ['-40', '-35', '-30', '-25', '-20', '-15', '-10', '-5', '0'])
        #    ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        plt.yticks(range(400, -1, -50),
            ['  -4', '-3', '-2', '-1', '0', '1', '2', '3', '4'])
        #    ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        ax.set_facecolor("black")

        ax.set_xlabel('Distance (kiloparsecs)')
        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nSun = Yellow Dot, GLat Magnification = 5')

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')

        if -9999. < ezGLon582Csv:
            plotNameCsv = plotName[:-3] + 'csv'
            #ziWhere = np.argwhere(ezGLon582Csv <= zi)
            ziEqualGreaterX, ziEqualGreaterY = np.nonzero(ezGLon582Csv <= zi)
            #zi = zi[ezGLon582Csv <= zi]
            #row_indices, col_indices = np.indices(np.transpose(zi).shape)
            #ziCsv = np.column_stack((row_indices.ravel()[::-1], col_indices.ravel(), np.transpose(zi).ravel()))
            ziCsv = np.column_stack((np.max(ziEqualGreaterY) - ziEqualGreaterY, np.max(ziEqualGreaterX) / 2. - ziEqualGreaterX, \
                zi[ezGLon582Csv <= zi].ravel()))
            # ezGLonGalCrossingGLonCenter
            np.savetxt(plotNameCsv, ziCsv, delimiter=",")
            # free memory
            #ziCsv = []



def plotEzGLon60XgLonSpectra():

    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global antXTVTName              # string

    global velocitySpanMax          # float
    global velocityBin              # float array

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGLonPlotRangeL         # integer list

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 604 and 601 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    plt.clf()
    plotName = 'ezGLon60XgLonSpectra.png'

    velGLatP90CountNonzero = np.count_nonzero(velGLatP90Count)
    #print(' velGLatP90Count =', velGLatP90Count)
    print('                         velGLatP90CountNonzero =', velGLatP90CountNonzero, 'of', len(velGLatP90Count) )

    velGLatP90CountNonzeroIndex = np.nonzero(velGLatP90Count)
    #print(' velGLatP90CountNonzeroIndex =', velGLatP90CountNonzeroIndex)
    #print(' velGLatP90CountNonzeroIndex[0] =', velGLatP90CountNonzeroIndex[0])

    #velGLatP90MaxIndex = np.argmax(velGLatP90, axis=0)
    velGLatP90Max = velGLatP90.max()
    print('                         gLon of maximum spectrum value =', np.argmax(np.argmax(velGLatP90 == velGLatP90Max, axis=0)) - 180)

    #yLimMax = 1.05 * velGLatP90Max
    yLimMax = 1.01 * velGLatP90Max
    print('                         yLimMax =', yLimMax)

    # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
    #yLimMin = 0.95 * velGLatP90.min()
    yLimMin = 0.99 * velGLatP90.min()
    print('                         yLimMin =', yLimMin)

    # Galactic quadrants 1 through 4
    for gQuadrant in range(1, 5):

        plotNumber = 600 + gQuadrant        # for this Galactic quadrant

        plotCountdown -= 1

        if ezGLonPlotRangeL[0] <= plotNumber and plotNumber <= ezGLonPlotRangeL[1]:

            #plotName = 'ezGal600gLonSpectraQ{gQuadrant}.png'
            plotName = f'ezGal{plotNumber}gLonSpectra.png'
            print()
            print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ============')

            plt.clf()

            fig, axs = plt.subplots(9, 10, figsize=(10, 6), layout='constrained')
            #print(' axs.flat[0:5] =', axs.flat[0:5])
            axsFlat = axs.flat

            fig.suptitle(titleS + f'\nAverage {antXTVTName} Velocity Spectra for' \
                + f' Galactic Longitudes (Galactic Quadrant {gQuadrant})', fontsize=12)

            gLonP180Start = [-1, 180, 270, 0, 90][gQuadrant]

            # 0 through 90 in this quadrant
            for i in range(90):

                gLonP180 = gLonP180Start + i
                #print(' gLonP180 =', gLonP180)

                #print(' i =', i)
                ax = axsFlat[i]

                if velGLatP90Count[gLonP180]:
                    ax.plot(velocityBin, velGLatP90[:, gLonP180], linewidth=0.5)
                    ax.grid(1)
            
                    ax.set_xlim(-velocitySpanMax, velocitySpanMax)
            
                    ax.set_ylim(yLimMin, yLimMax)

                    ax.tick_params('both',labelsize=5) 

                ax.set_xticks([], [])
                ax.set_yticks([], [])
                ax.axvline(linewidth=0.5, color='b')

                ax.text(0.02, 0.85, 'gLon', fontsize=5, transform=ax.transAxes)

                # add text with form of '+nnn' or '-nnn' degrees
                if gLonP180 < 180:
                    gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
                else:
                    gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros
                ax.text(0.99, 0.85, gLonDegS, fontsize=5, transform=ax.transAxes, horizontalalignment='right')

            if os.path.exists(plotName): # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzGLon605gLonSpectraCompare():
    # Compare to Page 48 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf
    # 230416 LTO15hcg plot is fairly close
    
    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global antXTVTName              # string

    global velocitySpanMax          # float
    global velocityBin              # float array

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGLonPlotRangeL         # integer list

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 605 and 605 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    plt.clf()
    plotName = 'ezGLon605gLonSpectraCompare.png'

    velGLatP90CountNonzero = np.count_nonzero(velGLatP90Count)
    #print(' velGLatP90Count =', velGLatP90Count)
    print('                         velGLatP90CountNonzero =', velGLatP90CountNonzero, 'of', len(velGLatP90Count) )

    velGLatP90CountNonzeroIndex = np.nonzero(velGLatP90Count)

    velGLatP90Max = velGLatP90.max()
    print('                         gLon of maximum spectrum value =', np.argmax(np.argmax(velGLatP90 == velGLatP90Max, axis=0)) - 180)

    yLimMax = 1.01 * velGLatP90Max
    print('                         yLimMax =', yLimMax)

    # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
    yLimMin = 0.99 * velGLatP90.min()
    print('                         yLimMin =', yLimMin)

    plotNumber = 605

    plotCountdown -= 1

    if ezGLonPlotRangeL[0] <= plotNumber and plotNumber <= ezGLonPlotRangeL[1] and velGLatP90CountSum:

        #plotName = 'ezGal600gLonSpectraQ{gQuadrant}.png'
        plotName = f'ezGal{plotNumber}gLonSpectra.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ============')

        plt.clf()

        fig, axs = plt.subplots(6, 10, figsize=(10, 6), layout='constrained')
        axsFlat = axs.flat

        fig.suptitle(titleS + f'\nAverage {antXTVTName} Velocity Spectra for' \
            + ' Galactic Longitudes 4 to 240', fontsize=12)

        # 4 through 241 by 4
        for i in range(60):

            gLonP180 = 184 + i + i + i + i
            if 360 < gLonP180:
                gLonP180 -= 360

            ax = axsFlat[i]

            if velGLatP90Count[gLonP180]:
                ax.plot(velocityBin, velGLatP90[:, gLonP180], linewidth=0.5)
                ax.grid(1)
        
                ax.set_xlim(-velocitySpanMax, velocitySpanMax)
        
                ax.set_ylim(yLimMin, yLimMax)

                ax.tick_params('both',labelsize=5) 

            ax.set_xticks([], [])
            ax.set_yticks([], [])
            ax.axvline(linewidth=0.5, color='b')

            ax.text(0.02, 0.85, 'gLon', fontsize=5, transform=ax.transAxes)

            # add text with form of '+nnn' or '-nnn' degrees
            if gLonP180 < 180:
                gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
            else:
                gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros
            ax.text(0.99, 0.85, gLonDegS, fontsize=5, transform=ax.transAxes, horizontalalignment='right')

        if os.path.exists(plotName): # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzGLon61XgLonSpectraCascade():

    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global antXTVTName              # string

    global velocitySpanMax          # float                 creation
    global velocityBin              # float array           creation

    global ezGal61XGain             # float

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGLonPlotRangeL         # integer list

    # if not wanted, or nothing in velGLatP90 to save or plot
    if not (ezGLonPlotRangeL[0] <= 614 and 610 <= ezGLonPlotRangeL[1] and velGLatP90CountSum):
        return(0)       # plot not needed

    plt.clf()
    plotName = 'ezGal61XgLonSpectraCascade.png'

    velGLatP90CountNonzero = np.count_nonzero(velGLatP90Count)
    #print(' velGLatP90Count =', velGLatP90Count)
    print('                         velGLatP90CountNonzero =', velGLatP90CountNonzero, 'of', len(velGLatP90Count) )

    velGLatP90CountNonzeroIndex = np.nonzero(velGLatP90Count)
    #print(' velGLatP90CountNonzeroIndex =', velGLatP90CountNonzeroIndex)
    #print(' velGLatP90CountNonzeroIndex[0] =', velGLatP90CountNonzeroIndex[0])

    #velGLatP90MaxIndex = np.argmax(velGLatP90, axis=0)
    velGLatP90Max = velGLatP90.max()
    print('                         gLon of maximum spectrum value =', np.argmax(np.argmax(velGLatP90 == velGLatP90Max, axis=0)) - 180)

    yLimMax = 1.01 * velGLatP90Max
    print('                         yLimMax =', yLimMax)

    # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
    yLimMin = 0.99 * velGLatP90.min()
    print('                         yLimMin =', yLimMin)

    # Galactic quadrants 0 (all) and quadrants 1 through 4
    for gQuadrant in range(0, 5):

        plotNumber = 610 + gQuadrant        # for this Galactic quadrant

        plotCountdown -= 1

        if ezGLonPlotRangeL[0] <= plotNumber and plotNumber <= ezGLonPlotRangeL[1]:

            plotName = f'ezGal{plotNumber}gLonSpectraCascade.png'
            print()
            print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ============')

            plt.clf()

            # assign according to value of gQuadrant
            gLonP180Start = [180, 180, 270,  0,  90][gQuadrant]
            gLonP180Stop  = [539, 269, 359, 89, 179][gQuadrant]
            gLonP180Qty   = [360,  90,  90, 90,  90][gQuadrant]
            yMax          = [179,  89, 179, -91, -1][gQuadrant]

            # https://stackoverflow.com/questions/29883344/how-can-i-make-waterfall-plots-in-matplotlib-and-python-2-7
            # https://stackoverflow.com/questions/4804005/matplotlib-figure-facecolor-background-color

            fig = plt.figure()
            ax = fig.add_subplot()

            # ezGal61XGain is the maximum height in ezGal61XgLonSpectraCascade plots
            gain = ezGal61XGain / velGLatP90Max

            for i in range(gLonP180Qty):
                # Vertical offset each line up by this offset amount: but we want the first traces plotted
                # at the top of the chart, and to work our way down
                gLonP180 = gLonP180Stop - i     # gLonP180 decreases from gLonP180Stop down to include gLonP180Start

                # Plot the line, and fill white under it, and increase the z-order each time
                #   so that lower lines and their fills are plotted on top of higher lines
                if gQuadrant:
                    # Galactic quadrants 1 through 4
                    # for the trace with the velGLatP90Max value,
                    #        (velGLatP90[:,gLonP180] * gain - gain) is the trace's baseline
                    y = (velGLatP90[:,gLonP180] * gain - gain) + (gLonP180 - 180.)
                else:
                    # Galactic quadrant "0" (all quadrants)
                    y = (velGLatP90[:,gLonP180-180] * gain - gain) + (gLonP180 - 360.)

                # what to do with velocity spectra that do not wiggle, and are unchanging
                if 1:
                    # plot all velocity spectra
                    yMax = max(yMax, y.max())

                    ax.plot(velocityBin, y, 'black', linewidth=0.5, zorder=i+i)
                
                    # draw a vertical thin white line below every velocity spectra data point
                    ax.fill_between(velocityBin, y, y-gain, facecolor='white', linewidth=0, zorder=i+i+1)
                else:
                    # do not plot velocity spectra with unchanging (missing?) velocity
                    yMaxThis = y.max()
                    yMinThis = y.min()
                    yMax = max(yMax, yMaxThis)

                    # plot only velocity spectra with changing velocity
                    if yMinThis < yMaxThis:
                        # velocity changes, plot it
                        ax.plot(velocityBin, y, 'black', linewidth=0.5, zorder=i+i)
                    
                        # draw a vertical thin white line below every velocity spectra data point
                        ax.fill_between(velocityBin, y, y-gain, facecolor='white', linewidth=0, zorder=i+i+1)

            plt.title(titleS)

            plt.xlabel('Velocity (km/s)')
            #velocitySpanMax = +dopplerSpanD2 * (299792458. / freqCenter) / 1000.  # = 253.273324388 km/s
            plt.xlim(-velocitySpanMax, velocitySpanMax)

            if gQuadrant:
                # Galactic quadrants 1 through 4
                plt.ylabel(f'Galactic Quadrant {gQuadrant}')
                plt.ylim(gLonP180Start-182, yMax+2)
            else:
                # Galactic quadrants 0 (all)
                plt.ylabel('Galactic Longitudes   (-180 thru +179 degrees)')
                plt.ylim(-186, yMax+6)

            if os.path.exists(plotName): # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), transparent=True)



def plotEzGLon710gLonDegP180_nnnByFreqBinAvg():

    global velGLatP90               # float 2d array
    global velGLatP90Count          # integer array
    global velGLatP90CountSum       # integer
    global antXTVTName              # string

    global velocitySpanMax          # float
    global velocityBin              # float array

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGLonPlotRangeL         # integer list

    # if anything in velGLatP90 to plot
    if ezGLonPlotRangeL[0] <= 710 and 710 <= ezGLonPlotRangeL[1] and velGLatP90CountSum:
        velGLatP90CountNonzero = np.count_nonzero(velGLatP90Count)
        print('                         velGLatP90CountNonzero =', velGLatP90CountNonzero, 'of', len(velGLatP90Count) )
        #plotCountdown += np.count_nonzero(velGLatP90Count)
        plotCountdown = velGLatP90CountNonzero

        if 1:
            # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
            yLimMin = 0.95 * velGLatP90.min()
            print('                         yLimMin =', yLimMin)

            yLimMax = 1.05 * velGLatP90.max()
            print('                         yLimMax =', yLimMax)

        for gLonP180 in range(361):                 # for every column, RtoL
            if velGLatP90Count[gLonP180]:      # if column used

                # create plotName with form of 'ezGal710gLonDegP180_nnnByFreqBinAvg.png'
                plotName = f'ezGLon710gLonDegP180_{gLonP180:03d}ByFreqBinAvg.png'
                print()
                print('  ' + str(plotCountdown) + ' plotting ' + plotName + ' ============')
                print('                         gLonP180 =', gLonP180)
                print('                         gLonP180 - 180 =', gLonP180 - 180)
                print('                         velGLatP90Count[gLonP180] =', velGLatP90Count[gLonP180])
                plotCountdown -= 1
                plt.clf()

                # velGLatP90 stores increasing velocity
                plt.plot(velocityBin, velGLatP90[:, gLonP180])

                plt.title(titleS)
                plt.grid(ezGalDispGrid)

                plt.xlabel('Velocity (km/s)')
                plt.xlim(-velocitySpanMax, velocitySpanMax)

                if 0:
                    # new ylim for each ezGal710gLonDegP180_nnnByFreqBinAvg plot
                    yLimMin = 0.95 * velGLatP90[:, gLonP180].min()
                    print('                         yLimMin =', yLimMin)

                    yLimMax = 1.05 * velGLatP90[:, gLonP180].max()
                    print('                         yLimMax =', yLimMax)

                plt.ylim(yLimMin, yLimMax)

                # create gLonDegS with form of '+nnn' or '-nnn' degrees
                if gLonP180 < 180:
                    gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
                else:
                    gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros

                plt.ylabel(f'{antXTVTName} Average Velocity Spectrum' \
                    + f'\n\nfor Galactic Longitude = {gLonDegS} deg', \
                    rotation=90, verticalalignment='bottom')

                if os.path.exists(plotName): # to force plot file date update, if file exists, delete it
                    os.remove(plotName)
                plt.savefig(plotName, dpi=300, bbox_inches='tight')



def printGoodbye(startTime):

    global programRevision          # string
    global commandString            # string
    global ezGLonPlotRangeL         # integer list

    # print status
    if 0:
        print()
        print('   ezRAObsName      =', ezRAObsName)
        if 0:
            print('   ezGalUseSamplesRawL      =', ezGalUseSamplesRawL)
            print('   ezGalAddAzDeg            =', ezGalAddAzDeg)
            print('   ezGalAddElDeg            =', ezGalAddElDeg)

            print('   ezGalHideFreqBinL        =', ezGalHideFreqBinL)
            print('   ezGalRfiLim              =', ezGalRfiLim)
            print('   ezGalUseSamplesAntL      =', ezGalUseSamplesAntL)
            print('   ezGalDispGrid            =', ezGalDispGrid)
            print('   ezGLonGalCrossingGLonCenter =', ezGLonGalCrossingGLonCenter)
            print('   ezGalDispFreqBin         =', ezGalDispFreqBin)
            #print('   ezGalDetectLevel         =', ezGalDetectLevel)

    print()
    print(' ezGLonPlotRangeL =', ezGLonPlotRangeL)

    stopTime = time.time()
    stopTimeS = time.ctime()
    print()
    print(' That Python command')
    print('  ', commandString)
    print(' took %d seconds = %1.1F minutes' % ((int(stopTime-startTime)),
        (float(int(stopTime-startTime))/60.))) # xxxxxx.x minutes
    print(' Now = %s' % stopTimeS[:-5])

    print()
    print(' programRevision =', programRevision)
    print()
    print()
    print()
    print()
    print()
    print('       The Society of Amateur Radio Astronomers (SARA)')
    print('                    radio-astronomy.org')
    print()
    print()
    print()
    print()
    print()



def main():

    #global programRevision          # string
    #global commandString            # string
    #global cmdDirectoryS            # string

    #global fileFreqMin              # float
    #global fileFreqMax              # float
    #global fileFreqBinQty           # integer

    #global fileNameLast             # string
    ##global fileWriteName            # string
    #global fileWrite                # file handle

    #global freqCenter               # float
    #global freqStep                 # float
    #global dopplerSpanD2            # float
    #global titleS                   # string
    #global plotCountdown            # integer
    #global ezGLonDispGrid           # integer
    global ezGLonGalCrossingGLonCenterL     # float list
    global ezGLonGalCrossingGLonCenter      # float
    #global ezGLonGalCrossingGLonNear         # float
    #global ezConGalCrossingGLonCenter       # integer
    #global ezConGalCrossingGLonNear         # float

    #global ezGLonPlotRangeL         # integer list


    startTime = time.time()

    printHello()
    
    ezGLonArguments()

    for ezGLonGalCrossingGLonCenter in ezGLonGalCrossingGLonCenterL:
        readDataDir()   # creates fileFreqMin, fileFreqMax, fileFreqBinQty, 
                        #   velGLatP90, velGLatP90Count, galDecP90GLatP90Count,
                        #   fileNameLast

        plotPrep()      # creates titleS, velocitySpanMax, velocityBin

        # velocity plots
        plotEzGLon510velGLat()
        plotEzGLon511velGLatCount()

        plotEzGlon570galArmsSun()
        plotEzGlon571galArmsSunMag5()
        plotEzGLon580galArmsSunI()
        plotEzGLon581galArmsSunIMag5()
        plotEzGLon582galArmsSunRIMag5()

        if 0:
            plotEzGLon516velGLatAvg()            # velocity spectrum Averages
            plotEzGLon517velGLatMax()            # velocity spectrum Maximums

            plotEzGLon520velGLatPolarI()
            plotEzGLon521velGLatPolarD()
            plotEzGLon525velGLatPolarCount()

            plotEzGLon530galDecGatLat()

            findVelGLatEdges()
            plotEzGLon540velGLatEdgesB()
            plotEzGLon541velGLatEdges()
            plotEzGLon550galRot()
            #plotEzGal551galRot2()
            plotEzGLon559planetRot()
            plotEzGLon560galMass()

            plotEzGLon570galArmsSun()
            plotEzGLon580galArmsSunI()

            plotEzGLon60XgLatSpectra()
            plotEzGLon605gLatSpectraCompare()
            plotEzGLon61XgLatSpectraCascade()

            plotEzGLon710gLatDegP180_nnnByFreqBinAvg()

    printGoodbye(startTime)

if __name__== '__main__':
  main()

# a@u22-221222a:~/aaaEzRABase/lto15hcg$ python3 ../ezRA/ezGLon230603a.py  .  -ezGLonPlotRangeL 0 699 -ezRAObsName LTO15 -ezGLonVelGLonEdgeLevelL 1.01  1.066  52
# a@u22-221222a:~/aaaEzRABase/lto15hcg$ python3 ../ezRA/ezGLon230603a.py  .  -ezGLonPlotRangeL 540 560 -ezRAObsName LTO15 -ezGLonVelGLonEdgeLevelL 1.05 30 160 -ezGLon540edgesUFile ezGLon540_1.05_30_160.txt

#  ../ezRA/ezCon230625a.py  /home/a/aaaEzRABase/lto16h/data/2021_280_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_281_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_282_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_282_21.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_283_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_284_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_285_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_286_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_287_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_288_00.rad.txt  /home/a/aaaEzRABase/lto16h/data/2021_289_00.rad.txt  -exzConGalCrossingGLatCenter23.4  -exzConGalCrossingGLatCenter-43.4  -ezConGalCrossingGLonCenterL  -5  16  -ezConAstroMath  1  -ezRAObsName  LTO16  -ezRAObsLat  40.3  -ezRAObsLon  -105.1  -ezRAObsAmsl  1524  -ezConPlotRangeL  191  191
# took 740 seconds = 12.3 minutes
# Now = Tue Jun 27 22:43:12

# python3 ../ezRA/ezGLon230628a.py *N001GLon.npz  -ezGLonGalCrossingGLonCenter 70 -h

# a@u22-221222a:~/aaaEzRABase/ezCon$ python3 ../ezRA/ezGLon230628a.py *GLon.npz  -ezGLonGalCrossingGLonCenter 0

# a@u22-221222a:~/ezRABase/lto16h$ 
# python3 ../ezRA/ezGLon241023b.py .  -ezGLonGalCrossingGLonCenterL 90 90 1  -ezGLonGalCrossingGLonNear 0.5  -ezGLonPlotRangeL 580 580  -ezGLon580Csv 1.18
# ring3d ezGLon580galArmsSunIP090.0P000.5.csv

# for 21 CSV files,
# ls *GLon.npz | grep radP070
# python3 ../ezRA/ezGLon241023b.py .  -ezGLonGalCrossingGLonCenterL 70 90 21  -ezGLonGalCrossingGLonNear 0.5  -ezGLonPlotRangeL 580 580  -ezGLon580Csv 1.18
# cat ezGLon580galArmsSunI*.csv  > ezGLon580.csv
# ls -ltrh
# ring3d ezGLon580.csv
#   Click "OK" button to approve "4-COLUMNS"
#   Option menu - Gradation
#   Option menu - Gradation - AXIS to "COLUMN-4"
#   Try Option menu - Gradation - "FADE-IN" to clicked, click the "SET" button
#   Try Option menu - See-Through to clicked

# 0-90 GLon,
# everyEzCon="-ezConPlotRangeL 191 191 -ezRAObsName LTO16h  -ezRAObsLat 40.29953361978003 -ezRAObsLon -105.08434917119554 -ezRAObsAmsl 1524  -ezConAstroMath 1 -ezConGalCrossingGLonCenterL 0 90 91  -ezConGalCrossingGLonNear 0.5"
# dirOut="241023rinearn"
# Now is ...
# Wed Oct 23 04:13:54 PM MDT 2024
# This script was started ...
# Wed Oct 23 02:31:41 PM MDT 2024
# a@u22-221222a:~/ezRABase/lto16h$ ls 241023rinearn/ | wc
#   24109   24109  719472
# a@u22-221222a:~/ezRABase/lto16h$ du -h 241023rinearn/
# 1.8G	241023rinearn/
# a@u22-221222a:~/ezRABase/lto16h$ ls 241023rinearn/*GLon.npz | grep radP0 | wc
#   23050   23050 1014314
# like    241023rinearn/2022_125_00.radP089.0GLon.npz
# cd 241023rinearn
# python3 ../../ezRA/ezGLon241023b.py  .  -ezGLonGalCrossingGLonCenterL 70 90 21  -ezGLonGalCrossingGLonNear 0.5  -ezGLonPlotRangeL 580 580  -ezGLon580Csv 1.18
# cat ezGLon580galArmsSunI*.csv  > ezGLon580.csv
# ls -ltrh
# ring3d ezGLon580.csv

# cd galLto15Show
# cat ezGLon580gal*.csv > ezGLon580.csv
# ring3d ezGLon580.csv


