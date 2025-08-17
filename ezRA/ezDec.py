programName = 'ezDec250811a.py'
programRevision = programName

# Easy Radio Astronomy (ezRA) ezDec sky pointing coordinates conversion program,
#   to convert sky pointing coordinates
#   to drift-scan Dec coordinate and possible Galactic plane crossings.

# https://github.com/tedcline/ezRA

# Copyright (c) 2025, Ted Cline   TedClineGit@gmail.com

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


# ezDec250811a, backslash e errors
# ezDec250808a, -ezDefaultsFile index fix, Az input fixes
# ezDec250731a, optionally print out GLon By Dec
# ezDec250730k, sky object looping, dusting
# ezDec250730h
# ezDec250730g dusting
# ezDec250730e dusting
# ezDec250730d, and plotted gLonDegDecHDegP180Right[]
# ezDec250730c, and plotted gLonDegDecHDegP180Left[]
# ezDec250730b, create gLonDegDecHDegP180Left[]
# ezDec250730a, start, create gLonDegDecHDegP18Left[]

# ezWhen240308a, "skyCoordinate" to "skyObject", -ezWhenSkyObjectL, dusted imports,
#   'No sky objects found'

import os
from astropy.time import Time
import matplotlib.pyplot as plt
import numpy as np


def printUsage():

    global programRevision          # string

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezDec.py [optional arguments]')
    print('  Linux:     python3 ezDec.py [optional arguments]')
    print()
    print('  Easy Radio Astronomy (ezRA) ezDec sky pointing coordinates conversion program,')
    print('     to convert sky pointing coordinates')
    print('     to drift-scan Dec coordinate and possible Galactic plane crossings.')
    print()
    print('  Arguments may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezDec program,')
    print("  then in order from the ezDefaults.txt in the ezDec.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  py ezDec.py -help                  (print this help)')
    print('  py ezDec.py -h                     (print this help)')
    print()
    print('    -ezRAObsName   Lebanon Kansas    (Observatory Name)')
    print('    -ezRAObsLat    39.8282           (Observatory Latitude  (degrees))')
    print('    -ezRAObsLon    -98.5696          (Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl   563.88            (Observatory Above Mean Sea Level (meters))')
    print()
    print('     Sun and/or Moon:')
    print('         Sun')
    print('         Moon')
    print()
    print('     Below uses "P" for Positive, and "N" for Negative.')
    print()
    print('     AzEl coordinates:')
    print('         Ax.xPx.x        where x.x are Azimuth (degrees) and Elevation (degrees) float numbers')
    print('         A123.4P56.7     Az=123.4 and El=+56.7')
    print('         A123.4N56.7     Az=123.4 and El=-56.7')
    print('         A12N56          Az=12    and El=-56')
    print('         (time and Earth location are used)')
    print()
    print('     RaDec coordinates:')
    print('         Rx.xPx.x        where x.x are RightAscension (hours) and Declination (degrees) float numbers')
    print('         R2.53P89.26     Polaris star')
    print('         R17.76N29       Galactic center')
    print('         R12.3P56.7      RA=12.3 and Dec=+56.7')
    print('         R12.3N56.7      RA=12.3 and Dec=-56.7')
    print('         R12N56          RA=12   and Dec=-56')
    print()
    print('     Galactic coordinates:')
    print('         GPx.xPx.x       where x.x are GLatitude (degrees) and GLongitude (degrees) float numbers')
    print('         GP0P0           Galactic center')
    print('         GP12.3P145.6    GLat=+12.3 and GLon=+145.6')
    print('         GN12.3N145.6    GLat=-12.3 and GLon=-145.6')
    print('         GN12N145        GLat=-12   and GLon=-145')
    print()
    print('     -ezDecSkyObjectL   rest of the ezDefaults.txt line is a list of sky objects (without comments)')
    print()
    print('     If not the current UTC midnight, enter the UTC day (Year, Month, Day):')
    print('         -YYMMDD')
    print()
    print('     If not the current UTC time, enter the UTC time (Year, Month, Day, Hour, minute):')
    print('         -YYMMDDHH')
    print('         -YYMMDDHHmm')
    print()
    #print('    -ezDecPlotRangeL    0  100    (save only this range of ezDec plots to file, to save time)')
    #print()
    print('    -ezDefaultsFile ../bigDish8.txt     (additional file of ezRA arguments)')
    print()
    print('    -eXXXXXXXXXXXXXXzIgonoreThisWholeOneWord')
    print('         (any one word starting with -eX is ignored, handy for long command line editing)')
    print()
    print()
    print(r'EXAMPLE:  py  ..\ezRA\ezDec.py  A180P45 -2401170523')
    print(r'EXAMPLE:  py  ..\ezRA\ezDec.py  GN12N145')
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
    print('            ezDec.py -help')

    print()
    print('=================================================')
    ###############################################print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    import sys
    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezDecArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    #global ezDecPlotRangeL                 # integer list
    global skyObjectL                       # list of strings

    print()
    print('   ezDecArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileNameInput, 'r')
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


            # be kind, ignore argument keyword capitalization
            thisLine0Lower = thisLine[0].lower()

            # ezRA arguments used by multiple programs:
            if thisLine0Lower == '-ezRAObsLat'.lower():
                ezRAObsLat  = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsLon'.lower():
                ezRAObsLon  = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsAmsl'.lower():
                ezRAObsAmsl = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsName'.lower():
                ezRAObsName = thisLine[1]

            #elif thisLine0Lower == '-ezDecPlotRangeL'.lower():
            #    ezDecPlotRangeL[0] = int(thisLine[1])
            #    ezDecPlotRangeL[1] = int(thisLine[2])

            elif thisLine0Lower == '-ezDecSkyObjectL'.lower():
                # must be a list of skyObjects (without comments), remember it in a string
                #skyObjectL.append(thisLine[1:])
                skyObjectL += thisLine[1:]

            elif thisLine0Lower[:5] == '-ezDec'.lower():
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
                pass    # unrecognized first word, but no error, allows for other ezRA programs

    except (FileNotFoundError, IOError):
    	pass

    else:
        fileDefaults.close()                #   then have processed all available lines in this defaults file



def ezDecArgumentsCommandLine():
    # process arguments from command line

    global dayYYMMDDHHmm                    # string
    global dayHH                            # string
    global skyObjectL                       # list of strings

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    #global ezDecPlotRangeL                 # integer list

    print()
    print('   ezDecArgumentsCommandLine ===============')

    cmdLineSplit = commandString.split()
    cmdLineSplitLen = len(cmdLineSplit)
    #print(' cmdLineSplit =', cmdLineSplit)
        
    # need at least one data directory or file
    if cmdLineSplitLen < 2:
        printUsage()

    cmdLineSplitIndex = 1
    cmdDirectoryS = ''

    while cmdLineSplitIndex < cmdLineSplitLen:

        # be kind, ignore argument keyword capitalization
        cmdLineArgLower = cmdLineSplit[cmdLineSplitIndex].lower()

        if cmdLineArgLower == '-help':
            printUsage()                    # will exit()

        elif cmdLineArgLower == '--help':
            printUsage()                    # will exit()

        elif cmdLineArgLower == '-h':
            printUsage()                    # will exit()

        elif cmdLineArgLower == '--h':
            printUsage()                    # will exit()


        elif 2 <= len(cmdLineArgLower) and cmdLineArgLower[:2] == '-e':

            # Ignoring whitespace, first characters of cmdLineSplit word are '-e'.
            # Not a data directory or file.

            # ezRA arguments used by multiple programs:
            if cmdLineArgLower == '-ezRAObsLat'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezRAObsLat  = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezRAObsLon'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezRAObsLon  = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezRAObsAmsl'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezRAObsAmsl = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezRAObsName'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezRAObsName = cmdLineSplit[cmdLineSplitIndex]   # cmd line allows only one ezRAObsName word

            #elif cmdLineArgLower == '-ezDecPlotRangeL'.lower():
            #    cmdLineSplitIndex += 1
            #    ezDecPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
            #    cmdLineSplitIndex += 1
            #    ezDecPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezDecArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 3 <= len(cmdLineArgLower) and cmdLineArgLower[:3] == '-ex':
                pass

            elif cmdLineArgLower[:7] == '-ezDec'.lower():
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(cmdLineSplit[cmdLineSplitIndex])
                print()
                print()
                print()
                print()
                exit()

            else:
                pass    # unrecognized first word, but no error, allows for other ezRA programs

        # -YYMMDD
        # 01234567
        elif len(cmdLineArgLower) == 7 and cmdLineArgLower[0] == '-':
            dayYYMMDDHHmm = cmdLineArgLower[1:]
            dayHH = ''

        # -YYMMDDHH
        # 0123456789
        elif len(cmdLineArgLower) == 9 and cmdLineArgLower[0] == '-':
            dayYYMMDDHHmm = cmdLineArgLower[1:]
            dayHH = cmdLineArgLower[7:9]

        # -YYMMDDHHmm
        # 012345678901
        elif len(cmdLineArgLower) == 11 and cmdLineArgLower[0] == '-':
            dayYYMMDDHHmm = cmdLineArgLower[1:]
            dayHH = cmdLineArgLower[7:9]

        else:
            # must be a skyObject, remember it in a string
            skyObjectL.append(cmdLineSplit[cmdLineSplitIndex])

        cmdLineSplitIndex += 1



def ezDecArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global dayYYMMDDHHmm                    # string
    global dayHH                            # string
    global dateUTCValue                     # class 'astropy.time.core.Time'
    global datetimeNowUTC                   # time = 2023-11-27 02:44:49.691405
    global skyObjectL                       # list of strings

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    #global ezDecPlotRangeL                 # integer list

    # defaults
    ezRAObsLat  = -999.                 # silly number
    ezRAObsLon  = -999.                 # silly number
    ezRAObsAmsl = -999.                 # silly number
    #ezRAObsName = 'LebanonKS'
    ezRAObsName = ''                    # silly name

    #ezDecPlotRangeL = [0, 9999]        # save this range of plots to file

    dayYYMMDDHHmm  = ''
    dayHH          = ''
    skyObjectL     = []

    # Program argument priority:
    #    Start with the argument value defaults inside the programs.
    #    Then replace those values with any arguments from the ezDefaults.txt in the program's directory.
    #    Then replace values with any arguments from the ezDefaults.txt in the current
    #       directory (where you are standing).
    #    Then replace values (in order) with any arguments from the command line (including
    #       any -ezDefaultsFile).
    #    Each last defined value wins.
    # The top (and bottom ?) of the program printout should list the resultant argument values.
    # Eventually support -ezez argument preface, to allow ignoring.

    # process arguments from ezDefaults.txt file in the same directory as this ezDec program
    ezDecArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezDecArgumentsFile('ezDefaults.txt')

    # process arguments from command line
    ezDecArgumentsCommandLine()

    # sanity tests

    if not len(skyObjectL):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  No sky objects found.')
        print()
        print()
        print()
        print()
        exit()

    # later, len(markerS) is 52
    #if 52 < len(skyObjectL):
    #if 1 < len(skyObjectL):
    if 0:
        print()
        print()
        print()
        print()
        print()
        #print(' ========== FATAL ERROR:  Too many skyObjects.  Limit is 52.')
        print(' ========== FATAL ERROR:  Too many skyObjects.  Limit is 1.')
        print()
        print()
        print()
        print()
        exit()

    # print status
    print()
    print('      ezRAObsName =', ezRAObsName)
    print('      ezRAObsLat  =', ezRAObsLat)
    print('      ezRAObsLon  =', ezRAObsLon)
    print('      ezRAObsAmsl =', ezRAObsAmsl)
    #print()
    #print('      ezDecPlotRangeL =', ezDecPlotRangeL)

    # set UTC day
    if not len(dayYYMMDDHHmm):
        datetimeNowUTC = Time.now()
        #datetimeNowUTC = Time.now(tz=timezone.utc)
        dateUTCValueS = datetimeNowUTC.to_value('fits', subfmt='date')
        #print('     dateUTCValueS =', dateUTCValueS)                   # 2023-11-27
        #                                                               # 01234567890
        dayYYMMDDHHmm = dateUTCValueS[2:4] + dateUTCValueS[5:7] + dateUTCValueS[8:10]

    elif len(dayYYMMDDHHmm) == 6:
        # Time('2000-01-02')
        # dayYYMMDDHHmm
        #    012345678
        datetimeNowUTC = Time('20' + dayYYMMDDHHmm[:2] + '-' + dayYYMMDDHHmm[2:4] + '-' + dayYYMMDDHHmm[4:6], \
            scale='utc')

    elif len(dayYYMMDDHHmm) == 8:
        # Time('2000-01-02 03')
        # dayYYMMDDHHmm
        #    012345678
        datetimeNowUTC = Time('20'+dayYYMMDDHHmm[:2] + '-'+dayYYMMDDHHmm[2:4] + '-'+dayYYMMDDHHmm[4:6] \
            + ' ' + dayYYMMDDHHmm[6:8] + ':00:00', scale='utc')

    elif len(dayYYMMDDHHmm) == 10:
        # Time('2000-01-02')
        # dayYYMMDDHHmm
        #    012345678
        datetimeNowUTC = Time('20'+dayYYMMDDHHmm[:2] + '-'+dayYYMMDDHHmm[2:4] + '-'+dayYYMMDDHHmm[4:6] \
            + ' ' + dayYYMMDDHHmm[6:8] + ':' + dayYYMMDDHHmm[8:10]+ ':00', scale='utc')

    print('\n      dayYYMMDDHHmm =', dayYYMMDDHHmm)
    print('      UTC time   =', datetimeNowUTC)                           # UTC time = 2023-11-27 02:44:49.691405
    #                                                                   #            01234567890

    dateUTCValue = datetimeNowUTC.to_value('mjd', subfmt='decimal')  
    print('      UTC time value =', dateUTCValue)                            #  UTC time value = 60275.12743086809027776018510280664
    #print('type(dateUTCValue) =', type(dateUTCValue))                   # type(dateUTCValue) = <class 'decimal.Decimal'>

    # set to start of UTC day
    #dateUTCValue = int(dateUTCValue)
    print('      UTC date =', int(dateUTCValue))                        # UTC date = 60275

    if ezRAObsLat  < -90. or ezRAObsLon < -180. or ezRAObsAmsl < -990.:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: Observatory location is undefined.')
        print('                         Set ezRAObsLat and ezRAObsLon and ezRAObsAmsl.')
        print()
        print()
        print()
        print()
        exit()



def ezDecPlotPrep():
    # creates azDegL, elDegL, markerSL, and colorSL

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    #global ezDecPlotRangeL                 # integer list
    global dayYYMMDDHHmm                    # string
    global dayHH                            # string
    global programName                      # string
    global titleS                           # string
    global dateUTCValue                     # class 'astropy.time.core.Time'
    global datetimeNowUTC                   # time = 2023-11-27 02:44:49.691405
    global skyObjectL                       # list of strings

    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global raHL                             # list of floats
    global decDegL                          # list of floats
    global gLatDegL                         # list of floats
    global gLonDegL                         # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global hourQty                          # integer

    print()
    print('   ezDecPlotPrep ===============')
    print('\n =================================================')
    print(' =================================================')


    if 0:
        # recorded for each marker
        azDegL   = []       
        elDegL   = []
        raHL     = []       
        decDegL  = []
        gLatDegL = []
        gLonDegL = []
        markerSL = []
        colorSL  = []

        legendSL = []

        # https://matplotlib.org/2.0.2/examples/color/named_colors.html
        # https://www.arrow.com/en/research-and-events/articles/resistor-color-code
        #colorSMenuL = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
        # but remove invisible yellow and white
        colorSMenuL = ['black', 'brown', 'red', 'orange', 'green', 'blue', 'violet', 'grey']
        colorSMenuLen = len(colorSMenuL)
        markerS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'    # length is 52
        #titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + u'           ' + fileObsName \
        #    + '          (' + programName + ')'
        titleS = 'UTC day ' + dayYYMMDDHHmm + '           ' + ezRAObsName \
            + '          (' + programName + ')'

    # telescope Earth location
    from astropy import units as u
    from astropy.coordinates import AltAz, EarthLocation, get_body, SkyCoord
    locBase = EarthLocation(lat = ezRAObsLat*u.deg, lon = ezRAObsLon*u.deg, height = ezRAObsAmsl*u.m)

    timeStampIsRequired = False

    # For each skyObject find pointingTelescopeThis
    for skyObjectIndex in range(len(skyObjectL)):
        #print('skyObjectL =', skyObjectL)
        #print('skyObjectIndex =', skyObjectIndex)
        skyObjectSThis = skyObjectL[skyObjectIndex].lower()

        # GPxPx for GLat (degrees) and GLon (degrees) float numbers
        # 012345
        if 5 <= len(skyObjectSThis) and skyObjectSThis[0] == 'g':
            # parse GLon, starts at gLonIndexSign with p or m
            if 'p' in skyObjectSThis[3:]:
                gLonIndexSign = 3 + skyObjectSThis[3:].index('p')
                gLonDegThis = float(skyObjectSThis[gLonIndexSign + 1:])
            elif 'n' in skyObjectSThis[3:]:
                gLonIndexSign = 3 + skyObjectSThis[3:].index('n')
                gLonDegThis = -float(skyObjectSThis[gLonIndexSign + 1:])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyObjectL[skyObjectIndex])
                print()
                print()
                print()
                print()
                exit()
            # parse GLat, starts at 1 with p or m, ends before gLonIndexSign
            if skyObjectSThis[1] == 'p':
                gLatDegThis = float(skyObjectSThis[2:gLonIndexSign])
            elif skyObjectSThis[1] == 'n':
                gLatDegThis = -float(skyObjectSThis[2:gLonIndexSign])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyObjectL[skyObjectIndex])
                print()
                print()
                print()
                print()
                exit()
            # have gLatDegThis and gLonDegThis, get astropy bearing
            pointingTelescopeThis = SkyCoord(b = gLatDegThis*u.deg, l = gLonDegThis*u.deg,
                frame = 'galactic', location = locBase)

        # RxPx for RightAscension (hours) and Declination (degrees) float numbers
        # 01234
        elif 4 <= len(skyObjectSThis) and skyObjectSThis[0] == 'r':
            # parse Declination, starts at decIndexSign with p or m
            if 'p' in skyObjectSThis[2:]:
                decIndexSign = 2 + skyObjectSThis[2:].index('p')
                decDegThis = float(skyObjectSThis[decIndexSign + 1:])
            elif 'n' in skyObjectSThis[2:]:
                decIndexSign = 2 + skyObjectSThis[2:].index('n')
                decDegThis = -float(skyObjectSThis[decIndexSign + 1:])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyObjectL[skyObjectIndex])
                print()
                print()
                print()
                print()
                exit()
            # parse RightAscension, starts at 1 with value, ends before decIndexSign
            raHThis = float(skyObjectSThis[1:decIndexSign])

            # have RightAscension and Declination, get astropy bearing
            pointingTelescopeThis = SkyCoord(ra = raHThis*u.hour, dec = decDegThis*u.deg,
                frame = 'icrs', location = locBase)

        # AxPx for Azimuth (degrees) and Elevation (degrees) float numbers
        # 01234
        elif 4 <= len(skyObjectSThis) and skyObjectSThis[0] == 'a':
            # parse Elevation, starts at decIndexSign with p or m
            if 'p' in skyObjectSThis[2:]:
                elIndexSign = 2 + skyObjectSThis[2:].index('p')
                elDegThis = float(skyObjectSThis[elIndexSign + 1:])
            elif 'n' in skyObjectSThis[2:]:
                elIndexSign = 2 + skyObjectSThis[2:].index('n')
                elDegThis = -float(skyObjectSThis[elIndexSign + 1:])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyObjectL[skyObjectIndex])
                print()
                print()
                print()
                print()
                exit()
            # parse Azimuth, starts at 1 with value, ends before elIndexSign
            azDegThis = float(skyObjectSThis[1:elIndexSign])

            # have Azimuth and Elevation, get astropy bearing
            datetimeUTCValue = Time(dateUTCValue, format='mjd')
            pointingTelescopeThis = SkyCoord(az = azDegThis*u.deg, alt = elDegThis*u.deg,
                frame = 'altaz', location = locBase, obstime = datetimeUTCValue)
            timeStampIsRequired = True

        # Moon
        # 01234
        elif skyObjectSThis == 'moon':
            # special case because Moon moves across the sky
            datetimeUTCValue = Time(dateUTCValue, format='mjd')
            pointingTelescopeThis = get_body('moon', datetimeUTCValue)
            timeStampIsRequired = True

        # Sun
        # 0123
        elif skyObjectSThis == 'sun':
            # special case because Sun moves across the sky
            datetimeUTCValue = Time(dateUTCValue, format='mjd')
            pointingTelescopeThis = get_body('sun', datetimeUTCValue)
            timeStampIsRequired = True

        else:
            print()
            print()
            print()
            print()
            print()
            print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
            print(skyObjectL[skyObjectIndex])
            print()
            print()
            print()
            print()
            exit()

        # now have pointingTelescopeThis

        if 0:
            # create and almost print gLonDegDecHDegP180Left[]
            gLonDegDecHDegP180Left = np.full(360, -200.)  # silly gLonDeg value
            for decHDeg in range(-180, 180):
                # start left Galactic plane crossing search with a RaDec
                raHThis = 19.
                decDegThis = decHDeg / 2.
                print('\n decHDeg =', decHDeg)
                pointingTelescopeThis = SkyCoord(ra = raHThis*u.hour, dec = decDegThis*u.deg,
                    frame = 'icrs', location = locBase)

                raHStepThis = 3.
                for i in range(15):
                    print('\n i =', i, '  raHStepThis =', raHStepThis)

                    # extract Gal coordinates
                    #print(' pointingTelescopeThis.galactic =', pointingTelescopeThis.galactic)
                    gLatDeg = float(pointingTelescopeThis.galactic.b.degree)
                    #gLatDeg = float(azEl.galactic.b.degree)
                    #print(' gLatDeg =', gLatDeg, 'degrees')
                    gLonDeg = float(pointingTelescopeThis.galactic.l.degree)
                    #gLonDeg = float(azEl.galactic.l.degree)
                    if 180. < gLonDeg:
                        gLonDeg -= 360.
                    #print(' gLonDeg =', gLonDeg, 'degrees')
                    print(' gLonDeg =', gLonDeg, '   gLatDeg =', gLatDeg)

                    # with same Dec, move closer to left Galactic plane crossing
                    if 0. < gLatDeg:
                        raHThis += raHStepThis
                    else:
                        raHThis -= raHStepThis

                    pointingTelescopeThis = SkyCoord(ra = raHThis*u.hour, dec = decDegThis*u.deg,
                        frame = 'icrs', location = locBase)

                    raHStepThis /= 2.

                if abs(gLatDeg) < 0.5:
                    gLonDegDecHDegP180Left[decHDeg + 180] = gLonDeg

                print(' gLonDegDecHDegP180Left =', gLonDegDecHDegP180Left)
                print(' gLonDegDecHDegP180Left.tolist() =', gLonDegDecHDegP180Left.tolist())

        gLonDegDecHDegP180Left = np.array([-200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -56.09398195983465, -52.3782994690489, -49.85824859345013, -47.981141923703206, -46.404495435645856, -45.012626660118144, -43.7434453312747, -42.564104370667565, -41.461293074741945, -40.41134443243902, -39.41038973142224, -38.44436209197073, -37.514085964943376, -36.61526722716417, -35.73851464789402, -34.88939334798653, -34.05336999488139, -33.2358990394859, -32.437381599506864, -31.653172236945466, -30.878592966633505, -30.118956437053498, -29.3695314287026, -28.630574039734654, -27.90232075552234, -27.17998090747477, -26.468767198800606, -25.76385892752137, -25.06042247142028, -24.368641346152515, -23.683659713445707, -23.005621697918457, -22.329652744854798, -21.66088960111142, -20.994442082792432, -20.335432623668737, -19.67895779178417, -19.025118060574016, -18.379018170882773, -17.730728643339262, -17.090354066294367, -16.45296574339784, -15.8186404871214, -15.18745133071252, -14.55946777805599, -13.929746345157014, -13.308369251815407, -12.68537762533498, -12.070847970265618, -11.449806302874833, -10.837333817461513, -10.223461748144985, -9.61825701389347, -9.00673690717258, -8.403974490800806, -7.794983092960308, -7.1948320863895106, -6.593541448322696, -5.9961582448116815, -5.397708742741997, -4.798227743799316, -4.2027582357796405, -3.611332270514481, -3.018971366925939, -2.4257054029819756, -1.8365726875244377, -1.246591632084744, -0.6607984796854112, -0.07420983267036263, 0.5081395910971965, 1.0962449128973173, 1.6800631927852598, 2.259571778052364, 2.844767675309405, 3.420600858302356, 4.002079377879794, 4.584173292028287, 5.161853722693181, 5.735101544776292, 6.313917631555063, 6.888264685378644, 7.4631349800650675, 8.0385115758199, 8.614377874342523, 9.185708183366785, 9.757496402375873, 10.329727297616753, 10.9023859284114, 11.475457646160375, 12.043918676996118, 12.61276465270442, 13.181982040542893, 13.751557551012088, 14.321478135497888, 14.89173098352378, 15.457294104111897, 16.023164745550858, 16.594340590703087, 17.160790624949254, 17.727512841854505, 18.28948633671503, 18.856719074650844, 19.42419041176378, 19.986880057260663, 20.549786814491686, 21.117909876741034, 21.68121966716809, 22.244715549398748, 22.80838744887289, 23.37222540765752, 23.936219579323197, 24.500360223639476, 25.059628143013754, 25.624032972774554, 26.188555636520743, 26.74817721112964, 27.312907565890306, 27.872718285536152, 28.43761939528908, 28.997582593466216, 29.562617989054026, 30.122697400795396, 30.682821406403075, 31.24799065392254, 31.808177029523662, 32.3683812021709, 32.933603861751614, 33.493816932548825, 34.05402110769305, 34.619217070544146, 35.17937672526543, 35.739500739525084, 36.30458973116403, 36.86461554046009, 37.429588338356005, 37.989479842791425, 38.55430017424037, 39.114020917980284, 39.67865209041482, 40.238165170447765, 40.80256997747663, 41.36684749307592, 41.93098817019502, 42.48997274816801, 43.05381070282308, 43.61748260514837, 44.18097849882999, 44.749297853059176, 45.31241129184493, 45.87531809194983, 46.443017291850566, 47.005479080235055, 47.57271177554018, 48.13969484839675, 48.706417090370294, 49.27286711391942, 49.839033348273446, 50.40490403560761, 50.9754767515288, 51.54072000862524, 52.110640548539145, 52.68021603986122, 53.24943343711299, 53.81827945398973, 54.39175012250064, 54.959812201910594, 55.53247078975714, 56.10470167960454, 56.676489934488856, 57.247820324417205, 57.82368654256713, 58.39906310362666, 58.97393341346402, 59.548280536490296, 60.12709652705153, 60.70535398130493, 61.28303436647178, 61.86011876112385, 62.4415972012145, 63.02243998136154, 63.60262633506519, 64.18714453380083, 64.7709628553634, 65.35405846204502, 65.9364080385663, 66.52299668002756, 67.11379929936332, 67.70378048832929, 68.29291312580044, 68.88116952068683, 69.47353042478125, 70.06996594788512, 70.66543550131797, 71.25990683432651, 71.85835630867813, 72.45573962420349, 73.05703024964237, 73.6621907547419, 74.26617254457344, 74.87394469284972, 75.48045506725113, 76.09066938317484, 76.69953203296149, 77.31701395848978, 77.93304601798651, 78.55258535084437, 79.17056741530007, 79.79695405347064, 80.42166586160995, 81.04964946248471, 81.68083864843325, 82.31516392695067, 82.9525522767558, 83.59793639941904, 84.24121623135271, 84.88731624086734, 85.54115588465186, 86.1976307055354, 86.85664024570774, 87.52308769330777, 88.19185089536755, 88.86781979780335, 89.54585793191515, 90.23584904152892, 90.92763012095736, 91.62605699368889, 92.33096530629766, 93.04217911088395, 93.7645189073067, 94.49778181088979, 95.23673917314466, 95.98616418813118, 96.74580065609666, 97.51537039855229, 98.30458938279186, 99.1031067154845, 99.91556818266412, 100.75159143258158, 101.60572235913979, 102.47746540791113, 103.3812936549756, 104.31156984135932, 105.2725878336406, 106.27354257054114, 107.32349118248547, 108.43131211884504, 109.60564345918418, 110.87482478310866, 112.26669359607018, 113.84334006327373, 115.7204467158203, 118.24550718797097, 123.90103309220859, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0])

        gLonDegDecHDegP180LeftMaskValid = -200. < gLonDegDecHDegP180Left

        if 0:
            # print and plot gLonDegDecHDegP180Left[]
            print('\n gLonDegDecHDegP180Left =', gLonDegDecHDegP180Left)

            plt.clf()
            plt.plot(gLonDegDecHDegP180Left)
            plt.title('gLonDegDecHDegP180Left')
            plt.xlabel('decHDegP180 (Half Degrees)')
            plt.ylabel('gLonDegDecHDegP180Left (Degrees)')
            plt.savefig('ezDec-gLonDegDecHDegP180Left.png', dpi=300, bbox_inches='tight')

            # Max and Min GLon of Galactic plane crossings
            gLonDegDecHDegP180LeftValid = gLonDegDecHDegP180Left[gLonDegDecHDegP180LeftMaskValid]
            print('\n Left Galactic plane crossings Max GLon =', gLonDegDecHDegP180LeftValid.max())
            print(' Left Galactic plane crossings Min GLon =', gLonDegDecHDegP180LeftValid.min())
            
            # Max and Min Dec of Galactic plane crossings
            #print('\n gLonDegDecHDegP180LeftMaskValid =', gLonDegDecHDegP180LeftMaskValid)
            print(' Left Galactic plane crossings Max Dec =', \
                90 - gLonDegDecHDegP180LeftMaskValid[::-1].argmax() / 2.)
            print(' Left Galactic plane crossings Min Dec =', \
                -90 + gLonDegDecHDegP180LeftMaskValid.argmax() / 2.)
        

        if 0:
            # create and almost print gLonDegDecHDegP180Right[]
            gLonDegDecHDegP180Right = np.full(360, -200.)  # silly gLonDeg value
            for decHDeg in range(-180, 180):
                # start right Galactic plane crossing search with a RaDec
                raHThis = 7.
                decDegThis = decHDeg / 2.
                print('\n decHDeg =', decHDeg)
                pointingTelescopeThis = SkyCoord(ra = raHThis*u.hour, dec = decDegThis*u.deg,
                    frame = 'icrs', location = locBase)

                raHStepThis = 3.
                for i in range(15):
                    print('\n i =', i, '  raHStepThis =', raHStepThis)

                    # extract Gal coordinates
                    #print(' pointingTelescopeThis.galactic =', pointingTelescopeThis.galactic)
                    gLatDeg = float(pointingTelescopeThis.galactic.b.degree)
                    #gLatDeg = float(azEl.galactic.b.degree)
                    #print(' gLatDeg =', gLatDeg, 'degrees')
                    gLonDeg = float(pointingTelescopeThis.galactic.l.degree)
                    #gLonDeg = float(azEl.galactic.l.degree)
                    if 180. < gLonDeg:
                        gLonDeg -= 360.
                    #print(' gLonDeg =', gLonDeg, 'degrees')
                    print(' gLonDeg =', gLonDeg, '   gLatDeg =', gLatDeg)

                    # with same Dec, move closer to right Galactic plane crossing
                    if 0. < gLatDeg:
                        raHThis -= raHStepThis
                    else:
                        raHThis += raHStepThis

                    pointingTelescopeThis = SkyCoord(ra = raHThis*u.hour, dec = decDegThis*u.deg,
                        frame = 'icrs', location = locBase)

                    raHStepThis /= 2.

                if abs(gLatDeg) < 0.5:
                    gLonDegDecHDegP180Right[decHDeg + 180] = gLonDeg

                print(' gLonDegDecHDegP180Right =', gLonDegDecHDegP180Right)
                print(' gLonDegDecHDegP180Right.tolist() =', gLonDegDecHDegP180Right.tolist())

        gLonDegDecHDegP180Right = np.array([-200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -56.09896690779141, -61.754492812029014, -64.27955328417966, -66.15665993672627, -67.73330640392982, -69.12517521689131, -70.39435654081586, -71.56868788115497, -72.6765088175145, -73.72645742945883, -74.72741216635939, -75.68843015864064, -76.61870634502435, -77.52253459208885, -78.3942776408602, -79.24840856741844, -80.08443181733583, -80.8968932845155, -81.6954106172081, -82.4846296014477, -83.25419934390334, -84.01383581186883, -84.76326082685534, -85.50221818911018, -86.2354810926933, -86.95782088911602, -87.66903469370237, -88.3739430063111, -89.07236987904258, -89.76415095847108, -90.45414206808488, -91.1321802021966, -91.80814910463243, -92.47691230669221, -93.1433597542923, -93.8023692944646, -94.45884411534814, -95.11268375913266, -95.75878376864722, -96.40206360058096, -97.0474477232442, -97.68483607304938, -98.31916135156672, -98.9503505375153, -99.57833413839006, -100.20304594652936, -100.82943258469993, -101.44741464915563, -102.06695398201344, -102.68298604151022, -103.30046796703851, -103.90933061682512, -104.51954493274886, -105.12605530715032, -105.73382745542656, -106.33780924525809, -106.94296975035766, -107.54426037579651, -108.14164369132186, -108.74009316567344, -109.33456449868203, -109.93003405211485, -110.52646957521873, -111.11883047931317, -111.70708687419958, -112.29621951167073, -112.88620070063669, -113.4770033199724, -114.0635919614337, -114.645941537955, -115.2290371446366, -115.81285546619918, -116.3973736649348, -116.97756001863843, -117.55840279878552, -118.13988123887614, -118.71696563352819, -119.29464601869506, -119.87290347294842, -120.4517194635097, -121.02606658653593, -121.60093689637333, -122.17631345743285, -122.75217967558277, -123.32351006551113, -123.89529832039545, -124.46752921024282, -125.04018779808942, -125.60824987749936, -126.18172054601027, -126.750566562887, -127.31978396013878, -127.88935945146082, -128.45927999137476, -129.02452324847116, -129.59509596439239, -130.16096665172654, -130.72713288608057, -131.2935829096297, -131.86030515160323, -132.4272882244598, -132.9945209197649, -133.55698270814943, -134.12468190805015, -134.68758870815506, -135.2507021469408, -135.81902150117, -136.38251739485162, -136.94618929717691, -137.51002725183196, -138.06901182980496, -138.63315250692406, -139.19743002252335, -139.76183482955224, -140.32134790958517, -140.8859790820197, -141.44569982575962, -142.01052015720856, -142.570411661644, -143.1353844595399, -143.69541026883596, -144.26049926047492, -144.82062327473454, -145.38078292945585, -145.94597889230695, -146.5061830674512, -147.06639613824836, -147.6316187978291, -148.19182297047632, -148.75200934607747, -149.3171785935969, -149.8773025992046, -150.43738201094595, -151.00241740653377, -151.56238060471094, -152.12728171446383, -152.68709243410967, -153.25182278887038, -153.8114443634792, -154.37596702722544, -154.94037185698625, -155.49963977636048, -156.06378042067678, -156.6277745923425, -157.19161255112712, -157.75528445060127, -158.3187803328319, -158.88209012325896, -159.45021318550832, -160.0131199427393, -160.5758095882362, -161.14328092534916, -161.71051366328498, -162.2724871581455, -162.83920937505076, -163.4056594092969, -163.97683525444913, -164.54270589588808, -165.1082690164762, -165.6785218645021, -166.24844244898787, -166.81801795945708, -167.3872353472956, -167.9560813230039, -168.52454235383962, -169.0976140715886, -169.67027270238322, -170.2425035976241, -170.81429181663322, -171.38562212565748, -171.9614884241801, -172.53686501993494, -173.1117353146213, -173.68608236844494, -174.2648984552237, -174.8381462773068, -175.41582670797172, -175.9979206221202, -176.57939914169762, -177.1552323246906, -177.74042822194764, -178.3199368072147, -178.90375508710267, -179.49186040890277, 179.9257901673297, 179.33920152031465, 178.7534083679153, 178.1634273124756, 177.57429459701808, 176.9810286330741, 176.38866772948552, 175.79724176422033, 175.2017722562007, 174.6022912572581, 174.00384175518835, 173.40645855167733, 172.80516791361052, 172.20501690703972, 171.59602550919928, 170.99326309282742, 170.3817429861066, 169.77653825185504, 169.16266618253854, 168.55019369712517, 167.92915202973438, 167.314622374665, 166.69163074818468, 166.070253654843, 165.440532221944, 164.8125486692875, 164.1813595128786, 163.5470342566022, 162.9096459337057, 162.2692713566608, 161.62098182911728, 160.97488193942604, 160.3210422082159, 159.6645673763313, 159.00555791720762, 158.3391103988886, 157.6703472551452, 156.99437830208157, 156.31634028655435, 155.63135865384754, 154.9395775285797, 154.23614107247863, 153.5312328011994, 152.82001909252526, 152.09767924447766, 151.36942596026535, 150.63046857129743, 149.88104356294653, 149.12140703336655, 148.34682776305453, 147.5626184004932, 146.76410096051413, 145.9466300051186, 145.11060665201353, 144.26148535210598, 143.38473277283583, 142.48591403505668, 141.55563790802927, 140.5896102685778, 139.588655567561, 138.53870692525808, 137.4358956293325, 136.25655466872533, 134.98737333988188, 133.59550456435414, 132.01885807629682, 130.1417514065499, 127.62170053095112, 123.90601804016532, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0, -200.0])

        gLonDegDecHDegP180RightMaskValid = -200. < gLonDegDecHDegP180Right

        if 0:
            # print and plot gLonDegDecHDegP180Right[]
            print('\n gLonDegDecHDegP180Right =', gLonDegDecHDegP180Right)

            plt.clf()
            plt.plot(gLonDegDecHDegP180Right)
            plt.title('gLonDegDecHDegP180Right')
            plt.xlabel('decHDegP180 (Half Degrees)')
            plt.ylabel('gLonDegDecHDegP180Right (Degrees)')
            plt.savefig('ezDec-gLonDegDecHDegP180Right.png', dpi=300, bbox_inches='tight')

            # Max and Min GLon of Right Galactic plane crossings
            gLonDegDecHDegP180RightValid = gLonDegDecHDegP180Right[gLonDegDecHDegP180RightMaskValid]
            print('\n Right Galactic plane crossings Max GLon =', gLonDegDecHDegP180RightValid.max())
            print(' Right Galactic plane crossings Min GLon =', gLonDegDecHDegP180RightValid.min())
            
            # Max and Min Dec of Right Galactic plane crossings
            #print('\n gLonDegDecHDegP180RightMaskValid =', gLonDegDecHDegP180RightMaskValid)
            print(' Right Galactic plane crossings Max Dec =', \
                90 - gLonDegDecHDegP180RightMaskValid[::-1].argmax() / 2.)
            print(' Right Galactic plane crossings Min Dec =', \
                -90 + gLonDegDecHDegP180RightMaskValid.argmax() / 2.)

        if 0:
            # print Left GLon and Right GLon By Dec
            print('\n   Declination (Degrees), Left Galactic Longitude (Degrees), ' \
                + 'Right Galactic Longitude (Degrees)\n')
            for decHDegP180 in reversed(range(0, 360)):
                print(f'{(decHDegP180 - 180.)/ 2.:6.1f}      ' \
                    + f'{gLonDegDecHDegP180Left[decHDegP180]:6.1f}     ' \
                    + f'{gLonDegDecHDegP180Right[decHDegP180]:6.1f}')


        print('\n for', skyObjectSThis)
        #if 0:
        if timeStampIsRequired:
            # extract AxEl coordinates

            if 0:
                #azDeg = float(azEl.altaz.az.degree)
                azDeg = float(pointingTelescopeThis.altaz.az.degree)
                print('\n     Azimuth =', azDeg, 'degrees')
                #elDeg = float(azEl.altaz.alt.degree)
                elDeg = float(pointingTelescopeThis.altaz.alt.degree)
                print('     Elevation =', elDeg, 'degrees')

            azEl = pointingTelescopeThis.transform_to(AltAz(obstime=datetimeUTCValue, location=locBase))
            #print(' azEl =', azEl)
            azDeg = float(azEl.altaz.az.degree)
            #print(' azDeg =', azDeg)
            print('\n     Azimuth =', azDeg, 'degrees')
            elDeg = float(azEl.altaz.alt.degree)
            #print(' elDeg =', elDeg)
            print('     Elevation =', elDeg, 'degrees')


        # extract Gal coordinates
        #print(' pointingTelescopeThis.galactic =', pointingTelescopeThis.galactic)
        gLatDeg = float(pointingTelescopeThis.galactic.b.degree)
        #gLatDeg = float(azEl.galactic.b.degree)
        #print(' gLatDeg =', gLatDeg, 'degrees')
        print('\n     Galactic Latitude  =', gLatDeg, 'degrees')
        gLonDeg = float(pointingTelescopeThis.galactic.l.degree)
        #gLonDeg = float(azEl.galactic.l.degree)
        if 180. < gLonDeg:
            gLonDeg -= 360.
        #print(' gLonDeg =', gLonDeg, 'degrees')
        print('     Galactic Longitude =', gLonDeg, 'degrees')

        raH = float(pointingTelescopeThis.gcrs.ra.hour)
            #print(' raH =', raH, 'Hours')
        print('\n     RightAscension =', raH, 'hours')
        decDeg = float(pointingTelescopeThis.gcrs.dec.degree)
        #print(' decDeg =', decDeg, 'degrees')
        print('     Declination    =', decDeg, 'degrees')

        # for decDeg half degree, look up the Galactic plane crossings
        decHDegP180 = int(decDeg * 2 + 180.5) 
        #print(' decHDegP180 =', decHDegP180)

        #print(' gLonDegDecHDegP180Left[decHDegP180] =', gLonDegDecHDegP180Left[decHDegP180], 'degrees')
        #print(' gLonDegDecHDegP180Right[decHDegP180] =', gLonDegDecHDegP180Right[decHDegP180], 'degrees')
        gLonDegDecHDegP180LeftCrossing = gLonDegDecHDegP180Left[decHDegP180]
        if -200. < gLonDegDecHDegP180LeftCrossing:
            print('\n     Drift-scan Left  Galactic plane crossing =', \
                gLonDegDecHDegP180LeftCrossing, 'Galactic Longitude (degrees)')
        else:
            print('\n     Drift-scan Left  Galactic plane crossing = NONE')
            
        gLonDegDecHDegP180RightCrossing = gLonDegDecHDegP180Right[decHDegP180]
        if -200. < gLonDegDecHDegP180RightCrossing:
            print('     Drift-scan Right Galactic plane crossing =', \
                gLonDegDecHDegP180RightCrossing, 'Galactic Longitude (degrees)')
        else:
            print('     Drift-scan Right Galactic plane crossing = NONE')

        print('\n =================================================')


