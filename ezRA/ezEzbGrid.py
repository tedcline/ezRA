programName = 'ezEzbGrid221121a.py'
#programRevision = programName + ' (N0RQV)'
programRevision = programName

# ezRA - Easy Radio Astronomy .ezb Data File Coordinate Grid Creator - ezEzbGrid

# ezEzbGrid221121a.py, defaultKS, inputing ezEzbGridRangeL, ezEzbGridBoxL, and ezEzbGridLineL
# ezEzbGrid221113a.py, changed time for good ezSky601AzEl
# ezEzbGrid221112a.py, first try to combine ezEzbAzEl.py, ezEzbRaDec.py, and ezEzbGal.py,
# ezEzbGal221112a.py, first try
# ezEzbRaDec221111a.py, first try
# ezEzbAzEl221111a.py, first try
# ezCon221111a.py, experimentEzc for AzEl into .ezb Spare1 and Spare2,
#   commented openFileSdre() and writeFileSdre(),
#   fixed 'FATAL ERROR:  ezRAObsLon' typo


from astropy.time import Time

import numpy as np
import math
import datetime
import os
import sys
import time



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezEzbGrid.py [optional arguments]')
    print('  Linux:     python3 ezEzbGrid.py [optional arguments]')
    print()
    print('  Easy Radio Astronomy (ezRA) ezEzbGrid .ezb Data File Coordinate Grid Creator program')
    print('  to create ezCon format .ezb condensed data files,')
    print('  to be displayed by the ezSky program, for study.')
    print()
    print('  Arguments may be in any order.')
    print()
    print('  Arguments are read first from inside the ezEzbGrid program,')
    print("  then in order from the ezDefaults.txt in the ezEzbGrid.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  py ezEzbGrid.py -help                          (print this help)')
    print('  py ezEzbGrid.py -h                             (print this help)')
    print()
    print('    -ezRAObsName            Lebanon Kansas       (Observatory Name)')
    print('    -ezRAObsLat             39.8282              (Observatory Latitude  (degrees))')
    print('    -ezRAObsLon             -98.5696             (Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl            563.88               (Observatory Above Mean Sea Level (meters))')
    print()
    print('    -ezEzbGrid              2                    (choice of grid created)')
    print('      -ezEzbGrid                1: create an AzEl     Horizontal grid')
    print('      -ezEzbGrid                2: create a  RaDec    Equatorial grid')
    print('      -ezEzbGrid                3: create a  GLatGLon Galactic   grid')
    print()
    print('    -ezEzbGridRangeL        0 360 0 90           (grid extreme corner coordinates)')
    print()
    print('    -ezEzbGridBoxL          15  15               (dimensions of each grid box)')
    print('    -ezEzbGridLineL         1   1                (sample spacing in grid lines)')
    print()
    print('    -ezEzbGridAstroMath     1                    (astroMath choice)')
    print('      -ezEzbGridAstroMath       0: no math (??)')
    print('      -ezEzbGridAstroMath       1: using math from MIT Haystack SRT (only for AzEl grid)')
    print('      -ezEzbGridAstroMath       2: using math from slower Astropy library')
    print()
    print('    -ezEzbGridUseVlsr       1                    (calculate VLSR (??))')
    print()
    print('    -ezEzbGridDateTime      2022-06-20T18:00:01  (dateTime for all data samples in AzEL grid)')
    print()
    print('    -ezDefaultsFile ../bigDish8.txt              (additional file of ezRA arguments)')
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
    print('            ezEzbGrid.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezEzbGridArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezEzbGrid                        # integer
    global ezEzbGridRangeL                  # float list
    global ezEzbGridBoxL                    # float list
    global ezEzbGridLineL                   # float list

    global ezEzbGridAstroMath               # integer
    global ezEzbGridUseVlsr                 # integer

    global ezEzbGridDateTimeS               # string


    print()
    print('   ezEzbGridArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

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
                if thisLine[1]:
                    ezRAObsName = thisLine[1]

            # integer arguments:
            elif thisLine0Lower == '-ezEzbGrid'.lower():
                ezEzbGrid = int(thisLine[1])

            elif thisLine0Lower == '-ezEzbGridAstroMath'.lower():
                ezEzbGridAstroMath = int(thisLine[1])

            elif thisLine0Lower == '-ezEzbGridUseVlsr'.lower():
                ezEzbGridUseVlsr = int(thisLine[1])
                
                
            # float arguments:


            # list arguments:
            elif thisLine0Lower == '-ezEzbGridRangeL'.lower():
                ezEzbGridRange0 = float(thisLine[1])
                ezEzbGridRange1 = float(thisLine[2])
                ezEzbGridRange2 = float(thisLine[3])
                ezEzbGridRange3 = float(thisLine[4])
                ezEzbGridRangeL = [ezEzbGridRange0, ezEzbGridRange1, ezEzbGridRange2, ezEzbGridRange3]

            elif thisLine0Lower == '-ezEzbGridBoxL'.lower():
                ezEzbGridBox0 = float(thisLine[1])
                ezEzbGridBox1 = float(thisLine[2])
                ezEzbGridBoxL = [ezEzbGridBox0, ezEzbGridBox1]

            elif thisLine0Lower == '-ezEzbGridLineL'.lower():
                ezEzbGridLine0 = float(thisLine[1])
                ezEzbGridLine1 = float(thisLine[2])
                ezEzbGridLineL = [ezEzbGridLine0, ezEzbGridLine1]


            # string arguments:
            elif thisLine0Lower == '-ezEzbGridDateTime'.lower():
                ezEzbGridDateTimeS = thisLine[1]


            elif thisLine0Lower[:5] == '-ezEzbGrid'.lower():
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



def ezEzbGridArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezEzbGrid                        # integer
    global ezEzbGridRangeL                  # float list
    global ezEzbGridBoxL                    # float list
    global ezEzbGridLineL                   # float list

    global ezEzbGridAstroMath               # integer
    global ezEzbGridUseVlsr                 # integer

    global ezEzbGridDateTimeS               # string

    global cmdDirectoryS                    # string            creation


    print()
    print('   ezEzbGridArgumentsCommandLine ===============')

    cmdLineSplit = commandString.split()
    cmdLineSplitLen = len(cmdLineSplit)
    #print(' cmdLineSplit =', cmdLineSplit)
        
    # need at least one data directory or file
    #if cmdLineSplitLen < 2:
    #    printUsage()

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
            

            # integer arguments:
            elif cmdLineArgLower == '-ezEzbGrid'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGrid = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezEzbGridAstroMath'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridAstroMath = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezEzbGridUseVlsr'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridUseVlsr = int(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:


            # list arguments:
            elif cmdLineArgLower == '-ezEzbGridRangeL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridRange0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezEzbGridRange1 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezEzbGridRange2 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezEzbGridRange3 = float(cmdLineSplit[cmdLineSplitIndex])
                ezEzbGridRangeL = [ezEzbGridRange0, ezEzbGridRange1, ezEzbGridRange2, ezEzbGridRange3]

            elif cmdLineArgLower == '-ezEzbGridBoxL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridBox0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezEzbGridBox1 = float(cmdLineSplit[cmdLineSplitIndex])
                ezEzbGridBoxL = [ezEzbGridBox0, ezEzbGridBox1]

            elif cmdLineArgLower == '-ezEzbGridLineL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridLine0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezEzbGridLine1 = float(cmdLineSplit[cmdLineSplitIndex])
                ezEzbGridLineL = [ezEzbGridLine0, ezEzbGridLine1]


            # string arguments:
            elif cmdLineArgLower == '-ezEzbGridDateTime'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridDateTimeS = cmdLineSplit[cmdLineSplitIndex]


            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezEzbGridArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            # ignore silly -ezez* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            elif 5 <= len(cmdLineArgLower) and cmdLineArgLower[:5] == '-ezez':
                pass

            else:
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
            # must be a data directory or file, remember it
            cmdDirectoryS = cmdDirectoryS + cmdLineSplit[cmdLineSplitIndex] + ' '

        cmdLineSplitIndex += 1



def ezEzbGridArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global programRevision                  # string
    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezEzbGrid                        # integer
    global ezEzbGridRangeL                  # float list
    global ezEzbGridBoxL                    # float list
    global ezEzbGridLineL                   # float list

    global ezEzbGridAstroMath               # integer
    global ezEzbGridUseVlsr                 # integer

    global ezEzbGridDateTimeS               # string

    global fileNameLast                     # string


    # defaults
    if 1:
        #ezRAObsName = 'LebanonKS'
        ezRAObsName = 'defaultKS'
        ezRAObsLat  =  39.8282    #Geographic Center of USA, near Lebanon, Kansas
        ezRAObsLon  = -98.5696
        ezRAObsAmsl = 563.88

        ezEzbGrid       = 3
        ezEzbGridRangeL = []
        ezEzbGridBoxL   = []
        ezEzbGridLineL  = []

        ezEzbGridAstroMath = 2
        ezEzbGridUseVlsr = 0

        ezEzbGridDateTimeS = '2022-03-21T05:00:01'


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

    # process arguments from ezDefaults.txt file in the same directory as this ezEzbGrid program
    ezEzbGridArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezEzbGridArgumentsFile('ezDefaults.txt')

    # process arguments from command line
    ezEzbGridArgumentsCommandLine()


    # sanity checks
    if not ezEzbGridRangeL:
        if ezEzbGrid == 1:
            ezEzbGridRangeL = [0, 360, 0, 90]
        if ezEzbGrid == 2:
            ezEzbGridRangeL = [0, 24, -90, 90]
        else:
            ezEzbGridRangeL = [-180, 180, -90, 90]
        
    if not ezEzbGridBoxL:
        if ezEzbGrid == 1:
            ezEzbGridBoxL = [30, 30]
        if ezEzbGrid == 2:
            ezEzbGridBoxL = [1, 30]
        else:
            ezEzbGridBoxL = [30, 30]
        
    if not ezEzbGridLineL:
        if ezEzbGrid == 1:
            ezEzbGridLineL = [1, 1]
        if ezEzbGrid == 2:
            ezEzbGridLineL = [0.1, 1]
        else:
            ezEzbGridLineL = [1, 1]

    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezEzbGrid       =', ezEzbGrid)
        print('   ezEzbGridRangeL =', ezEzbGridRangeL)
        print('   ezEzbGridBoxL   =', ezEzbGridBoxL)
        print('   ezEzbGridLineL  =', ezEzbGridLineL)
        print()
        print('   ezEzbGridAstroMath =', ezEzbGridAstroMath)
        print('   ezEzbGridUseVlsr   =', ezEzbGridUseVlsr)
        print()
        print('   ezEzbGridDateTime =', ezEzbGridDateTimeS)
        print()



def readDataDir():
    # Open each .txt radio file in each directory and read individual lines.
    # Creates ezRAObsLat, ezRAObsLon, ezRAObsAmsl, ezRAObsName,
    #   fileFreqMin, fileFreqMax, fileFreqBinQty,
    #   azimuth, elevation, dataTimeUtc, raw, rawLen, fileNameLast

    global cmdDirectoryS            # string

    global ezRAObsLat               # float
    global ezRAObsLon               # float
    global ezRAObsAmsl              # float
    global ezRAObsName              # string
    global fileNameLast             # string                                    creation
    global fileFreqMin              # float                                     creation
    global fileFreqMax              # float                                     creation
    global fileFreqBinQty           # integer                                   creation

    global dataTimeUtc              # 'astropy.time.core.Time' object array     creation
    global azDeg                    # float array                               creation
    global elDeg                    # float array                               creation
    global raH                      # float array                               creation
    global decDeg                   # float array                               creation
    global gLatDeg                  # float array                               creation
    global gLonDeg                  # float array                               creation

    global antLen                   # integer                                   creation

    print()
    print('   readDataDir ===============')

    ## 220301 new format
    ## ezRA ezCol .txt daily data file with 3-line non-comment header and
    ##   1-line samples each with timestamp and 256 values:
    ##
    ## from ezCol04b5ea.py
    ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb
    ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
    ## az 227.9 el 42.7 
    ## # times are in UTC
    ## 2022-02-15T05:30:55 10.523690382 10.570080895 10.535587705 10.527403187 ... C
    ## 2022-02-15T05:30:56 10.558290361 10.551762452 10.545512521 10.539835481 ...
    ## ...

    # read line 2
    ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb

    # read line 3
    ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
    fileFreqMin    = 1419.205
    fileFreqMax    = 1421.605
    fileFreqBinQty = 256

    if ezEzbGrid == 1:
        # AzEl grid
        azDeg = np.empty(0, dtype=float)
        elDeg = np.empty(0, dtype=float)
        # create data points along a few horizontal lines along unchanging elDegThis
        for elDegThis in np.arange(ezEzbGridRangeL[2], ezEzbGridRangeL[3]+ezEzbGridBoxL[1],
            ezEzbGridBoxL[1]):
                for azDegThis in np.arange(ezEzbGridRangeL[0], ezEzbGridRangeL[1]+ezEzbGridLineL[0],
                    ezEzbGridLineL[0]):
                        azDeg = np.concatenate([azDeg, np.array([azDegThis])])
                        elDeg = np.concatenate([elDeg, np.array([elDegThis])])

        # create data points along a few vertical lines along unchanging azDegThis
        for azDegThis in np.arange(ezEzbGridRangeL[0], ezEzbGridRangeL[1]+ezEzbGridBoxL[0],
            ezEzbGridBoxL[0]):
                for elDegThis in np.arange(ezEzbGridRangeL[2], ezEzbGridRangeL[3]+ezEzbGridLineL[1],
                    ezEzbGridLineL[1]):
                        azDeg = np.concatenate([azDeg, np.array([azDegThis])])
                        elDeg = np.concatenate([elDeg, np.array([elDegThis])])

        antLen = len(azDeg)
        
    elif ezEzbGrid == 2:
        # RaDec grid
        raH    = np.empty(0, dtype=float)
        decDeg = np.empty(0, dtype=float)
        # create data points along a few horizontal lines along unchanging decDeg
        for decDegThis in np.arange(ezEzbGridRangeL[2], ezEzbGridRangeL[3]+ezEzbGridBoxL[1],
            ezEzbGridBoxL[1]):
                for raHThis in np.arange(ezEzbGridRangeL[0], ezEzbGridRangeL[1]+ezEzbGridLineL[0],
                    ezEzbGridLineL[0]):
                        raH    = np.concatenate([raH,    np.array([raHThis])])
                        decDeg = np.concatenate([decDeg, np.array([decDegThis])])

        # create data points along a few vertical lines along unchanging raH
        for raHThis in np.arange(ezEzbGridRangeL[0], ezEzbGridRangeL[1]+ezEzbGridBoxL[0],
            ezEzbGridBoxL[0]):
                for decDegThis in np.arange(ezEzbGridRangeL[2], ezEzbGridRangeL[3]+ezEzbGridLineL[1],
                    ezEzbGridLineL[1]):
                        raH    = np.concatenate([raH,    np.array([raHThis])])
                        decDeg = np.concatenate([decDeg, np.array([decDegThis])])

        antLen = len(raH)

    else:
        # GLatGLon grid
        gLatDeg = np.empty(0, dtype=float)
        gLonDeg = np.empty(0, dtype=float)
        # create data points along a few horizontal lines along unchanging gLatDegThis
        for gLatDegThis in np.arange(ezEzbGridRangeL[2], ezEzbGridRangeL[3]+ezEzbGridBoxL[1],
            ezEzbGridBoxL[1]):
                for gLonDegThis in np.arange(ezEzbGridRangeL[0], ezEzbGridRangeL[1]+ezEzbGridLineL[0],
                    ezEzbGridLineL[0]):
                        gLatDeg = np.concatenate([gLatDeg, np.array([gLatDegThis])])
                        gLonDeg = np.concatenate([gLonDeg, np.array([gLonDegThis])])

        # create data points along a few vertical lines along unchanging gLonDegThis
        for gLonDegThis in np.arange(ezEzbGridRangeL[0], ezEzbGridRangeL[1]+ezEzbGridBoxL[0],
            ezEzbGridBoxL[0]):
                for gLatDegThis in np.arange(ezEzbGridRangeL[2], ezEzbGridRangeL[3]+ezEzbGridLineL[1],
                    ezEzbGridLineL[1]):
                        gLatDeg = np.concatenate([gLatDeg, np.array([gLatDegThis])])
                        gLonDeg = np.concatenate([gLonDeg, np.array([gLonDegThis])])

        antLen = len(gLatDeg)

    # Bases: astropy.time.TimeString
    # FITS format: “[±Y]YYYY-MM-DD[THH:MM:SS[.sss]]”.
    # https://docs.astropy.org/en/stable/time/#id3
    #dataTimeUtcThis = Time(fileLineSplit[0], format='fits', scale='utc')
    #dataTimeUtcThis = Time('YYYY-MM-DDTHH:MM:SS', format='fits', scale='utc')
    #dataTimeUtcThis = Time('2022-03-20T17:00:01', format='fits', scale='utc')
    dataTimeUtcThis = Time(ezEzbGridDateTimeS, format='fits', scale='utc')
    dataTimeUtc = np.full(antLen, dataTimeUtcThis)

    #programName = 'ezEzbAzEl221111a.py'
    fileNameLast = programName + 'x'        # need a 3-letter extension on file name, trimmed later


    # prepare to process data

    if ezRAObsLat < -90 or 90 < ezRAObsLat:
        print()
        print()
        print()
        print(f' ========== FATAL ERROR:  ezRAObsLat = {ezRAObsLat} is silly')
        print('                            Required: -90 <= ezRAObsLat <= +90')
        print()
        print()
        print()
        exit()

    if ezRAObsLon < -180 or 180 < ezRAObsLon:
        print()
        print()
        print()
        print(f' ========== FATAL ERROR:  ezRAObsLon = {ezRAObsLon} is silly')
        print('                            Required: -180 <= ezRAObsLon <= +180')
        print()
        print()
        print()
        exit()

    # Status after data files: Now have ezRAObsLat ezRAObsLon ezRAObsAmsl ezRAObsName
    # fileFreqMin fileFreqMax fileFreqBinQty fileNameLast rawLen refQty
    # azimuth[rawLen] elevation[rawLen] dataTimeUtc[rawLen] raw[fileFreqBinQty * rawLen]



def openFileEzb():
    # In case it will eventually error.  Creates fileWriteNameEzb, fileWriteEzb

    global fileNameLast             # string
    global fileWriteNameEzb         # string                creation
    global fileWriteEzb             # file handle           creation

    print()
    print('   openFileEzb ===============')

    ## data/rqv8ezb220218_00a.txt
    #                        4321-
    fileWriteNameEzb = fileNameLast.split(os.path.sep)[-1][:-4] + '.ezb'
    print('   opening', fileWriteNameEzb)

    # before much calculating, get proof can open output file
    fileWriteEzb = open(fileWriteNameEzb, 'w')
    if not (fileWriteEzb.mode == 'w'):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Can not open ')
        print(' ' + fileWriteNameEzb)
        print(' file to write data out')
        print()
        print()
        print()
        print()
        exit()



def createEzConOutEzb():
    # creates antXTV, and ezConOut[n, 20]
    # deletes antAvg, antMax,   refAvg, refMax,   antBAvg, antBMax,   antRBAvg, antRBMax

    # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  Spare1  Spare2  Spare3
    #          0           1    2       3        4        5     6      7       8       9
    #   AntAvg  AntMax    RefAvg  RefMax
    #   10      11        12      13
    #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
    #   14       15          16        17         18          19

    global ezRAObsLat               # float
    global ezRAObsLon               # float
    global ezRAObsAmsl              # float

    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global azDeg                    # float array
    global elDeg                    # float array
    global raH                      # float array
    global decDeg                   # float array
    global gLatDeg                  # float array
    global gLonDeg                  # float array

    global fileFreqBinQty           # integer

    global ezEzbGrid                # integer
    global ezEzbGridRangeL          # float list
    global ezEzbGridBoxL            # float list
    global ezEzbGridLineL           # float list

    global ezEzbGridAstroMath       # integer
    global ezEzbGridUseVlsr         # integer

    global ezEzbGridDateTimeS       # string

    global antLen                   # integer

    global ezConOut                 # float and int 2d array        creation

    global fileNameLast             # string

    print()
    print('   createEzConOutEzb ===============')
    print('                         ezEzbGridAstroMath =', ezEzbGridAstroMath)

    # for each sample in ant, create and collect .ezb coordinate numbers

    if ezEzbGridAstroMath == 1:
        # use Python port from MIT Haystack Small Radio Telescope (SRT) geom.c
        # https://www.haystack.mit.edu/haystack-public-outreach/srt-the-small-radio-telescope-for-education/
        # VLSR = Velocity of the Local Standard of Rest
        #   to remove Doppler effects of earth and Sun Galactic movements

        #decc = -(28. + 56. / 60.) * math.pi / 180.
        #print(' decc =', decc)
        #rac = (17. + 45.5 / 60.) * math.pi / 12.
        #print(' rac =', rac)
        #dp = 27.1 * math.pi / 180.
        #print(' dp =', dp)
        #rp = (12. + 51.4 / 60.) * math.pi / 12.
        #print(' rp =', rp)
        #x0 = 20. * math.cos(18. * math.pi / 12.) * math.cos(30. * math.pi / 180.)
        #print(' x0 =', x0)
        #y0 = 20.0 * math.sin(18.0 * math.pi / 12.0) * math.cos(30.0 * math.pi / 180.0)
        #print(' y0 =', y0)
        #z0 = 20.0 * math.sin(30.0 * math.pi / 180.0)        # sun 20km/s towards ra=18h dec=30.
        #print(' z0 =', z0)

        #decc = -0.5049819302436926
        #cosDecc = math.cos(decc)
        #print(' cosDecc =', cosDecc)
        #sinDecc = math.sin(decc)
        #print(' sinDecc =', sinDecc)
        cosDecc = 0.875183216565868
        sinDecc = -0.48379162605549625

        rac = 4.649120794999895

        #dp = 0.4729842272904633
        #sinDp = math.sin(dp)
        #print(' sinDp =', sinDp)
        #cosDp = math.cos(dp)
        #print(' cosDp =', cosDp)
        sinDp = 0.45554490723351554
        cosDp = 0.8902128046111265

        rp = 3.3658674624710643

        #cosRpMRac = math.cos(rp - rac)
        #print(' cosRpMRac =', cosRpMRac)
        #sinRpMRac = math.sin(rp - rac)
        #print(' sinRpMRac =', sinRpMRac)
        cosRpMRac = 0.28359695364827764
        sinRpMRac = -0.958943568663671

        # readclock() in time.c
        # says
        # t = gmtime(&now);
        # // gmtime Jan 1 is day 0
        # secs = tosecs(t->tm_year + 1900, t->tm_yday + 1, t->tm_hour, t->tm_min, t->tm_sec);

        # FITS format: “[±Y]YYYY-MM-DD[THH:MM:SS[.sss]]”.
        # dataTimeUtcVlsr1900 = Time('1900-01-01T00:00:00', format='fits', scale='utc')
        #   gives a warning: 
        #       WARNING: ErfaWarning: ERFA function "dtf2d" yielded 1 of "dubious year (Note 6)"
        #        [astropy._erfa.core]
        # OK, use year 2000 and add a year of seconds:
        # print(' (dataTimeUtcVlsr2000.mjd - dataTimeUtcVlsr1900.mjd) * 24. * 60. * 60. =',
        #    (dataTimeUtcVlsr2000.mjd - dataTimeUtcVlsr1900.mjd) * 24. * 60. * 60.)
        # gives (dataTimeUtcVlsr2000.mjd - dataTimeUtcVlsr1900.mjd) * 24. * 60. * 60. = 3155673600.0
        # check: 365.25 * 100 * 24. * 60. * 60. = 3155760000 seconds = yup, close
        # diff = 3155760000 - 3155673600.0 = 86400 = 24. * 60. * 60. = 1 day, so use 3155673600. below
        #
        #from astropy.time import Time
        dataTimeUtcVlsr2000 = Time('2000-01-01T00:00:00', format='fits', scale='utc')
        print(' dataTimeUtcVlsr2000.mjd =', dataTimeUtcVlsr2000.mjd)

    elif ezEzbGridAstroMath == 2:
        # use astropy
        from astropy import units as u
        from astropy.coordinates import EarthLocation
        from astropy.coordinates import SkyCoord

        locBase = EarthLocation(lat = ezRAObsLat*u.deg, lon = ezRAObsLon*u.deg, height = ezRAObsAmsl*u.m)

    ## calculate and fill missing ezConOut[n, 20] signal columns

    samplesQtyProcessed = 0

    for n in range(antLen):

        dataTimeUtcStrThis = dataTimeUtc[n].iso

        if ezEzbGridAstroMath == 1:
            # use Python port from MIT Haystack Small Radio Telescope (SRT) geom.c,
            # derivation comments removed in ezCon220826a.py
            if ezEzbGrid != 1:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  ezEzbGridAstroMath of  1  is not supported with')
                print(f'              ezEzbGrid of  {ezEzbGrid}')
                print()
                print()
                print()
                print()
                print()
                exit()

            azimuthRadThis = azimuth[n] * 0.01745329251
            elevationRadThis = elevation[n] * 0.01745329251
            cosElRad = math.cos(elevationRadThis)
            north = math.cos(azimuthRadThis) * cosElRad
            west = -math.sin(azimuthRadThis) * cosElRad
            zen = math.sin(elevationRadThis)

            d1lat = ezRAObsLat * 0.01745329251
            d1lon = ezRAObsLon * 0.01745329251

            cosD1lat = math.cos(d1lat)
            sinD1lat = math.sin(d1lat)
            pole = north * cosD1lat + zen * sinD1lat
            rad = zen * cosD1lat - north * sinD1lat

            dec = math.atan2(pole, math.sqrt(rad * rad + west * west))
            ha = math.atan2(west, rad)

            # with correction factor calculated below = 1.84308208361
            ra = -ha + (((dataTimeUtc[n].mjd * 86400. - 1577899000.5) / 86164.09053) % 1.) * 6.283185307 \
                - d1lon + 1.84308208361
            # 1.8325957145 = 0.29166666666 * 2 * 3.1415926535 radians from UTC for Loveland --- yup

            if ra < 0.:
                ra += 6.283185307
            elif 6.283185307 < ra:
                ra -= 6.283185307
            raDegThis = ra * 57.2957795147          # in degrees
            raHThis = raDegThis / 15.       # 24 / 360 = 1 / 15

            decDegThis = dec * 57.2957795147        # in degrees

            cosRa = math.cos(ra)
            cosDec = math.cos(dec)
            sinRa = math.sin(ra)
            sinDec = math.sin(dec)
            vsun = 3.1817257161747205e-15 * cosRa * cosDec \
                + 17.320508075688775 * sinRa * cosDec - 9.999999999999998 * sinDec

            x0 = cosRa * cosDec
            y0 = sinRa * cosDec
            z0 = sinDec
            y = y0 * 0.9170600744802925 + z0 * 0.3987490687063738

            z = z0 * 0.9170600744802925 - y0 * 0.3987490687063738
            soulat = math.atan2(z, np.sqrt(x0 * x0 + y * y))
            soulong = math.atan2(y, x0)

            # timeVlsr = for this sample n, seconds since start of 1900
            timeVlsr = (dataTimeUtc[n].mjd - dataTimeUtcVlsr2000.mjd) * 86400. + 3155673600.
            sunlong = (timeVlsr * 0.00001140795 + 280.) * 0.01745329251       # long=280 day 1

            vearth = -30. * math.cos(soulat) * math.sin(sunlong - soulong)
            gwest = cosDecc * math.cos(rp - rac)

            grad = cosDecc * math.sin(rp - rac)

            ggwest = gwest * sinDp + 0.43067750027824064

            gpole = gwest * cosDp - 0.22038881141180267

            lon0 = (math.atan2(ggwest, grad)) * 57.2957795147
            gwest = cosDec * math.cos(rp - ra)

            grad = cosDec * math.sin(rp - ra)

            ggwest = gwest * sinDp - sinDec * cosDp

            gpole = gwest * cosDp + sinDec * sinDp

            d1glat = (math.atan2(gpole, math.sqrt(ggwest * ggwest + grad * grad))) * 57.2957795147
            gLatDegThis = d1glat            # in degrees

            d1glon = (math.atan2(ggwest, grad)) * 57.2957795147 - lon0

            # map d1glon into (-180 to +180) degrees
            gLonDegThis = d1glon
            if gLonDegThis < -180.:
                gLonDegThis += 360.
            elif 180. < gLonDegThis:        # in degrees (+180 to +540) to (0 to +360)
                gLonDegThis -= 360.

            if ezEzbGridUseVlsr:
                vlsrThis = vsun + vearth    # km/s
            else:
                vlsrThis = 0.               # km/s

        elif ezEzbGridAstroMath == 2:
            # use astropy

            # Coordinate of sky target at the UTC time from the data file
            # SkyCoord() wants time = Time('1991-06-06 12:00:00')

            if ezEzbGrid == 1:
                # AzEl grid
                # extract 6 "This" coordinates
                azDegThis = azDeg[n]        # degrees
                elDegThis = elDeg[n]        # degrees

                cTarget = SkyCoord(az = azDegThis*u.deg, alt = elDegThis*u.deg,
                    obstime = dataTimeUtcStrThis, frame = 'altaz', location = locBase)

                raDegThis = float(cTarget.icrs.ra.degree)
                raHThis = raDegThis / 15.       # 24 / 360 = 1 / 15
                decDegThis = float(cTarget.icrs.dec.degree)

                gLatDegThis = float(cTarget.galactic.b.degree)
                gLonDegThis = float(cTarget.galactic.l.degree)
                if 180. < gLonDegThis:
                    gLonDegThis -= 360.
                
            elif ezEzbGrid == 2:
                # RaDec grid
                # extract 6 "This" coordinates
                raDegThis  = raDeg[n]       # hours
                decDegThis = decDeg[n]      # degrees

                cTarget = SkyCoord(ra=raDegThis*15.*u.deg, dec=decDegThis*u.deg,
                    obstime = dataTimeUtcStrThis, frame = 'icrs', location = locBase)

                azDegThis = float(cTarget.altaz.az.degree)
                elDegThis = float(cTarget.altaz.alt.degree)

                gLatDegThis = float(cTarget.galactic.b.degree)
                gLonDegThis = float(cTarget.galactic.l.degree)
                if 180. < gLonDegThis:
                    gLonDegThis -= 360.

            else:
                # GLatGLon grid
                # extract 6 "This" coordinates
                gLatDegThis = gLatDeg[n]    # degrees
                gLonDegThis = gLonDeg[n]    # degrees

                cTarget = SkyCoord(b=gLatDegThis*u.deg, l=gLonDegThis*u.deg,
                    obstime = dataTimeUtcStrThis, frame = 'galactic', location = locBase)

                azDegThis = float(cTarget.altaz.az.degree)
                elDegThis = float(cTarget.altaz.alt.degree)

                raDegThis = float(cTarget.icrs.ra.degree)
                raHThis = raDegThis / 15.       # 24 / 360 = 1 / 15
                decDegThis = float(cTarget.icrs.dec.degree)

            if ezEzbGridUseVlsr:        # astropy
                # https://astropy-cjhang.readthedocs.io/en/latest/api/
                #   astropy.coordinates.SkyCoord.html#astropy.coordinates.SkyCoord.radial_velocity_correction
                # brvc = barycentric radial velocity correction
                brvcThis = cTarget.radial_velocity_correction(kind='barycentric')    # in m/sec

                # Barycentric Radial Velocity Correction in km/s
                vlsrThis = -float(brvcThis / (1000. * u.m / u.s))      # to extract from units as km/s
            else:
                vlsrThis = 0.       # km/s

        else:
            # ezEzbGridAstroMath == 0:
            # fill with suspicious harmless values, to be ignored, faster ?
            azDegThis   = 0.            # degrees
            elDegThis   = 0.            # degrees
            raHThis     = 0.            # hours
            decDegThis  = 0.            # degrees
            gLatDegThis = 0.            # degrees
            gLonDegThis = 0.            # degrees
            vlsrThis    = 0.        # km/s

        # store in ezConOut[n, column] coordinate columns (0.0 for unfinished antXTVLdDop and antXTVUdDop)
        # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  Spare1  Spare2  Spare3
        #          0           1    2       3        4        5     6      7       8       9
        #   AntAvg  AntMax    RefAvg  RefMax
        #   10      11        12      13
        #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
        #   14       15          16        17         18          19
        if not samplesQtyProcessed:
            ezConOut = np.array([
                dataTimeUtc[n].mjd, raHThis, decDegThis, gLatDegThis, gLonDegThis, vlsrThis,
                1., azDegThis, elDegThis, 0.,
                1., 2., 3., 4.,
                5., n, 7., 8., 9., 1.])
        else:
            ezConOut = np.concatenate([ezConOut, np.array([
                dataTimeUtc[n].mjd, raHThis, decDegThis, gLatDegThis, gLonDegThis, vlsrThis,
                1., azDegThis, elDegThis, 0.,
                1., 2., 3., 4.,
                5., n, 7., 8., 9., 1.]) ])


        samplesQtyProcessed += 1

        # allow append to line
        print('\r  ', fileNameLast, '  Total samples processed for signals     =',
            f'{samplesQtyProcessed:,} of {antLen:,}', end='')

    print()
    ezConOut = np.reshape(ezConOut, (-1, 20))
    #print(np.shape(ezConOut))

    # make column 11 plot background yellow to improve trace contrast
    ezConOut[0, 11] = 0.
    # make column 12 plot background yellow to improve trace contrast
    ezConOut[0, 12] = 5.



def writeFileEzb():

    global programRevision          # string
    global commandString            # string
    global ezRAObsName              # string
    global fileWriteEzb             # file handle

    global ezConOut                 # float and int 2d array

    print()
    print('   writeFileEzb ===============')

    # record the (complex?) ezCon command line as a comment at the top of .ezb file
    fileWriteEzb.write(f'\n# from {programRevision}\n')
    fileWriteEzb.write(f'# {commandString}\n\n')
    fileWriteEzb.write(f'lat {ezRAObsLat} long {ezRAObsLon} amsl {ezRAObsAmsl} name {ezRAObsName}\n')
    fileWriteEzb.write(f'freqMin {fileFreqMin} freqMax {fileFreqMax} freqBinQty {fileFreqBinQty}\n')
    fileWriteEzb.write( \
        'ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  Spare1  Spare2  AntXCMDop' \
        + '    AntAvg  AntMax    RefAvg  RefMax' \
        + '    AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax\n')
    fileWriteEzb.write( \
        '#        0           1    2       3        4        5     6      7       8       9        ' \
        + '    10      11        12      13    ' \
        + '    14       15         16        17          18          19\n')

    # save ezConOut[] in columns
    # experimentEzc for AzEl into .ezb Spare1 and Spare2
    #    '%0.5f %0.3f %0.3f %0.3f %0.3f %0.3e %d %d %d %d ' + \
    ezConOutFmtS = \
        '%0.5f %0.3f %0.3f %0.3f %0.3f %0.3e %d %0.1f %0.1f %0.5e ' + \
        '%0.5e %0.5e %0.5e %0.5e ' + \
        '%0.5e %0.5e %0.5e %0.5e %0.5e %0.5e'
    for n in range(antLen):
        np.savetxt(fileWriteEzb, [ezConOut[n, :]], fmt = ezConOutFmtS)
    fileWriteEzb.write('\n')
    fileWriteEzb.close()   



def printGoodbye(startTime):

    global antLen                   # integer
    global programRevision          # string
    global commandString            # string

    global ezEzbGridUseVlsr         # integer

    # print status
    if 0:
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezEzbGrid       =', ezEzbGrid)
        print('   ezEzbGridRangeL =', ezEzbGridRangeL)
        print('   ezEzbGridBoxL   =', ezEzbGridBoxL)
        print('   ezEzbGridLineL  =', ezEzbGridLineL)
        print()
        print('   ezEzbGridAstroMath =', ezEzbGridAstroMath)
        print('   ezEzbGridUseVlsr   =', ezEzbGridUseVlsr)
        print()
        print('   ezEzbGridDateTime =', ezEzbGridDateTimeS)
        print()
        print(f'   antLen = {antLen:,}')

    stopTime = time.time()
    stopTimeS = time.ctime()
    OutString = f' antLen = {antLen:,}\n'
    OutString += '\n That Python command\n'
    OutString += f'  {commandString}\n'
    OutString += f' took {int(stopTime-startTime)} seconds = {(stopTime-startTime)/60.:1.1f} minutes\n'
    OutString += f' Now = {stopTimeS[:-5]}\n'
    OutString += f'\n programRevision = {programRevision}\n'
    print(OutString)
    #fileWriteStudy.write(OutString)

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



#A#####################################################################################



def main():

    startTime = time.time()

    printHello()
    
    ezEzbGridArguments()

    readDataDir()           # creates ezRAObsLat, ezRAObsLon, ezRAObsAmsl, ezRAObsName
                            #   fileFreqMin, fileFreqMax, fileFreqBinQty, 
                            #   azimuth, elevation, dataTimeUtc, raw, rawLen, fileNameLast

    openFileEzb()           # In case it will eventually error.  Creates fileWriteNameEzb, fileWriteEzb

    # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  Spare1  Spare2  Spare3
    #          0           1    2       3        4        5     6      7       8       9
    #   AntAvg  AntMax    RefAvg  RefMax
    #   10      11        12      13
    #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
    #   14       15          16        17         18          19
    createEzConOutEzb()                 # using ezEzbGridAstroMath, creates partial ezConOut,
                                        # deletes antAvg, antMax, refAvg, refMax,
                                        #   antBAvg, antBMax, antRBAvg, antRBMax

    writeFileEzb()

    printGoodbye(startTime)



if __name__== '__main__':
  main()

