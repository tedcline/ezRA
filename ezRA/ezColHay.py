programName = 'ezColHay240505a.py'
programRevision  = programName

# ezRA - Easy Radio Astronomy ezColHay Data COLlector program,
#   converting data from MIT Haystack SRT .rad data format.
#   COLlect radio signals into integrated frequency spectrum data ezRA .txt files.
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

# ezColHay240505a, write the new azDeg format
# ezColHay240430a, updated dataFlagsS from 'C' (Calibration) to 'R' (Reference) for ezCon240225a
# ezColHay230305a.py, boilerplate from ezSky
# ezColHay220930a.py, prep for Git
# ezColHay01m.py, output to ./data directory, 


import os                       # used to grab all files in the current directory
import sys                
import time
#import datetime

from astropy import units as u
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



# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
def ezColArgumentsFileRead(ezColArgumentsFileNameInput):
    # process arguments from file

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezColHayFileNamePrefix           # string

    #global ezColAzimuth                     # float
    #global ezColElevation                   # float

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

            elif thisLine0Lower == '-ezColHayFileNamePrefix'.lower():
                ezColHayFileNamePrefix = thisLine[1]


            # ezCol arguments
            # float arguments
            #elif thisLine0Lower == '-ezColAzimuth'.lower():
            #    ezColAzimuth = float(thisLine[1])

            #elif thisLine0Lower == '-ezColElevation'.lower():
            #    ezColElevation = float(thisLine[1])


            elif thisLine0Lower[:5] == '-ezColHay'.lower():
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

    global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezColHayFileNamePrefix           # string

    #global ezColAzimuth                     # float
    #global ezColElevation                   # float

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
                ezRAObsAmsl  = float(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:
            #elif cmdLineArgLower == 'ezColAzimuth'.lower():
            #    ezColAzimuth = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezColHayFileNamePrefix'.lower():
                # ezColHayFileNamePrefix allows only one word
                ezColHayFileNamePrefix = cmdLineSplit[cmdLineSplitIndex]



            #elif cmdLineArgLower == 'ezDefaultsFile'.lower():
            #    ezColArgumentsFileRead(cmdLineSplit[cmdLineSplitIndex])

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

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezColHayFileNamePrefix           # string

    #global ezColAzimuth                     # float
    #global ezColElevation                   # float

    #global cmdDirectoryS                    # string            creation


    # defaults
    ezRAObsName = ''
    ezRAObsLat  = -999.             # Observatory Latitude  (degrees)
    ezRAObsLon  = -999.             # Observatory Longitude (degrees)
    ezRAObsAmsl = -999.             # Observatory Above Mean Sea Level (meters)
    ezColHayFileNamePrefix = ''

    #ezColAzimuth   = 180.
    #ezColElevation =  45.


    #ezColArgumentsFileRead('ezDefaults.txt')    # process arguments from default ezDefaults.txt file

    ezColArgumentsCommandLine()         # process arguments from command line

    #if ezRAObsName and not ezColHayFileNamePrefix:
    #    ezColHayFileNamePrefix = ezRAObsName.split()[0]        # first word of ezRAObsName
    
    if ezColHayFileNamePrefix and not ezRAObsName:
        ezRAObsName = ezColHayFileNamePrefix                   # ezColHayFileNamePrefix is just one word
    
    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print('   ezColHayFileNamePrefix =', ezColHayFileNamePrefix)
        #print()
        #print('   ezColAzimuth   =', ezColAzimuth)
        #print('   ezColElevation =', ezColElevation)



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezColHay.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezColHay.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezColHay data Collector converter program')
    print('  to read MIT Haystack SRT format .rad radio spectrum data text file(s),')
    print('  and write one ezRA .txt radio spectrum data text file(s) into the assumed')
    print('  "data" directory.')
    print()
    print('  "radioDataFileDirectories" may be one or more .txt radio data files:')
    print('         py  ezColHay.py  220122_05.rad')
    print('         py  ezColHay.py  220122_05.rad 220122_06.rad')
    print('         py  ezColHay.py  220122_*.rad')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezColHay.py  220122')
    print('         py  ezColHay.py  220122 220123')
    print('         py  ezColHay.py  2201*')
    print('  "radioDataFileDirectories" may be a mix of .rad radio data files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezColHay program,')
    #print('  then in order from ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  python ezColHay.py -help              (print this help)')
    print('  python ezColHay.py -h                 (print this help)')
    print()
    print('    -ezRAObsName            bigDish 8   (Observatory Name)')
    print('    -ezRAObsLat             40.2        (Observatory Latitude  (degrees))')
    print('    -ezRAObsLon             -105.1      (Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl            1524        (Observatory Above Mean Sea Level (meters))')
    print('    -ezColHayFileNamePrefix bigDish8    (Data File Name Prefix)')
    print()
    #print('    -ezColAzimuth           180.0       (Azimuth   pointing of antenna (degrees))')
    #print('    -ezColElevation         45.0        (Elevation pointing of antenna (degrees))')
    #print()
    #print('    -ezDefaultsFile ..\\bigDish8.txt     (Additional file of default arguments)')
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

    global programRevision                  # string
    global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezColHayFileNamePrefix           # string


    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print('   ezColHayFileNamePrefix =', ezColHayFileNamePrefix)
        #print()
        #print('   ezColAzimuth   =', ezColAzimuth)
        #print('   ezColElevation =', ezColElevation)

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

def main():

    global programRevision                  # string
    #global cmd                              # string

    global ezRAObsName                      # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezColHayFileNamePrefix           # string

    #global ezColAzimuth                     # float
    #global ezColElevation                   # float

    global cmdDirectoryS                    # string            creation


    startTime = time.time()

    print()
    print(programRevision)
    print()

    printHello()
    
    ezColArguments()


    ###################################################################################

    # Open each data file and read individual lines

    samplesQty     = 0              # current number of samples from all files
    calQty         = 0              # current number of calibration samples
    #fileWriteNamePostS = 'abcdefghijklmnopqrstuvwxyz'

    #if len(sys.argv) > 1:
    #    #directoryList = sorted(sys.argv[1:])
    #    directoryList = sys.argv[1:]
    #else:
    #    directoryList = ['.']
    ##print(directoryList)

   
    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    #print(directoryList)
    #print(directoryListLen)
    
    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]
        #print(directory)
        #print(directory.lower())
        #print(directory.lower().endswith('.rad'))

        # if arguments are .rad filenames,
        # pass each them through together as a mini directory list of .rad files.
        # Allows one .rad file from a directory of .rad files.
        # Allows .bat batch file control.
        if(directory.lower().endswith('.rad')):
            # os.path.sep will later be added before filename, prepare for it
            if directory[0] == os.path.sep:
                fileList = [directory[1:]]              # fileList is list of just one file
                directory = ''
            else:
                fileList = [directory]                  # fileList is list of just one file
                directory = '.'
        else:
            fileList = os.listdir(directory)            # fileList is list of  many files
        #    fileList = sorted(os.listdir(directory))    # each directory is now sorted alphabetically
        #print(fileList)
        fileListLen = len(fileList)
        #fileListLen = 1
        #print(fileListLen)
        #print()
        #for fileCtr in range(fileListLen):
        #fileCtr = 1
        #if 1:
        for fileCtr in range(fileListLen):
            fileReadName = fileList[fileCtr]
            #fileReadName = sys.argv[1]
            #print(fileReadName)

            #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
            #    + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
            #    + ' = ' + directory + '\\' + fileReadName + \
            #    '                       ', end='')   # allow append to line
            #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
            #    + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
            #    + ' = ' + directory + os.path.sep + fileReadName + \
            #    '                       ', end='')   # allow append to line

            if(fileReadName.lower().endswith('.rad')):

                #fileRead = open(directory + '\\' + fileReadName, 'r')
                fileRead = open(directory + os.path.sep + fileReadName, 'r')
                #fileRead = open(fileReadName, 'r')
                #fileRead = open(sys.argv[1], 'r')
                if fileRead.mode == 'r':

                    #print(' samplesFileQty =', str(samplesFileQty))

                    #sampleOfRadFile = 0

                    #print('===========================================================')
                    #print()
                    #print()
                    #print()
                    #print()
                    #print(fileReadName)



                    # now process all lines in that file that ends with .rad and allow read
                    samplesQtyFile = 0           # current number of samples from this file
                    feedCalOnThis  = 0
                    #fileWriteNameThis = ''      # to avoid closing fileWriteNameThis file
                    #azimuthLast   = 9999        # silly value to force new fileWriteNameThis file
                    #elevationLast = 9999        # silly value
                    while(1):

                        print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
                            + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
                            + ' = ' + directory + os.path.sep + fileReadName + \
                            '                       ', end='')   # allow append to line

                        fileReadLine = fileRead.readline()

                        # LF always present: 0=EOF  1=LF  2=1Character
                        # get out of loop if blank line or less
                        if len(fileReadLine) < 1:    # if end of file, might be one ending linefeed
                            # syntax error, not a valid file, reject file
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        #print(' fileReadLine =')
                        #print(fileReadLine)

                        thisLine = fileReadLine.split()

                        if len(thisLine[0]) == 0:
                            continue                 #   skip to next line
                            

                        # process this .rad data file line

                        elif thisLine[0] == '*FeedCalOff':
                            feedCalOnThis = 0
                            continue                 #   skip to next line

                        elif thisLine[0] == '*FeedCalOn':
                            feedCalOnThis = 1
                            continue                 #   skip to next line

                        elif thisLine[0][0] == '*':
                            # comment line
                            continue                 #   skip to next line

                        elif not thisLine[0] == 'DATE':
                            # unknown line, syntax error, not a valid file, reject file
                            break                    #   skip to next file ????????????????????????????????


