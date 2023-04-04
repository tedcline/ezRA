programName = 'ezPlot230326a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezPlot data Plotter program,
#   PLOT analysis from one or more .ezb data files.
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

# TTD:
#       remove many global in main() ?????????
#       plotCountdown, 'plotting' lines only if plotting

# ezPlot230326a.py, ezPlot700 - ezPlot790: avg vs calendar days
# ezPlot230316a.py, -eX
# ezPlot230305a.py, boilerplate from ezSky
# ezPlot221123a.py, fixed ezPlot000timeUtcMjdSorted
# ezPlot221017a.py, polishing, ylabel
# ezPlot221016a.py, 
# ezPlot221015a.py, commas to prints, allow division by data1dSpanD100
# ezPlot221013a.py, commas to prints
# ezPlot220930a.py, prep for Git
# ezPlot220917a, polishing, max of 19 thin black vertical lines to plotEzCon191sigProg


import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from astropy.time import Time

import numpy as np
import os
import sys
import time


def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezPlot.py [optional arguments] dataFileDirectories')
    print('  Linux:     python3 ezPlot.py [optional arguments] dataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezPlot data analysis program')
    print('  to read ezCon format .ezb condensed data file(s),')
    print('  analyse them, optionally creating many .png plot files.')
    print()
    print('  "dataFileDirectories" may be one or more .ezb condensed data files:')
    print('         py  ezPlot.py  bigDish220320_05.ezb')
    print('         py  ezPlot.py  bigDish220320_05.ezb bigDish220321_00.ezb')
    print('         py  ezPlot.py  bigDish22032*.ezb')
    print('  "dataFileDirectories" may be one or more directories:')
    print('         py  ezPlot.py  bigDish2203')
    print('         py  ezPlot.py  bigDish2203 bigDish2204')
    print('         py  ezPlot.py  bigDish22*')
    print('  "dataFileDirectories" may be a mix of .ezb condensed data files and directories')
    print()
    print('  Arguments and "dataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezPlot program,')
    print("  then in order from the ezDefaults.txt in the ezPlot.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  python ezPlot.py -help             (print this help)')
    print('  python ezPlot.py -h                (print this help)')
    print()
    print('    -ezRAObsName   Lebanon Kansas    (Observatory Name)')
    print('    -ezRAObsLat    39.8282           (Observatory Latitude  (degrees))')
    print('    -ezRAObsLon    -98.5696          (Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl   563.88            (Observatory Above Mean Sea Level (meters))')
    print()
    print('    -ezPlotPlotRangeL     0  300     (save only this range of ezPlot plots to file, to save time)')
    print('    -ezPlotDispGrid       1          (turn on graphical display plot grids)')
    print()
    #print('    -ezPlotAstroMath      0           (astroMath choice)')
    #print('      -ezPlotAstroMath  1:    using math from MIT Haystack SRT')
    #print('      -ezPlotAstroMath  2:    using math from slower Astropy library')
    #print()
    print('    -ezDefaultsFile ../bigDish8.txt  (additional file of ezRA arguments)')
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
    print('            ezPlot.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezPlotArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    #global ezPlotAstroMath                  # integer

    global ezPlotDispGrid                   # integer
    global ezPlotPlotRangeL                 # integer list


    print()
    print('   ezPlotArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

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

            # integer arguments:
            elif thisLine0Lower == '-ezPlotDispGrid'.lower():
                ezPlotDispGrid = int(thisLine[1])

            #elif thisLine0Lower == '-ezPlotAstroMath'.lower():
            #    ezPlotAstroMath = int(thisLine[1])


            # float arguments:

            # list arguments:
            elif thisLine0Lower == '-ezPlotPlotRangeL'.lower():
                ezPlotPlotRangeL[0] = int(thisLine[1])
                ezPlotPlotRangeL[1] = int(thisLine[2])


            elif thisLine0Lower[:5] == '-ezPlot'.lower():
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



def ezPlotArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    #global ezPlotAstroMath                  # integer

    global ezPlotDispGrid                   # integer
    global ezPlotPlotRangeL                 # integer list

    global cmdDirectoryS                    # string            creation


    print()
    print('   ezPlotArgumentsCommandLine ===============')

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
            

            # integer arguments:
            elif cmdLineArgLower == '-ezPlotDispGrid'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezPlotDispGrid = int(cmdLineSplit[cmdLineSplitIndex])

            #elif cmdLineArgLower == '-ezPlotAstroMath'.lower():
            #    cmdLineSplitIndex += 1      # point to first argument value
            #    ezPlotAstroMath = int(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:

            # list arguments:
            elif cmdLineArgLower == '-ezPlotPlotRangeL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezPlotPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezPlotPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezPlotArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 3 <= len(cmdLineArgLower) and cmdLineArgLower[:3] == '-ex':
                cmdLineSplitIndex -= 1
                #pass

            # before -eX, old spelling:
            # ignore silly -ezez* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            elif 5 <= len(cmdLineArgLower) and cmdLineArgLower[:5] == '-ezez':
                cmdLineSplitIndex -= 1
                #pass

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



def ezPlotArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global programRevision                  # string
    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    #global ezPlotAstroMath                  # integer

    global fileNameLast                     # string
    global plotCountdown                    # integer
    global ezPlotDispGrid                   # integer
    global ezPlotPlotRangeL                 # integer list


    # defaults
    ezRAObsLat  = -999.                 # silly number
    ezRAObsLon  = -999.                 # silly number
    ezRAObsAmsl = -999.                 # silly number
    #ezRAObsName = 'LebanonKS'
    ezRAObsName = ''                    # silly name

    ezPlotDispGrid    = 0

    #ezPlotAstroMath = 1

    ezPlotPlotRangeL = [0, 9999]        # save this range of plots to file

    plotCountdown = 80                  # number of plots still to print

    # Program argument priority:
    #    Start with the argument value defaults inside the programs.
    #    Then replace those values with any arguments from the ezDefaults.txt in the program's directory.
    #    Then replace values with any arguments from the ezDefaults.txt in the current
    #       directory (where you are standing).
    #    Then replace values (in order) with any arguments from the command line (including
    #       any -ezDefaultsFile).
    #    Each last defined value wins.
    # The top (and bottom ?) of the program printout should list the resultant argument values.

    # process arguments from ezDefaults.txt file in the same directory as this ezPlot program
    ezPlotArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezPlotArgumentsFile('ezDefaults.txt')

    # process arguments from command line
    ezPlotArgumentsCommandLine()

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

    
    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezPlotDispGrid         =', ezPlotDispGrid)
        print()
        #print('   ezPlotAstroMath        =', ezPlotAstroMath)
        #print()
        print('   ezPlotPlotRangeL       =', ezPlotPlotRangeL)



def readDataDir():
    # Open each .ezb radio file in each directory and read individual lines.
    # Creates ezRAObsLat, ezRAObsLon, ezRAObsAmsl, ezRAObsName, fileNameLast, ezPlotIn, antLen

    global cmdDirectoryS            # string

    global ezRAObsLat               # float                                     creation
    global ezRAObsLon               # float                                     creation
    global ezRAObsAmsl              # float                                     creation
    global ezRAObsName              # string                                    creation
    global fileNameLast             # string                                    creation
    global studyOutString           # string                                    creation

    global ezPlotIn                 # float 2d array                            creation
    global antLen                   # integer                                   creation

    print()
    print('   readDataDir ===============')

    ezbQty = 0              # number of .ezb files
    antLen = 0              # number of samples in all .ezb files

    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    
    ezRAObsNameFile = ''
    #ezPlotIn = np.empty(0, 20)
    ezPlotIn = np.array([]).reshape(0, 20)
    studyOutString = '\n'

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
            print(f'\r {ezbQty + 1:,}  file = {fileCounter + 1:,} of {fileListLen:,}',
                f'in dir {directoryCounter + 1} of {directoryListLen} = ',
                directory + os.path.sep + fileReadName, end='')
            studyOutString += f' file = {ezbQty:,} = ' + directory + os.path.sep + fileReadName
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
                ezRAObsLat  = float(fileLineSplit[1])
                ezRAObsLon  = float(fileLineSplit[3])
                ezRAObsAmsl = float(fileLineSplit[5])
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

                # assume this is a valid .ezb data file
                # read data lines of this .ezb file
                # ignore blank and comment lines
                ezPlotIn = np.concatenate([ezPlotIn, np.loadtxt(fileRead)])

                # have processed that .ezb file
                ezbQty += 1            # current number of .ezb data files
                fileNameLast = fileReadName
                antLen = ezPlotIn.shape[0]
                print(f'       Total samples = {antLen:,}                                      ')
                studyOutString += f' ,  Total samples = {antLen:,}\n'

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
    print(f'\n Total samples read          = 1 through {antLen:,}\n')
    studyOutString += f'\n Total number of valid .ezb files = {ezbQty:,}\n'



def openFileStudy():
    # In case it will eventually error.  Creates fileWriteNameStudy, fileWriteStudy

    global fileNameLast             # string
    global fileWriteNameStudy       # string                creation
    global fileWriteStudy           # file handle           creation
    global studyOutString           # string

    print()
    print('   openFileStudy ===============')

    ## data/rqv8ezb220218_00a.txt
    #                        4321-
    fileWriteNameStudy = 'ezPlotStudy' + fileNameLast.split(os.path.sep)[-1][:-4] + '.txt'
    print('   opening', fileWriteNameStudy)

    # before much calculating, get proof can open output file
    fileWriteStudy = open(fileWriteNameStudy, 'w')
    if not (fileWriteStudy.mode == 'w'):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Can not open ')
        print(' ' + fileWriteNameStudy)
        print(' file to write study out')
        print()
        print()
        print()
        print()
        exit()

    fileWriteStudy.write(studyOutString)        # finally have file to write to

    # free studyOutString memory
    studyOutString = []
    studyOutString = None
    del studyOutString



def plotPrep():
    # creates antLenM1, titleS

    global antLen                   # integer
    global antLenM1                 # integer               creation

    global ezRAObsName              # string
    global fileNameLast             # string

    global titleS                   # string                creation

    global ezPlotInIdxByMjdRel      # eventually float array
    global calendar366Days          # eventually float array
    global colorPenSL               # list of strings       creation

    print()
    print('   rawPlotPrep ===============')

    antLenM1 = antLen - 1

    # plot titles
    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + '           ' + ezRAObsName \
        + '          (' + programName + ')'

    ezPlotInIdxByMjdRel = []        # empty list to trigger filling if needed
    calendar366Days     = []        # empty list to trigger filling if needed

    colorPenSL = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']



def printGoodbye(startTime):

    global antLen                   # integer
    global programRevision          # string
    global commandString            # string
    global fileWriteStudy           # file handle

    # print status
    if 0:
        print()
        print('   ezRAObsName      =', ezRAObsName)
        if 0:
            print('   ezPlotRawSamplesUseL      =', ezPlotRawSamplesUseL)
            print('   ezPlotAzimuth             =', ezPlotAzimuth)
            print('   ezPlotElevation           =', ezPlotElevation)
            print('   ezPlotAddAzDeg            =', ezPlotAddAzDeg)
            print('   ezPlotAddElDeg            =', ezPlotAddElDeg)
            print('   ezPlotRawFreqBinHideL     =', ezPlotRawFreqBinHideL)
            print('   ezPlotAntSamplesUseL      =', ezPlotAntSamplesUseL)
            print('   ezPlotAntSampleSnipL      =', ezPlotAntSampleSnipL)
            print('   ezPlotAntAvgTrimFracL     =', ezPlotAntAvgTrimFracL)
            print('   ezPlotAntFreqBinSmooth    =', ezPlotAntFreqBinSmooth)
            print('   ezPlotRefAvgTrimFracL     =', ezPlotRefAvgTrimFracL)
            print('   ezPlotDispGrid            =', ezPlotDispGrid)
            print('   ezPlotDispFreqBin         =', ezPlotDispFreqBin)
        print('   antLen =', antLen)

    stopTime = time.time()
    stopTimeS = time.ctime()
    OutString = f'\n antLen = {antLen:,}\n'
    OutString += '\n That Python command\n'
    OutString += f'  {commandString}\n'
    OutString += f' took {int(stopTime-startTime)} seconds = {(stopTime-startTime)/60.:1.1f} minutes\n'
    OutString += f' Now = {stopTimeS[:-5]}\n'
    OutString += f'\n programRevision = {programRevision}\n\n'
    print(OutString)
    fileWriteStudy.write(OutString)

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



def plotEzPlot1dSamplesAnt(plotName, plotData1d, plotXLabel, plotYLimL, plotColorS, plotYLabel):

    # plotName                                  # string
    # plotData1d                                # float 1d array
    # plotXLabel                                # string
    # plotYLimL                                 # list
    # plotColorS                                # string
    # plotYLabel                                # string

    global titleS                               # string
    global ezPlotDispGrid                       # integer
    global antLenM1                             # integer

    global ezPlotIn                             # float 2d array
    global xTickLocsAnt                         # array         creation?
    global xTickLabelsAnt                       # list          creation?
    global xLabelSAnt                           # string        creation?

    plt.clf()

    plt.plot(plotData1d, plotColorS)

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)
    
    if plotXLabel:
        plt.xlabel(plotXLabel)
        xTickLocsSorted, xTickLabelsSorted = plt.xticks()
        for i in range(len(xTickLocsSorted) - 1)[::-1]:
            xTickLabelsSorted[i] = f'{int(xTickLocsSorted[i]):,}'
        xTickLocsSorted[-1] = antLenM1
        if 0.975 < xTickLocsSorted[-2] / antLenM1:   # if last label overlaps, blank it
            xTickLabelsSorted[-1] = ''
        else:
            xTickLabelsSorted[-1] = f'{antLenM1:,}'
        plt.xticks(xTickLocsSorted, xTickLabelsSorted, rotation=45, ha='right', rotation_mode='anchor')
    else:
        if not len(xTickLocsAnt):
            xTickLocsAnt, xTickLabelsAnt = plt.xticks()
            # dataTimeUtcStrThis = dataTimeUtc[n].iso
            # https://docs.astropy.org/en/stable/time/#id3
            # iso   TimeISO   ‘2000-01-01 00:00:00.000’
            #                  01234567890123456
            # may remove silly values, and shorten lists, so process indices in decreasing order
            for i in range(len(xTickLocsAnt) - 1)[::-1]:
                xTickLocsAntIInt = int(xTickLocsAnt[i])
                if 0 <= xTickLocsAntIInt and xTickLocsAntIInt <= antLenM1:
                    xTickLabelsAnt[i] = f'{xTickLocsAntIInt:,}  ' \
                        + Time(ezPlotIn[xTickLocsAntIInt, 0], format='mjd', scale='utc').iso[11:16]
                else:       # remove silly values
                    xTickLocsAnt = np.delete(xTickLocsAnt, i)
                    xTickLabelsAnt = np.delete(xTickLabelsAnt, i)
            # fill xTickLabelsAnt[-1], samplesQtyM1 is usually less than xTickLocsAnt[-1]
            xTickLocsAnt[-1] = antLenM1
            if 0.975 < xTickLocsAnt[-2] / antLenM1:   # if last label overlaps, blank it
                xTickLabelsAnt[-1] = ''
            else:
                xTickLabelsAnt[-1] = f'{antLenM1:,}  ' \
                    + Time(ezPlotIn[-1, 0], format='mjd', scale='utc').iso[11:16]
        xLabelSAnt = f'Sample Number (last={antLenM1:,}) with UTC Hour:Min (last=' \
            + Time(ezPlotIn[-1, 0], format='mjd', scale='utc').iso[11:16] + ')'
        plt.xlabel(xLabelSAnt)
        plt.xticks(xTickLocsAnt, xTickLabelsAnt, rotation=45, ha='right', rotation_mode='anchor')
    plt.xlim(0, antLenM1)

    plt.ylabel(plotYLabel)
    if len(plotYLimL):
        plt.ylim(plotYLimL[0], plotYLimL[1])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



# ezPlotIn column plots #########################################################

def plotEzPlot000timeUtcMjdSorted():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array
    global antLen                               # integer
    global ezPlotInIdxByMjdRel                  # eventually float array

    if 0 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 0:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot000timeUtcMjdSorted.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    timeUtcMjdMax = ezPlotIn[:, 0].max()
    timeUtcMjdMin = ezPlotIn[:, 0].min()
    print('                         timeUtcMjdMax =', timeUtcMjdMax)
    print('                         timeUtcMjdAvg =', ezPlotIn[:, 0].sum() / antLen)
    print('                         timeUtcMjdMin =', timeUtcMjdMin)

    timeUtcMjdMaxS = Time(timeUtcMjdMax, format='mjd', scale='utc').iso
    #'2021-09-19 04:58:12.345'
    # 01234567890123456
    timeUtcMjdMaxS = timeUtcMjdMaxS[:10] + '   ' + timeUtcMjdMaxS[11:16]
    timeUtcMjdMinS = Time(timeUtcMjdMin, format='mjd', scale='utc').iso
    timeUtcMjdMinS = timeUtcMjdMinS[:10] + '   ' + timeUtcMjdMinS[11:16]

    # ezPlotIn[n:] indices sorted by MJD
    if not len(ezPlotInIdxByMjdRel):
        ezPlotInIdxByMjdRel = ezPlotIn[:, 0].argsort()
        #ezPlotInIdxByMjdRel -= ezPlotInIdxByMjdRel[0]

    # MJD relative to the start of the minimum MJD
    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[ezPlotInIdxByMjdRel, 0]-int(timeUtcMjdMin),
        f'{antLen:,} Samples, sorted Chronologically', [], 'green',
        'UTC Time in Relative Modified Julian Days - Chronological' \
            + '\n\nMinimum = ' + timeUtcMjdMinS \
            + '\n\nMaximum = ' + timeUtcMjdMaxS)



def plotEzPlot001timeUtcMjdUnsorted():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array
    global antLen                               # integer

    if 1 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 1:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot001timeUtcMjdUnsorted.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    timeUtcMjdMax = ezPlotIn[:, 0].max()
    timeUtcMjdMin = ezPlotIn[:, 0].min()
    print('                         timeUtcMjdMax =', timeUtcMjdMax)
    print('                         timeUtcMjdAvg =', ezPlotIn[:, 0].sum() / antLen)
    print('                         timeUtcMjdMin =', timeUtcMjdMin)
    
    timeUtcMjdMaxS = Time(timeUtcMjdMax, format='mjd', scale='utc').iso
    #'2021-09-19 04:58:12.345'
    # 01234567890123456
    timeUtcMjdMaxS = timeUtcMjdMaxS[:10] + '   ' + timeUtcMjdMaxS[11:16]
    timeUtcMjdMinS = Time(timeUtcMjdMin, format='mjd', scale='utc').iso
    timeUtcMjdMinS = timeUtcMjdMinS[:10] + '   ' + timeUtcMjdMinS[11:16]

    # plot MJD from start of minimum day to end of maximum day
    timeUtcMjdMinInt = int(timeUtcMjdMin)
    yMax = int(timeUtcMjdMax) + 1 - timeUtcMjdMinInt
    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 0] - timeUtcMjdMinInt, '', [0, yMax], 'green',
        'UTC Time in Relative Modified Julian Days' \
            + '\n\nMinimum = ' + timeUtcMjdMinS \
            + '\n\nMaximum = ' + timeUtcMjdMaxS)



