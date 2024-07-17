programName = 'ezSky240715a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezSky Sky Mapper program,
#   to read ezCon format .ezb condensed data text file(s)
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
#       MollweideL x and y scales not linear, so xticks and yticks wrong
#       Sorry I did not include Az and El as .ezb columns 1 and 2
#       Sorry I ordered gLat before gLon

# ezSky240715a, sys.version
# ezSky240712a, ezSkyBackground1.jpg notes
# ezSky240711a, raw strings for 3 '\' characters to fix the 3 (Python3.12+ ?)
#       SyntaxWarning: invalid escape sequence '\ '
# ezSky240615a, fixed ezSkyGridGalacticBox() division by zero bugs, dusting
# ezSky240607a, ezSkyXYLimL useage note =
#   Milky Way Galaxy center = Sagittarius A* = 17h 45m 40.0409s, −29° 0′ 28.118″
#       17.75 * 15 degrees is 266.25
#   ezRABase\lto16h>py  ..\ezRA\ezSky240606a.py  . -ezSkyInput 14 -ezSkyPlotRangeL 405 405
#       -ezSkyXYLimL 999 999   265.25 267.25   -39 -19   0.5
# ezSky240606a, a default ezSkyXYLimL for ezSky505
# ezSky240603a, dusting, temporarily disabled ezSky406 with the Cygrid module
# ezSky240220a, ezSky201: "<= 304" to "< 304" 2 places
# ezSky240204a, ezSky406 with the Cygrid module
#   https://github.com/bwinkel/cygrid
#   Cygrid: A fast Cython-powered convolution-based gridding module for Python
#   http://adsabs.harvard.edu/abs/2016A%26A...591A..12W
# ezSky240131b.py,
#   galacticGLatHalfDeg, galacticGLonHalfDeg back to gLatHalfDeg, gLonHalfDeg in 92 places,
# ezSky240131a.py, was freeing memory in ezSkyGridGalactic()
# ezSky240130c.py, ezSky505GMIL, ezSkyGridGalacticBox(),
#   # ezSkyXYLimL filter
# ezSky240130b.py, ezSky505GMIL, ezSkyGridGalacticBox(),
#   galacticGLatHalfDeg, galacticGLonHalfDeg to gLatHalfDeg, gLonHalfDeg,
#   order: x before y, and then like in .ezb file: gLat before gLon
# ezSky240130a.py, ezSky505GMIL, ezSkyGridGalacticBox(),
#   radecRaHalfDeg, radecDecHalfDeg to raHalfDeg, decHalfDeg,
#   radecRaHalfDegScaled, radecDecHalfDegScaled to raHalfDegScaled, decHalfDegScaled,
#   radecRaDegMinMaxL, radecDecDegMinMaxL to raDegMinMaxL, decDegMinMaxL
# ezSky240129a.py, ezSky505GMIL, ezSkyGridGalacticBox()
# ezSky240128b.py, ezSky505GMIL, ezSkyGridGalacticBox()
# ezSky240128a.py, ezSky405RIL, print radecRaDegMid and radecDecDegMid,
#   breadcrumb dots and connected dots, helpscreen
# ezSky240126a.py, ezSkyGridRadecBox()
# ezSky240125a.py, ezSky405RIL,
#   calling of ezSkyGridRadec(), ezSkyGridRadecBox(), and ezSkyGridGalactic()
# ezSky240124a.py, ezSky405RIL
# ezSky240123b.py, ezSky405RIL, -ezSkyXYLimL
# ezSky240123a.py, ezSky405RIL radio Sky Radec map Interpolated with XYLimits,
#   -ezSkyXYLimL
# ezSky240108b.py, ezSky450 Grote Reber grid
# ezSky240108a.py, dusting
# ezSky240105a.py, dusting
# ezSky231231a.py, ezSky600 dots
# ezSky231228e.py, ezSky450 Grote Reber
# ezSky231228d.py, ezSky450 Grote Reber, left needing warping
# ezSky231228c.py, ezSky450 Grote Reber, warps ?!
# ezSky231228b.py, ezSky450 Grote Reber, sorta warped !
# ezSky231228a.py, ezSky450 Grote Reber
# ezSky231227d.py, ezSky450 Grote Reber
# ezSky231227a.py, ezSky450 Grote Reber
# ezSky231226c.py, ezSky450 Grote Reber
# ezSky231226b.py, ezSky450 Grote Reber
# ezSky231226a.py, ezSky450 Grote Reber
# ezSky231224a.py, ezSky450 Grote Reber
# ezSky231222a.py, ezSky450 Grote Reber
# ezSky231211a.py, comments
# ezSky231209d.py, ezSky450 Grote Reber
# ezSky231209c.py, ezSky450 Grote Reber
# ezSky231209b.py, ezSky450 Grote Reber
#   ezSky200 thin horizontal lines to matching colors
# ezSky231209a.py, print ezSkyInput in printGoodbye()
#   ezSky200 AntXTVT violet needs green for better contrast
#   ezSky200 AntB           needs next best red contrast
#       AntXTVT violet   becomes newgreen
#       Ref     red      becomes violet
#       AntB    green    becomes red
#               newgreen becomes green
# ezSky231206a.py, ezSky450 Grote Reber
# ezSky231205b.py, ezSky450 Grote Reber
# ezSky231203a.py, red for AntXTVT, violet for Ref
# ezSky231124a.py, red horizontal average lines on ezSky200
# ezSky230827a.py, removed '''
# ezSky230824a.py, print ezSkyPlotRangeL in printGoodbye()
# ezSky230803a.py, plotEzSky1dSamplesAnt and plt.scatter now with s=1
# ezSky230728a.py, add -ezSkyAddRAH and -ezSkyAddDecDeg
# ezSky230708a.py, skipping past ezSky230630axxxxxxxxxxxx.py and
#   retreating to ezSky230629a.py with
#   ezSkyGalCrossingGLatCenter and ezSkyGalCrossingGLatNear and
#   ezSkyGalCrossingGLonCenter and ezSkyGalCrossingGLonNear
# ezSky230630a.py, to match ezGal and ezGLot
#   changed to ezSkyGalCrossingGLatSpanL and ezSkyGalCrossingGLonSpanL
# ezSky230629a.py, ezSkyGalCrossingGLat to ezSkyGalCrossingGLatNear
#   ezSkyGalCrossingGLonCenter, ezSkyGalCrossingGLonNear
# ezSky230610a.py, ezSkyGalCrossingGLatCenter
#   found ezSky512 MollweideL y scale not linear !
# ezSky230527a.py, "Radec" to "RaDec"
# ezSky230413a.py, yLim of ezSky031gLatDegSorted and ezSky032gLatDegSortedCross
#   ezSky032gLatDegSortedCross still has a xTick bug if is the first plotted
# ezSky230412a.py, added plotEzSky031gLatDegSorted(),
#   corrected plotEzSky042gLonDegSortedCross() to plotEzSky032gLatDegSortedCross()
# ezSky230408c.py, plotEzSky042gLonDegSortedCross()
# ezSky230408b.py, maskGalactic, plotEzSkyMollweide(502), plotEzSkyMollweide(512),
#   ezSkyGalCrossingGLat, ezSkyVOGain, plotCountdown
# ezSky230408a.py, plotEzSky041gLonDegSorted()
# ezSky230321a.py, astropy only if needed, only last -ezSkyMaskOutL
# ezSky230320b.py, reorder -ezSkyMaskOutL args
# ezSky230320a.py, masks out and in
# ezSky230319c.py, masks out and in
# ezSky230319b.py, masks out and in
# ezSky230319a.py, masks last in ezSky221004a, masks out and in
# ezSky230318c.py, removed messy plotEzSky502GOI() notes
# ezSky230318b.py, plotEzSky502GOI() with notes
# ezSky230318a.py, plotEzSky502GOI()
# ezSky230317b.py, plotEzSky502GOI()
# ezSky230317a.py, commented plotEzSky502GOI()
# ezSky230316c.py, plotEzSky502GOI() Mollweide, fixed -eX
# ezSky230316b.py, commented Mollweide, ezSky100input_* color traces
# ezSky230316a.py, -eX
# ezSky230311a.py, Galactic Mollweide plotEzSky502GOI()
# ezSky230308a.py, cleanup
# ezSky230305a.py, plt.close(fig) "deprecated in Matplotlib 3.6"
# ezSky221205b.py, new .py header
# ezSky221205a.py, ezSky201RBMax fixed highlight Right Ascensions,
#   allows for ezConAstroMath=2 calculation noise of 1 HalfDeg Declination
# ezSky221202a.py, new ezSky201RBMax highlights wrong Right Ascension,
#   call to plotEzSky201RBMax() commented out
# ezSky221125a.py, ezSky201RBVOMax to ezSky201RBMax
# ezSky221122a.py, ezSky080elDeg ylim -95 to +195
# ezSky221121h.py, ezSky201RBVOMax
# ezSky221118a.py, 'ezSky600azEl_' + ezSkyInputS + '.png'
# ezSky221116a.py, help's -ezSkyPlotRange to -ezSkyPlotRangeL
# ezSky221115a.py, ezSky601 to ezSky600, ezSky600 minus sign typo
# ezSky221111a.py, experimentEzc with AzEl in .ezb Spare1 and Spare2,
#   ezSky070azDeg, ezSky080elDeg, ezSky601azEl,
#   plotEzSky200RBVO() gain error if min == max,
#   plot color of ezSky301RBT and ezSky309RBTC
# ezSky221027a.py, fix ezSky309RBTC plot center offset
# ezSky221017a.py, polishing
# ezSky221015a.py, commas to prints
# ezSky221014a.py, commas to prints
# ezSky221013b.py, directoryListLen now an f-string, raHalfDeg now wraps around, commas to prints
# ezSky221012b.py, galacticGLonHalfDeg now wraps around
# ezSky221012a.py, git prepare, plots renamed, ezSkyVOGain, raHalfDeg -= 720
# ezSky221006b.py, rewrite for git, stole from ezPlot220930a.py
# ezSky220914a.py, polished ezSky200RP_, color to ezSky010


#import matplotlib
#matplotlib.use('agg')
import matplotlib.pyplot as plt

import os
import sys
import time
import datetime

import numpy as np

from scipy.interpolate import griddata
#from scipy.ndimage.filters import gaussian_filter
from scipy.ndimage import gaussian_filter

# to find polygon for mask
#####from PIL import Image, ImageDraw

#from matplotlib.nxutils import points_inside_poly

import math       # for sin() and cos() and radians()



