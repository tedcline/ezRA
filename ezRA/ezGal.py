programName = 'ezGal241126a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezGal GALaxy explorer program,
#   to read ezCon format *Gal.npz condensed data text file(s),
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

# ezGal241126a, are GalC.npz files really needed ?   Commented out on 241126
# ezGal241024a, print galSunRadiusKpc (7.971022488, in kiloparsecs)
# ezGal240318a, 
#   in ezCon: velGLonP180[:, gLonP180] += antXTVT[:, n][::-1]
#   incoming velGLonP180 is now still the summed antXTVT frequency spectra, with decending frequency.
#   maskOffBelowThis = 1.0      # LTO15HC
#   Ooops!, ezGal516 and ezGal517 were plotting the simple processed antXTVT frequency values
#   receding velocity = (fileFreqBin doppler MHz) * (299792458. m/s / 1420.406 MHz) / 1000. = km/s




# still tedd in findVelGLonEdges()





# ezGal240227b, dusting, findVelGLonEdges() error message
# ezGal240227a, dusting
# ezGal240226a, ezSky601 - ezSky605 errors with ax.set_xticks([], []), so
#   ax.xaxis.set_ticks([])
# ezGal231212a.py, per Ted's Oct 18, 2023 at 8:14 PM email,
#   ezGal511 renamed to ezGal519, to align with the "Count" ezSky309,
#   ezGal525 renamed to ezGal529, to align with the future "Count" ezGal519
# ezGal230820a.py, removed 'Galaxy plane' from ezGal520 ezGal521 ezGal525 and ezGal710
# ezGal230818a.py, default ezGalVelGLonEdgeLevelL to [1.01, 20, 160],
#   error message if no data available for gLon = highGLonMin
# ezGal230802a.py, commented   layout='constrained'   for laptop python3.8.10
# ezGal230528a.py, 'Spectra for Galaxy plane at' to 'Velocity Spectra for'
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
    print('  Windows:   py      ezGal.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezGal.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezGal GALaxy explorer program,')
    print('  to read ezCon format *Gal.npz condensed data text file(s),')
    print('  and optionally create .png plot files.')
    print()
    print('  "radioDataFileDirectories" may be one or more *Gal.npz condensed data text files:')
    print('         py  ezGal.py  bigDish220320_05Gal.npz')
    print('         py  ezGal.py  bigDish220320_05Gal.npz bigDish220321_00Gal.npz')
    print('         py  ezGal.py  bigDish22032*Gal.npz')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezGal.py  .')
    print('         py  ezGal.py  bigDish2203')
    print('         py  ezGal.py  bigDish2203 bigDish2204')
    print('         py  ezGal.py  bigDish22*')
    print('  "radioDataFileDirectories" may be a mix of *Gal.npz condensed data text files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezGal program,')
    print("  then in order from the ezDefaults.txt in the ezGal.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('    -ezRAObsName         bigDish    (observatory name for plot titles)')
    print()
    print('    -ezGalPlotRangeL     0  500     (save only this range of ezGal plots to file, to save time)')
    print('    -ezGalDispGrid          1       (turn on graphical display plot grids)')
    print()
    print('    -ezGalVelGLonEdgeLevelL  1.06   40   140    (velGLon level for ezGal540velGLonEdgesB)')
    print('        (velGLon level for ezGal540velGLonEdgesB: velGLonLevel, highGLonMin, velGLonUEdge[gLon=0])')
    print()
    print('    -ezGal540edgesUFile  edgesUFile.txt')
    print('        (read edgesUFile.txt for velGLonUEdge values')
    print('    -ezGal540edgesLFile  edgesLFile.txt')
    print('        (read edgesLFile.txt for velGLonLEdge values')
    print()
    print('    -ezGal61XGain           150     (maximum height in ezGal61XgLonSpectraCascade plots)')
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
    print('            ezGal.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezGalArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsName                      # string

    global ezGalDispGrid                    # integer

    global ezGal540edgesUFile               # string
    global ezGal540edgesLFile               # string
    global ezGalVelGLonEdgeLevelL           # float list
    global ezGal61XGain                     # float

    global ezGalPlotRangeL                  # integer list


    print()
    print('   ezGalArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

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
            elif thisLine0Lower == '-ezGalDispGrid'.lower():
                ezGalDispGrid = int(thisLine[1])


            # float arguments:
            elif thisLine0Lower == '-ezGal61XGain'.lower():
                ezGal61XGain = float(thisLine[1])


            # string arguments:
            elif thisLine0Lower == '-ezGal540edgesUFile'.lower():
                ezGal540edgesUFile = thisLine[1]

            elif thisLine0Lower == '-ezGal540edgesLFile'.lower():
                ezGal540edgesLFile = thisLine[1]


            # list arguments:
            elif thisLine0Lower == '-ezGalVelGLonEdgeLevelL'.lower():
                ezGalVelGLonEdgeLevelL[0] = float(thisLine[1])
                ezGalVelGLonEdgeLevelL[1] = float(thisLine[2])
                ezGalVelGLonEdgeLevelL[2] = float(thisLine[3])

            elif thisLine0Lower == '-ezGalPlotRangeL'.lower():
                ezGalPlotRangeL[0] = int(thisLine[1])
                ezGalPlotRangeL[1] = int(thisLine[2])


            elif 6 <= len(thisLine0Lower) and thisLine0Lower[:6] == '-ezGal'.lower():
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



def ezGalArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsName                      # string

    global ezGal540edgesUFile               # string
    global ezGal540edgesLFile               # string
    global ezGalVelGLonEdgeLevelL           # float list
    global ezGal61XGain                     # float

    global ezGalPlotRangeL                  # integer list
    global ezGalDispGrid                    # integer

    global cmdDirectoryS                    # string            creation


    print()
    print('   ezGalArgumentsCommandLine ===============')

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
            elif cmdLineArgLower == 'ezGalDispGrid'.lower():
                ezGalDispGrid = int(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:
            elif cmdLineArgLower == 'ezGal61XGain'.lower():
                ezGal61XGain = float(cmdLineSplit[cmdLineSplitIndex])


            # string arguments:
            elif cmdLineArgLower == 'ezGal540edgesUFile'.lower():
                ezGal540edgesUFile = cmdLineSplit[cmdLineSplitIndex]

            elif cmdLineArgLower == 'ezGal540edgesLFile'.lower():
                ezGal540edgesLFile = cmdLineSplit[cmdLineSplitIndex]


            # list arguments:
            elif cmdLineArgLower == 'ezGalVelGLonEdgeLevelL'.lower():
                ezGalVelGLonEdgeLevelL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGalVelGLonEdgeLevelL[1] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGalVelGLonEdgeLevelL[2] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezGalPlotRangeL'.lower():
                ezGalPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGalPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezDefaultsFile'.lower():
                ezGalArgumentsFile(cmdLineSplit[cmdLineSplitIndex])


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



def ezGalArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global ezRAObsName                      # string

    global ezGal540edgesUFile               # string
    global ezGal540edgesLFile               # string
    global ezGalVelGLonEdgeLevelL           # float list
    global ezGal61XGain                     # float

    global ezGalPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global ezGalDispGrid                    # integer


    # defaults
    #ezRAObsName = 'LebanonKS'
    #ezRAObsName = 'defaultKS'
    ezRAObsName = ''                # overwritten by optional argument

    ezGal540edgesUFile = ''
    ezGal540edgesLFile = ''
    #ezGalVelGLonEdgeLevelL = [1.06, 40, 140]    # velGLon level for ezGal540velGLonEdgesB: velGLonLevel, highGLonMin, velGLonUEdge[gLon=0])
    ezGalVelGLonEdgeLevelL = [1.01, 20, 160]    # velGLon level for ezGal540velGLonEdgesB: velGLonLevel, highGLonMin, velGLonUEdge[gLon=0])

    ezGal61XGain = 120.             # maximum height in ezGal61XgLonSpectraCascade plots
    
    ezGalPlotRangeL = [0, 9999]     # save this range of plots to file
    plotCountdown = 25              # number of plots still to print + 1
    ezGalDispGrid = 0

    # process arguments from ezDefaults.txt file in the same directory as this ezGal program
    ezGalArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezGalArgumentsFile('ezDefaults.txt')

    ezGalArgumentsCommandLine()             # process arguments from command line
    
    ezGalVelGLonEdgeLevelL[1] = int(ezGalVelGLonEdgeLevelL[1])
    ezGalVelGLonEdgeLevelL[2] = int(ezGalVelGLonEdgeLevelL[2])

    # print status
    print()
    print('   ezRAObsName =', ezRAObsName)
    print()
    print('   ezGal540edgesUFile =', ezGal540edgesUFile)
    print('   ezGal540edgesLFile =', ezGal540edgesLFile)
    print('   ezGalVelGLonEdgeLevelL =', ezGalVelGLonEdgeLevelL)
    print()
    print('   ezGal61XGain           =', ezGal61XGain)
    print()
    print('   ezGalPlotRangeL =', ezGalPlotRangeL)
    print('   ezGalDispGrid   =', ezGalDispGrid)



def readDataDir():
    # Open each data file in directory and read individual lines.

    global ezRAObsName              # string
    global fileObsName              # string                                    creation
    global fileFreqMin              # float                                     creation
    global fileFreqMax              # float                                     creation
    global fileFreqBinQty           # integer                                   creation

    global velGLonP180              # float 2d array                            creation
    global velGLonP180Count         # integer array                             creation
    global velGLonP180CountSum      # integer                                   creation
    global galDecP90GLonP180Count   # integer 2d array                          creation
    global antXTVTName              # string                                    creation

    global fileNameLast             # string                                    creation

    print()
    print('   readDataDir ===============')

    #directoryList = sorted(cmdDirectoryS.split())           # sorted needed on Linux
    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    
    VelNpz_Qty = 0
    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]

        # if arguments are .txt filenames,
        # pass each of them through together as a mini directory list of .txt files.
        # Allows one .txt file from a directory of .txt files.
        if directory.endswith('Gal.npz'):
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
            print(f'\r {VelNpz_Qty + 1}  file = {fileCounter + 1} of {fileListLen}',
                f' in dir {directoryCounter + 1} of {directoryListLen} =',
                directory + os.path.sep + fileReadName, '                                      ',
                end='')   # allow append to line

            if not fileReadName.endswith('Gal.npz'):
                continue                                # skip to next file

            npzfile = np.load(fileReadName)

            if not VelNpz_Qty:                      # if first *Gal.npz file
                fileObsName    = npzfile['fileObsName'].tolist()
                if ezRAObsName:
                    fileObsName = ezRAObsName       # overwrite fileObsName with argument
                fileFreqMin    = float(npzfile['fileFreqMin'])
                fileFreqMax    = float(npzfile['fileFreqMax'])
                fileFreqBinQty = int(npzfile['fileFreqBinQty'])

                # Velocity by Galactic Longitude (gLon) grid.
                # gLon is -180thru+180, adding 180, gives gLonP180 as 0thru360 which is more convenient.
                # velGLonP180 is fileFreqBinQty by 0thru360 gLonP180
                #velGLonP180 = np.zeros([fileFreqBinQty, 361], dtype = float)
                velGLonP180 = npzfile['velGLonP180']
                
                # incoming velGLonP180 is now still the summed antXTVT frequency spectra, with decending frequency.
                # For each spectrum, velGLonP180Count[gLonP180] recorded the quantity summed.

                # velGLonP180Count is count of saved spectra in velGLonP180
                #velGLonP180Count = np.zeros([361], dtype = int)
                velGLonP180Count = npzfile['velGLonP180Count']
                # Declination (dec) is -90thru+90, adding 90, gives decP90 as 0thru180 which is more convenient.
                # galDecP90GLonP180Count is 0thru180 decP90 by 0thru360
                #galDecP90GLonP180Count = np.zeros([181, 361], dtype = int)
                galDecP90GLonP180Count = npzfile['galDecP90GLonP180Count']
                #print(npzfile.files)
                #print('antXTVTName' in npzfile.files)
                if 'antXTVTName' in npzfile.files:     # was added to file definition later on 230401
                    antXTVTName = npzfile['antXTVTName']
                else:
                    antXTVTName = 'AntXTVT'
            else:
                # ignore npzfile['fileFreqMin'] 
                # ignore npzfile['fileFreqMax']
                # ignore npzfile['fileFreqBinQty'] 
                velGLonP180            += npzfile['velGLonP180']
                velGLonP180Count       += npzfile['velGLonP180Count']
                galDecP90GLonP180Count += npzfile['galDecP90GLonP180Count']
                if 'antXTVTName' in npzfile.files:     # was added to file definition later on 230401
                    antXTVTName = npzfile['antXTVTName']
                else:
                    antXTVTName = 'AntXTVT'

            VelNpz_Qty += 1
            fileNameLast = fileReadName
            print()

    # have now read all the Gal.npz files

    # maybe blank out the last filename
    if not fileReadName.endswith('Gal.npz'):
        print('\r                                                                              ' \
            + '                                                                                ')
    else:
        print()
    
    if not VelNpz_Qty:                      # if no first *Gal.npz file
        print()
        print()
        print(" ========== FATAL ERROR: no data file loaded")
        print()
        print()
        print()
        exit()


    print(' fileNameLast =', fileNameLast)
    print(' VelNpz_Qty   =', VelNpz_Qty)

    print()
    print(' fileFreqMin = ', fileFreqMin)
    print(' fileFreqMax = ', fileFreqMax)
    print(' fileFreqBinQty = ', fileFreqBinQty)

    print()
    print(' velGLonP180.shape = ', velGLonP180.shape)
    print(' velGLonP180Count.shape = ', velGLonP180Count.shape)
    print(' galDecP90GLonP180Count.shape = ', galDecP90GLonP180Count.shape)
    print(' antXTVTName =', antXTVTName)

    print()
    velGLonP180CountSum = velGLonP180Count.sum()
    print(' velGLonP180CountSum =', velGLonP180CountSum)

    if not velGLonP180CountSum:       # if nothing in velGLonP180 to save or plot
        print()
        print()
        print(" ========== FATAL ERROR: no data loaded")
        print()
        print()
        print()
        exit()


    # for fileNameLast of  data/2021_333_00.txt  create fileVelWriteName as  data/2021_333_00GalC.npz
    fileVelWriteName = fileNameLast.split(os.path.sep)[-1][:-7] + 'GalC.npz'   # ezGal combines *Gal.npz
    print('      fileObsName = ', fileObsName)
    # are GalC.npz files really needed ?   Commented out on 241126
    #np.savez_compressed(fileVelWriteName, fileObsName=np.array(fileObsName),
    #    fileFreqMin=np.array(fileFreqMin), fileFreqMax=np.array(fileFreqMax),
    #    fileFreqBinQty=np.array(fileFreqBinQty),
    #    velGLonP180=velGLonP180, velGLonP180Count=velGLonP180Count,
    #    galDecP90GLonP180Count=galDecP90GLonP180Count)

    # Prepare velGLonP180 for later plots.
    # velGLonP180 has been filled with sums of samples.  Now for each column, convert to sum's average.
    for gLonP180 in range(361):
        if velGLonP180Count[gLonP180]:
            velGLonP180[:, gLonP180] /= velGLonP180Count[gLonP180]

    # mask low values with Not-A-Number (np.nan) to not plot
    #maskOffBelowThis = 0.975    # N0RQVHC
    #maskOffBelowThis = 0.9      # WA6RSV
    maskOffBelowThis = 1.0      # LTO15HC
    print('      maskOffBelowThis = ', maskOffBelowThis)
    maskThisOff = (velGLonP180 < maskOffBelowThis)
    #velGLonP180[maskThisOff] = np.nan                   # maskOffBelowThis is the do not plot
    velGLonP180[maskThisOff] = maskOffBelowThis         # maskOffBelowThis is the minumum everywhere



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

    velocitySpanMax = dopplerSpanD2 * (299792458. / freqCenter) / 1000.  # = 253.273324388 km/s
    print('                         velocitySpanMax =', velocitySpanMax)
    velocityBin = np.linspace(-velocitySpanMax, velocitySpanMax, fileFreqBinQty)
    #print('                         velocityBin =', velocityBin)
    print('                         len(velocityBin) =', len(velocityBin))



def plotEzGal510velGLon():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to save or plot
    if ezGalPlotRangeL[0] <= 510 and 510 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal510velGLon.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        print()

        xi = np.arange(-180, +181, 1)           # +180 thru -180 degrees in degrees, galaxy centered
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

        print('                         np.nanmax(velGLonP180) =', np.nanmax(velGLonP180))
        #print('                         np.mean(velGLonP180[~np.isnan(velGLonP180)]) =',
        #    np.mean(velGLonP180[~np.isnan(velGLonP180)]))
        print('                         np.mean(velGLonP180) =', np.mean(velGLonP180))
        print('                         np.nanmin(velGLonP180) =', np.nanmin(velGLonP180))
        pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'))
        #pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'), vmin=1.025, vmax=1.21)

        #gridColor = 'black'
        gridColor = 'white'
        # horizonal thin black line
        plt.axhline(y =   0, linewidth=0.5, color=gridColor)

        # vertical thin black lines
        plt.axvline(x =  90, linewidth=0.5, color=gridColor)
        plt.axvline(x =   0, linewidth=0.5, color=gridColor)
        plt.axvline(x = -90, linewidth=0.5, color=gridColor)

        cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        plt.ylim(-velocitySpanMax, velocitySpanMax)        # in velocity

        #    plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
        #        + f'\n\nVelocity Count Sum = {velGLonP180CountSum}' \
        #        + f'\n\nVelocity Count Nonzero = {velGLonP180CountNonzero}' \
        #        + f' of {len(velGLonP180Count)}',
        #        rotation=90, verticalalignment='bottom')
        plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}'
            + f' Nonzero={velGLonP180CountNonzero} of {len(velGLonP180Count)}',
            rotation=90, verticalalignment='bottom')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal519velGLonCount():

    global plotCountdown            # integer
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 519 and 519 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal519velGLonCount.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()
        plt.plot(np.arange(-180, +181, 1), velGLonP180Count)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(182, -182)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        print()

        plt.ylabel('Velocity Data Counts by Galactic Longitude' \
            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
            + f' Nonzero = {velGLonP180CountNonzero} of {len(velGLonP180Count)}')
        #    rotation=90, verticalalignment='bottom')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')


        # print out velGLonCount status
        fileWriteGLonName = 'ezGal519velGLonCount.txt'
        fileWriteGLon = open(fileWriteGLonName, 'w')
        if not (fileWriteGLon.mode == 'w'):
            print()
            print()
            print()
            print()
            print()
            print(' ========== FATAL ERROR:  Can not open ')
            print(' ' + fileWriteGLonName)
            print(' file to write out velGLonCount data')
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
            fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLonP180Count[gLonP180]:5d}  {gLonP180 + 180:4d}  ' \
                + fileWriteGLonHashS[:velGLonP180Count[gLonP180]] + '\n'
            fileWriteGLon.write(fileWriteGLonS)

        fileWriteGLonS = f'0000  {velGLonP180Count[180]:5d}  0000  ' \
            + fileWriteGLonHashS[:velGLonP180Count[180]] + '\n'
        fileWriteGLon.write(fileWriteGLonS)

        for gLonP180 in range(181, 361):                          # for every column, RtoL, 181 thru 360
            fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLonP180Count[gLonP180]:5d}  {gLonP180 - 180:4d}  ' \
                + fileWriteGLonHashS[:velGLonP180Count[gLonP180]] + '\n'
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
            if velGLonP180Count[gLonP180] <= velGLonCountTrigger:
                fileWriteGLon.write(f': G{gLonP180 + 180:03d}    * have {velGLonP180Count[gLonP180]:5d}\n')
                fileWriteGLon.write(':600\n')
                fileWriteGLon.write(':240\n')
                fileWriteGLon.write(':060\n')
                fileWriteGLon.write('*\n')
        for gLonP180 in range(180, 361):                          # for every column, RtoL, 180 thru 360
            if velGLonP180Count[gLonP180] <= velGLonCountTrigger:
                fileWriteGLon.write(f': G{gLonP180 - 180:03d}    * have {velGLonP180Count[gLonP180]:5d}\n')
                fileWriteGLon.write(':600\n')
                fileWriteGLon.write(':240\n')
                fileWriteGLon.write(':060\n')
                fileWriteGLon.write('*\n')

        fileWriteGLon.close()   