def plotEzPlot002timeUtcMjd24hours():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array
    global antLen                               # integer

    if 2 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 2:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot002timeUtcMjd24hours.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    timeUtcMjdMaxS = Time(ezPlotIn[:, 0].max(), format='mjd', scale='utc').iso
    #'2021-09-19 04:58:12.345'
    # 01234567890123456
    timeUtcMjdMaxS = timeUtcMjdMaxS[:10] + '   ' + timeUtcMjdMaxS[11:16]
    timeUtcMjdMinS = Time(ezPlotIn[:, 0].min(), format='mjd', scale='utc').iso
    timeUtcMjdMinS = timeUtcMjdMinS[:10] + '   ' + timeUtcMjdMinS[11:16]

    ezPlot002timeUtcMjd24hours = (ezPlotIn[:, 0] % 1.0) * 24.
    
    print('                         ezPlot002timeUtcMjd24hoursMax =',
        ezPlot002timeUtcMjd24hours.max())
    print('                         ezPlot002timeUtcMjd24hoursAvg =',
        ezPlot002timeUtcMjd24hours.sum() / antLen)
    print('                         ezPlot002timeUtcMjd24hoursMin =',
        ezPlot002timeUtcMjd24hours.min())

    # fraction of MJD Day * 24 hours
    plotEzPlot1dSamplesAnt(plotName, ezPlot002timeUtcMjd24hours, '', [0., 24.], 'green',
        'UTC Hours Since Start of UTC Day' \
            + '\n\nMinimum = ' + timeUtcMjdMinS \
            + '\n\nMaximum = ' + timeUtcMjdMaxS)



