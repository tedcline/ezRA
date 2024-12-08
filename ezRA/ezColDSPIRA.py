programName = 'ezColDSPIRA240801a.py'
programRevision  = programName

# ezRA - Easy Radio Astronomy ezColDSPIRA Data COLlector program,
#   converting data from the DSPIRA .csv radio spectrum data format
#   into integrated frequency spectrum data ezRA .txt files,
#   into the "data" directory.
#   https://wvurail.org/dspira-lessons
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

# ezColDSPIRA240801a, fileWrite.write() f string
# ezColDSPIRA240721b, use comment
# ezColDSPIRA240721a, create new 'data' directory if needed
#   -overwriteFile
# ezColDSPIRA240715c, use '-ezColUtcOffset -6' for summer Colorado
# ezColDSPIRA240715b, ezColUtcOffset from ezColIFAvg230305a
# ezColDSPIRA240715a, from ezColIFAvg230305a

# ezColIFAvg230305a.py, boilerplate from ezSky
# ===========skipping ezColIFAvg221126a.py, create new 'data' directory if needed
# ezColIFAvg220930a.py, prep for Git
# ezColIFAvg01N.py, sort input file directory,
# ezColIFAvg01L.py, first try, convert one "IF Average Plugin" .txt output radio spectrum data file
#         to ezRA .txt radio spectrum data file.
#     The "IF Average Plugin" radio spectrum data collection method is described in the "cheap-and-easy" post,
#         https://www.rtl-sdr.com/cheap-and-easy-hydrogen-line-radio-astronomy-with-a-rtl-sdr-wifi-parabolic-
#             grid-dish-lna-and-sdrsharp/
#     The "IF Average Plugin" radio spectrum data collection method is delivered with the 
#         Society of Amateur Radio Astronomers (SARA) introductory Scope-in-a-Box,
#         https://www.radio-astronomy.org/store/projects/scope-in-a-box
#     The "IF Average Plugin" .txt output radio spectrum data file looks like,
#         4/28/2021 6:43:57 AM  Counts:451000
#         1419.205000000  0.322551440
#         1419.207343750  0.320824318
#         1419.209687500  0.318060119
#         ...
#         1421.597968750  0.327361641
#         1421.600312500  0.326069956
#         1421.602656250  0.323774396
# 
#     Write output files into 'data' directory.  Assumes 'data' directory exists.

import os                       # used to grab all files in the current directory
import sys                
import time
#import datetime

#from astropy import units as u
from astropy.time import Time

import numpy as np


def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezColDSPIRA.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezColDSPIRA.py [optional arguments] radioDataFileDirectories')
    print()
    print('  ezRA - Easy Radio Astronomy ezColDSPIRA Data COLlector program,')
    print('  converting data from the DSPIRA .csv radio spectrum data format')
    print('  into integrated frequency spectrum data ezRA .txt files,')
    print('  into the "data" directory.')
    print('  https://wvurail.org/dspira-lessons')
    print()
    print('  "radioDataFileDirectories" may be one or more .csv radio data files:')
    print('         py  ezColDSPIRA.py  220122_0005.csv')
    print('         py  ezColDSPIRA.py  220122_0005.csv 220122_0006.csv')
    print('         py  ezColDSPIRA.py  220122_*.csv')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezColDSPIRA.py  220122')
    print('         py  ezColDSPIRA.py  220122 220123')
    print('         py  ezColDSPIRA.py  2201*')
    print('  "radioDataFileDirectories" may be a mix of .csv radio data files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezColDSPIRA program,')
    print('  then in order from ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  python ezColDSPIRA.py -help        (print this help)')
    print('  python ezColDSPIRA.py -h           (print this help)')
    print()
    print('    -ezRAObsName     bigDish 8       (Observatory Name)')
    print('    -ezRAObsLat      40.2            (Observatory Latitude  (degrees))')
    print('    -ezRAObsLon      -105.1          (Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl     1524            (Observatory Above Mean Sea Level (meters))')
    #print('    -ezColFileNamePrefix bigDish8    (Data File Name Prefix)')
    print()
    print('    -ezColAzimuth    180.0           (Azimuth   pointing of antenna (degrees))')
    print('    -ezColElevation  45.0            (Elevation pointing of antenna (degrees))')
    print()
    print('    -ezColUtcOffset  -6      (time zone adjust, -6 for summer Colorado USA')
    print("    -overwriteFile    0      (0 to NOT overwrite existing 'data' directory files")
    print()
    print(r'    -ezDefaultsFile ..\bigDish8.txt     (Additional file of default arguments)')
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
    global cmd                      # string

    #print(' startTime = ', startTime)
    #print(' time.asctime(time.time() = %s ' % time.asctime(time.time()))
    #print(' time.asctime(time.localtime() = %s ' % time.asctime(time.localtime()))
    print()
    print('=================================================')
    #print(' Local time = %s ' % time.asctime(time.localtime()))
    print(' Local time =', time.asctime(time.localtime()))

    print(' programRevision =', programRevision)
    print()

    #print(sys.argv)
    #print(len(sys.argv))
    cmd = ''
    for i in sys.argv:
        #cmd = cmd + i + '  '
        cmd += i + '  '
    print(' This Python command = ' + cmd)