def plotEzGal516velGLonAvg():
    # spectrum Averages in dots

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 516 and 516 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal516velGLonAvg.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        #plt.plot(np.arange(-180, +181, 1), np.mean(velGLonP180, axis=0))
        # Ooops!, was plotting the simple processed antXTVT frequency values
        # receding velocity = (fileFreqBin doppler MHz) * (299792458. m/s / 1420.406 MHz) / 1000. = km/s
        # velocity = (fileFreqBin doppler MHz) * 211.061103656 = km/s
        plt.plot(np.arange(-180, +181, 1), np.mean(velGLonP180, axis=0) * 211.061103656)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(182, -182)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )

        plt.ylabel('Average Velocity (km/s) by Galactic Longitude' \
            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
            + f' Nonzero = {velGLonP180CountNonzero} of {len(velGLonP180Count)}')
        #    rotation=90, verticalalignment='bottom')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal517velGLonMax():
    # spectrum Maximums in dots

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 517 and 517 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal517velGLonMax.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        #plt.plot(np.arange(-180, +181, 1), np.amax(velGLonP180, axis=0))
        # Ooops!, was plotting the simple processed antXTVT frequency values
        # receding velocity = (fileFreqBin doppler MHz) * (299792458. m/s / 1420.406 MHz) / 1000. = km/s
        # velocity = (fileFreqBin doppler MHz) * 211.061103656 = km/s
        plt.plot(np.arange(-180, +181, 1), np.amax(velGLonP180, axis=0) * 211.061103656)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(182, -182)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )

        plt.ylabel('Maximum Velocity (km/s) by Galactic Longitude' \
            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
            + f' Nonzero = {velGLonP180CountNonzero} of {len(velGLonP180Count)}')
        #    rotation=90, verticalalignment='bottom')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal520velGLonPolarI():
    # velGLon Polar plot where Increasing Radius Is Increasing "Velocity"

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 520 and 520 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal520velGLonPolarI.png'     # Velocity by Galactic Longitude with pcolormesh
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        rad = np.arange(0, fileFreqBinQty, 1)        # 0 to fileFreqBinQty in freqBins
        azm = np.linspace(0, np.pi + np.pi, 361, endpoint=True)
        r, theta = np.meshgrid(rad, azm)

        plt.grid(0)
        im = plt.pcolormesh(theta, r, velGLonP180.T, cmap=plt.get_cmap('gnuplot'), shading='auto')

        fig.colorbar(im, ax=ax, pad=0.1)

        polarPlot = plt.plot(azm, r, color='black', linestyle='none')
        plt.grid(1)

        plt.title(titleS)

        ax.set_rgrids((fileFreqBinQty/2.,), ('',))
        ax.set_theta_zero_location('S', offset=0.)
        ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

        radiusTextQuadrant = fileFreqBinQty * 1.1
        ax.text(-2.55, radiusTextQuadrant, 'Quadrant 1', color='red', horizontalalignment='right')
        ax.text(-0.6,  radiusTextQuadrant, 'Quadrant 2', color='red', horizontalalignment='right')
        ax.text( 0.6,  radiusTextQuadrant, 'Quadrant 3', color='red')
        ax.text( 2.55, radiusTextQuadrant, 'Quadrant 4', color='red')
        ax.text(-3.05, radiusTextQuadrant*0.95, 'Toward', color='blue', horizontalalignment='right')
        ax.text( 3.05, radiusTextQuadrant*0.95, 'Galactic Center', color='blue')
        ax.text(-2.2, radiusTextQuadrant*0.95, 'Sun at\nCenter', color='blue', horizontalalignment='right')

        ax.set_xlabel('Galactic Longitude (degrees) of Spectra')
        ax.set_ylabel('Increasing Radius Is Increasing "Velocity",\n\n' \
            + 'Increasing Radius Is Increasing Receding,\n\n' \
            + 'Increasing Radius Is Decreasing Doppler Frequency\n\n')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal521velGLonPolarD():
    # velGLon Polar plot where Decreasing Radius Is Increasing "Velocity"

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 521 and 521 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal521velGLonPolarD.png'     # Velocity by Galactic Longitude with pcolormesh
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        rad = np.arange(0, fileFreqBinQty, 1)        # 0 to fileFreqBinQty in freqBins
        azm = np.linspace(0, np.pi + np.pi, 361, endpoint=True)
        r, theta = np.meshgrid(rad, azm)

        plt.grid(0)
        im = plt.pcolormesh(theta, r, velGLonP180[::-1].T, cmap=plt.get_cmap('gnuplot'), shading='auto')

        fig.colorbar(im, ax=ax, pad=0.1)

        polarPlot = plt.plot(azm, r, color='black', linestyle='none')
        plt.grid(1)

        plt.title(titleS)

        ax.set_rgrids((fileFreqBinQty/2.,), ('',))
        ax.set_theta_zero_location('S', offset=0.)
        ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

        radiusTextQuadrant = fileFreqBinQty * 1.1
        ax.text(-2.55, radiusTextQuadrant, 'Quadrant 1', color='red', horizontalalignment='right')
        ax.text(-0.6,  radiusTextQuadrant, 'Quadrant 2', color='red', horizontalalignment='right')
        ax.text( 0.6,  radiusTextQuadrant, 'Quadrant 3', color='red')
        ax.text( 2.55, radiusTextQuadrant, 'Quadrant 4', color='red')
        ax.text(-3.05, radiusTextQuadrant*0.95, 'Toward', color='blue', horizontalalignment='right')
        ax.text( 3.05, radiusTextQuadrant*0.95, 'Galactic Center', color='blue')
        ax.text(-2.2, radiusTextQuadrant*0.95, 'Sun at\nCenter', color='blue', horizontalalignment='right')

        ax.set_xlabel('Galactic Longitude (degrees) of Spectra')
        ax.set_ylabel('Decreasing Radius Is Increasing "Velocity",\n\n' \
            + 'Decreasing Radius Is Increasing Receding,\n\n' \
            + 'Decreasing Radius Is Decreasing Doppler Frequency\n\n')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal529velGLonPolarCount():

    global plotCountdown            # integer
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 529 and 529 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal529velGLonPolarCount.png'     # Velocity by Galactic Longitude with pcolormesh
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        rad = np.arange(0, fileFreqBinQty, 1)        # 0 to fileFreqBinQty in freqBins
        azm = np.linspace(0, np.pi + np.pi, 361, endpoint=True)
        r, theta = np.meshgrid(rad, azm)

        velGLonP180CountPolar = np.zeros_like(velGLonP180.T, dtype=int)
        for gLonP180 in range(361):
            if velGLonP180Count[gLonP180]:
                velGLonP180CountPolar[gLonP180, :] += velGLonP180Count[gLonP180]

        plt.grid(0)
        im = plt.pcolormesh(theta, r, velGLonP180CountPolar, cmap=plt.get_cmap('gnuplot'), shading='auto')

        fig.colorbar(im, ax=ax, pad=0.1)

        polarPlot = plt.plot(azm, r, color='black', linestyle='none')
        plt.grid(1)

        plt.title(titleS)

        ax.set_rgrids((fileFreqBinQty,), ('',))
        ax.set_theta_zero_location('S', offset=0.)
        ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

        radiusTextQuadrant = fileFreqBinQty * 1.1
        ax.text(-2.55, radiusTextQuadrant, 'Quadrant 1', color='red', horizontalalignment='right')
        ax.text(-0.6,  radiusTextQuadrant, 'Quadrant 2', color='red', horizontalalignment='right')
        ax.text( 0.6,  radiusTextQuadrant, 'Quadrant 3', color='red')
        ax.text( 2.55, radiusTextQuadrant, 'Quadrant 4', color='red')
        ax.text(-3.05, radiusTextQuadrant*0.95, 'Toward', color='blue', horizontalalignment='right')
        ax.text( 3.05, radiusTextQuadrant*0.95, 'Galactic Center', color='blue')

        ax.set_xlabel('Galactic Longitude (degrees) of Spectra')
        ax.set_ylabel('Velocity Data Counts by Galactic Longitude' \
            + f'\n\nVelocity Count Sum = {velGLonP180CountSum:,}' \
            + f'\n\nVelocity Count Nonzero = {np.count_nonzero(velGLonP180Count)}' \
            + f' of {len(velGLonP180Count)}\n\n')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal530galDecGLon():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global galDecP90GLonP180Count   # integer 2d array

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 530 and 530 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        pltNameS = 'ezGal530galDecGLon.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        xi = np.arange(-180, +181, 1)           # +180 thru -180 degrees in degrees, galaxy centered
        yi = np.arange(0, 181, 1)               # 0 thru 180 decP90

        xi, yi = np.meshgrid(xi, yi)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        if 0:
            maskOffBelowThis = 0.975    # N0RQVHC
            maskOffBelowThis = 0.9      # WA6RSV
            maskOffBelowThis = -10
            print(' maskOffBelowThis = ', maskOffBelowThis)
            maskThisOff = (velGLonP180 < maskOffBelowThis)
            velGLonP180[maskThisOff] = np.nan

        pts = plt.contourf(xi, yi, galDecP90GLonP180Count, 20, cmap=plt.get_cmap('gnuplot'))

        #gridColor = 'black'
        gridColor = 'white'

        # horizonal thin black line
        plt.axhline(y =  90, linewidth=0.5, color=gridColor)

        # vertical thin black lines
        plt.axvline(x =  90, linewidth=0.5, color=gridColor)
        plt.axvline(x =   0, linewidth=0.5, color=gridColor)
        plt.axvline(x = -90, linewidth=0.5, color=gridColor)

        cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        plt.ylabel('Velocity Counts on Declination by Galactic Longitude' \
            + f'\nVelocity Count Sum = {velGLonP180CountSum:,}')
        #    rotation=90, verticalalignment='bottom')
        plt.ylim(0, 180)                # in decP90
        plt.yticks([0,     30,    60,    90,  120,  150,  180],
                   ['-90', '-60', '-30', '0', '30', '60', '90'])

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def findVelGLonEdges():
    # if needed for later plots,
    #   reads   ezGal540edgesUFile .txt file and
    #   writes 'ezGal540edgesUFileOut.txt' file with velGLonUEdge values
    # if needed for later plots,
    #   reads   ezGal540edgesLFile .txt file and
    #   writes 'ezGal540edgesLFileOut.txt' file with velGLonLEdge values
    #    -ezGalVelGLonEdgeLevelL  1.06   40   140    (velGLon level for ezGal540velGLonEdgesB)
    #        (velGLon level for ezGal540velGLonEdgesB: velGLonLevel, highGLonMin, edgeUGLon0)

    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global velocityBin              # float array
    global ezGalPlotRangeL          # integer list

    global ezGal540edgesUFile       # string
    global ezGal540edgesLFile       # string
    global ezGalVelGLonEdgeLevelL           # float list
    global velGLonUEdge             # float array
    global velGLonLEdge             # float array

    # read or calculate velGLonUEdge and velGLonLEdge, needed later for
    #   plotEzGal540velGLonEdgesB()
    #   plotEzGal541velGLonEdges()
    #   plotEzGal550galRot()
    #   plotEzGal560galMass()
    if not (ezGalPlotRangeL[0] <= 569 and 540 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # calculation not needed

    print()
    print('          findVelGLonEdges ================================')
    print('                         ezGalVelGLonEdgeLevelL =', ezGalVelGLonEdgeLevelL)

    # load velGLonUEdgeFile values from ezGal540edgesUFile file
    velGLonUEdgeFile = []
    try:
        velGLonUEdgeFile = np.loadtxt(ezGal540edgesUFile)

    except (FileNotFoundError, IOError):
        if ezGal540edgesUFile:
            print()
            print()
            print()
            print()
            print('   Error in opening file or reading ' + ezGal540edgesUFile + ' file.')
            print()
            print()
            print()
            print()
            exit()

    print('      no error opening ' + ezGal540edgesUFile)
    print('      velGLonUEdgeFile =', velGLonUEdgeFile)
    print('      len(velGLonUEdgeFile) =', len(velGLonUEdgeFile))
    print()

    # load velGLonLEdgeFile values from ezGal540edgesLFile file
    velGLonLEdgeFile = []
    try:
        velGLonLEdgeFile = np.loadtxt(ezGal540edgesLFile)

    except (FileNotFoundError, IOError):
        if ezGal540edgesLFile:
            print()
            print()
            print()
            print()
            print('   Error in opening file or reading ' + ezGal540edgesLFile + ' file.')
            print()
            print()
            print()
            print()
            exit()

    print('      no error opening ' + ezGal540edgesLFile)
    print('      velGLonLEdgeFile =', velGLonLEdgeFile)
    print('      len(velGLonLEdgeFile) =', len(velGLonLEdgeFile))

    if not ezGal540edgesUFile or not ezGal540edgesLFile:
        # need to create velGLonUEdge and velGLonLEdge

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        velGLonP180Max  = np.nanmax(velGLonP180)
        velGLonP180Mean = np.mean(velGLonP180)
        velGLonP180Min  = np.nanmin(velGLonP180)
        print('                         velGLonP180Max  =', velGLonP180Max)
        print('                         velGLonP180Mean =', velGLonP180Mean)
        print('                         velGLonP180Min  =', velGLonP180Min)

        velGLonUEdge = np.full(361, np.nan)     # unused nan will not plot
        velGLonLEdge = np.full(361, np.nan)     # unused nan will not plot

        # for Galactic plane crossings, velGLonUEdge will be the max velocity vs Galactic Longitude.
        # Page 46 of
        #   https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf

        # -ezGalVelGLonEdgeLevelL  1.06   40   140    (velGLon level for ezGal540velGLonEdgesB)
        #   (velGLon level for ezGal540velGLonEdgesB: velGLonLevel, highGLonMin, velGLonUEdge[gLon=0])
        #velGLonLevel = ezGalVelGLonEdgeLevelL[0]
        highGLonMin  = ezGalVelGLonEdgeLevelL[1]

        # For most of each used gLon, calculate the Upper and Lower edges of each velGLonP180 spectrum,
        #   in freqBin, where the velGLonP180 spectrum power value is greater or equal to velGLonLevel.
        # But for the 'low positive gLon', where the gLon is less than highGLonMin and positive.
        # For these 'low positive gLon', the velGLonP180 spectrum values are so weak,
        #   ezGal calculates the Upper edges as along a straight line
        #   from the Upper edge of highGLonMin, to ezGalVelGLonEdgeLevelL[3] where gLon is 0.
        # This straight line typically slopes up to the right,
        #   with the left end at the top of the (inner Galactic arms) triangle.
        # So, using  gLonP180 coordinates, for low positive gLon,
        #   the calculated velGLonUEdgeFreqBinThis is on the line,
        #   from (x1, y1) to (x0, y0), meaning
        #   from (highGLonMin+180, velGLonUEdge[highGLonMin+180]) to (180, ezGalVelGLonEdgeLevelL[2])
        # slopeLowGLon = (y1 - y0) / (x1 - x0)
        # slopeLowGLon = (velGLonUEdge[highGLonMin+180] - ezGalVelGLonEdgeLevelL[2]) / (highGLonMin+180 - 180)
        # slopeLowGLon = (velGLonUEdge[highGLonMin+180] - ezGalVelGLonEdgeLevelL[2]) / highGLonMin
        slopeLowGLon = 999.     # silly value flag
        for gLonP180 in reversed(range(361)):
            if velGLonP180Count[gLonP180]:
                gLon = gLonP180 - 180
                # calculate Upper and Lower Detection Doppler of this velGLonP180 spectrum, in freqBin
                # https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
                # Tuple of arrays returned :  (array([ 4,  7, 11], dtype=int32),)
                # velGLonP180AboveLevelFreqBins are the freqBins with velGLonP180 >= velGLonEdgeLevel
                #velGLonP180AboveLevelFreqBins = np.where(velGLonEdgeLevel <= velGLonP180[:, gLonP180])[0]
                velGLonP180AboveLevelFreqBins = np.where(ezGalVelGLonEdgeLevelL[0] <= velGLonP180[:, gLonP180])[0]

                if velGLonP180AboveLevelFreqBins.any():
                    #print('========= gLon =', gLon)
                    if 0 <= gLon and gLon < highGLonMin:
                        # for low positive gLon, calculate slopeLowGLon
                        if 990. < slopeLowGLon:     # if slopeLowGLon still silly
                            # slopeLowGLon never got calculated below
                            print()
                            print()
                            print()
                            print()
                            print(f'   Error: ezGalVelGLonEdgeLevelL[1] ({highGLonMin}) value is invalid.')
                            print(f'          No data available for gLon = {highGLonMin} degrees.')
                            print()
                            print(f'          Next lower  used gLon is {highGLonMin} degrees.')
                            print(f'          Next higher used gLon is {highGLonMin} degrees.')
                            print()
                            print()
                            print()

                # tedd

                # nextLowerUsedGLon = np.where(ezGalVelGLonEdgeLevelL[0] <= velGLonP180[:, gLonP180])[0]
                velGLonP180AboveLevelFreqBins = np.where(ezGalVelGLonEdgeLevelL[0] <= velGLonP180[:, gLonP180])[0]
                if velGLonP180Count[gLonP180]:



                    if 1:
                        print()
                        print()
                        print()
                        print()
                        exit()
                        velGLonUEdge[gLonP180] = ezGalVelGLonEdgeLevelL[2] + gLon * slopeLowGLon
                    else:
                        velGLonUEdgeFreqBinThis = velGLonP180AboveLevelFreqBins[-1]     # use last element of list
                        velGLonUEdge[gLonP180] = velocityBin[velGLonUEdgeFreqBinThis]
                        if highGLonMin == gLon:
                            slopeLowGLon = (velGLonUEdge[highGLonMin+180] - ezGalVelGLonEdgeLevelL[2]) / highGLonMin
                        # # in case of a gap in gLon data, calculate slopeLowGLon for all highGLonMin <= gLon
                        # if highGLonMin <= gLon:
                        #     slopeLowGLon = (velGLonUEdge[highGLonMin+180] - ezGalVelGLonEdgeLevelL[2]) / highGLonMin
                    velGLonLEdgeFreqBinThis = velGLonP180AboveLevelFreqBins[0]          # use first element of list
                    velGLonLEdge[gLonP180] = velocityBin[velGLonLEdgeFreqBinThis]
                elif 0 <= gLon and gLon < highGLonMin:
                    # for low positive gLon
                    velGLonUEdge[gLonP180] = ezGalVelGLonEdgeLevelL[2] + gLon * slopeLowGLon

        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.medfilt.html
        ###################from scipy.signal import medfilt
        #velGLonUEdge[181:] = medfilt(velGLonUEdge[181:], 9)
        ###################velGLonUEdge[181:] = medfilt(velGLonUEdge[181:], 35)

    # if available, use ezGal540edgesUFile
    if ezGal540edgesUFile:
        velGLonUEdge = velGLonUEdgeFile

    # if available, use ezGal540edgesLFile
    if ezGal540edgesLFile:
        velGLonLEdge = velGLonLEdgeFile

    # write( velGLonUEdge to 'ezGal540edgesUFileOut.txt'
    fileWriteUEdge = open('ezGal540edgesUFileOut.txt', 'w')
    if not (fileWriteUEdge.mode == 'w'):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Can not open ')
        print(' ezGal540edgesUFileOut.txt')
        print(' file to write out velGLonUEdge values')
        print()
        print()
        print()
        print()
        exit()

    fileWriteUEdge.write('\n# velGLonUEdge values for -ezGalVelGLonEdgeLevelL  ' \
        + str(ezGalVelGLonEdgeLevelL[0]) + '  ' + str(ezGalVelGLonEdgeLevelL[1]) + '  ' +  str(ezGalVelGLonEdgeLevelL[2]) + '\n')
    for gLonP180 in range(361):
        if not (gLonP180 % 10):
            # before each multiple of 10
            if gLonP180 < 180:
                fileWriteUEdgeWriteS = f'# Galactic Longitude -{180 - gLonP180:03d}\n'    # '-nnn' with leading zeros
            else:
                fileWriteUEdgeWriteS = f'# Galactic Longitude +{gLonP180 - 180:03d}\n'    # '+nnn' with leading zeros
            fileWriteUEdge.write(fileWriteUEdgeWriteS)
        fileWriteUEdgeWriteS = f'{velGLonUEdge[gLonP180]:f}\n'
        fileWriteUEdge.write(fileWriteUEdgeWriteS)
    fileWriteUEdge.write('# end of file\n')
    fileWriteUEdge.close()

    # write( velGLonLEdge to 'ezGal540edgesLFileOut.txt'
    fileWriteLEdge = open('ezGal540edgesLFileOut.txt', 'w')
    if not (fileWriteLEdge.mode == 'w'):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Can not open ')
        print(' ezGal540edgesLFileOut.txt')
        print(' file to write out velGLonLEdge values')
        print()
        print()
        print()
        print()
        exit()

    fileWriteLEdge.write('\n# velGLonLEdge values for -ezGalVelGLonEdgeLevelL  ' \
        + str(ezGalVelGLonEdgeLevelL[0]) + '  ' + str(ezGalVelGLonEdgeLevelL[1]) + '  ' +  str(ezGalVelGLonEdgeLevelL[2]) + '\n')
    for gLonP180 in range(361):
        if not (gLonP180 % 10):
            # before each multiple of 10
            if gLonP180 < 180:
                fileWriteLEdgeWriteS = f'# Galactic Longitude -{180 - gLonP180:03d}\n'    # '-nnn' with leading zeros
            else:
                fileWriteLEdgeWriteS = f'# Galactic Longitude +{gLonP180 - 180:03d}\n'    # '+nnn' with leading zeros
            fileWriteLEdge.write(fileWriteLEdgeWriteS)
        fileWriteLEdgeWriteS = f'{velGLonLEdge[gLonP180]:f}\n'
        fileWriteLEdge.write(fileWriteLEdgeWriteS)
    fileWriteLEdge.write('# end of file\n')
    fileWriteLEdge.close()



def plotEzGal540velGLonEdgesB():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global velocitySpanMax          # float
    global velocityBin              # float array

    global titleS                   # string
    #global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    global ezGalVelGLonEdgeLevelL   # float list
    global velGLonUEdge             # float array
    global velGLonLEdge             # float array

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 540 and 540 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # plot not needed

    pltNameS = f'ezGal540velGLonEdgesB_{ezGalVelGLonEdgeLevelL[0]:0.4f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

    plt.clf()

    xi = np.arange(-180, +181, 1)           # +180 thru -180 degrees in degrees, galaxy centered
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

    pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'))
    #pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'), vmin=1.025, vmax=1.21)

    #gridColor = 'black'
    gridColor = 'white'

    # horizonal thin black line
    plt.axhline(y =   0, linewidth=0.5, color=gridColor)

    # vertical thin black lines
    plt.axvline(x =  90, linewidth=0.5, color=gridColor)
    plt.axvline(x =   0, linewidth=0.5, color=gridColor)
    plt.axvline(x = -90, linewidth=0.5, color=gridColor)

    cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

    plt.title(titleS)
    #plt.grid(ezGalDispGrid)
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    plt.xlim(180, -180)        # in degrees
    plt.xticks([ 180,   90,   0,   -90,   -180],
               ['180', '90', '0', '-90', '-180'])

    plt.ylim(-velocitySpanMax, velocitySpanMax)        # in velocity

    # all used velGLonUEdge are red  shifted
    plt.plot(np.arange(-180, +181, 1), velGLonUEdge, 'r.')

    # all used velGLonLEdge are blue shifted
    plt.plot(np.arange(-180, +181, 1), velGLonLEdge, 'b.')

    plt.title(titleS)
    #plt.grid(ezGalDispGrid)
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    plt.xlim(180, -180)        # in degrees
    plt.xticks([ 180,   90,   0,   -90,   -180],
               ['180', '90', '0', '-90', '-180'])

    ylabelS = 'Velocity Edges: Upper (Red) and Lower (Blue) (km/s)\n'
    ylabelS += f'ezGalVelGLonEdgeLevelL = {ezGalVelGLonEdgeLevelL[0]:0.3f}  {ezGalVelGLonEdgeLevelL[1]:d}  {ezGalVelGLonEdgeLevelL[2]:d}'
    plt.ylabel(ylabelS)

    velGLonUEdgeQ1Max = np.nanmax(velGLonUEdge[180:271])
    print('                         velGLonUEdgeQ1Max =', velGLonUEdgeQ1Max, 'at glon =',
        np.where(velGLonUEdge[180:271] == velGLonUEdgeQ1Max)[-1][0])    # use last element of list

    if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
        os.remove(pltNameS)
    plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal541velGLonEdges():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global ezGalVelGLonEdgeLevelL   # float list
    global velGLonUEdge             # float array
    global velGLonLEdge             # float array

    global titleS                   # string
    global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 541 and 541 <= ezGalPlotRangeL[1] and velGLonUEdge.any()):
        return(0)       # plot not needed

    pltNameS = f'ezGal541velGLonEdges_{ezGalVelGLonEdgeLevelL[0]:0.4f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

    plt.clf()

    # horizonal thin black line
    plt.axhline(y =   0, linewidth=0.5, color='black')

    # vertical thin black lines
    plt.axvline(x =  90, linewidth=0.5, color='black')
    plt.axvline(x =   0, linewidth=0.5, color='black')
    plt.axvline(x = -90, linewidth=0.5, color='black')

    # all used velGLonUEdge are red  shifted
    plt.plot(np.arange(-180, +181, 1), velGLonUEdge, 'r.')

    # all used velGLonLEdge are blue shifted
    plt.plot(np.arange(-180, +181, 1), velGLonLEdge, 'b.')


    plt.title(titleS)
    #plt.grid(ezGalDispGrid)
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    plt.xlim(180, -180)        # in degrees
    plt.xticks([ 180,   90,   0,   -90,   -180],
               ['180', '90', '0', '-90', '-180'])

    ylabelS = 'Velocity Upper Edge (Red) and Lower Edge (Blue)  (km/s)\n'
    ylabelS += f'ezGalVelGLonEdgeLevelL = {ezGalVelGLonEdgeLevelL[0]:0.3f}  {ezGalVelGLonEdgeLevelL[1]:d}  {ezGalVelGLonEdgeLevelL[2]:d}'
    plt.ylabel(ylabelS)
    plt.ylim(-270, 270)

    velGLonUEdgeQ1Max = np.nanmax(velGLonUEdge[180:271])
    print('                         velGLonUEdgeQ1Max =', velGLonUEdgeQ1Max, 'at glon =',
        np.where(velGLonUEdge[180:271] == velGLonUEdgeQ1Max)[-1][0])    # use last element of list

    if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
        os.remove(pltNameS)
    plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal550galRot():

    global plotCountdown            # integer

    global ezGalVelGLonEdgeLevelL   # float list
    global velGLonUEdge             # float array

    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 550 and 550 <= ezGalPlotRangeL[1] and velGLonUEdge.any()):
        return(0)       # plot not needed

    pltNameS = f'ezGal550galRot_{ezGalVelGLonEdgeLevelL[0]:0.4f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    #print('                         velGLonUEdge =', velGLonUEdge)

    plt.clf()

    # Status: for Galactic plane crossings, velGLonUEdge are max velocities vs Galactic longitude.
    # Page 45 Eq2 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf
    #   says for 0 <= gLon <= 90 ("quadrant I"), the max Galactic velocity around Galactic center
    #   = galVelMax
    #   = galGasVelMaxKm + (Sun Galactic rotation speed) * sin(gLon)
    # https://en.wikipedia.org/wiki/Sun says (Sun Galactic rotation speed) is 220 km/s
    #   = galGasVelMaxKm + (220 km/s)                    * sin(gLon)
    galGasVelMaxKm = np.add(velGLonUEdge[180:180 + 91], 220 * np.sin(np.radians(np.arange(91))))   # in km/s

    #print('                         velGLonUEdge[180:180 + 91] =', velGLonUEdge[180:180 + 91])
    #print('                         np.sin(np.radians(np.arange(91)) =', np.sin(np.radians(np.arange(91))))
    #print('                         galGasVelMaxKm =', galGasVelMaxKm)

    # calculate galGasRadiusKm[]
    # Page 54 Eq3 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf
    #   says for 0 <= gLon <= 90 ("quadrant I"), the Galactic gas radius from Galactic center
    #   = galGasRadiusKm
    #   = (Solar radius from Galactic center) * (Sun Galactic rotation speed) * sin(gLon) /
    #       ((Sun Galactic rotation speed) * sin(gLon) + velGLonUEdge[180:180 + 91])
    # https://en.wikipedia.org/wiki/Galactic_Center says (Solar radius from Galactic center) is 26,000 ly
    # https://en.wikipedia.org/wiki/Light-year says light year lt is 9.46e12 km
    #   = (26000 ly * 9.46e12 km/ly)          * (220 km/s)                    * sin(gLon) /
    #       ((220 km/s)                    * sin(gLon) + velGLonUEdge[180:180 + 91])
    galGasRadiusKm = (26000. * 9.46e12) * 220. * np.sin(np.radians(np.arange(91))) \
        / (220. * np.sin(np.radians(np.arange(91))) + velGLonUEdge[180:180 + 91])   # in km
    #galGasRadiusLy = galGasRadiusKm / 9.46e12                                       # in light years
    galGasRadiusKpc = galGasRadiusKm / 3.0857e16                                    # in kiloparsecs
    #print('                         galGasRadiusLy.max() =', galGasRadiusLy.max())
    print('                         galGasRadiusKpc.max() =', galGasRadiusKpc.max())


    #plt.plot(galGasRadiusLy, galGasVelMaxKm, 'g.')
    plt.plot(galGasRadiusKpc, galGasVelMaxKm, 'g.')

    plt.title(titleS)
    plt.grid(ezGalDispGrid)
    #plt.xlabel('Gas Radius from Galactic Center (Light Years)  (Sun = 26,000 ly)')
    plt.xlabel('Gas Radius from Galactic Center (kiloparsecs)  (Sun = 8 kpc)')
    #plt.xlim(0, 26000)        # radius from 0 to Solar radius from Galactic center (=26000 light years)
    #plt.xticks([0,   5000.,   10000.,   15000.,   20000.,   25000.],
    #           ['0', '5,000', '10,000', '15,000', '20,000', '25,000'])
    plt.xlim(-0.2, 8.5)

    ylabelS = 'Gas Max Velocity around Galactic Center (km/s)\n'
    ylabelS += f'ezGalVelGLonEdgeLevelL = {ezGalVelGLonEdgeLevelL[0]:0.3f}  {ezGalVelGLonEdgeLevelL[1]:d}  {ezGalVelGLonEdgeLevelL[2]:d}'
    plt.ylabel(ylabelS)

    ax = plt.gca()
    #ax.text(0.95, 0.05, '( wikipedia.org/wiki/Sun says "about 220 km/s" )', horizontalalignment='right', transform=ax.transAxes)
    ax.text(0.02, 0.95, '( wikipedia.org/wiki/Sun says "about 220 km/s" )', transform=ax.transAxes)

    galGasVelMaxKmQ1Max = np.nanmax(galGasVelMaxKm)
    plt.ylim(0, 1.1*galGasVelMaxKmQ1Max)

    velGLonUEdgeQ1Max = np.nanmax(velGLonUEdge[180:271])
    print('                         velGLonUEdgeQ1Max =', velGLonUEdgeQ1Max, 'at glon =',
        np.where(velGLonUEdge[180:271] == velGLonUEdgeQ1Max)[0][0])     # use first element of list

    print('                         galGasVelMaxKmQ1Max =', galGasVelMaxKmQ1Max, 'at glon =',
        np.where(galGasVelMaxKm == galGasVelMaxKmQ1Max)[0][0])     # use first element of list
    #ax.text(0.95, 0.12, f'Max = {int(galGasVelMaxKmQ1Max):d}', horizontalalignment='right', transform=ax.transAxes)
    ax.text(0.02, 0.89, f'maximum = {int(galGasVelMaxKmQ1Max):d} = {int(100.*galGasVelMaxKmQ1Max/220):d}%', transform=ax.transAxes)
    # 230509: LTO15 (-ezGalVelGLonEdgeLevelL 1.05 30 160) sees galGasVelMaxKmQ1Max as 224
    #   wikipedia.org/wiki/Sun says "about 220 km/s"
    #   https://astronomy.stackexchange.com/questions/47521/how-was-the-speed-of-the-sun-around-the-milky-way-galaxy-calculated
    #       speaks of 220, 220-230, 250, 230, 240, 246, 200-279, 218 and 220~250 km/s
    #       and has a graph with large error ranges
    #   224 / 220 is 1.01 is 101% which looks close
    # 230509: LTO16 (-ezGalVelGLonEdgeLevelL 1.16 43 125) sees galGasVelMaxKmQ1Max as 224
    #   224 / 220 is 1.01 is 101% which looks close

    if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
        os.remove(pltNameS)
    plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal551galRot2():
    # Galaxy Rotation in 2 quadrants (gLon from 0 to 180)

    global plotCountdown            # integer

    global ezGalVelGLonEdgeLevelL   # float list
    global velGLonUEdge             # float array
    global velGLonLEdge             # float array

    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 551 and 551 <= ezGalPlotRangeL[1] and velGLonUEdge.any()):
        return(0)       # plot not needed

    pltNameS = f'ezGal551galRot2_{ezGalVelGLonEdgeLevelL[0]:0.4f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    print('                         velGLonUEdge =', velGLonUEdge)

    plt.clf()

    # https://en.wikipedia.org/wiki/Galactic_quadrant
    #   where l is galactic longitude:
    #       1st galactic quadrant   I –   0 ≤ l ≤  90 degrees
    #       2nd galactic quadrant  II –  90 ≤ l ≤ 180 degrees
    #       3rd galactic quadrant III – 180 ≤ l ≤ 270 degrees
    #       4th galactic quadrant  IV – 270 ≤ l ≤ 360 degrees

    # Status: for Galactic plane crossings, velGLonUEdge are max radial-from-Sun velocities vs Galactic longitude.
    # Page 45 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf
    #   says for 0 <= gLon <= 90 ("quadrant I"), the max gas velocity around Galactic center
    #   = galVelMax
    #   = galGasVelMaxKm + (Sun Galactic rotation speed) * sin(gLon)
    # https://en.wikipedia.org/wiki/Sun says (Sun Galactic rotation speed) is 220 km/s
    #   = galGasVelMaxKm + (220 km/s)                    * sin(gLon)
    galGasVelMaxUKm = np.add(velGLonUEdge[180:180 + 91], 220 * np.sin(np.radians(np.arange(91))))   # in km/s
    galGasVelMaxLKm = np.add(velGLonLEdge[90:90 + 91][::-1], 220 * np.sin(np.radians(np.arange(91))))   # in km/s

    #galGasVelMaxKm = np.concatenate([galGasVelMaxKm, galGasVelMax2QKm])
    #print('                         velGLonUEdge[180:180 + 91] =', velGLonUEdge[180:180 + 91])
    #print('                         np.sin(np.radians(np.arange(91)) =', np.sin(np.radians(np.arange(91))))
    print('                         galGasVelMaxUKm =', galGasVelMaxUKm)

    plt.plot(galGasVelMaxUKm, 'r.')
    plt.plot(galGasVelMaxLKm, 'b.')

    galGasRadiusUKm = (26000. * 9.46e12) * 220. * np.sin(np.radians(np.arange(91))) \
        / 220. * np.sin(np.radians(np.arange(91))) + galGasVelMaxUKm             # in km
    galGasRadiusLKm = (26000. * 9.46e12) * 220. * np.sin(np.radians(np.arange(91))) \
        / 220. * np.sin(np.radians(np.arange(91))) + galGasVelMaxLKm             # in km

    plt.title(titleS)
    plt.grid(ezGalDispGrid)
    plt.xlabel('Gas Radius from Galactic Center (Light Years)  (Sun = 26,000 ly)')
    ##########plt.xlim(0, 26000)        # radius from 0 to Solar radius from Galactic center (=26000 light years)
    ##########plt.xticks([0,   5000.,   10000.,   15000.,   20000.,   25000.],
    ##########           ['0', '5,000', '10,000', '15,000', '20,000', '25,000'])

    ylabelS = 'Gas Max Velocity around Galactic Center (km/s)\n'
    ylabelS += f'ezGalVelGLonEdgeLevelL = {ezGalVelGLonEdgeLevelL[0]:0.3f}  {ezGalVelGLonEdgeLevelL[1]:d}  {ezGalVelGLonEdgeLevelL[2]:d}'
    plt.ylabel(ylabelS)

    if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
        os.remove(pltNameS)
    plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal559planetRot():

    global plotCountdown            # integer

    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 559 and 559 <= ezGalPlotRangeL[1]):
        return(0)       # plot not needed

    pltNameS = f'ezGal559planetRot.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    #print('                         velGLonUEdge =', velGLonUEdge)

    plt.clf()

    # https://en.wikipedia.org/wiki/Planet#Solar_System
    name               =          ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    semiMajorAxisAU    = np.array([0.39,      0.72,    1.,      1.52,    5.2,       9.54,    19.19,     30.07,     39.42 ])
    orbitalPeriodYears = np.array([0.24,      0.62,    1.,      1.88,   11.86,     29.45,    84.02,    164.79,    247.9  ])

    # https://en.wikipedia.org/wiki/Astronomical_unit says AU = 1.495978707e11 m
    semiMajorAxisKm = semiMajorAxisAU * 1.495978707e8               # into km
    orbitalPeriodSec = orbitalPeriodYears * 365.25 * 24 * 60 * 60   # into sec

    # velocity = circumference / period
    velocityKmPerSec = semiMajorAxisKm * 2 * np.pi / orbitalPeriodSec

    plt.plot(semiMajorAxisAU, velocityKmPerSec, 'bo-')

    for i in range(9):
        plt.text(semiMajorAxisAU[i]+1, velocityKmPerSec[i], name[i], fontsize=9)

    plt.title(titleS)
    #plt.grid(ezGalDispGrid)
    plt.xlabel('Radius from Sun (AU)')
    plt.xlim(-1., 45.)

    plt.ylabel('Velocity around Sun (km/sec)')

    ax = plt.gca()
    ax.text(0.95, 0.95, '( wikipedia.org/wiki/Planet#Solar_System )', horizontalalignment='right', transform=ax.transAxes)
    ax.text(0.52, 0.75, '"Keplerian Rotation"', transform=ax.transAxes)

    if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
        os.remove(pltNameS)
    plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal560galMass():

    global plotCountdown            # integer

    global ezGalVelGLonEdgeLevelL   # float list
    global velGLonUEdge             # float array

    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 560 and 560 <= ezGalPlotRangeL[1] and velGLonUEdge.any()):
        return(0)       # plot not needed

    pltNameS = f'ezGal560galMass_{ezGalVelGLonEdgeLevelL[0]:0.4f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

    plt.clf()

    # Status: for Galactic plane crossings, velGLonUEdge are max velocities vs Galactic longitude.
    # Page 45 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf
    #   says for 0 <= gLon <= 90 ("quadrant I"), the max Galactic velocity around Galactic center
    #   = galVelMax
    #   = galGasVelMaxKm + (Sun Galactic rotation speed) * sin(gLon)
    # https://en.wikipedia.org/wiki/Sun says (Sun Galactic rotation speed) is 220 km/s
    #   = galGasVelMaxKm + (220 km/s)                      * sin(gLon)
    galGasVelMaxKm = np.add(velGLonUEdge[180:180 + 91], 220 * np.sin(np.radians(np.arange(91))))   # in km/s
    #print('                         velGLonUEdge[180:180 + 91] =', velGLonUEdge[180:180 + 91])
    #print('                         np.sin(np.radians(np.arange(91)) =', np.sin(np.radians(np.arange(91))))
    #print('                         galGasVelMaxKm =', galGasVelMaxKm)

    # Page 54 says for 0 <= gLon <= 90 ("quadrant I"), the Galactic gas radius from Galactic center
    #   = galGasRadiusKm
    #   = (Solar radius from Galactic center)      * (Sun Galactic rotation speed) * sin(gLon) /
    #       (Sun Galactic rotation speed) * sin(gLon) + galGasVelMaxKm
    # https://en.wikipedia.org/wiki/Galactic_Center says (Solar radius from Galactic center) is 26,000 ly
    # https://en.wikipedia.org/wiki/Light-year says light year lt is 9.46e12 km
    # https://en.wikipedia.org/wiki/Sun says (Sun Galactic rotation speed) is 220 km/s
    #   = (26000 ly * 9.46e12 km/ly)               * (220 km/s)                    * sin(gLon) /
    #       (220 km/s)                    * sin(gLon) + galGasVelMaxKm
    galGasRadiusKm = (26000. * 9.46e12) * 220. * np.sin(np.radians(np.arange(91))) \
        / 220. * np.sin(np.radians(np.arange(91))) + galGasVelMaxKm             # in km
    #galGasRadiusLy = galGasRadiusKm / 9.46e12                                   # in light years
    galGasRadiusKpc = galGasRadiusKm / 3.0857e16                                # in kiloparsecs
    #print('                         galGasRadiusLy.max() =', galGasRadiusLy.max())
    print('                         galGasRadiusKpc.max() =', galGasRadiusKpc.max())

    # https://phys.libretexts.org/Bookshelves/University_Physics/Book%3A_Physics_(Boundless)/5%3A_Uniform_Circular_Motion_and_Gravitation/5.6%3A_Keplers_Laws
    # equation "(5.6.20)" says G * M / r = v * v
    # M = v * v * r / G
    # with large center mass M, radius r, and gravitational constant G (6.6743e-11 m3 kg-1 s-2)

    # M = v * v * r / G
    # M = (km/s) * (km/s) * (km) / (m3 kg-1 s-2))
    # M = (km/s) * (km/s) * (km) * (m-3 kg s2))
    # M = (k) * (k) * (k) * kg
    galGasVelMaxM = galGasVelMaxKm * 1e3            # km/s to meters/s
    galGasRadiusM = galGasRadiusKm * 1e3            # km   to meters
    galMassKg = np.multiply(np.multiply(galGasVelMaxM, galGasVelMaxM), galGasRadiusM) / 6.6743e-11   # in kg
    print('                         np.nanmax(galMassKg) =', np.nanmax(galMassKg), 'kg')
    print(f'                         np.nanmax(galMassKg) / 1.98e30 = {(np.nanmax(galMassKg)/1.98e30):0.4g} solar masses')
    print('                         solar mass = 1.98e30 kg')
    #print('                         galMassKg =', galMassKg)
    # https://nypost.com/2019/03/11/astronomers-have-figured-out-how-much-the-milky-way-weighs
    # https://en.wikipedia.org/wiki/Milky_Way  says 1.15e12 solar masses
    # https://en.wikipedia.org/wiki/Solar_mass says solar mass is 1.98e30 kg
    # galMassKg prediction = 1.15e12 solarMasses * 1.98e30 kg/solarMasses= 2.277e42 kg
    galMassSolarMasses = galMassKg / 1.98e30

    # lto15hcg data finds np.nanmax(galMassKg) = 2.8552e+41 kg = about a tenth of prediction (missing is dark matter ?)
    #   https://en.wikipedia.org/wiki/Milky_Way says "90% of the mass of the galaxy is dark matter"

    #plt.plot(galGasRadiusLy, galMassKg, 'b.')
    plt.plot(galGasRadiusKpc, galMassSolarMasses, 'b.')

    plt.title(titleS)
    plt.grid(ezGalDispGrid)
    #plt.xlabel('Gas Radius from Galactic Center (Light Years)  (Sun = 26,000 ly)')
    plt.xlabel('Radius from Galactic Center (kiloparsecs)  (Sun = 8 kpc)')
    #plt.xlim(0, 26000)        # radius from 0 to Solar radius from Galactic center (=26000 light years)
    #plt.xticks([0,   5000.,   10000.,   15000.,   20000.,   25000.],
    #           ['0', '5,000', '10,000', '15,000', '20,000', '25,000'])
    plt.xlim(-0.2, 8.5)

    #ylabelS = 'Enclosed Mass (kg)\n'
    ylabelS = 'Enclosed Mass (Solar Masses)\n'
    ylabelS += f'ezGalVelGLonEdgeLevelL = {ezGalVelGLonEdgeLevelL[0]:0.3f}  {ezGalVelGLonEdgeLevelL[1]:d}  {ezGalVelGLonEdgeLevelL[2]:d}'
    plt.ylabel(ylabelS)

    ax = plt.gca()
    #ax.text(0.95, 0.05, '( wikipedia.org/wiki/Milky_Way says 1.15e+12 )', horizontalalignment='right', transform=ax.transAxes)
    ax.text(0.02, 0.95, '( wikipedia.org/wiki/Milky_Way says 1.15e+12 )', transform=ax.transAxes)
    ax.text(0.02, 0.89, '( Sofue 2017 says 1e+11 )', transform=ax.transAxes)

    galMassSolarMassesQ1Max = np.nanmax(galMassSolarMasses)
    plt.ylim(0, 1.1*galMassSolarMassesQ1Max)

    velGLonUEdgeQ1Max = np.nanmax(velGLonUEdge[180:271])
    print('                         velGLonUEdgeQ1Max =', velGLonUEdgeQ1Max, 'at glon =',
        np.where(velGLonUEdge[180:271] == velGLonUEdgeQ1Max)[0][0])     # use first element of list

    print('                         galMassSolarMassesQ1Max =', galMassSolarMassesQ1Max, 'at glon =',
        np.where(galMassSolarMasses == galMassSolarMassesQ1Max)[0][0])     # use first element of list
    #ax.text(0.95, 0.12, f'Max = {galMassSolarMassesQ1Max:0.2e}', horizontalalignment='right', transform=ax.transAxes)
    #ax.text(0.02, 0.89, f'maximum = {galMassSolarMassesQ1Max:0.2e} = {galMassSolarMassesQ1Max/1.15e10:0.1f}%', transform=ax.transAxes)
    ax.text(0.02, 0.83, f'measured maximum = {galMassSolarMassesQ1Max:0.2e}', transform=ax.transAxes)
    ax.text(0.02, 0.77, f'the mass beyond Sun radius is not measured', transform=ax.transAxes)
    # 230509: LTO15 (-ezGalVelGLonEdgeLevelL 1.05 30 160) sees galMassSolarMassesQ1Max as 9.14e10
    #   wikipedia.org/wiki/Milky_Way says 1.15e12
    #   9.14e10 / 1.15e12 is 0.080 is 8.0%
    #   whereas wikipedia.org/wiki/Milky_Way says 'much (about 90%) of the mass of the Milky Way is invisible to telescopes,
    #       neither emitting nor absorbing electromagnetic radiation. This conjectural mass has been termed "dark matter".'
    #   So, remaining 2% of Galactic Mass is beyond Galactic radius of Sun ?  Seems possible.
    # 230509: LTO16 (-ezGalVelGLonEdgeLevelL 1.16 43 125) sees galMassSolarMassesQ1Max as 8.95e10
    #   8.95e10 / 1.15e12 is 0.078 is 7.8%
    #   So, remaining 2.2% of Galactic Mass is beyond Galactic radius of Sun ?  Seems possible.

    ax.text(0.98, 0.15, '( wikipedia.org/wiki/Milky_Way says', horizontalalignment='right', transform=ax.transAxes)
    ax.text(0.97, 0.09, '(about 90%) ... of the Milky Way', horizontalalignment='right', transform=ax.transAxes)
    ax.text(0.99, 0.03, 'is invisible ... termed "dark matter" )', horizontalalignment='right', transform=ax.transAxes)

    if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
        os.remove(pltNameS)
    plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal570galArmsSun():
    # plot Galactic Arms with Sun in center

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global fileFreqBinQty           # integer
    global velocityBin              # float array

    global titleS                   # string
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 570 and 570 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # plot not needed

    pltNameS = 'ezGal570galArmsSun.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

    plt.clf()

    if velGLonP180CountSum:         # if anything in velGLonP180 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusPlotLimit = galSunRadiusKm * 3.

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        for gLonDeg in range(0, 241):
            gLonDegP180 = gLonDeg + 180
            if 360 <= gLonDegP180:
                gLonDegP180 -= 360

            if velGLonP180Count[gLonDegP180] > 0:       # if column used
                #gLonDegRad = gLonDeg * np.pi / 180.
                gLonDegRad = gLonDeg * 0.01745329251
                gLonDegRadMany = np.full(fileFreqBinQty, gLonDegRad)

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
                addend2 = -galSunRadiusKm2 * math.sin(gLonDegRad) * math.sin(gLonDegRad)
                addend3 = galSunRadiusKm * math.cos(gLonDegRad)
                addend1p2 = addend1 + addend2
                # trim negative addend1p2 before sqrt()
                addend1p2[addend1p2 < 0.] = np.nan

                # use positive sqrt()
                addend12 = np.sqrt(addend1p2)      # np.sqrt passes np.nan
                plotRadii = (addend12 + addend3)
                # trim negative plotRadii
                plotRadii[plotRadii < 0.] = np.nan

                polarPlot = ax.scatter(gLonDegRadMany, plotRadii,
                    c=velGLonP180[:,gLonDegP180], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

                # use negative sqrt()
                addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
                plotRadii = (addend12 + addend3)
                # trim negative plotRadii
                plotRadii[plotRadii < 0.] = np.nan

                polarPlot = ax.scatter(gLonDegRadMany, plotRadii,
                    c=velGLonP180[:,gLonDegP180], s=1, cmap=plt.get_cmap('gnuplot'), alpha=0.75)

        # Add a color bar which maps values to colors.
        plt.colorbar(polarPlot, pad=0.1)

        # Plot yellow Sun at center, and green Galactic Center
        polarPlot = ax.scatter(0., 0., c='black', s=120, alpha=0.75)
        polarPlot = ax.scatter(0., 0., c='yellow', s=100, alpha=1.)
        polarPlot = ax.scatter(0., galSunRadiusKm, c='black', s=120, alpha=0.75)
        polarPlot = ax.scatter(0., galSunRadiusKm, c='green', s=100, alpha=1.)

        plt.title(titleS)

        ax.set_rgrids((galSunRadiusPlotLimit,), ('',))
        ax.set_theta_zero_location('N', offset=0.0)
        ax.set_thetagrids((0, 90, 180, 270), ('0', '90', '                               180 and -180 Galactic Longitude', '-90'))
        ax.set_rmax(galSunRadiusPlotLimit)
        ax.set_facecolor("black")

        radiusTextQuadrant = galSunRadiusPlotLimit * 1.4
        ax.text( 0.9,  radiusTextQuadrant, 'Quadrant 1', color='red', verticalalignment='center')
        ax.text( 2.25, radiusTextQuadrant, 'Quadrant 2', color='red', verticalalignment='center')
        ax.text(-2.25, radiusTextQuadrant, 'Quadrant 3', color='red', verticalalignment='center', horizontalalignment='right')
        ax.text(-0.9,  radiusTextQuadrant, 'Quadrant 4', color='red', verticalalignment='center', horizontalalignment='right')

        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nSun = Yellow Dot, Galactic Center = Green Dot\n\n')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal580galArmsGC():
    # plot Galactic Arms with Galactic Center in center

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global fileFreqBinQty           # integer
    global velocityBin              # float array

    global titleS                   # string
    global ezGalPlotRangeL          # integer list

    plotCountdown -= 1

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 580 and 580 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # plot not needed

    pltNameS = 'ezGal580galArmsGC.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

    plt.clf()

    if velGLonP180CountSum:         # if anything in velGLonP180 to plot

        galSunRadiusKm = 26000. * 9.46e12                   # = 2.4596e+17
        galSunRadiusKm2 = galSunRadiusKm * galSunRadiusKm   # = 6.0496322e+34
        galSunRadiusKpc = galSunRadiusKm * 3.24078e-17      # 7.971022488, in kiloparsecs
        print('                         galSunRadiusKpc =', galSunRadiusKpc)
        galSunRadiusPlotLimit = galSunRadiusKm * 4.

        x = []
        y = []
        z = []

        # longest plotRadii needed, to draw edge toward top right corner, at
        #   sqrt(20*20 + 30*30) is 36.06
        plotRadiiEdgeMany = np.linspace(0., 37., 371)       # each tenth of kiloparsec
        velGLonP180MinMany = np.full_like(plotRadiiEdgeMany, velGLonP180.min())

        gLonDegFirst = -1
        gLonDegLast = 241
        for gLonDeg in range(gLonDegFirst, gLonDegLast+1):
            gLonDegP180 = gLonDeg + 180
            if 360 <= gLonDegP180:
                gLonDegP180 -= 360

            #gLonDegRad = gLonDeg * np.pi / 180.
            gLonDegRad = gLonDeg * 0.01745329251

            cosGLonDegRad = math.cos(gLonDegRad)
            sinGLonDegRad = math.sin(gLonDegRad)

            if gLonDegFirst < gLonDeg and gLonDeg < gLonDegLast:
                # plot a radius, but not an edge
                if velGLonP180Count[gLonDegP180] > 0:       # if column used
                    gLonDegRadMany = np.full(fileFreqBinQty, gLonDegRad)

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

                    notIsNanPlotRadii = np.logical_not(np.isnan(plotRadii))

                    if notIsNanPlotRadii.any():
                        # append only those x values where corresponding plotRadii is not a nan
                        #x = plotRadii * cos(gLonDeg - 90.)
                        #x = plotRadii * sin(gLonDegRad)
                        #x = plotRadii * sinGLonDegRad
                        x += (-plotRadii[notIsNanPlotRadii] * sinGLonDegRad).tolist()

                        # append only those y values where corresponding plotRadii is not a nan
                        #y = plotRadii * sin(gLonDeg - 90.)
                        #y = plotRadii * -cos(gLonDegRad)
                        #y = plotRadii * -cosGLonDegRad
                        y += (-plotRadii[notIsNanPlotRadii] * -cosGLonDegRad - galSunRadiusKpc).tolist()

                        # append only those z values where corresponding plotRadii is not a nan
                        z += velGLonP180[:,gLonDegP180][notIsNanPlotRadii].tolist()

                    # use negative sqrt()
                    addend12 = -np.sqrt(addend1p2)      # np.sqrt passes np.nan
                    plotRadii = (addend12 + addend3) * 3.24078e-17      #  in kiloparsec

                    # trim negative plotRadii
                    plotRadii[plotRadii < 0.] = np.nan

                    notIsNanPlotRadii = np.logical_not(np.isnan(plotRadii))
                    if notIsNanPlotRadii.any():
                        # append only those x values where corresponding plotRadii is not a nan
                        #x = plotRadii * cos(gLonDeg - 90.)
                        #x = plotRadii * sin(gLonDegRad)
                        #x = plotRadii * sinGLonDegRad
                        x += (-plotRadii[notIsNanPlotRadii] * sinGLonDegRad).tolist()

                        # append only those y values where corresponding plotRadii is not a nan
                        #y = plotRadii * sin(gLonDeg - 90.)
                        #y = plotRadii * -cos(gLonDegRad)
                        #y = plotRadii * -cosGLonDegRad
                        y += (-plotRadii[notIsNanPlotRadii] * -cosGLonDegRad - galSunRadiusKpc).tolist()

                        # append only those z values where corresponding plotRadii is not a nan
                        z += velGLonP180[:,gLonDegP180][notIsNanPlotRadii].tolist()

            else:
                # plot an edge radius, all as velGLonP180.min()
                x += (-plotRadiiEdgeMany * sinGLonDegRad).tolist()
                y += (-plotRadiiEdgeMany * -cosGLonDegRad - galSunRadiusKpc).tolist()
                z += velGLonP180MinMany.tolist()

        xi = np.linspace(-20., 20., 401)   # in kiloparsec
        yi = np.linspace(20., -20., 401)   # in kiloparsec
        xi, yi = np.meshgrid(xi, yi)
        zi = griddata((x, y), z, (xi, yi), method='linear')
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

        # Plot green Galactic Center at center, and yellow Sun
        polarPlot = ax.scatter(200., 200., c='black', s=120, alpha=1.)
        polarPlot = ax.scatter(200., 200., c='green', s=100, alpha=1.)
        polarPlot = ax.scatter(200., galSunRadiusKpc * 10. + 200., c='black',  s=120, alpha=1.)
        polarPlot = ax.scatter(200., galSunRadiusKpc * 10. + 200., c='yellow', s=100, alpha=1.)

        plt.title(titleS)
        plt.xticks(range(0, 401, 50),
            ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        plt.yticks(range(400, -1, -50),
            ['-20', '-15', '-10', '-5', '0', '5', '10', '15', '20'])
        ax.set_facecolor("black")

        ax.set_xlabel('Distance (kiloparsecs)')
        ax.set_ylabel('Possible Galactic Atomic Hydrogen\n\nGalactic Center = Green Dot, Sun = Yellow Dot')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal60XgLonSpectra():

    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global antXTVTName              # string

    global velocitySpanMax          # float
    global velocityBin              # float array

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 604 and 601 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # plot not needed

    plt.clf()
    pltNameS = 'ezGal60XgLonSpectra.png'

    velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
    #print(' velGLonP180Count =', velGLonP180Count)
    print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )

    velGLonP180CountNonzeroIndex = np.nonzero(velGLonP180Count)
    #print(' velGLonP180CountNonzeroIndex =', velGLonP180CountNonzeroIndex)
    #print(' velGLonP180CountNonzeroIndex[0] =', velGLonP180CountNonzeroIndex[0])

    #velGLonP180MaxIndex = np.argmax(velGLonP180, axis=0)
    velGLonP180Max = velGLonP180.max()
    print('                         gLon of maximum spectrum value =', np.argmax(np.argmax(velGLonP180 == velGLonP180Max, axis=0)) - 180)

    #yLimMax = 1.05 * velGLonP180Max
    yLimMax = 1.01 * velGLonP180Max
    print('                         yLimMax =', yLimMax)

    # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
    #yLimMin = 0.95 * velGLonP180.min()
    yLimMin = 0.99 * velGLonP180.min()
    print('                         yLimMin =', yLimMin)

    # Galactic quadrants 1 through 4
    for gQuadrant in range(1, 5):

        plotNumber = 600 + gQuadrant        # for this Galactic quadrant

        plotCountdown -= 1

        if ezGalPlotRangeL[0] <= plotNumber and plotNumber <= ezGalPlotRangeL[1]:

            #pltNameS = 'ezGal600gLonSpectraQ{gQuadrant}.png'
            pltNameS = f'ezGal{plotNumber}gLonSpectra.png'
            print()
            print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ============')

            plt.clf()

            #fig, axs = plt.subplots(9, 10, figsize=(10, 6), layout='constrained')
            fig, axs = plt.subplots(9, 10, figsize=(10, 6))
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

                if velGLonP180Count[gLonP180]:
                    ax.plot(velocityBin, velGLonP180[:, gLonP180], linewidth=0.5)
                    ax.grid(1)
            
                    ax.set_xlim(-velocitySpanMax, velocitySpanMax)
            
                    ax.set_ylim(yLimMin, yLimMax)

                    ax.tick_params('both',labelsize=5) 

                #ax.set_xticklabels([])
                #ax.set_xticks([], [])
                #ax.set_yticks([], [])
                ax.xaxis.set_ticks([])
                ax.yaxis.set_ticks([])
                ax.axvline(linewidth=0.5, color='b')

                ax.text(0.02, 0.85, 'gLon', fontsize=5, transform=ax.transAxes)

                # add text with form of '+nnn' or '-nnn' degrees
                if gLonP180 < 180:
                    gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
                else:
                    gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros
                ax.text(0.99, 0.85, gLonDegS, fontsize=5, transform=ax.transAxes, horizontalalignment='right')

            if os.path.exists(pltNameS): # to force plot file date update, if file exists, delete it
                os.remove(pltNameS)
            plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal605gLonSpectraCompare():
    # Compare to Page 48 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/Radioastro_21cm_2012b.pdf
    # 230416 LTO15hcg plot is fairly close
    
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global antXTVTName              # string

    global velocitySpanMax          # float
    global velocityBin              # float array

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 605 and 605 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # plot not needed

    plt.clf()
    pltNameS = 'ezGal605gLonSpectraCompare.png'

    velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
    #print(' velGLonP180Count =', velGLonP180Count)
    print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )

    velGLonP180CountNonzeroIndex = np.nonzero(velGLonP180Count)

    velGLonP180Max = velGLonP180.max()
    print('                         gLon of maximum spectrum value =', np.argmax(np.argmax(velGLonP180 == velGLonP180Max, axis=0)) - 180)

    yLimMax = 1.01 * velGLonP180Max
    print('                         yLimMax =', yLimMax)

    # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
    yLimMin = 0.99 * velGLonP180.min()
    print('                         yLimMin =', yLimMin)

    plotNumber = 605

    plotCountdown -= 1

    if ezGalPlotRangeL[0] <= plotNumber and plotNumber <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        #pltNameS = 'ezGal600gLonSpectraQ{gQuadrant}.png'
        pltNameS = f'ezGal{plotNumber}gLonSpectra.png'
        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ============')

        plt.clf()

        #fig, axs = plt.subplots(6, 10, figsize=(10, 6), layout='constrained')
        fig, axs = plt.subplots(6, 10, figsize=(10, 6))
        axsFlat = axs.flat

        fig.suptitle(titleS + f'\nAverage {antXTVTName} Spectra for' \
            + ' Galactic Longitudes 4 to 240', fontsize=12)

        # 4 through 241 by 4
        for i in range(60):

            gLonP180 = 184 + i + i + i + i
            if 360 < gLonP180:
                gLonP180 -= 360

            ax = axsFlat[i]

            if velGLonP180Count[gLonP180]:
                ax.plot(velocityBin, velGLonP180[:, gLonP180], linewidth=0.5)
                ax.grid(1)
        
                ax.set_xlim(-velocitySpanMax, velocitySpanMax)
        
                ax.set_ylim(yLimMin, yLimMax)

                ax.tick_params('both',labelsize=5) 

            #ax.set_xticks([], [])
            #ax.set_yticks([], [])
            ax.xaxis.set_ticks([])
            ax.yaxis.set_ticks([])
            ax.axvline(linewidth=0.5, color='b')

            ax.text(0.02, 0.85, 'gLon', fontsize=5, transform=ax.transAxes)

            # add text with form of '+nnn' or '-nnn' degrees
            if gLonP180 < 180:
                gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
            else:
                gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros
            ax.text(0.99, 0.85, gLonDegS, fontsize=5, transform=ax.transAxes, horizontalalignment='right')

        if os.path.exists(pltNameS): # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal61XgLonSpectraCascade():

    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global antXTVTName              # string

    global velocitySpanMax          # float                 creation
    global velocityBin              # float array           creation

    global ezGal61XGain             # float

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    # if not wanted, or nothing in velGLonP180 to save or plot
    if not (ezGalPlotRangeL[0] <= 614 and 610 <= ezGalPlotRangeL[1] and velGLonP180CountSum):
        return(0)       # plot not needed

    plt.clf()
    pltNameS = 'ezGal61XgLonSpectraCascade.png'

    velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
    #print(' velGLonP180Count =', velGLonP180Count)
    print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )

    velGLonP180CountNonzeroIndex = np.nonzero(velGLonP180Count)
    #print(' velGLonP180CountNonzeroIndex =', velGLonP180CountNonzeroIndex)
    #print(' velGLonP180CountNonzeroIndex[0] =', velGLonP180CountNonzeroIndex[0])

    #velGLonP180MaxIndex = np.argmax(velGLonP180, axis=0)
    velGLonP180Max = velGLonP180.max()
    print('                         gLon of maximum spectrum value =', np.argmax(np.argmax(velGLonP180 == velGLonP180Max, axis=0)) - 180)

    yLimMax = 1.01 * velGLonP180Max
    print('                         yLimMax =', yLimMax)

    # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
    yLimMin = 0.99 * velGLonP180.min()
    print('                         yLimMin =', yLimMin)

    # Galactic quadrants 0 (all) and quadrants 1 through 4
    for gQuadrant in range(0, 5):

        plotNumber = 610 + gQuadrant        # for this Galactic quadrant

        plotCountdown -= 1

        if ezGalPlotRangeL[0] <= plotNumber and plotNumber <= ezGalPlotRangeL[1]:

            pltNameS = f'ezGal{plotNumber}gLonSpectraCascade.png'
            print()
            print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ============')

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
            gain = ezGal61XGain / velGLonP180Max

            for i in range(gLonP180Qty):
                # Vertical offset each line up by this offset amount: but we want the first traces plotted
                # at the top of the chart, and to work our way down
                gLonP180 = gLonP180Stop - i     # gLonP180 decreases from gLonP180Stop down to include gLonP180Start

                # Plot the line, and fill white under it, and increase the z-order each time
                #   so that lower lines and their fills are plotted on top of higher lines
                if gQuadrant:
                    # Galactic quadrants 1 through 4
                    # for the trace with the velGLonP180Max value,
                    #        (velGLonP180[:,gLonP180] * gain - gain) is the trace's baseline
                    y = (velGLonP180[:,gLonP180] * gain - gain) + (gLonP180 - 180.)
                else:
                    # Galactic quadrant "0" (all quadrants)
                    y = (velGLonP180[:,gLonP180-180] * gain - gain) + (gLonP180 - 360.)

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

            if os.path.exists(pltNameS): # to force plot file date update, if file exists, delete it
                os.remove(pltNameS)
            plt.savefig(pltNameS, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor(), transparent=True)