def plotEzPlot003timeUtcMjdBetween():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array
    global antLen                               # integer
    global antLenM1                             # integer

    if 3 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 3:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot003timeUtcMjdBetween.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    # start with 1 to ignore sample 0
    # 24 * 60 * 60 = 86400 seconds in one MJD Day
    timeUtcMjdBetween = abs(ezPlotIn[:, 0][1:] - ezPlotIn[:, 0][:-1]) * 86400

    timeUtcMjdBetweenMax = timeUtcMjdBetween.max()
    timeUtcMjdBetweenAvg = timeUtcMjdBetween.sum() / antLenM1
    timeUtcMjdBetweenMin = timeUtcMjdBetween.min()
    print('                         timeUtcMjdBetweenMax =', timeUtcMjdBetweenMax)
    print('                         timeUtcMjdBetweenAvg =', timeUtcMjdBetweenAvg)
    print('                         timeUtcMjdBetweenMin =', timeUtcMjdBetweenMin)

    # truncate y axis if too large
    if timeUtcMjdBetweenMax - timeUtcMjdBetweenMin > 400:
        yScale = [0, 400]
    else:
        yScale = []

    timeUtcMjdBetweenAvgInt = int((timeUtcMjdBetweenAvg) + 0.5)
    timeUtcMjdBetweenSpanInt \
        = int((timeUtcMjdBetweenMax - timeUtcMjdBetweenMin) + 0.5)

    plotEzPlot1dSamplesAnt(plotName, timeUtcMjdBetween, '', yScale, 'green',
        f'Seconds Between {antLen:,} Samples' \
            + f'\n\nMedian={int(np.median(timeUtcMjdBetween) + 0.5)}' \
            + f'  Mean={timeUtcMjdBetweenAvgInt}' \
            + f'  Span={timeUtcMjdBetweenSpanInt}')



def plotEzPlot010raH():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 10 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 10:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot010raH.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1


    print('                         raHMax =', ezPlotIn[:, 1].max())
    print('                         raHAvg =', np.mean(ezPlotIn[:, 1]))
    print('                         raHMin =', ezPlotIn[:, 1].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 1], '', [0., 24.], 'green',
        'Right Ascension (hours)')



def plotEzPlot020decDeg():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 20 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 20:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot020decDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         decDegMax =', ezPlotIn[:, 2].max())
    print('                         decDegAvg =', np.mean(ezPlotIn[:, 2]))
    print('                         decDegMin =', ezPlotIn[:, 2].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 2], '', [-90., 90.], 'green',
        'Declination (degrees)')



def plotEzPlot030gLatDeg():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 30 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 30:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot030gLatDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         gLatDegMax =', ezPlotIn[:, 3].max())
    print('                         gLatDegAvg =', np.mean(ezPlotIn[:, 3]))
    print('                         gLatDegMin =', ezPlotIn[:, 3].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 3], '', [-90., 90.], 'green',
        'Galactic Latitude (degrees)')



def plotEzPlot040gLonDeg():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 40 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 40:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot040gLonDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         gLonDegMax =', ezPlotIn[:, 4].max())
    print('                         gLonDegAvg =', np.mean(ezPlotIn[:, 4]))
    print('                         gLonDegMin =', ezPlotIn[:, 4].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 4], '', [-180., 180.], 'green',
        'Galactic Longitude (degrees)')



def plotEzPlot050vLSR():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 50 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 50:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot050vLSR.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         vlsrMax =', ezPlotIn[:, 5].max())
    print('                         vlsrAvg =', np.mean(ezPlotIn[:, 5]))
    print('                         vlsrMin =', ezPlotIn[:, 5].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 5], '', [], 'green',
        'Velocity from Local Standard of Rest (km/s)')



def plotEzPlot100ant():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 100 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 100:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot100ant.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         antAvgMax =', ezPlotIn[:, 10].max())
    print('                         antAvgAvg =', np.mean(ezPlotIn[:, 10]))
    print('                         antAvgMin =', ezPlotIn[:, 10].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 10], '', [], 'blue',
        'Ant Antenna Spectrum Average')



def plotEzPlot110antMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 110 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 110:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot110antMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         antMaxMax =', ezPlotIn[:, 11].max())
    print('                         antMaxAvg =', np.mean(ezPlotIn[:, 11]))
    print('                         antMaxMin =', ezPlotIn[:, 11].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 11], '', [], 'blue',
        'Ant Antenna Spectrum Maximum')



def plotEzPlot120ref():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 120 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 120:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot120ref.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         refAvgMax =', ezPlotIn[:, 12].max())
    print('                         refAvgAvg =', np.mean(ezPlotIn[:, 12]))
    print('                         refAvgMin =', ezPlotIn[:, 12].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 12], '', [], 'red',
        'Ref Reference Spectrum Average')



def plotEzPlot130refMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 130 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 130:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot130refMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         refMaxMax =', ezPlotIn[:, 13].max())
    print('                         refMaxAvg =', np.mean(ezPlotIn[:, 13]))
    print('                         refMaxMin =', ezPlotIn[:, 13].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 13], '', [], 'red',
        'Ref Reference Spectrum Maximum')



def plotEzPlot140antB():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 140 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 140:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot140antB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         antBAvgMax =', ezPlotIn[:, 14].max())
    print('                         antBAvgAvg =', np.mean(ezPlotIn[:, 14]))
    print('                         antBAvgMin =', ezPlotIn[:, 14].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 14], '', [], 'green',
        'AntB Spectrum Average')



def plotEzPlot150antBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 150 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 150:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot150antBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         antBMaxMax =', ezPlotIn[:, 15].max())
    print('                         antBMaxAvg =', np.mean(ezPlotIn[:, 15]))
    print('                         antBMaxMin =', ezPlotIn[:, 15].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 15], '', [], 'green',
        'AntB Spectrum Maximum')



def plotEzPlot160antRB():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array


    if 160 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 160:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot160antRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         antRBAvgMax =', ezPlotIn[:, 16].max())
    print('                         antRBAvgAvg =', np.mean(ezPlotIn[:, 16]))
    print('                         antRBAvgMin =', ezPlotIn[:, 16].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 16], '', [], 'orange',
        'AntRB Spectrum Average')



def plotEzPlot170antRBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 170 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 170:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot170antRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         antRBMaxMax =', ezPlotIn[:, 17].max())
    print('                         antRBMaxAvg =', np.mean(ezPlotIn[:, 17]))
    print('                         antRBMaxMin =', ezPlotIn[:, 17].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 17], '', [], 'orange',
        'AntRB Spectrum Maximum')



def plotEzPlot180antXTVT():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 180 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 180:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot180antXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         AntXTVTAvgMax =', ezPlotIn[:, 18].max())
    print('                         AntXTVTAvgAvg =', np.mean(ezPlotIn[:, 18]))
    print('                         AntXTVTAvgMin =', ezPlotIn[:, 18].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 18], '', [], 'violet',
        'AntXTVT Spectrum Average')



def plotEzPlot190antXTVTMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array

    if 190 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 190:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot190antXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         AntXTVTMaxMax =', ezPlotIn[:, 19].max())
    print('                         AntXTVTMaxAvg =', np.mean(ezPlotIn[:, 19]))
    print('                         AntXTVTMaxMin =', ezPlotIn[:, 19].min())

    plotEzPlot1dSamplesAnt(plotName, ezPlotIn[:, 19], '', [], 'violet',
        'AntXTVT Spectrum Maximum')