#tedd1
                        # asume this is the start of a valid 4-line data set
                        #print(thisLine)



                        # process first line of 4-line data set
                        # DATE 2020:181:00:00:05 obsn 346 az 227.9 el 73.9 freq_MHz  1420.4000
                        #   Tsys 453.943 Tant 1125.553 vlsr   23.16 glat 60.042 glon 201.727 source 
                        # 0    1                 2    3   4  5     6  7    8         9
                        #   10   11      12   13       14     15    16   17     18   19      20
                        # https://docs.astropy.org/en/stable/api/astropy.time.TimeYearDayTime.html#astropy.time.TimeYearDayTime
                        # TimeYearDayTime
                        # format='yday'
                        # “YYYY:DOY:HH:MM:SS.sss…"
                        dataTimeUtcThis = Time(thisLine[1], format='yday', scale='utc')

                        azimuthThis   = float(thisLine[5])
                        elevationThis = float(thisLine[7])
                        #print('azimuthThis   = ', azimuthThis)
                        #print('elevationThis = ', elevationThis)



                        # read second line of 4-line data set
                        # Fstart 1419.200 fstop 1421.600 spacing 0.009375 bw    2.400 fbw    2.400 MHz
                        #   nfreq 256 nsam 5242880 npoint 256 integ    16 sigma    1.158 bsw 0
                        # 0      1        2     3        4       5        6     7     8      9     10
                        #   11    12  13   14      15     16  17       18 19       20    21  22

                        fileReadLine = fileRead.readline()
                        #print(' fileReadLine =')
                        #print(fileReadLine)

                        # LF always present: 0=EOF  1=LF  2=1Character
                        # get out of loop if blank line or less
                        if len(fileReadLine) < 1:    # if end of file, might be one ending linefeed
                            # syntax error, not a valid file, reject file
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        thisLine = fileReadLine.split()

                        if len(thisLine[0]) == 0:
                            # syntax error, not a valid file, reject file
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        dataFreqMin = float(thisLine[1])            # Fstart
                        dataFreqMax = float(thisLine[3])            # fstop
                        freqBinQty  = int(thisLine[12])             # nfreq



                        # read third line of 4-line data set
                        # Spectrum     15 integration periods

                        fileReadLine = fileRead.readline()
                        #print(' fileReadLine =')
                        #print(fileReadLine)

                        # LF always present: 0=EOF  1=LF  2=1Character
                        # get out of loop if blank line or less
                        if len(fileReadLine) < 1:    # if end of file, might be one ending linefeed
                            # syntax error, not a valid file, reject file
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        thisLine = fileReadLine.split()

                        if len(thisLine[0]) == 0:
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????



                        # read fourth line of 4-line data set
                        #    0.000  333.169  332.083  336.201  340.355  347.480  358.517  370.244  ...

                        fileReadLine = fileRead.readline()
                        #print(' fileReadLine =')
                        #print(fileReadLine)

                        # LF always present: 0=EOF  1=LF  2=1Character
                        # get out of loop if blank line or less
                        if len(fileReadLine) < 1:    # if end of file, might be one ending linefeed
                            # syntax error, not a valid file, reject file
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        thisLine = fileReadLine.split()

                        if len(thisLine[0]) == 0:
                            fileRead.close()         #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        # hide that the first Haystack .rad data value always appears to be 0.000
                        thisLine[0] = thisLine[1]

                        #radDataL.append(float(thisLine[i]))

                        #print(azimuthLast, elevationLast)
                        #if azimuthThis != azimuthLast or elevationThis != elevationLast:

                        # if first sample of this file
                        if not samplesQtyFile:
                            # begin a new fileWriteNameThis file with header
                            #fileWriteSamplesQty = 0

                            # if old data file open, close it
                            #if len(fileWriteNameThis):
                            #    fileWrite.close() 

                            #fileWriteName = fileReadName + '.txt'
                            # want just 'data/xxxxxx.rad.txt'  from '/abc/def/xxxxxx.rad'
                            fileWriteName = 'data' + os.path.sep + fileReadName.split(os.path.sep)[-1] + '.txt'

                            ### try to not write over existing data files,
                            ### assumes 'data' directory exists
                            ### fileNameHourS = 'YYMMDD_HH'
                            ###                  0123456789
                            ###fileNameHourS = timeStampS[2:4] + timeStampS[5:7] + dateDayThisS + '_' + timeStampS[11:13]
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
                                + f'\nlat {ezRAObsLat:g} long {ezRAObsLon:g} amsl {ezRAObsAmsl:g} name ' \
                                + ezRAObsName \
                                + f'\nfreqMin {dataFreqMin:g} freqMax {dataFreqMax:g} freqBinQty {freqBinQty:d}'\
                                + f'\naz {azimuthThis:g} el {elevationThis:g}' \
                                + '\n# times are in UTC\n')

                            azimuthLast   = azimuthThis
                            elevationLast = elevationThis

                        elif azimuthThis != azimuthLast or elevationThis != elevationLast:
                            #fileWrite.write(f'az {azimuthThis:g} el {elevationThis:g}\n')
                            fileWrite.write(f'azDeg {azimuthThis:g} elDeg {elevationThis:g}\n')
                            azimuthLast   = azimuthThis
                            elevationLast = elevationThis

                        if feedCalOnThis:
                            #dataFlagsS = ' C\n'
                            dataFlagsS = ' R\n'
                            calQty += 1
                        else:
                            dataFlagsS = ' \n'

                        # write data line
                        # dataTimeUtcThis = Time(thisLine[1], format='yday', scale='utc')
                        # Time('2000-01-01 02:03:04', out_subfmt='date_hms').iso
                        #   '2000-01-01 02:03:04.000'
                        timeStampS = dataTimeUtcThis.strftime('%Y-%m-%dT%H:%M:%S ')
                        # timeStampS = '2022-12-22T21:19:49 '
                        print()
                        #print('time stamp =', timeStampS[:-1])
                        #print('filename =', fileNameS)
                        #print('file sample =', fileSample)
                        #print(timeStampS[:-1], '          ', fileNameS, '         ', fileSample)
                        print(samplesQty, '    ', timeStampS, '    ', fileWriteName, '   ', samplesQtyFile, \
                            dataFlagsS[:-1])

                        #fileWrite.write(timeStampS + ' '.join('{:.9g}'.format(i) for i in data) + dataFlagsS)
                        fileWrite.write(timeStampS + ' '.join(thisLine) + dataFlagsS)

                        samplesQty     += 1
                        samplesQtyFile += 1
                        #print('      samplesFileQty = ' + str(samplesFileQty) + \
                        #    '         ', end='')   # allow append to line

                        # now have processed that line in that file that ends with 0-9 and allows read

                    # now have processed all lines in that file that ends with 0-9 and allows read
                    #while(1):

                fileWrite.close()
                fileRead.close()
                # now have processed all lines in that file that ends with 0-9
                #if fileRead.mode == 'r':

            # now have processed all lines in that file
            ##if(fileReadName.lower().endswith('.rad ')):
            #if 1:

        # now have processed all lines in that directory
        ##for fileCtr in range(fileListLen):
        #if 1:

    # now have processed all lines in all directories
    #for directoryCounter in range(directoryListLen):

    # blank out the last filename
    print('\r                                                                              ' \
        + '                                                                                ')
    #print('\r samplesFileQty =', samplesFileQty, \
    #    '                                                                                              ')

    print(' Total             samples read   =', samplesQty)
    print(' Total calibration samples read   =', calQty)
    print()

    if not samplesQty:
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