def printUsage():

    global programRevision                  # string

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print()
    print('  Windows:   py      ezSky.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezSky.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezSky Sky Mapper program,')
    print('  to read ezCon format .ezb condensed data text file(s),')
    print('  and optionally create .png plot files.')
    print()
    print('  "radioDataFileDirectories" may be one or more .ezb condensed data text files:')
    print('         py  ezSky.py  bigDish220320_05.ezb')
    print('         py  ezSky.py  bigDish220320_05.ezb bigDish220321_00.ezb')
    print('         py  ezSky.py  bigDish22032*.ezb')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezSky.py  .')
    print('         py  ezSky.py  bigDish2203')
    print('         py  ezSky.py  bigDish2203 bigDish2204')
    print('         py  ezSky.py  bigDish22*')
    print('  "radioDataFileDirectories" may be a mix of .ezb condensed data text files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezSky program,')
    print("  then in order from the ezDefaults.txt in the ezSky.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('DESCRIPTION:')
    print()
    print('  py  ezSky.py -help               (print this help)')
    print('  py  ezSky.py -h                  (print this help)')
    print()
    print('    -ezRAObsName         bigDish   (observatory name for plot titles)')
    print()
    print('    -ezSkyInput          18        (choose input .ezb data column)')
    print()
    print("    -ezSkyAddRAH         9.4       (add to data file's Right Ascension (hours))")
    print("    -ezSkyAddDecDeg      -2.6      (add to data file's Declination     (degrees))")
    print()
    print('    -ezSkyDispGrid       1         (turn on graphical display plot grids)')
    print('    -ezSkyVOGain         100       (vertical offset gain  of ezSky200RBPVO_  plot traces)')
    #print('    -ezSkyTraceColor     blue      (color of plot traces)')
    print('    -ezSkyHalfTallDec    9         (almost half height of ezSky301RBPT_  plot traces',
        '(in halfDegrees))')
    print()
    print('    -ezSkyMaskIn         ezSkyMaskBigDish_-49.7_-90.npz')
    print()
    print('    -ezSkyMaskOutL       ezSkyMaskBigDish_-49.7_-90    -49.7    -90.0')
    print('         (Radio sky mask input for ezSky plots, unseen sky as white,')
    print('          from declination -49.6 to -90 degrees to create radio sky mask.')
    print('          Northern hemisphere: south horizon declination = latitude - 90.')
    print('          Written to file "ezSkyMaskBigDish_-49.7_-90.npz".)')
    print()
    print('    -ezSkyGalCrossingGLatCenter   1.0')
    print('         (defines center of Galactic crossing  in Galactic Latitude degrees)')
    print('    -ezSkyGalCrossingGLatNear     3.0')
    print('         (defines "close to Galactic crossing" in Galactic Latitude degrees)')
    print()
    print('    -ezSkyGalCrossingGLonCenter   71.0')
    print('         (defines center of Galactic crossing  in Galactic Longitude degrees)')
    print('    -ezSkyGalCrossingGLonNear     2.0')
    print('         (defines "close to Galactic crossing" in Galactic Longitude degrees)')
    print()
    print('    -ezSkyPlotRangeL     0  300    (save only this range of ezSky plots to file, to save time)')
    print()
    #print('    -ezSkyXYLimL controls the zoomed interpolated ezSky405 and ezSky406 plots')
    print('    -ezSkyXYLimL controls the zoomed interpolated ezSky405 plot')
    print('    -ezSkyXYLimL     999  999     999  999     999 999      0')
    print('         (also plot into minimum-sized sky boxes,')
    print('          with X and Y used limits,')
    print('          with no data dots (size 0))')
    print('    -ezSkyXYLimL     0.04 .05     999  999     999 999      0')
    print('         (also plot into 0.04 by 0.05  sky boxes (RaDec or Galactic degrees),')
    print('          with X and Y used limits,')
    print('          with no data dots (size 0))')
    print('    -ezSkyXYLimL     999  999     12.3 14.5    67  78.95    10')
    print('         (also plot into minimum-sized sky boxes,')
    print('          with XMin XMax YMin YMax minimum and maximum limits (RaDec or Galactic degrees),')
    print('          with data dot size of 10)')
    print('    -ezSkyXYLimL     0.04 .05     12.3 14.5    67  78.95    -5')
    print('         (also plot into 0.04 by 0.05  sky boxes (RaDec or Galactic degrees),')
    print('          with XMin XMax YMin YMax minimum and maximum limits (RaDec or Galactic degrees),')
    print('          with data connected dot size of 5)')
    print()
    print(r'    -ezDefaultsFile ..\bigDish.txt      (additional file of ezRA arguments)')
    print()
    print('    -eXXXXXXXXXXXXXXzIgonoreThisWholeOneWord')
    print('         (any one word starting with -eX is ignored, handy for long command line editing)')
    print()
    print('EXAMPLES:')
    print()
    print(r'  Windows:   py       ..\ezRA\ezSky.py  .')
    print(r'             py       ..\ezRA\ezSky.py  .  -ezSkyInput  18  -ezSkyPlotRangeL  200  450')
    print()
    print('  Linux:     python3  ../ezRA/ezSky.py  .')
    print('             python3  ../ezRA/ezSky.py  .  -ezSkyInput  18  -ezSkyPlotRangeL  200  450')
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
    print('            ezSky.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print(' Python sys.version =', sys.version)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezSkyArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsName                      # string

    global ezSkyAddRAH                      # float
    global ezSkyAddDecDeg                   # float

    global ezSkyDispGrid                    # integer
    global ezSkyInput                       # integer
    global ezSkyVOGain                      # float
    global ezSkyHalfTallDec                 # integer

    global ezSkyGalCrossingGLatCenter       # float
    global ezSkyGalCrossingGLatNear         # float
    global ezSkyGalCrossingGLonCenter       # float
    global ezSkyGalCrossingGLonNear         # float

    global ezSkyMaskOutL                    # list of string and floats
    global ezSkyMaskInL                     # list of strings
    global ezSkyXYLimL                      # list of floats

    global ezSkyPlotRangeL                  # integer list

    print()
    print('   ezSkyArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileNameInput, 'r')

        print('      success opening ' + ezDefaultsFileNameInput)

        while 1:
            fileLine = fileDefaults.readline()

            # len(fileLine): 0=EOF  1=LFonly  2=1CharacterWithLF
            if not fileLine:         # if end of file
                break                     # get out of while loop

            fileLineSplit = fileLine.split()
            # len(fileLineSplit): 0=EOF  0=LFonly  1=1CharacterWithLF
            if not fileLineSplit:    # if blank line
                continue                  #   skip to next line

            if fileLineSplit[0][0] == '#':    # ignoring whitespace, if first character of first word
                continue                  # it is a comment, skip to next line


            # be kind, ignore argument keyword capitalization
            fileLineSplit0Lower = fileLineSplit[0].lower()

            # ezRA arguments used by multiple programs:
            if fileLineSplit0Lower == '-ezRAObsName'.lower():
                ezRAObsName = fileLineSplit[1]
                #ezRAObsName = uni.encode(fileLineSplit[1])
                #ezRAObsName = str.encode(fileLineSplit[1])

            # ezSky arguments:
            elif fileLineSplit0Lower == '-ezSkyAddRAH'.lower():
                ezSkyAddRAH = float(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyAddDecDeg'.lower():
                ezSkyAddDecDeg = float(fileLineSplit[1])


            elif fileLineSplit0Lower == '-ezSkyDispGrid'.lower():
                ezSkyDispGrid = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyInput'.lower():
                ezSkyInput = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyVOGain'.lower():
                ezSkyVOGain = float(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyGalCrossingGLatCenter'.lower():
                ezSkyGalCrossingGLatCenter = float(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyGalCrossingGLatNear'.lower():
                ezSkyGalCrossingGLatNear = float(fileLineSplit[1])


            elif fileLineSplit0Lower == '-ezSkyGalCrossingGLonCenter'.lower():
                ezSkyGalCrossingGLonCenter = float(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyGalCrossingGLonNear'.lower():
                ezSkyGalCrossingGLonNear = float(fileLineSplit[1])


            elif fileLineSplit0Lower == '-ezSkyHalfTallDec'.lower():
                ezSkyHalfTallDec = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyPlotRangeL'.lower():
                ezSkyPlotRangeL[0] = int(fileLineSplit[1])
                ezSkyPlotRangeL[1] = int(fileLineSplit[2])

            elif fileLineSplit0Lower == '-ezSkyMaskOutL'.lower():
                ezSkyMaskOutL = []
                ezSkyMaskOutL.append(fileLineSplit[1])
                ezSkyMaskOutL.append(float(fileLineSplit[2]))
                ezSkyMaskOutL.append(float(fileLineSplit[3]))

            elif fileLineSplit0Lower == '-ezSkyMaskIn'.lower():
                ezSkyMaskInL.append(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyXYLimL'.lower():
                ezSkyMaskOutL = []
                ezSkyMaskOutL.append(float(fileLineSplit[1]))
                ezSkyMaskOutL.append(float(fileLineSplit[2]))
                ezSkyMaskOutL.append(float(fileLineSplit[3]))
                ezSkyMaskOutL.append(float(fileLineSplit[4]))
                ezSkyMaskOutL.append(float(fileLineSplit[5]))
                ezSkyMaskOutL.append(float(fileLineSplit[6]))
                ezSkyMaskOutL.append(float(fileLineSplit[7]))


            elif 6 <= len(fileLineSplit0Lower) and fileLineSplit0Lower[:6] == '-ezSky'.lower():
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
    	#print ('   Warning: Error in opening file or reading ' + ezDefaultsFileNameInput + ' file.')
    	##print ('   ... Using defaults ...')
    	#print ()
    	#print ()
    	#print ()
    	#print ()
    	pass

    else:
        fileDefaults.close()                # have processed all available lines in this defaults file



def ezSkyArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsName                      # string

    global ezSkyAddRAH                      # float
    global ezSkyAddDecDeg                   # float

    global ezSkyDispGrid                    # integer
    global ezSkyInput                       # integer
    global ezSkyVOGain                      # float
    global ezSkyHalfTallDec                 # integer

    global ezSkyGalCrossingGLatCenter       # float
    global ezSkyGalCrossingGLatNear         # float
    global ezSkyGalCrossingGLonCenter       # float
    global ezSkyGalCrossingGLonNear         # float

    global ezSkyMaskOutL                    # list of string and floats
    global ezSkyMaskInL                     # list of strings
    global ezSkyXYLimL                      # list of floats

    global ezSkyPlotRangeL                  # integer list

    global cmdDirectoryS                    # string            create

    print()
    print('   ezSkyArgumentsCommandLine ===============')

    cmdLineSplit = commandString.split()
    cmdLineSplitLen = len(cmdLineSplit)
        
    if cmdLineSplitLen < 2:
        # need at least one data directory or file
        printUsage()

    cmdLineSplitIndex = 1
    cmdDirectoryS = ''

    while cmdLineSplitIndex < cmdLineSplitLen:
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
            # Must be an argument.
            # Remove '-'
            cmdLineArg = cmdLineSplit[cmdLineSplitIndex][1:]
            # ignoring whitespace, first character of cmdLineSplit word was '-', now removed
            if cmdLineArg[0] == '-':
                cmdLineArg = cmdLineArg[1:]
                # ignoring whitespace, first 2 characters of cmdLineSplit word were '--', now removed

            # be kind, ignore argument keyword capitalization
            cmdLineArgLower = cmdLineArg.lower()
            #print()
            #print()
            #print()
            #print()
            #print('= cmdLineArg =', cmdLineArg, '=')
            cmdLineSplitIndex += 1      # point to first argument value


            if cmdLineArgLower == 'help':
                printUsage()

            elif cmdLineArgLower == 'h':
                printUsage()


            # ezRA arguments used by multiple programs:
            elif cmdLineArgLower == 'ezRAObsName'.lower():
                ezRAObsName = cmdLineSplit[cmdLineSplitIndex]   # cmd line allows only one ezRAObsName word
                #ezRAObsName = uni.encode(cmdLineSplit[cmdLineSplitIndex])
                #ezRAObsName = str.encode(cmdLineSplit[cmdLineSplitIndex])
            

            # ezSky arguments:
            elif cmdLineArgLower == 'ezSkyAddRAH'.lower():
                ezSkyAddRAH = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyAddDecDeg'.lower():
                ezSkyAddDecDeg = float(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezSkyDispGrid'.lower():
                ezSkyDispGrid = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyInput'.lower():
                ezSkyInput = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyVOGain'.lower():
                ezSkyVOGain = float(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezSkyGalCrossingGLatCenter'.lower():
                ezSkyGalCrossingGLatCenter = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyGalCrossingGLatNear'.lower():
                ezSkyGalCrossingGLatNear = float(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezSkyGalCrossingGLonCenter'.lower():
                ezSkyGalCrossingGLonCenter = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyGalCrossingGLonNear'.lower():
                ezSkyGalCrossingGLonNear = float(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezSkyHalfTallDec'.lower():
                ezSkyHalfTallDec = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyPlotRangeL'.lower():
                ezSkyPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezSkyPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezDefaultsFile'.lower():
                ezSkyArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyMaskOutL'.lower():
                ezSkyMaskOutL = []
                ezSkyMaskOutL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezSkyMaskOutL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyMaskOutL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'ezSkyMaskIn'.lower():
                ezSkyMaskInL.append(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyXYLimL'.lower():
                ezSkyXYLimL = []
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezSkyXYLimL.append(float(cmdLineSplit[cmdLineSplitIndex]))


            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 2 <= len(cmdLineArgLower) and cmdLineArgLower[:2] == 'ex':
                cmdLineSplitIndex -= 1
                #pass

            # before -eX, old spelling:
            elif 4 <= len(cmdLineArgLower) and cmdLineArgLower[:4] == 'ezez':
                # ignore this one word that starts with '-ezez'
                cmdLineSplitIndex -= 1
                #pass

            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(cmdLineArg)
                print()
                print()
                print()
                print()
                exit()
                
        cmdLineSplitIndex += 1



def ezSkyArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global programRevision                  # string
    global commandString                    # string

    global ezRAObsName                      # string

    global ezSkyAddRAH                      # float
    global ezSkyAddDecDeg                   # float

    global ezSkyDispGrid                    # integer
    global ezSkyInput                       # integer
    global ezSkyVOGain                      # float
    global ezSkyHalfTallDec                 # integer
    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer

    global ezSkyGalCrossingGLatCenter       # float
    global ezSkyGalCrossingGLatNear         # float
    global ezSkyGalCrossingGLonCenter       # float
    global ezSkyGalCrossingGLonNear         # float

    global ezSkyMaskOutL                    # list of string and floats
    global ezSkyMaskInL                     # list of strings
    global ezSkyXYLimL                      # list of floats

    global radecPower                       # empty list or float 1d array
    global radecPowerBox                    # empty list or float 1d array
    global galacticPower                    # empty list or float 1d array
    global galacticPowerBox                 # empty list or float 1d array

    global ezSkyBackground1                 # string
    global ezSkyBackground1XMax             # integer
    global ezSkyBackground1YMax             # integer

    # defaults
    #ezRAObsName = 'LebanonKS'
    ezRAObsName = ''                        # silly name

    ezSkyAddRAH    = 0.
    ezSkyAddDecDeg = 0.

    ezSkyInput    = 14
    ezSkyDispGrid = 0

    ezSkyVOGain = 50.

    # (ezSkyHalfTallDec + 1 + ezSkyHalfTallDec) = thickness of tall plot trace (last drawn wins)
    ezSkyHalfTallDec = 3

    ezSkyGalCrossingGLatCenter = 0.
    ezSkyGalCrossingGLatNear   = 0.
    ezSkyGalCrossingGLonCenter = 0.
    ezSkyGalCrossingGLonNear   = 0.
    
    ezSkyMaskOutL    = []
    ezSkyMaskInL     = []
    ezSkyXYLimL      = [999., 999.,   999., 999.,   999., 999.,   0.]
    radecPower       = []                      # flag as empty
    radecPowerBox    = []                      # flag as empty
    galacticPower    = []                      # flag as empty
    galacticPowerBox = []                      # flag as empty

    ezSkyPlotRangeL = [0, 9999]             # save this range of plots to file

    plotCountdown = 26                      # number of possible plots still to print + 1

    # process arguments from ezDefaults.txt file in the same directory as this ezCon program
    ezSkyArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezSkyArgumentsFile('ezDefaults.txt')

    ezSkyArgumentsCommandLine()             # process arguments from command line

    if not cmdDirectoryS:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  No .ezb data files nor directories requested.')
        print()
        print()
        print()
        print()
        exit()
    
    #ezSkyMaskFileLong = '.' + os.path.sep + ezSkyMaskFile
    # in same directory as this program
    # ezRA's ezSky uses ezSkyBackground1.jpg
    #   which came with Jun-24-2021 emailed permission from Whitham D. Reeve
    #       http://www.reeve.com/Documents/Articles%20Papers/Reeve_CelestialRadioSources.pdf
    #   who got the image with permission from
    #   the International Telecommunication Union (ITU) Recommendation P.372-8 (04/03)
    #       https://www.itu.int/rec/R-REC-P.372-8-200304-S/en
    #   which leads to pages 20-23 of
    #       https://www.itu.int/dms_pubrec/itu-r/rec/p/R-REC-P.372-8-200304-S!!PDF-E.pdf
    ezSkyBackground1 = os.path.dirname(__file__) + os.path.sep + 'ezSkyBackground1.jpg'  
    ezSkyBackground1XMax = 1624
    ezSkyBackground1YMax =  812

    # print status
    print()
    print('   ezRAObsName =', ezRAObsName)
    print()
    print('   ezSkyAddRAH    =', ezSkyAddRAH)
    print('   ezSkyAddDecDeg =', ezSkyAddDecDeg)
    print()
    print('   ezSkyInput  =', ezSkyInput)
    print('   ezSkyVOGain =', ezSkyVOGain)
    print('   ezSkyHalfTallDec =', ezSkyHalfTallDec)
    print('   ezSkyDispGrid    =', ezSkyDispGrid)
    print('   ezSkyPlotRangeL  =', ezSkyPlotRangeL)
    print()
    print('   ezSkyGalCrossingGLatCenter =', ezSkyGalCrossingGLatCenter)
    print('   ezSkyGalCrossingGLatNear   =', ezSkyGalCrossingGLatNear)
    print('   ezSkyGalCrossingGLonCenter =', ezSkyGalCrossingGLonCenter)
    print('   ezSkyGalCrossingGLonNear   =', ezSkyGalCrossingGLonNear)
    print()
    print('   ezSkyMaskInL     =', ezSkyMaskInL)
    print('   ezSkyMaskOutL    =', ezSkyMaskOutL)
    print('   ezSkyXYLimL      =', ezSkyXYLimL)

    # sanity tests
    if ezSkyMaskOutL and ezSkyMaskOutL[1] <= ezSkyMaskOutL[2]:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  ezSkyMaskOutL: ', ezSkyMaskOutL[1], 'is <=', ezSkyMaskOutL[2])
        print()
        print()
        print()
        print()
        exit()



def readDataDir():
    # Open each .ezb radio file in each directory and read individual lines.
    # Creates ezRAObsName, ezSkyInputS, fileNameLast, raH, decDeg, gLatDeg, gLonDeg, power, antLen

    global cmdDirectoryS            # string

    global ezRAObsName              # string                                    create
    global ezSkyInput               # integer
    global ezSkyInputS              # string                                    create
    global fileNameLast             # string                                    create

    global ezSkyAddRAH              # float
    global ezSkyAddDecDeg           # float

    global raH                      # float 1d array                            create
    global decDeg                   # float 1d array                            create
    global gLatDeg                  # float 1d array                            create
    global gLonDeg                  # float 1d array                            create
    global azDeg                    # float 1d array                            create
    global elDeg                    # float 1d array                            create
    global power                    # float 1d array                            create
    global antLen                   # integer                                   create

    print()
    print('   readDataDir ===============')

    # initialize numpys
    raH     = np.array([])
    decDeg  = np.array([])
    gLatDeg = np.array([])
    gLonDeg = np.array([])
    azDeg   = np.array([])
    elDeg   = np.array([])
    power   = np.array([])          # from selected .ezb column

    ezbQty = 0       # number of .ezb files
    antLen = 0       # number of samples in all .ezb files

    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    
    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]

        # if arguments are .ezb filenames,
        # pass each of them through together as a mini directory list of .ezb files.
        # Allows one .ezb file from a directory of .ezb files.
        # Allows .bat batch file control.
        if directory.lower().endswith('.ezb'):
            fileList = [directory]
            directory = '.'
        else:
            fileList = sorted(os.listdir(directory))        # each directory sorted alphabetically
        fileListLen = len(fileList)
        for fileCounter in range(fileListLen):
            fileReadName = fileList[fileCounter]

            if not fileReadName.lower().endswith('.ezb'):
                continue            # skip to next file

            if fileReadName[0] == os.path.sep or fileReadName[0] == '.':
                fileReadNameFull = fileReadName
            else:
                fileReadNameFull = directory + os.path.sep + fileReadName

            # allow append to line
            print(f'\r file = {fileCounter + 1:,} of {fileListLen:,} in dir {directoryCounter + 1}' \
                + f' of {directoryListLen} = ' + directory + os.path.sep + fileReadName, end='')
            fileRead = open(fileReadNameFull, 'r')
            if fileRead.mode == 'r':

                # read line 1
                # find next non-End-Of-File non-blank non-comment line of .ezb file
                # fetch a new line
                fileLine = fileRead.readline()
                # len(fileLine): 0=EOF  1=LFonly  2=1CharacterWithLF
                fileLineSplit = fileLine.split()
                # len(fileLineSplit): 0=EOF  0=LFonly  1=1CharacterWithLF
                # ignore blank and comment lines
                # while ((not EOF) and ((LFonly) or (first char == '#'))):
                while(fileLine and ((not fileLineSplit) or (fileLineSplit[0][0] == '#'))):
                    # fetch a new line
                    fileLine = fileRead.readline()
                    fileLineSplit = fileLine.split()
                if not fileLine:                        # if end of file
                    continue                            #   skip to next file

                # process first non-blank non-comment line of .ezb file
                ## lat 40.3 long -105.1 amsl 1524.0 name stemDish1
                if fileLineSplit[0] != 'lat':           # if not a valid data file
                    continue                            #   skip to next file
                if fileLineSplit[2] != 'long':          # if not a valid data file
                    continue                            #   skip to next file
                if fileLineSplit[4] != 'amsl':          # if not a valid data file
                    continue                            #   skip to next file
                if fileLineSplit[6] != 'name':          # if not a valid data file
                    continue                            #   skip to next file
                #ezRAObsLat  = float(fileLineSplit[1])
                #ezRAObsLon  = float(fileLineSplit[3])
                #ezRAObsAmsl = float(fileLineSplit[5])
                if not ezRAObsName:
                    ezRAObsName = ' '.join(fileLineSplit[7:])


                # read line 2
                # find next non-End-Of-File non-blank non-comment line of .ezb file
                fileLine = fileRead.readline()
                fileLineSplit = fileLine.split()
                # ignore blank and comment lines
                while(fileLine and ((not fileLineSplit) or (fileLineSplit[0][0] == '#'))):
                    fileLine = fileRead.readline()
                    fileLineSplit = fileLine.split()
                if not fileLine:                        # if end of file
                    continue                            #   skip to next file

                # process second non-blank non-comment line of .ezb file
                ## freqMin 1419.2 freqMax 1421.61 freqBinQty 256
                if fileLineSplit[0] != 'freqMin':       # if not a valid data file
                    continue                            #   skip to next file
                if fileLineSplit[2] != 'freqMax':       # if not a valid data file
                    continue                            #   skip to next file
                if fileLineSplit[4] != 'freqBinQty':    # if not a valid data file
                    continue                            #   skip to next file
                #fileFreqMin    = float(fileLineSplit[1])
                #fileFreqMax    = float(fileLineSplit[3])
                #fileFreqBinQty = float(fileLineSplit[5])


                # read line 3
                # find next non-End-Of-File non-blank non-comment line of .ezb file
                fileLine = fileRead.readline()
                fileLineSplit = fileLine.split()
                # ignore blank and comment lines
                while(fileLine and ((not fileLineSplit) or (fileLineSplit[0][0] == '#'))):
                    fileLine = fileRead.readline()
                    fileLineSplit = fileLine.split()
                if not fileLine:                        # if end of file
                    continue                            #   skip to next file

                # parse third non-blank non-comment line of .ezb file, must start with 'ezbMenu:'
                ## ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  Vlsr  ...
                if fileLineSplit[0] != 'ezbMenu:':      # if not a valid data file
                    continue                            #   skip to next file

                # ezSkyInputS like '14AntBAvg'
                ezSkyInputS = ('0' + str(ezSkyInput))[-2:] + fileLineSplit[ezSkyInput + 1]

                # assume this is a valid .ezb data file
                # read data lines of this .ezb file
                # ignore blank and comment lines

                # collect as lists, later convert to more compact numpys
                raHL     = []
                decDegL  = []
                gLatDegL = []
                gLonDegL = []
                azDegL   = []
                elDegL   = []
                powerL   = []    # from selected .ezb column
                while 1:
                    # find next non-End-Of-File non-blank non-comment line of .ezb file
                    fileLine = fileRead.readline()
                    fileLineSplit = fileLine.split()
                    # ignore blank and comment lines
                    while(fileLine and ((not fileLineSplit) or (fileLineSplit[0][0] == '#'))):
                        fileLine = fileRead.readline()
                        fileLineSplit = fileLine.split()
                    if not fileLine:                        # if end of file
                        break                               #   drop out of while loop

                    raHThis = float(fileLineSplit[1]) + ezSkyAddRAH
                    if raHThis < 0.:
                        raHThis += 24.
                    elif 24. <= raHThis:
                        raHThis -= 24.
                    raHL.append(raHThis)
                    decDegL.append(float(fileLineSplit[2]) + ezSkyAddDecDeg)
                    gLatDegL.append(float(fileLineSplit[3]))
                    gLonDegL.append(float(fileLineSplit[4]))
                    azDegL.append(float(fileLineSplit[7]))
                    elDegL.append(float(fileLineSplit[8]))
                    powerL.append(float(fileLineSplit[ezSkyInput])) # from selected .ezb column

                    antLen += 1
                    
                # have processed that .ezb file
                ezbQty += 1            # current number of .ezb data files
                fileNameLast = fileReadName
                print(f'       Last sample = {antLen - 1:,}                                      ')

                # to save memory, collect lists into more more compact numpys
                raH      = np.concatenate([raH,     np.array(raHL    )])
                raHL     = []
                decDeg   = np.concatenate([decDeg,  np.array(decDegL )])
                decDegL  = []
                gLatDeg  = np.concatenate([gLatDeg, np.array(gLatDegL)])
                gLatDegL = []
                gLonDeg  = np.concatenate([gLonDeg, np.array(gLonDegL)])
                gLonDegL = []
                azDeg    = np.concatenate([azDeg, np.array(azDegL)])
                azDegL   = []
                elDeg    = np.concatenate([elDeg, np.array(elDegL)])
                elDegL   = []
                power    = np.concatenate([power,   np.array(powerL  )])    # from selected .ezb column
                powerL   = []

                #if(fileName.lower().endswith('.ezb')):
            # have processed that file

        #for fileCtr in range(fileListLen):
        # have processed that directory

    #for directoryCtr in range(directoryListLen):
    # have processed all directories

    # blank out last non-.ezb filename
    print('\r                                                                                  ')

    if ezbQty < 1:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  No .ezb data files found.')
        print()
        print()
        print()
        print()
        exit()

    print(f' Total number of valid .ezb files = {ezbQty:,}')
    print(f'\n Total samples read          = 0 through {antLen - 1:,}\n')



#A#####################################################################################



def plotPrep():
    # creates antLenM1, titleS, ezbColumnColor

    global antLen                   # integer
    global antLenM1                 # integer               create

    global ezRAObsName              # string
    global fileNameLast             # string
    global titleS                   # string                create

    global ezbColumnColor           # string list           create

    print('  plotPrep ===============')

    antLenM1 = antLen - 1

    # plot titles
    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + '           ' + ezRAObsName \
        + '          (' + programName + ')'

    #ezbColumnColor = ['green', 'green', 'green', 'green', 'green', 'green', 'green',
    #    'black', 'black', 'violet',
    #    'blue', 'blue', 'red', 'red', 'green', 'green', 'orange', 'orange', 'violet', 'violet']
    ezbColumnColor = [ \
        'green', 'green', 'green',  'green',  'green', 'green', 'green',  'black',  'black', 'violet',
        'blue',  'blue',  'violet', 'violet', 'red',   'red',   'orange', 'orange', 'green', 'green']
    #    0,       1,       2,        3,        4,       5,       6,        7,        8,       9
    


def plotEzSky1dSamplesAnt(plotName, plotData1d, plotXLabel, plotYLimL, plotColorS, plotYLabel):

    # plotName                                  # string
    # plotData1d                                # float 1d array
    # plotXLabel                                # string
    # plotYLimL                                 # list
    # plotColorS                                # string
    # plotYLabel                                # string

    global titleS                               # string
    global ezSkyDispGrid                        # integer
    global antLenM1                             # integer

    global xTickLocsAnt                         # array         create?
    global xTickLabelsAnt                       # list          create?
    global xLabelSAnt                           # string        create?

    plt.clf()

    if plotXLabel:
        # sorted data
        #plt.scatter(range(antLen), plotData1d, s=0.001, c=plotColorS)
        plt.scatter(range(antLen), plotData1d, s=1., c=plotColorS)
        plt.xlabel(plotXLabel)
    else:
        # unsorted data
        plt.plot(plotData1d, plotColorS)
        plt.xlabel(f'Sample Number (last={antLenM1:,})')

    plt.title(titleS)
    plt.grid(ezSkyDispGrid)

    if not len(xTickLocsAnt):
        xTickLocsAnt, xTickLabelsAnt = plt.xticks()
        # may remove silly values, and shorten lists, so best to process indices in decreasing order
        for i in range(len(xTickLocsAnt) - 1)[::-1]:
            xTickLocsAntIInt = int(xTickLocsAnt[i])
            if 0 <= xTickLocsAntIInt and xTickLocsAntIInt <= antLen:
                xTickLabelsAnt[i] = f'{xTickLocsAntIInt:,}'
            else:       # remove silly values
                xTickLocsAnt = np.delete(xTickLocsAnt, i)
                xTickLabelsAnt = np.delete(xTickLabelsAnt, i)
    plt.xticks(xTickLocsAnt, xTickLabelsAnt, rotation=45, ha='right', rotation_mode='anchor')
    plt.xlim(0, antLenM1)

    plt.ylabel(plotYLabel)
    if len(plotYLimL):
        plt.ylim(plotYLimL[0], plotYLimL[1])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



# ezSkyIn column plots #########################################################

def plotEzSky010raH():

    global raH                              # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 10 or 10 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky010raH.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         raHMax =', raH.max())
    print('                         raHAvg =', np.mean(raH))
    print('                         raHMin =', raH.min())

    plotEzSky1dSamplesAnt(plotName, raH, '', [0., 24.], 'green',
        'Right Ascension (hours)')



def plotEzSky020decDeg():

    global decDeg                           # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 20 or 20 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky020decDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         decDegMax =', decDeg.max())
    print('                         decDegAvg =', np.mean(decDeg))
    print('                         decDegMin =', decDeg.min())

    plotEzSky1dSamplesAnt(plotName, decDeg, '', [-90., 90.], 'green',
        'Declination (degrees)')



def plotEzSky030gLatDeg():

    global gLatDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 30 or 30 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky030gLatDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLatDegMax =', gLatDeg.max())
    print('                         gLatDegAvg =', np.mean(gLatDeg))
    print('                         gLatDegMin =', gLatDeg.min())

    plotEzSky1dSamplesAnt(plotName, gLatDeg, '', [-90., 90.], 'green',
        'Galactic Latitude (degrees)')



def plotEzSky031gLatDegSorted():

    global gLatDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global antLen                           # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 31 or 31 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky031gLatDegSorted.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLatDegMax =', gLatDeg.max())
    print('                         gLatDegAvg =', np.mean(gLatDeg))
    print('                         gLatDegMin =', gLatDeg.min())

    plotEzSky1dSamplesAnt(plotName, np.sort(gLatDeg), f'{antLen:,} Samples Sorted by Value', [-90., 90.], 'green',
        'Sorted Galactic Latitude (degrees)')



def plotEzSky032gLatDegSortedCross():

    global gLatDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global antLen                           # integer

    global ezSkyGalCrossingGLatCenter       # float
    global ezSkyGalCrossingGLatNear         # float

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 32 or 32 < ezSkyPlotRangeL[0] or ezSkyGalCrossingGLatNear == 0.:
        return(1)

    plotName = 'ezSky032gLatDegSortedCross.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLatDegMax =', gLatDeg.max())
    print('                         gLatDegAvg =', np.mean(gLatDeg))
    print('                         gLatDegMin =', gLatDeg.min())

    # set non-Galactic-Crossings to np.nan, so will not plot
    plotData1d = np.sort(gLatDeg)
    plotData1d[plotData1d < ezSkyGalCrossingGLatCenter - ezSkyGalCrossingGLatNear] = np.nan
    plotData1d[ezSkyGalCrossingGLatCenter + ezSkyGalCrossingGLatNear < plotData1d] = np.nan

    # causes xTick bug if no xTickLocsAnt yet =============================
    #plotEzSky1dSamplesAnt(plotName, plotData1d, f'{np.count_nonzero(~np.isnan(plotData1d)):,} Galactic Crossing Samples Sorted by Value', [-90., 90.], 'green',
    #    'Sorted Galactic Latitude (degrees)')
    ylabelText = f'Sorted Galactic Latitude (degrees)\nezSkyGalCrossingGLatNear = {ezSkyGalCrossingGLatNear}'
    plotEzSky1dSamplesAnt(plotName, plotData1d, f'{np.count_nonzero(~np.isnan(plotData1d)):,} Galactic Crossing Samples Sorted by Value', [-90., 90.], 'green',
        ylabelText)



def plotEzSky040gLonDeg():

    global gLonDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 40 or 40 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky040gLonDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLonDegMax =', gLonDeg.max())
    print('                         gLonDegAvg =', np.mean(gLonDeg))
    print('                         gLonDegMin =', gLonDeg.min())

    plotEzSky1dSamplesAnt(plotName, gLonDeg, '', [-180., 180.], 'green',
        'Galactic Longitude (degrees)')



def plotEzSky041gLonDegSorted():

    global gLonDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global antLen                           # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 41 or 41 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky041gLonDegSorted.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLonDegMax =', gLonDeg.max())
    print('                         gLonDegAvg =', np.mean(gLonDeg))
    print('                         gLonDegMin =', gLonDeg.min())

    #plotEzSky1dSamplesAnt(plotName, gLonDeg, '', [-180., 180.], 'green',
    #    'Galactic Longitude (degrees)')
    plotEzSky1dSamplesAnt(plotName, np.sort(gLonDeg), f'{antLen:,} Samples Sorted by Value', [-180., 180.], 'green',
        'Sorted Galactic Longitude (degrees)')



def plotEzSky043gLonDegSortedCross():

    global gLonDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global antLen                           # integer

    global ezSkyGalCrossingGLonCenter       # float
    global ezSkyGalCrossingGLonNear         # float

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 43 or 43 < ezSkyPlotRangeL[0] or ezSkyGalCrossingGLonNear == 0.:
        return(1)

    plotName = 'ezSky042gLonDegSortedCross.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLonDegMax =', gLonDeg.max())
    print('                         gLonDegAvg =', np.mean(gLonDeg))
    print('                         gLonDegMin =', gLonDeg.min())

    # set non-Galactic-Crossings to np.nan, so will not plot
    plotData1d = np.sort(gLonDeg)
    plotData1d[plotData1d < ezSkyGalCrossingGLonCenter - ezSkyGalCrossingGLonNear] = np.nan
    plotData1d[ezSkyGalCrossingGLonCenter + ezSkyGalCrossingGLonNear < plotData1d] = np.nan

    # causes xTick bug if no xTickLocsAnt yet =============================
    #plotEzSky1dSamplesAnt(plotName, plotData1d, f'{np.count_nonzero(~np.isnan(plotData1d)):,} Galactic Crossing Samples Sorted by Value', [-90., 90.], 'green',
    #    'Sorted Galactic Longitude (degrees)')
    ylabelText = f'Sorted Galactic Longitude (degrees)\nezSkyGalCrossingGLonNear = {ezSkyGalCrossingGLonNear}'
    plotEzSky1dSamplesAnt(plotName, plotData1d, f'{np.count_nonzero(~np.isnan(plotData1d)):,} Galactic Crossing Samples Sorted by Value', [-90., 90.], 'green',
        ylabelText)



def plotEzSky070azDeg():

    global azDeg                            # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 70 or 70 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky070azDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         azDegMax =', azDeg.max())
    print('                         azDegAvg =', np.mean(azDeg))
    print('                         azDegMin =', azDeg.min())

    plotEzSky1dSamplesAnt(plotName, azDeg, '', [0., 360.], 'green',
        'Azimuth (degrees)')



def plotEzSky080elDeg():

    global elDeg                            # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 80 or 80 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky080elDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         elDegMax =', elDeg.max())
    print('                         elDegAvg =', np.mean(elDeg))
    print('                         elDegMin =', elDeg.min())

    plotEzSky1dSamplesAnt(plotName, elDeg, '', [-95., 195.], 'green',
        'Elevation (degrees)')



def plotEzSky100input():

    global power                            # float 1d array
    global ezSkyInputS                      # string

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 100 or 100 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky100input_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print(f'                         {ezSkyInputS[2:]}Max = {power.max()}')
    print(f'                         {ezSkyInputS[2:]}Avg = {np.mean(power)}')
    print(f'                         {ezSkyInputS[2:]}Min = {power.min()}')

    #plotEzSky1dSamplesAnt(plotName, power, '', [], 'green', ezSkyInputS[2:])
    plotEzSky1dSamplesAnt(plotName, power, '', [], ezbColumnColor[ezSkyInput], ezSkyInputS[2:])



def ezSkyGridRadec():
    # using raH, decDeg, and power,
    #   fill radecPower, create radecCount, raHalfDeg, decHalfDeg

    global raH                      # float 1d array, from .ezb files
    global decDeg                   # float 1d array, from .ezb files
    global power                    # float 1d array, from .ezb files

    global radecCount               # float   1d array                          fill
    global radecPower               # float   1d array                          create
    global raHalfDeg                # integer 1d array                          create
    global decHalfDeg               # integer 1d array                          create

    #global ezSkyPlotRangeL          # integer list

    ## if Radec grid not needed, then return
    #if ezSkyPlotRangeL[1] < 200 or 405 < ezSkyPlotRangeL[0]:
    #    return(1)

    print()
    print('  ezSkyGridRadec ================================')

    # integrate .ezb file data into grids,
    #   gridRadecCount and gridRadecPower for RaDec map    (in half-degree grid)
    gridRadecRaHalfDegRange = 360 + 360 + 1                 # Ra=0    thru 360 degrees, or 0 thru 720 halfdeg
    gridRadecDecHalfDegRange = 90 + 90 + 90 + 90 + 1        # Dec=-90 thru Lat=+90 deg, or 0 thru 360 halfdeg
    gridRadecCount = np.zeros([gridRadecRaHalfDegRange, gridRadecDecHalfDegRange], dtype = int)
    gridRadecPower = np.zeros([gridRadecRaHalfDegRange, gridRadecDecHalfDegRange], dtype = float)

    # account for grid's 0.5 degree per index
    for i in range(antLen):
        # One raH hour is 15 degrees.
        # One raH hour is 30 halfDegrees.
        raHalfDeg = int(raH[i] * 30.)                       # integer halfDegree
        # raHalfDeg wraps around, use raHalfDeg=0
        if 720 <= raHalfDeg:
            raHalfDeg -= 720
        decHalfDeg = int(decDeg[i] + decDeg[i] + 180.)      # integer halfDegree with offset
        gridRadecCount[raHalfDeg, decHalfDeg] += 1          # count     of gridBox
        gridRadecPower[raHalfDeg, decHalfDeg] += power[i]   # power sum of gridBox

    # raHalfDeg wraps around, copy raHalfDeg=0 to raHalfDeg=720
    gridRadecCount[720, :] = gridRadecCount[0, :]
    gridRadecPower[720, :] = gridRadecPower[0, :]

    #raH    = []         # free memory
    #decDeg = []         # free memory

    # unravel grids and collect as lists, and later convert to more compact numpys
    radecCountL = []
    radecPowerL = []
    raHalfDegL  = []
    decHalfDegL = []
    for decHalfDeg in range(gridRadecDecHalfDegRange):
        for raHalfDeg in range(gridRadecRaHalfDegRange):
            if gridRadecCount[raHalfDeg, decHalfDeg]:
                radecCountL.append(gridRadecCount[raHalfDeg, decHalfDeg])
                # calculate average power
                radecPowerL.append(gridRadecPower[raHalfDeg, decHalfDeg] \
                    / gridRadecCount[raHalfDeg, decHalfDeg]) 
                raHalfDegL.append(raHalfDeg)
                decHalfDegL.append(decHalfDeg)

    gridRadecCount = []     # free memory
    gridRadecPower = []     # free memory

    # create compact numpys from lists
    radecCount  = np.array(radecCountL)
    radecCountL = []                        # free memory
    radecPower  = np.array(radecPowerL)
    radecPowerL = []                        # free memory
    raHalfDeg   = np.array(raHalfDegL)
    raHalfDegL  = []                        # free memory
    decHalfDeg  = np.array(decHalfDegL)
    decHalfDegL = []                        # free memory

    print(f'                         len(radecPower) = {len(radecPower):,}')



def ezSkyGridRadecBox():
    # using raH, decDeg, power, and ezSkyXYLimL,
    #   fill radecPowerBox, create radecCountBox, radecRaBox, radecDecBox,  
    #   raDegPerBox, decDegPerBox, raDegMinMaxL, and decDegMinMaxL

    global raH                      # float 1d array, from .ezb files
    global decDeg                   # float 1d array, from .ezb files
    global power                    # float 1d array, from .ezb files
    global ezSkyXYLimL              # list of floats

    global radecCountBox            # float   1d array                          fill
    global radecPowerBox            # float   1d array                          create
    global radecRaBox               # integer 1d array                          create
    global radecDecBox              # integer 1d array                          create
    global raDegPerBox              # float                                     create
    global decDegPerBox             # float                                     create
    global raDegMinMaxL             # list of floats                            create
    global decDegMinMaxL            # list of floats                            create

    print()
    print('  ezSkyGridRadecBox ================================')

    # define the 721 by 361 grid boxes

    # create min(xData)
    raHMin = raH.min()
    raDegMin = raHMin * 15.
    print('                         raDegMin   =', raDegMin, '        raHMin    =', raHMin)

    # create max(xData)
    raHMax = raH.max()
    raDegMax = raHMax * 15.
    if raDegMin == raDegMax:
        raDegMax += 1e-8        # to avoid division by a zero raDegPerBox
    print('                         raDegMax   =', raDegMax, '        raHMax    =', raHMax)

    # create min(yData)
    decDegMin = decDeg.min()
    print('                         decDegMin  =', decDegMin)

    # create max(yData)
    decDegMax = decDeg.max()
    if decDegMin == decDegMax:
        decDegMax += 1e-8       # to avoid division by a zero decDegPerBox
    print('                         decDegMax  =', decDegMax)

    print()
    print('                         ezSkyXYLimL        =', ezSkyXYLimL)
    # ezSkyXYLimL is [xPerBox, yPerBox, xMin, xMax, yMin, yMax]
    #                 0        1        2     3     4     5

    # create raDegPerBox and raDegMinMaxL[:1]
    raDegMinMaxL = [999., 999.]                                 # silly values
    if 0. < ezSkyXYLimL[0] and ezSkyXYLimL[0] <= 360.:          # if xPerBox not silly
        raDegPerBox = ezSkyXYLimL[0]                            # use xPerBox
        if 0. <= ezSkyXYLimL[2] and ezSkyXYLimL[2] <= 360.:     # if xMin not silly
            raDegMinMaxL[0] = ezSkyXYLimL[2]                    # use xMin
        else:
            raDegMinMaxL[0] = raDegMin                          # use min(xData)

        if 0. <= ezSkyXYLimL[3] and ezSkyXYLimL[3] <= 360.:     # if xMax not silly
            raDegMinMaxL[1] = ezSkyXYLimL[3]                    # use xMax
        else:
            # use min(max(xData), xMax that xPerBox will allow)
            raDegMinMaxL[1] = min(raDegMax, raDegMinMaxL[0] + 720. * ezSkyXYLimL[0], 360.)

    else:                                                       # xPerBox is silly, create xPerBox
        if 0. <= ezSkyXYLimL[2] and ezSkyXYLimL[2] <= 360.:     # if xMin not silly
            raDegMinMaxL[0] = ezSkyXYLimL[2]                    # use xMin
        else:
            raDegMinMaxL[0] = raDegMin                          # use min(xData)

        if 0. <= ezSkyXYLimL[3] and ezSkyXYLimL[3] <= 360.:     # if xMax not silly
            raDegMinMaxL[1] = ezSkyXYLimL[3]                    # use xMax
        else:
            raDegMinMaxL[1] = raDegMax                          # use max(xData)
        #  create xPerBox
        raDegPerBox = (raDegMinMaxL[1] - raDegMinMaxL[0]) / 720.
    print()
    print('                         raDegPerBox        =', raDegPerBox)
    print('                         raDegMinMaxL       =', raDegMinMaxL)

    # create decDegPerBox and decDegMinMaxL[:1]
    decDegMinMaxL = [999., 999.]                                # silly values
    if 0. < ezSkyXYLimL[1] and ezSkyXYLimL[1] <= 180.:          # if yPerBox not silly
        decDegPerBox = ezSkyXYLimL[1]                           # use yPerBox
        if -90. <= ezSkyXYLimL[4] and ezSkyXYLimL[4] <= 90.:    # if yMin not silly
            decDegMinMaxL[0] = ezSkyXYLimL[4]                   # use yMin
        else:
            decDegMinMaxL[0] = decDegMin                        # use min(yData)

        if -90. <= ezSkyXYLimL[5] and ezSkyXYLimL[5] <= 90.:    # if yMax not silly
            decDegMinMaxL[1] = ezSkyXYLimL[5]                   # use yMax
        else:
            # use min(max(yData), yMax that yPerBox will allow)
            decDegMinMaxL[1] = min(decDegMax, decDegMinMaxL[0] + 360. * ezSkyXYLimL[1], 180.)

    else:                                                       # yPerBox is silly, create yPerBox
        if -90. <= ezSkyXYLimL[4] and ezSkyXYLimL[4] <= 90.:    # if yMin not silly
            decDegMinMaxL[0] = ezSkyXYLimL[4]                   # use yMin
        else:
            decDegMinMaxL[0] = decDegMin                        # use min(yData)

        if -90. <= ezSkyXYLimL[5] and ezSkyXYLimL[5] <= 90.:    # if yMax not silly
            decDegMinMaxL[1] = ezSkyXYLimL[5]                   # use yMax
        else:
            decDegMinMaxL[1] = decDegMax                        # use max(yData)
        #  create yPerBox
        decDegPerBox = (decDegMinMaxL[1] - decDegMinMaxL[0]) / 360.
    print('                         decDegPerBox       =', decDegPerBox)
    print('                         decDegMinMaxL      =', decDegMinMaxL)

    # integrate .ezb file data into grids,
    #   gridRadecCount and gridRadecPower for RaDec map
    gridRadecRaBoxRange  = 360 + 360 + 2            # Ra=  0 thru 720
    gridRadecDecBoxRange = 90 + 90 + 90 + 90 + 2    # Dec= 0 thru 360
    gridRadecCount = np.zeros([gridRadecRaBoxRange, gridRadecDecBoxRange], dtype = int)
    gridRadecPower = np.zeros([gridRadecRaBoxRange, gridRadecDecBoxRange], dtype = float)

    # account for grid's raDegPerBox and decDegPerBox
    for i in range(antLen):
        raDegThis = raH[i] * 15.
        if raDegThis <= raDegMinMaxL[1]:
            raBox  = int(0.5 * (raDegThis - raDegMinMaxL[0])  / raDegPerBox + 0.5)          # integer raBox
            decDegThis = decDeg[i]
            if decDegThis <= decDegMinMaxL[1]:
                decBox = int(0.5 * (decDegThis - decDegMinMaxL[0]) / decDegPerBox + 0.5)    # integer decBox
                #print('======= raBox  =', raBox)
                #print('======= decBox =', decBox)
                if 0 <= raBox and raBox <= 720 and 0 <= decBox and decBox <= 180:   # if inside canvas
                    gridRadecCount[raBox, decBox] += 1                              # count     of gridBox
                    gridRadecPower[raBox, decBox] += power[i]                       # power sum of gridBox


    # unravel grids and collect as lists, and later convert to more compact numpys
    radecCountBoxL = []
    radecPowerBoxL = []
    radecRaBoxL    = []
    radecDecBoxL   = []
    for y in range(gridRadecDecBoxRange):
        for x in range(gridRadecRaBoxRange):
            if gridRadecCount[x, y]:
                radecCountBoxL.append(gridRadecCount[x, y])
                # calculate average power
                radecPowerBoxL.append(gridRadecPower[x, y] \
                    / gridRadecCount[x, y]) 
                radecRaBoxL.append(x)
                radecDecBoxL.append(y)

    gridRadecCount = []     # free memory
    gridRadecPower = []     # free memory

    # create compact numpys from lists
    radecCountBox  = np.array(radecCountBoxL)
    radecCountBoxL = []    # free memory
    radecPowerBox  = np.array(radecPowerBoxL)
    radecPowerBoxL = []    # free memory
    radecRaBox     = np.array(radecRaBoxL)
    radecRaBoxL    = []    # free memory
    radecDecBox    = np.array(radecDecBoxL)
    radecDecBoxL   = []    # free memory



def plotEzSky200RBVO():
    # radio Sky Radec map with Background, power Vertical Offset

    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezbColumnColor           # string list
    global ezSkyInputS              # string
    global ezSkyVOGain              # float

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 200 or 200 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky200RBVO_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot RaDec background
    backImg = plt.imread(ezSkyBackground1)    # Reeve map

    imgaxes = fig.add_axes(ax.get_position(), label='image', xticks=[], yticks=[])
    #print(ax.get_position())

    imgaxes.set_xlim(0, ezSkyBackground1XMax)
    imgaxes.set_ylim(0, ezSkyBackground1YMax)

    plt.gca().invert_yaxis()

    # comment next line to remove background
    img = imgaxes.imshow(backImg, aspect='auto')

    ax.set_axis_off()

    # map radec to background image
    imgaxesRatioX = ezSkyBackground1XMax / 720
    imgaxesRatioY = ezSkyBackground1YMax / 360
    raHalfDegScaled  = (720 - raHalfDeg ) * imgaxesRatioX
    decHalfDegScaled = (360 - decHalfDeg) * imgaxesRatioY

    # thin horizontal line on each used scaled declination
    decHalfDegScaledLast = 9999      # silly value
    for y in decHalfDegScaled:
        if decHalfDegScaledLast != y:
            decHalfDegScaledLast = y
            plt.axhline(y=decHalfDegScaledLast, linewidth=0.5, c=ezbColumnColor[ezSkyInput])

    # calculate signal gain
    radecPowerMax = radecPower.max()
    print('                         radecPowerMax =', radecPowerMax)
    radecPowerAvg = np.mean(radecPower)
    print('                         radecPowerAvg =', radecPowerAvg)
    radecPowerMin = radecPower.min()
    print('                         radecPowerMin =', radecPowerMin)
    if radecPowerMax == radecPowerMin:
        radecPowerGain = 0.
    elif radecPowerAvg - radecPowerMin < radecPowerMax - radecPowerAvg:
        # gain determined from span above average
        radecPowerGain = ezSkyVOGain / (radecPowerMax  - radecPowerAvg)
    else:
        # gain determined from span below average
        radecPowerGain = ezSkyVOGain / (radecPowerAvg - radecPowerMin)









    print('                                            radecPowerGain =', radecPowerGain)








    # plot each radecPower value as a dot with a radecPowerScaled offset from its scaled declination
    radecPowerScaled = radecPowerGain * (radecPowerAvg - radecPower)
    plt.scatter(raHalfDegScaled, decHalfDegScaled + radecPowerScaled, s=1, marker='.',
        c=ezbColumnColor[ezSkyInput])

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xticks([i * imgaxesRatioX for i in range(720, -1, -60)],
        ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])

    plt.ylabel(f'{ezSkyInputS[2:]} Vertical Offset in RaDec Coordinates')
    plt.yticks([i * imgaxesRatioY for i in range(360, -1, -30)],
        ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])
    imgaxes.tick_params(axis='both', labelsize=6)

    plt.subplots_adjust(left=0.4, right=0.5, bottom=0.4, top=0.5)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky201RBMax():
    # radio Sky Radec map with Background, dots on left and right maximum power

    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezbColumnColor           # string list
    global ezSkyInputS              # string
    global ezSkyVOGain              # float

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 201 or 201 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky201RBMax_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot RaDec background
    backImg = plt.imread(ezSkyBackground1)    # Reeve map

    imgaxes = fig.add_axes(ax.get_position(), label='image', xticks=[], yticks=[])
    #print(ax.get_position())

    imgaxes.set_xlim(0, ezSkyBackground1XMax)
    imgaxes.set_ylim(0, ezSkyBackground1YMax)

    plt.gca().invert_yaxis()

    # comment next line to remove background
    img = imgaxes.imshow(backImg, aspect='auto')

    ax.set_axis_off()

    # map radec to background image
    imgaxesRatioX = ezSkyBackground1XMax / 720
    imgaxesRatioY = ezSkyBackground1YMax / 360
    raHalfDegScaled  = (720 - raHalfDeg ) * imgaxesRatioX
    decHalfDegScaled = (360 - decHalfDeg) * imgaxesRatioY

    # galRaHDegLeft054304[] has RaHDeg halfDeg data for Left side of Galactic Plane, for 54 through 304 decHalfDeg
    #365,370,420,428,432,435,
    galRaHDegLeft054304 = np.array([ \
    400,412,420,428,432,435,
    443,446,450,453,456,460,463,466,468,469,
    471,474,477,479,481,482,484,485,486,489,
    491,492,493,495,496,497,499,500,501,503,
    504,505,507,508,509,510,511,512,513,514,
    515,516,516,517,518,519,520,521,522,522,
    523,524,525,526,526,527,528,529,530,530,
    531,532,532,533,534,535,535,536,537,537,
    538,538,539,540,540,541,541,542,542,543,
    543,544,545,545,546,546,547,547,548,549,
    549,550,550,551,551,552,552,553,554,555,
    555,556,556,557,558,558,559,559,560,561,
    561,562,562,563,563,563,564,564,564,565,
    566,566,567,567,568,568,569,570,570,571,
    571,572,572,573,573,574,574,574,575,575,
    576,577,577,578,578,579,579,580,580,581,
    581,582,583,583,584,584,585,585,586,587,
    587,588,588,589,590,590,591,592,593,593,
    594,595,595,596,596,597,598,598,599,600,
    601,602,602,603,604,605,605,606,607,608,
    609,610,610,611,612,613,614,614,615,616,
    617,618,619,621,622,622,624,625,626,627,
    628,630,632,633,634,636,637,638,640,641,
    642,644,647,648,649,652,654,657,659,660,
    662,665,668,671,675,678,681,685,688,692,
    696,703,707,715])
    #print('          len(galRaHDegLeft054304)  =', len(galRaHDegLeft054304))    # 250

    # galRaHDegRight054304[] has RaHDeg halfDeg data for Right side of Galactic Plane, for 54 through 304 decHalfDeg
    galRaHDegRight054304 = np.array([ \
    363,355,347,343,336,332,
    328,325,321,318,315,311,308,305,302,300,
    299,297,294,292,289,288,287,284,283,282,
    280,278,277,276,273,272,271,270,269,268,
    266,265,264,263,262,261,260,259,258,257,
    256,254,253,253,252,251,250,249,249,248,
    247,246,246,245,244,243,242,242,241,241,
    240,239,238,237,236,236,235,235,234,234,
    233,232,231,230,230,229,229,228,228,227,
    226,225,225,224,224,223,223,222,221,221,
    220,220,219,219,218,218,217,216,216,215,
    215,214,214,213,213,213,212,212,211,210,
    209,209,208,208,207,207,206,206,205,204,
    204,203,203,203,203,202,202,201,201,200,
    200,199,199,198,197,197,196,196,195,195,
    194,193,193,192,192,191,191,190,190,189,
    188,188,187,187,186,186,185,184,183,183,
    183,182,182,181,180,180,179,179,178,178,
    177,176,176,175,175,174,173,172,171,170,
    170,169,168,167,166,166,165,165,164,163,
    162,161,160,159,159,158,157,156,155,154,
    153,152,151,150,149,148,147,145,144,143,
    142,141,139,137,136,135,133,132,131,129,
    127,126,124,122,120,119,117,114,111,109,
    108,106,103,100, 96, 93, 90, 86, 83, 75,
    72,  68, 60, 52])
    #72,  68, 60,  0]
    #print('          len(galRaHDegRight054304) =', len(galRaHDegRight054304))   # 250

    galRaHDegRight054304Scaled  = (720 - galRaHDegRight054304) * imgaxesRatioX
    galRaHDegLeft054304Scaled  = (720 - galRaHDegLeft054304) * imgaxesRatioX
    decHDegScaled = (360 - np.array(range(54,304))) * imgaxesRatioY

    plt.scatter(galRaHDegRight054304Scaled, decHDegScaled, s=100, marker='.', c='red')
    plt.scatter(galRaHDegLeft054304Scaled, decHDegScaled, s=100, marker='.', c='red')


    # For each declination, find and plot dots on MaxRight and on MaxLeft data indexes
    decHalfDegLast = -9999                     # silly low value
    nMaxRight = -1                                  # silly value
    nMaxLeft  = -1                                  # silly value
    radecPowerMaxRight = -9999                      # silly low value
    radecPowerMaxLeft  = -9999                      # silly low value
    # walk through data, already sorted as increasing RaH then increasing Dec 
    for n in range(len(decHalfDegScaled)):
        #print(f'          n = {n}',
        #    f'  decHalfDeg = {decHalfDeg[n]}',
        #    f'  raHalfDeg = {raHalfDeg[n]}',
        #    f'  radecPower[n] = {radecPower[n]}',
        #    f'  radecPowerMaxRight = {radecPowerMaxRight}',
        #    f'  nMaxRight = {nMaxRight}')

        #if decHalfDegLast != decHalfDeg[n]:   # if new Dec
        # if definately new Dec (allow for ezConAstroMath=2 calculation noise of 1 HalfDeg)
        if decHalfDegLast + 1 < decHalfDeg[n]:
            decHalfDegLast = decHalfDeg[n]
            #print(f'       decHalfDeg jumped')
            if nMaxRight + 1:                       # if not silly value, plot MaxRight
                # if have Galactic plane galRaHDegRight054304 data for this declination
                if 54 <= decHalfDeg[nMaxRight] and decHalfDeg[nMaxRight] < 304:
                    # Right Ascension (hours) difference from Galactic Plane data
                    #print(f'\n          nMaxRight at decHalfDeg = {decHalfDeg[nMaxRight]}',
                    #    f'  raHalfDeg = {raHalfDeg[nMaxRight]}')
                    # print the offset, of nMaxRight vs Right side of Galactic Plane
                    # galRaHDegRight054304[] has RaHDeg halfDeg data for Right side of Galactic Plane,
                    #   for only 54 through 304 decHalfDeg
                    # (30 halfDeg per Right Ascension hour)
                    #print('============== nMaxRight =', nMaxRight)
                    #print('============== raHalfDeg[nMaxRight] =', raHalfDeg[nMaxRight])
                    #print('============== decHalfDeg[nMaxRight] =', decHalfDeg[nMaxRight])
                    #print('============== galRaHDegRight054304[decHalfDeg[nMaxRight] - 54] =', galRaHDegRight054304[decHalfDeg[nMaxRight] - 54])
                    raHDiff = (raHalfDeg[nMaxRight] \
                        - galRaHDegRight054304[decHalfDeg[nMaxRight] - 54]) / 30.
                    print(f'\n          DecDeg = {decHalfDeg[nMaxRight] / 2. - 90.}',
                        f'  RaH = {raHalfDeg[nMaxRight] / 30.:.1f}        Right raHDiff = {raHDiff:.1f}')

                plt.scatter(raHalfDegScaled[nMaxRight], decHalfDegScaled[nMaxRight],
                    s=100, marker='.', c='green')
                nMaxRight = -1                      # reset to silly value
            radecPowerMaxRight = -9999              # reset to silly low value

            if nMaxLeft + 1:                        # if not silly value, plot MaxLeft
                # if have Galactic plane galRaHDegLeft054304 data for this declination
                if 54 <= decHalfDeg[nMaxLeft] and decHalfDeg[nMaxLeft] < 304:
                    # Right Ascension (hours) difference from Galactic Plane data
                    #print(f'\n          nMaxLeft  at decHalfDeg = {decHalfDeg[nMaxLeft]}',
                    #    f'  raHalfDeg = {raHalfDeg[nMaxLeft]}')
                    # print the offset, of nMaxLeft vs Left side of Galactic Plane
                    # galRaHDegLeft054304[] has RaHDeg halfDeg data for Left side of Galactic Plane,
                    #   for only 54 through 304 decHalfDeg
                    # (30 halfDeg per Right Ascension hour)
                    raHDiff = (raHalfDeg[nMaxLeft] \
                        - galRaHDegLeft054304[decHalfDeg[nMaxLeft] - 54]) / 30.
                    print(f'          DecDeg = {decHalfDeg[nMaxLeft] / 2. - 90.}',
                        f'  RaH = {raHalfDeg[nMaxLeft] / 30.:.1f}    Left raHDiff = {raHDiff:.1f}')

                plt.scatter(raHalfDegScaled[nMaxLeft], decHalfDegScaled[nMaxLeft],
                    s=100, marker='.', c='green')
                nMaxLeft = -1                       # reset to silly value
            radecPowerMaxLeft = -9999               # reset to silly low value

            #print()
            #print(f'                 {n}:{nMaxLeft}:{nMaxRight}')
            #print(f'                 {decHalfDeg[nMaxLeft]}:{decHalfDeg[nMaxRight]}:')
            #print(f'{raHalfDeg[nMaxLeft]},{raHalfDeg[nMaxRight]},')

        if raHalfDeg[n] < 360:
            # on right half of RaDec
            if radecPowerMaxRight < radecPower[n]:  # if found the new maxRight
                radecPowerMaxRight = radecPower[n]
                nMaxRight = n
        else:
            # on left half of RaDec
            if radecPowerMaxLeft < radecPower[n]:   # if found the new maxLeft
                radecPowerMaxLeft = radecPower[n]
                nMaxLeft = n

    # loop completed, but maybe plot nMaxRight or MaxLeft

    if nMaxRight + 1:                               # if not silly value, plot MaxRight
        # if have Galactic plane galRaHDegRight054304 data for this declination
        if 54 <= decHalfDeg[nMaxRight] and decHalfDeg[nMaxRight] <= 304:
            # Right Ascension (hours) difference from Galactic Plane data
            #print(f'\n          nMaxRight at decHalfDeg = {decHalfDeg[nMaxRight]}',
            #    f'  raHalfDeg = {raHalfDeg[nMaxRight]}')
            raHDiff = (raHalfDeg[nMaxRight] \
                - galRaHDegRight054304[decHalfDeg[nMaxRight] - 54]) / 30.
            #print(f'\n          decHalfDeg = {decHalfDeg[nMaxRight]}',
            #    f'  raHalfDeg = {raHalfDeg[nMaxRight]}')
            print(f'\n          DecDeg = {decHalfDeg[nMaxRight] / 2. - 90.}',
                f'  RaH = {raHalfDeg[nMaxRight] / 30.:.1f}        Right raHDiff = {raHDiff:.1f}')

        plt.scatter(raHalfDegScaled[nMaxRight], decHalfDegScaled[nMaxRight],
            s=100, marker='.', c='green')

    if nMaxLeft + 1:                               # if not silly value, plot MaxLeft
        # if have Galactic plane galRaHDegLeft054304 data for this declination
        if 54 <= decHalfDeg[nMaxLeft] and decHalfDeg[nMaxLeft] <= 304:
            # Right Ascension (hours) difference from Galactic Plane data
            #print(f'\n          nMaxLeft  at decHalfDeg = {decHalfDeg[nMaxRight]}',
            #    f'  raHalfDeg = {raHalfDeg[nMaxRight]}')
            raHDiff = (raHalfDeg[nMaxLeft] \
                - galRaHDegLeft054304[decHalfDeg[nMaxLeft] - 54]) / 30.
            #print(f'\n          decHalfDeg = {decHalfDeg[nMaxRight]}',
            #    f'  raHalfDeg = {raHalfDeg[nMaxRight]}')
            print(f'          DecDeg = {decHalfDeg[nMaxLeft] / 2. - 90.}',
                f'  RaH = {raHalfDeg[nMaxLeft] / 30.:.1f}    Left raHDiff = {raHDiff:.1f}')

        plt.scatter(raHalfDegScaled[nMaxLeft], decHalfDegScaled[nMaxLeft],
            s=100, marker='.', c='green')


    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xticks([i * imgaxesRatioX for i in range(720, -1, -60)],
        ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])

    plt.ylabel(f'{ezSkyInputS[2:]} Local Maximum in RaDec Coordinates')
    plt.yticks([i * imgaxesRatioY for i in range(360, -1, -30)],
        ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])
    imgaxes.tick_params(axis='both', labelsize=6)

    plt.subplots_adjust(left=0.4, right=0.5, bottom=0.4, top=0.5)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky300RB():
    # radio Sky Radec map with Background, power color

    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 300 or 300 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky300RB_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot RaDec background
    backImg = plt.imread(ezSkyBackground1)    # Reeve map

    imgaxes = fig.add_axes(ax.get_position(), label='image', xticks=[], yticks=[])
    #print(ax.get_position())

    imgaxes.set_xlim(0, ezSkyBackground1XMax)
    imgaxes.set_ylim(0, ezSkyBackground1YMax)

    plt.gca().invert_yaxis()

    # comment next line to remove background
    img = imgaxes.imshow(backImg, aspect='auto')

    ax.set_axis_off()

    # map radec to background image
    imgaxesRatioX = ezSkyBackground1XMax / 720
    imgaxesRatioY = ezSkyBackground1YMax / 360
    raHalfDegScaled  = (720 - raHalfDeg ) * imgaxesRatioX
    decHalfDegScaled = (360 - decHalfDeg) * imgaxesRatioY

    # plot each radecPower value as a dot with a radecPower color
    pts = plt.scatter(raHalfDegScaled, decHalfDegScaled, s=1, marker='|',
        c=radecPower, cmap=plt.get_cmap('gnuplot'))

    cbar = plt.colorbar(pts, orientation='horizontal', shrink=0.3, pad=0.06)
    cbar.ax.tick_params(labelsize=6)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xticks([i * imgaxesRatioX for i in range(720, -1, -60)],
        ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])

    plt.ylabel(f'{ezSkyInputS[2:]} Color in RaDec Coordinates')
    plt.yticks([i * imgaxesRatioY for i in range(360, -1, -30)],
        ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])
    imgaxes.tick_params(axis='both', labelsize=6)

    plt.subplots_adjust(left=0.4, right=0.5, bottom=0.4, top=0.5)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky301RBT():
    # radio Sky Radec map with Background, power color Tall
    
    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezSkyInputS              # string
    global ezSkyHalfTallDec         # integer

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 301 or 301 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky301RBT_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot RaDec background
    backImg = plt.imread(ezSkyBackground1)    # Reeve map

    imgaxes = fig.add_axes(ax.get_position(), label='image', xticks=[], yticks=[])
    #print(ax.get_position())

    imgaxes.set_xlim(0, ezSkyBackground1XMax)
    imgaxes.set_ylim(0, ezSkyBackground1YMax)

    plt.gca().invert_yaxis()

    # comment next line to remove background
    img = imgaxes.imshow(backImg, aspect='auto')

    ax.set_axis_off()

    # map radec to background image
    imgaxesRatioX = ezSkyBackground1XMax / 720
    imgaxesRatioY = ezSkyBackground1YMax / 360
    raHalfDegScaled  = (720 - raHalfDeg ) * imgaxesRatioX
    decHalfDegScaled = (360 - decHalfDeg) * imgaxesRatioY

    #    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    #    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
    #        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
    #        # plot each radecPower value as a dot with a radecPower color
    #        pts = plt.scatter(raHalfDegScaled, decHalfDegScaled-reachTallDecHalfDegScaled,
    #            s=1, marker='|', c=radecPower, cmap=plt.get_cmap('gnuplot'))
    #        pts = plt.scatter(raHalfDegScaled, decHalfDegScaled+reachTallDecHalfDegScaled,
    #            s=1, marker='|', c=radecPower, cmap=plt.get_cmap('gnuplot'))
    #        cbar2 = plt.colorbar(pts, orientation='horizontal', shrink=0.3, pad=0.06)
    #    # plot center, without offset
    #    pts = plt.scatter(raHalfDegScaled, decHalfDegScaled,
    #        s=1, marker='|', c=radecPower, cmap=plt.get_cmap('gnuplot'))

    # plot center, without offset
    raHalfDegScaledAll = raHalfDegScaled + 0.
    decHalfDegScaledAll = decHalfDegScaled + 0.
    radecPowerAll = radecPower + 0.
    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
        # plot each radecPower value as a dot with a radecPower color
        raHalfDegScaledAll = np.concatenate([raHalfDegScaledAll,
            raHalfDegScaled, raHalfDegScaled])
        decHalfDegScaledAll = np.concatenate([decHalfDegScaledAll,
            decHalfDegScaled-reachTallDecHalfDegScaled,
            decHalfDegScaled+reachTallDecHalfDegScaled])
        radecPowerAll = np.concatenate([radecPowerAll,
            radecPower, radecPower])
    # plot center, without offset
    pts = plt.scatter(raHalfDegScaledAll, decHalfDegScaledAll,
        s=1, marker='|', c=radecPowerAll, cmap=plt.get_cmap('gnuplot'))
    # free memory
    raHalfDegScaledAll  = []
    decHalfDegScaledAll = []
    radecPowerAll       = []

    cbar = plt.colorbar(pts, orientation='horizontal', shrink=0.3, pad=0.06)
    cbar.ax.tick_params(labelsize=6)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xticks([i * imgaxesRatioX for i in range(720, -1, -60)],
        ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])

    plt.ylabel(f'{ezSkyInputS[2:]} Color Tall in RaDec Coordinates')
    plt.yticks([i * imgaxesRatioY for i in range(360, -1, -30)],
        ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])
    imgaxes.tick_params(axis='both', labelsize=6)

    plt.subplots_adjust(left=0.4, right=0.5, bottom=0.4, top=0.5)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky309RBTC():
    # radio Sky Radec map with Background, Count Tall

    global radecCount               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezSkyHalfTallDec         # integer

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 309 or 309 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky309RBTC.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot RaDec background
    backImg = plt.imread(ezSkyBackground1)    # Reeve map

    imgaxes = fig.add_axes(ax.get_position(), label='image', xticks=[], yticks=[])
    #print(ax.get_position())

    imgaxes.set_xlim(0, ezSkyBackground1XMax)
    imgaxes.set_ylim(0, ezSkyBackground1YMax)

    plt.gca().invert_yaxis()

    # comment next line to remove background
    img = imgaxes.imshow(backImg, aspect='auto')

    ax.set_axis_off()

    # map radec to background image
    imgaxesRatioX = ezSkyBackground1XMax / 720
    imgaxesRatioY = ezSkyBackground1YMax / 360
    raHalfDegScaled  = (720 - raHalfDeg ) * imgaxesRatioX
    decHalfDegScaled = (360 - decHalfDeg) * imgaxesRatioY

    # plot center, without offset
    raHalfDegScaledAll = raHalfDegScaled + 0.
    decHalfDegScaledAll = decHalfDegScaled + 0.
    radecCountAll = radecCount + 0.
    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
        # plot each radecPower value as a dot with a radecPower color
        raHalfDegScaledAll = np.concatenate([raHalfDegScaledAll,
            raHalfDegScaled, raHalfDegScaled])
        decHalfDegScaledAll = np.concatenate([decHalfDegScaledAll,
            decHalfDegScaled-reachTallDecHalfDegScaled,
            decHalfDegScaled+reachTallDecHalfDegScaled])
        radecCountAll = np.concatenate([radecCountAll,
            radecCount, radecCount])
    # plot center, without offset
    pts = plt.scatter(raHalfDegScaledAll, decHalfDegScaledAll,
        s=1, marker='|', c=radecCountAll, cmap=plt.get_cmap('gnuplot'))
    # free memory
    raHalfDegScaledAll  = []
    decHalfDegScaledAll = []
    radecCountAll       = []

    cbar = plt.colorbar(pts, orientation='horizontal', shrink=0.3, pad=0.06)
    cbar.ax.tick_params(labelsize=6)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xticks([i * imgaxesRatioX for i in range(720, -1, -60)],
        ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])

    plt.ylabel('Count Color Tall in RaDec Coordinates')
    plt.yticks([i * imgaxesRatioY for i in range(360, -1, -30)],
        ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])
    imgaxes.tick_params(axis='both', labelsize=6)

    plt.subplots_adjust(left=0.4, right=0.5, bottom=0.4, top=0.5)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)