def plotEzPlot191sigProg():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list
    global ezPlotIn                             # float 2d array
    global antLenM1                             # integer

    global xTickLocsAnt                         # array         creation?
    global xTickLabelsAnt                       # list          creation?
    global xLabelSAnt                           # string        creation?

    if 191 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 191:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot191sigProg.png'    # Signal Computation Progression
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plt.clf()

    # using gLatDeg, calculate a gain to fit it within -100 to +100 of its average
    print()
    gLatDegMax = ezPlotIn[:, 3].max()
    print('                         gLatDegMax =', gLatDegMax)
    gLatDegAvg = np.mean(ezPlotIn[:, 3])
    print('                         gLatDegAvg =', gLatDegAvg)
    gLatDegAvg = 0.                                                 # center trace on zero
    gLatDegMin = ezPlotIn[:, 3].min()
    print('                         gLatDegMin =', gLatDegMin)
    if gLatDegMax == gLatDegMin:          # gLatDeg will not vary when ezConAstroMath == 0
        gLatDegGain = 0.
    elif gLatDegAvg - gLatDegMin < gLatDegMax - gLatDegAvg:
        gLatDegGain = 93. / (gLatDegMax  - gLatDegAvg)
    else:
        gLatDegGain = 93. / (gLatDegAvg - gLatDegMin)

    gLatDegY = gLatDegGain * (ezPlotIn[:, 3] - gLatDegAvg)

    # thin black horizontal line on center
    plt.axhline(y = 0., linewidth=0.5, color='k')

    # max of 19 thin black vertical lines, one on each Galactic Latitude zero-crossing (19 looked good)
    gLatDegYPos = 0. < gLatDegY                                 # true if gLatDegY is positive
    gLatDegVertLineX = []                                       # list of x for vertical lines
    x = 0
    while len(gLatDegVertLineX) <= 19 and x < antLenM1:         # but max of 19 vertical lines
        if gLatDegYPos[x] != gLatDegYPos[x + 1]:                # if gLatDegY changes from/to positive
            gLatDegVertLineX.append(x)                          #   remember x
        x += 1
    # now either len(gLatDegVertLineX) = 19 + 1, or successfully studied all of gLatDegYPos
    if gLatDegVertLineX and len(gLatDegVertLineX) <= 19:        # if 1 to 19 vertical lines
        for x in gLatDegVertLineX:
            plt.axvline(x = x, linewidth=0.5, color='k')

    plt.plot(gLatDegY, c='blue')


    # using antAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antAvgMax = ezPlotIn[:, 10].max()
    print('                         antAvgMax =', antAvgMax)
    antAvgAvg = np.mean(ezPlotIn[:, 10])
    print('                         antAvgAvg =', antAvgAvg)
    antAvgMin = ezPlotIn[:, 10].min()
    print('                         antAvgMin =', antAvgMin)
    if antAvgMax == antAvgMin:              # antAvg may not vary
        antAvgGain = 0.
    elif antAvgAvg - antAvgMin < antAvgMax - antAvgAvg:
        antAvgGain = 93. / (antAvgMax  - antAvgAvg)
    else:
        antAvgGain = 93. / (antAvgAvg - antAvgMin)
    plt.plot(antAvgGain * (ezPlotIn[:, 10] - antAvgAvg) + 2000., c='blue')


    # using antMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antMaxMax = ezPlotIn[:, 11].max()
    print('                         antMaxMax =', antMaxMax)
    antMaxAvg = np.mean(ezPlotIn[:, 11])
    print('                         antMaxAvg =', antMaxAvg)
    antMaxMin = ezPlotIn[:, 11].min()
    print('                         antMaxMin =', antMaxMin)
    if antMaxMax == antMaxMin:              # antMax may not vary
        antMaxGain = 0.
    elif antMaxAvg - antMaxMin < antMaxMax - antMaxAvg:
        antMaxGain = 93. / (antMaxMax  - antMaxAvg)
    else:
        antMaxGain = 93. / (antMaxAvg - antMaxMin)
    plt.plot(antMaxGain * (ezPlotIn[:, 11] - antMaxAvg) + 1800., c='blue')


    # using refAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    refAvgMax = ezPlotIn[:, 12].max()
    print('                         refAvgMax =', refAvgMax)
    refAvgAvg = np.mean(ezPlotIn[:, 12])
    print('                         refAvgAvg =', refAvgAvg)
    refAvgMin = ezPlotIn[:, 12].min()
    print('                         refAvgMin =', refAvgMin)
    if refAvgMax == refAvgMin:              # refAvg may not vary
        refAvgGain = 0.
    elif refAvgAvg - refAvgMin < refAvgMax - refAvgAvg:
        refAvgGain = 93. / (refAvgMax  - refAvgAvg)
    else:
        refAvgGain = 93. / (refAvgAvg - refAvgMin)
    plt.plot(refAvgGain * (ezPlotIn[:, 12] - refAvgAvg) + 1600., c='red')


    # using refMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    refMaxMax = ezPlotIn[:, 13].max()
    print('                         refMaxMax =', refMaxMax)
    refMaxAvg = np.mean(ezPlotIn[:, 13])
    print('                         refMaxAvg =', refMaxAvg)
    refMaxMin = ezPlotIn[:, 13].min()
    print('                         refMaxMin =', refMaxMin)
    if refMaxMax == refMaxMin:              # refMax may not vary
        refMaxGain = 0.
    elif refMaxAvg - refMaxMin < refMaxMax - refMaxAvg:
        refMaxGain = 93. / (refMaxMax  - refMaxAvg)
    else:
        refMaxGain = 93. / (refMaxAvg - refMaxMin)
    plt.plot(refMaxGain * (ezPlotIn[:, 13] - refMaxAvg) + 1400., c='red')


    # using antBAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antBAvgMax = ezPlotIn[:, 14].max()
    print('                         antBAvgMax =', antBAvgMax)
    antBAvgAvg = np.mean(ezPlotIn[:, 14])
    print('                         antBAvgAvg =', antBAvgAvg)
    antBAvgMin = ezPlotIn[:, 14].min()
    print('                         antBAvgMin =', antBAvgMin)
    if antBAvgMax == antBAvgMin:            # antBAvg may not vary
        antBAvgGain = 0.
    elif antBAvgAvg - antBAvgMin < antBAvgMax - antBAvgAvg:
        antBAvgGain = 93. / (antBAvgMax  - antBAvgAvg)
    else:
        antBAvgGain = 93. / (antBAvgAvg - antBAvgMin)
    plt.plot(antBAvgGain * (ezPlotIn[:, 14] - antBAvgAvg) + 1200., c='green')


    # using antBMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antBMaxMax = ezPlotIn[:, 15].max()
    print('                         antBMaxMax =', antBMaxMax)
    antBMaxAvg = np.mean(ezPlotIn[:, 15])
    print('                         antBMaxAvg =', antBMaxAvg)
    antBMaxMin = ezPlotIn[:, 15].min()
    print('                         antBMaxMin =', antBMaxMin)
    if antBMaxMax == antBMaxMin:            # antBMax may not vary
        antBMaxGain = 0.
    elif antBMaxAvg - antBMaxMin < antBMaxMax - antBMaxAvg:
        antBMaxGain = 93. / (antBMaxMax  - antBMaxAvg)
    else:
        antBMaxGain = 93. / (antBMaxAvg - antBMaxMin)
    plt.plot(antBMaxGain * (ezPlotIn[:, 15] - antBMaxAvg) + 1000., c='green')


    # using antRBAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antRBAvgMax = ezPlotIn[:, 16].max()
    print('                         antRBAvgMax =', antRBAvgMax)
    antRBAvgAvg = np.mean(ezPlotIn[:, 16])
    print('                         antRBAvgAvg =', antRBAvgAvg)
    antRBAvgMin = ezPlotIn[:, 16].min()
    print('                         antRBAvgMin =', antRBAvgMin)
    if antRBAvgMax == antRBAvgMin:          # antRBAvg may not vary
        antRBAvgGain = 0.
    elif antRBAvgAvg - antRBAvgMin < antRBAvgMax - antRBAvgAvg:
        antRBAvgGain = 93. / (antRBAvgMax  - antRBAvgAvg)
    else:
        antRBAvgGain = 93. / (antRBAvgAvg - antRBAvgMin)
    plt.plot(antRBAvgGain * (ezPlotIn[:, 16] - antRBAvgAvg) + 800., c='orange')


    # using antRBMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antRBMaxMax = ezPlotIn[:, 17].max()
    print('                         antRBMaxMax =', antRBMaxMax)
    antRBMaxAvg = np.mean(ezPlotIn[:, 17])
    print('                         antRBMaxAvg =', antRBMaxAvg)
    antRBMaxMin = ezPlotIn[:, 17].min()
    print('                         antRBMaxMin =', antRBMaxMin)
    if antRBMaxMax == antRBMaxMin:          # antRBMax may not vary
        antRBMaxGain = 0.
    elif antRBMaxAvg - antRBMaxMin < antRBMaxMax - antRBMaxAvg:
        antRBMaxGain = 93. / (antRBMaxMax  - antRBMaxAvg)
    else:
        antRBMaxGain = 93. / (antRBMaxAvg - antRBMaxMin)
    plt.plot(antRBMaxGain * (ezPlotIn[:, 17] - antRBMaxAvg) + 600., c='orange')


    # using antXTVTAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antXTVTAvgMax = ezPlotIn[:, 18].max()
    print('                         antXTVTAvgMax =', antXTVTAvgMax)
    antXTVTAvgAvg = np.mean(ezPlotIn[:, 18])
    print('                         antXTVTAvgAvg =', antXTVTAvgAvg)
    antXTVTAvgMin = ezPlotIn[:, 18].min()
    print('                         antXTVTAvgMin =', antXTVTAvgMin)
    if antXTVTAvgMax == antXTVTAvgMin:      # antXTVTAvg may not vary
        antXTVTAvgGain = 0.
    elif antXTVTAvgAvg - antXTVTAvgMin < antXTVTAvgMax - antXTVTAvgAvg:
        antXTVTAvgGain = 93. / (antXTVTAvgMax  - antXTVTAvgAvg)
    else:
        antXTVTAvgGain = 93. / (antXTVTAvgAvg - antXTVTAvgMin)
    plt.plot(antXTVTAvgGain * (ezPlotIn[:, 18] - antXTVTAvgAvg) + 400., c='violet')


    # using antXTVTMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antXTVTMaxMax = ezPlotIn[:, 19].max()
    print('                         antXTVTMaxMax =', antXTVTMaxMax)
    antXTVTMaxAvg = np.mean(ezPlotIn[:, 19])
    print('                         antXTVTMaxAvg =', antXTVTMaxAvg)
    antXTVTMaxMin = ezPlotIn[:, 19].min()
    print('                         antXTVTMaxMin =', antXTVTMaxMin)
    if antXTVTMaxMax == antXTVTMaxMin:      # antXTVTMax may not vary
        antXTVTMaxGain = 0.
    elif antXTVTMaxAvg - antXTVTMaxMin < antXTVTMaxMax - antXTVTMaxAvg:
        antXTVTMaxGain = 93. / (antXTVTMaxMax  - antXTVTMaxAvg)
    else:
        antXTVTMaxGain = 93. / (antXTVTMaxAvg - antXTVTMaxMin)
    plt.plot(antXTVTMaxGain * (ezPlotIn[:, 19] - antXTVTMaxAvg) + 200., c='violet')


    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    if not len(xTickLocsAnt):
        xTickLocsAnt, xTickLabelsAnt = plt.xticks()
        # dataTimeUtcStrThis = dataTimeUtc[n].iso
        # https://docs.astropy.org/en/stable/time/#id3
        # iso   TimeISO   ‘2000-01-01 00:00:00.000’
        #                  01234567890123456
        # may remove silly values, and shorten lists, so best to process indices in decreasing order
        for i in range(len(xTickLocsAnt) - 1)[::-1]:
            xTickLocsAntIInt = int(xTickLocsAnt[i])
            if 0 <= xTickLocsAntIInt and xTickLocsAntIInt <= antLenM1:
                xTickLabelsAnt[i] = f'{xTickLocsAntIInt:,} ' \
                    + Time(ezPlotIn[xTickLocsAntIInt, 0], format='mjd', scale='utc').iso[11:16]
            else:       # remove silly values
                xTickLocsAnt = np.delete(xTickLocsAnt, i)
                xTickLabelsAnt = np.delete(xTickLabelsAnt, i)
        # fill xTickLabelsAnt[-1], samplesQtyM1 is usually less than xTickLocsAnt[-1]
        xTickLocsAnt[-1] = antLenM1
        if 0.975 < xTickLocsAnt[-2] / antLenM1:   # if last label overlaps, blank it
            xTickLabelsAnt[-1] = ''
        else:
            xTickLabelsAnt[-1] = f'{antLenM1:,}  ' \
                + Time(ezPlotIn[-1, 0], format='mjd', scale='utc').iso[11:16]
        xLabelSAnt = f'Sample Number (last={antLenM1:,}) with UTC Hour:Min (last=' \
            + Time(ezPlotIn[-1, 0], format='mjd', scale='utc').iso[11:16] + ')'
    plt.xticks(xTickLocsAnt, xTickLabelsAnt, rotation=45, ha='right', rotation_mode='anchor')
    plt.xlabel(xLabelSAnt)
    plt.xlim(0, antLenM1)

    plt.ylabel('Signal Computation Progression\nfrom Ant to AntXTVT')
    plt.ylim(-150, 2150)
    plt.yticks([ \
          2000., 1800.,    1600., 1400.,
         1200.,  1000.,     800.,    600.,       400.,      200.,         0.],
        ['Ant', 'AntMax', 'Ref', 'RefMax',
        'AntB', 'AntBMax', 'AntRB', 'AntRBMax', 'AntXTVT', 'AntXTVTMax', 'GLatDeg'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')


def plotEzPlot698azimuth():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list


    if 698 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 698:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot698azimuth.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         azimuthMax =', azimuth.max())
    print('                         azimuthAvg =', np.mean(azimuth))
    print('                         azimuthMin =', azimuth.min())

    plotEzPlot1dSamplesAnt(plotName, azimuth, '', [], 'green',
        'Azimuth (Degrees)')

    # free azimuth memory
    azimuth = []
    azimuth = None
    del azimuth


def plotEzPlot699elevation():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list


    if 699 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 699:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot699elevation.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         elevationMax =', elevation.max())
    print('                         elevationAvg =', np.mean(elevation))
    print('                         elevationMin =', elevation.min())

    plotEzPlot1dSamplesAnt(plotName, elevation, '', [], 'green',
        'Elevation (Degrees)')

    # free elevation memory
    elevation = []
    elevation = None
    del elevation



#A#################################################################################################
def plotEzPlot1dSamplesRa(plotName, ezPlotInColumn, plotYLabel):

    # plotName                                  # string
    # ezPlotInColumn                            # integer
    # plotYLabel                                # string

    global titleS                               # string
    global ezPlotDispGrid                       # integer
    global antLen                               # integer
    global antLenM1                             # integer

    global ezPlotIn                             # float 2d array
    global ezPlotInIdxByMjdRel                  # eventually float array
    global colorPenSL                           # list of strings

    plt.clf()

    # ezPlotIn[n:] indices sorted by MJD
    if not len(ezPlotInIdxByMjdRel):
        ezPlotInIdxByMjdRel = ezPlotIn[:, 0].argsort()
        #ezPlotInIdxByMjdRel -= ezPlotInIdxByMjdRel[0]

    # To avoid retrace lines caused by new Right Ascension trace, plot each Ra trace separately.
    # Just keep records until stepping forward into new Ra trace.
    lastStartIndex = 0
    penIndex = 1                         # new pen color (1 through 7) for each plotted day
    for index in range(1, antLen):   # start loop with index == 1
        # new Ra trace ?  (this Ra <= last Ra ?)
        if ezPlotIn[ezPlotInIdxByMjdRel[index], 1] \
                < ezPlotIn[ezPlotInIdxByMjdRel[index - 1], 1]:
            # just stepped forward into a new Ra trace, plot the last Ra trace
            print(f'\r         plotting {lastStartIndex:,}          ,       {index - 1:,}')

            # x list = (Right Ascension sorted by time)
            # y list = (ezPlotInColumn sorted by time)
            plt.plot([ezPlotIn[ezPlotInIdxByMjdRel[i], 1] \
                for i in range(lastStartIndex, index - 1) ],  \
                [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]  \
                for i in range(lastStartIndex, index - 1) ],  \
                c=colorPenSL[penIndex] )                                  # using pens 1-7

            lastStartIndex = index
            penIndex += 1
            if penIndex > 7:        # using only pens 1-7
                penIndex = 1

    # out of loop, plot the last Ra trace
    print(f'\r         plotting {lastStartIndex:,}          ,       {antLenM1:,}')
    plt.plot([ezPlotIn[ezPlotInIdxByMjdRel[i], 1] \
        for i in range(lastStartIndex, antLen) ], \
        [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]     \
        for i in range(lastStartIndex, antLen) ], \
        c=colorPenSL[penIndex] )

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    plt.xlabel(f'Decreasing Right Ascension (Hours) ({antLen:,} Samples)')
    plt.xlim(24.0, 0.0)
    #plt.xticks([0.0, 6.0, 12.0, 18.0, 23.93], ['0', '6', '12', '18', '23.93'])
    plt.xticks([0.0, 6.0, 12.0, 18.0, 24.0], ['0', '6', '12', '18', '24'])

    plt.ylabel(plotYLabel)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzPlot200raAnt():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 200 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 200:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot200raAnt.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 10, 'Ant Spectrum Average by Right Ascension')



