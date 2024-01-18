programName = 'ezWhen240118a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezWhen sky object visibility projection program,
#   to plot Sun, Moon, Galactic and/or RaDec coordinates onto AzEl coordinates
#   for each hour of one UTC day.
#   To answer, WHEN is that sky object visible ?
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

# ezWhen240118a, ezWhen220 typo, sanity tests for ezRAObsLat, ezRAObsLon, ezRAObsAmsl
# ezWhen240117b, -ezWhenPlotL
# ezWhen240117a, Sun, Moon, legend colors, xlabels, ylabels
# ezWhen240115d, legends
# ezWhen240115c, renamed to ezWhen100azEl, ezWhen110azElS, ezWhen120azElN,
#   ezWhen210azElDS, ezWhen220azElDN, ezWhen300azElPZ
# ezWhen240115b, ezWhen210azElPS
# ezWhen240115a, ezWhen210azElPS
# ezWhen240114b, ezWhen210azElPS
# ezWhen240114a, ezWhen200azElPZ looks good ?
# ezWhen240113a, main() reorganized, ezWhen100azEl looks good ?
# ezWhen240110a,
# ezWhen231126h, azEl polar plot with dated title and filename, buggy
# ezWhen231126g, azEl plot with dated title and filename
# ezWhen231126f, first azEl plot
# ezWhen231126e, converts each UTC hour and each coordinate to Az and El
# ezWhen231126d, loops on sky coordinates
# ezWhen231126c, reads command line date
# ezWhen231126b, reads command line sky coordinates
# ezWhen231126a,
# ezWhen231125a, no astroplan, new start with astropy
# ezWhen231009c,
# ezWhen231009b,
# ezWhen231009a,

import matplotlib.pyplot as plt
#from matplotlib import cm

#from astropy.time import Time

## use astropy
#from astropy import units as u
#from astropy.coordinates import EarthLocation
#from astropy.coordinates import SkyCoord

import sys
import os


