programName = 'stereoJoin250120a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy stereoJoin program,
#   to read in left and right images, Left.png Right.png,
#   and plant and frame and write out one stereoOutput/ZLeft.png file,
#   after creating an stereoOutput directory.
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

# TTD:

# stereoJoin250120a, much dusting
# stereoJoin250118a, os.path.sep for Windows and Linux
# stereoJoin250117c,
# stereoJoin250117b,
# stereoJoin250117a,

# ezSky250105c, mesh .csv file for -ezSkyBallCsv and ezSky400


#matplotlib.use('agg')
import matplotlib.pyplot as plt

import os
import sys
import time

import numpy as np



def printUsage():

    global programRevision                  # string

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print()
    print('  Windows:   py      stereoJoin.py Left.png Right.png')
    print('  Linux:     python3 stereoJoin.py Left.png Right.png')
    print()
    print('  stereoJoin program to read in left and right images, Left.png Right.png,')
    print('  and plant and frame and write out one stereoOutput/ZLeft.png file,')
    print('  after creating an stereoOutput directory.')
    print()
    print('  py  stereoJoin.py -help          (print this help)')
    print('  py  stereoJoin.py -h             (print this help)')
    print()
    print('    -eXXXXXXXXXXXXXXzIgonoreThisWholeOneWord')
    print('         (any one word starting with -eX is ignored, handy for long command line editing)')
    print()
    print('EXAMPLES:')
    print()
    print(r'  Windows:  py       ..\ezRA\stereoJoin.py  aaa_003L.png aaa_003R.png')
    print(r'            py       ..\ezRA\stereoJoin.py  aaa_004L.png aaa_004R.png')
    print()
    print('  Linux:     python3  ../ezRA/stereoJoin.py  aaa_003L.png aaa_003R.png')
    print('             python3  ../ezRA/stereoJoin.py  aaa_004L.png aaa_004R.png')
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
    print('            stereoJoin.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print(' Python sys.version =', sys.version)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def stereoJoinArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global cmdDirectoryS                    # string            create

    print()
    print('   stereoJoinArgumentsCommandLine ===============')

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
            cmdLineSplitIndex += 1      # point to first argument value


            if cmdLineArgLower == 'help':
                printUsage()

            elif cmdLineArgLower == 'h':
                printUsage()


            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 2 <= len(cmdLineArgLower) and cmdLineArgLower[:2] == 'ex':
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



def stereoJoinArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global programRevision                  # string
    global commandString                    # string

    global cmdDirectoryS                    # string
    global cmdDirectoryL                    # list of strings

    global imageLeft                        # numpy of floats
    global imageRight                       # numpy of floats


    stereoJoinArgumentsCommandLine()        # process arguments from command line

    #if not cmdDirectoryS:
    print('               cmdDirectoryS =', cmdDirectoryS, '=')
    cmdDirectoryL = cmdDirectoryS.split()
    print('               cmdDirectoryL =', cmdDirectoryL, '=')
    if len(cmdDirectoryL) != 2:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  input data files inadequate:')
        print('               ', cmdDirectoryL)
        print()
        print()
        print()
        print()
        exit()



def plotStereo():
    # radio Sky Radec map with Background, power Vertical Offset

    global cmdDirectoryL            # list of strings
    
    
    print()
    #print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')
    plt.clf()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    imageLeft = plt.imread(cmdDirectoryL[0])
    print('                         imageLeft.shape =', imageLeft.shape)

    height, width, deep = imageLeft.shape
    print('                         height =', height)
    print('                         width  =', width)
    widthD2 = int(width / 2.)
    print('                         widthD2 =', widthD2)
    widthD4 = int(width / 4.)
    print('                         widthD4 =', widthD4)
    print('                         deep   =', deep)

    imageLeft = imageLeft[:,widthD4:widthD4+widthD2,:]
    print('                         imageLeft.shape =', imageLeft.shape)

    #plt.imsave(cmdDirectoryL[0][:-4]+'.2.png', imageLeft)



    imageRight = plt.imread(cmdDirectoryL[1])
    print()
    print('                         imageRight.shape =', imageRight.shape)

    height, width, deep = imageRight.shape
    heightM1 = height - 1
    print('                         height =', height)
    print('                         width  =', width)
    widthM1 = width - 1
    widthD2 = int(width / 2.)
    widthD2M1 = widthD2 - 1
    print('                         widthD2 =', widthD2)
    widthD4 = int(width / 4.)
    print('                         widthD4 =', widthD4)
    print('                         deep   =', deep)

    imageRight = imageRight[:,widthD4:widthD4+widthD2,:]
    print('                         imageRight.shape =', imageRight.shape)

    #plt.imsave(cmdDirectoryL[1][:-4]+'.2.png', imageRight)



    imageStereo = np.concatenate((imageLeft, imageRight), axis=1)
    print()
    print('                         imageStereo.shape =', imageStereo.shape)
    #print('                         imageStereo[0,0,:] =', imageStereo[0,0,:])
    # imageStereo[0,0,:] = [0. 0. 0. 1.]

    pixelWhite = np.array([1.0, 1.0, 1.0, 1.0])

    for heightIndex in range (height):
        imageStereo[heightIndex,0,:] = pixelWhite           # left
        imageStereo[heightIndex,widthD2M1,:] = pixelWhite   # middleLeft
        imageStereo[heightIndex,widthD2,:] = pixelWhite     # middleRight
        imageStereo[heightIndex,widthM1,:] = pixelWhite     # right

    for widthIndex in range (width):
        imageStereo[0,widthIndex,:] = pixelWhite            # top
        imageStereo[heightM1,widthIndex,:] = pixelWhite     # bottom

    # if does not exist - create new 'stereoOutput' directory
    if not os.path.exists('stereoOutput'):
        os.makedirs('stereoOutput')
        print(' Created new "stereoOutput" directory')

    outFileName = 'stereoOutput' + os.path.sep + 'Z' + cmdDirectoryL[0]

    print('                         outFileName =', outFileName, '=')
    plt.imsave(outFileName, imageStereo)



def printGoodbye():

    global commandString            # string
    global startTime
    global programRevision          # string

    stopTime = time.time()
    stopTimeS = time.ctime()
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

    startTime = time.time()

    #print('programRevision = ' + programRevision)
    print()

    commandString = ''
    for i in sys.argv:
        commandString += i + '  '
    print(' This Python command =', commandString)

    if len(sys.argv) < 3:
        printUsage()

    printHello()

    stereoJoinArguments()

    plotStereo()

    printGoodbye()



if __name__== '__main__':
  main()



# python3  ../ezRA/stereoJoin250120a.py  *.png
# python3  ../ezRA/stereoJoin250120a.py  rot3.1.png  rot3.0.png