def plotEzPlot210raAntMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 210 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 210:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot210raAntMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 11, 'AntMax Spectrum Average by Right Ascension')



def plotEzPlot220raRef():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 220 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 220:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot220raRef.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 12, 'Ref Spectrum Average by Right Ascension')



def plotEzPlot230raRefMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 230 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 230:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot230raRefMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 13, 'RefMax Spectrum Average by Right Ascension')



def plotEzPlot240raAntB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 240 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 240:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot240raAntB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 14, 'AntB Spectrum Average by Right Ascension')



def plotEzPlot250raAntBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 250 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 250:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot250raAntBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 15, 'AntBMax Spectrum Average by Right Ascension')



def plotEzPlot260raAntRB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 260 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 260:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot260raAntRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 16, 'AntRB Spectrum Average by Right Ascension')



def plotEzPlot270raAntRBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 270 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 270:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot270raAntRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 17, 'AntRBMax Spectrum Average by Right Ascension')



def plotEzPlot280raAntXTVT():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 280 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 280:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot280raAntXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 18, 'AntXTVT Spectrum Average by Right Ascension')



def plotEzPlot290raAntXTVTMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 290 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 290:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot290raAntXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesRa(plotName, 19, 'AntXTVTMax Spectrum Average by Right Ascension')



#A#################################################################################################



def plotEzPlot1dSamplesUtc(plotName, ezPlotInColumn, plotYLabel):

    # plotName                                  # string
    # ezPlotInColumn                            # integer
    # plotYLabel                                # string

    global titleS                               # string
    global ezPlotDispGrid                       # integer
    global antLen                               # integer
    global antLenM1                             # integer

    global ezPlotIn                             # float 2d array
    global ezPlotInIdxByMjdRel                  # eventually float array
    global colorPenSL                           # list of strings

    plt.clf()

    # ezPlotIn[n:] indices sorted by MJD
    if not len(ezPlotInIdxByMjdRel):
        ezPlotInIdxByMjdRel = ezPlotIn[:, 0].argsort()
        #ezPlotInIdxByMjdRel -= ezPlotInIdxByMjdRel[0]

    # To avoid retrace lines caused by new UTC day, plot each UTC day separately.
    # Just keep records until stepping forward into new UTC day.
    lastStartIndex = 0                         # skip 0
    timeUtcMjdThisDay = int(ezPlotIn[ezPlotInIdxByMjdRel[0], 0])
    timeUtcMjdLastStartDay = timeUtcMjdThisDay
    penIndex = 1                         # new pen color (1 through 7) for each plotted day
    for index in range(1, antLen):   # start loop with index == 1
    
        timeUtcMjdThisDay = int(ezPlotIn[ezPlotInIdxByMjdRel[index], 0])
        
        if timeUtcMjdLastStartDay < timeUtcMjdThisDay:      # new UTC day ?
            # just stepped forward into a new UTC day, plot the last UTC day
            print(f'\r         plotting {lastStartIndex:,}          ,       {index - 1:,}')

            # x list = (frac part of MJD) * 24 hours
            # y list = ezPlotInColumn
            plt.plot([ (ezPlotIn[ezPlotInIdxByMjdRel[i], 0] % 1.0) * 24.0 \
                for i in range(lastStartIndex, index - 1) ],  \
                [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]  \
                for i in range(lastStartIndex, index - 1) ],  \
                c=colorPenSL[penIndex] )                                  # using pens 1-7

            lastStartIndex = index
            penIndex += 1
            if penIndex > 7:        # using only pens 1-7
                penIndex = 1

            timeUtcMjdLastStartDay = timeUtcMjdThisDay

    # out of loop, plot the last UTC day
    # x list = (frac part of MJD) * 24 hours
    # y list = ezPlotInColumn
    print(f'\r         plotting {lastStartIndex:,}          ,       {antLenM1:,}')
    plt.plot([ (ezPlotIn[ezPlotInIdxByMjdRel[i], 0] % 1.0) * 24.0 \
        for i in range(lastStartIndex, antLen) ], \
        [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]     \
        for i in range(lastStartIndex, antLen) ], \
        c=colorPenSL[penIndex] )

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    plt.xlabel(f'UTC hours  ({antLen:,} Samples)')
    plt.xlim(0, 24)
    plt.xticks([0.0, 6.0, 12.0, 18.0, 24.0], ['0', '6', '12', '18', '24'])

    plt.ylabel(plotYLabel)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzPlot300utcAnt():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 300 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 300:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot300utcAnt.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 10, 'Ant Spectrum Average by UTC day')



def plotEzPlot310utcAntMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 310 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 310:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot310utcAntMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 11, 'AntMax Spectrum Average by UTC day')



def plotEzPlot320utcRef():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 320 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 320:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot320utcRef.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 12, 'Ref Spectrum Average by UTC day')



def plotEzPlot330utcRefMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 330 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 330:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot330utcRefMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 13, 'RefMax Spectrum Average by UTC day')