def ezColArgumentsFileRead(ezColArgumentsFileNameInput):
    # process arguments from file

    #global programRevision                  # string
    #global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    #global ezColFileNamePrefix              # string

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColUtcOffset                   # float

    #global cmdDirectoryS                    # string            creation


    print()
    print('   ezColArgumentsFileRead(' + ezColArgumentsFileNameInput + ') ===============')

    #ezDefaultsFileName = r'.\ezDefaults.txt'
    #ezDefaultsFileName = 'ezDefaults.txt'
    #ezDefaultstFileName = os.path.dirname(__file__) + r'\ezDefaults.txt'
    #print(' os.path.dirname(__file__) =' + os.path.dirname(__file__) + '=')
    #print(' len(os.path.dirname(__file__)) = ', len(os.path.dirname(__file__)))
    if os.path.sep in ezColArgumentsFileNameInput:
        ezDefaultsFileName = ezColArgumentsFileNameInput
    else:
        # try looking in the same directory as this ezCol program
        if os.path.dirname(__file__):
            ezDefaultsFileName = os.path.dirname(__file__) + os.path.sep + ezColArgumentsFileNameInput
        else:
            ezDefaultsFileName = '.'  + os.path.sep + ezColArgumentsFileNameInput

    print()
    print('  ', ezDefaultsFileName)


    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileName, 'r')

        #if fileDefaults.mode == 'r':
        # process each line in ezDefaultsFileName
        while 1:
            #print()
            fileLine = fileDefaults.readline()
            #print(fileLine)

            # LF always present: 0=EOF  1=LF  2=1Character
            if len(fileLine) < 1:         # if end of file
                break                     # get out of while loop

            thisLine = fileLine.split()
            if len(thisLine) < 1:         # if line all whitespace
                continue                  # skip to next line

            #print('=', thisLine[0], '=')
            #print('=', thisLine[0][0], '=', '#', '=')
            if thisLine[0][0] == '#':    # ignoring whitespace, if first character of first word
                continue                  # it is a comment, skip to next line


            # be kind, ignore argument keyword capitalization
            thisLine0Lower = thisLine[0].lower()
            #print('= thisLine0Lower =', thisLine0Lower, '=')

            # process recognised arguments used by this program

            # ezRA family arguments
            if thisLine0Lower == '-ezRAObsName'.lower():
                ezRAObsName = thisLine[1]
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])

            elif thisLine0Lower == '-ezRAObsLat'.lower():
                ezRAObsLat  = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsLon'.lower():
                ezRAObsLon  = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsAmsl'.lower():
                ezRAObsAmsl = float(thisLine[1])

            #elif thisLine0Lower == '-ezColFileNamePrefix'.lower():
            #    ezColFileNamePrefix = thisLine[1]


            # ezCol arguments
            # float arguments
            elif thisLine0Lower == '-ezColAzimuth'.lower():
                ezColAzimuth = float(thisLine[1])

            elif thisLine0Lower == '-ezColElevation'.lower():
                ezColElevation = float(thisLine[1])

            elif thisLine0Lower == '-ezColUtcOffset'.lower():
                ezColUtcOffset = float(thisLine[1])

            elif thisLine0Lower[:5] == '-ezCol'.lower():
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Defaults file ( ' + ezDefaultsFileName + ' )')
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
    	print ()
    	print ()
    	print ()
    	print ()
    	print ('   Warning: Error in opening file or reading ' + ezDefaultsFileName + ' file.')
    	#print ('   ... Using defaults ...')
    	print ()
    	print ()
    	print ()
    	print ()

    else:
        fileDefaults.close()       #   then have processed all available lines in this defaults file