def printUsage():

    global programRevision          # string

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezWhen.py [optional arguments]')
    print('  Linux:     python3 ezWhen.py [optional arguments]')
    print()
    print('  Easy Radio Astronomy (ezRA) ezWhen sky object visibility projection program,')
    print('     to plot Sun, Moon, Galactic and/or RaDec coordinates onto AzEl coordinates')
    print('     for each hour of one UTC day.')
    print('     To answer, WHEN is that sky object visible ?')
    print()
    print('  Arguments may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezWhen program,')
    print("  then in order from the ezDefaults.txt in the ezWhen.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  py ezWhen.py -help                  (print this help)')
    print('  py ezWhen.py -h                     (print this help)')
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
    print('     Below uses "P" for Plus, and "M" for Minus.')
    print()
    print('     Galactic coordinates:')
    print('         GPx.xPx.x       where x.x are GLongitude (degrees) and GLatitude (degrees) float numbers')
    print('         GP0P0           Galactic center')
    print('         GP123.4P56.7    GLon=+123.4 and GLat=+56.7')
    print('         GM123.4M56.7    GLon=-123.4 and GLat=-56.7')
    print('         GM123M56        GLon=-123   and GLat=-56')
    print()
    print('     RaDec coordinates:')
    print('         Rx.xPx.x        where x.x are RightAscension (hours) and Declination (degrees) float numbers')
    print('         R2.53P89.26     Polaris star')
    print('         R17.76M29       Galactic center')
    print('         R12.3P56.7      RA=12.3 and Dec=+56.7')
    print('         R12.3M56.7      RA=12.3 and Dec=-56.7')
    print('         R12M56          RA=12   and Dec=-56')
    print()
    print('     If not the current UTC day, enter the UTC day (Year, Month, Day):')
    print('         -YYMMDD')
    print()
    print('    -ezWhenPlotRangeL    0  100    (save only this range of ezWhen plots to file, to save time)')
    print()
    print('    -ezDefaultsFile ../bigDish8.txt     (additional file of ezRA arguments)')
    print()
    print('    -eXXXXXXXXXXXXXXzIgonoreThisWholeOneWord')
    print('         (any one word starting with -eX is ignored, handy for long command line editing)')
    print()
    print()
    print('EXAMPLE:  py  ../ezRA/ezWhen.py  sun  Moon  R0P60  GP0P0  Gp80m10  -240117')
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
    print('            ezWhen.py -help')

    print()
    print('=================================================')
    ###############################################print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezConArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezWhenPlotRangeL                 # integer list

    print()
    print('   ezConArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

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

            elif thisLine0Lower == '-ezWhenPlotRangeL'.lower():
                ezWhenPlotRangeL[0] = int(thisLine[1])
                ezWhenPlotRangeL[1] = int(thisLine[2])

            elif thisLine0Lower[:5] == '-ezWhen'.lower():
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



def ezConArgumentsCommandLine():
    # process arguments from command line

    global dayYYMMDD                        # string
    global skyCoordinateSL                  # list of strings

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezWhenPlotRangeL                 # integer list

    print()
    print('   ezConArgumentsCommandLine ===============')

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

            elif cmdLineArgLower == '-ezWhenPlotRangeL'.lower():
                cmdLineSplitIndex += 1
                ezWhenPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezWhenPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                ezWhenArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 3 <= len(cmdLineArgLower) and cmdLineArgLower[:3] == '-ex':
                pass

            elif cmdLineArgLower[:7] == '-ezWhen'.lower():
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
            dayYYMMDD = cmdLineArgLower[1:]

        else:
            # must be a skyCoordinate, remember it in a string
            skyCoordinateSL.append(cmdLineSplit[cmdLineSplitIndex])

        cmdLineSplitIndex += 1



def ezConArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global dayYYMMDD                        # string
    global dateUTCValue                     # class 'astropy.time.core.Time'
    global skyCoordinateSL                  # list of strings

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezWhenPlotRangeL                 # integer list

    # defaults
    ezRAObsLat  = -999.                 # silly number
    ezRAObsLon  = -999.                 # silly number
    ezRAObsAmsl = -999.                 # silly number
    #ezRAObsName = 'LebanonKS'
    ezRAObsName = ''                    # silly name

    ezWhenPlotRangeL = [0, 9999]        # save this range of plots to file

    dayYYMMDD       = ''
    skyCoordinateSL = []

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

    # process arguments from ezDefaults.txt file in the same directory as this ezCon program
    ezConArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezConArgumentsFile('ezDefaults.txt')

    # process arguments from command line
    ezConArgumentsCommandLine()

    # sanity tests

    # later, len(markerS) is 52
    if 52 < len(skyCoordinateSL):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Too many skyCoordinates.  Limit is 52.')
        print()
        print()
        print()
        print()
        exit()

    from astropy.time import Time

    # set UTC day
    if not len(dayYYMMDD):
        datetimeNowUTC = Time.now()
        dateUTCValueS = datetimeNowUTC.to_value('fits', subfmt='date')
        #print('     dateUTCValueS =', dateUTCValueS)                        # 2023-11-27
        #                                                               # 01234567890
        dayYYMMDD = dateUTCValueS[2:4] + dateUTCValueS[5:7] + dateUTCValueS[8:10]
    else:
        # Time('2000-01-02')
        # dayYYMMDD
        #    0123456
        datetimeNowUTC = Time('20' + dayYYMMDD[:2] + '-' + dayYYMMDD[2:4] + '-' + dayYYMMDD[4:6])

    print('      dayYYMMDD =', dayYYMMDD)
    print('      UTC time =', datetimeNowUTC)                              # UTC time = 2023-11-27 02:44:49.691405
    #                                                                   #            01234567890

    dateUTCValue = datetimeNowUTC.to_value('mjd', subfmt='decimal')  
    print('      UTC time value =', dateUTCValue)                            #  UTC time value = 60275.12743086809027776018510280664
    #print('type(dateUTCValue) =', type(dateUTCValue))                   # type(dateUTCValue) = <class 'decimal.Decimal'>

    # set to start of UTC day
    dateUTCValue = int(dateUTCValue)
    print('      UTC date =', dateUTCValue)                                  # UTC date = 60275

    # print status
    print()
    print('      ezRAObsName =', ezRAObsName)
    print('      ezRAObsLat  =', ezRAObsLat)
    print('      ezRAObsLon  =', ezRAObsLon)
    print('      ezRAObsAmsl =', ezRAObsAmsl)
    print()
    print('      ezWhenPlotRangeL =', ezWhenPlotRangeL)

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



def plotPrep():
    # creates azDegL, elDegL, markerSL, and colorSL

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezWhenPlotRangeL                 # integer list
    global dayYYMMDD                        # string
    global programName                      # string
    global titleS                           # string
    global dateUTCValue                     # class 'astropy.time.core.Time'
    global skyCoordinateSL                  # list of strings

    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings

    # use astropy
    from astropy import units as u
    #from astropy.coordinates import EarthLocation
    #from astropy.coordinates import SkyCoord
    from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun, get_body
    from astropy.time import Time

    # recorded for each marker
    azDegL   = []       
    elDegL   = []
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
    #titleS = 'UTC day ' + dayYYMMDD + u'           ' + ezRAObsName \
    #    + '          (' + programName + ')'
    titleS = 'UTC day ' + dayYYMMDD + '           ' + ezRAObsName \
        + '          (' + programName + ')'

    # telescope Earth location
    locBase = EarthLocation(lat = ezRAObsLat*u.deg, lon = ezRAObsLon*u.deg, height = ezRAObsAmsl*u.m)

    # For each SkyCoordinate find pointingTelescopeThis
    for skyCoordinateIndex in range(len(skyCoordinateSL)):
        #print('skyCoordinateIndex =', skyCoordinateIndex)
        skyCoordinateSThis = skyCoordinateSL[skyCoordinateIndex].lower()

        # GPxPx for GLon (degrees) and GLat (degrees) float numbers
        # 012345
        if 5 <= len(skyCoordinateSThis) and skyCoordinateSThis[0] == 'g':
            # parse GLat, starts at gLatIndexSign with p or m
            if 'p' in skyCoordinateSThis[3:]:
                gLatIndexSign = 3 + skyCoordinateSThis[3:].index('p')
                gLatDegThis = float(skyCoordinateSThis[gLatIndexSign + 1:])
            elif 'm' in skyCoordinateSThis[3:]:
                gLatIndexSign = 3 + skyCoordinateSThis[3:].index('m')
                gLatDegThis = -float(skyCoordinateSThis[gLatIndexSign + 1:])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyCoordinateSL[skyCoordinateIndex])
                print()
                print()
                print()
                print()
                exit()
            # parse GLon, starts at 1 with p or m, ends before gLatIndexSign
            if skyCoordinateSThis[1] == 'p':
                gLonDegThis = float(skyCoordinateSThis[2:gLatIndexSign])
            elif skyCoordinateSThis[1] == 'm':
                gLonDegThis = -float(skyCoordinateSThis[2:gLatIndexSign])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyCoordinateSL[skyCoordinateIndex])
                print()
                print()
                print()
                print()
                exit()
            # have gLonDegThis and gLatDegThis, get astropy bearing
            pointingTelescopeThis = SkyCoord(l = gLonDegThis*u.deg, b = gLatDegThis*u.deg,
                frame = 'galactic', location = locBase)

            ## extract RaDec coordinates
            #raDegThis = float(pointingTelescope.icrs.ra.degree)
            #raHrThis = raDegThis / 15.       # 24 / 360 = 1 / 15
            ##print(' raHrThis =', raHrThis, 'Hours')
            #decDegThis = float(pointingTelescope.icrs.dec.degree)
            ##print(' decDegThis =', decDegThis, 'degrees')

        # RxPx for RightAscension (hours) and Declination (degrees) float numbers
        # 01234
        elif 4 <= len(skyCoordinateSThis) and skyCoordinateSThis[0] == 'r':
            # parse Declination, starts at decIndexSign with p or m
            if 'p' in skyCoordinateSThis[2:]:
                decIndexSign = 2 + skyCoordinateSThis[2:].index('p')
                decDegThis = float(skyCoordinateSThis[decIndexSign + 1:])
            elif 'm' in skyCoordinateSThis[2:]:
                decIndexSign = 2 + skyCoordinateSThis[2:].index('m')
                decDegThis = -float(skyCoordinateSThis[decIndexSign + 1:])
            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
                print(skyCoordinateSL[skyCoordinateIndex])
                print()
                print()
                print()
                print()
                exit()
            # parse RightAscension, starts at 1 with value, ends before decIndexSign
            raHrThis = float(skyCoordinateSThis[1:decIndexSign])
            raDegThis = raHrThis * 15.       # 24 / 360 = 1 / 15

            # have RightAscension and Declination, get astropy bearing
            #pointingTelescope = SkyCoord(ra = raDegThis*u.deg, dec = decDegThis*u.deg,
            #    obstime = dataTimeUtcStrThis, frame = 'icrs', location = locBase)
            pointingTelescopeThis = SkyCoord(ra = raDegThis*u.deg, dec = decDegThis*u.deg,
                frame = 'icrs', location = locBase)

        # Sun
        # 0123
        elif skyCoordinateSThis == 'sun':
            # https://stackoverflow.com/questions/47663082
            # pick noon UTC
            datetimeUTCValue = Time(dateUTCValue + 12 / 24, format='mjd')
            # get astropy bearing
            pointingTelescopeThis = get_sun(datetimeUTCValue)

        # Moon
        # 01234
        elif skyCoordinateSThis == 'moon':
            # pick noon UTC
            #datetimeUTCValue = Time(dateUTCValue + 12 / 24, format='mjd')
            datetimeUTCValue = Time(dateUTCValue, format='mjd')
            # get astropy bearing
            # https://docs.astropy.org/en/stable/api/astropy.coordinates.get_body.html#astropy.coordinates.get_body
            #from astropy.coordinates import solar_system_ephemeris      # just curious of menu
            #print(solar_system_ephemeris.bodies)       # just curious of menu
            #   says ('earth', 'sun', 'moon', 'mercury', 'venus', 'earth-moon-barycenter', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune')
            pointingTelescopeThis = get_body('moon', datetimeUTCValue, location = locBase)

        else:
            print()
            print()
            print()
            print()
            print()
            print(' ========== FATAL ERROR:  Command line has this unrecognized word:')
            print(skyCoordinateSL[skyCoordinateIndex])
            print()
            print()
            print()
            print()
            exit()

        # have pointingTelescopeThis for skyCoordinateSThis

        # for each hourUTC find AzEl, and grow azDegL, elDegL, markerSL, and colorSL
        for hourUTC in range(24):
            #print()
            #print('hourUTC =', hourUTC)

            datetimeUTCValue = Time(dateUTCValue + hourUTC / 24, format='mjd')
            #print(' UTC time =', datetimeUTCValue)                              # UTC time = 60275.1
            #print('type(datetimeUTCValue) =', type(datetimeUTCValue))           # type(datetimeUTCValue) = <class 'astropy.time.core.Time'>

            # extract AzEl coordinates
            azEl = pointingTelescopeThis.transform_to(AltAz(obstime=datetimeUTCValue, location=locBase))
            azDeg = azEl.az.degree
            #print(' azDeg =', azDeg)
            elDeg = azEl.alt.degree
            #print(' elDeg =', elDeg)

            # recorded for each marker
            azDegL.append(azDeg)
            elDegL.append(elDeg)
            markerSL.append(f'${markerS[skyCoordinateIndex]}{hourUTC}$')
            colorSL.append(colorSMenuL[skyCoordinateIndex % colorSMenuLen])

        legendSL.append(f'{markerS[skyCoordinateIndex]}  {skyCoordinateSL[skyCoordinateIndex]}')



