programName = 'ezFix230305a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezFix frequency spectrum data ezRA .txt file editor program.
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
# dataTimeUtcVlsr2000.mjd = 51544.0
# Log what ezFix is doing

# ezFix230305a.py, boilerplate from ezSky
# ezFix230301a.py, -ezez help wording
# ezFix230228a.py, -EM and -ES and many code improvements
# ezFix230226a.py, 
# ezFix230225b.py, 
# ezFix230225a.py, 
# ezFix230223d.py, 
# ezFix230223c.py, RG, RL, RAG, and RAL needs dataType
# ezFix230223b.py, 
# ezFix230223a.py, many code improvements
# ezFix230222b.py, many changes
# ezFix230222a.py, many changes
# ezFix230221b.py,
#   -EM  A 123 456 0 9999 2.1  (Edit Multiply: Ant (Any/Ant/Ref=1/A/R) samples 123 through 456,
#       freqBin 0 through 9999, multiply spectrum values by 2.1
#   -ES  R 123 456 0 9999 2.1  (Edit Set:      Ref (Any/Ant/Ref=1/A/R) samples 123 through 456,
#       freqBin 0 through 9999, set spectrum values to 2.1
# ezFix230221a.py, 
#   Edit Multiply: -EM AnyAntRef1AR sampleFirst sampleLast freqBinFirst freqBinLast Multiplier
# ezFix230216a.py, revised help screen
# ezFix230215a.py, -EG to -EC (Edit Ceiling), -EL to -EF (Edit Floor),
#   -EGS (Edit Gain Samples), -EGF (Edit Gain Frequency bin)
# ezFix221122a.py, -ET sign of 'sHH' to ezFixTimeShiftMM and ezFixTimeShiftSS
# ezFix220930a.py, prep for Git
# ezFix10z05u.py, ezDefaults.txt, ezCon to ezFix,

#import seaborn as sb

import os                       # used to grab all files in the current directory

import sys                

import time
#import datetime

#import matplotlib
#matplotlib.use('agg')
#import matplotlib.pyplot as plt
#plt.rcParams['agg.path.chunksize'] = 20000    # to support my many data points

#from astropy.time import Time
#from astropy import modeling

#import numpy as np

#from scipy.interpolate import griddata
#from scipy.ndimage.filters import gaussian_filter

import math
#math.isfinite
#from math import isfinite



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezFix.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezFix.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezFix data file changer program')
    print('  to remove unwanted samples from, combine, edit,')
    print('  and split frequency spectrum data ezRA .txt files,')
    print('  and write one or two "data" directory frequency spectrum data ezRA .txt files.')
    print('  ezFix will create a "data" directory if neccessary.')
    print()
    print('  "radioDataFileDirectories" may be one or more .txt radio data files:')
    print('         py  ezFix.py  bigDish220320_05.txt')
    print('         py  ezFix.py  bigDish220320_05.txt bigDish220321_00.txt')
    print('         py  ezFix.py  bigDish22032*.txt')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezFix.py  bigDish2203')
    print('         py  ezFix.py  bigDish2203 bigDish2204')
    print('         py  ezFix.py  bigDish22*')
    print('  "radioDataFileDirectories" may be a mix of .txt radio data files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezFix program,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('  Default is to create, in the "data" directory,')
    print('  an output filename with the base of the first unremoved input filename,')
    print('  adding one "b" character to make unique, followed by ".txt" .')
    print('  If that filename exists, will try "c", or try "d", ... up to "z".')
    print()
    print('  Each sample is tested against argument criteria,')
    print('  and is Removed away or is Edited.')
    print()
    print('EXAMPLES:')
    print()
    print('  py ezFix.py -help      (print this help)')
    print('  py ezFix.py -h         (print this help)')
    print()
    print('    -KN    123  456  (Keep only Raw sample Numbers 123 through 456, inclusive)')
    # ezFixKeepNumL
    print()
    print('    -RN    123  456  (Remove away Raw sample Numbers 123 through 456, inclusive)')
    # ezFixRemoveNumL
    print()
    print('    -RT  R           (Remove away sample if Type is a Reference (Any/Ant/Ref=1/A/R) sample)')
    # ezFixRemoveTypeS
    print()
    print('    -RG  A 0.678     (Remove away Ant (Any/Ant/Ref=1/A/R) sample if a spectrum value is Greater)')
    # ezFixRemoveGreaterL
    print('    -RL  A 0.678     (Remove away Ant (Any/Ant/Ref=1/A/R) sample if a spectrum value is Less   )')
    # ezFixRemoveLessL
    print()
    print('    -RAG A 0.678     (Remove away Ant (Any/Ant/Ref=1/A/R) sample if spectrum Average is Greater)')
    # ezFixRemoveAvgGreaterL
    print('    -RAL A 0.678     (Remove away Ant (Any/Ant/Ref=1/A/R) sample if spectrum Average is Less   )')
    # ezFixRemoveAvgLessL
    print()
    print()
    print('    -ET  -07:00:00             (Edit Timestamps: add this time (sHH:MM:SS) to all timestamps)')
    # ezFixEditTimeS
    print()
    print('    -EC  A 0.678               (Edit Ceiling: so no Ant (Any/Ant/Ref=1/A/R)')
    print('                                     sample spectrum values more than 0.678)')
    # ezFixEditCeilingL
    print('    -EF  A 0.678               (Edit Floor:   so no Ant (Any/Ant/Ref=1/A/R)')
    print('                                     sample spectrum values less than 0.678)')
    # ezFixEditFloorL
    print()
    print()
    print('    -EM  A 123 456 0 9999 2.1  (Edit Multiply: Ant (Any/Ant/Ref=1/A/R) samples 123 through 456,')
    print('                                     freqBin 0 through 9999, multiply spectrum values by 2.1)')
    # ezFixEditMultL
    print()
    print('    -ES  R 123 456 0 9999 2.1  (Edit Set:      Ref (Any/Ant/Ref=1/A/R) samples 123 through 456,')
    print('                                     freqBin 0 through 9999, set spectrum values to 2.1)')
    # ezFixEditSetL
    print()
    #
    # Which data values must be parsed and converted from data strings?:
    #      data values needed:  timeStamp   spectrum    dataFlags
    #
    # ezFixKeepNumL             No          No          No
    # ezFixRemoveNumL           No          No          No
    # ezFixRemoveTypeS                                  Y
    #
    # ezFixRemoveGreaterL                   Y           Y
    # ezFixRemoveLessL                      Y           Y
    # ezFixRemoveAvgGreaterL                Y           Y
    # ezFixRemoveAvgLessL                   Y           Y
    #
    # ezFixEditTimeS            Y           Y           Y
    #
    # ezFixEditCeilingL         Y           Y           Y
    # ezFixEditFloorL           Y           Y           Y
    #
    # ezFixEditMultL            Y           Y           Y
    # ezFixEditSetL             Y           Y           Y
    #
    # for any edit, all 3 are needed to be parsed (for data line reconstruction)
    #
    print()
    print('    -removed   bigDishRemoved.txt  (write removed   samples to bigDishRemoved.txt,')
    print('                                        even if file exists)')
    print('    -overwrite bigDishOut.txt      (write remaining samples to bigDishOut.txt,')
    print('                                        even if file exists)')
    print()
    print('    -ezRAObsName     bigDish 2 (force Observatory Name - FROM THE REST OF COMMAND LINE !!!)')
    print('    -ezRAObsLat      39.8282   (force Observatory Latitude  (degrees))')
    print('    -ezRAObsLon      -98.5696  (force Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl     563.88    (force Observatory Above Mean Sea Level (meters))')
    print()
    print('    -ezFixAzimuth   180.0      (force Azimuth   (degrees))')
    print('    -ezFixElevation 45.0       (force Elevation (degrees))')
    print('    -ezFixAddAzDeg  9.4        (if no ezFixAzimuth,   add to all file Azimuth   (degrees))')
    print('    -ezFixAddElDeg  -2.6       (if no ezFixElevation, add to all file Elevation (degrees))')
    print()
    print('    -ezDefaultsFile bigDish8.txt   (file of default arguments)')
    print()
    print('    -ezezIgonoreThisWholeOneWord')
    print('         (any one word starting with -ezez is ignored, handy for long command line editing)')
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

    print(' ( programRevision =', programRevision, ')')
    print()

    #print(sys.argv)
    #print(len(sys.argv))
    cmd = ''
    for i in sys.argv:
        #cmd = cmd + i + '  '
        cmd += i + '  '
    print(' This Python command = ' + cmd)



def ezFixArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global cmd                              # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezFixAzimuth                     # float
    global ezFixElevation                   # float
    global ezFixAddAzDeg                    # float
    global ezFixAddElDeg                    # float

    global ezFixKeepNumL                    # integer list
    global ezFixRemoveNumL                  # integer list
    global ezFixRemoveTypeS                 # string

    global ezFixRemoveGreaterL              # string and float list
    global ezFixRemoveLessL                 # string and float list
    global ezFixRemoveAvgGreaterL           # string and float list
    global ezFixRemoveAvgLessL              # string and float list

    global ezFixEditTimeS                   # string
    
    global ezFixEditCeilingL                # string and float list
    global ezFixEditFloorL                  # string and float list

    global ezFixEditMultL                   # string and integer and float list
    global ezFixEditSetL                    # string and integer and float list

    global ezFixOverwriteFilename           # string
    global ezFixRemovedWriteFilename        # string

    global cmdDirectoryS                    # string


    print()
    print('   ezFixArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileNameInput, 'r')

        #if fileDefaults.mode == 'r':
        # process each line in ezDefaultsFileNameInput
        
        #print('   ezColArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')
        print('      success opening ' + ezDefaultsFileNameInput)

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

            # ezRA arguments used by multiple programs:
            if thisLine0Lower == '-ezRAObsName'.lower():
                # note: to allow multiple words, read in the rest of line !!!!!!!!!!!
                ezRAObsName = ' '.join(thisLine[1:])
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])
                #print(      'ezRAObsName =', ezRAObsName, '=')

            elif thisLine0Lower == '-ezRAObsLat'.lower():
                ezRAObsLat  = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsLon'.lower():
                ezRAObsLon  = float(thisLine[1])

            elif thisLine0Lower == '-ezRAObsAmsl'.lower():
                ezRAObsAmsl = float(thisLine[1])


            # float arguments:
            elif thisLine0Lower == '-ezFixAzimuth'.lower():
                ezFixAzimuth = float(thisLine[1])

            elif thisLine0Lower == '-ezFixElevation'.lower():
                ezFixElevation = float(thisLine[1])

            elif thisLine0Lower == '-ezFixAddAzDeg'.lower():
                ezFixAddAzDeg = float(thisLine[1])

            elif thisLine0Lower == '-ezFixAddElDeg'.lower():
                ezFixAddElDeg = float(thisLine[1])


            # list arguments:
            elif thisLine0Lower == '-KN'.lower():
                ezFixKeepNumL.append(int(thisLine[1]))
                ezFixKeepNumL.append(int(thisLine[2]))

            elif thisLine0Lower == '-RN'.lower():
                ezFixRemoveNumL.append(int(thisLine[1]))
                ezFixRemoveNumL.append(int(thisLine[2]))

            elif thisLine0Lower == '-RG'.lower():
                ezFixRemoveGreaterL.append(thisLine[1])
                ezFixRemoveGreaterL.append(float(thisLine[2]))

            elif thisLine0Lower == '-RL'.lower():
                ezFixRemoveLessL.append(thisLine[1])
                ezFixRemoveLessL.append(float(thisLine[2]))

            elif thisLine0Lower == '-RAG'.lower():
                ezFixRemoveAvgGreaterL.append(thisLine[1])
                ezFixRemoveAvgGreaterL.append(float(thisLine[2]))

            elif thisLine0Lower == '-RAL'.lower():
                ezFixRemoveAvgLessL.append(thisLine[1])
                ezFixRemoveAvgLessL.append(float(thisLine[2]))

            elif thisLine0Lower == '-EC'.lower():
                ezFixEditCeilingL.append(thisLine[1])
                ezFixEditCeilingL.append(float(thisLine[2]))

            elif thisLine0Lower == '-EF'.lower():
                ezFixEditFloorL.append(thisLine[1])
                ezFixEditFloorL.append(float(thisLine[2]))

            elif thisLine0Lower == '-EM'.lower():
                ezFixEditMultL.append(thisLine[1])
                ezFixEditMultL.append(int(thisLine[2]))
                ezFixEditMultL.append(int(thisLine[3]))
                ezFixEditMultL.append(int(thisLine[4]))
                ezFixEditMultL.append(int(thisLine[5]))
                ezFixEditMultL.append(float(thisLine[6]))

            elif thisLine0Lower == '-ES'.lower():
                ezFixEditSetL.append(thisLine[1])
                ezFixEditSetL.append(int(thisLine[2]))
                ezFixEditSetL.append(int(thisLine[3]))
                ezFixEditSetL.append(int(thisLine[4]))
                ezFixEditSetL.append(int(thisLine[5]))
                ezFixEditSetL.append(float(thisLine[6]))


            # string arguments:
            elif thisLine0Lower == '-RT'.lower():
                ezFixRemoveTypeS = thisLine[1]

            elif thisLine0Lower == '-ET'.lower():
                ezFixEditTimeS = thisLine[1]


            elif thisLine0Lower[:6] == '-ezFix'.lower():
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


            elif thisLine0Lower == '-ezez'.lower():
                pass                # ignore


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
        fileDefaults.close()                #   then have processed all available lines in this defaults file