def plotEzPlot340utcAntB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 340 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 340:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot340utcAntB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 14, 'AntB Spectrum Average by UTC day')



def plotEzPlot350utcAntBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 350 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 350:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot350utcAntBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 15, 'AntBMax Spectrum Average by UTC day')



def plotEzPlot360utcAntRB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 360 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 360:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot360utcAntRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 16, 'AntRB Spectrum Average by UTC day')



def plotEzPlot370utcAntRBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 370 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 370:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot370utcAntRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 17, 'AntRBMax Spectrum Average by UTC day')



def plotEzPlot380utcAntXTVT():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 380 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 380:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot380utcAntXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 18, 'AntXTVT Spectrum Average by UTC day')



def plotEzPlot390utcAntXTVTMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 390 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 390:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot390utcAntXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesUtc(plotName, 19, 'AntXTVTMax Spectrum Average by UTC day')



#A#################################################################################################



def plotEzPlot1dSamplesSid(plotName, ezPlotInColumn, plotYLabel):

    # plotName                                  # string
    # ezPlotInColumn                            # integer
    # plotYLabel                                # string

    global titleS                               # string
    global ezPlotDispGrid                       # integer
    global antLen                               # integer
    global antLenM1                             # integer

    global ezPlotIn                             # float 2d array
    global ezPlotInIdxByMjdRel                  # eventually float array

    global colorPenSL                           # list of strings

    plt.clf()

    # ezPlotIn[n:] indices sorted by MJD
    if not len(ezPlotInIdxByMjdRel):
        ezPlotInIdxByMjdRel = ezPlotIn[:, 0].argsort()
        #ezPlotInIdxByMjdRel -= ezPlotInIdxByMjdRel[0]

    # Sidereal Day math
    # ((365.0 + 0.25 + 0.01 + 0.0025) ...
    # ((23 * 60) + 56) * 60) + 4.091 = 86164.091 seconds in sidereal day
    # UTC Day = 24 * 60 * 60 = 86400 seconds in UTC day
    # sidereal day / UTC day = 86164.091 / 86400 = 0.99726957
    siderealOfUtc = 0.99726957

    # To avoid retrace lines caused by new sidereal day, plot each sidereal day separately.
    # Just keep records until stepping forward into new sidereal day.
    lastStartIndex = 0                         # skip 0
    timeUtcMjdThis       = ezPlotIn[ezPlotInIdxByMjdRel[0], 0]
    timeUtcMjdLastStart  = timeUtcMjdThis
    timeUtcMjdLastStart0 = timeUtcMjdLastStart      # defines left side of plot
    penIndex = 1                         # new pen color (1 through 7) for each plotted day
    for index in range(1, antLen):   # start loop with index == 1

        timeUtcMjdThis = ezPlotIn[ezPlotInIdxByMjdRel[index], 0]

        if timeUtcMjdLastStart + siderealOfUtc < timeUtcMjdThis:      # new sidereal day ?
            # just stepped forward into a new sidereal day, plot the last sidereal day
            print(f'\r         plotting {lastStartIndex:,}          ,       {index - 1:,}')

            # x list = ((timeUtcMjdThis - timeUtcMjdLastStart0) % siderealOfUtc) * 24.0
            # y list = ezPlotInColumn
            plt.plot([((ezPlotIn[ezPlotInIdxByMjdRel[i], 0] \
                - timeUtcMjdLastStart0) % siderealOfUtc) *  24.0 \
                for i in range(lastStartIndex, index - 2) ],  \
                [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]  \
                for i in range(lastStartIndex, index - 2) ],  \
                c=colorPenSL[penIndex] )                                  # using pens 1-7

            lastStartIndex = index
            penIndex += 1
            if penIndex > 7:        # using only pens 1-7
                penIndex = 1

            timeUtcMjdLastStart += siderealOfUtc

    # out of loop, plot the last sidereal day
    # x list = ((timeUtcMjdThis - timeUtcMjdLastStart0) % siderealOfUtc) * 24.0
    # y list = ezPlotInColumn
    print(f'\r         plotting {lastStartIndex:,}          ,       {antLenM1:,}')
    plt.plot([((ezPlotIn[ezPlotInIdxByMjdRel[i], 0] \
        - timeUtcMjdLastStart0) % siderealOfUtc) *  24.0 \
        for i in range(lastStartIndex, antLen) ], \
        [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]     \
        for i in range(lastStartIndex, antLen) ], \
        c=colorPenSL[penIndex] )

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    plt.xlabel(f'Hours of Sidereal Day  ({antLen:,} Samples)')
    plt.xlim(0.0, 24.0)
    plt.xticks([0.0, 6.0, 12.0, 18.0, 23.93], ['0', '6', '12', '18', '23.93'])

    plt.ylabel(plotYLabel)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzPlot400sidAnt():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 400 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 400:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot400sidAnt.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 10, 'Ant Spectrum Average by Sidereal day')



def plotEzPlot410sidAntMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 410 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 410:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot410sidAntMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 11, 'AntMax Spectrum Average by Sidereal day')



def plotEzPlot420sidRef():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 420 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 420:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot420sidRef.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 12, 'Ref Spectrum Average by Sidereal day')



def plotEzPlot430sidRefMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 430 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 430:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot430sidRefMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 13, 'RefMax Spectrum Average by Sidereal day')



def plotEzPlot440sidAntB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 440 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 440:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot440sidAntB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 14, 'AntB Spectrum Average by Sidereal day')



def plotEzPlot450sidAntBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 450 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 450:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot450sidAntBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 15, 'AntBMax Spectrum Average by Sidereal day')



def plotEzPlot460sidAntRB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 460 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 460:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot460sidAntRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 16, 'AntRB Spectrum Average by Sidereal day')



def plotEzPlot470sidAntRBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 470 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 470:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot470sidAntRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 17, 'AntRBMax Spectrum Average by Sidereal day')



def plotEzPlot480sidAntXTVT():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 480 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 480:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot480sidAntXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 18, 'AntXTVT Spectrum Average by Sidereal day')



def plotEzPlot490sidAntXTVTMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 490 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 490:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot490sidAntXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSid(plotName, 19, 'AntXTVTMax Spectrum Average by Sidereal day')



#A#################################################################################################



def plotEzPlot1dSamplesSorted(plotName, ezPlotInColumn, plotYLabel):

    global titleS                               # string
    global ezPlotDispGrid                       # integer

    global ezPlotIn                             # float 2d array

    plt.clf()

    plt.plot(np.sort(ezPlotIn[:, ezPlotInColumn]))       # sorted by value

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    plt.xlabel(f'{antLen:,} Samples Sorted by Value')
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
    plt.xlim(-antLenM1 * 0.01, antLenM1 * 1.01)

    plt.ylabel(plotYLabel)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzPlot500sortedAnt():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 500 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 500:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot500sortedAnt.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 10, 'Ant Spectrum Average Sorted by Value')



def plotEzPlot510sortedAntMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 510 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 510:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot510sortedAntMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 11, 'AntMax Spectrum Average by Sidereal day')



def plotEzPlot520sortedRef():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 520 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 520:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot520sortedRef.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 12, 'Ref Spectrum Average Sorted by Value')



def plotEzPlot530sortedRefMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 530 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 530:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot530sortedRefMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 13, 'RefMax Spectrum Average Sorted by Value')



def plotEzPlot540sortedAntB():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 540 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 540:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot540sortedAntB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 14, 'AntB Spectrum Average Sorted by Value')



def plotEzPlot550sortedAntBMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 550 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 550:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot550sortedAntBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 15, 'AntBMax Spectrum Average Sorted by Value')



def plotEzPlot560sortedAntRB():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 560 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 560:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot560sortedAntRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 16, 'AntRB Spectrum Average Sorted by Value')



def plotEzPlot570sortedAntRBMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 570 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 570:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot570sortedAntRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 17, 'AntRBMax Spectrum Average Sorted by Value')



def plotEzPlot580sortedAntXTVT():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 580 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 580:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot580sortedAntXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 18, 'AntXTVT Spectrum Average Sorted by Value')



def plotEzPlot590sortedAntXTVTMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 590 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 590:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot590sortedAntXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesSorted(plotName, 19, 'AntXTVTMax Spectrum Average Sorted by Value')



#A#################################################################################################



def plotEzPlot1dSamplesHist(plotName, ezPlotInColumn, plotYLabel):

    # plotName                                  # string
    # ezPlotInColumn                            # integer
    # plotYLabel                                # string

    global titleS                               # string
    global ezPlotDispGrid                       # integer

    global ezPlotIn                             # float 2d array

    plt.clf()

    plt.hist(ezPlotIn[:, ezPlotInColumn], color = 'blue', edgecolor = 'black', bins = 100)

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    plt.xlabel(f'Sample Value ({antLen:,} Samples)')
    plt.xlim(0.99 * ezPlotIn[:, ezPlotInColumn].min(), 1.01 * ezPlotIn[:, ezPlotInColumn].max())

    plt.ylabel(plotYLabel)
    yTickLocsAnt, yTickLabelsAnt = plt.yticks()
    # may remove silly values, and shorten lists, so best to process indices in decreasing order
    for i in range(len(yTickLocsAnt) - 1)[::-1]:
        yTickLocsAntIInt = int(yTickLocsAnt[i])
        if 0 <= yTickLocsAntIInt and yTickLocsAntIInt <= antLen:
            yTickLabelsAnt[i] = f'{yTickLocsAntIInt:,}'
        else:       # remove silly values
            yTickLocsAnt = np.delete(yTickLocsAnt, i)
            yTickLabelsAnt = np.delete(yTickLabelsAnt, i)
    plt.yticks(yTickLocsAnt, yTickLabelsAnt)
    #plt.ylim(-antLenM1 * 0.01, None)
    plt.ylim(-yTickLocsAnt[-1] * 0.01, None)
    
    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzPlot600histAnt():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 600 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 600:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot600histAnt.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 10, 'Ant Spectrum Average Histogram')



def plotEzPlot610histAntMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 610 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 610:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot610histAntMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 11, 'AntMax Spectrum Average by Sidereal day')



def plotEzPlot620histRef():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 620 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 620:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot620histRef.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 12, 'Ref Spectrum Average Histogram')