def main():

    #global ezRAObsLat                       # float
    #global ezRAObsLon                       # float
    #global ezRAObsAmsl                      # float
    #global ezRAObsName                      # string
    #global ezDecPlotRangeL                  # integer list

    #global dayYYMMDDHHmm                    # string
    #global dateUTCValue                     # class 'astropy.time.core.Time'
    #global skyObjectL                       # list of strings


    printHello()

    ezDecArguments()

    ezDecPlotPrep()

    #ezWhen030azEl()     # AzEl plot
    #ezWhen050raDec()    # RaDec plot
    #ezWhen080gal()      # Galactic plot

    #ezWhen110azElS()    # AzEl South plot
    #ezWhen120azElN()    # AzEl North plot

    #ezWhen210azElDS()   # AzEl Dome South plot
    #ezWhen220azElDN()   # AzEl Dome North plot

    #ezWhen300azElPZ()   # AzEl Polar Zenith plot

    print(f'\n programRevision = {programRevision}')
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



if __name__== '__main__':
  main()

# a@u22-221222a:~/aaaEzRABase/ezWhen$ 
#   python3 ../ezRA/ezWhen240113a.py  Gm0p0  -exR3p10 Gp40p0 Gp80p0 R0p60
#   python3  ../ezRA/ezWhen240117b.py  sun  Moon  R0P60  GP0P0  Gp80p10  Gp80m10  -240317  -ezWhenPlotRangeL 0 210
#   python3 ../ezRA/ezWhen240307c.py   -240307  -ezWhenPlotRangeL 0 99 gp0p0 gp0p20 gp0p40 gp0p60 gp0p80 gp0p100 gp0p120 gp0p140 gp0p160 gp0p180
#   -ezWhenSkyObjectL gp0p0 gp0p20 gp0p40 gp0p60 gp0p80 gp0p100 gp0p120 gp0p140 gp0p160 gp0p180

# py  ..\..\ezDec250730g.py  A45P40
# py  ..\..\ezDec250730k.py      A180P45 -2401170523 moon sun
# 4 humps = py  ..\..\ezDec250730k.py  Gp0n123