def ezWhen100azEl():
    # AzEl plot, from azDegL, elDegL, markerSL, and colorSL
    
    global dayYYMMDD                        # string
    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global titleS                           # string
    global ezWhenPlotRangeL                 # integer list

    # if plot not wanted, then return
    if ezWhenPlotRangeL[1] < 100 or 100 < ezWhenPlotRangeL[0]:
        return(1)

    plotName = 'ezWhen100azEl' + dayYYMMDD + '.png'
    print()
    print('   ezWhen100azEl = AzEl plot ===============')

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot()

    #print()
    #print(' azDegL   =', azDegL)
    #print(' elDegL   =', elDegL)
    #print(' markerSL =', markerSL)
    #print(' colorSL  =', colorSL)

    for i in range(len(azDegL)):
        plt.scatter(azDegL[i], elDegL[i], marker=markerSL[i], s=100., c=colorSL[i])

    plt.title(titleS)

    #plt.xlabel('\nAzimuth (Degrees)')
    #plt.xlabel('\nMarkers = Legend + UTC Hour        Azimuth (Degrees)                                ')
    plt.xlabel('Azimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours')
    plt.xlim(0., 360.)
    plt.xticks( \
        [0.,          30.,  60.,  90.,        120.,  150.,  180.,         210.,  240.,  270.,        300.,  330.,  360.],
        ['0\nNorth', '30', '60', '90\nEast', '120', '150', '180\nFacing South', '210', '240', '270\nWest', '300', '330', '360\nNorth'])

    plt.ylabel('Elevation Above Horizon (Degrees)')
    plt.ylim(0., 90.)

    ezWhenDispGrid = 1
    plt.grid(ezWhenDispGrid)

    # legend for each SkyCoordinate
    ax.text(370., 85., 'Legend', color='black')
    ax.text(370., 80., '======', color='black')
    for i in range(len(legendSL)):
        ax.text(370., 75.-i*5., legendSL[i], color=colorSL[i*24])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def ezWhen110azElS():
    # AzEl South plot, from azDegL, elDegL, markerSL, and colorSL
    
    global dayYYMMDD                        # string
    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global titleS                           # string
    global ezWhenPlotRangeL                 # integer list

    # if plot not wanted, then return
    if ezWhenPlotRangeL[1] < 110 or 110 < ezWhenPlotRangeL[0]:
        return(1)

    plotName = 'ezWhen110azElS' + dayYYMMDD + '.png'
    print()
    print('   ezWhen110azElS = AzEl South plot ===============')

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot()

    #print()
    #print(' azDegL   =', azDegL)
    #print(' elDegL   =', elDegL)
    #print(' markerSL =', markerSL)
    #print(' colorSL  =', colorSL)

    for i in range(len(azDegL)):
        azDegThis = azDegL[i]
        elDegThis = elDegL[i]

        if 90. <= azDegThis and azDegThis <= 270. and 0. <= elDegThis and elDegThis <= 90.:
            plt.scatter(azDegThis, elDegThis, marker=markerSL[i], s=100., c=colorSL[i])

    plt.title(titleS)

    plt.xlim(90., 270.)
    plt.xticks( \
        [90.,         120.,  150.,  180.,         210.,  240.,  270.],
        ['90\nEast', '120', '150', '180\nFacing South', '210', '240', '270\nWest'])
    #plt.xlabel('\nFacing South,  Azimuth (Degrees)')
    #plt.xlabel('Facing South,  Azimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hour')
    plt.xlabel('Azimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours')

    plt.ylabel('Elevation Above Horizon (Degrees)')
    plt.ylim(0., 90.)

    ezWhenDispGrid = 1
    plt.grid(ezWhenDispGrid)

    # legend for each SkyCoordinate
    ax.text(275., 85., 'Legend', color='black')
    ax.text(275., 80., '======', color='black')
    for i in range(len(legendSL)):
        ax.text(275., 75.-i*5., legendSL[i], color=colorSL[i*24])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def ezWhen120azElN():
    # AzEl North plot, from azDegL, elDegL, markerSL, and colorSL
    
    global dayYYMMDD                        # string
    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global titleS                           # string
    global ezWhenPlotRangeL                 # integer list

    # if plot not wanted, then return
    if ezWhenPlotRangeL[1] < 120 or 120 < ezWhenPlotRangeL[0]:
        return(1)

    plotName = 'ezWhen120azElN' + dayYYMMDD + '.png'
    print()
    print('   ezWhen120azElN = AzEl North plot ===============')

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot()

    #print()
    #print(' azDegL   =', azDegL)
    #print(' elDegL   =', elDegL)
    #print(' markerSL =', markerSL)
    #print(' colorSL  =', colorSL)

    for i in range(len(azDegL)):
        azDegThis = azDegL[i]
        if 0. <= azDegThis and azDegThis <= 90.:
            azDegThis += 360.
        elDegThis = elDegL[i]

        if 270. <= azDegThis and azDegThis <= 450. and 0. <= elDegThis and elDegThis <= 90.:
            plt.scatter(azDegThis, elDegThis, marker=markerSL[i], s=100., c=colorSL[i])

    plt.title(titleS)

    plt.xlim(270., 450.)
    plt.xticks( \
        [ 270.,        300.,  330., 360.,        390., 420., 450.],
        ['270\nWest', '300', '330',  '0\nFacing North', '30', '60', '90\nEast'])
    plt.xlabel('Azimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours')

    plt.ylabel('Elevation Above Horizon (Degrees)')
    plt.ylim(0., 90.)

    ezWhenDispGrid = 1
    plt.grid(ezWhenDispGrid)

    # legend for each SkyCoordinate
    ax.text(455., 85., 'Legend', color='black')
    ax.text(455., 80., '======', color='black')
    for i in range(len(legendSL)):
        ax.text(455., 75.-i*5., legendSL[i], color=colorSL[i*24])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def ezWhen210azElDS():
    # AzEl Dome South plot, from azDegL, elDegL, markerSL, and colorSL

    global dayYYMMDD                        # string
    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global titleS                           # string
    global ezWhenPlotRangeL                 # integer list

    # if plot not wanted, then return
    if ezWhenPlotRangeL[1] < 210 or 210 < ezWhenPlotRangeL[0]:
        return(1)

    plotName = 'ezWhen210azElDS' + dayYYMMDD + '.png'
    print()
    print('   ezWhen210azElDS = AzEl Dome South plot ===============')

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot()

    #print()
    #print(' azDegL   =', azDegL)
    #print(' elDegL   =', elDegL)
    #print(' markerSL =', markerSL)
    #print(' colorSL  =', colorSL)

    import numpy as np
    piD180 = 3.141 / 180.
    piD360 = 3.141 / 360.

    if 1:
        # plot markers
        for i in range(len(azDegL)):
            azDegThis = azDegL[i]
            elDegThis = elDegL[i]

            if 90. <= azDegThis and azDegThis <= 270. and 0. <= elDegThis and elDegThis <= 90.:
                # warp azDegThis and elDegThis into x and y
                # https://en.wikipedia.org/wiki/Aitoff_projection
                # https://en.wikipedia.org/wiki/Sinc_function
                elRad = elDegThis * piD180
                cosElRad = np.cos(elRad)
                sinElRad = np.sin(elRad)

                azDiffD2Rad = (azDegThis - 180.) * piD360

                alpha = np.arccos(cosElRad * np.cos(azDiffD2Rad))
                if not alpha:
                    alpha += 1e-10
                sincAlpha = np.sin(alpha) / alpha

                x = 180. + 2 * cosElRad * np.sin(azDiffD2Rad) / sincAlpha / piD180
                y = sinElRad / sincAlpha / piD180

                plt.scatter(x, y, marker=markerSL[i], s=100., c=colorSL[i])

    if 1:
        # draw grid of dots
        #for azDegThis in range(90, 271, 5):
        #    for elDegThis in range(0, 91, 5):
        for azDegThis in range(90, 271, 10):
            for elDegThis in range(0, 91, 10):
                #print('               azDegThis =', azDegThis, '    elDegThis =', elDegThis)

                # warp azDegThis and elDegThis into x and y
                # https://en.wikipedia.org/wiki/Aitoff_projection
                # https://en.wikipedia.org/wiki/Sinc_function
                elRad = elDegThis * piD180
                cosElRad = np.cos(elRad)
                sinElRad = np.sin(elRad)

                azDiffD2Rad = (azDegThis - 180.) * piD360

                alpha = np.arccos(cosElRad * np.cos(azDiffD2Rad))
                if not alpha:
                    alpha += 1e-10
                sincAlpha = np.sin(alpha) / alpha

                x = 180. + 2 * cosElRad * np.sin(azDiffD2Rad) / sincAlpha / piD180
                y = sinElRad / sincAlpha / piD180

                plt.scatter(x, y, s=0.1, c='black')
 
    if 0:
        # Draw border
        for azDegThis in range(90, 271, 5):
            for elDegThis in range(0, 91, 5):
                #print('               azDegThis =', azDegThis, '    elDegThis =', elDegThis)

                # warp azDegThis and elDegThis into x and y
                # https://en.wikipedia.org/wiki/Aitoff_projection
                # https://en.wikipedia.org/wiki/Sinc_function
                elRad = elDegThis * piD180
                cosElRad = np.cos(elRad)
                sinElRad = np.sin(elRad)

                azDiffD2Rad = (azDegThis - 180.) * piD360

                alpha = np.arccos(cosElRad * np.cos(azDiffD2Rad))
                if not alpha:
                    alpha += 1e-10
                sincAlpha = np.sin(alpha) / alpha

                x = 180. + 2 * cosElRad * np.sin(azDiffD2Rad) / sincAlpha / piD180
                y = sinElRad / sincAlpha / piD180

                plt.scatter(x, y, s=0.1, c='black')
 
    ax.text(180., 95., 'Zenith', color='black', verticalalignment='bottom', horizontalalignment='center')
    ax.text(90., -5., '90\u00b0\nEast', color='black', verticalalignment='top', horizontalalignment='right')
    #ax.text(180., -5., '180\u00b0\n\nFacing South', color='black', verticalalignment='top', horizontalalignment='center')
    #ax.text(180., -5., '180\u00b0\nFacing South', color='black', verticalalignment='top', horizontalalignment='center')
    ax.text(180., -5., '180\u00b0\nFacing South\nAzimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours'
        , color='black', verticalalignment='top', horizontalalignment='center')
    ax.text(270., -5., '270\u00b0\nWest', color='black', verticalalignment='top', horizontalalignment='left')

    plt.axis('equal')       # x and y scales the same
    plt.axis('off')

    plt.title(dayYYMMDD)

    #plt.xlabel('Azimuth')
    #plt.xlabel('Azimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours')
    #plt.xlim(0., 360.)
    plt.xlim(80., 280.)

    plt.ylabel('Elevation Above Horizon (Degrees)')
    plt.ylim(-10., 100.)

    plt.title(titleS)

    #ax.grid(False)  # Hide grid lines
    plt.grid(False)

    # legend for each SkyCoordinate
    ax.text(285., 108., 'Legend', color='black')
    ax.text(285., 100., '======', color='black')
    for i in range(len(legendSL)):
        ax.text(285., 92.-i*8., legendSL[i], color=colorSL[i*24])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def ezWhen220azElDN():
    # AzEl Dome North plot, from azDegL, elDegL, markerSL, and colorSL

    global dayYYMMDD                        # string
    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global titleS                           # string
    global ezWhenPlotRangeL                 # integer list

    # if plot not wanted, then return
    if ezWhenPlotRangeL[1] < 220 or 220 < ezWhenPlotRangeL[0]:
        return(1)

    plotName = 'ezWhen220azElDS' + dayYYMMDD + '.png'
    print()
    print('   ezWhen220azElDN = AzEl Dome North plot ===============')

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot()

    #print()
    #print(' azDegL   =', azDegL)
    #print(' elDegL   =', elDegL)
    #print(' markerSL =', markerSL)
    #print(' colorSL  =', colorSL)

    import numpy as np
    piD180 = 3.141 / 180.
    piD360 = 3.141 / 360.

    if 1:
        # plot markers
        for i in range(len(azDegL)):
            azDegThis = azDegL[i]
            if 0. <= azDegThis and azDegThis <= 90.:
                azDegThis += 360.
            elDegThis = elDegL[i]

            if 270. <= azDegThis and azDegThis <= 450. and 0. <= elDegThis and elDegThis <= 90.:
                # warp azDegThis and elDegThis into x and y
                # https://en.wikipedia.org/wiki/Aitoff_projection
                # https://en.wikipedia.org/wiki/Sinc_function
                elRad = elDegThis * piD180
                cosElRad = np.cos(elRad)
                sinElRad = np.sin(elRad)

                azDiffD2Rad = (azDegThis - 360.) * piD360

                alpha = np.arccos(cosElRad * np.cos(azDiffD2Rad))
                if not alpha:
                    alpha += 1e-10
                sincAlpha = np.sin(alpha) / alpha

                x = 360. + 2 * cosElRad * np.sin(azDiffD2Rad) / sincAlpha / piD180
                y = sinElRad / sincAlpha / piD180

                plt.scatter(x, y, marker=markerSL[i], s=100., c=colorSL[i])

    if 1:
        # draw grid of dots
        #for azDegThis in range(90, 271, 5):
        #    for elDegThis in range(0, 91, 5):
        for azDegThis in range(270, 451, 10):
            for elDegThis in range(0, 91, 10):
                #print('               azDegThis =', azDegThis, '    elDegThis =', elDegThis)

                # warp azDegThis and elDegThis into x and y
                # https://en.wikipedia.org/wiki/Aitoff_projection
                # https://en.wikipedia.org/wiki/Sinc_function
                elRad = elDegThis * piD180
                cosElRad = np.cos(elRad)
                sinElRad = np.sin(elRad)

                azDiffD2Rad = (azDegThis - 360.) * piD360

                alpha = np.arccos(cosElRad * np.cos(azDiffD2Rad))
                if not alpha:
                    alpha += 1e-10
                sincAlpha = np.sin(alpha) / alpha

                x = 360. + 2 * cosElRad * np.sin(azDiffD2Rad) / sincAlpha / piD180
                y = sinElRad / sincAlpha / piD180

                plt.scatter(x, y, s=0.1, c='black')
 
    if 0:
        # Draw border
        for azDegThis in range(270, 451, 5):
            for elDegThis in range(0, 91, 5):
                #print('               azDegThis =', azDegThis, '    elDegThis =', elDegThis)

                # warp azDegThis and elDegThis into x and y
                # https://en.wikipedia.org/wiki/Aitoff_projection
                # https://en.wikipedia.org/wiki/Sinc_function
                elRad = elDegThis * piD180
                cosElRad = np.cos(elRad)
                sinElRad = np.sin(elRad)

                azDiffD2Rad = (azDegThis - 360.) * piD360

                alpha = np.arccos(cosElRad * np.cos(azDiffD2Rad))
                if not alpha:
                    alpha += 1e-10
                sincAlpha = np.sin(alpha) / alpha

                x = 360. + 2 * cosElRad * np.sin(azDiffD2Rad) / sincAlpha / piD180
                y = sinElRad / sincAlpha / piD180

                plt.scatter(x, y, s=0.1, c='black')
 
    ax.text(360., 95., 'Zenith', color='black', verticalalignment='bottom', horizontalalignment='center')
    ax.text(270., -5., '270\u00b0\nWest', color='black', verticalalignment='top', horizontalalignment='right')
    #ax.text(360., -5., '0\u00b0\n\nFacing North', color='black', verticalalignment='top', horizontalalignment='center')
    #ax.text(360., -5., '0\u00b0\nFacing North', color='black', verticalalignment='top', horizontalalignment='center')
    ax.text(360., -5., '0\u00b0\nFacing North\nAzimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours'
        , color='black', verticalalignment='top', horizontalalignment='center')
    ax.text(450., -5., '90\u00b0\nEast', color='black', verticalalignment='top', horizontalalignment='left')

    plt.axis('equal')       # x and y scales the same
    plt.axis('off')

    plt.title(dayYYMMDD)

    #plt.xlabel('Azimuth')
    #plt.xlabel('Azimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours')
    plt.xlim(260., 460.)

    plt.ylabel('Elevation')
    plt.ylim(-10., 100.)

    plt.title(titleS)

    #ax.grid(False)  # Hide grid lines
    plt.grid(False)

    # legend for each SkyCoordinate
    ax.text(465., 108., 'Legend', color='black')
    ax.text(465., 100., '======', color='black')
    for i in range(len(legendSL)):
        ax.text(465., 92.-i*8., legendSL[i], color=colorSL[i*24])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def ezWhen300azElPZ():
    # AzEl Polar Zenith plot, from azDegL, elDegL, markerSL, and colorSL

    global dayYYMMDD                        # string
    global azDegL                           # list of floats
    global elDegL                           # list of floats
    global markerSL                         # list of strings
    global colorSL                          # list of strings
    global legendSL                         # list of strings
    global titleS                           # string
    global ezWhenPlotRangeL                 # integer list

    # if plot not wanted, then return
    if ezWhenPlotRangeL[1] < 300 or 300 < ezWhenPlotRangeL[0]:
        return(1)

    plotName = 'ezWhen300azElPZ' + dayYYMMDD + '.png'
    print()
    print('   ezWhen300azElPZ = AzEl Polar Zenith plot ===============')

    plt.clf()
    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')

    #print()
    #print(' azDegL   =', azDegL)
    #print(' elDegL   =', elDegL)
    #print(' markerSL =', markerSL)
    #print(' colorSL  =', colorSL)

    piD180 = 3.141 / 180.

    if 0:
        for i in range(len(azDegL)):
            plt.scatter(azDegL[i], elDegL[i], marker=markerSL[i], s=100., c=colorSL[i])

        plt.title(dayYYMMDD)

        plt.xlabel('Azimuth')
        plt.xlim(0., 360.)

        plt.ylabel('Elevation')
        plt.ylim(0., 90.)

        ezWhenDispGrid = 1
        plt.grid(ezWhenDispGrid)

    #import numpy as np
    #theta = np.array([i * 6.282 / 360 for i in azDegL])
    #r = np.array(elDegL)
    #print(' theta =', theta)
    #print(' r =', r)
    #print(' markerSL =', markerSL)
    #print(' colorSL =', colorSL)

    #ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    #ax.scatter(thetaL, elDegL)
    #ax.scatter(np.array(thetaL), np.array(elDegL))
    #area = 200 * r**2
    #area = r
    #colors = theta
    #c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)
    #c = ax.scatter(theta, r, marker=markerSL[i], s=100., c=colorSL[i])
    if 1:
        for i in range(len(azDegL)):
            #c = ax.scatter(theta[i], r[i], marker=markerSL[i], s=100., c=colorSL[i])
            #c = ax.scatter(azDegL[i] * 3.141 / 180, elDegL[i], marker=markerSL[i], s=100., c=colorSL[i])
            c = ax.scatter(azDegL[i] * piD180, elDegL[i], marker=markerSL[i], s=100., c=colorSL[i])

    plt.title(titleS)

    #plt.xlim(0, 6.282)
    plt.ylim(90., 0.)

    #ax.set_rgrids((fileFreqBinQty/2.,), ('',))
    #ax.set_theta_zero_location('S', offset=0.)
    ax.set_theta_zero_location('N', offset=0.)
    #ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))
    #ax.set_thetagrids((90, 180, 270, 360), ('90\u00b0\nEast', '180\u00b0\nFacing South', '270\u00b0\nWest', 'Bending over backwards North\n0\u00b0'))
    ax.set_thetagrids((90, 180, 270, 360),
        ('90\u00b0\nEast', '\n\n180\u00b0\nFacing South\nAzimuth (Degrees)\nMarkers = Location of Legend Sky Object at UTC Hours',
        ' 270\u00b0\n West', 'Bending over backwards North\n0\u00b0'))
    ax.set_rlabel_position(135)
    #ax.text( 1.4, -2.5, 'Elevation', color='black')
    ax.text(135 * piD180, -3., 'Elevation\nAbove\nHorizon\n(Degrees)', color='black', verticalalignment='top', horizontalalignment='right')
    #radiusTextQuadrant = fileFreqBinQty * 1.1
    #ax.text(-2.55, radiusTextQuadrant, 'Quadrant 1', color='red', horizontalalignment='right')
    #ax.text(-0.6,  radiusTextQuadrant, 'Quadrant 2', color='red', horizontalalignment='right')
    #ax.text( 0.6,  radiusTextQuadrant, 'Quadrant 3', color='red')
    #ax.text( 2.55, radiusTextQuadrant, 'Quadrant 4', color='red')
    #ax.text(-3.05, radiusTextQuadrant*0.95, 'Toward', color='blue', horizontalalignment='right')
    #ax.text( 3.05, radiusTextQuadrant*0.95, 'Galactic Center', color='blue')
    #ax.text(-2.2, radiusTextQuadrant*0.95, 'Sun at\nCenter', color='blue', horizontalalignment='right')

    # legend for each SkyCoordinate
    legendPolarS = 'Legend\n======'
    #for i in range(len(legendSL)):
    #   legendPolarS = legendPolarS + '\n' + legendSL[i]
    ax.text(305. * piD180, -55., legendPolarS, color='black', verticalalignment='top', horizontalalignment='left')
    for i in range(len(legendSL)):
        legendPolarS = '\n' * (i+2) + legendSL[i]
        ax.text(305. * piD180, -55., legendPolarS, color=colorSL[i*24], verticalalignment='top', horizontalalignment='left')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def main():

    #global ezRAObsLat                       # float
    #global ezRAObsLon                       # float
    #global ezRAObsAmsl                      # float
    #global ezRAObsName                      # string
    #global ezWhenPlotRangeL                 # integer list

    #global dayYYMMDD                        # string
    #global dateUTCValue                     # class 'astropy.time.core.Time'
    #global skyCoordinateSL                  # list of strings

    printHello()
    
    ezConArguments()

    plotPrep()

    ezWhen100azEl()     # AzEl plot
    ezWhen110azElS()    # AzEl South plot
    ezWhen120azElN()    # AzEl North plot
    
    ezWhen210azElDS()   # AzEl Dome South plot
    ezWhen220azElDN()   # AzEl Dome North plot

    ezWhen300azElPZ()   # AzEl Polar Zenith plot

    print()
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



if __name__== '__main__':
  main()

# a@u22-221222a:~/aaaEzRABase/ezWhen$ 
#   python3 ../ezRA/ezWhen240113a.py  Gm0p0  -exR3p10 Gp40p0 Gp80p0 R0p60
#   python3  ../ezRA/ezWhen240117b.py  sun  Moon  R0P60  GP0P0  Gp80p10  Gp80m10  -240317  -ezWhenPlotRangeL 0 210

