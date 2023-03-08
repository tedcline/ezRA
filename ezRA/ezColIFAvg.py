programName = 'ezColIFAvg220930a.py'
programRevision  = programName

# ezRA - Easy Radio Astronomy ezColIFAvg Data COLlector program,
#   converting data from the "IF Average Plugin" radio spectrum data
#   collection method from "cheap-and-easy" post .txt data format.
#   COLlect radio signals into integrated frequency spectrum data ezRA .txt files.
# https://github.com/tedcline/ezRA

# Copyright (c) 2023, Ted Cline   TedClineGit@gmail.com

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

    #global cmdDirectoryS                    # string            creation


    print()
    print('   ezColArgumentsFileRead(' + ezColArgumentsFileNameInput + ') ===============')

    #ezDefaultsFileName = '.\\ezDefaults.txt'
    #ezDefaultsFileName = 'ezDefaults.txt'
    #ezDefaultstFileName = os.path.dirname(__file__) + '\ezDefaults.txt'
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



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezColIFAvg.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezColIFAvg.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezColIFAvg data Collector converter program')
    print('  to read IFAvg format .txt radio spectrum data text file(s),')
    print('  and write one ezRA .txt radio spectrum data text file into the assumed')
    print('  "data" directory.')
    print()
    print('  "radioDataFileDirectories" may be one or more .txt radio data files:')
    print('         py  ezColIFAvg.py  220122_0005.txt')
    print('         py  ezColIFAvg.py  220122_0005.txt 220122_0006.txt')
    print('         py  ezColIFAvg.py  220122_*.txt')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezColIFAvg.py  220122')
    print('         py  ezColIFAvg.py  220122 220123')
    print('         py  ezColIFAvg.py  2201*')
    print('  "radioDataFileDirectories" may be a mix of .txt radio data files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezColIFAvg program,')
    print('  then in order from ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  python ezColIFAvg.py -help         (print this help)')
    print('  python ezColIFAvg.py -h            (print this help)')
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
    print('    -ezDefaultsFile ..\\bigDish8.txt     (Additional file of default arguments)')
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

    global cmdDirectoryS                    # string            creation


    startTime = time.time()

    print()
    print(programRevision)
    print()

    printHello()
    
    ezColArguments()


    ###################################################################################

    # Open each data file and read individual lines

    #samplesQty     = 0              # current number of samples from all files
    #calQty         = 0              # current number of calibration samples
    #fileWriteNamePostS = 'abcdefghijklmnopqrstuvwxyz'

    samplesFileOutQty = 0           # current number of samples to putput file
    freqBinQtyLast    = 0           # ready for first output sample
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
    print(directoryList)
    print(directoryListLen)
    
    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]
        if(directory.lower().endswith('.txt')):
            fileList = [directory]
            directory = '.'
        else:
            #fileList = os.listdir(directory)
            fileList = sorted(os.listdir(directory))        # each directory is now sorted alphabetically
        #print(fileList)
        fileListLen = len(fileList)
        #print(fileListLen)
        print()
        for fileCtr in range(fileListLen):
            fileName = fileList[fileCtr]
            #print(fileName)

            #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
            #    + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
            #    + ' = ' + directory + '\\' + fileName + \
            #    '                       ', end='')   # allow append to line
            print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
                + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
                + ' = ' + directory + os.path.sep + fileName + \
                '                       ', end='')   # allow append to line
            #if(fileName.lower().endswith('.txt')):
            #    fileRead = open(directory + '\\' + fileName, 'r')
            if(fileName.lower().endswith('.txt')):
                if fileName[0] == '/':
                    fileRead = open(fileName, 'r')
                else:
                    fileRead = open(directory + os.path.sep + fileName, 'r')

                if fileRead.mode == 'r':
                    #print(' samplesFileOutQty =', str(samplesFileOutQty))

                    fileLine = fileRead.readline()

                    #print()
                    #print(fileName)
                    #print(fileLine)

                    # LF always present: 0=EOF  1=LF  2=1Character
                    # get out of loop if blank line or less
                    if len(fileLine) < 1:        # if end of file, might be one ending linefeed
                        fileRead.close()         #   then have processed all lines in this data file
                        continue                 #   skip to next file

                    # try to read first line of a 1025 line sample

                    thisLine = fileLine.split()
                    if not (len(thisLine) == 4): # if not a valid data file
                        fileRead.close()         #   then have processed all lines in this data file
                        continue                 #   skip to next file


                    # read first line of file
                    # 4/9/2021 12:14:01 PM  Counts:451000
                    # 0        1        2   3                   word index

                    # read time from file in file order
                    # fileHour, fileDayS, fileMonthS, and fileYearS are the file's
                    #   version of time and will need conversion to UTC later
                    dateItems = thisLine[0].split('/')
                    if not (len(dateItems) == 3):  # if not a valid data file
                        fileRead.close()           #   then have processed all lines in this data file
                        continue                   #   skip to next file
                    fileMonthS  = ('0' + dateItems[0])[-2:]  # insure 2-character fileMonthS
                    fileDayS    = ('0' + dateItems[1])[-2:]  # insure 2-character fileDayS
                    fileYearS   = dateItems[2]               # assume 4-character fileYearS

                    timeItems = thisLine[1].split(':')
                    if not (len(timeItems) == 3):  # if not a valid data file
                        fileRead.close()           #   then have processed all lines in this data file
                        continue                   #   skip to next file
                    fileHour = int(timeItems[0])
                    dataMinuteS = ('0' + timeItems[1])[-2:]  # no UTC conversion neccessary
                    dataSecondS = ('0' + timeItems[2])[-2:]  # no UTC conversion neccessary


                    # do fileHour math with integers
                    if (thisLine[2][0] == 'A') and (fileHour == 12):     # if 'AM'
                        fileHour = 0

                    if (thisLine[2][0] == 'P') and (fileHour < 12):     # if 'PM'
                        fileHour += 12

                    fileHourS = ('0' + str(fileHour))[-2:]   # insure 2-character fileHourS

                    # Bases: astropy.time.TimeString
                    # FITS format: “[±Y]YYYY-MM-DD[THH:MM:SS[.sss]]”.
                    # https://docs.astropy.org/en/stable/time/#id3
                    # iso   TimeISO   ‘2000-01-01 00:00:00.000’

                    dataTimeStrThis = fileYearS + '-' + fileMonthS + '-' + fileDayS \
                        + ' ' + fileHourS + ':' + dataMinuteS + ':' + dataSecondS
                    #print('dataTimeStrThis =' + dataTimeStrThis + '=')

                    # convert to UTC: convert dataTimeStrThis to dataTimeUtcThis

                    dataTime = Time(dataTimeStrThis, format='iso', scale='utc')
                    #print( 'dataTime =', dataTime)
                    #print()

                    # create Time object of timeDeltaUtc (= Local to UTC)

                    # first, create Time object of noon UTC on 2020-01-23
                    time12UtcStr = '2020-01-23 12:00:00'
                    #print('time12UtcStr =' + time12UtcStr + '=')
                    time12Utc = Time(time12UtcStr, format='iso', scale='utc')
                    #print(time12Utc)
                    #print( 'time12Utc =', time12Utc)
                    #print()

                    # second, create Time object for local of that noon UTC on 2020-01-23
                    ###timeLocal12UtcStr = '2020-01-23 ' + ('0' + str(int(12 + sdrUtcOffset)))[-2:] + ':00:00'
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
     
                    # fourth, add that difference to file's dataTime
                    dataTimeUtcThis = dataTime + timeUtcDelta
                    #print(dataTimeUtcThis)
                    #print( 'dataTimeUtcThis =', dataTimeUtcThis)
                    #print()

                    # fifth, get string of that sum
                    ######dataTimeUtcStrThis = dataTimeUtcThis.iso
                    #print()
                    #print('dataTimeUtcStrThis =' + dataTimeUtcStrThis + '=')
                    # dataTimeUtcStrThis =2021-04-13 21:04:58.000=
                    #                    01234567890123456789
                    # https://rushter.com/blog/python-strings-and-memory/
                    #print()
                    #print(sys.getsizeof(dataTimeUtcStrThis))    # says 72
                    #print(sys.getsizeof(dataTimeUtc))           # says 48
                    #print(sys.getsizeof(dataTimeUtc.iso))       # says 72
                    ## https://en.wikipedia.org/wiki/Julian_day
                    ## MJD gives the number of days since midnight on November 17, 1858
                    #print(sys.getsizeof(dataTimeUtc.mjd))       # says 32 ------------- chosen form
                    #print(dataTimeUtc.mjd)          # says 59332.26918981481
                    #print(sys.getsizeof(59332.26918981481))     # says 24 - but also need MJD units later
                    #print(59332.26918981481)        # says 59332.26918981481
                    #print(59332 / 365)              # says 162.55342465753424
                    #print(.26918981481)             # says 0.26918981481
                    #print(.00000000001 * 24 * 60 * 60)   # says 8.64e-07 = parts of second for last digit
                    # So, below, store as numpy of MJD
                    
                    #dataTimeUtcStrL.append(dataTimeUtcStrThis)

                    #    # RrrAaaa_Eeee_YYMMDD_Nnnn.txt
                    #    # 0123456789012
                    #    azimuthThis   = float(fileName.split(os.path.sep)[-1][3:7]) / 10.0
                    #    elevationThis = float(fileName.split(os.path.sep)[-1][8:12]) / 10.0
                    #
                    #    if elevationThis > 90.0:
                    #        # to allow calculations, rotate dish
                    #        elevationThis = 180 - elevationThis
                    #        azimuthThis   -= 180.0
                    #        if azimuthThis < 0.0:
                    #            azimuthThis   += 360.0
                    #        #print('after adjustment, using azimuthThis   = ', azimuthThis)
                    #        #print('after adjustment, using elevationThis = ', elevationThis)
                    #    #print('azimuthThis   = ', azimuthThis)
                    #    #print('elevationThis = ', elevationThis)

                    # Downloading ftp://anonymous:mail%40astropy.org@gdc.cddis.eosdis.nasa.gov/
                    #       pub/products/iers/finals2000A.all
                    #       |===========================================| 3.3M/3.3M (100.00%)         4s

                    # read all data lines of this input file
                    freqBinQty = 0
                    #radDataL = []                   # RADio DATA List
                    radDataS = ''                   # RADio DATA long string

                    #    # ignore the first sdrFreqBinQtyPre data lines
                    #    for i in range(sdrFreqBinQtyPre):
                    #        fileLine = fileRead.readline()

                    #        if len(fileLine) < 2:        # if end of file, might be one ending linefeed
                    #            fileRead.close()         #   then have processed all lines in this data file
                    #            break                    #   onto next file

                    #for FreqBin in range(sdrFreqBinQty):
                    while 1:
                        fileLine = fileRead.readline()
                        #print(fileLine)
                        #print(float(fileLine.split()[1]))

                        if len(fileLine) < 2:        # if end of file, might be one ending linefeed
                            fileRead.close()         #   then have processed all lines in this data file
                            break                    #   onto next file

                        fileFreqLast = float(fileLine.split()[0])           # take first number on line
                        if not freqBinQty:
                            #dataFreqMin = float(fileLine.split()[0])        # take first number on line
                            dataFreqMin = fileFreqLast                      # remember first number on line

                        #radDataL.append(float(fileLine.split()[1]))         # take second number on line
                        #radDataS = radDataS + ' ' + fileLine.split()[1]     # take second number on line
                        radDataS += ' ' + fileLine.split()[1]               # take second number on line

                        freqBinQty += 1

                    fileRead.close()                #   then have processed all lines in this data file

                    #dataFreqMax = float(fileLine.split()[0])      # take first number on lastine
                    dataFreqMax = fileFreqLast                    # remember first number on last line

                    if not freqBinQty:
                        print()
                        print('     No data, so skipping', fileName)
                        print()
                        #fileRead.close()         #   then have processed all lines in this data file
                        break                    #   onto next file, do not save any data

                    if freqBinQtyLast:           # if not first read sample
                        if freqBinQtyLast != freqBinQty:
                            print()
                            print()
                            print()
                            print()
                            print()
                            print(' ========== FATAL ERROR:')
                            print('     freqBinQty =', freqBinQtyLast, '  in file', fileNameLast, '  but')
                            print('     freqBinQty =', freqBinQty,     '  in file', fileName)
                            print()
                            print('     Must have same number of frequencies in all input data files.')
                            print()
                            print()
                            print()
                            print()
                            print()
                            exit()

                    #print(radDataL)
                    fileNameLast   = fileName
                    freqBinQtyLast = freqBinQty

                    # ignore the last sdrFreqBinQtyPost data lines of file, do not even read them ??????
                    #    for i in range(sdrFreqBinQtyPost):
                    #    fileLine = fileRead.readline()
                    #    if len(fileLine) < 2:        # if end of file, might be one ending linefeed
                    #        fileRead.close()         #   then have processed all lines in this data file
                    #        break                    #   onto next file

                    # if first sample of this output file
                    if not samplesFileOutQty:
                        # begin a new fileWriteNameThis file with header
                        #fileWriteSamplesQty = 0

                        # if old data file open, close it
                        #if len(fileWriteNameThis):
                        #    fileWrite.close() 

                        #fileWriteName = fileReadName + '.txt'
                        # assumes 'data' directory exists
                        #fileWriteName = 'data' + os.path.sep + fileReadName
                        #fileWriteName = 'data' + os.path.sep + fileName
                        # want just 'data/xxxxxx.txt'  from '/abc/def/xxxxxx.txt'
                        fileWriteName = 'data' + os.path.sep + fileName.split(os.path.sep)[-1]

                        ### try to not write over existing data files,
                        ### assumes 'data' directory exists
                        ### fileNameHourS = 'YYMMDD_HH'
                        ###                  0123456789
                        ###fileNameHourS = timeStampS[2:4] + timeStampS[5:7] + dateDayThisS + '_' +
                        ###      timeStampS[11:13]
                        ###fileNameMidS = 'data' + os.path.sep + fileNamePreS + fileNameHourS  
                        ##fileWriteNameAvail = 0
                        ##for i in range(26):
                        ##    fileWriteNameThis = fileReadName + fileWriteNamePostS[i] + '.txt'
                        ##    #print(fileWriteNameThis)
                        ##    #print(os.path.exists(fileWriteNameThis))
                        ##    if not os.path.exists(fileWriteNameThis):   # if fileNameS is available
                        ##        fileWriteNameAvail = 1
                        ##        break           # get out of FOR loop
                        ##if not fileWriteNameAvail:
                        ##    # no available filenames
                        ##    print()
                        ##    print('ERROR: already too many files with', \
                        ##        'same filename base on this UTC hour')
                        ##    print()
                        ##    exit()

                        # open() with 1 to write buffer to file after every '\n'
                        fileWrite = open(fileWriteName, 'w', 1)

                        ## 220301 new format
                        ## ezRA ezCol .txt daily data file with 3-line non-comment header and
                        ##   1-line samples each with timestamp and 256 values:
                        ##
                        ## from ezCol04b5ea.py
                        ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb
                        ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
                        ## az 227.9 el 42.7 
                        ## # times are in UTC
                        ## 2022-03-01T05:30:55 10.523690382 10.570080895 10.535587705 10.527403187 ... C
                        ## 2022-03-01T05:31:56 10.558290361 10.551762452 10.545512521 10.539835481 ...
                        ## ...
                        ## az 227.9 el 42.7 
                        ## 2022-03-01T06:32:55 10.523690382 10.570080895 10.535587705 10.527403187 ... C
                        ## 2022-03-01T06:33:56 10.558290361 10.551762452 10.545512521 10.539835481 ...
                        ## ...
                        #fileWrite.write('from ' + programRevision  \
                        #    + '\nlat {:g}'.format(sdrQthLat) \
                        #    + ' long {:g}'.format(sdrQthLon) \
                        #    + ' amsl ' + str(sdrQthAmsl) \
                        #    + ' name ' + sdrQthName \
                        #    + '\nfreqMin {:g}'.format(dataFreqMin) \
                        #    + ' freqMax {:g}'.format(dataFreqMax) \
                        #    + ' freqBinQty ' + str(nfreq) \
                        #    + '\naz {:g}'.format(azimuthThis) \
                        #    + ' el {:g}'.format(elevationThis) \
                        #    + '\n# times are in UTC\n')
                        fileWrite.write(
                            'from ' + programRevision \
                            + '\nlat {:g} long {:g} amsl {:g} name '.format( \
                            ezRAObsLat, ezRAObsLon, ezRAObsAmsl) \
                            + ezRAObsName \
                            + '\nfreqMin {:g} freqMax {:g} freqBinQty {:d}'.format( \
                            dataFreqMin, dataFreqMax, freqBinQty) \
                            + '\naz {:g} el {:g}'.format(ezColAzimuth, ezColElevation) \
                            + '\n# times are in UTC\n')

                    # write data line
                    # dataTimeUtcThis = Time(thisLine[1], format='yday', scale='utc')
                    # Time('2000-01-01 02:03:04', out_subfmt='date_hms').iso
                    #   '2000-01-01 02:03:04.000'
                    #timeStampS = dataTimeUtcThis.strftime('%Y-%m-%dT%H:%M:%S ')
                    timeStampS = dataTimeUtcThis.strftime('%Y-%m-%dT%H:%M:%S')
                    # timeStampS = '2022-12-22T21:19:49 '
                    print()
                    #print('time stamp =', timeStampS[:-1])
                    #print('filename =', fileNameS)
                    #print('file sample =', fileSample)
                    #print(timeStampS[:-1], '          ', fileNameS, '         ', fileSample)
                    print(samplesFileOutQty, '    ', timeStampS, '    ', fileWriteName)

                    #fileWrite.write(timeStampS + ' '.join('{:.9g}'.format(i) for i in data) + dataFlagsS)
                    #fileWrite.write(timeStampS + ' '.join(thisLine) + dataFlagsS)
                    #fileWrite.write(timeStampS + ' '.join(radDataL) + '\n')
                    fileWrite.write(timeStampS + radDataS + '\n')

                    #samplesQty     += 1
                    #samplesQtyFile += 1
                    #samplesFileQty += 1
                    samplesFileOutQty += 1

                    #print('      samplesFileQty = ' + str(samplesFileQty) + \
                    #    '         ', end='')   # allow append to line

                    # now have processed that line in that input file that ends with .txt and allows read
                
                # now have processed all lines in that input file that ends with .txt and allows read
                #if fileRead.mode == 'r':

            # now have processed that output file
            #if(fileName.lower().endswith('.txt')):
            print()

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