def plotEzPlot630histRefMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 630 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 630:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot630histRefMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 13, 'RefMax Spectrum Average Histogram')



def plotEzPlot640histAntB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 640 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 640:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot640histAntB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 14, 'AntB Spectrum Average Histogram')



def plotEzPlot650histAntBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 650 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 650:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot650histAntBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 15, 'AntBMax Spectrum Average Histogram')



def plotEzPlot660histAntRB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 660 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 660:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot660histAntRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 16, 'AntRB Spectrum Average Histogram')



def plotEzPlot670histAntRBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 670 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 670:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot670histAntRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 17, 'AntRBMax Spectrum Average Histogram')



def plotEzPlot680histAntXTVT():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 680 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 680:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot680histAntXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 18, 'AntXTVT Spectrum Average Histogram')



def plotEzPlot690histAntXTVTMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 690 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 690:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot690histAntXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesHist(plotName, 19, 'AntXTVTMax Spectrum Average Histogram')



#A#################################################################################################



def studyTime(column, data1dName):
    # returns long string

    # column                                    # integer
    # data1dName                                # string

    global ezPlotIn                             # float and int 2d array

    # '5 * str(column - 10)' below provides a (unique?) 5-character string.
    #  RefMax is .ezb file column 13, so later, in the large ezConStudyxxx.txt file,
    #  search for ' 33333' to easily find the RefMax section.
    OutString = f'\n  {fileNameLast}  ================================== ' \
        + f'{5 * str(column - 10)} Time study of {data1dName}\n'

    data1d = ezPlotIn[:, column]
    
    data1dMax = data1d.max()
    data1dMin = data1d.min()
    OutString += f'                         {data1dName}Max = {data1dMax}\n'
    OutString += f'                         {data1dName}Avg = {np.mean(data1d)}\n'
    OutString += f'                         {data1dName}Min = {data1dMin}\n'

    data1dSpanD100 = (data1dMax - data1dMin) / 100.
    # to allow division by data1dSpanD100
    if not data1dSpanD100:
        data1dSpanD100 = 1e-14

    OutString += f'\n Sample numbers of 20 highest-values of {data1dName}:\n'
    data1dIdxbyValueHigh = np.array(data1d).argsort()[::-1][:20]
    for i in range(len(data1dIdxbyValueHigh)):
        data1dThis = data1d[data1dIdxbyValueHigh[i]]
        data1dThisPercent = (data1dThis - data1dMin) / data1dSpanD100
        OutString += f' i = {i}      sample {data1dIdxbyValueHigh[i]}' \
            + f'      {data1dName} = {data1dThis}       {data1dThisPercent} %'
        if data1dThisPercent < 95:
            OutString += '  <=========== < 95%\n'
        else:
            OutString += '\n'
        if i == 4 or i == 9 or i == 14:
            OutString += '\n'
    OutString += '                 Maybe try arguments like    -ezConAntSampleSnip '\
        + f'{data1dIdxbyValueHigh[0]}\n'

    OutString += f'\n Sample numbers of 20 lowest-values of {data1dName}:\n'
    data1dIdxbyValueLow = np.array(data1d).argsort()[:20]
    for i in range(len(data1dIdxbyValueLow)):
        data1dThis = data1d[data1dIdxbyValueLow[i]]
        data1dThisPercent = (data1dThis - data1dMin) / data1dSpanD100
        OutString += f' i = {i}      sample {data1dIdxbyValueLow[i]}' \
            + f'      {data1dName} = {data1dThis}       {data1dThisPercent} %'
        if 5 < data1dThisPercent:
            OutString += '  <=========== > 5%\n'
        else:
            OutString += '\n'
        if i == 4 or i == 9 or i == 14:
            OutString += '\n'
    OutString += '                 Maybe try arguments like    -ezConAntSampleSnip '\
        + f'{data1dIdxbyValueLow[0]}\n'

    OutString += f'\n Sample numbers of 20 largest change values of {data1dName}:\n'
    data1dIdxbyValueDeltaHighM1 = np.array(abs(data1d[1:] - data1d[:-1])).argsort()[::-1][:20]
    for i in range(len(data1dIdxbyValueDeltaHighM1)):
        data1dDeltaThis = \
            data1d[data1dIdxbyValueDeltaHighM1[i] + 1] - data1d[data1dIdxbyValueDeltaHighM1[i]]
        OutString += f' i = {i}      sample {data1dIdxbyValueDeltaHighM1[i] + 1}' \
            + f'      {data1dName}Delta = {data1dDeltaThis}' \
            + f'       {data1dDeltaThis / data1dSpanD100} %\n'
        if i == 4 or i == 9 or i == 14:
            OutString += '\n'
    OutString += '                 Maybe try arguments like    -ezConAntSampleSnip '\
        + f'{data1dIdxbyValueDeltaHighM1[0] + 1}\n\n\n\n'
        
    return(OutString)



def writeFileStudy():

    global fileWriteStudy           # file handle

    print()
    print('   writeFileStudy ===============')

    fileWriteStudy.write( \
        '\n============================================================================ ant\n\n\n\n\n')
    fileWriteStudy.write(studyTime(10, 'AntAvg'))
    fileWriteStudy.write(studyTime(11, 'AntMax'))

    fileWriteStudy.write( \
        '\n============================================================================ ref\n\n\n\n\n')
    fileWriteStudy.write(studyTime(12, 'RefAvg'))
    fileWriteStudy.write(studyTime(13, 'RefMax'))
    
    fileWriteStudy.write( \
        '\n============================================================================ antB\n\n\n\n\n')
    fileWriteStudy.write(studyTime(14, 'AntBAvg'))
    fileWriteStudy.write(studyTime(15, 'AntBMax'))
    
    fileWriteStudy.write( \
        '\n============================================================================ antRB\n\n\n\n\n')
    fileWriteStudy.write(studyTime(16, 'AntRBAvg'))
    fileWriteStudy.write(studyTime(17, 'AntRBMax'))

    fileWriteStudy.write( \
        '\n============================================================================ antXTVT\n\n\n\n\n')
    fileWriteStudy.write(studyTime(18, 'AntXTVTAvg'))
    fileWriteStudy.write(studyTime(19, 'AntXTVTMax'))
    fileWriteStudy.write( \
        '\n============================================================================\n\n\n\n\n')



#A#################################################################################################

def plotEzPlot1dSamplesCal(plotName, ezPlotInColumn, plotYLabel):

    # plotName                                  # string
    # ezPlotInColumn                            # integer
    # plotYLabel                                # string

    global titleS                               # string
    global ezPlotDispGrid                       # integer
    global antLen                               # integer
    global antLenM1                             # integer

    global ezPlotIn                             # float 2d array
    global ezPlotInIdxByMjdRel                  # eventually float array
    global calendar366Days                      # eventually float array
    global colorPenSL                           # list of strings

    plt.clf()

    # ezPlotIn[n:] indices sorted by MJD
    if not len(ezPlotInIdxByMjdRel):
        ezPlotInIdxByMjdRel = ezPlotIn[:, 0].argsort()
        #ezPlotInIdxByMjdRel -= ezPlotInIdxByMjdRel[0]

    # Calendar Day math
    if not len(calendar366Days):
        # calculate mjdMarch1950_2050L for many years
        mjdMarchLast = 32976.               # MJD of Mar-1-1949
        mjdMarch1950_2050L = []
        for year in range(1950, 2051):
            if year % 4:                    # if leap year (2000 = leap year)
                mjdMarchLast += 366.
            else:                           # not leap year
                mjdMarchLast += 365.
            mjdMarch1950_2050L.append(mjdMarchLast)
        #print(' mjdMarch1950_2050L =', mjdMarch1950_2050L)

        # calculate calendar366Days from each sample's mjd
        print()
        calendar366Days = np.empty(antLen)
        for index in range(antLen):
            mjdThis = ezPlotIn[ezPlotInIdxByMjdRel[index], 0]

            # mjdMarchDays = first mjd >= mjdMarch1950_2050L
            for mjdMarch1950_2050LThis in reversed(mjdMarch1950_2050L):
                if mjdMarch1950_2050LThis <= mjdThis:
                    mjdMarchDays = mjdThis - mjdMarch1950_2050LThis
                    break
            #print(' mjdMarchDays =', mjdMarchDays)
            # calendar366Days = (mjdMarchDays + 29. + 31.) % 366.   # as if Feb-29 leap year
            print(f'\r         sample {index:,}   of  {antLenM1:,}     ',
                'calendar366Day =', (mjdMarchDays + 60.) % 366., '              ', end='')
            calendar366Days[ezPlotInIdxByMjdRel[index]] = (mjdMarchDays + 60.) % 366.
        mjdMarch1950_2050L = []
        print()
        print('         calendar366Days.max() =', calendar366Days.max())    # just below 366.
        print('         calendar366Days.min() =', calendar366Days.min())    # just above 0.
        print()

    # To avoid retrace lines caused by new Calendar Year, plot each Calendar Year separately.
    # Just keep records until stepping forward into new Calendar Year.
    lastStartIndex = 0
    calendar366DaysLast = calendar366Days[ezPlotInIdxByMjdRel[0]]
    penIndex = 1                         # new pen color (1 through 7) for each plotted day
    for index in range(1, antLen):   # start loop with index == 1

        calendar366DaysThis = calendar366Days[ezPlotInIdxByMjdRel[index]]

        if calendar366DaysThis < calendar366DaysLast:      # new Calendar Year ?
            # just stepped forward into a new Calendar Year, plot the last Calendar Year
            print(f'\r         plotting {lastStartIndex:,}          ,       {index - 1:,}')

            # x list = calendar366Days
            # y list = ezPlotInColumn
            plt.plot([ calendar366Days[ezPlotInIdxByMjdRel[i]] \
                for i in range(lastStartIndex, index - 1) ],  \
                [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]  \
                for i in range(lastStartIndex, index - 1) ],  \
                c=colorPenSL[penIndex] )                                # using pens 1-7

            lastStartIndex = index
            penIndex += 1
            if penIndex > 7:        # using only pens 1-7
                penIndex = 1

        calendar366DaysLast = calendar366DaysThis

    # out of loop, plot the last Calendar Year
    # x list = calendar366Days
    # y list = ezPlotInColumn
    print(f'\r         plotting {lastStartIndex:,}          ,       {antLenM1:,}')
    plt.plot([ calendar366Days[ezPlotInIdxByMjdRel[i]] \
        for i in range(lastStartIndex, antLen) ], \
        [ ezPlotIn[ezPlotInIdxByMjdRel[i], ezPlotInColumn]  \
        for i in range(lastStartIndex, antLen) ], \
        c=colorPenSL[penIndex] )

    plt.title(titleS)
    plt.grid(ezPlotDispGrid)

    plt.xlabel(f'Calendar Year (Months) ({antLen:,} Samples)')
    plt.xlim(0., 366.)
    plt.xticks([0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335],
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    plt.ylabel(plotYLabel)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzPlot700calAnt():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 700 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 700:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot700calAnt.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 10, 'Ant Spectrum Average by Calendar Day')