def ezColArgumentsCommandLine():
    # process arguments from command line

    #global programRevision                  # string
    global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    #global ezColFileNamePrefix              # string

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColUtcOffset                   # float
    global overwriteFile                    # integer

    global cmdDirectoryS                    # string            creation



    print()
    print('   ezColArgumentsCommandLine ===============')

    cmdLineSplit = cmd.split()
    cmdLineSplitLen = len(cmdLineSplit)
        
    #if cmdLineSplitLen < 2:
    #    # need at least one data directory or file
    #    printUsage()

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
            # Must be an argument.
            # Remove '-'
            cmdLineArg = cmdLineSplit[cmdLineSplitIndex][1:]
            # ignoring whitespace, first character of cmdLineSplit word was '-', now removed
            if cmdLineArg[0] == '-':
                cmdLineArg = cmdLineArg[1:]
                # ignoring whitespace, first 2 characters of cmdLineSplit word were '--', now removed

            cmdLineArgLower = cmdLineArg.lower()
            #print('= cmdLineArg =', cmdLineArg, '=')
            cmdLineSplitIndex += 1      # point to first argument value

            # ezRA arguments used by multiple programs:
            if cmdLineArgLower == 'help':
                printUsage()

            if cmdLineArgLower == 'h':
                printUsage()

            elif cmdLineArgLower == 'ezRAObsName'.lower():
                ezRAObsName = cmdLineSplit[cmdLineSplitIndex]   # cmd line allows only one ezRAObsName word
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])
            
            elif cmdLineArgLower == 'ezRAObsLat'.lower():
                ezRAObsLat  = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezRAObsLon'.lower():
                ezRAObsLon  = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezRAObsAmsl'.lower():
                ezRAObsAmsl = float(cmdLineSplit[cmdLineSplitIndex])

            #elif cmdLineArgLower == 'ezColFileNamePrefix'.lower():
            #    ezColFileNamePrefix = cmdLineSplit[cmdLineSplitIndex]


            # float arguments:
            elif cmdLineArgLower == 'ezColAzimuth'.lower():
                ezColAzimuth = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezColElevation'.lower():
                ezColElevation = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezColUtcOffset'.lower():
                ezColUtcOffset = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'overwriteFile'.lower():
                overwriteFile = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezDefaultsFile'.lower():
                ezColArgumentsFileRead(cmdLineSplit[cmdLineSplitIndex])

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



def ezColArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    #global programRevision                  # string
    #global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    #global ezColFileNamePrefix              # string

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColUtcOffset                   # float
    global overwriteFile                    # integer

    #global cmdDirectoryS                    # string            creation


    # defaults
    if 1:
        ezRAObsName = 'default KS'          # Geographic Center of USA, near Lebanon, Kansas
        ezRAObsLat  =  39.8282              # Observatory Latitude  (degrees)
        ezRAObsLon  = -98.5696              # Observatory Longitude (degrees)
        ezRAObsAmsl = 563.88                # Observatory Above Mean Sea Level (meters)
        ezColFileNamePrefix = ''

        ezColAzimuth   = 180.0              # Azimuth   pointing of antenna (degrees)
        ezColElevation =  45.0              # Elevation pointing of antenna (degrees)

        ezColUtcOffset = 0.                 # timezone correction
        overwriteFile  = 1                  # 1 to overwrite existing 'data' directory files

    ezColArgumentsFileRead('ezDefaults.txt')    # process arguments from default ezDefaults.txt file

    ezColArgumentsCommandLine()         # process arguments from command line

    if not ezColFileNamePrefix:
        ezColFileNamePrefix = ezRAObsName.split()[0]        # first word of ezRAObsName

    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        #print('   ezColFileNamePrefix =', ezColFileNamePrefix)
        print()
        print('   ezColAzimuth   =', ezColAzimuth)
        print('   ezColElevation =', ezColElevation)
        print()
        print('   ezColUtcOffset =', ezColUtcOffset)
        print('   overwriteFile =', overwriteFile)



def printGoodbye(startTime):

    global programRevision          # string
    global cmd                      # string

    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        #print('   ezColFileNamePrefix =', ezColFileNamePrefix)
        print()
        print('   ezColAzimuth   =', ezColAzimuth)
        print('   ezColElevation =', ezColElevation)
        print()
        print('   ezColUtcOffset =', ezColUtcOffset)
        print('   overwriteFile =', overwriteFile)

    stopTime = time.time()
    stopTimeS = time.ctime()
    print()
    print(' That Python command')
    print('   ' + cmd + '           ')
    print(' took %d seconds = %1.1F minutes' % ((int(stopTime-startTime)),
        (float(int(stopTime-startTime))/60.))) # xxxxxx.x minutes
    print(' Now = %s' % stopTimeS[:-5])

    #print(' Helpful commands:')
    print()
    print(' ( programRevision =', programRevision, ')')
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