def ezFixArgumentsCommandLine():
    # process arguments from command line

    global cmd                              # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezFixAzimuth                     # float
    global ezFixElevation                   # float
    global ezFixAddAzDeg                    # float
    global ezFixAddElDeg                    # float

    global ezFixKeepNumL                    # integer list
    global ezFixRemoveNumL                  # integer list
    global ezFixRemoveTypeS                 # string

    global ezFixRemoveGreaterL              # string and float list
    global ezFixRemoveLessL                 # string and float list
    global ezFixRemoveAvgGreaterL           # string and float list
    global ezFixRemoveAvgLessL              # string and float list

    global ezFixEditTimeS                   # string
    
    global ezFixEditCeilingL                # string and float list
    global ezFixEditFloorL                  # string and float list

    global ezFixEditMultL                   # string and integer and float list
    global ezFixEditSetL                    # string and integer and float list

    global ezFixOverwriteFilename           # string
    global ezFixRemovedWriteFilename        # string

    global cmdDirectoryS                    # string


    print()
    print('   ezFixArgumentsCommandLine ===============')

    cmdLineSplit = cmd.split()
    cmdLineSplitLen = len(cmdLineSplit)
        
    if cmdLineSplitLen < 2:
        # need at least one data directory or file
        printUsage()

    cmdLineSplitIndex = 1       # units = command line words
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
                #ezRAObsName = cmdLineSplit[cmdLineSplitIndex]   # cmd line allows only one ezRAObsName word
                # note: to allow multiple words, read in the rest of command line !!!!!!!!!!!
                ezRAObsName = ' '.join(cmdLineSplit[cmdLineSplitIndex:])
                cmdLineSplitIndex = 9e99    # have just read in the rest of command line !!!!!!!!!!!
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])

            elif cmdLineArgLower == 'ezRAObsLat'.lower():
                ezRAObsLat  = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezRAObsLon'.lower():
                ezRAObsLon  = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezRAObsAmsl'.lower():
                ezRAObsAmsl = float(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:
            elif cmdLineArgLower == 'ezFixAzimuth'.lower():
                ezFixAzimuth = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezFixElevation'.lower():
                ezFixElevation = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezFixAddAzDeg'.lower():
                ezFixAddAzDeg = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == 'ezFixAddElDeg'.lower():
                ezFixAddElDeg = float(cmdLineSplit[cmdLineSplitIndex])


            # list arguments:
            elif cmdLineArgLower == 'KN'.lower():
                ezFixKeepNumL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixKeepNumL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'RN'.lower():
                ezFixRemoveNumL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixRemoveNumL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'RG'.lower():
                ezFixRemoveGreaterL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixRemoveGreaterL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'RL'.lower():
                ezFixRemoveLessL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixRemoveLessL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'RAG'.lower():
                ezFixRemoveAvgGreaterL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixRemoveAvgGreaterL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'RAL'.lower():
                ezFixRemoveAvgLessL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixRemoveAvgLessL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'EC'.lower():
                ezFixEditCeilingL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixEditCeilingL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'EF'.lower():
                ezFixEditFloorL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixEditFloorL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'EM'.lower():
                ezFixEditMultL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixEditMultL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditMultL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditMultL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditMultL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditMultL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == 'ES'.lower():
                ezFixEditSetL.append(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezFixEditSetL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditSetL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditSetL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditSetL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezFixEditSetL.append(float(cmdLineSplit[cmdLineSplitIndex]))


            # string arguments:
            elif cmdLineArgLower == 'RT'.lower():
                ezFixRemoveTypeS = cmdLineSplit[cmdLineSplitIndex]

            elif cmdLineArgLower == 'ET'.lower():
                ezFixEditTimeS = cmdLineSplit[cmdLineSplitIndex]

            elif cmdLineArgLower == 'overwrite'.lower():
                ezFixOverwriteFilename = cmdLineSplit[cmdLineSplitIndex]

            elif cmdLineArgLower == 'removed'.lower():
                ezFixRemovedWriteFilename = cmdLineSplit[cmdLineSplitIndex]

            elif cmdLineArgLower == 'ezDefaultsFile'.lower():
                ezFixArgumentsFile(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == 'ezez'.lower():
                pass                # ignore


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



def ezFixArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezFixAzimuth                     # float
    global ezFixElevation                   # float
    global ezFixAddAzDeg                    # float
    global ezFixAddElDeg                    # float

    global ezFixKeepNumL                    # integer list
    global ezFixRemoveNumL                  # integer list
    global ezFixRemoveTypeS                 # string

    global ezFixRemoveGreaterL              # string and float list
    global ezFixRemoveLessL                 # string and float list
    global ezFixRemoveAvgGreaterL           # string and float list
    global ezFixRemoveAvgLessL              # string and float list

    global ezFixEditTimeS                   # string
    
    global ezFixEditCeilingL                # string and float list
    global ezFixEditFloorL                  # string and float list

    global ezFixEditMultL                   # string and integer and float list
    global ezFixEditSetL                    # string and integer and float list

    global ezFixOverwriteFilename           # string
    global ezFixRemovedWriteFilename        # string

    global cmdDirectoryS                    # string


    # defaults
    #ezRAObsName = 'LebanonKS'
    ezRAObsName = ''
    ezRAObsLat                =  math.inf   # silly value, to disable
    ezRAObsLon                =  math.inf   # silly value, to disable
    ezRAObsAmsl               =  math.inf   # silly value, to disable

    ezFixAzimuth              =  math.inf   # silly value, to disable
    ezFixElevation            =  math.inf   # silly value, to disable
    ezFixAddAzDeg             = 0.          # ignored if ezFixAzimuth
    ezFixAddElDeg             = 0.          # ignored if ezFixElevation

    ezFixKeepNumL             = []          # empty, to disable
    ezFixRemoveNumL           = []          # empty, to disable
    ezFixRemoveTypeS          = ''          # empty, to disable

    ezFixRemoveGreaterL       = []          # empty, to disable
    ezFixRemoveLessL          = []          # empty, to disable
    ezFixRemoveAvgGreaterL    = []          # empty, to disable
    ezFixRemoveAvgLessL       = []          # empty, to disable

    ezFixEditTimeS            = ''          # empty, to disable

    ezFixEditCeilingL         = []          # empty, to disable
    ezFixEditFloorL           = []          # empty, to disable

    ezFixEditMultL            = []          # empty, to disable
    ezFixEditSetL             = []          # empty, to disable

    ezFixOverwriteFilename    = ''          # empty, to disable
    ezFixRemovedWriteFilename = ''          # empty, to disable

    #ezFixArgumentsFile('ezDefaults.txt')        # process arguments from ezDefaults.txt file

    ezFixArgumentsCommandLine()                 # process arguments from command line

    if 1:
        # print status after arguments
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezFixAzimuth   =', ezFixAzimuth)
        print('   ezFixElevation =', ezFixElevation)
        print('   ezFixAddAzDeg  =', ezFixAddAzDeg)
        print('   ezFixAddElDeg  =', ezFixAddElDeg)
        print()
        print('   ezFixKeepNumL    =', ezFixKeepNumL)
        print('   ezFixRemoveNumL  =', ezFixRemoveNumL)
        print('   ezFixRemoveTypeS =', ezFixRemoveTypeS)
        print()
        print('   ezFixRemoveGreaterL    =', ezFixRemoveGreaterL)
        print('   ezFixRemoveLessL       =', ezFixRemoveLessL)
        print('   ezFixRemoveAvgGreaterL =', ezFixRemoveAvgGreaterL)
        print('   ezFixRemoveAvgLessL    =', ezFixRemoveAvgLessL)
        print()
        print('   ezFixEditTimeS    =', ezFixEditTimeS)
        print()
        print('   ezFixEditCeilingL =', ezFixEditCeilingL)
        print('   ezFixEditFloorL   =', ezFixEditFloorL)
        print()
        print('   ezFixEditMultL    =', ezFixEditMultL)
        print('   ezFixEditSetL     =', ezFixEditSetL)
        print()
        print('   ezFixOverwriteFilename    =', ezFixOverwriteFilename)
        print('   ezFixRemovedWriteFilename =', ezFixRemovedWriteFilename)
        print()



def readDataDir():
    # Open each .txt radio file in each directory and read individual lines.

    global ezRAObsName              # string
    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float

    global ezFixAzimuth                     # float
    global ezFixElevation                   # float
    global ezFixAddAzDeg                    # float
    global ezFixAddElDeg                    # float

    global ezFixKeepNumL                    # integer list
    global ezFixRemoveNumL                  # integer list
    global ezFixRemoveTypeS                 # string

    global ezFixRemoveGreaterL              # string and float list
    global ezFixRemoveLessL                 # string and float list
    global ezFixRemoveAvgGreaterL           # string and float list
    global ezFixRemoveAvgLessL              # string and float list

    global ezFixEditTimeS                   # string
    
    global ezFixEditCeilingL                # string and float list
    global ezFixEditFloorL                  # string and float list

    global ezFixEditMultL                   # string and integer and float list
    global ezFixEditSetL                    # string and integer and float list

    global ezFixOverwriteFilename           # string
    global ezFixRemovedWriteFilename        # string

    global cmdDirectoryS                    # string


    print()
    print('   readDataDir ===============')

    if ezFixEditTimeS:
        # detect the sign and parse the ezFixEditTimeS into ezFixTimeShiftHH, ezFixTimeShiftMM, and ezFixEditTimeSS
        # -ET   -07:00:00 (Edit samples: add this time (sHH:MM:SS) to all timestamps)
        ezFixEditTimeSSplit = ezFixEditTimeS.split(':')
        ezFixTimeShiftHH = int(ezFixEditTimeSSplit[0])     # positive or negative 'sHH'
        # apply sign of 'sHH' to ezFixTimeShiftMM and ezFixEditTimeSS
        if ezFixEditTimeSSplit[0][0] == '-':               # if 'sHH' is negative (may be '-00')
            ezFixTimeShiftMM = -int(ezFixEditTimeSSplit[1])
            ezFixEditTimeSS = -int(ezFixEditTimeSSplit[2])
        else:
            ezFixTimeShiftMM = int(ezFixEditTimeSSplit[1])
            ezFixEditTimeSS = int(ezFixEditTimeSSplit[2])

    # if one of these argument values are not empty, may need to reconstruct data line
    ezFixEditedMaybe = ezFixEditTimeS or ezFixEditCeilingL or ezFixEditFloorL or ezFixEditMultL or ezFixEditSetL

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

    #fileObsName = ''
    sampleRemovedCount = 0     # number of removed samples
    sampleOutCount     = 0     # number of unremoved samples
    sampleCount        = 0     # number of removed and unremoved samples
    sampleEditedCount  = 0     # number of edited samples

    fileFreqMinLast    = 0     # 0 to flag not used yet
    fileFreqMaxLast    = 0     # 0 to flag not used yet
    fileFreqBinQtyLast = 0     # 0 to flag not used yet

    fileWriteRemoved   = 0     # 0 to flag file is not opened yet
    fileOut            = 0     # 0 to flag file is not opened yet

    ezFixKeepNumLen   = len(ezFixKeepNumL)
    ezFixRemoveNumLen = len(ezFixRemoveNumL)
    fileOutNameS      = ''     # to allow printing if unused
    timeStampUtcS     = ''     # will fill if needed
    
    # https://www.timeanddate.com/calendar/months/
    # January - 31 days
    # February - 28 days in a common year and 29 days in leap years
    # March - 31 days
    #            April - 30 days
    #            May - 31 days
    #            June - 30 days
    # July - 31 days
    # August - 31 days
    # September - 30 days
    #            October - 31 days
    #            November - 30 days
    #            December - 31 days
    monthsDaysL = [31,   31, 28, 31,   30, 31, 30,   31, 31, 30,   31, 30, 31]      # non-leap year Dec-Jan-Dec

    # if does not exist - create new 'data' directory
    if not os.path.exists('data'):
        os.makedirs('data')
        print(' Created new "data" directory')

    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]

        # if arguments are .txt filenames,
        # pass each of them through together as a mini directory list of .txt files.
        # Allows one .txt file from a directory of .txt files.
        # Allows .bat batch file control.
        if directory.lower().endswith('.txt'):
            fileList = [directory]
            directory = '.'
        else:
            fileList = os.listdir(directory)
            #fileList = sorted(os.listdir(directory))        # each directory is now sorted alphabetically
        fileListLen = len(fileList)
        #print(fileList)
        #print(fileListLen)
        #print()
        for fileCounter in range(fileListLen):
            fileReadName = fileList[fileCounter]
            #fileReadName = sys.argv[1]
            #print('  ', fileReadName)
            print()

            if not fileReadName.lower().endswith('.txt'):
                continue            # skip to next file

            fileRead = open(directory + os.path.sep + fileReadName, 'r')
            if fileRead.mode == 'r':
                #print(fileReadName)
                # read line 1 (required)
                ## from ezCol
                #thisLineSplit = fileRead.readline().split()
                thisLine = fileRead.readline()
                #print()
                #print(thisLine)
                ##thisLineSplit = thisLine.split()
                ##thisLineSplitLen = len(thisLineSplit)
                thisLineLen = len(thisLine)

                # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                ##    if not thisLineSplitLen:
                ##        break                           # End-Of-File, so get out of while loop
                ##    while(thisLineSplit[0][0] == '#'):  # passthrough data file comments (starting with '#')
                ##        fileOut.write(thisLine)
                ##        #thisLineSplit = fileRead.readline().split()
                ##        thisLine = fileRead.readline()
                ##        #print()
                ##        #print(thisLine)
                ##        thisLineSplit = thisLine.split()
                ##        thisLineSplitLen = len(thisLineSplit)
                ##        # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                ##        if not thisLineSplitLen:
                ##            break                               # End-Of-File, so get out of while loop
                #print()
                #print('AAAAAAAAA')
                #print(thisLineSplit)

                if not thisLineLen:
                    break                               # End-Of-File, so get out of while loop

                # requiring 'from ezCol'.
                #            01234567890
                # skip to next data file if line has too few characters
                if thisLineLen < 10:             # if not a valid data file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                         #   skip to next data file
                # skip to next data file if first characters not 'from ezCol'
                if thisLine[0:10] != 'from ezCol':   # if not a valid data file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                         #   skip to next data file
                ## skip to next data file if second word has less than 5 characters
                #if len(thisLineSplit[1]) < 5:        # if not a valid data file
                #    fileRead.close()                 #   then have processed all lines in this data file
                #    continue                         #   skip to next data file
                ## skip to next data file if second word not start with 'ezCol'
                #if thisLineSplit[1][:5] != 'ezCol':  # if not a valid data file
                #    fileRead.close()                 #   then have processed all lines in this data file
                #    continue                         #   skip to next data file

                # now assume a valid ezCol .txt data file

                # ezFix output format, 220616:
                #    from ezCol  ezFix10z05s.py  Jun-15-2021a  N0RQV
                #    #from ezCol  ezFix10z05s.py  Jun-15-2021a  N0RQV
                #    #optional comments 1
                #    #from ezCol09j8.py (Mar-13-2022a N0RQV)
                #    #optional comments 2
                #    lat 40.2995 long -105.084 amsl 1524 name N0RQV8 ez
                #    #optional comments 3
                #    freqMin 1419.2 freqMax 1421.61 freqBinQty 256
                #    #optional comments 4
                #    az 227.9 el 42.7
                #    #optional comments 5
                #    2022-03-16T00:00:00 1.09008573e-07 1.09265745e-07 1.11500545e-07 ... 
                #    #optional comments 6
                #    az 227.9 el 42.0
                #    #optional comments 7
                #    2022-03-16T01:00:00 1.09008573e-07 1.09265745e-07 1.11500545e-07 ... 
                #    #optional comments 8

                # start output file
                if ezFixOverwriteFilename:
                    fileOut = open('data' + os.path.sep + ezFixOverwriteFilename, 'w')
                else:
                    # create unused output filename
                    fileOutNameRootS = 'data' + os.path.sep \
                        + fileReadName.split(os.path.sep)[-1][:-4]
                    # try with one trailing character
                    fileOutNamePostS = 'bcdefghijklmnopqrstuvwxyz'
                    #fileOutNameS = ''       # to flag if no available filenames
                    for i in range(25):
                        fileOutNameS = fileOutNameRootS + fileOutNamePostS[i] + '.txt'
                        # if fileOutNameS is available
                        if not os.path.exists(fileOutNameS):
                            break           # get out of FOR loop
                    if not fileOutNameS:
                        # no available filenames
                        print()
                        print()
                        print()
                        print()
                        print()
                        print(' ========== FATAL ERROR: already too many files with',
                            'same fileName base:')
                        print(fileOutNameRootS)
                        print()
                        print()
                        print()
                        print()
                        print()
                        exit()
                    fileOut = open(fileOutNameS, 'w')

                if ezFixRemovedWriteFilename:
                    # start ezFixRemovedWriteFilename file
                    fileWriteRemoved = open(ezFixRemovedWriteFilename, 'w')
                    #print(' fileWriteRemoved =', fileWriteRemoved)
                    if not (fileWriteRemoved.mode == 'w'):
                        print()
                        print()
                        print()
                        print()
                        print()
                        print(' ========== FATAL ERROR:  Can not open ')
                        print(' ' + ezFixRemovedWriteFilename)
                        print(' file to write data out')
                        print()
                        print()
                        print()
                        print()
                        exit()

                fileOut.write('from ezCol  ' + programRevision + '\n')
                fileOut.write('#' + thisLine)        # passthrough, now as a comment
                # ezFixRemovedWriteFilename output does not passthrough comments
                if ezFixRemovedWriteFilename:
                    fileWriteRemoved.write('from ezCol  ' + programRevision + '\n')


                # read line 2 (required)
                ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb
                thisLine = fileRead.readline()
                thisLineSplit = thisLine.split()
                thisLineLen = len(thisLine)
                # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                if not thisLineLen:
                    break                               # End-Of-File, so get out of while loop
                while(thisLine[0] == '#'):          # passthrough data file comments (starting with '#')
                    fileOut.write(thisLine)
                    thisLine = fileRead.readline()
                    #print()
                    #print(thisLine)
                    thisLineSplit = thisLine.split()
                    thisLineLen = len(thisLine)
                    if not thisLineLen:
                        break                               # End-Of-File, so get out of while loop
                if not thisLineLen:
                    break                               # End-Of-File, so get out of while loop

                ### after optional comments, requiring 'lat '.
                ###            0123

                ### error if line has too few characters
                ##if thisLineLen < 4:                  # if not a valid data file
                ##    print('\n\nERROR\n\n\n')
                ##    fileRead.close()                 #   then have processed all lines in this data file
                ##    exit()
                ### error if first characters not 'lat '
                ##if thisLine[0:3] != 'lat ':          # if not a valid data file
                ##    print('\n\nERROR\n\n\n')
                ##    fileRead.close()                 #   then have processed all lines in this data file
                ##    exit()
                ### error if line has less than 2 words
                ##thisLineSplit = thisLine.split()
                ##if thisLineSplitLen < 7:             # if not a valid data file
                ##    print('\n\nERROR\n\n\n')
                ##    fileRead.close()                 #   then have processed all lines in this data file
                ##    exit()

                # assume a valid line
                fileObsLat  = float(thisLineSplit[1])
                print('   fileObsLat  = ', fileObsLat)
                fileObsLon = float(thisLineSplit[3])
                print('   fileObsLon  = ', fileObsLon)
                fileObsAmsl = float(thisLineSplit[5])
                print('   fileObsAmsl = ', fileObsAmsl)
                #    if not fileObsName and 7 < len(thisLineSplit):
                #        #fileObsName = ' '.join(i for i in thisLineSplit[7:])
                #        # bug: replace with thisLine[qqqq:] (to allow double spaces in name?)
                fileObsName = ' '.join(thisLineSplit[7:])
                print('   fileObsName = ', fileObsName)

                if not math.isfinite(ezRAObsLat):   # if not enabled
                    ezRAObsLat = fileObsLat
                    print()
                    print('   ezRAObsLat changed to ', ezRAObsLat)
                    print()
                elif ezRAObsLat != fileObsLat:
                    print()
                    print()
                    print()
                    print()
                    print()
                    print('   WARNING:                 ezRAObsLat in file = ', fileObsLat)
                    print('             does NOT match current ezRAObsLat = ', ezRAObsLat)
                    print()

                if not math.isfinite(ezRAObsLon):   # if not enabled
                    ezRAObsLon = fileObsLon
                    print()
                    print('   ezRAObsLon changed to ', ezRAObsLon)
                    print()
                elif ezRAObsLon != fileObsLon:
                    print()
                    print()
                    print()
                    print()
                    #sys.stdout.write('\a')
                    #sys.stdout.flush()
                    print()
                    print('   WARNING:                 ezRAObsLon in file = ', fileObsLon)
                    print('             does NOT match current ezRAObsLon = ', ezRAObsLon)
                    print()

                if not math.isfinite(ezRAObsAmsl):   # if not enabled
                    ezRAObsAmsl = fileObsAmsl
                    print()
                    print('   ezRAObsAmsl changed to ', ezRAObsAmsl)
                    print()
                elif ezRAObsAmsl != fileObsAmsl:
                    print()
                    print()
                    print()
                    print()
                    print()
                    print('   WARNING:                 ezRAObsAmsl in file = ', fileObsAmsl)
                    print('             does NOT match current ezRAObsAmsl = ', ezRAObsAmsl)
                    print()

                if not ezRAObsName:                  # if not enabled
                    ezRAObsName = fileObsName
                    print()
                    print('   ezRAObsName changed to ', ezRAObsName)
                    print()
                elif ezRAObsName != fileObsName:
                    print()
                    print()
                    print()
                    print()
                    print()
                    print('   WARNING:                 ezRAObsName in file = ', fileObsName)
                    print('             does NOT match current ezRAObsName = ', ezRAObsName)
                    print()

                fileOut.write( \
                    f'lat {ezRAObsLat:g} long {ezRAObsLon:g} amsl ' + str(ezRAObsAmsl) \
                    + ' name ' + ezRAObsName + '\n')
                if ezFixRemovedWriteFilename:
                    fileWriteRemoved.write( \
                        f'lat {ezRAObsLat:g} long {ezRAObsLon:g} amsl ' + str(ezRAObsAmsl) \
                        + ' name ' + ezRAObsName + '\n')


                # read line 3 (required)
                ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
                # assume a valid line
                thisLine = fileRead.readline()
                thisLineSplit = thisLine.split()
                thisLineSplitLen = len(thisLineSplit)
                # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                if not thisLineSplitLen:
                    break                               # End-Of-File, so get out of while loop
                while(thisLineSplit[0][0] == '#'):          # passthrough data file comments (starting with '#')
                    fileOut.write(thisLine)
                    thisLine = fileRead.readline()
                    #print()
                    #print(thisLine)
                    thisLineSplit = thisLine.split()
                    thisLineSplitLen = len(thisLineSplit)
                    # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                    if not thisLineSplitLen:
                        break                               # End-Of-File, so get out of while loop
                if not thisLineSplitLen:
                    break                               # End-Of-File, so get out of while loop

                fileFreqMin    = float(thisLineSplit[1])
                print('   fileFreqMin    = ', fileFreqMin)
                fileFreqMax    = float(thisLineSplit[3])
                print('   fileFreqMax    = ', fileFreqMax)
                fileFreqBinQty = int  (thisLineSplit[5])
                print('   fileFreqBinQty = ', fileFreqBinQty)

                if not fileFreqMinLast:
                    fileFreqMinLast = fileFreqMin
                elif fileFreqMinLast != fileFreqMin:
                    print()
                    print()
                    print()
                    print()
                    print()
                    print('   WARNING:                 FreqMin in file = ', fileFreqMin)
                    print('             does NOT match current FreqMin = ', fileFreqMinLast)
                    print()
                    exit()

                if not fileFreqMaxLast:
                    fileFreqMaxLast = fileFreqMax
                elif fileFreqMaxLast != fileFreqMax:
                    print()
                    print()
                    print()
                    print()
                    print()
                    print('   WARNING:                 FreqMax in file = ', fileFreqMax)
                    print('             does NOT match current FreqMax = ', fileFreqMaxLast)
                    print()
                    exit()

                if not fileFreqBinQtyLast:
                    fileFreqBinQtyLast = fileFreqBinQty
                elif fileFreqBinQtyLast != fileFreqBinQty:
                    print()
                    print()
                    print()
                    print()
                    print()
                    print('   WARNING:                 FreqMin in file = ', fileFreqBinQty)
                    print('             does NOT match current FreqMin = ', fileFreqBinQtyLast)
                    print()
                    exit()

                fileOut.write( \
                    f'freqMin {fileFreqMin:g} freqMax {fileFreqMax:g} freqBinQty ' \
                    + str(fileFreqBinQty) + '\n')
                if ezFixRemovedWriteFilename:
                    fileWriteRemoved.write( \
                        f'freqMin {fileFreqMin:g} freqMax {fileFreqMax:g} freqBinQty ' \
                        + str(fileFreqBinQty) + '\n')


                # read line 4 (required)
                ## az 227.9 el 42.7 
                # assume a valid line
                thisLine = fileRead.readline()
                thisLineSplit = thisLine.split()
                thisLineSplitLen = len(thisLineSplit)
                # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                if not thisLineSplitLen:
                    break                               # End-Of-File, so get out of while loop
                while(thisLineSplit[0][0] == '#'):          # passthrough data file comments (starting with '#')
                    fileOut.write(thisLine)
                    thisLine = fileRead.readline()
                    #print()
                    #print(thisLine)
                    thisLineSplit = thisLine.split()
                    thisLineSplitLen = len(thisLineSplit)
                    # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                    if not thisLineSplitLen:
                        break                               # End-Of-File, so get out of while loop
                if not thisLineSplitLen:
                    break                               # End-Of-File, so get out of while loop

                # add correction factor to file's Azimuth   (Degrees)
                dataAzimuth    = float(thisLineSplit[1]) + ezFixAddAzDeg
                # add correction factor to file's Elevation (Degrees)
                dataElevation  = float(thisLineSplit[3]) + ezFixAddElDeg

                print()
                print('   dataAzimuth   = ', dataAzimuth)
                print('   dataElevation = ', dataElevation)

                if math.isfinite(ezFixAzimuth):     # if enabled, use ezFixAzimuth
                    dataAzimuth = ezFixAzimuth

                if math.isfinite(ezFixElevation):   # if enabled, use ezFixElevation
                    dataElevation = ezFixElevation

                fileOut.write(f'az {dataAzimuth:g} el {dataElevation:g}\n')
                if ezFixRemovedWriteFilename:
                    fileWriteRemoved.write(f'az {dataAzimuth:g} el {dataElevation:g}\n')


                # now process all wanted data lines in that file that ends with .txt and allow read
                #sampleCount = 0        # increments whether or not the data line was collected
                #while(sampleCount < ezConUseSamplesRawLast):
                sampleCountFile = 0
                while 1:

                    #print('\r file = ' + str(fileCounter + 1) + ' of ' + str(fileListLen) \
                    #    + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
                    #    + ' = ' + directory + '/' + fileReadName + \
                    #    '                       ', end='')   # allow append to line
                    print('\r file = ' + str(fileCounter + 1) + ' of ' + str(fileListLen) \
                        + ' in dir ' + str(directoryCounter + 1) + ' of ' + str(directoryListLen) \
                        + ' = ' + directory + os.path.sep + fileReadName, end='')   # allow append to line
                    #    + ' = ' + directory + os.path.sep + fileReadName + \
                    #    '                       ', end='')   # allow append to line

                    # read line 5+
                    ## # times are in UTC
                    ## 2022-02-15T05:30:55 10.523690382 10.570080895 10.535587705 10.527403187 ... C
                    ## 2022-02-15T05:30:56 10.558290361 10.551762452 10.545512521 10.539835481 ...
                    ## ...
                    thisLine = fileRead.readline()
                    #print()
                    #print()
                    #print(thisLine)
                    #print('len(thisLine) =', len(thisLine))
                    #time.sleep(2)
                    thisLineSplit = thisLine.split()
                    thisLineSplitLen = len(thisLineSplit)
                    # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                    if not thisLineSplitLen:
                        break                               # End-Of-File, so get out of while loop
                    while(thisLineSplit[0][0] == '#'):  # passthrough data file comments
                        fileOut.write(thisLine)
                        thisLine = fileRead.readline()
                        #print()
                        #print(thisLine)
                        thisLineSplit = thisLine.split()
                        thisLineSplitLen = len(thisLineSplit)
                        # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                        if not thisLineSplitLen:
                            break                               # End-Of-File, so get out of while loop
                    # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                    if not thisLineSplitLen:
                        break                               # End-Of-File, so get out of while loop
                    #print('\nthisLineSplit =', thisLineSplit[:5])    

                    if fileFreqBinQty < thisLineSplitLen: # if enough words for a data line

                        # assume a data line

                        # need to remove sample ?   Before tests, assume no
                        ezFixRemoveRawThis = 0

                        # conditionals of the tests below are designed to speed execution, if ezFixRemoveRawThis, then no more tests are needed

                        # -KN : Keep Raw sample Numbers only if in an ezFixKeepNumL pair range
                        if ezFixKeepNumLen:                     # if ezFixKeepNumL enabled
                            ezFixKeepNumThis = 0                # assume not to keep
                            for ezFixKeepNumIndex in range(0, ezFixKeepNumLen, 2):
                                if ezFixKeepNumL[ezFixKeepNumIndex] <= sampleCount \
                                    and sampleCount <= ezFixKeepNumL[ezFixKeepNumIndex + 1]:
                                        ezFixKeepNumThis = 1    # yes, keep this raw sample
                                        break                   # get out of loop
                            if not ezFixKeepNumThis:            # if not wanted
                                ezFixRemoveRawThis = 1          # yes, remove this raw sample


                        # -RN : Remove away Raw sample Numbers if in an ezFixRemoveNumL pair range
                        if not ezFixRemoveRawThis and ezFixRemoveNumLen:          # if ezFixRemoveNumL enabled
                            for ezFixRemoveNumIndex in range(0, ezFixRemoveNumLen, 2):
                                if ezFixRemoveNumL[ezFixRemoveNumIndex] <= sampleCount \
                                    and sampleCount <= ezFixRemoveNumL[ezFixRemoveNumIndex + 1]:
                                        ezFixRemoveRawThis = 1  # yes, remove this raw sample
                                        break                   # get out of loop


                        # parse data flags
                        if not ezFixRemoveRawThis and fileFreqBinQty + 2 <= thisLineSplitLen:       # if data flags
                            dataFlagsS = (''.join(thisLineSplit[fileFreqBinQty + 1:])).lower()
                            #print('thisLineSplit[fileFreqBinQty + 1:] = ', thisLineSplit[fileFreqBinQty + 1:], ' ==============================================')
                            #dataFlagsS = thisLineSplit[fileFreqBinQty + 1:].lower()     # allow spaces
                        else:
                            dataFlagsS = ''
                        #print('\n\ndataFlagsS = ', dataFlagsS)


                        # -RT : Remove away sample if dataType ezFixRemoveTypeS[0][0] is a requested (Any/Ant/Ref=1/A/R) sample)
                        if not ezFixRemoveRawThis and ezFixRemoveTypeS:          # if ezFixRemoveTypeS enabled
                            ezFixRemoveTypeS00 = ezFixRemoveTypeS[0][0].lower()
                            #charInDataflags = ezFixRemoveTypeS00 in dataFlagsS
                            #print('\n\n... ezFixRemoveTypeS00 = ', ezFixRemoveTypeS00, ' =======================================')
                            #print('\n\n... charInDataflags = ', charInDataflags, ' =======================================')
                            if ezFixRemoveTypeS00 in dataFlagsS or (not dataFlagsS and ezFixRemoveTypeS00 == 'a') or ezFixRemoveTypeS00 == '1':
                                ezFixRemoveRawThis = 1          # yes, remove this raw sample, no more tests needed
                                #print('\n\n... removed: ezFixRemoveTypeS00 = ', ezFixRemoveTypeS00)


                        # parse timeStamp and spectrum data
                        if not ezFixRemoveRawThis:
                            # parse timeStamp from strings
                            timeStampUtcS = thisLineSplit[0]

                            # convert spectrum data from strings
                            radDataL = list(map(float, thisLineSplit[1:fileFreqBinQty + 1]))
                            #print()
                            #print('thisLineSplit =', thisLineSplit)
                            #print('radDataL =', radDataL)
                            #print('len(radDataL) =', len(radDataL))
                            #print('len(thisLineSplit) =', len(thisLineSplit))
                            #print()


                        # -RG : Remove away (Any/Ant/Ref=1/A/R) sample if any spectrum value is Greater
                        if not ezFixRemoveRawThis and ezFixRemoveGreaterL:
                            # -RG dataType ezFixRemoveGreaterL[0] is not empty
                            ezFixRemoveGreaterL00 = ezFixRemoveGreaterL[0][0].lower()
                            if ezFixRemoveGreaterL00 in dataFlagsS or (not dataFlagsS and ezFixRemoveGreaterL00 == 'a') or ezFixRemoveGreaterL00 == '1':
                                if ezFixRemoveGreaterL[1] < max(radDataL):
                                    ezFixRemoveRawThis = 1     # yes, remove this raw sample, no more tests needed


                        # -RL : Remove away (Any/Ant/Ref=1/A/R) sample if any spectrum value is Less
                        if not ezFixRemoveRawThis and ezFixRemoveLessL:
                            # -RL dataType ezFixRemoveLessL[0] is not empty
                            ezFixRemoveLessL00 = ezFixRemoveLessL[0][0].lower()
                            if ezFixRemoveLessL00 in dataFlagsS or (not dataFlagsS and ezFixRemoveLessL00 == 'a') or ezFixRemoveLessL00 == '1':
                                if min(radDataL) < ezFixRemoveLessL[1]:
                                    ezFixRemoveRawThis = 1     # yes, remove this raw sample, no more tests needed


                        # -RAG : Remove away (Any/Ant/Ref=1/A/R) sample if spectrum Average is Greater
                        if not ezFixRemoveRawThis and ezFixRemoveAvgGreaterL:
                            # -RAG dataType ezFixRemoveAvgGreaterL[0] is not empty
                            ezFixRemoveAvgGreaterL00 = ezFixRemoveAvgGreaterL[0][0].lower()
                            if ezFixRemoveAvgGreaterL00 in dataFlagsS or (not dataFlagsS and ezFixRemoveAvgGreaterL00 == 'a') or ezFixRemoveAvgGreaterL00 == '1':
                                radDataLAvg = sum(radDataL) / fileFreqBinQty
                                if ezFixRemoveAvgGreaterL[1] < radDataLAvg:
                                    ezFixRemoveRawThis = 1     # yes, remove this raw sample, no more tests needed


                        # -RAL : Remove away (Any/Ant/Ref=1/A/R) sample if spectrum Average is Less
                        if not ezFixRemoveRawThis and ezFixRemoveAvgLessL:
                            # -RAL dataType ezFixRemoveAvgLessL[0] is not empty
                            ezFixRemoveAvgLessL00 = ezFixRemoveAvgLessL[0][0].lower()
                            if ezFixRemoveAvgLessL00 in dataFlagsS or (not dataFlagsS and ezFixRemoveAvgLessL00 == 'a') or ezFixRemoveAvgLessL00 == '1':
                                radDataLAvg = sum(radDataL) / fileFreqBinQty
                                if radDataLAvg < ezFixRemoveAvgLessL[1]:
                                    ezFixRemoveRawThis = 1     # yes, remove this raw sample, no more tests needed


                        # -ET  -07:00:00 (Edit Timestamps: add this time (sHH:MM:SS) to all timestamps)
                        if not ezFixRemoveRawThis and ezFixEditTimeS:
                            # read in data timestamp
                            # 2022-05-06T00:00:23
                            #timeStampUtcS = thisLineSplit[0]
                            #print(' timeStampUtcS =', timeStampUtcS)
                            timestampTSplit = timeStampUtcS.split('T')
                            # 2022-05-06
                            timestampDateMinusSplit = timestampTSplit[0].split('-')
                            timestampYYYY  = int(timestampDateMinusSplit[0])
                            timestampMonth = int(timestampDateMinusSplit[1])
                            timestampDD    = int(timestampDateMinusSplit[2])
                            # 00:00:23
                            timestampTimeColonSplit = timestampTSplit[1].split(':')
                            timestampHH = int(timestampTimeColonSplit[0])
                            timestampMM = int(timestampTimeColonSplit[1])
                            timestampSS = int(timestampTimeColonSplit[2])

                            timestampSS += ezFixEditTimeSS
                            if timestampSS < 0:
                                # borrow from timestampMM
                                timestampSS += 60
                                timestampMM -= 1
                            elif 60 <= timestampSS:
                                # carry into timestampMM
                                timestampSS -= 60
                                timestampMM += 1

                            timestampMM += ezFixTimeShiftMM
                            if timestampMM < 0:
                                # borrow from timestampHH
                                timestampMM += 60
                                timestampHH -= 1
                            elif 60 <= timestampMM:
                                # carry into timestampHH
                                timestampMM -= 60
                                timestampHH += 1

                            timestampHH += ezFixTimeShiftHH
                            if timestampHH < 0:
                                # borrow from timestampDD
                                timestampHH += 24
                                timestampDD -= 1
                            elif 24 <= timestampHH:
                                # carry into timestampDD
                                timestampHH -= 24
                                timestampDD += 1

                            timestampMonthChanged = 0                               # assume no change
                            if timestampDD < 1:
                                # borrow from timestampMonth
                                timestampDD += monthsDaysL[timestampMonth - 1]
                                timestampMonth -= 1                                 # but what if into Feb or Dec ?
                                timestampMonthChanged = 1
                            elif monthsDaysL[timestampMonth] < timestampDD:
                                # carry into timestampMonth
                                timestampDD = 1
                                timestampMonth += 1                                 # but what if into Mar or Jan ?
                                timestampMonthChanged = 1

                            if timestampMonthChanged:
                                # adjustments needed if into Jan or Dec, or Feb or Mar
                                if timestampMonth == 13:                            # if was into Jan
                                    # carry into timestampYYYY
                                    timestampMonth = 1
                                    timestampYYYY += 1
                                elif timestampMonth == 0:                           # if was into Dec
                                    # borrow from timestampYYYY
                                    timestampMonth = 12
                                    timestampYYYY -= 1
                                else:
                                    # If was into Feb or Mar:
                                    # monthsDaysL and above assumed non-leap year with 28 days in Feb.
                                    # But is the sample year a leap year ?
                                    # https://www.timeanddate.com/date/leapyear.html
                                    # Leap year must be evenly divisible by 4;
                                    # If the year can also be evenly divided by 100, it is not a leap year;
                                    # unless...
                                    # The year is also evenly divisible by 400. Then it is a leap year.
                                    # According to these rules, the years 2000 and 2400 are leap years,
                                    # while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.
                                    # February is 28 days in a common year, and 29 days in leap years.
                                    if timestampYYYY % 4:
                                        leapYear = 0            # not divisible by 4, not a leap year
                                    elif not (timestampYYYY % 400):
                                        leapYear = 1            # divisible by 400, is a leap year
                                    elif timestampYYYY % 100:
                                        leapYear = 1            # divisible by 4, not divisible by 100, is a leap year
                                    else:
                                        leapYear = 0            # not divisible by 400, divisible by 100, not a leap year

                                    if leapYear:
                                        # then undo the change Feb or Mar month mistake
                                        #if timestampMonth == 2:            # if was thought to move backward into Feb
                                        #    timestampDD = 29
                                        #else:                              # was thought to move forward into Mar
                                        #    timestampMonth = 2
                                        #    timestampDD = 29
                                        # so in both directions, the answer is the same Feb-29
                                        timestampMonth = 2
                                        timestampDD = 29

                            # create new data timestamp
                            # 2022-05-06T00:00:23
                            # 01234567890123456789
                            timeStampUtcS = f'{timestampYYYY:04d}-{timestampMonth:02d}' \
                                + f'-{timestampDD:02d}T{timestampHH:02d}:{timestampMM:02d}' \
                                + f':{timestampSS:02d}'
                            #print(' timeStampUtcS =', timeStampUtcS)

                            # replace old timeStampUtcS
                            thisLine = timeStampUtcS + thisLine[19:]
                            #thisLineSplit = thisLine.split()
                            thisLineSplit[0] = timeStampUtcS
                            sampleEditedCount += 1


                        # Edit Ceiling: no (Any/Ant/Ref=1/A/R) sample spectrum values greater than ezFixEditCeilingL[1]
                        if not ezFixRemoveRawThis and ezFixEditCeilingL:
                            # -EC dataType ezFixEditCeilingL[0] is not empty
                            ezFixEditCeilingL00 = ezFixEditCeilingL[0][0].lower()
                            if ezFixEditCeilingL00 in dataFlagsS or (not dataFlagsS and ezFixEditCeilingL00 == 'a') or ezFixEditCeilingL00 == '1':
                                radDataL = [min(y, ezFixEditCeilingL[1]) for y in radDataL]
                                #print()
                                #print('     radDataL =', radDataL)
                                #print('     max(radDataL) =', max(radDataL))
                                sampleEditedCount += 1


                        # Edit Floor: no (Any/Ant/Ref=1/A/R) sample spectrum values less than ezFixEditFloorL[1]
                        if not ezFixRemoveRawThis and ezFixEditFloorL:
                            # -EF dataType ezFixEditFloorL[0] is not empty
                            ezFixEditFloorL00 = ezFixEditFloorL[0][0].lower()
                            if ezFixEditFloorL00 in dataFlagsS or (not dataFlagsS and ezFixEditFloorL00 == 'a') or ezFixEditFloorL00 == '1':
                                radDataL = [max(y, ezFixEditFloorL[1]) for y in radDataL]
                                sampleEditedCount += 1


                        # -EM  A 123 456 0 9999 2.1  (Edit Multiply: Ant (Any/Ant/Ref=1/A/R) samples 123 through 456,
                        #                               freqBin 0 through 9999, multiply spectrum values by 2.1)
                        if not ezFixRemoveRawThis and ezFixEditMultL:
                            # -EM dataType ezFixEditMultL[0] is not empty
                            ezFixEditMultL00 = ezFixEditMultL[0][0].lower()
                            if ezFixEditMultL00 in dataFlagsS or (not dataFlagsS and ezFixEditMultL00 == 'a') or ezFixEditMultL00 == '1':
                                if ezFixEditMultL[1] <= sampleCount and sampleCount <= ezFixEditMultL[2]:
                                    # sampleCount is within requested range, so multiply requested freqBin
                                    multiplyValue = ezFixEditMultL[5]
                                    radDataL[ezFixEditMultL[3]:ezFixEditMultL[4] + 1] = [y * multiplyValue for y in radDataL[ezFixEditMultL[3]:ezFixEditMultL[4] + 1]]
                                    #print()
                                    #print()
                                    #print('    sampleCount = ', sampleCount)
                                    #print('    ezFixEditMultL00 = ', ezFixEditMultL00)
                                    #print()
                                    sampleEditedCount += 1


                        # -ES  R 123 456 0 9999 2.1  (Edit Set:      Ref (Any/Ant/Ref=1/A/R) samples 123 through 456,
                        #                               freqBin 0 through 9999, set spectrum values to 2.1)
                        if not ezFixRemoveRawThis and ezFixEditSetL:
                            # -ES dataType ezFixEditSetL[0] is not empty
                            ezFixEditSetL00 = ezFixEditSetL[0][0].lower()
                            #print('    ezFixEditSetL00 =', ezFixEditSetL00, '=')
                            #print('    dataFlagsS =', dataFlagsS, '=')
                            if ezFixEditSetL00 in dataFlagsS or (not dataFlagsS and ezFixEditSetL00 == 'a') or ezFixEditSetL00 == '1':
                                if ezFixEditSetL[1] <= sampleCount and sampleCount <= ezFixEditSetL[2]:
                                    # sampleCount is within requested range, so set requested freqBin
                                    setValue = ezFixEditSetL[5]
                                    radDataL[ezFixEditSetL[3]:ezFixEditSetL[4] + 1] = [setValue for y in radDataL[ezFixEditSetL[3]:ezFixEditSetL[4] + 1]]
                                    #print()
                                    #print()
                                    #print('    sampleCount =', sampleCount)
                                    #print('    ezFixEditSetL00 =', ezFixEditSetL00)
                                    #print('    ezFixEditedMaybe =', ezFixEditedMaybe)
                                    #print()
                                    sampleEditedCount += 1


                        #print()
                        #print(' ezFixRemoveRawThis =', ezFixRemoveRawThis)
                        if ezFixRemoveRawThis:
                            # if removed output file enabled
                            if ezFixRemovedWriteFilename:
                                # write removed sample, sample unchanged
                                fileWriteRemoved.write(thisLine)
                            #else:
                            #    pass            # current sample unwanted
                                
                            sampleRemovedCount += 1

                        else:
                            # ezFixRemoveRawThis is 0
                            # write kept sample
                            if ezFixEditedMaybe:
                                # sample may have been edited, need to reconstruct data line
                                fileOut.write(timeStampUtcS + ' ' \
                                    + ' '.join(f'{x:.9g}' for x in radDataL) + ' ' + dataFlagsS.upper() + '\n')
                            else:
                                # sample was not changed
                                fileOut.write(thisLine)

                            #print(' sampleOutCount =', sampleOutCount)
                            sampleOutCount += 1

                        sampleCountFile += 1         # increments whether or not the data line was removed
                        sampleCount     += 1         # increments whether or not the data line was removed
                        #if 5 < sampleCount:
                        #    exit()

                        # allow append to line
                        print('    number of samples read =', sampleCountFile,
                            '    total sample count =', sampleCount, '              ', end='')

                        # flow on to next file line

                    ## az 227.9 el 42.7 
                    elif 4 <= thisLineSplitLen:
                        #if thisLineSplit[0][0] == '#':      # data file comments start with '#'
                        #    pass                            # flow on to next file line
                        while(thisLineSplit[0][0] == '#'):  # passthrough data file comments
                            fileOut.write(thisLine)
                            #thisLineSplit = fileRead.readline().split()
                            thisLine = fileRead.readline()
                            #print()
                            #print(thisLine)
                            thisLineSplit = thisLine.split()
                            if not thisLineSplitLen:
                                break                               # End-Of-File, so get out of while loop
                        # thisLineSplitLen ==    0=EOF  1=LF  2=1Character
                        if not thisLineSplitLen:
                            break                               # End-Of-File, so get out of while loop

                        #elif thisLineSplit[0] == 'az':
                        if thisLineSplit[0] == 'az':
                            # assume an az line
                            # add correction factor to file's Azimuth   (Degrees)
                            dataAzimuth   = float(thisLineSplit[1]) + ezFixAddAzDeg
                            # add correction factor to file's Elevation (Degrees)
                            dataElevation = float(thisLineSplit[3]) + ezFixAddElDeg

                            print('dataAzimuth   = ', dataAzimuth)
                            print('dataElevation = ', dataElevation)

                            if math.isfinite(ezFixAzimuth):     # if enabled, use ezFixAzimuth
                                dataAzimuth = ezFixAzimuth

                            if math.isfinite(ezFixElevation):   # if enabled, use ezFixElevation
                                dataElevation = ezFixElevation

                            fileOut.write(thisLine)

                        # flow on to next file line
                    # flow on to next file line

                #while 1:

                print()
                fileNameLast = fileReadName
                fileRead.close()

            # now have processed all lines in that file that allows read
            #if fileRead.mode == 'r':

        # now have processed all files in that directory
        #for fileCounter in range(fileListLen):

    # now have processed all lines in all directories
    #for directoryCounter in range(directoryListLen):

    # blank out the last filename
    print('\r                                                                              ' \
        + '                                                                                ')
    #print('\r samplesFileQty =', samplesFileQty, \
    #    '                                                                                              ')

    if fileWriteRemoved:
        fileWriteRemoved.close()

    if fileOut:
        fileOut.close()

    #print(' Total             samples read   =', sampleCount)

    if not sampleCount:
        print()
        print()
        print(" ========== FATAL ERROR: no data file loaded")
        print()
        print()
        print()
        exit()

    ###################################################################################

    if 1:
        # print status at ending
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezFixAzimuth   =', ezFixAzimuth)
        print('   ezFixElevation =', ezFixElevation)
        print('   ezFixAddAzDeg  =', ezFixAddAzDeg)
        print('   ezFixAddElDeg  =', ezFixAddElDeg)
        print()
        print('   ezFixKeepNumL    =', ezFixKeepNumL)
        print('   ezFixRemoveNumL  =', ezFixRemoveNumL)
        print('   ezFixRemoveTypeS =', ezFixRemoveTypeS)
        print()
        print('   ezFixRemoveGreaterL    =', ezFixRemoveGreaterL)
        print('   ezFixRemoveLessL       =', ezFixRemoveLessL)
        print('   ezFixRemoveAvgGreaterL =', ezFixRemoveAvgGreaterL)
        print('   ezFixRemoveAvgLessL    =', ezFixRemoveAvgLessL)
        print()
        print('   ezFixEditTimeS    =', ezFixEditTimeS)
        print()
        print('   ezFixEditCeilingL =', ezFixEditCeilingL)
        print('   ezFixEditFloorL   =', ezFixEditFloorL)
        print()
        print('   ezFixEditMultL    =', ezFixEditMultL)
        print('   ezFixEditSetL     =', ezFixEditSetL)
        print()
        print('   ezFixOverwriteFilename    =', ezFixOverwriteFilename)
        print('   ezFixRemovedWriteFilename =', ezFixRemovedWriteFilename)
        print()

    print('                         ezFixRemovedWriteFilename =', ezFixRemovedWriteFilename)
    print('                         fileOutNameS              =', fileOutNameS)
    print()
    print('                         Total removed   samples read   =', sampleRemovedCount,
        f'     === {100. * sampleRemovedCount / sampleCount:0.02f} % === removed')
    print('                         Total unremoved samples read   =', sampleOutCount)
    print()
    print('                         Total Edited    samples        =', sampleEditedCount)



def printGoodbye(startTime):

    global programRevision          # string
    global cmd                      # string

    if 0:
        # print status at ending
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezFixAzimuth   =', ezFixAzimuth)
        print('   ezFixElevation =', ezFixElevation)
        print('   ezFixAddAzDeg  =', ezFixAddAzDeg)
        print('   ezFixAddElDeg  =', ezFixAddElDeg)
        print()
        print('   ezFixKeepNumL    =', ezFixKeepNumL)
        print('   ezFixRemoveNumL  =', ezFixRemoveNumL)
        print('   ezFixRemoveTypeS =', ezFixRemoveTypeS)
        print()
        print('   ezFixRemoveGreaterL    =', ezFixRemoveGreaterL)
        print('   ezFixRemoveLessL       =', ezFixRemoveLessL)
        print('   ezFixRemoveAvgGreaterL =', ezFixRemoveAvgGreaterL)
        print('   ezFixRemoveAvgLessL    =', ezFixRemoveAvgLessL)
        print()
        print('   ezFixEditTimeS    =', ezFixEditTimeS)
        print()
        print('   ezFixEditCeilingL =', ezFixEditCeilingL)
        print('   ezFixEditFloorL   =', ezFixEditFloorL)
        print()
        print('   ezFixEditMultL    =', ezFixEditMultL)
        print('   ezFixEditSetL     =', ezFixEditSetL)
        print()
        print('   ezFixOverwriteFilename    =', ezFixOverwriteFilename)
        print('   ezFixRemovedWriteFilename =', ezFixRemovedWriteFilename)
        print()

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



#################################################################################################

def main():

    startTime = time.time()

    printHello()
    
    ezFixArguments()

    if 0:
        printUsage()

    readDataDir()

    printGoodbye(startTime)



if __name__== '__main__':
  main()