def plotEzPlot710calAntMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 710 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 710:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot710calAntMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 11, 'AntMax Spectrum Average by Calendar Day')



def plotEzPlot720calRef():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 720 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 720:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot720calRef.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 12, 'Ref Spectrum Average by Calendar Day')



def plotEzPlot730calRefMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 730 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 730:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot730calRefMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 13, 'RefMax Spectrum Average by Calendar Day')



def plotEzPlot740calAntB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 740 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 740:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot740calAntB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 14, 'AntB Spectrum Average by Calendar Day')



def plotEzPlot750calAntBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 750 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 750:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot750calAntBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 15, 'AntBMax Spectrum Average by Calendar Day')



def plotEzPlot760calAntRB():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 760 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 760:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot760calAntRB.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 16, 'AntRB Spectrum Average by Calendar Day')



def plotEzPlot770calAntRBMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 770 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 770:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot770calAntRBMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 17, 'AntRBMax Spectrum Average by Calendar Day')



def plotEzPlot780calAntXTVT():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 780 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 780:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot780calAntXTVT.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 18, 'AntXTVT Spectrum Average by Calendar Day')



def plotEzPlot790calAntXTVTMax():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    global ezPlotPlotRangeL                     # integer list

    if 790 < ezPlotPlotRangeL[0] or ezPlotPlotRangeL[1] < 790:
        plotCountdown -= 1
        return(1)

    plotName = 'ezPlot790calAntXTVTMax.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    plotEzPlot1dSamplesCal(plotName, 19, 'AntXTVTMax Spectrum Average by Calendar Day')



#A#################################################################################################



def main():

    global programRevision          # string
    global commandString            # string
    global cmdDirectoryS            # string

    global ezRAObsLat               # float
    global ezRAObsLon               # float
    global ezRAObsAmsl              # float
    global ezRAObsName              # string
    global fileNameLast             # string

    global ezPlotIn                 # float 2d array
    global fileWriteNameStudy       # string
    global fileWriteStudy           # file handle

    global ezPlotAstroMath          # integer

    global titleS                   # string
    global plotCountdown            # integer
    global ezPlotDispGrid           # integer

    global xTickLocsAnt             # array
    global xTickLabelsAnt           # list
    global xLabelSAnt               # string

    global ezPlotPlotRangeL         # integer list

    startTime = time.time()
    xTickLocsAnt = []               # force new xTickLocsAnt
    xTickLabelsHeatAntL = []        # force new xTickLabelsHeatAntL


    #################################################################################################
    #
    # The old ezPlot does NOT yet support the new .ezb format files.
    # A new ezPlot is NOT included.
    # A new ezPlot will support ONLY the new .ezb format files.
    # The new ezPlot is planned to optionally plot
    #     timeUtcMjdSorted,
    #     timeUtcMjdUnsorted,
    #     timeUtcMjd24hours,
    #     timeUtcMjdBetween,
    #     raH,
    #     decDeg,
    #     gLatDeg,
    #     gLonDeg,
    #     and VLSR.
    # And for both Average and Maximum values of each of the sample's Ant, Ref, AntB, AntRB,
    #   and AntXTVT signals, ezPlot will optionally plot
    #     the signal by Ant sample number,
    #     the signal by rightAscension (hours),
    #     the signal by UTC time (hours),
    #     the signal by sidereal time (hours),
    #     the signal by sorted value,
    #     and the signal's histogram.
    # And ezPlot will optionally plot the signalProgression (sigProg).
    # And (calculated using ezRAObsLat, ezRAObsLon, and ezRAObsAmsl) ezPlot may optionally
    #   plot the azimuth and elevation.
    # I count 72 plots.
    #
    #################################################################################################
    #
    # ezPlot plot number system:
    #
    #      X-axis:                  #+HHMM                  Count
    #    timeUtcMjdSorted                                   000
    #    timeUtcMjdUnsorted         001
    #    timeUtcMjd24hours          002
    #    timeUtcMjdBetween          003
    #
    #    raH                        010
    #    decDeg                     020
    #
    #    gLatDeg                    030
    #    gLonDeg                    040
    #
    #    vlsr                       050
    #
    #    count (=1)                (060)
    #    spare1(=0)                (070)
    #    spare2(=0)                (080)
    #    spare3(=0)                (090)
    #
    #############################################################
    # 
    #                                      RaH  UTC  Sid    Sorted  Hist  
    #      X-axis:                  #+HHMM RaH  UTC  Sid    Count   Value
    #    ant                        100    200  300  400    500     600
    #    antMax                     110    210  310  410    510     610
    #    ref                        120    220  320  420    520     620
    #    refMax                     130    230  330  430    530     630
    #
    #    antB                       140    240  340  440    540     640
    #    antBMax                    150    250  350  450    550     650
    #    antRB                      160    260  360  460    560     660
    #    antRBMax                   170    270  370  470    570     670
    #    antXTVT                    180    280  380  480    580     680
    #    antXTVTMax                 190    290  390  490    590     690
    #
    #    sigProg                    191
    #
    #############################################################
    #
    # calculated with ezRAObsLat, ezRAObsLon, and ezRAObsAmsl:
    #    azimuth                    698
    #    elevation                  699
    #
    #################################################################################################

    printHello()

    ezPlotArguments()

    readDataDir()           # creates ezRAObsLat, ezRAObsLon, ezRAObsAmsl, ezRAObsName, fileNameLast,
                            #   ezPlotIn, antLen

    openFileStudy()         # In case it will eventually error.  Creates fileWriteNameStudy, fileWriteStudy

    plotPrep()              # creates antLenM1, titleS, ezPlotInIdxByMjdRel

    # plot ezPlots with X-axis: #+HHMM

    plotEzPlot000timeUtcMjdSorted()
    plotEzPlot001timeUtcMjdUnsorted()
    plotEzPlot002timeUtcMjd24hours()
    plotEzPlot003timeUtcMjdBetween()

    plotEzPlot010raH()
    plotEzPlot020decDeg()
    plotEzPlot030gLatDeg()
    plotEzPlot040gLonDeg()
    plotEzPlot050vLSR()

    plotEzPlot100ant()
    plotEzPlot110antMax()

    plotEzPlot120ref()
    plotEzPlot130refMax()

    plotEzPlot140antB()
    plotEzPlot150antBMax()

    plotEzPlot160antRB()
    plotEzPlot170antRBMax()

    plotEzPlot180antXTVT()
    plotEzPlot190antXTVTMax()

    plotEzPlot191sigProg()

    #plotEzPlot698azimuth()
    #plotEzPlot699elevation()



    # plot ezPlots with X-axis: RaH

    plotEzPlot200raAnt()
    plotEzPlot210raAntMax()

    plotEzPlot220raRef()
    plotEzPlot230raRefMax()

    plotEzPlot240raAntB()
    plotEzPlot250raAntBMax()

    plotEzPlot260raAntRB()
    plotEzPlot270raAntRBMax()

    plotEzPlot280raAntXTVT()
    plotEzPlot290raAntXTVTMax()



    # plot ezPlots with X-axis: UTC

    plotEzPlot300utcAnt()
    plotEzPlot310utcAntMax()

    plotEzPlot320utcRef()
    plotEzPlot330utcRefMax()

    plotEzPlot340utcAntB()
    plotEzPlot350utcAntBMax()

    plotEzPlot360utcAntRB()
    plotEzPlot370utcAntRBMax()

    plotEzPlot380utcAntXTVT()
    plotEzPlot390utcAntXTVTMax()



    # plot ezPlots with X-axis: sidereal time

    plotEzPlot400sidAnt()
    plotEzPlot410sidAntMax()

    plotEzPlot420sidRef()
    plotEzPlot430sidRefMax()

    plotEzPlot440sidAntB()
    plotEzPlot450sidAntBMax()

    plotEzPlot460sidAntRB()
    plotEzPlot470sidAntRBMax()

    plotEzPlot480sidAntXTVT()
    plotEzPlot490sidAntXTVTMax()



    # plot ezPlots with X-axis: sorted

    plotEzPlot500sortedAnt()
    plotEzPlot510sortedAntMax()

    plotEzPlot520sortedRef()
    plotEzPlot530sortedRefMax()

    plotEzPlot540sortedAntB()
    plotEzPlot550sortedAntBMax()

    plotEzPlot560sortedAntRB()
    plotEzPlot570sortedAntRBMax()

    plotEzPlot580sortedAntXTVT()
    plotEzPlot590sortedAntXTVTMax()



    # plot ezPlots with X-axis: histogram

    plotEzPlot600histAnt()
    plotEzPlot610histAntMax()

    plotEzPlot620histRef()
    plotEzPlot630histRefMax()

    plotEzPlot640histAntB()
    plotEzPlot650histAntBMax()

    plotEzPlot660histAntRB()
    plotEzPlot670histAntRBMax()

    plotEzPlot680histAntXTVT()
    plotEzPlot690histAntXTVTMax()



    # plot ezPlots with X-axis: calendar days

    plotEzPlot700calAnt()
    plotEzPlot710calAntMax()

    plotEzPlot720calRef()
    plotEzPlot730calRefMax()

    plotEzPlot740calAntB()
    plotEzPlot750calAntBMax()

    plotEzPlot760calAntRB()
    plotEzPlot770calAntRBMax()

    plotEzPlot780calAntXTVT()
    plotEzPlot790calAntXTVTMax()



    writeFileStudy()

    printGoodbye(startTime)



if __name__== '__main__':
  main()