#########################################################################################################
# Main method
def main():

    global programRevision                  # string
    global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    #global ezColFileNamePrefix              # string

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColUtcOffset                   # float
    global overwriteFile                    # integer

    global cmdDirectoryS                    # string            creation


    startTime = time.time()

    print()
    print(programRevision)
    print()

    printHello()
    
    ezColArguments()

    if ezColUtcOffset:
        # prepare for UTC/local time shift, using ezColUtcOffset
        # create Time object of timeDeltaUtc (= Local to UTC)

        # first, create Time object of noon UTC on 2020-01-23
        time12UtcStr = '2020-01-23 12:00:00'
        #print('time12UtcStr =' + time12UtcStr + '=')
        time12Utc = Time(time12UtcStr, format='iso', scale='utc')
        #print(time12Utc)
        #print( 'time12Utc =', time12Utc)
        #print()

        # second, create Time object for local of that noon UTC on 2020-01-23
        timeLocal12UtcStr = '2020-01-23 ' + ('0' + str(int(12 + ezColUtcOffset)))[-2:] + ':00:00'
        #print('sdrUtcOffset =' + str(int(sdrUtcOffset)) + '=')
        #print('str(int(12 + sdrUtcOffset)) =' + str(int(12 + sdrUtcOffset)) + '=')
        #print('timeLocalStr =' + timeLocal12UtcStr + '=')
        timeLocal12Utc = Time(timeLocal12UtcStr, format='iso', scale='utc')
        #print(timeLocal12Utc)
        #print( 'timeLocal12Utc =', timeLocal12Utc)
        #print()

        # third, get difference
        timeUtcDelta = time12Utc - timeLocal12Utc
        #print(timeUtcDelta)
        #print( 'timeUtcDelta =', timeUtcDelta)
        #print()

        # now prepared for UTC/local time shift

    ###################################################################################

    # Open each data file and read individual lines

    #samplesQty     = 0              # current number of samples from all files
    #calQty         = 0              # current number of calibration samples
    #fileWriteNamePostS = 'abcdefghijklmnopqrstuvwxyz'

    samplesFileOutQty = 0           # current number of samples to output file
    fileWrite = ''

    #    if len(sys.argv) > 1:
    #        #directoryList = sorted(sys.argv[1:])
    #        #directoryList = sys.argv[1:]
    #        directoryList = cmdDirectoryS.split()
    #        directoryListLen = len(directoryList)
    #    else:
    #        directoryList = ['.']
    #        directoryListLen = 1
    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    #print(directoryList)
    #print(directoryListLen)

    # if does not exist - create new 'data' directory
    if not os.path.exists('data'):
        os.makedirs('data')
        print(' Created new "data" directory')

    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]
        #if(directory.lower().endswith('.txt')):
        if(directory.lower().endswith('.csv')):
            fileList = [directory]
            directory = '.'
        else:
            #fileList = os.listdir(directory)
            fileList = sorted(os.listdir(directory))        # each directory is now sorted alphabetically
        #print(fileList)
        fileListLen = len(fileList)
        #print(fileListLen)
        print()
        dateUTCSLast = ''       # flag to force new fileWrite
        for fileCtr in range(fileListLen):
            fileName = fileList[fileCtr]
            #print(fileName)

            #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
            #    + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
            #    + ' = ' + directory + r'\' + fileName + \
            #    '                       ', end='')   # allow append to line
            print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
                + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
                + ' = ' + directory + os.path.sep + fileName + \
                '                       ', end='')   # allow append to line
            #if(fileName.lower().endswith('.txt')):
            #    fileRead = open(directory + r'\' + fileName, 'r')
            #if(fileName.lower().endswith('.txt')):
            if(fileName.lower().endswith('.csv')):
                if fileName[0] == '/':
                    fileRead = open(fileName, 'r')
                else:
                    fileRead = open(directory + os.path.sep + fileName, 'r')

                if fileRead.mode == 'r':
                    #print(' samplesFileOutQty =', str(samplesFileOutQty))

                    # filename
                    # 2024-07-15_11.48.44.3_N0RQV_180_45_spectrum.csv
                    # 0          1          2     3   4  5
                    # 01234567890
                    #            01234567890
                    # N0RQV240715_11.txt

                    fileNameSplitL = fileName.split('_')
                    #print()
                    #print('======== fileNameSplitL =', fileNameSplitL)

                    # want 2024-07-15T11:48:44.3 10.523690382 10.570080895 10.535587705 ...
                    dateFileS = fileNameSplitL[0]               # 2024-07-15
                    timeFileS = fileNameSplitL[1][0:2] + ':' \
                        + fileNameSplitL[1][3:5] + ':' \
                        + fileNameSplitL[1][6:]                 # 11:48:44.3
                    ezRAObsName = fileNameSplitL[2]
                    ezColAzimuthS = fileNameSplitL[3]
                    ezColElevationS = fileNameSplitL[4]

                    #print('======== dateFileS =', dateFileS)
                    #print('======== timeFileS =', timeFileS)
                    #print('======== ezRAObsName =', ezRAObsName)
                    #print('======== ezColAzimuthS =', ezColAzimuthS)
                    #print('======== ezColElevationS =', ezColElevationS)

                    dateTimeStrThis = dateFileS + 'T' + timeFileS
                    #print('dateTimeStrThis =' + dateTimeStrThis + '=')

                    if ezColUtcOffset:
                        # Bases: astropy.time.TimeString
                        # FITS format: “[±Y]YYYY-MM-DD[THH:MM:SS[.sss]]”.
                        # https://docs.astropy.org/en/stable/time/#id3
                        # fits  TimeFITS  ‘2000-01-01T00:00:00.000’

                        # convert to UTC: convert dateTimeStrThis to dateTimeUtcThis

                        dateTime = Time(dateTimeStrThis, format='fits', scale='utc')
                        #print( 'dateTime =', dateTime)
                        #print()

                        # add that UTC difference to file's dateTime
                        dateTimeUtcThis = dateTime + timeUtcDelta
                        #print(dateTimeUtcThis)
                        #print( 'dateTimeUtcThis =', dateTimeUtcThis)
                        #print()

                        # get string of that sum
                        #dateTimeUtcStrThis = dateTimeUtcThis.iso
                        dateTimeUtcStrThis = dateTimeUtcThis.fits   # 2024-07-15T11:48:44.3
                        #                                               24 07 15 11
                        #                                             01234567890123
                        #print()
                        #print('dateTimeUtcStrThis =' + dateTimeUtcStrThis + '=')
                        dateUTCS = dateTimeUtcStrThis[2:4] + dateTimeUtcStrThis[5:7] \
                                + dateTimeUtcStrThis[8:10]
                    else:
                        dateUTCS = dateFileS
                        dateTimeUtcStrThis = dateTimeStrThis

                    # read radio data
                    # 1.414000000000000000e+03,2.720000036060810089e-02
                    # 1.414002400000000080e+03,3.480000048875808716e-02
                    # 1.414004899999999907e+03,4.010000079870223999e-02
                    # ...
                    freqBinQty = 0
                    radDataS = ''                   # RADio DATA long string
                    fileLine = fileRead.readline()
                    while 1 < len(fileLine):
                        thisLineSplit = fileLine.split(',')
                        if not freqBinQty:
                            dataFreqMin = float(thisLineSplit[0])
                        radDataS += ' ' + thisLineSplit[1][:-1]  # trim off last character '\n'
                        freqBinQty += 1
                        fileLine = fileRead.readline()
                    dataFreqMax = float(thisLineSplit[0])
                    fileRead.close()

                    if not freqBinQty:
                        print()
                        print('     No data, so skipping', fileName)
                        print()
                        break                    #   onto next file, do not save any data

                    # now have dataFreqMin, dataFreqMax, and freqBinQty

                    # if need new fileWrite
                    if dateUTCSLast != dateUTCS:
                    
                        # close any last fileWrite data file
                        if len(dateUTCSLast):
                            fileWrite.close()

                        dateUTCSLast = dateUTCS

                        # begin a new fileWriteName file with header
                        # dateTimeUtcStrThis is 2024-07-15T11:48:44.3
                        #                       01234567890123
                        # want fileWriteName like N0RQV240715_11.txt
                        fileWriteName = 'data' + os.path.sep + ezRAObsName \
                            + dateUTCS + '_' + dateTimeUtcStrThis[11:13] + '.txt'

                        if not overwriteFile:
                            # create unused output filename
                            #fileWriteNameRootS = 'data' + os.path.sep \
                            #    + fileReadName.split(os.path.sep)[-1][:-4]
                            fileWriteNameRootS = fileWriteName[:-4]     # without '.txt'
                            # try with one trailing character
                            fileWriteNamePostS = 'bcdefghijklmnopqrstuvwxyz'
                            for i in range(25):
                                fileWriteName = fileWriteNameRootS + fileWriteNamePostS[i] + '.txt'
                                # if fileWriteName is available
                                if not os.path.exists(fileWriteName):
                                    break               # get out of FOR loop
                            else:
                                # no available filenames
                                print()
                                print()
                                print()
                                print()
                                print()
                                print(' ========== FATAL ERROR: already too many files with',
                                    'same fileName base:')
                                print(fileWriteNameRootS)
                                print()
                                print()
                                print()
                                print()
                                print()
                                exit()
                        fileWrite = open(fileWriteName, 'w')

                        # write file header

                        ## 220301 new format
                        ## ezRA ezCol .txt daily data file with 3-line non-comment header and
                        ##   1-line samples each with timestamp and 256 values:
                        ##
                        ## from ezCol04b5ea.py
                        ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb
                        ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
                        ## az 227.9 el 42.7 
                        ## # times are in UTC
                        ## 2022-03-01T05:30:55 10.523690382 10.570080895 10.535587705 ...
                        ## 2022-03-01T05:31:56 10.558290361 10.551762452 10.545512521 ...
                        ## ...
                        ## az 227.9 el 42.7 
                        ## 2022-03-01T06:32:55 10.523690382 10.570080895 10.535587705 ...
                        ## 2022-03-01T06:33:56 10.558290361 10.551762452 10.545512521 ...
                        ## ...

                        fileWrite.write(
                            f'from {programRevision} {cmd}\n' \
                            + f'lat {ezRAObsLat:g} long {ezRAObsLon:g} amsl {ezRAObsAmsl:g} ' \
                            + 'name ' + ezRAObsName \
                            + f'\nfreqMin {dataFreqMin:g} freqMax {dataFreqMax:g} ' \
                            + f'freqBinQty {freqBinQty:d}' \
                            + f'\nazDeg {ezColAzimuthS} elDeg {ezColElevationS}' \
                            + '\n# times are in UTC\n')
                        ezColAzimuthSLast = ezColAzimuthS
                        ezColElevationSLast = ezColElevationS

                    if ezColAzimuthSLast != ezColAzimuthS or ezColElevationSLast != ezColElevationS:
                        fileWrite.write(f'azDeg {ezColAzimuthS} elDeg {ezColElevationS}' + '\n')
                        ezColAzimuthSLast = ezColAzimuthS
                        ezColElevationSLast = ezColElevationS

                    #print(radDataS + '\n')
                    # write radio data
                    #fileWrite.write(dateS + 'T' + timeS + radDataS + '\n')
                    fileWrite.write(dateTimeUtcStrThis + radDataS + '\n')

                    fileNameLast = fileName

                    samplesFileOutQty += 1

                    #print('      samplesFileQty = ' + str(samplesFileQty) + \
                    #    '         ', end='')   # allow append to line

                    # now have processed that line in that input file that ends with .csv and allows read
                
                # now have processed all lines in that input file that ends with .csv and allows read
                #if fileRead.mode == 'r':

            # now have processed that output file
            #if(fileName.lower().endswith('.csv')):
            #print()

        # now have processed that directory
        #for fileCtr in range(fileListLen):

    # now have processed all directories
    #for directoryCounter in range(directoryListLen):

    #print(' fileWrite =', fileWrite)
    if fileWrite:
        fileWrite.close()

    # blank out the last filename
    print('\r                                                                              ' \
        + '                                                                                ')

    print()
    print()
    print(' Total samples read =', str(samplesFileOutQty))

    if not samplesFileOutQty:
        print()
        print()
        print()
        print(" ========== FATAL ERROR: no data loaded from files")
        print()
        print()
        print()
        exit()

    printGoodbye(startTime)

    ###################################################################################

if __name__ == "__main__":
    main()

# a@u22-221222a:~/ezRABase/dspira$           
# python3 ../ezRA/ezColDSPIRA240721b.py  -ezRAObsLat 40.2  -ezRAObsLon -105.1  -ezRAObsAmsl 1524  -ezColUtcOffset -6  -overwriteFile 1  dspira240721
# python3 ../ezRA/ezCon.py  -ezConPlotRangeL 87 97  -exzConRawSamplesUseL data/N0RQV240721_00.txt  -exzConAntXInput  -ezConAntXTFreqBinsFracL 0.61 0.68
# python3 ../ezRA/ezSky.py  -exzConPlotRangeL   -exzConRawSamplesUseL  -ezSkyInput 19 .