def plotEzGal710gLonDegP180_nnnByFreqBinAvg():

    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global antXTVTName              # string

    global velocitySpanMax          # float
    global velocityBin              # float array

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global ezGalPlotRangeL          # integer list

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 710 and 710 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print('                         velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        #plotCountdown += np.count_nonzero(velGLonP180Count)
        plotCountdown = velGLonP180CountNonzero

        if 1:
            # same ylim for all ezGal710gLonDegP180_nnnByFreqBinAvg plots
            yLimMin = 0.95 * velGLonP180.min()
            print('                         yLimMin =', yLimMin)

            yLimMax = 1.05 * velGLonP180.max()
            print('                         yLimMax =', yLimMax)

        for gLonP180 in range(361):                 # for every column, RtoL
            if velGLonP180Count[gLonP180]:      # if column used

                # create pltNameS with form of 'ezGal710gLonDegP180_nnnByFreqBinAvg.png'
                pltNameS = f'ezGal710gLonDegP180_{gLonP180:03d}ByFreqBinAvg.png'
                print()
                print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ============')
                print('                         gLonP180 =', gLonP180)
                print('                         gLonP180 - 180 =', gLonP180 - 180)
                print('                         velGLonP180Count[gLonP180] =', velGLonP180Count[gLonP180])
                plotCountdown -= 1
                plt.clf()

                # velGLonP180 stores increasing velocity
                plt.plot(velocityBin, velGLonP180[:, gLonP180])

                plt.title(titleS)
                plt.grid(ezGalDispGrid)

                plt.xlabel('Velocity (km/s)')
                plt.xlim(-velocitySpanMax, velocitySpanMax)

                if 0:
                    # new ylim for each ezGal710gLonDegP180_nnnByFreqBinAvg plot
                    yLimMin = 0.95 * velGLonP180[:, gLonP180].min()
                    print('                         yLimMin =', yLimMin)

                    yLimMax = 1.05 * velGLonP180[:, gLonP180].max()
                    print('                         yLimMax =', yLimMax)

                plt.ylim(yLimMin, yLimMax)

                # create gLonDegS with form of '+nnn' or '-nnn' degrees
                if gLonP180 < 180:
                    gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
                else:
                    gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros

                plt.ylabel(f'{antXTVTName} Average Velocity Spectrum' \
                    + f'\n\nGalactic Longitude = {gLonDegS} degrees', \
                    rotation=90, verticalalignment='bottom')

                if os.path.exists(pltNameS): # to force plot file date update, if file exists, delete it
                    os.remove(pltNameS)
                plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def printGoodbye(startTime):

    global programRevision          # string
    global commandString            # string

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
            print('   ezGalDispFreqBin         =', ezGalDispFreqBin)
            #print('   ezGalDetectLevel         =', ezGalDetectLevel)

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
    #global ezGalDispGrid            # integer

    #global ezGalPlotRangeL          # integer list


    startTime = time.time()

    printHello()
    
    ezGalArguments()

    readDataDir()   # creates fileFreqMin, fileFreqMax, fileFreqBinQty, 
                    #   velGLonP180, velGLonP180Count, galDecP90GLonP180Count,
                    #   galDecP90GLonP180Count, fileNameLast

    plotPrep()      # creates titleS, velocitySpanMax, velocityBin

    # velocity plots
    plotEzGal510velGLon()
    plotEzGal519velGLonCount()          # creates ezGal519velGLonCount.txt

    plotEzGal516velGLonAvg()            # velocity spectrum Averages
    plotEzGal517velGLonMax()            # velocity spectrum Maximums

    plotEzGal520velGLonPolarI()
    plotEzGal521velGLonPolarD()
    plotEzGal529velGLonPolarCount()

    plotEzGal530galDecGLon()

    findVelGLonEdges()
    plotEzGal540velGLonEdgesB()
    plotEzGal541velGLonEdges()
    plotEzGal550galRot()
    #plotEzGal551galRot2()
    plotEzGal559planetRot()
    plotEzGal560galMass()

    plotEzGal570galArmsSun()
    plotEzGal580galArmsGC()

    plotEzGal60XgLonSpectra()
    plotEzGal605gLonSpectraCompare()
    plotEzGal61XgLonSpectraCascade()

    plotEzGal710gLonDegP180_nnnByFreqBinAvg()

    printGoodbye(startTime)

if __name__== '__main__':
  main()

# a@u22-221222a:~/aaaEzRABase/lto15hcg$ python3 ../ezRA/ezGal230504b.py  .  -ezGalPlotRangeL 0 699 -ezRAObsName LTO15 -ezGalVelGLonEdgeLevelL 1.01  1.066  52
# a@u22-221222a:~/aaaEzRABase/lto15hcg$ python3 ../ezRA/ezGal230508c.py  .  -ezGalPlotRangeL 540 560 -ezRAObsName LTO15 -ezGalVelGLonEdgeLevelL 1.05 30 160 -ezGal540edgesUFile ezGal540_1.05_30_160.txt