def plotEzSky400RI():
    # radio Sky Radec map of Interpolated Power

    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 400 or 400 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky400RI_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    raHalfDegMin = raHalfDeg.min()
    print('                         raHalfDegMin  =', raHalfDegMin)
    raHalfDegMax = raHalfDeg.max()
    print('                         raHalfDegMax  =', raHalfDegMax)

    decHalfDegMin = decHalfDeg.min()
    print('                         decHalfDegMin =', decHalfDegMin)
    decHalfDegMax = decHalfDeg.max()
    print('                         decHalfDegMax =', decHalfDegMax)


    if raHalfDegMin == raHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Right Ascension value.')
        print()
        print('              raHalfDegMin == raHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        #radecPower = None           # free memory
        #del radecPower

        #raHalfDeg = None       # free memory
        #del raHalfDeg

        #decHalfDeg = None      # free memory
        #del decHalfDeg

        return(2)

    if decHalfDegMin == decHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Declination value.')
        print()
        print('              decHalfDegMin == decHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        #radecPower = None           # free memory
        #del radecPower

        #raHalfDeg = None       # free memory
        #del raHalfDeg

        #decHalfDeg = None      # free memory
        #del decHalfDeg

        return(3)

    xi = np.arange(0.,  721., 1.)         # in   0 to 360 degrees in half-degrees
    yi = np.arange(-180.,  181., 1.)        # in -90 to +90 degrees in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    zi = griddata((raHalfDeg, decHalfDeg-180.), radecPower, (xi, yi), method='linear')

    ###zi = gaussian_filter(zi, 9.)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))
    ax.scatter(raHalfDeg, decHalfDeg-180., marker='.', s=0.5,
        color='black', linewidths=0)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xlim(600, 480)      # inverts x axis
    plt.xticks([ 0.,    60., 120., 180., 240., 300., 360., 420., 480., 540., 600., 660., 720.],
               [' 0  ', '2', '4',  '6',  '8',  '10', '12', '14', '16', '18', '20', '22', '24'])

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in RaDec Coordinates')
    plt.ylim(-180, 180)
    plt.yticks( \
        [-180., -150., -120., -90.,  -60.,  -30.,  0.,  30.,  60.,  90.,  120., 150., 180.],
        ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzSky405RIL():
    # radio Sky Radec map of Interpolated Power with XYLimits

    global raH                      # float 1d array, from .ezb files
    global decDeg                   # float 1d array, from .ezb files
    global radecPowerBox            # empty list or float 1d array
    global radecRaBox               # integer 1d array
    global radecDecBox              # integer 1d array
    global raDegPerBox              # float
    global decDegPerBox             # float
    global raDegMinMaxL             # list of floats
    global decDegMinMaxL            # list of floats
    global ezSkyInputS              # string
    global ezSkyXYLimL              # list of floats

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 405 or 405 < ezSkyPlotRangeL[0] or not ezSkyXYLimL:
        return(1)

    plotName = 'ezSky405RIL_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPowerBox):
        # fill radecPowerBox, create radecCountBox, radecRaBox, radecDecBox,  raDegMinMaxL, and decDegMinMaxL
        ezSkyGridRadecBox()

    print()
    radecRaBoxMin = radecRaBox.min()
    print('                         radecRaBoxMin  =', radecRaBoxMin)
    radecRaBoxMax = radecRaBox.max()
    print('                         radecRaBoxMax  =', radecRaBoxMax)

    radecDecBoxMin = radecDecBox.min()
    print('                         radecDecBoxMin =', radecDecBoxMin)
    radecDecBoxMax = radecDecBox.max()
    print('                         radecDecBoxMax =', radecDecBoxMax)


    if radecRaBoxMin == radecRaBoxMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Right Ascension value.')
        print()
        print('              radecRaBoxMin == radecRaBoxMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        return(2)

    if radecDecBoxMin == radecDecBoxMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Declination value.')
        print()
        print('              radecDecBoxMin == radecDecBoxMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        return(3)

    # defines whole grid canvas, all may not be used
    xi = np.arange(0.,  721., 1.)         # in   0 to 360 degrees in half-degrees
    yi = np.arange(0.,  361., 1.)        # in -90 to +90 degrees in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    # interpolate radecPowerBox values onto (xi, yi) meshgrid
    #zi = griddata((radecRaBox, radecDecBox), radecPowerBox, (xi, yi), method='nearest')
    zi = griddata((radecRaBox, radecDecBox), radecPowerBox, (xi, yi), method='linear')

    # ezSkyXYLimL filter for ezSky405
    #zi = gaussian_filter(zi, 9.)
    #zi = gaussian_filter(zi, 1.)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))
    # breadcrumbs
    if ezSkyXYLimL[6]:
        raDeg = raH * 15.
        maskCrumbs = np.logical_and(raDegMinMaxL[0]  <= raDeg, raDeg  <= raDegMinMaxL[1])
        maskCrumbs = np.logical_and(decDegMinMaxL[0] <= decDeg, maskCrumbs)
        maskCrumbs = np.logical_and(maskCrumbs,                decDeg <= decDegMinMaxL[1])

        radecRaBoxCrumbs  = 0.5 * (raDeg[maskCrumbs]  - raDegMinMaxL[0])  / raDegPerBox
        radecDecBoxCrumbs = 0.5 * (decDeg[maskCrumbs] - decDegMinMaxL[0]) / decDegPerBox
        maskCrumbs = []   # free memory
        
        if 0. < ezSkyXYLimL[6]:
            ax.scatter(radecRaBoxCrumbs, radecDecBoxCrumbs, marker='.', s=ezSkyXYLimL[6]*40.,
                color='black', linewidths=0)
        else:
            ax.plot(radecRaBoxCrumbs, radecDecBoxCrumbs, marker='.', markersize=-ezSkyXYLimL[6],
                color='black')

    plt.title(titleS)

    plt.xlabel('Right Ascension (Degrees)\nRight Ascension (Hours)')
    plt.xlim(raDegMinMaxL[1], raDegMinMaxL[0])
    radecRaBoxMid = (radecRaBoxMin + radecRaBoxMax) / 2.
    radecRaDegMid = (raDegMinMaxL[0] + raDegMinMaxL[1]) / 2.
    print()
    print('                         radecRaDegMid  =', radecRaDegMid)
    plt.xticks([radecRaBoxMin, radecRaBoxMid, radecRaBoxMax],
                [f'{raDegMinMaxL[0]:.4f}\n{raDegMinMaxL[0]/15.:.4f}',
                    f'{radecRaDegMid:.4f}\n{radecRaDegMid/15.:.4f}',
                    f'{raDegMinMaxL[1]:.4f}\n{raDegMinMaxL[1]/15.:.4f}'])

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in RaDec Coordinates\nDeclination (Degrees)')
    plt.ylim(decDegMinMaxL[0], decDegMinMaxL[1])
    radecDecBoxMid = (radecDecBoxMin + radecDecBoxMax) / 2.
    radecDecDegMid = (decDegMinMaxL[0] + decDegMinMaxL[1]) / 2.
    print('                         radecDecDegMid =', radecDecDegMid)
    plt.yticks([radecDecBoxMin, radecDecBoxMid, radecDecBoxMax],
               [f'{decDegMinMaxL[0]:.4f}', f'{radecDecDegMid:.4f}', f'{decDegMinMaxL[1]:.4f}'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzSky406RILC():
    # radio Sky Radec map of Interpolated Power with XYLimits using Cygrid module
    #   https://github.com/bwinkel/cygrid
    #   Cygrid: A fast Cython-powered convolution-based gridding module for Python
    #   http://adsabs.harvard.edu/abs/2016A%26A...591A..12W

    global raH                      # float 1d array, from .ezb files
    global decDeg                   # float 1d array, from .ezb files
    global radecPowerBox            # empty list or float 1d array
    global radecRaBox               # integer 1d array
    global radecDecBox              # integer 1d array
    global raDegPerBox              # float
    global decDegPerBox             # float
    global raDegMinMaxL             # list of floats
    global decDegMinMaxL            # list of floats
    global ezSkyInputS              # string
    global ezSkyXYLimL              # list of floats

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 406 or 406 < ezSkyPlotRangeL[0] or not ezSkyXYLimL:
        return(1)

    plotName = 'ezSky406RILC_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPowerBox):
        # fill radecPowerBox, create radecCountBox, radecRaBox, radecDecBox,  raDegMinMaxL, and decDegMinMaxL
        ezSkyGridRadecBox()

    print()
    radecRaBoxMin = radecRaBox.min()
    print('                         radecRaBoxMin  =', radecRaBoxMin)
    radecRaBoxMax = radecRaBox.max()
    print('                         radecRaBoxMax  =', radecRaBoxMax)

    radecDecBoxMin = radecDecBox.min()
    print('                         radecDecBoxMin =', radecDecBoxMin)
    radecDecBoxMax = radecDecBox.max()
    print('                         radecDecBoxMax =', radecDecBoxMax)


    if radecRaBoxMin == radecRaBoxMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Right Ascension value.')
        print()
        print('              radecRaBoxMin == radecRaBoxMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        return(2)

    if radecDecBoxMin == radecDecBoxMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Declination value.')
        print()
        print('              radecDecBoxMin == radecDecBoxMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        return(3)











    # https://bwinkel.github.io/cygrid/latest/api/cygrid.SlGrid.html#cygrid.SlGrid.get_datacube

    #from astropy.io import fits
    #import matplotlib.pyplot as plt
    import cygrid       # py -m pip install cygrid

    # read-in data, lon/lat are 1D, input_signal has 2nd dimension: 1,
    # i.e., we are not gridding spectra but single values
    #input_lon, input_lat, input_signal = get_data()
    #radecRaBox, radecDecBox, radecPowerBox = get_data()


    # defines whole grid canvas, all may not be used
    xi = np.arange(0.,  721., 1.)       # in   0 to 360 degrees in half-degrees
    yi = np.arange(0.,  361., 1.)       # in -90 to +90 degrees in half-degrees
    xi = np.arange(0.,  362., 1.)
    yi = np.arange(-90.,  91., 0.5)
    xi = np.arange(-1.,  722., 1.)
    yi = np.arange(-1.,  722., 1.)






    # https://arxiv.org/pdf/1604.06667.pdf
    #   Listing 1. Basic Cygrid usage.

    from astropy.io import fits
    import cygrid       # py -m pip install cygrid

    # read-in data
    #glon, glat, signal = get_data (...)
    glon = radecRaBox
    glat = radecDecBox
    signal = radecPowerBox

    # define target FITS/WCS header
    header = {
        'NAXIS': 3,
        'NAXIS1': 101,
        'NAXIS2': 101,
        'NAXIS3': 1024,
        'CTYPE1': 'GLON -SFL',
        'CTYPE2': 'GLAT -SFL',
        'CDELT1': -0.1,
        'CDELT2': 0.1,
        'CRPIX1': 51,
        'CRPIX2': 51,
        'CRVAL1': 12.345,
        'CRVAL2': 3.14,
        }

    # prepare gridder
    kernelsize_sigma = 0.2

    kernel_type = 'gauss1d'
    kernel_params = (kernelsize_sigma, )
    kernel_support = 3 * kernelsize_sigma
    hpx_maxres = kernelsize_sigma / 2

    mygridder = cygrid.WcsGrid(header)  # ?????????????????????????????
    mygridder.set_kernel(
        kernel_type,
        kernel_params,
        kernel_support,
        hpx_maxres
        )

    # do the gridding
    mygridder.grid(glon, glat, signal)

    # query result and store to disk
    data_cube = mygridder.get_datacube()
    fits.writeto(
        'example.fits',
        header=header, data=data_cube
        )













    # prepare gridder
    kernelsize_sigma = 0.2

    kernel_type = 'gauss1d'
    kernel_params = (kernelsize_sigma, )  # must be a tuple
    kernel_support = 3 * kernelsize_sigma
    hpx_maxres = kernelsize_sigma / 2

    #mygridder = cygrid.SlGrid(target_lon, target_lat)
    mygridder = cygrid.SlGrid(xi, yi)
    mygridder.set_kernel(
        kernel_type,
        kernel_params,
        kernel_support,
        hpx_maxres,
        )

    print('                         radecRaBox.min()   =', radecRaBox.min())

    # do the actual gridding
    #mygridder.grid(input_lon, input_lat, input_signal)
    mygridder.grid(radecRaBox, radecDecBox, radecPowerBox)
    target_signal = gridder.get_datacube()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    #ax.scatter(target_lon, target_lat, c=target_signal)
    ax.scatter(xi, yi, c=target_signal)
    plt.show()

    # ezSkyXYLimL filter for ezSky405
    #zi = gaussian_filter(zi, 9.)
    #zi = gaussian_filter(zi, 1.)

    #plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))

    # breadcrumbs
    if ezSkyXYLimL[6]:
        raDeg = raH * 15.
        maskCrumbs = np.logical_and(raDegMinMaxL[0]  <= raDeg, raDeg  <= raDegMinMaxL[1])
        maskCrumbs = np.logical_and(decDegMinMaxL[0] <= decDeg, maskCrumbs)
        maskCrumbs = np.logical_and(maskCrumbs,                decDeg <= decDegMinMaxL[1])

        radecRaBoxCrumbs  = 0.5 * (raDeg[maskCrumbs]  - raDegMinMaxL[0])  / raDegPerBox
        radecDecBoxCrumbs = 0.5 * (decDeg[maskCrumbs] - decDegMinMaxL[0]) / decDegPerBox
        maskCrumbs = []   # free memory

        if 0. < ezSkyXYLimL[6]:
            ax.scatter(radecRaBoxCrumbs, radecDecBoxCrumbs, marker='.', s=ezSkyXYLimL[6]*40.,
                color='black', linewidths=0)
        else:
            ax.plot(radecRaBoxCrumbs, radecDecBoxCrumbs, marker='.', markersize=-ezSkyXYLimL[6],
                color='black')

    plt.title(titleS)

    plt.xlabel('Right Ascension (Degrees)\nRight Ascension (Hours)')
    plt.xlim(raDegMinMaxL[1], raDegMinMaxL[0])
    radecRaBoxMid = (radecRaBoxMin + radecRaBoxMax) / 2.
    radecRaDegMid = (raDegMinMaxL[0] + raDegMinMaxL[1]) / 2.
    print()
    print('                         radecRaDegMid  =', radecRaDegMid)
    plt.xticks([radecRaBoxMin, radecRaBoxMid, radecRaBoxMax],
                [f'{raDegMinMaxL[0]:.4f}\n{raDegMinMaxL[0]/15.:.4f}',
                    f'{radecRaDegMid:.4f}\n{radecRaDegMid/15.:.4f}',
                    f'{raDegMinMaxL[1]:.4f}\n{raDegMinMaxL[1]/15.:.4f}'])

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in RaDec Coordinates\nDeclination (Degrees)')
    plt.ylim(decDegMinMaxL[0], decDegMinMaxL[1])
    radecDecBoxMid = (radecDecBoxMin + radecDecBoxMax) / 2.
    radecDecDegMid = (decDegMinMaxL[0] + decDegMinMaxL[1]) / 2.
    print('                         radecDecDegMid =', radecDecDegMid)
    plt.yticks([radecDecBoxMin, radecDecBoxMid, radecDecBoxMax],
               [f'{decDegMinMaxL[0]:.4f}', f'{radecDecDegMid:.4f}', f'{decDegMinMaxL[1]:.4f}'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzSky450RIR():
    # radio Sky Radec map of Interpolated Power, Grote Reber 1944
    # 2 hemispheres, centered on RaDec of (20,0) and (6?,0)
    # http://www.bigear.org/CSMO/HTML/CS13/cs13p14.htm
    # has figure that says 1.9 meters (158 MHz)

    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 450 or 450 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky450RIR_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(radecPower):
        # fill radecPower, create radecCount, raHalfDeg, decHalfDeg
        ezSkyGridRadec()

    raHalfDegMin = raHalfDeg.min()
    print('                         raHalfDegMin  =', raHalfDegMin)
    raHalfDegMax = raHalfDeg.max()
    print('                         raHalfDegMax  =', raHalfDegMax)

    decHalfDegMin = decHalfDeg.min()
    print('                         decHalfDegMin =', decHalfDegMin)
    decHalfDegMax = decHalfDeg.max()
    print('                         decHalfDegMax =', decHalfDegMax)

    if raHalfDegMin == raHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Right Ascension value.')
        print()
        print('              raHalfDegMin == raHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        radecPower = None           # free memory
        del radecPower

        raHalfDeg = None       # free memory
        del raHalfDeg

        decHalfDeg = None      # free memory
        del decHalfDeg

        return(2)

    if decHalfDegMin == decHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Declination value.')
        print()
        print('              decHalfDegMin == decHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        radecPower = None           # free memory
        del radecPower

        raHalfDeg = None       # free memory
        del raHalfDeg

        decHalfDeg = None      # free memory
        del decHalfDeg

        return(3)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    xiHalfDeg = np.arange(0.,  781., 1.)        # 0 to +390 degrees in half-degrees
    yiHalfDeg = np.arange(-180.,  181., 1.)     # in -90 to +90 degrees in half-degrees
    xiHalfDeg, yiHalfDeg = np.meshgrid(xiHalfDeg, yiHalfDeg)

    if 1:               # 1 for no fill
        zi = griddata((raHalfDeg, decHalfDeg-180), radecPower, (xiHalfDeg, yiHalfDeg),
            method='linear')
    else:
        # add 5 minimum points, along both bottom and top, to help griddata interpolate all space
        radecPowerMin = radecPower.min()
        raHalfDegFiller  = np.array([0, 180, 390, 600, 780,   0, 180, 390, 600, 780])
        decHalfDegFiller = np.array([0,   0,   0,   0,   0, 360, 360, 360, 360, 360])  # bot and top
        radecPowerFiller      = np.full_like(raHalfDegFiller, radecPowerMin)
        zi = griddata((np.append(raHalfDeg, raHalfDegFiller, axis=0),
            np.append(decHalfDeg, decHalfDegFiller, axis=0)-180),
            np.append(radecPower, radecPowerFiller, axis=0),
            (xiHalfDeg, yiHalfDeg), method='linear')
    zi[:, 720:781] = zi[:, 0:61]        # Reber left hemisphere went past RA=24, repeating to RA=2



    if 0:           # 1 to mask the zi data into hemispheres - useful ??
        # calculate mask450, where true inside plotted hemispheres
        mask450 = np.zeros_like(xiHalfDeg, dtype=bool)      # False means do not plot

        # mask unused middle strip
        mask450[:, 360:420] = True       # True does not plot

        radiusMax2 = 180. * 180.        # 32,400
        #print('=========== radiusMax2 =', radiusMax2)
        # calculate mask450 for right hemisphere
        x0Right = 180   # right hemisphere is centered on 6*15*2=180 half-degrees
        for x in range(181):            # RA = 0 thru 6
            x0RightDelta = (x - x0Right)
            x0RightDelta2 = x0RightDelta * x0RightDelta
            for y in range(181):        # positive half-degrees
                y2 = y * y
                #print('=========== x0RightDelta2 + y2', x0RightDelta2 + y2)
                if radiusMax2 <= (x0RightDelta2 + y2):
                    # right hemisphere,
                    #   right edge at         0 half-degrees
                    #   left  edge at 0+360=360 half-degrees
                    mask450[180+y,x]     = True
                    mask450[180-y,x]     = True
                    mask450[180+y,360-x] = True
                    mask450[180-y,360-x] = True
                    
                    # left hemisphere,
                    #   right edge at 14*15*2=420 half-degrees
                    #   left  edge at 420+360=780 half-degrees
                    mask450[180-y,x+420] = True
                    mask450[180+y,x+420] = True
                    mask450[180+y,780-x] = True
                    mask450[180-y,780-x] = True
                else:
                    break   # on this x, no more True to be found                    

        #print('=========== mask450 =', mask450)
        #print('=========== sum(mask450) =', sum(mask450))

        # a mask needs to be boolean
        zi[mask450]   = np.nan      # True does not plot



    if 1:       # 1 for warping space into 2 hemispheres
        # https://adsabs.harvard.edu/pdf/1944ApJ...100..279R
        # https://chandra.harvard.edu/graphics/chronicle/cyga/radiosky_good.gif
        #   centered on RA=6 and RA=18
        # shows Grote Reber's 1944 Nicolosi globular projection of Interpolated Power plot.
        # https://en.wikipedia.org/wiki/Nicolosi_globular_projection
        # has complex math projection formulas.

        # Nicolosi globular projection warping definition:
        #   https://en.wikipedia.org/wiki/Nicolosi_globular_projection
        # and
        #   Page 234 of
        #   An album of map projections
        #   Professional Paper 1453
        #   By: John P. Snyder and Philip M. Voxland
        #   https://doi.org/10.3133/pp1453
        #   https://pubs.usgs.gov/publication/pp1453
        #       That last link adds talk of b and the "plus or minus sign in equation 203"
        # also https://observablehq.com/@toja/nicolosi-globular-projection
        
        # But all that math did not work well, so I now try the math from "achille hui",
        # https://math.stackexchange.com/questions/1672580/formula-for-nicolosi-globular-projection
        
        print("                         Compare to Grote Reber's 1944 paper:")
        print('                           https://adsabs.harvard.edu/pdf/1944ApJ...100..279R')
        print('                           https://chandra.harvard.edu/graphics/chronicle/cyga/radiosky_good.gif')
        print('                         Jansky and Reber history:')
        print('                           http://www.bigear.org/CSMO/HTML/CS12/cs12p08.htm')
        print('                           http://www.bigear.org/CSMO/HTML/CS13/cs13p14.htm')

        # create full sky RaDec coordinates, RA=0 thru 24 thru 2,
        #   RA=12 to 14 not used

        # R is the radius of the globe to be projected.

        # calculate each warp mapping (xiWarpedHalfDeg,yiWarpedHalfDeg) for
        #   one quarter of one hemisphere, bottom right at center = 0,0
        pi = np.pi
        piD2 = pi / 2.
        piD360 = pi / 360.
        showSize = 180
        for yHalfDeg in range(1, showSize):
            #print('=========== yHalfDeg =', yHalfDeg)

            # precalculations       
            yHalfDegP180 = yHalfDeg + 180       # Plus  180
            yHalfDegM180 = yHalfDeg - 180       # Minus 180 ?????????????????????????????????????
            yHalfDegF180 = 180 - yHalfDeg       # From  180

            # for special cases, the full formulae fail, handle below
            if yHalfDeg == 0 or yHalfDeg == 180:
                pass
            else:
                yRad = yHalfDeg * piD360     # = (yHalfDeg / 2) * (pi / 180)
                v = yRad / piD2
                c = np.cos(yRad)
                c2 = c * c
                s = np.sin(yRad)
                q = (1. - v * v) / (2. * (s - v))
                q2 = q * q

            #for xHalfDeg in range(0, 180):          # 0 thru 179 half-degrees
            for xHalfDeg in range(1, showSize):
                #print('=========== xHalfDeg =', xHalfDeg, ' yHalfDeg =', yHalfDeg)

                # handle special cases, where the full formulae fail
                if xHalfDeg == 0:           # meridian
                    xiWarpedHalfDeg = -1.   # flag no warp needed
                elif xHalfDeg == 180:       # left edge, use simpler formulae
                    xiWarpedRad = c
                    yiWarpedRad = s
                    xiWarpedHalfDeg = piD2 * xiWarpedRad / piD360
                    yiWarpedHalfDeg = piD2 * yiWarpedRad / piD360
                elif yHalfDeg == 0:         # equator
                    xiWarpedHalfDeg = -1.   # flag no warp needed
                elif yHalfDeg == 180:       # north pole
                    xiWarpedHalfDeg = 0.
                    yiWarpedHalfDeg = 180.
                else:
                    xRad = xHalfDeg * piD360     # = (xHalfDeg / 2) * (pi / 180)
                    u = xRad / piD2
                    p = (1 - u * u) / (2 * u)
                    p2 = p * p
                    A = 2 * p2 * q * (q - s) / (p2 + q2)
                    B = 4 * p2 * q2 * c2 / (p2 + q2)
                    delta = -A + np.sqrt(A * A + B)
                    xiWarpedRad = delta / (2 * p)
                    yiWarpedRad = s - delta / (2 * q)
                    xiWarpedHalfDeg = piD2 * xiWarpedRad / piD360
                    yiWarpedHalfDeg = piD2 * yiWarpedRad / piD360

                #print('                 xiWarpedHalfDeg =', xiWarpedHalfDeg,
                #    ' yiWarpedHalfDeg =', yiWarpedHalfDeg)
                #    ' b =', b)

                if 0 <= xiWarpedHalfDeg:
                    # warp needed

                    # Now have xiWarpedHalfDeg and yiWarpedHalfDeg
                    #   = warped from xiHalfDeg and yiHalfDeg.
                    # Warp eight sky points to that Nicolosi_globular_projection

                    # warp to Grote Reber's 1944 right hemisphere,
                    #   RA=0 thru 12, centered on RA=6 (180 half-degrees)

                    # precalculations
                    xHalfDegP180 = xHalfDeg + 180       # Plus 180
                    xHalfDegF180 = 180 - xHalfDeg       # From 180
                    
                    # warp top left sky bearing
                    xiHalfDeg[yHalfDegP180, xHalfDegP180] = 180. + xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegP180, xHalfDegP180] = yiWarpedHalfDeg

                    # warp bottom left sky bearing
                    xiHalfDeg[yHalfDegF180, xHalfDegP180] = 180. + xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegF180, xHalfDegP180] = -yiWarpedHalfDeg

                    # warp top right sky bearing
                    xiHalfDeg[yHalfDegP180, xHalfDegF180] = 180. - xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegP180, xHalfDegF180] = yiWarpedHalfDeg

                    # warp bottom right sky bearing
                    xiHalfDeg[yHalfDegF180, xHalfDegF180] = 180. - xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegF180, xHalfDegF180] = -yiWarpedHalfDeg

                    # warp to Grote Reber's 1944 left hemisphere,
                    #   RA=14 thru 2, centered on RA=20 (600 half-degrees)

                    # precalculations
                    xHalfDegP600 = xHalfDeg + 600       # Plus 600
                    xHalfDegF600 = 600 - xHalfDeg       # From 600

                    # warp top left sky bearing
                    xiHalfDeg[yHalfDegP180, xHalfDegP600] = 600. + xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegP180, xHalfDegP600] = yiWarpedHalfDeg

                    # warp bottom left sky bearing
                    xiHalfDeg[yHalfDegF180, xHalfDegP600] = 600. + xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegF180, xHalfDegP600] = -yiWarpedHalfDeg

                    # warp top right sky bearing
                    xiHalfDeg[yHalfDegP180, xHalfDegF600] = 600. - xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegP180, xHalfDegF600] = yiWarpedHalfDeg

                    # warp bottom right sky bearing
                    xiHalfDeg[yHalfDegF180, xHalfDegF600] = 600. - xiWarpedHalfDeg
                    yiHalfDeg[yHalfDegF180, xHalfDegF600] = -yiWarpedHalfDeg

    #print()
    #print('=========== len(raHalfDeg)  =', len(raHalfDeg))
    #print('=========== len(decHalfDeg) =', len(decHalfDeg))
    #print('=========== len(radecPower) =', len(radecPower))

    #zi = gaussian_filter(zi, 9.)



    if 1:           # 1 to mask the warped space into hemispheres
        # calculate mask450, where true inside plotted hemispheres
        mask450 = np.zeros_like(xiHalfDeg, dtype=bool)      # False means do not plot

        radiusMax2 = 180. * 180.        # 32,400
        #print('=========== radiusMax2 =', radiusMax2)
        # calculate mask450 for right hemisphere
        x0Right = 180   # right hemisphere is centered on 6*15*2=180 half-degrees
        for x in range(182):            # RA = 0 thru 6
            for y in range(182):        # positive half-degrees
                xWarped = xiHalfDeg[y, x]
                x0RightWarpedDelta = (xWarped - x0Right)
                x0RightWarpedDelta2 = x0RightWarpedDelta * x0RightWarpedDelta
                yWarped = yiHalfDeg[y, x]
                yWarped2 = yWarped * yWarped
                #print('=========== x0RightDelta2 + y2', x0RightDelta2 + y2)
                if radiusMax2 <= (x0RightWarpedDelta2 + yWarped2):
                    # right hemisphere,
                    #   right edge at         0 half-degrees
                    #   left  edge at 0+360=360 half-degrees
                    mask450[ y,    x] = True
                    mask450[-y,    x] = True
                    mask450[ y,360-x] = True
                    mask450[-y,360-x] = True
                    
                    # left hemisphere,
                    #   right edge at 14*15*2=420 half-degrees
                    #   left  edge at 420+360=780 half-degrees
                    mask450[ y,420+x] = True
                    mask450[-y,420+x] = True
                    mask450[ y,780-x] = True
                    mask450[-y,780-x] = True
                else:
                    break   # on this x, no more True to be found                    
        # remove whisker at top of hemispheres
        mask450[ 360,:] = True          # True does not plot

        #print('=========== mask450 =', mask450)
        #print('=========== sum(mask450) =', sum(mask450))

        # mask unused middle strip
        mask450[:,360:420] = True       # True does not plot

        # a mask needs to be boolean
        zi[mask450]   = np.nan          # True does not plot    ????????????????????????????????????????????????



    if 0:
        # border
        ziMin = zi.min()
        #print(np.shape(zi))     # says (361, 721)
        zi[:,   0] = ziMin
        zi[:, 720] = ziMin



    # plot contour lines and contour fills
    plt.contourf(xiHalfDeg, yiHalfDeg, zi, 100, cmap=plt.get_cmap('gnuplot'))



    if 0:
        imgaxes = fig.add_axes(ax.get_position(), label='image', xticks=[], yticks=[])
        #print(ax.get_position())

        imgaxes.set_xlim(0, ezSkyBackground1XMax)
        imgaxes.set_ylim(0, ezSkyBackground1YMax)

        plt.gca().invert_yaxis()

        # comment next line to remove background
        img = imgaxes.imshow(zi, aspect='auto')



    zi = None     # free memory
    del zi

    ylabelText = f'{ezSkyInputS[2:]} Interpolated in Mollweide Galactic Coordinates'

    #plt.contourf(xiHalfDeg, yiHalfDeg, zi, 100, cmap=plt.get_cmap('gnuplot'))

    if 0:
        ax.scatter(raHalfDeg, decHalfDeg-180., marker='.', s=0.5,
            color='black', linewidths=0)

    if 0:
        ax.scatter(xiHalfDeg, yiHalfDeg, marker='.', s=0.5,
            color='black', linewidths=0)

    if 0:
        ax.scatter(xiHalfDeg[180:180+showSize,180:180+showSize],
            yiHalfDeg[180:180+showSize,180:180+showSize], marker='.', s=0.5,
            color='black', linewidths=0)
                
    if 1:
        # horizontal grids
        for y in range(20, 341, 20):
            ax.scatter(xiHalfDeg[y,1:360], yiHalfDeg[y,1:360], marker='.', s=0.5,
                color='black', linewidths=0)
            ax.scatter(xiHalfDeg[y,421:780], yiHalfDeg[y,421:780], marker='.', s=0.5,
                color='black', linewidths=0)

        # outer circles, meridians
        for x in [1, 359, 421, 779, 180, 600]:
            ax.scatter(xiHalfDeg[0:360,x], yiHalfDeg[0:360,x], marker='.', s=0.5,
                color='black', linewidths=0)

        # vertical grids
        for x in range(30, 360, 30):
            ax.scatter(xiHalfDeg[20:340,x], yiHalfDeg[20:340,x], marker='.', s=0.5,
                color='black', linewidths=0)
            ax.scatter(xiHalfDeg[20:340,x+420], yiHalfDeg[20:340,x+420], marker='.', s=0.5,
                color='black', linewidths=0)

    if 0:
        fig.text(180., 300.95, 'Latitude', \
            horizontalalignment='left', verticalalignment='top', fontsize=10)

    ax.set_xticks([])   # disable
    ax.set_yticks([])   # disable

    plt.axis('equal')      # x and y scales the same

    plt.title(titleS)

    plt.xlim(800, -20)        # inverts x axis, with left and right margins

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated Like Grote Reber 1944')
    plt.ylim(-180, 180)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def ezSkyGridGalactic():
    # fill galacticPower, create galacticGLatHalfDeg, galacticGLonHalfDeg, maskGalactic

    global gLatDeg                  # float 1d array
    global gLonDeg                  # float 1d array
    global power                    # float 1d array

    global galacticPower            # float   1d array                          fill
    global galacticGLatHalfDeg      # integer 1d array                          create
    global galacticGLonHalfDeg      # integer 1d array                          create

    global ezSkyMaskOutL            # list of string and floats
    global ezSkyMaskInL             # list of strings

    global maskGalactic             # integer 2d array

    global ezSkyPlotRangeL          # integer list

    ## if galactic grid not needed, then return
    #if ezSkyPlotRangeL[1] < 500 or 523 < ezSkyPlotRangeL[0]:
    #    return(1)

    print()
    print('  ezSkyGridGalactic ================================')

    # integrate .ezb file data into grids,
    #   gridGalacticCount and gridGalacticPower for Galactic map (in half-degree grid)
    # gLat=-90 through +90 degrees,    or 0 through 360  halfdegrees
    gridGalacticGLatHalfDegRange = 90 + 90 + 90 + 90 + 1
    # gLon=-180 through +180 degrees, or 0 through 719 halfdegrees
    gridGalacticGLonHalfDegRange = 360 + 360 + 1
    gridGalacticCount = np.zeros([gridGalacticGLatHalfDegRange, gridGalacticGLonHalfDegRange], dtype = int)
    #print(np.shape(gridGalacticCount))     # says (361, 721)
    gridGalacticPower = np.zeros([gridGalacticGLatHalfDegRange, gridGalacticGLonHalfDegRange], dtype = float)
    #print(np.shape(gridGalacticPower))     # says (361, 721)

    # account for grid's 0.5 degree per index
    for i in range(antLen):
        # use 180 and 360 offsets to make all indices positive
        gLatHalfDeg = int(gLatDeg[i] + gLatDeg[i] + 180.5)          # round to integer halfDegree 0 thru 360
        gLonHalfDeg = int(gLonDeg[i] + gLonDeg[i] + 360.5)          # round to integer halfDegree 0 thru 720
        # gLonHalfDeg wraps around, use gLonHalfDeg=0
        if 720 <= gLonHalfDeg:
            gLonHalfDeg -= 720                                      # closest integer halfDegree 0 thru 719
        gridGalacticCount[gLatHalfDeg, gLonHalfDeg] += 1            # count     of gridBox
        gridGalacticPower[gLatHalfDeg, gLonHalfDeg] += power[i]     # power sum of gridBox

    # gLonHalfDeg wraps around, copy gLonHalfDeg=0 to gLonHalfDeg=720
    gridGalacticCount[:, 720] = gridGalacticCount[:, 0]
    gridGalacticPower[:, 720] = gridGalacticPower[:, 0]

    #gLatDeg = []        # free memory
    #gLonDeg = []        # free memory
    #power   = []        # free memory

    # unravel grids and collect as lists, and later convert to more compact numpys
    galacticPowerL       = []
    galacticGLatHalfDegL = []
    galacticGLonHalfDegL = []
    for gLatHalfDeg in range(gridGalacticGLatHalfDegRange):
        for gLonHalfDeg in range(gridGalacticGLonHalfDegRange):
            if gridGalacticCount[gLatHalfDeg, gLonHalfDeg]:
                # calculate average power
                galacticPowerL.append(gridGalacticPower[gLatHalfDeg, gLonHalfDeg] \
                    / gridGalacticCount[gLatHalfDeg, gLonHalfDeg])
                galacticGLatHalfDegL.append(gLatHalfDeg)
                galacticGLonHalfDegL.append(gLonHalfDeg)

    gridGalacticCount = []                                  # free memory
    gridGalacticPower = []                                  # free memory

    # create compact numpys from lists
    galacticPower        = np.array(galacticPowerL)
    galacticPowerL       = []                               # free memory
    galacticGLatHalfDeg  = np.array(galacticGLatHalfDegL)
    galacticGLatHalfDegL = []                               # free memory
    galacticGLonHalfDeg  = np.array(galacticGLonHalfDegL)
    galacticGLonHalfDegL = []                               # free memory

    print(f'                         len(galacticPower) = {len(galacticPower):,}')


    # if maskGalactic not needed, then return
    if not ezSkyMaskInL and not ezSkyMaskOutL:
        maskGalactic = []       # flag maskGalactic as not available
        return(1)

    #print(np.shape(zi))     # says (361, 721)
    maskGalactic = np.zeros([361, 721], dtype = int)

    # N0RQV Lat = 40.4
    # 40.4 + 3 = 43.4
    # ezSkyMaskN0RQV_90_43.4.npz
    # 40.4 - 90 = -49.6
    # ezSkyMaskN0RQV_-49.6_-90.npz

    # decDegMax = 43.5
    # 43.5 + 3 = 46.5
    # ezSkyMaskLto_90_46.5.npz
    # LTO Lat = 40.3
    # 40.3 - 90 = -49.7
    # ezSkyMaskLto_-49.7_-90.npz

    # read in maskGalactic masks
    for ezSkyMaskInName in ezSkyMaskInL:
        print()
        print(' Loading maskGalactic from', ezSkyMaskInName, 'file ...')
        #print(maskGalactic.files)
        maskGalactic += np.load(ezSkyMaskInName)['maskGalactic']

    if ezSkyMaskOutL:
        from astropy import units as u
        #from astropy.time import Time
        #from astropy.coordinates import EarthLocation
        from astropy.coordinates import SkyCoord

        maskGalThis = np.zeros([361, 721], dtype = int)
        ezSkyMaskOutName = ezSkyMaskOutL[0]

        maskPlotDecDegN = ezSkyMaskOutL[1]                  # north border
        maskPlotDecHalfDegN = min(maskPlotDecDegN,  90.0)   # trim silly values
        maskPlotDecHalfDegN += maskPlotDecHalfDegN + 180    # halfDegrees

        maskPlotDecDegS = ezSkyMaskOutL[2]                  # south border
        maskPlotDecHalfDegS = max(maskPlotDecDegS, -90.0)   # trim silly values
        maskPlotDecHalfDegS += maskPlotDecHalfDegS + 180    # halfDegrees

        print()
        print(' Modifying Galactic plot mask into', ezSkyMaskOutName+'.npz file ...')

        for maskPlotGalLonHDeg in range(360 + 1 + 360):  # starting at right side of plot
            print('\r    maskPlotGalLonHDeg =', maskPlotGalLonHDeg, '    of 720       ', end='')
            # maskGalLonDegUnits: -180.0 to 0.0 to +180.0   with degree units
            maskGalLonDegUnits = ((maskPlotGalLonHDeg - 360) / 2.)*u.deg
            for maskPlotGalLatHDeg in range(361):   # 361 = 180 + 1 + 180, starting at bottom of plot
                cTarget = SkyCoord( \
                    b = ((maskPlotGalLatHDeg - 180) / 2.)*u.deg, \
                    l = maskGalLonDegUnits, \
                    frame = 'galactic')
                cTargetDecDeg = float(cTarget.icrs.dec.degree)

                if maskPlotDecDegS <= cTargetDecDeg and cTargetDecDeg <= maskPlotDecDegN:
                    maskGalThis[maskPlotGalLatHDeg, maskPlotGalLonHDeg] = 1    # True gets np.nan later

        maskGalactic += maskGalThis

        #maskGalThis = None         # free memory
        #del maskGalThis

        # write maskGalactic to .npz file
        print()
        print(' Saving maskGalactic to', ezSkyMaskOutName+'.npz file ...')
        #print(' maskGalactic before=', maskGalactic)
        #print('     maskGalactic.sum() =', maskGalactic.sum())
        #print('     (maskGalactic == 0).sum() =', (maskGalactic == 0).sum())
        #print('     np.shape(maskGalactic) =', np.shape(maskGalactic))
        maskGalactic = maskGalactic != 0         # make file compress to smaller ?
        np.savez_compressed(ezSkyMaskOutName, maskGalactic=maskGalactic)



def ezSkyGridGalacticBox():
    # using gLatDeg, gLonDeg, power, and ezSkyXYLimL,
    #   fill galacticPowerBox, create gLatBox, gLonBox,
    #   gLatDegPerBox, gLonDegPerBox, gLatDegMinMaxL, and gLonDegMinMaxL

    global gLatDeg                  # float 1d array, from .ezb files
    global gLonDeg                  # float 1d array, from .ezb files
    global power                    # float 1d array, from .ezb files
    global ezSkyXYLimL              # list of floats

    global galacticPowerBox         # float   1d array                          fill
    global gLatBox                  # integer 1d array                          create
    global gLonBox                  # integer 1d array                          create
    global gLatDegPerBox            # float                                     create
    global gLonDegPerBox            # float                                     create
    global gLatDegMinMaxL           # list of floats                            create
    global gLonDegMinMaxL           # list of floats                            create


    print()
    print('  ezSkyGridGalacticBox ================================')

    # define the 721 by 361 grid boxes

    # create min(xData)
    gLonDegMin = gLonDeg.min()
    print('                         gLonDegMin  =', gLonDegMin)

    # create max(xData)
    gLonDegMax = gLonDeg.max()
    print('                         gLonDegMax  =', gLonDegMax)

    # create min(yData)
    gLatDegMin = gLatDeg.min()
    print('                         gLatDegMin  =', gLatDegMin)

    # create max(yData)
    gLatDegMax = gLatDeg.max()
    print('                         gLatDegMax  =', gLatDegMax)

    print()
    print('                         ezSkyXYLimL =', ezSkyXYLimL)
    # ezSkyXYLimL is [xPerBox, yPerBox, xMin, xMax, yMin, yMax]
    #                 0        1        2     3     4     5

    # create gLonDegPerBox and gLonDegMinMaxL[:1]
    gLonDegMinMaxL = [999., 999.]                               # silly values
    if 0. < ezSkyXYLimL[0] and ezSkyXYLimL[0] <= 360.:          # if xPerBox not silly
        gLonDegPerBox = ezSkyXYLimL[0]                          # use xPerBox
        if -180. <= ezSkyXYLimL[2] and ezSkyXYLimL[2] <= 180.:  # if xMin not silly
            gLonDegMinMaxL[0] = ezSkyXYLimL[2]                  # use xMin
        else:
            gLonDegMinMaxL[0] = gLonDegMin                      # use min(xData)

        if -180. <= ezSkyXYLimL[3] and ezSkyXYLimL[3] <= 180.:  # if xMax not silly
            gLonDegMinMaxL[1] = ezSkyXYLimL[3]                  # use xMax
        else:
            # use min(max(xData), xMax that xPerBox will allow)
            gLonDegMinMaxL[1] = min(gLonDegMax, gLonDegMinMaxL[0] + 720. * ezSkyXYLimL[0], 360.)

    else:                                                       # xPerBox is silly, create xPerBox
        if -180. <= ezSkyXYLimL[2] and ezSkyXYLimL[2] <= 180.:  # if xMin not silly
            gLonDegMinMaxL[0] = ezSkyXYLimL[2]                  # use xMin
        else:
            gLonDegMinMaxL[0] = gLonDegMin                      # use min(xData)

        if -180. <= ezSkyXYLimL[3] and ezSkyXYLimL[3] <= 180.:  # if xMax not silly
            gLonDegMinMaxL[1] = ezSkyXYLimL[3]                  # use xMax
        else:
            gLonDegMinMaxL[1] = gLonDegMax                      # use max(xData)
        #  create xPerBox
        gLonDegPerBox = (gLonDegMinMaxL[1] - gLonDegMinMaxL[0]) / 720.
    print()
    print('                         gLonDegPerBox  =', gLonDegPerBox)
    print('                         gLonDegMinMaxL =', gLonDegMinMaxL)

    # create gLatDegPerBox and gLatDegMinMaxL[:1]
    gLatDegMinMaxL = [999., 999.]                               # silly values
    if 0. < ezSkyXYLimL[1] and ezSkyXYLimL[1] <= 180.:          # if yPerBox not silly
        gLatDegPerBox = ezSkyXYLimL[1]                          # use yPerBox
        if -90. <= ezSkyXYLimL[4] and ezSkyXYLimL[4] <= 90.:    # if yMin not silly
            gLatDegMinMaxL[0] = ezSkyXYLimL[4]                  # use yMin
        else:
            gLatDegMinMaxL[0] = gLatDegMin                      # use min(yData)

        if -90. <= ezSkyXYLimL[5] and ezSkyXYLimL[5] <= 90.:    # if yMax not silly
            gLatDegMinMaxL[1] = ezSkyXYLimL[5]                  # use yMax
        else:
            # use min(max(yData), yMax that yPerBox will allow)
            gLatDegMinMaxL[1] = min(gLatDegMax, gLatDegMinMaxL[0] + 360. * ezSkyXYLimL[1], 180.)

    else:                                                       # yPerBox is silly, create yPerBox
        if -90. <= ezSkyXYLimL[4] and ezSkyXYLimL[4] <= 90.:    # if yMin not silly
            gLatDegMinMaxL[0] = ezSkyXYLimL[4]                  # use yMin
        else:
            gLatDegMinMaxL[0] = gLatDegMin                      # use min(yData)

        if -90. <= ezSkyXYLimL[5] and ezSkyXYLimL[5] <= 90.:    # if yMax not silly
            gLatDegMinMaxL[1] = ezSkyXYLimL[5]                  # use yMax
        else:
            gLatDegMinMaxL[1] = gLatDegMax                      # use max(yData)
        #  create yPerBox
        gLatDegPerBox = (gLatDegMinMaxL[1] - gLatDegMinMaxL[0]) / 360.
    print('                         gLatDegPerBox  =', gLatDegPerBox)
    print('                         gLatDegMinMaxL =', gLatDegMinMaxL)

    # integrate .ezb file data into grids,
    #   gridGalacticCount and gridGalacticPower for Galactic map
    gridGalacticGLonBoxRange = 360 + 360 + 2            # gLonBox= 0 thru 720
    gridGalacticGLatBoxRange = 180 + 180 + 2            # gLonBox= 0 thru 360
    gridGalacticCount = np.zeros([gridGalacticGLatBoxRange, gridGalacticGLonBoxRange], dtype = int)
    gridGalacticPower = np.zeros([gridGalacticGLatBoxRange, gridGalacticGLonBoxRange], dtype = float)

    # account for grid's gLonDegPerBox and gLatDegPerBox
    for i in range(antLen):
        gLonDegThis = gLonDeg[i]
        if gLonDegThis <= gLonDegMinMaxL[1]:
            gLonBoxIndex = int(0.5 * (gLonDegThis - gLonDegMinMaxL[0]) / gLonDegPerBox + 0.5)       # integer gLonBoxIndex
            gLatDegThis = gLatDeg[i]
            if gLatDegThis <= gLatDegMinMaxL[1]:
                gLatBoxIndex = int(0.5 * (gLatDegThis - gLatDegMinMaxL[0]) / gLatDegPerBox + 0.5)   # integer gLatBoxIndex
                #print('======= gLatBoxIndex =', gLatBoxIndex)
                #print('======= gLonBoxIndex =', gLonBoxIndex)
                if  0 <= gLatBoxIndex and gLatBoxIndex <= gridGalacticGLonBoxRange and \
                    0 <= gLonBoxIndex and gLonBoxIndex <= gridGalacticGLonBoxRange:     # if inside canvas
                        gridGalacticCount[gLatBoxIndex, gLonBoxIndex] += 1              # count     of gridBox
                        gridGalacticPower[gLatBoxIndex, gLonBoxIndex] += power[i]       # power sum of gridBox

    # gLonDeg wraps around, copy gLonDeg=0 to gLonDeg=360
    gridGalacticCount[:, 360] = gridGalacticCount[:, 0]
    gridGalacticPower[:, 360] = gridGalacticPower[:, 0]

    #gLatDeg = []        # free memory
    #gLonDeg = []        # free memory
    #power   = []        # free memory

    # unravel grids and collect as lists, and later convert to more compact numpys
    galacticPowerBoxL = []
    gLatBoxL          = []
    gLonBoxL          = []
    for gLatBoxIndex in range(gridGalacticGLatBoxRange):
        for gLonBoxIndex in range(gridGalacticGLonBoxRange):
            if gridGalacticCount[gLatBoxIndex, gLonBoxIndex]:
                # calculate average power
                galacticPowerBoxL.append(gridGalacticPower[gLatBoxIndex, gLonBoxIndex] \
                    / gridGalacticCount[gLatBoxIndex, gLonBoxIndex])
                gLatBoxL.append(gLatBoxIndex)
                gLonBoxL.append(gLonBoxIndex)

    gridGalacticPower = []      # free memory
    gridGalacticCount = []      # free memory

    # create compact numpys from lists
    galacticPowerBox  = np.array(galacticPowerBoxL)
    galacticPowerBoxL = []   # free memory
    gLatBox   = np.array(gLatBoxL)
    gLatBoxL  = []   # free memory
    gLonBox   = np.array(gLonBoxL)
    gLonBoxL  = []   # free memory

    print(f'                         len(galacticPowerBox) = {len(galacticPowerBox):,}')
    #print(f'                         len(gLatBox) = {len(gLatBox):,}')
    #print(f'                         len(gLonBox) = {len(gLonBox):,}')



def plotEzSky500GMI():
    # radio Sky Galactic Mercator projection map of Interpolated power

    global galacticPower                    # float   1d array
    global galacticGLatHalfDeg              # integer 1d array
    global galacticGLonHalfDeg              # integer 1d array

    global maskGalactic                     # integer 2d array
    #global ezSkyGalCrossingGLatCenter       # float
    #global ezSkyGalCrossingGLatNear         # float
    #global ezSkyGalCrossingGLonCenter       # float
    #global ezSkyGalCrossingGLonNear         # float

    global ezSkyInputS                      # string

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global titleS                           # string
    #global ezSkyDispGrid                   # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 500 or 500 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky500GMI_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(galacticPower):
        # fill galacticPower, create galacticGLatHalfDeg, galacticGLonHalfDeg, maskGalactic
        ezSkyGridGalactic()

    galacticGLatHalfDegMin = galacticGLatHalfDeg.min()
    print('                         galacticGLatHalfDegMin =', galacticGLatHalfDegMin)
    galacticGLatHalfDegMax = galacticGLatHalfDeg.max()
    print('                         galacticGLatHalfDegMax =', galacticGLatHalfDegMax)

    galacticGLonHalfDegMin = galacticGLonHalfDeg.min()
    print('                         galacticGLonHalfDegMin =', galacticGLonHalfDegMin)
    galacticGLonHalfDegMax = galacticGLonHalfDeg.max()
    print('                         galacticGLonHalfDegMax =', galacticGLonHalfDegMax)

    if galacticGLatHalfDegMin == galacticGLatHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Latitude value.')
        print()
        print('              galacticGLatHalfDegMin == galacticGLatHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(2)

    if galacticGLonHalfDegMin == galacticGLonHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Longitude  value.')
        print()
        print('              galacticGLonHalfDegMin == galacticGLonHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(3)

    xi = np.arange(0., 720.5, 1.)       # represents -180 through +180 degrees, in half-degrees
    yi = np.arange(0., 360.5, 1.)       # represents  -90 through  +90 degrees, in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    # interpolate galacticPower values onto (xi, yi) meshgrid
    zi = griddata((galacticGLonHalfDeg, galacticGLatHalfDeg), galacticPower, (xi, yi), method='nearest')
    #print(np.shape(zi))     # says (361, 721)

    zi = gaussian_filter(zi, 9.)

    if len(maskGalactic):                           # if maskGalactic available
        # a mask needs to be boolean
        zi[maskGalactic != 0] = np.nan              # True gets np.nan

    #zi[np.isnan(zi)] = galacticPower.min()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot contour lines and contour fills
    plt.contour(xi, yi, zi, 20, linewidths=0.2, colors='black')
    plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))

    # optional thin black lines of true data
    ax.scatter(galacticGLonHalfDeg, galacticGLatHalfDeg, marker='.', s=0.5, color='black', linewidths=0)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    # 0 through 720 represents -180 through +180 degrees, in half-degrees
    plt.xlim(720, 0)        # in half-degrees, inverted x axis
    plt.xticks([ 720.,  660.,  600.,  540., 480., 420., 360., 300.,  240.,  180.,  120.,   60.,    0.],
               [ '180', '150', '120', '90', '60', '30', '0',  '-30', '-60', '-90', '-120', '-150', '-180'])

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in Mercator Galactic Coordinates')
    # 0 through 360 represents -90 through +90 degrees, in half-degrees
    plt.ylim(0, 360)        # in half-degrees
    plt.yticks([0.,    30.,   60.,   90.,   120.,  150.,  180., 210., 240., 270., 300., 330., 360.],
               ['-90', '-75', '-60', '-45', '-30', '-15', '0',  '15', '30', '45', '60', '75', '90'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky505GMIL():
    # radio Sky Galactic Mercator projection map of Interpolated power with XYLimits

    global gLatDeg                  # float 1d array, from .ezb files
    global gLonDeg                  # float 1d array, from .ezb files

    global galacticPowerBox         # float   1d array                          fill
    global gLatBox                  # integer 1d array                          create
    global gLonBox                  # integer 1d array                          create

    global gLatDegPerBox            # float                                     create
    global gLonDegPerBox            # float                                     create
    global gLatDegMinMaxL           # list of floats                            create
    global gLonDegMinMaxL           # list of floats                            create
    global ezSkyInputS              # string
    global ezSkyXYLimL              # list of floats

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global titleS                           # string
    #global ezSkyDispGrid                   # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 505 or 505 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky505GMIL_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(galacticPowerBox):
        # fill galacticPowerBox, create gLatBox, gLonBox,
        #   gLatDegPerBox, gLonDegPerBox, gLatDegMinMaxL, and gLonDegMinMaxL
        ezSkyGridGalacticBox()

    print()
    # X axis
    gLonBoxMin = gLonBox.min()
    print('                         gLonBoxMin =', gLonBoxMin)
    gLonBoxMax = gLonBox.max()
    print('                         gLonBoxMax =', gLonBoxMax)

    # Y axis
    gLatBoxMin = gLatBox.min()
    print('                         gLatBoxMin  =', gLatBoxMin)
    gLatBoxMax = gLatBox.max()
    print('                         gLatBoxMax  =', gLatBoxMax)


    if gLatBoxMin == gLatBoxMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Latitude value.')
        print()
        print('              gLatBoxMin == gLatBoxMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(2)

    if gLonBoxMin == gLonBoxMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Longitude  value.')
        print()
        print('              gLonBoxMin == gLonBoxMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(3)

    xi = np.arange(0., 720.5, 1.)       # represents -180 through +180 degrees, in half-degrees
    yi = np.arange(0., 360.5, 1.)       # represents  -90 through  +90 degrees, in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    # interpolate galacticPowerBox values onto (xi, yi) meshgrid
    #zi = griddata((gLonBox, gLatBox), galacticPowerBox, (xi, yi), method='nearest')
    zi = griddata((gLonBox, gLatBox), galacticPowerBox, (xi, yi), method='linear')
    #print(np.shape(zi))     # says (361, 721)

    # ezSkyXYLimL filter for ezSky505
    #zi = gaussian_filter(zi, 9.)

    #zi[np.isnan(zi)] = galacticPowerBox.min()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # plot contour lines and contour fills
    #plt.contour(xi, yi, zi, 20, linewidths=0.2, colors='black')
    plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))

    # breadcrumbs
    if ezSkyXYLimL[6]:
        maskCrumbs = np.logical_and(gLatDegMinMaxL[0] <= gLatDeg, gLatDeg <= gLatDegMinMaxL[1])
        maskCrumbs = np.logical_and(gLonDegMinMaxL[0] <= gLonDeg, maskCrumbs)
        maskCrumbs = np.logical_and(maskCrumbs,                   gLonDeg <= gLonDegMinMaxL[1])

        gLatBoxCrumbs = 0.5 * (gLatDeg[maskCrumbs] - gLatDegMinMaxL[0]) / gLatDegPerBox
        gLonBoxCrumbs = 0.5 * (gLonDeg[maskCrumbs] - gLonDegMinMaxL[0]) / gLonDegPerBox
        maskCrumbs = []   # free memory

        if 0. < ezSkyXYLimL[6]:
            ax.scatter(gLonBoxCrumbs, gLatBoxCrumbs, marker='.', s=ezSkyXYLimL[6]*40.,
                color='black', linewidths=0)
        else:
            ax.plot(gLonBoxCrumbs, gLatBoxCrumbs, marker='.', markersize=-ezSkyXYLimL[6],
                color='black')

    plt.title(titleS)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xlabel('Galactic Longitude (Degrees)')
    plt.xlim(gLonBoxMax, gLonBoxMin)
    gLonBoxMid = (gLonBoxMin + gLonBoxMax) / 2.
    gLonDegMid = (gLonDegMinMaxL[0] + gLonDegMinMaxL[1]) / 2.
    print()
    print('                         gLonBoxMid =', gLonBoxMid)
    print('                         gLonDegMid =', gLonDegMid)
    plt.xticks([gLonBoxMin, gLonBoxMid, gLonBoxMax],
        [f'{gLonDegMinMaxL[0]:.4f}',
            f'{gLonDegMid:.4f}',
            f'{gLonDegMinMaxL[1]:.4f}'])

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in Galactic Coordinates' \
        + '\nGalactic Latitude (Degrees)')
    plt.ylim(gLatBoxMin, gLatBoxMax)
    gLatBoxMid = (gLatBoxMin + gLatBoxMax) / 2.
    gLatDegMid = (gLatDegMinMaxL[0] + gLatDegMinMaxL[1]) / 2.
    print('                         gLatBoxMid =', gLatBoxMid)
    print('                         gLatDegMid =', gLatDegMid)
    plt.yticks([gLatBoxMin, gLatBoxMid, gLatBoxMax],
        [f'{gLatDegMinMaxL[0]:.4f}',
            f'{gLatDegMid:.4f}',
            f'{gLatDegMinMaxL[1]:.4f}'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky510GSI():
    # radio Sky Galactic Sinusoidal projection map of Interpolated power
    # https://en.wikipedia.org/wiki/Sinusoidal_projection
    
    global galacticPower                    # float   1d array
    global galacticGLatHalfDeg              # integer 1d array
    global galacticGLonHalfDeg              # integer 1d array

    global maskGalactic                     # integer 2d array
    #global ezSkyGalCrossingGLatCenter       # float
    #global ezSkyGalCrossingGLatNear         # float
    #global ezSkyGalCrossingGLonCenter       # float
    #global ezSkyGalCrossingGLonNear         # float

    global ezSkyInputS                      # string

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global titleS                           # string
    #global ezSkyDispGrid                   # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 510 or 510 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky510GSI_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(galacticPower):
        # fill galacticPower, create gLatHalfDeg, gLonHalfDeg, maskGalactic
        ezSkyGridGalactic()

    galacticGLatHalfDegMin = galacticGLatHalfDeg.min()
    print('                         galacticGLatHalfDegMin =', galacticGLatHalfDegMin)
    galacticGLatHalfDegMax = galacticGLatHalfDeg.max()
    print('                         galacticGLatHalfDegMax =', galacticGLatHalfDegMax)

    galacticGLonHalfDegMin = galacticGLonHalfDeg.min()
    print('                         galacticGLonHalfDegMin =', galacticGLonHalfDegMin)
    galacticGLonHalfDegMax = galacticGLonHalfDeg.max()
    print('                         galacticGLonHalfDegMax =', galacticGLonHalfDegMax)

    if galacticGLatHalfDegMin == galacticGLatHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Latitude value.')
        print()
        print('              galacticGLatHalfDegMin == galacticGLatHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(2)

    if galacticGLonHalfDegMin == galacticGLonHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Longitude value.')
        print()
        print('              galacticGLonHalfDegMin == galacticGLonHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(3)

    # create a (xi, yi) meshgrid rectangular grid
    xi = np.arange(0., 720.5, 1.)       # represents -180 through +180 degrees, in half-degrees
    yi = np.arange(0., 360.5, 1.)       # represents  -90 through  +90 degrees, in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    # interpolate galacticPower values onto (xi, yi) meshgrid
    zi = griddata((galacticGLonHalfDeg, galacticGLatHalfDeg), galacticPower, (xi, yi), method='nearest')
    #print(np.shape(zi))     # says (361, 721)

    zi = gaussian_filter(zi, 9.)

    if len(maskGalactic):                           # if maskGalactic available
        # a mask needs to be boolean
        zi[maskGalactic != 0] = np.nan              # True gets np.nan

    #zi[np.isnan(zi)] = galacticPower.min()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Warp that (xi, yi) rectangular grid according to the Sinusoidal projection.
    # Accounting for 360 offset, reduce the bottom south half's xi by sin(yi), mirror for the top north half
    for gLatHalfDeg in range(0, 180):         # in half-degrees
        gLatHalfDegSin = math.sin(math.radians(gLatHalfDeg / 2.))
        for gLonHalfDeg in range(0, 721):     # in half-degrees
            xi[    gLatHalfDeg, gLonHalfDeg] = \
                (xi[    gLatHalfDeg, gLonHalfDeg] - 360.) * gLatHalfDegSin + 360.
            xi[360-gLatHalfDeg, gLonHalfDeg] = \
                (xi[360-gLatHalfDeg, gLonHalfDeg] - 360.) * gLatHalfDegSin + 360.

    # plot contour lines and contour fills
    plt.contour(xi, yi, zi, 20, linewidths=0.2, colors='black')
    plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))

    # Draw thin black lines of true data paths.
    # Likewise, after accounting for offsets,
    #   reduce each galacticGLonHalfDeg[i] by cos(galacticGLatHalfDeg[i])
    galacticGLonHalfDegSinusoidal = np.empty_like(galacticGLonHalfDeg)
    for i in range(len(galacticGLonHalfDeg)):
        galacticGLonHalfDegSinusoidal[i] = (galacticGLonHalfDeg[i] - 360.) \
            * math.cos(math.radians(abs(galacticGLatHalfDeg[i] - 180.)) / 2.) + 360.
    ax.scatter(galacticGLonHalfDegSinusoidal, galacticGLatHalfDeg, marker='.', s=0.5,
        color='black', linewidths=0)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    # 0 through 720 represents -180 through +180 degrees, in half-degrees
    plt.xlim(725, -5)        # in half-degrees, inverted x axis
    plt.xticks([ 720.,  660.,  600.,  540., 480., 420., 360., 300.,  240.,  180.,  120.,   60.,    0.],
               [ '180', '150', '120', '90', '60', '30', '0',  '-30', '-60', '-90', '-120', '-150', '-180'])

    plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in Sinusoidal Galactic Coordinates')
    # 0 through 360 represents -90 through +90 degrees, in half-degrees
    plt.ylim(-5, 365)        # in half-degrees
    plt.yticks([0.,    30.,   60.,   90.,   120.,  150.,  180., 210., 240., 270., 300., 330., 360.],
               ['-90', '-75', '-60', '-45', '-30', '-15', '0',  '15', '30', '45', '60', '75', '90'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSkyMollweide(plotNumber):
    # plotNumber    integer         # 520 or 522 or 523

    #def plotEzSky520GOI():
    # radio Sky Galactic Mollweide projection map of Interpolated power.
    # "M" already used, so "GOI" using second letter "O" from "Mollweide".
    # https://en.wikipedia.org/wiki/Mollweide_projection

    #def plotEzSky522GOLat():
    # radio Sky Galactic Mollweide projection map of ezSkyGalCrossingGLatNear Data points

    #def plotEzSky523GOLon():
    # radio Sky Galactic Mollweide projection map of ezSkyGalCrossingGLonNear Data points

    global galacticPower                    # float   1d array
    global galacticGLatHalfDeg              # integer 1d array
    global galacticGLonHalfDeg              # integer 1d array

    global ezSkyInputS                      # string
    global maskGalactic                     # integer 2d array
    global ezSkyGalCrossingGLatCenter       # float
    global ezSkyGalCrossingGLatNear         # float
    global ezSkyGalCrossingGLonCenter       # float
    global ezSkyGalCrossingGLonNear         # float

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string
    global titleS                           # string
    #global ezSkyDispGrid                   # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < plotNumber or plotNumber < ezSkyPlotRangeL[0]:
        return(1)

    if plotNumber == 520:
        plotName = 'ezSky520GOI_' + ezSkyInputS + '.png'
    elif plotNumber == 522:
        plotName = 'ezSky522GOLat.png'
    elif plotNumber == 523:
        plotName = 'ezSky523GOLon.png'
    else:
        # not supported
        return(2)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    if not len(galacticPower):
        # fill galacticPower, create galacticGLatHalfDeg, galacticGLonHalfDeg, maskGalactic
        ezSkyGridGalactic()

    galacticGLatHalfDegMin = galacticGLatHalfDeg.min()
    print('                         galacticGLatHalfDegMin =', galacticGLatHalfDegMin)
    galacticGLatHalfDegMax = galacticGLatHalfDeg.max()
    print('                         galacticGLatHalfDegMax =', galacticGLatHalfDegMax)

    galacticGLonHalfDegMin = galacticGLonHalfDeg.min()
    print('                         galacticGLonHalfDegMin =', galacticGLonHalfDegMin)
    galacticGLonHalfDegMax = galacticGLonHalfDeg.max()
    print('                         galacticGLonHalfDegMax =', galacticGLonHalfDegMax)

    if plotNumber == 520 and galacticGLatHalfDegMin == galacticGLatHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Latitude value.')
        print()
        print('              galacticGLatHalfDegMin == galacticGLatHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(3)

    if plotNumber == 520 and galacticGLonHalfDegMin == galacticGLonHalfDegMax:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('============= WARNING: Can not create the ' + plotName + ' plot.')
        print('              All this data has only one Galactic Longitude value.')
        print()
        print('              galacticGLonHalfDegMin == galacticGLonHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(4)

    # create a (xi, yi) meshgrid rectangular grid
    xi = np.arange(0., 720.5, 1.)       # represents -180 through +180 degrees, in half-degrees
    yi = np.arange(0., 360.5, 1.)       # represents  -90 through  +90 degrees, in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Mollweide projection warping definition:
    # theta and Lat and Lon are in radians.
    # R is the radius of the globe to be projected.
    # Given Lat and Lon,
    # xiWarped = (R * sqrt(2)) * (2 / pi) * (Lon - 0) * cos(theta)
    # yiWarped = (R * sqrt(2)) * sin(theta)
    # after finding a theta such that
    # 2 * theta + sin(2 * theta) = pi * sin(Lat)

    # Calculate the top left quarter of the projection warping,
    # and mirror across vertical and horizontal mid lines.

    pie    = math.pi
    piD360 = pie / 360

    # calculate all the thetas once
    # The gLatHalfDeg values needed are 1 to 180 in halfDegrees.
    # Pre-calculate the theta for each gLatHalfDeg value
    theta = np.empty(181)
    for gLatHalfDeg in range(181):         # in half-degrees
        gLatHalfDegRad = gLatHalfDeg * piD360
        theta0 = gLatHalfDegRad
        # guessing that 50 iterations should calculate close enough
        for i in range(50):
            #theta1 = theta0 - ((2 * theta0 + math.sin(2 * theta0) - pie * math.sin(gLatHalfDegRad)) / (2 + 2 * math.cos(2 * theta0)))
            theta1 = theta0 - ((2 * theta0 + math.sin(2 * theta0) - pie * math.sin(gLatHalfDegRad)) / (4 * math.cos(theta0) * math.cos(theta0)))
            theta0 = theta1
        theta[gLatHalfDeg] = theta1
    # Printing all values of theta numpy without truncation
    #np.set_printoptions(threshold=np.inf)
    #print(' theta =', theta)
    #print(' theta.tolist() =', theta.tolist())
    #exit()

    # Warp that (xi, yi) rectangular grid according to the Mollweide projection.
    globeRadius = 127.3     # tuned to get about 0 <= xi <= 720 and 0 <= yi <= 360
    globeRadiusSqrt2 = globeRadius * math.sqrt(2.)
    globeRadiusSqrt2T2DPi = (globeRadiusSqrt2 + globeRadiusSqrt2) / pie
    globeRadiusSqrt2T2PiDPiD360 = globeRadiusSqrt2T2DPi * piD360

    # calculate xiWarped and yiWarped for one quarter of earth.
    # Then warp each quarter of earth's xi and yi.
    for gLatHalfDeg in range(181):         # in half-degrees
        #yiWarped = (globeRadius * sqrt(2)) * math.sin(theta[gLatHalfDeg])
        yiWarped = globeRadiusSqrt2 * math.sin(theta[gLatHalfDeg])
        for gLonHalfDeg in range(361):     # in half-degrees
            #xiWarped = (R * sqrt(2)) * (2 / pi) * radOf(gLonHalfDeg - 0) * math.cos(theta[gLatHalfDeg])
            #xiWarped = globeRadiusSqrt2T2DPi * gLonHalfDeg * piD360 * math.cos(theta[gLatHalfDeg])
            xiWarped = globeRadiusSqrt2T2PiDPiD360 * gLonHalfDeg * math.cos(theta[gLatHalfDeg])

            # later, xlim mirrors left-right, leaving 0,0 at bottom right

            #print(np.shape(xi))     # says (361, 721)

            # after xlim, warp top left
            xi[180+gLatHalfDeg, 360+gLonHalfDeg] = 360 + xiWarped
            yi[180+gLatHalfDeg, 360+gLonHalfDeg] = 180 + yiWarped

            # after xlim, warp top right
            xi[180+gLatHalfDeg, 360-gLonHalfDeg] = 360 - xiWarped
            yi[180+gLatHalfDeg, 360-gLonHalfDeg] = 180 + yiWarped

            # after xlim, warp bottom left
            xi[180-gLatHalfDeg, 360+gLonHalfDeg] = 360 + xiWarped
            yi[180-gLatHalfDeg, 360+gLonHalfDeg] = 180 - yiWarped

            # after xlim, warp bottom right
            xi[180-gLatHalfDeg, 360-gLonHalfDeg] = 360 - xiWarped
            yi[180-gLatHalfDeg,     gLonHalfDeg] = 180 - yiWarped

    #print(' xi.max() =', xi.max())
    #print(' xi.min() =', xi.min())
    #print(' yi.max() =', yi.max())
    #print(' yi.min() =', yi.min())

    if plotNumber == 520:
        # interpolate galacticPower values onto (xi, yi) meshgrid
        zi = griddata((galacticGLonHalfDeg, galacticGLatHalfDeg), galacticPower, (xi, yi), method='nearest')
        #print(np.shape(zi))     # says (361, 721)

        zi = gaussian_filter(zi, 9.)

        if len(maskGalactic):                           # if maskGalactic available
            # a mask needs to be boolean
            zi[maskGalactic != 0] = np.nan              # True gets np.nan

        #zi[np.isnan(zi)] = galacticPower.min()

        if 0:
            # border
            ziMin = zi.min()
            #print(np.shape(zi))     # says (361, 721)
            zi[:,   0] = ziMin
            zi[:, 720] = ziMin

        # plot contour lines and contour fills
        plt.contour(xi, yi, zi, 20, linewidths=0.2, colors='black')
        plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))

        zi = None     # free memory
        del zi

        if 1:
            # draw thin black lines of true data paths,
            # warp each galacticGLatHalfDeg[i] and galacticGLonHalfDeg[i]
            galacticGLatHalfDegMollweide = np.empty_like(galacticGLatHalfDeg)
            galacticGLonHalfDegMollweide = np.empty_like(galacticGLatHalfDeg)
            for i in range(len(galacticGLatHalfDeg)):
                galacticGLonHalfDegMollweide[i] = xi[galacticGLatHalfDeg[i], galacticGLonHalfDeg[i]]
                galacticGLatHalfDegMollweide[i] = yi[galacticGLatHalfDeg[i], galacticGLonHalfDeg[i]]
            ax.scatter(galacticGLonHalfDegMollweide, galacticGLatHalfDegMollweide, marker='.', s=0.5,
                color='black', linewidths=0)
            galacticGLatHalfDegMollweide = None     # free memory
            del galacticGLatHalfDegMollweide
            galacticGLonHalfDegMollweide = None     # free memory
            del galacticGLonHalfDegMollweide

        ylabelText = f'{ezSkyInputS[2:]} Interpolated in Mollweide Galactic Coordinates'

    elif plotNumber == 522:
        # plotNumber is 522

        if ezSkyGalCrossingGLatNear == 0.:
            return(5)

        # draw red dots of true data paths, if defined as a Galactic Crossing.
        # warp each galacticGLatHalfDeg[i] and galacticGLonHalfDeg[i]
        #print(' galacticGLatHalfDeg =', galacticGLatHalfDeg)

        ezSkyGalCrossingGLatHalfDegMax = int(180 + ezSkyGalCrossingGLatCenter + ezSkyGalCrossingGLatCenter + ezSkyGalCrossingGLatNear + ezSkyGalCrossingGLatNear)     # convert to halfDegrees
        ezSkyGalCrossingGLatHalfDegMin = int(180 + ezSkyGalCrossingGLatCenter + ezSkyGalCrossingGLatCenter - ezSkyGalCrossingGLatNear - ezSkyGalCrossingGLatNear)     # convert to halfDegrees
        galacticGLatHalfDegMollweideL = []
        galacticGLonHalfDegMollweideL = []
        for i in range(len(galacticGLatHalfDeg)):
            # if defined as a Galactic Crossing
            if ezSkyGalCrossingGLatHalfDegMin <= galacticGLatHalfDeg[i] and galacticGLatHalfDeg[i] <= ezSkyGalCrossingGLatHalfDegMax:
                galacticGLonHalfDegMollweideL.append(xi[galacticGLatHalfDeg[i], galacticGLonHalfDeg[i]])
                galacticGLatHalfDegMollweideL.append(yi[galacticGLatHalfDeg[i], galacticGLonHalfDeg[i]])
        ax.scatter(galacticGLonHalfDegMollweideL, galacticGLatHalfDegMollweideL, marker='.', s=10,
            color='red', linewidths=0)
        galacticGLatHalfDegMollweideL = []      # free memory
        galacticGLonHalfDegMollweideL = []      # free memory

        # border
        #print(np.shape(xi))     # says (361, 721)
        ax.plot(xi[:,   0], yi[:,   0], linewidth=0.5, color='black')
        ax.plot(xi[:, 720], yi[:, 720], linewidth=0.5, color='black')

        ylabelText = f'{ezSkyInputS[2:]} Galactic Crossings\nezSkyGalCrossingGLatNear = {ezSkyGalCrossingGLatNear}'

    else:
        # plotNumber is 523

        if ezSkyGalCrossingGLonNear == 0.:
            return(6)

        # draw red dots of true data paths, if defined as a Galactic Crossing.
        # warp each galacticGLonHalfDeg[i] and galacticGLatHalfDeg[i]
        #print(' galacticGLonHalfDeg =', galacticGLonHalfDeg)

        ezSkyGalCrossingGLonHalfDegMax = int(360 + ezSkyGalCrossingGLonCenter + ezSkyGalCrossingGLonCenter + ezSkyGalCrossingGLonNear + ezSkyGalCrossingGLonNear)     # convert to halfDegrees
        ezSkyGalCrossingGLonHalfDegMin = int(360 + ezSkyGalCrossingGLonCenter + ezSkyGalCrossingGLonCenter - ezSkyGalCrossingGLonNear - ezSkyGalCrossingGLonNear)     # convert to halfDegrees
        galacticGLatHalfDegMollweideL = []
        galacticGLonHalfDegMollweideL = []
        for i in range(len(galacticGLonHalfDeg)):
            # if defined as a Galactic Crossing
            if ezSkyGalCrossingGLonHalfDegMin <= galacticGLonHalfDeg[i] and galacticGLonHalfDeg[i] <= ezSkyGalCrossingGLonHalfDegMax:
                galacticGLonHalfDegMollweideL.append(xi[galacticGLatHalfDeg[i], galacticGLonHalfDeg[i]])
                galacticGLatHalfDegMollweideL.append(yi[galacticGLatHalfDeg[i], galacticGLonHalfDeg[i]])
        ax.scatter(galacticGLonHalfDegMollweideL, galacticGLatHalfDegMollweideL, marker='.', s=10,
            color='red', linewidths=0)
        galacticGLatHalfDegMollweideL = []      # free memory
        galacticGLonHalfDegMollweideL = []      # free memory

        # border
        #print(np.shape(xi))     # says (361, 721)
        ax.plot(xi[:,   0], yi[:,   0], linewidth=0.5, color='black')
        ax.plot(xi[:, 720], yi[:, 720], linewidth=0.5, color='black')

        ylabelText = f'{ezSkyInputS[2:]} Galactic Crossings\nezSkyGalCrossingGLonNear = {ezSkyGalCrossingGLonNear}'

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    # 0 through 720 represents -180 through +180 degrees, in half-degrees
    plt.xlim(725, -5)        # in half-degrees, inverted x axis
    plt.xticks([ 720.,  660.,  600.,  540., 480., 420., 360., 300.,  240.,  180.,  120.,   60.,    0.],
               [ '180', '150', '120', '90', '60', '30', '0',  '-30', '-60', '-90', '-120', '-150', '-180'])

    #plt.ylabel(f'{ezSkyInputS[2:]} Interpolated in Mollweide Galactic Coordinates')
    plt.ylabel(ylabelText)
    # 0 through 360 represents -90 through +90 degrees, in half-degrees
    plt.ylim(-5, 365)        # in half-degrees
    plt.yticks([0.,    30.,   60.,   90.,   120.,  150.,  180., 210., 240., 270., 300., 330., 360.],
               ['-90', '-75', '-60', '-45', '-30', '-15', '0',  '15', '30', '45', '60', '75', '90'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def plotEzSky600azEl():
    # radio Sky AzEl AzimuthElevation map, Power color

    global azDeg                    # float 1d array
    global elDeg                    # float 1d array
    global power                    # float 1d array

    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    plotCountdown -= 1

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 600 or 600 < ezSkyPlotRangeL[0]:
        return(1)

    plotName = 'ezSky600azEl_' + ezSkyInputS + '.png'

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    #ax.set_axis_off()

    #pts = plt.scatter(azDeg, elDeg,
    #    s=1, marker='|', c=power, cmap=plt.get_cmap('gnuplot'))
    pts = plt.scatter(azDeg, elDeg,
        s=10, marker='.', c=power, cmap=plt.get_cmap('gnuplot'))

    cbar = plt.colorbar(pts, orientation='horizontal', shrink=0.3, pad=0.06)
    cbar.ax.tick_params(labelsize=6)

    # plot wide grid lines
    plt.axhline(y=0., linewidth=0.5, color='black')
    plt.axvline(x=90., linewidth=0.5, color='black')
    plt.axvline(x=180., linewidth=0.5, color='black')
    plt.axvline(x=270., linewidth=0.5, color='black')

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    plt.xlim(0, 360)
    #plt.xticks([i * imgaxesRatioX for i in range(720, -1, -60)],
    #    ['0', '2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])
    #xticks = [i for i in range(0, 361, 30)]
    #xticksS = [str(i) for i in xticks]
    #plt.xticks(xticks)
    plt.xticks(range(0, 361, 30))

    plt.ylabel(f'{ezSkyInputS[2:]} Color in AzEl Coordinates')
    plt.ylim(-90, 90)
    #plt.yticks([i * imgaxesRatioY for i in range(360, -1, -30)],
    #    ['-90', '-75', '-60', '-45', '-30', '-15', '0', '15', '30', '45', '60', '75', '90'])
    #imgaxes.tick_params(axis='both', labelsize=6)
    #plt.yticks(range(-90, 91, 30))     # but uses ugly large dash for minus sign !
    plt.yticks(range(-90, 91, 30), 
        ['-90', '-60', '-30', '0', '30', '60', '90'])

    #plt.subplots_adjust(left=0.4, right=0.5, bottom=0.4, top=0.5)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')
    #plt.close(fig)



def printGoodbye():

    global antLen                   # integer
    global commandString            # string
    global startTime
    global programRevision          # string
    global ezSkyPlotRangeL          # integer list

    # print status
    if 0:
        print()
        print('   ezRAObsName      =', ezRAObsName)
        if 0:
            print('   ezSkyDispGrid            =', ezSkyDispGrid)
        print('   antLen =', antLen)

    print()
    print(' ezSkyInput =', ezSkyInput)
    print(' ezSkyPlotRangeL =', ezSkyPlotRangeL)

    stopTime = time.time()
    stopTimeS = time.ctime()
    print(f'\n       Last sample = {antLen - 1:,}\n')
    print('That Python command')
    print(f'  {commandString}')
    print(f' took {int(stopTime-startTime):,} seconds = {(stopTime-startTime)/60.:1.1f} minutes')
    print(f' Now = {stopTimeS[:-5]}\n')
    print(f' programRevision = {programRevision}')
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

    global startTime
    global programRevision          # string
    global commandString            # string

    global radecCount               # float   1d array
    global radecPower               # float   1d array
    global raHalfDeg                # integer 1d array
    global decHalfDeg               # integer 1d array
    
    global xTickLocsAnt             # array

    startTime = time.time()

    #print('programRevision = ' + programRevision)
    print()

    commandString = ''
    for i in sys.argv:
        commandString += i + '  '
    print(' This Python command =', commandString)

    if len(sys.argv) < 2:
        printUsage()

    xTickLocsAnt = []               # force new xTickLocsAnt

    printHello()

    ezSkyArguments()

    # create ezRAObsName, ezSkyInputS, fileNameLast, raH, decDeg, gLatDeg, gLonDeg, power, antLen
    readDataDir()

    # create antLenM1, titleS, ezbColumnColor
    plotPrep()

    # plot the input data
    plotEzSky010raH()
    plotEzSky020decDeg()
    plotEzSky030gLatDeg()
    plotEzSky031gLatDegSorted()
    plotEzSky032gLatDegSortedCross()
    plotEzSky040gLonDeg()
    plotEzSky041gLonDegSorted()
    plotEzSky043gLonDegSortedCross()
    plotEzSky070azDeg()
    plotEzSky080elDeg()

    plotEzSky100input()

    # plot the azEl plots

    plotEzSky600azEl()

    # free azEl memory
    azDeg = []
    elDeg = []

    # plot the raDec plots
    
    # if needed, creates radecCount, radecPower, raHalfDeg, decHalfDeg
    #ezSkyGridRadec()

    plotEzSky200RBVO()  # radio Sky Radec map with Background, power Vertical Offset
    plotEzSky201RBMax() # radio Sky Radec map with Background, dots on left and right maximum power

    plotEzSky300RB()    # radio Sky Radec map with Background, power color
    plotEzSky301RBT()   # radio Sky Radec map with Background, power color Tall
    plotEzSky309RBTC()  # radio Sky Radec map with Background, Count Tall

    plotEzSky400RI()    # radio Sky Radec map Interpolated
    plotEzSky405RIL()   # radio Sky Radec map Interpolated with XYLimits
    #plotEzSky406RILC()  # radio Sky Radec map Interpolated with XYLimits using Cygrid module
    plotEzSky450RIR()   # radio Sky Radec map Interpolated, Grote Reber 1944

    # free radec memory
    radecCount = []
    radecPower = []
    raHalfDeg  = []
    decHalfDeg = []

    # plot the Galactic plots

    # if needed, creates galacticPower, galacticGLatHalfDeg, galacticGLonHalfDeg
    #ezSkyGridGalactic()

    plotEzSky500GMI()   # radio Sky Galactic Mercator   projection map of Interpolated power
    #plotEzSkyMercator(500)
    #plotEzSkyMercator(502)
    #plotEzSkyMercator(503)
    plotEzSky505GMIL()   # radio Sky Galactic Mercator  projection map of Interpolated power with XYLimits
    plotEzSky510GSI()   # radio Sky Galactic Sinusoidal projection map of Interpolated power
    #plotEzSkySinusoidal(510)
    #plotEzSkySinusoidal(512)
    #plotEzSkySinusoidal(513)
    #plotEzSky502GOI()   # radio Sky Galactic Mollweide  projection map of Interpolated power
    plotEzSkyMollweide(520)     # plotEzSky520GOI
    plotEzSkyMollweide(522)     # plotEzSky522GOLat
    plotEzSkyMollweide(523)     # plotEzSky523GOLon

    printGoodbye()



if __name__== '__main__':
  main()


# python3 ../ezRA/ezColGB20m240126a.py  data/Skynet_59735_AP_-_ST3_81159_29887.A.raw.txt -overwrite Skynet_59735_AP_-_ST3_81159_29887.A.raw6.txt ezColGB20mInput 6h
# python3 ../ezRA/ezCon.py   data/Skynet_59735_AP_-_ST3_81159_29887.A.raw6.txt -ezConPlotRangeL 191 191
# python3 ../ezRA/ezSky240126a.py Skynet_59735_AP_-_ST3_81159_29887.A.raw6.ezb -ezSkyInput 10 -ezSkyPlotRangeL 405 405 -ezSkyXYLimL 999 999 999 999 999 999 0 


# python3 ../ezRA/ezColGB20m240126a.py  data/Skynet_59735_AP_-_ST3_81159_29887.A.cal.txt -overwrite Skynet_59735_AP_-_ST3_81159_29887.A.cal6.txt ezColGB20mInput 6
# python3 ../ezRA/ezCon.py   data/Skynet_59735_AP_-_ST3_81159_29887.A.cal6.txt -ezConPlotRangeL 191 191
# python3 ../ezRA/ezSky240126a.py Skynet_59735_AP_-_ST3_81159_29887.A.cal6.ezb -ezSkyInput 10 -ezSkyPlotRangeL 405 405 -ezSkyXYLimL 999 999 999 999 999 999 0 

# python3 ../ezRA/ezSky240128a.py  Skynet_59735_AP_-_ST3_81159_29887.A.raw5.ezb -ezSkyInput 10 -ezSkyPlotRangeL 405 405  -ezSkyXYLimL 999 999  999 999  999 999  -5

# python3 ../ezRA/ezSky240130c.py  Skynet_59735_AP_-_ST3_81159_29887.A.cal5.ezb -ezSkyInput 10 -ezSkyPlotRangeL 505 505  -ezSkyXYLimL 999 999  999 999  999 999  0

# ezRABase\lto16h>py  ..\ezRA\ezSky240606a.py  . -ezSkyInput 14 -ezSkyPlotRangeL 405 405 -ezSkyXYLimL 999 999 265.25 267.25 -39 -19 0.5

