programName = 'ezSky221202a.py'
#programRevision = programName + ' (N0RQV)'
programRevision = programName

# Easy Radio Astronomy (ezRA) ezSky Sky Mapper program,
#   to read ezCon format .ezb condensed data text file(s)
#   and optionally create .png plot files.

# TTD:
#       remove many global in main() ?????????
#       plotCountdown, 'plotting' lines only if plotting

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
# ezSky221012b.py, gLonHalfDeg now wraps around
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
from scipy.ndimage.filters import gaussian_filter

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
    print('EXAMPLES:')
    print()
    print('  py  ezSky.py -help               (print this help)')
    print('  py  ezSky.py -h                  (print this help)')
    print()
    print('    -ezRAObsName         bigDish   (observatory name for plot titles)')
    print()
    print('    -ezSkyInput          18        (choose .ezb data column)')
    print()
    print('    -ezSkyDispGrid       1         (turn on graphical display plot grids)')
    print('    -ezSkyVOGain         100       (vertical offset gain  of ezSky200RBPVO_  plot traces)')
    #print('    -ezSkyTraceColor     blue      (color of plot traces)')
    print('    -ezSkyHalfTallDec    9         (almost half height of ezSky301RBPT_  plot traces',
        '(in halfDegrees))')
    print()
    #print('    -ezSkyMaskFile       ezSkyMask-N-48bigDish.npy')
    #print('         (radio sky mask input for ezSky404GIP_  and ezSky405GIPS_  plots, unseen sky as white)')
    #print('    -ezSkyMaskDecDegN    -49.6     (observatory horizon = ezRAObsLat - 90.0)')
    #print('         (north edge degrees to create radio sky mask.  Use',
    #    'default silly -99 to disable creation)')
    #print('    -ezSkyMaskDecDegS    -90.0     (below horizon south celestial pole = -90.0)')
    #print('         (south edge degrees to create radio sky mask.  Use',
    #    'default silly  99 to disable creation)')
    #print('    -ezSkyMaskWrite      1         (default = 0 = not write sky mask to file)')
    #print()
    print('    -ezSkyPlotRangeL     0  300    (save only this range of ezSky plots to file, to save time)')
    print()
    print('    -ezDefaultsFile ..\\bigDish.txt      (additional file of ezRA arguments)')
    print()
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
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezSkyArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsName                      # string

    global ezSkyDispGrid                    # integer
    global ezSkyInput                       # integer
    global ezSkyVOGain                      # float
    global ezSkyHalfTallDec                 # integer

    global ezSkyMaskFile                    # string
    global ezSkyMaskDecDegN                 # integer
    global ezSkyMaskDecDegS                 # integer
    global ezSkyMaskWrite                   # integer

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
            elif fileLineSplit0Lower == '-ezSkyDispGrid'.lower():
                ezSkyDispGrid = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyInput'.lower():
                ezSkyInput = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyVOGain'.lower():
                ezSkyVOGain = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyHalfTallDec'.lower():
                ezSkyHalfTallDec = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyMaskFile'.lower():
                ezSkyMaskFile = fileLineSplit[1]

            elif fileLineSplit0Lower == '-ezSkyMaskDecDegN'.lower():
                ezSkyMaskDecDegN = float(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyMaskDecDegS'.lower():
                ezSkyMaskDecDegS = float(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyMaskWrite'.lower():
                ezSkyMaskWrite = int(fileLineSplit[1])

            elif fileLineSplit0Lower == '-ezSkyPlotRangeL'.lower():
                ezSkyPlotRangeL[0] = int(fileLineSplit[1])
                ezSkyPlotRangeL[1] = int(fileLineSplit[2])


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

    global ezSkyDispGrid                    # integer
    global ezSkyInput                       # integer
    global ezSkyVOGain                      # float
    global ezSkyHalfTallDec                 # integer

    global ezSkyMaskFile                    # string
    global ezSkyMaskDecDegN                 # integer
    global ezSkyMaskDecDegS                 # integer
    global ezSkyMaskWrite                   # integer

    global ezSkyPlotRangeL                  # integer list

    global cmdDirectoryS                    # string            creation

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
            elif cmdLineArgLower == 'ezSkyDispGrid'.lower():
                ezSkyDispGrid = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyInput'.lower():
                ezSkyInput = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyVOGain'.lower():
                ezSkyVOGain = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyHalfTallDec'.lower():
                ezSkyHalfTallDec = int(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezSkyMaskFile'.lower():
                ezSkyMaskFile = cmdLineSplit[cmdLineSplitIndex]

            elif cmdLineArgLower == 'ezSkyMaskDecDegN'.lower():
                ezSkyMaskDecDegN = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyMaskDecDegS'.lower():
                ezSkyMaskDecDegS = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezSkyMaskWrite'.lower():
                ezSkyMaskWrite = int(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezSkyPlotRangeL'.lower():
                ezSkyPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezSkyPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezDefaultsFile'.lower():
                ezSkyArgumentsFile(cmdLineSplit[cmdLineSplitIndex])


            elif 4 <= len(cmdLineArgLower) and cmdLineArgLower[:4] == 'ezez':
                # ignore this one word that starts with '-ezez'
                pass

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

    global ezSkyDispGrid                    # integer
    global ezSkyInput                       # integer
    global ezSkyVOGain                      # float
    global ezSkyHalfTallDec                 # integer
    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer

    global ezSkyMaskFile                    # string
    global ezSkyMaskDecDegN                 # integer
    global ezSkyMaskDecDegS                 # integer
    global ezSkyMaskWrite                   # integer

    global ezSkyBackground1                 # string
    global ezSkyBackground1XMax             # integer
    global ezSkyBackground1YMax             # integer

    # defaults
    #ezRAObsName = 'LebanonKS'
    ezRAObsName = ''                        # silly name

    ezSkyInput    = 14
    ezSkyDispGrid = 0

    ezSkyVOGain = 50.

    # (ezSkyHalfTallDec + 1 + ezSkyHalfTallDec) = thickness of tall plot trace (last drawn wins)
    ezSkyHalfTallDec = 3

    #ezSkyMaskFile = 'ezSkyMask-S419.npy'   # south edge =  41.9 degees Dec
    #ezSkyMaskFile = 'ezSkyMask-N-311.npy'  # north edge = -31.1 degees Dec
    #ezSkyMaskFile = 'ezSkyMask-S419N-311N0RQV.npy' # Sto41.9,Nto-31.1 Dec = N0RQV
    ezSkyMaskFile = ''
    # northern hemispere: south horizon declination = latitude - 90
    # N0RQV = south horizon declination = latitude - 90 = 40.4 - 90 = -49.6
    # ezSkyMaskDecDegN =  sdrQthLat - 90.0
    # ezSkyMaskDecDegN = -49.6
    ezSkyMaskDecDegN = -99      # north edge of mask, -99 = silly value, to disable modifying mask
    ezSkyMaskDecDegS =  99      # south edge of mask,  99 = silly value, to disable modifying mask
    ezSkyMaskWrite = 0          # default = 0: not write mask to file

    ezSkyPlotRangeL = [0, 9999]             # save this range of plots to file

    plotCountdown = 15                      # number of plots still to print

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
    ezSkyBackground1 = os.path.dirname(__file__) + os.path.sep + 'ezSkyBackground1.jpg'  
    ezSkyBackground1XMax = 1624
    ezSkyBackground1YMax =  812

    # print status
    print()
    print('   ezRAObsName =', ezRAObsName)
    print()
    print('   ezSkyInput  =', ezSkyInput)
    print('   ezSkyVOGain =', ezSkyVOGain)
    print('   ezSkyHalfTallDec =', ezSkyHalfTallDec)
    print('   ezSkyDispGrid    =', ezSkyDispGrid)
    print('   ezSkyPlotRangeL  =', ezSkyPlotRangeL)
    print()
    print('   ezSkyMaskFile    =', ezSkyMaskFile)
    print('   ezSkyMaskDecDegN =', ezSkyMaskDecDegN)
    print('   ezSkyMaskDecDegS =', ezSkyMaskDecDegS)
    print('   ezSkyMaskWrite   =', ezSkyMaskWrite)



def readDataDir():
    # Open each .ezb radio file in each directory and read individual lines.
    # Creates ezRAObsName, ezSkyInputS, fileNameLast, raH, decDeg, gLatDeg, gLonDeg, power, antLen

    global cmdDirectoryS            # string

    global ezRAObsName              # string                                    creation
    global ezSkyInput               # integer
    global ezSkyInputS              # string                                    creation
    global fileNameLast             # string                                    creation

    global raH                      # float 1d array                            creation
    global decDeg                   # float 1d array                            creation
    global gLatDeg                  # float 1d array                            creation
    global gLonDeg                  # float 1d array                            creation
    global azDeg                    # float 1d array                            creation
    global elDeg                    # float 1d array                            creation
    global power                    # float 1d array                            creation
    global antLen                   # integer                                   creation

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

                # collect as lists, later convert to compact numpys
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

                    raHL.append(float(fileLineSplit[1]))
                    decDegL.append(float(fileLineSplit[2]))
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

                # to save memory, collect lists into more compact numpys
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
    global antLenM1                 # integer               creation

    global ezRAObsName              # string
    global fileNameLast             # string
    global titleS                   # string                creation

    global ezbColumnColor           # string list           creation

    print('  plotPrep ===============')

    antLenM1 = antLen - 1

    # plot titles
    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + '           ' + ezRAObsName \
        + '          (' + programName + ')'

    ezbColumnColor = ['green', 'green', 'green', 'green', 'green', 'green', 'green',
        'black', 'black', 'violet',
        'blue', 'blue', 'red', 'red', 'green', 'green', 'orange', 'orange', 'violet', 'violet']



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

    global xTickLocsAnt                         # array         creation?
    global xTickLabelsAnt                       # list          creation?
    global xLabelSAnt                           # string        creation?

    plt.clf()

    plt.plot(plotData1d, plotColorS)

    plt.title(titleS)
    plt.grid(ezSkyDispGrid)

    plt.xlabel(f'Sample Number (last={antLenM1:,})')
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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 10 or 10 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky010raH.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 20 or 20 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky020decDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 30 or 30 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky030gLatDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         gLatDegMax =', gLatDeg.max())
    print('                         gLatDegAvg =', np.mean(gLatDeg))
    print('                         gLatDegMin =', gLatDeg.min())

    plotEzSky1dSamplesAnt(plotName, gLatDeg, '', [-90., 90.], 'green',
        'Galactic Latitude (degrees)')



def plotEzSky040gLonDeg():

    global gLonDeg                          # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 40 or 40 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky040gLonDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print('                         gLonDegMax =', gLonDeg.max())
    print('                         gLonDegAvg =', np.mean(gLonDeg))
    print('                         gLonDegMin =', gLonDeg.min())

    plotEzSky1dSamplesAnt(plotName, gLonDeg, '', [-180., 180.], 'green',
        'Galactic Longitude (degrees)')



def plotEzSky070azDeg():

    global azDeg                            # float 1d array

    global ezSkyPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global fileNameLast                     # string

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 70 or 70 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky070azDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 80 or 80 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky080elDeg.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 100 or 100 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky100input_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1

    print(f'                         {ezSkyInputS[2:]}Max = {power.max()}')
    print(f'                         {ezSkyInputS[2:]}Avg = {np.mean(power)}')
    print(f'                         {ezSkyInputS[2:]}Min = {power.min()}')

    plotEzSky1dSamplesAnt(plotName, power, '', [], 'green',
        ezSkyInputS[2:])



def ezSkyGridRadec():
    # If needed, creates radecCount, radecPower, radecRaHalfDeg, radecDecHalfDeg

    global raH                      # float 1d array, from .ezb files
    global decDeg                   # float 1d array, from .ezb files
    global power                    # float 1d array, from .ezb files

    global radecCount               # float   1d array                          creation
    global radecPower               # float   1d array                          creation
    global radecRaHalfDeg           # integer 1d array                          creation
    global radecDecHalfDeg          # integer 1d array                          creation

    # if Radec grid not needed, then return
    if ezSkyPlotRangeL[1] < 200 or 399 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    print()
    print('  ezSkyGridRadec ================================')

    # integrate .ezb file data into grids,
    #   gridRadecCount and gridRadecPower for RaDec map    (in half-degree grid)
    gridRadecRaHalfDegRange = 360 + 360 + 1            # Ra=0    thru 360 degrees, or 0 thru 720 halfdeg
    gridRadecDecHalfDegRange = 90 + 90 + 90 + 90 + 1   # Dec=-90 thru Lat=+90 deg, or 0 thru 360 halfdeg
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

    raH    = []         # free memory
    decDeg = []         # free memory

    # unravel grids and collect as lists, and later convert to compact numpys
    radecCountL      = []
    radecPowerL      = []
    radecRaHalfDegL  = []
    radecDecHalfDegL = []
    for decHalfDeg in range(gridRadecDecHalfDegRange):
        for raHalfDeg in range(gridRadecRaHalfDegRange):
            if gridRadecCount[raHalfDeg, decHalfDeg]:
                radecCountL.append(gridRadecCount[raHalfDeg, decHalfDeg])
                # calculate average power
                radecPowerL.append(gridRadecPower[raHalfDeg, decHalfDeg] \
                    / gridRadecCount[raHalfDeg, decHalfDeg]) 
                radecRaHalfDegL.append(raHalfDeg)
                radecDecHalfDegL.append(decHalfDeg)

    gridRadecCount = []     # free memory
    gridRadecPower = []     # free memory

    # create compact numpys from lists
    radecCount       = np.array(radecCountL)
    radecCountL      = []   # free memory
    radecPower       = np.array(radecPowerL)
    radecPowerL      = []   # free memory
    radecRaHalfDeg   = np.array(radecRaHalfDegL)
    radecRaHalfDegL  = []   # free memory
    radecDecHalfDeg  = np.array(radecDecHalfDegL)
    radecDecHalfDegL = []   # free memory

    print(f'                         len(radecPower) = {len(radecPower):,}')



def plotEzSky200RBVO():
    # radio Sky Radec map with background, Power Vertical Offset

    global radecPower               # float   1d array
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 200 or 200 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky200RBVO_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
    radecRaHalfDegScaled  = (720 - radecRaHalfDeg ) * imgaxesRatioX
    radecDecHalfDegScaled = (360 - radecDecHalfDeg) * imgaxesRatioY

    # thin black horizontal line on each used scaled declination
    radecDecHalfDegScaledLast = 9999      # silly value
    for y in radecDecHalfDegScaled:
        if radecDecHalfDegScaledLast != y:
            radecDecHalfDegScaledLast = y
            plt.axhline(y=radecDecHalfDegScaledLast, linewidth=0.5, color='black')

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

    # plot each radecPower value as a dot with a radecPowerScaled offset from its scaled declination
    radecPowerScaled = radecPowerGain * (radecPowerAvg - radecPower)
    plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled + radecPowerScaled, s=1, marker='.',
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
    plt.close(fig)



def plotEzSky201RBMax():
    # radio Sky Radec map with background, dots on left and right maximum Power

    global radecPower               # float   1d array
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 201 or 201 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky201RBMax_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
    radecRaHalfDegScaled  = (720 - radecRaHalfDeg ) * imgaxesRatioX
    radecDecHalfDegScaled = (360 - radecDecHalfDeg) * imgaxesRatioY

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
    print('galRaHDegLeft054304 =', len(galRaHDegLeft054304))

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
    print('galRaHDegRight054304 =', len(galRaHDegRight054304))

    galRaHDegRight054304Scaled  = (720 - galRaHDegRight054304) * imgaxesRatioX
    galRaHDegLeft054304Scaled  = (720 - galRaHDegLeft054304) * imgaxesRatioX
    decHDegScaled = (360 - np.array(range(54,304))) * imgaxesRatioY

    plt.scatter(galRaHDegRight054304Scaled, decHDegScaled, s=100, marker='.', c='red')
    plt.scatter(galRaHDegLeft054304Scaled, decHDegScaled, s=100, marker='.', c='red')

    # find and plot dots on MaxRight and on MaxLeft
    radecDecHalfDegScaledLast = 9999                # silly value
    radecPowerMaxRight = -9999                      # silly value
    radecPowerMaxLeft  = -9999                      # silly value
    nMaxRight = -1                                  # silly value
    nMaxLeft  = -1                                  # silly value
    # walk through data, already sorted as increasing RaH then increasing Dec 
    for n in range(len(radecDecHalfDegScaled)):
        if radecDecHalfDegScaledLast != radecDecHalfDegScaled[n]:   # if new Dec
            radecDecHalfDegScaledLast = radecDecHalfDegScaled[n]
            print()
            #print(f'                 {radecDecHalfDeg[nMaxLeft]}:{radecDecHalfDeg[nMaxRight]}:')
            #print(f'{radecRaHalfDeg[nMaxLeft]},{radecRaHalfDeg[nMaxRight]},')
            if nMaxRight + 1:                       # if not silly value, plot MaxLeft
                if radecDecHalfDeg[nMaxRight] <= 304:   # if <= DecHDeg top of Galactic plane
                    raHDiff = (radecRaHalfDeg[nMaxRight] \
                        - galRaHDegRight054304[radecDecHalfDeg[nMaxRight] - 54]) / 30.
                    #print(f'    nMaxRight = {nMaxRight}   RaH = {radecRaHalfDeg[nMaxRight]/30.:.1f}',
                    #    f'  DecDeg = {radecDecHalfDeg[nMaxRight]/2.-90.}   raHDiff = {raHDiff:.1f}')
                    print(f' DecDeg = {radecDecHalfDeg[nMaxRight]/2.-90.}',
                        f'  RaH = {radecRaHalfDeg[nMaxRight]/30.:.1f}   Right raHDiff = {raHDiff:.1f}')
                plt.scatter(radecRaHalfDegScaled[nMaxRight], radecDecHalfDegScaled[nMaxRight],
                    s=100, marker='.', c='green')
                radecPowerMaxRight = -9999          # reset to silly value
                nMaxRight = -1                      # reset to silly value
            if nMaxLeft + 1:                        # if not silly value, plot MaxLeft
                #print(f'nMaxLeft = {nMaxLeft}   RaH = {radecRaHalfDeg[nMaxLeft]/30.}',
                #    f'  DecDeg = {radecDecHalfDeg[nMaxLeft]/2.}')
                if radecDecHalfDeg[nMaxLeft] <= 304:   # if <= DecHDeg top of Galactic plane
                    raHDiff = (radecRaHalfDeg[nMaxLeft] \
                        - galRaHDegLeft054304[radecDecHalfDeg[nMaxLeft] - 54]) / 30.
                    #print(f'  nMaxLeft = {nMaxLeft}   RaH = {radecRaHalfDeg[nMaxLeft]/30.:.1f}',
                    #    f'  DecDeg = {radecDecHalfDeg[nMaxLeft]/2.-90.}   raHDiff = {raHDiff:.1f}')
                    print(f' DecDeg = {radecDecHalfDeg[nMaxLeft]/2.-90.}',
                        f'  RaH = {radecRaHalfDeg[nMaxLeft]/30.:.1f}   Left  raHDiff = {raHDiff:.1f}')
                plt.scatter(radecRaHalfDegScaled[nMaxLeft], radecDecHalfDegScaled[nMaxLeft],
                    s=100, marker='.', c='green')
                radecPowerMaxLeft  = -9999          # reset to silly value
                nMaxLeft = -1                       # reset to silly value
        if radecRaHalfDeg[n] < 360:                 # if on right half of RaDec
            if radecPowerMaxRight < radecPower[n]:  # if found the new maxRight
                radecPowerMaxRight = radecPower[n]
                nMaxRight = n
        else:
            if radecPowerMaxLeft < radecPower[n]:   # if found the new maxLeft
                radecPowerMaxLeft = radecPower[n]
                nMaxLeft = n

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
    plt.close(fig)



def plotEzSky300RB():
    # radio Sky Radec map with background, Power color

    global radecPower               # float   1d array
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 300 or 300 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky300RB_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
    radecRaHalfDegScaled  = (720 - radecRaHalfDeg ) * imgaxesRatioX
    radecDecHalfDegScaled = (360 - radecDecHalfDeg) * imgaxesRatioY

    # plot each radecPower value as a dot with a radecPower color
    pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled, s=1, marker='|',
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
    plt.close(fig)



def plotEzSky301RBT():
    # radio Sky Radec map with background, Power color Tall

    global radecPower               # float   1d array
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 301 or 301 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky301RBT_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
    radecRaHalfDegScaled  = (720 - radecRaHalfDeg ) * imgaxesRatioX
    radecDecHalfDegScaled = (360 - radecDecHalfDeg) * imgaxesRatioY

    #    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    #    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
    #        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
    #        # plot each radecPower value as a dot with a radecPower color
    #        pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled-reachTallDecHalfDegScaled,
    #            s=1, marker='|', c=radecPower, cmap=plt.get_cmap('gnuplot'))
    #        pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled+reachTallDecHalfDegScaled,
    #            s=1, marker='|', c=radecPower, cmap=plt.get_cmap('gnuplot'))
    #        cbar2 = plt.colorbar(pts, orientation='horizontal', shrink=0.3, pad=0.06)
    #    # plot center, without offset
    #    pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled,
    #        s=1, marker='|', c=radecPower, cmap=plt.get_cmap('gnuplot'))

    # plot center, without offset
    radecRaHalfDegScaledAll = radecRaHalfDegScaled + 0.
    radecDecHalfDegScaledAll = radecDecHalfDegScaled + 0.
    radecPowerAll = radecPower + 0.
    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
        # plot each radecPower value as a dot with a radecPower color
        radecRaHalfDegScaledAll = np.concatenate([radecRaHalfDegScaledAll,
            radecRaHalfDegScaled, radecRaHalfDegScaled])
        radecDecHalfDegScaledAll = np.concatenate([radecDecHalfDegScaledAll,
            radecDecHalfDegScaled-reachTallDecHalfDegScaled,
            radecDecHalfDegScaled+reachTallDecHalfDegScaled])
        radecPowerAll = np.concatenate([radecPowerAll,
            radecPower, radecPower])
    # plot center, without offset
    pts = plt.scatter(radecRaHalfDegScaledAll, radecDecHalfDegScaledAll,
        s=1, marker='|', c=radecPowerAll, cmap=plt.get_cmap('gnuplot'))
    # free memory
    radecRaHalfDegScaledAll = []
    radecDecHalfDegScaledAll = []
    radecPowerAll = []

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
    plt.close(fig)



def plotEzSky309RBTC():
    # radio Sky Radec map with background, Count Tall

    global radecCount               # float   1d array
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
    global ezSkyHalfTallDec         # integer

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    global ezSkyBackground1         # string
    global ezSkyBackground1XMax     # integer
    global ezSkyBackground1YMax     # integer

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 309 or 309 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky309RBTC.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
    radecRaHalfDegScaled  = (720 - radecRaHalfDeg ) * imgaxesRatioX
    radecDecHalfDegScaled = (360 - radecDecHalfDeg) * imgaxesRatioY

    '''
    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
        # plot each radecCount value as a dot with a radecCount color
        pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled-reachTallDecHalfDegScaled,
            s=1, marker='|', c=radecCount, cmap=plt.get_cmap('gnuplot'))
        pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled+reachTallDecHalfDegScaled,
            s=1, marker='|', c=radecCount, cmap=plt.get_cmap('gnuplot'))
    # plot center offset
    pts = plt.scatter(radecRaHalfDegScaled, radecDecHalfDegScaled,
        s=1, marker='|', c=radecCount, cmap=plt.get_cmap('gnuplot'))
    '''

    # plot center, without offset
    radecRaHalfDegScaledAll = radecRaHalfDegScaled + 0.
    radecDecHalfDegScaledAll = radecDecHalfDegScaled + 0.
    radecCountAll = radecCount + 0.
    # to make tall, plot low scaled offset, then plot high scaled offset, from outside to inside
    for reachTallDec in range(ezSkyHalfTallDec, 0, -1):
        reachTallDecHalfDegScaled = reachTallDec * imgaxesRatioY
        # plot each radecPower value as a dot with a radecPower color
        radecRaHalfDegScaledAll = np.concatenate([radecRaHalfDegScaledAll,
            radecRaHalfDegScaled, radecRaHalfDegScaled])
        radecDecHalfDegScaledAll = np.concatenate([radecDecHalfDegScaledAll,
            radecDecHalfDegScaled-reachTallDecHalfDegScaled,
            radecDecHalfDegScaled+reachTallDecHalfDegScaled])
        radecCountAll = np.concatenate([radecCountAll,
            radecCount, radecCount])
    # plot center, without offset
    pts = plt.scatter(radecRaHalfDegScaledAll, radecDecHalfDegScaledAll,
        s=1, marker='|', c=radecCountAll, cmap=plt.get_cmap('gnuplot'))
    # free memory
    radecRaHalfDegScaledAll = []
    radecDecHalfDegScaledAll = []
    radecCountAll = []

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
    plt.close(fig)


def plotEzSky400RI():
    # radio Sky Radec map of Interpolated Power

    global radecPower               # float   1d array
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 400 or 400 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky400RI_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

    radecRaHalfDegMin = radecRaHalfDeg.min()
    print('                         radecRaHalfDegMin =', radecRaHalfDegMin)
    radecRaHalfDegMax = radecRaHalfDeg.max()
    print('                         radecRaHalfDegMax =', radecRaHalfDegMax)

    radecDecHalfDegMin = radecDecHalfDeg.min()
    print('                         radecDecHalfDegMin =', radecDecHalfDegMin)
    radecDecHalfDegMax = radecDecHalfDeg.max()
    print('                         radecDecHalfDegMax =', radecDecHalfDegMax)


    if radecRaHalfDegMin == radecRaHalfDegMax:
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
        print('              radecRaHalfDegMin == radecRaHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(2)

    if radecDecHalfDegMin == radecDecHalfDegMax:
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
        print('              radecDecHalfDegMin == radecDecHalfDegMax')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        return(3)

    xi = np.arange(0.,  721., 1.)         # in   0 to 360 degrees in half-degrees
    yi = np.arange(-180.,  181., 1.)        # in -90 to +90 degrees in half-degrees
    xi, yi = np.meshgrid(xi, yi)

    zi = griddata((radecRaHalfDeg, radecDecHalfDeg-180.), radecPower, (xi, yi), method='linear')

    ###zi = gaussian_filter(zi, 9.)

    maskPlotDecHalfDegN = ezSkyMaskDecDegN + ezSkyMaskDecDegN + 180
    maskPlotDecHalfDegS = ezSkyMaskDecDegS + ezSkyMaskDecDegS + 180

    maskRadec = (maskPlotDecHalfDegS <= yi) & (yi <= maskPlotDecHalfDegN)    # True gets np.nan later

    zi[maskRadec] = np.nan              # True gets np.nan

    maskRadec = None        # free memory
    del maskRadec

    fig = plt.figure()
    ax = fig.add_subplot(111)

    plt.contourf(xi, yi, zi, 100, cmap=plt.get_cmap('gnuplot'))
    #plt.plot(radecRaHalfDeg, radecDecHalfDeg-180., 'black')
    ax.scatter(radecRaHalfDeg, radecDecHalfDeg-180., marker='.', s=0.5,
        color='black', linewidths=0)

    plt.title(titleS)
    ###plt.grid(ezSkyDispGrid)

    #plt.xlim(720, 0)        # inverts x axis
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
    plt.close(fig)



def ezSkyGridGalactic():
    # If needed, creates galacticPower, galacticGLatHalfDeg, galacticGLonHalfDeg

    global gLatDeg                  # float 1d array
    global gLonDeg                  # float 1d array
    global power                    # float 1d array

    global galacticPower            # float   1d array                          creation
    global galacticGLatHalfDeg      # integer 1d array                          creation
    global galacticGLonHalfDeg      # integer 1d array                          creation

    # if galactic grid not needed, then return
    if ezSkyPlotRangeL[1] < 400 or 499 < ezSkyPlotRangeL[0]:
        return(1)

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

    gLatDeg = []        # free memory
    gLonDeg = []        # free memory
    power   = []        # free memory

    # unravel grids and collect as lists, and later convert to compact numpys
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

    gridGalacticCount = []      # free memory
    gridGalacticPower = []      # free memory

    # create compact numpys from lists
    galacticPower        = np.array(galacticPowerL)
    galacticPowerL       = []   # free memory
    galacticGLatHalfDeg  = np.array(galacticGLatHalfDegL)
    galacticGLatHalfDegL = []   # free memory
    galacticGLonHalfDeg  = np.array(galacticGLonHalfDegL)
    galacticGLonHalfDegL = []   # free memory

    print(f'                         len(galacticPower) = {len(galacticPower):,}')

    #galacticGLatHalfDeg = np.clip(galacticGLatHalfDeg, -180, 180)   # easy insurance
    #galacticGLonHalfDeg = np.clip(galacticGLonHalfDeg, -360, 359)   # easy insurance



def plotEzSky500GMI():
    # radio Sky Galactic Mercator projection map of Interpolated Power

    global galacticPower            # float   1d array
    global galacticGLatHalfDeg      # integer 1d array
    global galacticGLonHalfDeg      # integer 1d array

    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 500 or 500 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky500GMI_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
        print('              All this data has only one Right Ascension value.')
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
        print('              All this data has only one Declination value.')
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

    zi[np.isnan(zi)] = galacticPower.min()

    #maskPlotDecHalfDegN = ezSkyMaskDecDegN + ezSkyMaskDecDegN + 180
    #maskPlotDecHalfDegS = ezSkyMaskDecDegS + ezSkyMaskDecDegS + 180

    #maskRadec = (maskPlotDecHalfDegS <= yi) & (yi <= maskPlotDecHalfDegN)    # True gets np.nan later

    ######maskGalactic = np.zeros((180 + 1 + 180, 360 + 1 + 360), dtype=bool)   # True gets np.nan later
    ######zi[maskGalactic] = np.nan              # True gets np.nan

    ######maskGalactic = None     # free memory
    ######del maskGalactic

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
    plt.close(fig)



def plotEzSky501GSI():
    # radio Sky Galactic Sinusoidal projection map of Interpolated Power

    global galacticPower            # float   1d array
    global galacticGLatHalfDeg      # integer 1d array
    global galacticGLonHalfDeg      # integer 1d array

    global ezSkyInputS              # string

    global ezSkyPlotRangeL          # integer list
    global plotCountdown            # integer
    global fileNameLast             # string
    global titleS                   # string
    #global ezSkyDispGrid           # integer

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 501 or 501 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky501GSI_' + ezSkyInputS + '.png'
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

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
        print('              All this data has only one Right Ascension value.')
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
        print('              All this data has only one Declination value.')
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

    zi[np.isnan(zi)] = galacticPower.min()

    #maskPlotDecHalfDegN = ezSkyMaskDecDegN + ezSkyMaskDecDegN + 180
    #maskPlotDecHalfDegS = ezSkyMaskDecDegS + ezSkyMaskDecDegS + 180

    #maskRadec = (maskPlotDecHalfDegS <= yi) & (yi <= maskPlotDecHalfDegN)    # True gets np.nan later

    ######maskGalactic = np.zeros((180 + 1 + 180, 360 + 1 + 360), dtype=bool)   # True gets np.nan later
    ######zi[maskGalactic] = np.nan              # True gets np.nan

    ######maskGalactic = None     # free memory
    ######del maskGalactic

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # accounting for 360 offset, reduce the bottom south half's xi by sin(yi), mirror for the top north half
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

    # likewise, after accounting for offsets,
    #   reduce each galacticGLonHalfDeg[i] by cos(galacticGLatHalfDeg[i])
    galacticGLonHalfDegSinusoidal = np.empty_like(galacticGLonHalfDeg)
    for i in range(len(galacticGLonHalfDeg)):
        galacticGLonHalfDegSinusoidal[i] = (galacticGLonHalfDeg[i] - 360.) \
            * math.cos(math.radians(abs(galacticGLatHalfDeg[i] - 180.)) / 2.) + 360.

    # optional thin black lines of true data
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
    plt.close(fig)



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

    # if plot not wanted, then return
    if ezSkyPlotRangeL[1] < 600 or 600 < ezSkyPlotRangeL[0]:
        plotCountdown -= 1
        return(1)

    plotName = 'ezSky600azEl_' + ezSkyInputS + '.png'

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plotCountdown -= 1
    plt.clf()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    #ax.set_axis_off()

    pts = plt.scatter(azDeg, elDeg,
        s=1, marker='|', c=power, cmap=plt.get_cmap('gnuplot'))

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
    plt.close(fig)



def printGoodbye():

    global antLen                   # integer
    global commandString            # string
    global startTime
    global programRevision          # string

    # print status
    if 0:
        print()
        print('   ezRAObsName      =', ezRAObsName)
        if 0:
            print('   ezSkyDispGrid            =', ezSkyDispGrid)
        print('   antLen =', antLen)

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
    global radecRaHalfDeg           # integer 1d array
    global radecDecHalfDeg          # integer 1d array
    
    global xTickLocsAnt             # array


    startTime = time.time()

    print('programRevision = ' + programRevision)
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
    plotEzSky040gLonDeg()
    plotEzSky070azDeg()
    plotEzSky080elDeg()

    plotEzSky100input()

    # plot the azEl plots

    plotEzSky600azEl()

    # free azEl memory
    azDeg = []
    elDeg = []

    # plot the raDec plots
    
    # if needed, creates radecCount, radecPower, radecRaHalfDeg, radecDecHalfDeg
    ezSkyGridRadec()

    plotEzSky200RBVO()
    #plotEzSky201RBMax()

    plotEzSky300RB()
    plotEzSky301RBT()
    plotEzSky309RBTC()

    plotEzSky400RI()

    # free radec memory
    radecCount      = []
    radecPower      = []
    radecRaHalfDeg  = []
    radecDecHalfDeg = []

    # plot the Galactic plots

    # if needed, creates galacticPower, galacticGLatHalfDeg, galacticGLonHalfDeg
    ezSkyGridGalactic()

    plotEzSky500GMI()
    plotEzSky501GSI()

    printGoodbye()



if __name__== '__main__':
  main()

