programName = 'ezGal221123a.py'
programRevision = programName

# Easy Radio Astronomy (ezRA) ezGal GALaxy explorer program,
#   to read ezCon format *Gal.npz condensed data text file(s),
#   and optionally create .png plot files.

# TTD:
#       remove many global in main() ?????????
#       plotCountdown, 'plotting' lines only if plotting

# ezGal221123a.py, to ezGal690, and to X axis using -byFreqBinX
# ezGal221117a.py, "Galaxy Crossing" to "Galaxy Plane"
# ezGal221117a.py,
#   ezGal530velDecGLon.png to ezGal530galDecGLon.png,
#   ezGal550velGRot_*.png to ezGal550galRot_*.png,
#   ezGal690GLonDegP180_*ByFreqBinAvg.png to ezGal590gLonDegP180_*ByFreqBinAvg.png
# ezGal221017a.py, polishing
# ezGal221016a.py, polishing
# ezGal221013a.py, polishing
# ezGal221012a.py, polishing
# Jul-28-2022a, ezGal10z05b.py,
#   removed warning for missing ezDefaults.txt, ezCon to ezGal, ezVel to ezGal,
#   galGLon to velGLon, velDecP90GLonP180Count to galDecP90GLonP180Count
# ezGal10z05a.py, first try with *Gal.npz input, Jul-15-2022a  N0RQV
#   from "ezVelV7 (2).py"
#   Vel.npz changed to Gal.npz,
#   in ezVel512velGLonPolar plt.pcolormesh() gets shading='auto'
#   in ezVel513velGLonCountPolar plt.pcolormesh() gets shading='auto'
# May- 6-2021a  N0RQV
# ezVelV7.py, added fileObsName to loaded Vel.npz file format for plot titles,
#   fileObsName can be overwritten by optional ezRAObsName argument,
#   commented out unused arguments


import seaborn as sb

import os                       # used to grab all files in the current directory

import sys                

import time
import datetime

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
#plt.rcParams['agg.path.chunksize'] = 20000    # to support my many data points

from astropy import units as u
from astropy.time import Time
from astropy.coordinates import EarthLocation
from astropy.coordinates import SkyCoord
#from astropy import modeling

import numpy as np

from scipy.interpolate import griddata
from scipy.ndimage.filters import gaussian_filter

import math



def printUsage():
    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezGal.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezGal.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezGal GALaxy explorer program,')
    print('  to read ezCon format *Gal.npz condensed data text file(s),')
    print('  and optionally create .png plot files.')
    print()
    print('  "radioDataFileDirectories" may be one or more *Gal.npz condensed data text files:')
    print('         py  ezGal.py  bigDish220320_05Gal.npz')
    print('         py  ezGal.py  bigDish220320_05Gal.npz bigDish220321_00Gal.npz')
    print('         py  ezGal.py  bigDish22032*Gal.npz')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezGal.py  .')
    print('         py  ezGal.py  bigDish2203')
    print('         py  ezGal.py  bigDish2203 bigDish2204')
    print('         py  ezGal.py  bigDish22*')
    print('  "radioDataFileDirectories" may be a mix of *Gal.npz condensed data text files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezGal program,')
    print("  then in order from the ezDefaults.txt in the ezGal.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('    -ezRAObsName         bigDish   (observatory name for plot titles)')
    print()
    print('    -ezGalPlotRangeL     0  500      (save only this range of ezGal plots to file, to save time)')
    print('    -ezGalDispGrid       1           (turn on graphical display plot grids)')
    print()
    print('    -ezGalVelGLonEdgeFrac   0.5    ')
    print('         (velGLon level fraction for ezGal540velGLonEdgesB)')
    print('    -ezGalVelGLonEdgeLevel  0.5    ')
    print('         (velGLon level for ezGal540velGLonEdgesB, if 0 then use only ezGalVelGLonEdgeFrac)')
    print()
    print('    -ezDefaultsFile ../bigDish8.txt     (additional file of ezRA arguments)')
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
    print('            ezGal.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezGalArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsName                      # string

    global ezGalDispGrid                    # integer

    global ezGalVelGLonEdgeFrac             # float
    global ezGalVelGLonEdgeLevel            # float
    global ezGalPlotRangeL                  # integer list


    print()
    print('   ezGalArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileNameInput, 'r')

        # process each line in ezDefaultsFileNameInput
        
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


            thisLine0Lower = thisLine[0].lower()

            # ezRA arguments used by multiple programs:
            if thisLine0Lower == '-ezRAObsName'.lower():
                ezRAObsName = thisLine[1]
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])


            # integer arguments:
            elif thisLine0Lower == '-ezGalDispGrid'.lower():
                ezGalDispGrid = int(thisLine[1])


            # float arguments:
            elif thisLine0Lower == '-ezGalVelGLonEdgeFrac'.lower():
                ezGalVelGLonEdgeFrac = float(thisLine[1])

            elif thisLine0Lower == '-ezGalVelGLonEdgeLevel'.lower():
                ezGalVelGLonEdgeLevel = float(thisLine[1])


            # list arguments:
            ###elif thisLine0Lower == 'ezGalUseSamplesRawL'.lower():
            ###    ezGalUseSamplesRawL.append(int(thisLine[1]))
            ###    ezGalUseSamplesRawL.append(int(thisLine[2]))


            elif thisLine0Lower == '-ezGalPlotRangeL'.lower():
                ezGalPlotRangeL[0] = int(thisLine[1])
                ezGalPlotRangeL[1] = int(thisLine[2])


            elif 6 <= len(thisLine0Lower) and thisLine0Lower[:6] == '-ezGal'.lower():
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
    	#print ('   Warning: Error in opening file or reading ' + ezDefaultsFileName + ' file.')
    	##print ('   ... Using defaults ...')
    	#print ()
    	#print ()
    	#print ()
    	#print ()
    	pass

    else:
        fileDefaults.close()       #   then have processed all available lines in this Defaults file



def ezGalArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsName                      # string

    global ezGalVelGLonEdgeFrac             # float
    global ezGalVelGLonEdgeLevel            # float

    global ezGalPlotRangeL                  # integer list
    global ezGalDispGrid                    # integer

    global cmdDirectoryS                    # string            creation


    print()
    print('   ezGalArgumentsCommandLine ===============')

    cmdLineSplit = commandString.split()
    cmdLineSplitLen = len(cmdLineSplit)
        
    if cmdLineSplitLen < 2:
        # need at least one data directory or file
        printUsage()

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
            # Must be an option.
            # Remove '-'
            cmdLineOption = cmdLineSplit[cmdLineSplitIndex][1:]
            # ignoring whitespace, first character of cmdLineSplit word was '-', now removed
            if cmdLineOption[0] == '-':
                cmdLineOption = cmdLineOption[1:]
                # ignoring whitespace, first 2 characters of cmdLineSplit word were '--', now removed

            cmdLineOptionLower = cmdLineOption.lower()
            cmdLineSplitIndex += 1      # point to first option value


            if cmdLineOptionLower == 'help':
                printUsage()

            elif cmdLineOptionLower == 'h':
                printUsage()


            # ezRA arguments used by multiple programs:
            elif cmdLineOptionLower == 'ezRAObsName'.lower():
                ezRAObsName = cmdLineSplit[cmdLineSplitIndex]   # cmd line allows only one ezRAObsName word
                #ezRAObsName = uni.encode(thisLine[1])
                #ezRAObsName = str.encode(thisLine[1])
            

            # integer arguments:
            elif cmdLineOptionLower == 'ezGalDispGrid'.lower():
                ezGalDispGrid = int(cmdLineSplit[cmdLineSplitIndex])


            # float arguments:
            elif cmdLineOptionLower == 'ezGalVelGLonEdgeFrac'.lower():
                ezGalVelGLonEdgeFrac = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineOptionLower == 'ezGalVelGLonEdgeLevel'.lower():
                ezGalVelGLonEdgeLevel = float(cmdLineSplit[cmdLineSplitIndex])


            # list arguments:
            elif cmdLineOptionLower == 'ezGalPlotRangeL'.lower():
                ezGalPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezGalPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineOptionLower == 'ezDefaultsFile'.lower():
                ezGalArgumentsFile(cmdLineSplit[cmdLineSplitIndex])


            elif 4 <= len(cmdLineOptionLower) and cmdLineOptionLower[:4] == 'ezez':
                # ignore this one word that starts with '-ezez'
                pass


            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Command line has this unrecognized first word:')
                print('-' + cmdLineOption)
                print()
                print()
                print()
                print()
                exit()
                
        cmdLineSplitIndex += 1



def ezGalArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    #global programRevision                  # string
    #global commandString                    # string

    global ezRAObsName                      # string

    global ezGalVelGLonEdgeFrac             # float
    global ezGalVelGLonEdgeLevel            # float

    global ezGalPlotRangeL                  # integer list
    global plotCountdown                    # integer
    global ezGalDispGrid                    # integer


    # defaults
    #ezRAObsName = 'LebanonKS'
    #ezRAObsName = 'defaultKS'
    ezRAObsName = ''                # overwritten by optional argument

    ezGalVelGLonEdgeFrac  = 0.5     # velGLon level fraction for ezGal540velGLonEdgesB
    ezGalVelGLonEdgeLevel = 0.      # velGLon level for ezGal540velGLonEdgesB, if not 0 then
                                    #   ezGalVelGLonEdgeFrac ignored

    ezGalPlotRangeL = [0, 9999]     # save this range of plots to file
    plotCountdown = 9               # number of plots still to print
    ezGalDispGrid = 0

    # process arguments from ezDefaults.txt file in the same directory as this ezGal program
    ezGalArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezGalArgumentsFile('ezDefaults.txt')

    ezGalArgumentsCommandLine()             # process arguments from command line
    
    # print status
    print()
    print('   ezRAObsName =', ezRAObsName)
    print()
    print('   ezGalVelGLonEdgeFrac  =', ezGalVelGLonEdgeFrac)
    print('   ezGalVelGLonEdgeLevel =', ezGalVelGLonEdgeLevel)
    print()
    print('   ezGalPlotRangeL =', ezGalPlotRangeL)
    print('   ezGalDispGrid   =', ezGalDispGrid)



def readDataDir():
    # Open each data file in directory and read individual lines.

    global ezRAObsName              # string
    global fileObsName              # string                                    creation
    global fileFreqMin              # float                                     creation
    global fileFreqMax              # float                                     creation
    global fileFreqBinQty           # integer                                   creation

    global velGLonP180              # float 2d array                            creation
    global velGLonP180Count         # integer array                             creation
    global velGLonP180CountSum      # integer                                   creation
    global galDecP90GLonP180Count   # integer 2d array                          creation

    global fileNameLast             # string                                    creation

    print()
    print('   readDataDir ===============')

    #directoryList = sorted(cmdDirectoryS.split())           # sorted needed on Linux
    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    
    VelNpz_Qty = 0
    for directoryCounter in range(directoryListLen):
        directory = directoryList[directoryCounter]

        # if arguments are .txt filenames,
        # pass each of them through together as a mini directory list of .txt files.
        # Allows one .txt file from a directory of .txt files.
        if directory.endswith('Gal.npz'):
            fileList = [directory]
            directory = '.'
        else:
            fileList = sorted(os.listdir(directory))        # sorted needed on Linux
        fileListLen = len(fileList)
        for fileCounter in range(fileListLen):
            fileReadName = fileList[fileCounter]
            #print('\r file =', fileCounter + 1, ' of', fileListLen,
            #    ' in dir', directoryCounter + 1, ' of', directoryListLen,
            #    ' =', directory + os.path.sep + fileReadName, '                                      ',
            #    end='')   # allow append to line
            print(f'\r {VelNpz_Qty + 1}  file = {fileCounter + 1} of {fileListLen}',
                f' in dir {directoryCounter + 1} of {directoryListLen} =',
                directory + os.path.sep + fileReadName, '                                      ',
                end='')   # allow append to line

            if not fileReadName.endswith('Gal.npz'):
                continue                                # skip to next file

            npzfile = np.load(fileReadName)

            if not VelNpz_Qty:                      # if first *Gal.npz file
                fileObsName    = npzfile['fileObsName'].tolist()
                if ezRAObsName:
                    fileObsName = ezRAObsName       # overwrite fileObsName with argument
                fileFreqMin    = float(npzfile['fileFreqMin'])
                fileFreqMax    = float(npzfile['fileFreqMax'])
                fileFreqBinQty = int(npzfile['fileFreqBinQty'])

                # Velocity by Galactic Longitude (gLon) grid.
                # gLon is -180thru+180, adding 180, gives gLonP180 as 0thru360 which is more convenient.
                # velGLonP180 is fileFreqBinQty by 0thru360 gLonP180
                #velGLonP180 = np.zeros([fileFreqBinQty, 361], dtype = float)
                velGLonP180 = npzfile['velGLonP180']
                # velGLonP180Count is count of saved spectrums in velGLonP180
                #velGLonP180Count = np.zeros([361], dtype = int)
                velGLonP180Count = npzfile['velGLonP180Count']
                # Declination (dec) is -90thru+90, adding 90, gives decP90 as 0thru180 which is more convenient.
                # galDecP90GLonP180Count is 0thru180 decP90 by 0thru360
                #galDecP90GLonP180Count = np.zeros([181, 361], dtype = int)
                galDecP90GLonP180Count = npzfile['galDecP90GLonP180Count']
            else:
                # ignore npzfile['fileFreqMin'] 
                # ignore npzfile['fileFreqMax']
                # ignore npzfile['fileFreqBinQty'] 
                velGLonP180            += npzfile['velGLonP180']
                velGLonP180Count       += npzfile['velGLonP180Count']
                galDecP90GLonP180Count += npzfile['galDecP90GLonP180Count']

            VelNpz_Qty += 1
            fileNameLast = fileReadName
            print()

    # have now read all Gal.npz files

    # maybe blank out the last filename
    if not fileReadName.endswith('Gal.npz'):
        print('\r                                                                              ' \
            + '                                                                                ')
    else:
        print()
    
    if not VelNpz_Qty:                      # if no first *Gal.npz file
        print()
        print()
        print(" ========== FATAL ERROR: no data file loaded")
        print()
        print()
        print()
        exit()


    print(' fileNameLast =', fileNameLast)
    print(' VelNpz_Qty   =', VelNpz_Qty)

    print()
    print('fileFreqMin = ', fileFreqMin)
    print('fileFreqMax = ', fileFreqMax)
    print('fileFreqBinQty = ', fileFreqBinQty)

    print()
    print('velGLonP180.shape = ', velGLonP180.shape)
    print('velGLonP180Count.shape = ', velGLonP180Count.shape)
    print('galDecP90GLonP180Count.shape = ', galDecP90GLonP180Count.shape)

    print()
    velGLonP180CountSum = velGLonP180Count.sum()
    print('   velGLonP180CountSum =', velGLonP180CountSum)

    if not velGLonP180CountSum:       # if nothing in velGLonP180 to save or plot
        print()
        print()
        print(" ========== FATAL ERROR: no data loaded")
        print()
        print()
        print()
        exit()


    # for fileNameLast of  data/2021_333_00.txt  create fileVelWriteName as  data/2021_333_00GalC.npz
    fileVelWriteName = fileNameLast.split(os.path.sep)[-1][:-7] + 'GalC.npz'   # ezGal combines *Gal.npz
    print('   fileObsName = ', fileObsName)
    np.savez_compressed(fileVelWriteName, fileObsName=np.array(fileObsName),
        fileFreqMin=np.array(fileFreqMin), fileFreqMax=np.array(fileFreqMax),
        fileFreqBinQty=np.array(fileFreqBinQty),
        velGLonP180=velGLonP180, velGLonP180Count=velGLonP180Count,
        galDecP90GLonP180Count=galDecP90GLonP180Count)

    # Prepare velGLonP180 for later plots.
    # velGLonP180 has been filled with sums of samples.  Now for each column, convert to sum's average.
    for gLonP180 in range(361):
        if velGLonP180Count[gLonP180]:
            velGLonP180[:, gLonP180] /= velGLonP180Count[gLonP180]

    if 1:
        # mask low values with Not-A-Number (np.nan) to not plot
        #maskOffBelowThis = 0.975    # N0RQVHC
        #maskOffBelowThis = 0.9      # WA6RSV
        maskOffBelowThis = 1.0      # LTO15HC
        print(' maskOffBelowThis = ', maskOffBelowThis)
        maskThisOff = (velGLonP180 < maskOffBelowThis)
        #velGLonP180[maskThisOff] = np.nan                   # maskOffBelowThis is the do not plot
        velGLonP180[maskThisOff] = maskOffBelowThis         # maskOffBelowThis is the minumum everywhere



def plotPrep():
    # creates freqStep, dopplerSpanD2, freqCenter, titleS, byFreqBinX

    global fileObsName              # string
    global fileFreqMin              # float
    global fileFreqMax              # float
    global fileFreqBinQty           # integer

    global freqStep                 # float                 creation
    global dopplerSpanD2            # float                 creation
    global freqCenter               # float                 creation
    global titleS                   # string                creation

    global byFreqBinX               # float array           creation

    print()
    print('   plotPrep ===============')

    print('                         fileFreqMin =', fileFreqMin)
    print('                         fileFreqMax =', fileFreqMax)

    #freqStep = 0.00234375           # 2.4 MHz / 1024 = 0.00234375 MHz
    # fileFreqMin = 1419.205         #0000      -1.2 Doppler
    #                                #0512       0.0 Doppler
    # fileFreqMax = 1421.60265625    #1023       1.2 Doppler
    # (1421.60265625 - 1419.205 ) * 512 / 1023 = 1.2
    # 1.2  + 1419.205 = 1420.405 ------- yup
    #freqStep = (fileFreqMax - fileFreqMin) / (freqBinQtyPre + fileFreqBinQty - 1)
    freqStep = (fileFreqMax - fileFreqMin) / (fileFreqBinQty - 1)
    print('                         freqStep =', freqStep)
    #dopplerSpanD2 = (freqBinQtyPre + fileFreqBinQty) * 0.5 * freqStep
    #dopplerSpanD2 = fileFreqBinQty * 0.5 * freqStep         # Doppler spans -dopplerSpanD2 thru +dopplerSpanD2
    dopplerSpanD2 = (fileFreqMax - fileFreqMin) / 2.        # Doppler spans -dopplerSpanD2 thru +dopplerSpanD2
    print('                         dopplerSpanD2 =', dopplerSpanD2)
    #freqCenter = fileFreqMin + dopplerSpanD2
    freqCenter = (fileFreqMin + fileFreqMax) / 2.
    print('                         freqCenter =', freqCenter)

    #titleS = '  ' + fileNameLast.split('\\')[-1] + u'           N\u00D8RQV          (' + programName + ')'
    #titleS = '  ' + fileNameLast.split('\\')[-1] + u'           WA6RSV          (' + programName + ')'
    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + u'           ' + fileObsName \
        + '          (' + programName + ')'

    # increasing freq
    byFreqBinX = np.arange(fileFreqBinQty) * freqStep - dopplerSpanD2



def plotEzGal510velGLon():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global freqStep                 # float
    global ezGalPlotRangeL          # integer list

    pltNameS = 'ezGal510velGLon.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # if anything in velGLonP180 to save or plot
    if ezGalPlotRangeL[0] <= 510 and 510 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print(' velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        print()

        xi = np.arange(-180, +181, 1)           # +180 thru -180 degrees in degrees, galaxy centered
        #yi = np.arange(0, fileFreqBinQty, 1)    # 0 to fileFreqBinQty in freqBins
        # speed of light = 299,792,458 meters per second
        #    rawPlotPrep ===============
        #       fileFreqMin = 1419.2
        #       fileFreqMax = 1421.6
        #       freqStep = 0.009411764705881818
        #       dopplerSpanD2 = 1.1999999999999318
        #       freqCenter = 1420.4
        # velocity = (fileFreqBin doppler MHz) * (299792458. m/s / 1420.406 MHz) / 1000. = km/s
        # velocity spans = -dopplerSpanD2 * (299792458. / freqCenter) thru
        #                  +dopplerSpanD2 * (299792458. / freqCenter)
        #velocitySpanMax = +1.1999999999999318 * (299792458. / 1420.406) / 1000.  # = 253.273324388 km/s
        velocitySpanMax = +dopplerSpanD2 * (299792458. / freqCenter) / 1000.  # = 253.273324388 km/s
        yi = np.linspace(-velocitySpanMax, velocitySpanMax, fileFreqBinQty)

        xi, yi = np.meshgrid(xi, yi)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        print('                         np.nanmax(velGLonP180) =', np.nanmax(velGLonP180))
        print('                         np.mean(velGLonP180[~np.isnan(velGLonP180)]) =',
            np.mean(velGLonP180[~np.isnan(velGLonP180)]))
        print('                         np.nanmin(velGLonP180) =', np.nanmin(velGLonP180))
        pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'))
        #pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'), vmin=1.025, vmax=1.21)

        # horizonal thin black line
        plt.axhline(y =   0, linewidth=0.5, color='black')

        # vertical thin black lines
        plt.axvline(x =  90, linewidth=0.5, color='black')
        plt.axvline(x =   0, linewidth=0.5, color='black')
        plt.axvline(x = -90, linewidth=0.5, color='black')

        cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        plt.ylim(-velocitySpanMax, velocitySpanMax)        # in velocity

        #    plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
        #        + f'\n\nVelocity Count Sum = {velGLonP180CountSum}' \
        #        + f'\n\nVelocity Count Nonzero = {velGLonP180CountNonzero}' \
        #        + f' of {len(velGLonP180Count)}',
        #        rotation=90, verticalalignment='bottom')
        plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}'
            + f' Nonzero={velGLonP180CountNonzero} of {len(velGLonP180Count)}',
            rotation=90, verticalalignment='bottom')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal511velGLonCount():

    global plotCountdown            # integer
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezGalDispGrid            # integer
    #global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    pltNameS = 'ezGal511velGLonCount.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 511 and 511 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()
        plt.plot(np.arange(-180, +181, 1), velGLonP180Count)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print(' velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        print()

        plt.ylabel('Velocity Data Counts by Galactic Longitude' \
            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
            + f' Nonzero = {velGLonP180CountNonzero} of {len(velGLonP180Count)}')
        #    rotation=90, verticalalignment='bottom')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')


        # print out velGLonCount status
        fileWriteGLonName = 'ezGal511velGLonCount.txt'
        fileWriteGLon = open(fileWriteGLonName, 'w')
        if not (fileWriteGLon.mode == 'w'):
            print()
            print()
            print()
            print()
            print()
            print(' ========== FATAL ERROR:  Can not open ')
            print(' ' + fileWriteGLonName)
            print(' file to write out velGLonCount data')
            print()
            print()
            print()
            print()
            exit()


        fileWriteGLonHashS = '########################################' \
            + '########################################'                        # 40 + 40 = 80 '#'

        fileWriteGLon.write('\ngLonDeg (-180thru180)   velGLonCount   gLonDegForHaystackSrt.cmd '\
            + '(180thru359to0thru180)       (RtoL)\n\n')

        for gLonP180 in range(180):                               # for every column, RtoL, 0 thru 179
            fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLonP180Count[gLonP180]:5d}  {gLonP180 + 180:4d}  ' \
                + fileWriteGLonHashS[:velGLonP180Count[gLonP180]] + '\n'
            fileWriteGLon.write(fileWriteGLonS)

        fileWriteGLonS = f'0000  {velGLonP180Count[180]:5d}  0000  ' \
            + fileWriteGLonHashS[:velGLonP180Count[180]] + '\n'
        fileWriteGLon.write(fileWriteGLonS)

        for gLonP180 in range(181, 361):                          # for every column, RtoL, 181 thru 360
            fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLonP180Count[gLonP180]:5d}  {gLonP180 - 180:4d}  ' \
                + fileWriteGLonHashS[:velGLonP180Count[gLonP180]] + '\n'
            fileWriteGLon.write(fileWriteGLonS)


        # print out velGLonCount Things-To-Do for Haystack srt.cmd command file
        velGLonCountTrigger = 15
        fileWriteGLon.write( \
            '\n\n\n\n\n* velGLonCount Things-To-Do for Haystack srt.cmd command file    (RtoL)')
        fileWriteGLon.write('\n* velGLonCountTrigger = ' + str(velGLonCountTrigger))
        fileWriteGLon.write('\n\n:5              * short pause of 5 seconds')
        fileWriteGLon.write('\n: record')
        fileWriteGLon.write('\n* later, do not forget at the end,       : roff\n\n')
        fileWriteGLon.write( \
            '\n* 600 + 240 + 060 = 900 seconds = 10 + 4 + 1 minutes = 15 min data collection\n\n')

        for gLonP180 in range(180):                               # for every column, RtoL, 0 thru 179
            if velGLonP180Count[gLonP180] <= velGLonCountTrigger:
                fileWriteGLon.write(f': G{gLonP180 + 180:03d}    * have {velGLonP180Count[gLonP180]:5d}\n')
                fileWriteGLon.write(':600\n')
                fileWriteGLon.write(':240\n')
                fileWriteGLon.write(':060\n')
                fileWriteGLon.write('*\n')
        for gLonP180 in range(180, 361):                          # for every column, RtoL, 180 thru 360
            if velGLonP180Count[gLonP180] <= velGLonCountTrigger:
                fileWriteGLon.write(f': G{gLonP180 - 180:03d}    * have {velGLonP180Count[gLonP180]:5d}\n')
                fileWriteGLon.write(':600\n')
                fileWriteGLon.write(':240\n')
                fileWriteGLon.write(':060\n')
                fileWriteGLon.write('*\n')

        fileWriteGLon.close()   



def plotEzGal520velGLonPolar():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    pltNameS = 'ezGal520velGLonPolar.png'     # Velocity by Galactic Longitude with pcolormesh
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 520 and 520 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        rad = np.arange(0, fileFreqBinQty, 1)        # 0 to fileFreqBinQty in freqBins
        azm = np.linspace(0, np.pi + np.pi, 361, endpoint=True)
        r, theta = np.meshgrid(rad, azm)

        im = plt.pcolormesh(theta, r, velGLonP180.T, cmap=plt.get_cmap('gnuplot'), shading='auto')

        fig.colorbar(im, ax=ax, pad=0.1)

        polarPlot = plt.plot(azm, r, color='black', linestyle='none')
        plt.grid()


        plt.title(titleS)

        ax.set_rgrids((fileFreqBinQty/2.,), ('',))
        ax.set_theta_zero_location('S', offset=0.)
        ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

        ax.set_xlabel('Galactic Longitude (degrees) of Galaxy Plane Spectrums')
        ax.set_ylabel('Radius Is Increasing "Velocity",\n\n' \
            + 'Radius Is Increasing Receding,\n\n' \
            + 'Radius Is Decreasing Doppler\n\n')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal521velGLonPolarCount():

    global plotCountdown            # integer
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    pltNameS = 'ezGal521velGLonPolarCount.png'     # Velocity by Galactic Longitude with pcolormesh
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 521 and 521 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()

        fig = plt.figure()
        ax = fig.add_subplot(projection='polar')

        rad = np.arange(0, fileFreqBinQty, 1)        # 0 to fileFreqBinQty in freqBins
        azm = np.linspace(0, np.pi + np.pi, 361, endpoint=True)
        r, theta = np.meshgrid(rad, azm)

        velGLonP180CountPolar = np.zeros_like(velGLonP180.T, dtype=int)
        for gLonP180 in range(361):
            if velGLonP180Count[gLonP180]:
                velGLonP180CountPolar[gLonP180, :] += velGLonP180Count[gLonP180]

        im = plt.pcolormesh(theta, r, velGLonP180CountPolar, cmap=plt.get_cmap('gnuplot'), shading='auto')

        fig.colorbar(im, ax=ax, pad=0.1)

        polarPlot = plt.plot(azm, r, color='black', linestyle='none')
        plt.grid()

        plt.title(titleS)

        ax.set_rgrids((fileFreqBinQty/2.,), ('',))
        ax.set_theta_zero_location('S', offset=0.)
        ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

        ax.set_xlabel('Galactic Longitude (degrees) of Galaxy Plane Spectrums')
        ax.set_ylabel('Velocity Data Counts by Galactic Longitude' \
            + f'\n\nVelocity Count Sum = {velGLonP180CountSum:,}' \
            + f'\n\nVelocity Count Nonzero = {np.count_nonzero(velGLonP180Count)}' \
            + f' of {len(velGLonP180Count)}\n\n')

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal530galDecGLon():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global galDecP90GLonP180Count   # integer 2d array

    global titleS                   # string
    global ezGalDispGrid            # integer
    #global fileFreqBinQty           # integer
    global ezGalPlotRangeL          # integer list

    pltNameS = 'ezGal530galDecGLon.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 530 and 530 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()

        xi = np.arange(-180, +181, 1)           # +180 thru -180 degrees in degrees, galaxy centered
        yi = np.arange(0, 181, 1)               # 0 thru 180 decP90

        xi, yi = np.meshgrid(xi, yi)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        if 0:
            maskOffBelowThis = 0.975    # N0RQVHC
            maskOffBelowThis = 0.9      # WA6RSV
            maskOffBelowThis = -10
            print(' maskOffBelowThis = ', maskOffBelowThis)
            maskThisOff = (velGLonP180 < maskOffBelowThis)
            velGLonP180[maskThisOff] = np.nan

        pts = plt.contourf(xi, yi, galDecP90GLonP180Count, 20, cmap=plt.get_cmap('gnuplot'))

        plt.axhline(y =  90, linewidth=0.5, color='black')
        plt.axvline(x =  90, linewidth=0.5, color='black')
        plt.axvline(x =   0, linewidth=0.5, color='black')
        plt.axvline(x = -90, linewidth=0.5, color='black')

        cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        plt.ylabel('Velocity Counts on Declination by Galactic Longitude' \
            + f'\nVelocity Count Sum = {velGLonP180CountSum:,}')
        #    rotation=90, verticalalignment='bottom')
        plt.ylim(0, 180)                # in decP90
        plt.yticks([0,     30,    60,    90,  120,  150,  180],
                   ['-90', '-60', '-30', '0', '30', '60', '90'])

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal540velGLonEdgesB():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global freqStep                 # float
    global ezGalPlotRangeL          # integer list

    pltNameS = 'ezGal540velGLonEdgesB.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # if anything in velGLonP180 to save or plot
    if ezGalPlotRangeL[0] <= 540 and 540 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()

        # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
        velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
        print(' velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
        print()

        xi = np.arange(-180, +181, 1)           # +180 thru -180 degrees in degrees, galaxy centered
        #yi = np.arange(0, fileFreqBinQty, 1)    # 0 to fileFreqBinQty in freqBins
        # speed of light = 299,792,458 meters per second
        #    rawPlotPrep ===============
        #       fileFreqMin = 1419.2
        #       fileFreqMax = 1421.6
        #       freqStep = 0.009411764705881818
        #       dopplerSpanD2 = 1.1999999999999318
        #       freqCenter = 1420.4
        # velocity = (fileFreqBin doppler MHz) * (299792458. m/s / 1420.406 MHz) / 1000. = km/s
        # velocity spans = -dopplerSpanD2 * (299792458. / freqCenter) thru
        #                  +dopplerSpanD2 * (299792458. / freqCenter)
        #velocitySpanMax = +1.1999999999999318 * (299792458. / 1420.406) / 1000.  # = 253.273324388 km/s
        velocitySpanMax = +dopplerSpanD2 * (299792458. / freqCenter) / 1000.  # = 253.273324388 km/s
        yi = np.linspace(-velocitySpanMax, velocitySpanMax, fileFreqBinQty)

        xi, yi = np.meshgrid(xi, yi)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        print('                         np.nanmax(velGLonP180) =', np.nanmax(velGLonP180))
        print('                         np.mean(velGLonP180[~np.isnan(velGLonP180)]) =',
            np.mean(velGLonP180[~np.isnan(velGLonP180)]))
        print('                         np.nanmin(velGLonP180) =', np.nanmin(velGLonP180))
        pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'))
        #pts = plt.contourf(xi, yi, velGLonP180, 100, cmap=plt.get_cmap('gnuplot'), vmin=1.025, vmax=1.21)

        # horizonal thin black line
        plt.axhline(y =   0, linewidth=0.5, color='black')

        # vertical thin black lines
        plt.axvline(x =  90, linewidth=0.5, color='black')
        plt.axvline(x =   0, linewidth=0.5, color='black')
        plt.axvline(x = -90, linewidth=0.5, color='black')

        cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        plt.ylim(-velocitySpanMax, velocitySpanMax)        # in velocity

        #    plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
        #        + f'\n\nVelocity Count Sum = {velGLonP180CountSum}' \
        #        + f'\n\nVelocity Count Nonzero = {velGLonP180CountNonzero}' \
        #        + f' of {len(velGLonP180Count)}',
        #        rotation=90, verticalalignment='bottom')
        #    plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
        #        + f'\nVelocity Count:   Sum={velGLonP180CountSum}'
        #        + f'  Nonzero={velGLonP180CountNonzero} of {len(velGLonP180Count)}',
        #        rotation=90, verticalalignment='bottom')

        velGLonP180Max = velGLonP180.max()
        velGLonP180Min = velGLonP180.min()
        # if ezGalVelGLonEdgeLevel not 0, then ezGalVelGLonEdgeFrac ignored
        if ezGalVelGLonEdgeLevel:
            velGLonEdgeLevel = ezGalVelGLonEdgeLevel
            # create pltNameS with form of 'ezGal540velGLonEdgesB_nnnnn.png'
            pltNameS = f'ezGal540velGLonEdgesB_{ezGalVelGLonEdgeLevel:0.4f}.png'
        else:
            velGLonEdgeLevel = ezGalVelGLonEdgeFrac * (velGLonP180Max - velGLonP180Min) + velGLonP180Min
            # create pltNameS with form of 'ezGal540velGLonEdgesB_0.nnnnn.png'
            pltNameS = f'ezGal540velGLonEdgesB_{ezGalVelGLonEdgeFrac:0.4f}.png'

        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        print(' ezGalVelGLonEdgeFrac  =', ezGalVelGLonEdgeFrac)
        print(' ezGalVelGLonEdgeLevel =', ezGalVelGLonEdgeLevel)

        print('                         velGLonP180Max   =', velGLonP180Max)
        print('                         velGLonEdgeLevel =', velGLonEdgeLevel)
        print('                         velGLonP180Min   =', velGLonP180Min)

        velGLonUEdgeFreqBin = np.full(361, np.nan)      # unused nan will not plot
        velGLonLEdgeFreqBin = np.full(361, np.nan)      # unused nan will not plot

        # for Galactic plane crossings, velGLonUEdge will be the max velocity vs Galactic Longitude.
        # Page 46 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/
        #   Radioastro_21cm_2012b.pdf
        #   says the max Galactic velocity around Galactic center
        #   = galVelMax
        #   = velGLonUEdge + (earth Galactic rotation speed) * sin(gLon)
        #   = velGLonUEdge + (218 km/s)                      * sin(gLon)
        # galVelMax = velGLonUEdge + 218 * math.sin(math.radians(arange(361)))       # km/s
        galVelMax = np.full(361, np.nan)      # unused nan will not plot

        for gLonP180 in range(361):
            if velGLonP180Count[gLonP180]:
                # calculate Upper and Lower Detection Doppler of this velGLonP180 spectrum
                # https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
                # Tuple of arrays returned :  (array([ 4,  7, 11], dtype=int32),)
                # velGLonP180AboveLevelFreqBins are the freqBins with velGLonP180 >= velGLonEdgeLevel
                velGLonP180AboveLevelFreqBins = np.where(velGLonEdgeLevel <= velGLonP180[:, gLonP180])[0]

                if velGLonP180AboveLevelFreqBins.any():
                    velGLonUEdgeFreqBinThis = velGLonP180AboveLevelFreqBins[-1] # use last  element of list
                    velGLonLEdgeFreqBinThis = velGLonP180AboveLevelFreqBins[ 0] # use first element of list

                    # for the current gLonP180, ignoring nan,
                    #   remember the max velGLonUEdgeFreqBinThis and min velGLonLEdgeFreqBinThis


                    if np.isnan(velGLonUEdgeFreqBin[gLonP180]):
                        velGLonUEdgeFreqBin[gLonP180] = velGLonUEdgeFreqBinThis
                    else:
                        velGLonUEdgeFreqBin[gLonP180] = max(velGLonUEdgeFreqBin[gLonP180],
                        velGLonUEdgeFreqBinThis)

                    if np.isnan(velGLonLEdgeFreqBin[gLonP180]):
                        velGLonLEdgeFreqBin[gLonP180] = velGLonLEdgeFreqBinThis
                    else:
                        velGLonLEdgeFreqBin[gLonP180] = max(velGLonLEdgeFreqBin[gLonP180],
                        velGLonLEdgeFreqBinThis)

        # convert freqBin to velocity (km/s)
        velocityStep = freqStep * (299792458. / freqCenter) / 1000.                     # km/s
        velGLonUEdge = (velGLonUEdgeFreqBin - int(fileFreqBinQty / 2)) * velocityStep   # km/s
        velGLonLEdge = (velGLonLEdgeFreqBin - int(fileFreqBinQty / 2)) * velocityStep   # km/s

        # all used velGLonUEdgeFreqBin, are red  shifted
        plt.plot(np.arange(-180, +181, 1), velGLonUEdge, 'r.')

        # all used velGLonLEdgeFreqBin, are blue shifted
        plt.plot(np.arange(-180, +181, 1), velGLonLEdge, 'b.')


        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        ylabelS = 'Velocity Edges: Upper (Red) and Lower (Blue) (km/s)\n'
        #    # if ezGalVelGLonEdgeLevel not 0, then ezGalVelGLonEdgeFrac ignored
        #    if ezGalVelGLonEdgeLevel:
        #        ylabelS += f'ezGalVelGLonEdgeLevel = {ezGalVelGLonEdgeLevel:0.6f}'
        #    else:
        #        ylabelS += f'ezGalVelGLonEdgeFrac = {ezGalVelGLonEdgeFrac:0.6f}\n\n'
        #        ylabelS += f'velGLonEdgeLevel = {velGLonEdgeLevel:0.6f}'
        ylabelS += f'ezGalVelGLonEdge: Frac={ezGalVelGLonEdgeFrac:0.4f} Level={ezGalVelGLonEdgeLevel:0.4f}'
        plt.ylabel(ylabelS)
        #plt.ylim(-270, 270)

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal541velGLonEdges():

    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global ezGalVelGLonEdgeFrac     # float
    global ezGalVelGLonEdgeLevel            # float

    global titleS                   # string
    global ezGalDispGrid            # integer
    global fileFreqBinQty           # integer
    global dopplerSpanD2            # float
    global ezGalPlotRangeL          # integer list

    # If anything in velGLonP180 to plot.
    if ezGalPlotRangeL[0] <= 541 and 541 <= ezGalPlotRangeL[1] and velGLonP180CountSum:

        velGLonP180Max = velGLonP180.max()
        velGLonP180Min = velGLonP180.min()
        # if ezGalVelGLonEdgeLevel not 0, then ezGalVelGLonEdgeFrac ignored
        if ezGalVelGLonEdgeLevel:
            velGLonEdgeLevel = ezGalVelGLonEdgeLevel
            # create pltNameS with form of 'ezGal541velGLonEdges_nnnnn.png'
            pltNameS = f'ezGal541velGLonEdges_{ezGalVelGLonEdgeLevel:0.4f}.png'
        else:
            velGLonEdgeLevel = ezGalVelGLonEdgeFrac * (velGLonP180Max - velGLonP180Min) + velGLonP180Min
            # create pltNameS with form of 'ezGal541velGLonEdges_0.nnnnn.png'
            pltNameS = f'ezGal541velGLonEdges_{ezGalVelGLonEdgeFrac:0.4f}.png'

        print()
        print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')

        plt.clf()

        print(' ezGalVelGLonEdgeFrac  =', ezGalVelGLonEdgeFrac)
        print(' ezGalVelGLonEdgeLevel =', ezGalVelGLonEdgeLevel)

        print('                         velGLonP180Max   =', velGLonP180Max)
        print('                         velGLonEdgeLevel =', velGLonEdgeLevel)
        print('                         velGLonP180Min   =', velGLonP180Min)

        velGLonUEdgeFreqBin = np.full(361, np.nan)      # unused nan will not plot
        velGLonLEdgeFreqBin = np.full(361, np.nan)      # unused nan will not plot

        # for Galactic plane crossings, velGLonUEdge will be the max velocity vs Galactic Longitude.
        # Page 46 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/
        #   Radioastro_21cm_2012b.pdf
        #   says the max Galactic velocity around Galactic center
        #   = galVelMax
        #   = velGLonUEdge + (earth Galactic rotation speed) * sin(gLon)
        #   = velGLonUEdge + (218 km/s)                      * sin(gLon)
        # galVelMax = velGLonUEdge + 218 * math.sin(math.radians(arange(361)))       # km/s
        galVelMax = np.full(361, np.nan)      # unused nan will not plot

        for gLonP180 in range(361):
            if velGLonP180Count[gLonP180]:
                # calculate Upper and Lower Detection Doppler of this velGLonP180 spectrum
                # https://thispointer.com/find-the-index-of-a-value-in-numpy-array/
                # Tuple of arrays returned :  (array([ 4,  7, 11], dtype=int32),)
                # velGLonP180AboveLevelFreqBins are the freqBins with velGLonP180 >= velGLonEdgeLevel
                velGLonP180AboveLevelFreqBins = np.where(velGLonEdgeLevel <= velGLonP180[:, gLonP180])[0]

                if velGLonP180AboveLevelFreqBins.any():
                    velGLonUEdgeFreqBinThis = velGLonP180AboveLevelFreqBins[-1] # use last  element of list
                    velGLonLEdgeFreqBinThis = velGLonP180AboveLevelFreqBins[ 0] # use first element of list

                    # for the current gLonP180, ignoring nan,
                    #   remember the max velGLonUEdgeFreqBinThis and min velGLonLEdgeFreqBinThis


                    if np.isnan(velGLonUEdgeFreqBin[gLonP180]):
                        velGLonUEdgeFreqBin[gLonP180] = velGLonUEdgeFreqBinThis
                    else:
                        velGLonUEdgeFreqBin[gLonP180] = max(velGLonUEdgeFreqBin[gLonP180],
                        velGLonUEdgeFreqBinThis)

                    if np.isnan(velGLonLEdgeFreqBin[gLonP180]):
                        velGLonLEdgeFreqBin[gLonP180] = velGLonLEdgeFreqBinThis
                    else:
                        velGLonLEdgeFreqBin[gLonP180] = max(velGLonLEdgeFreqBin[gLonP180],
                        velGLonLEdgeFreqBinThis)

        # convert freqBin to velocity (km/s)
        velocityStep = freqStep * (299792458. / freqCenter) / 1000.                     # km/s
        velGLonUEdge = (velGLonUEdgeFreqBin - int(fileFreqBinQty / 2)) * velocityStep   # km/s
        velGLonLEdge = (velGLonLEdgeFreqBin - int(fileFreqBinQty / 2)) * velocityStep   # km/s

        # horizonal thin black line
        plt.axhline(y =   0, linewidth=0.5, color='black')

        # vertical thin black lines
        plt.axvline(x =  90, linewidth=0.5, color='black')
        plt.axvline(x =   0, linewidth=0.5, color='black')
        plt.axvline(x = -90, linewidth=0.5, color='black')

        # all used velGLonUEdgeFreqBin, are red  shifted
        plt.plot(np.arange(-180, +181, 1), velGLonUEdge, 'r.')

        # all used velGLonLEdgeFreqBin, are blue shifted
        plt.plot(np.arange(-180, +181, 1), velGLonLEdge, 'b.')


        plt.title(titleS)
        #plt.grid(ezGalDispGrid)
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([ 180,   90,   0,   -90,   -180],
                   ['180', '90', '0', '-90', '-180'])

        ylabelS = 'Velocity Upper Edge (Red) and Lower Edge (Blue)  (km/s)\n'
        #    # if ezGalVelGLonEdgeLevel not 0, then ezGalVelGLonEdgeFrac ignored
        #    if ezGalVelGLonEdgeLevel:
        #        ylabelS += f'ezGalVelGLonEdgeLevel = {ezGalVelGLonEdgeLevel:0.6f}'
        #    else:
        #        ylabelS += f'ezGalVelGLonEdgeFrac = {ezGalVelGLonEdgeFrac:0.6f}\n\n'
        #        ylabelS += f'velGLonEdgeLevel = {velGLonEdgeLevel:0.6f}'
        ylabelS += f'ezGalVelGLonEdge  Frac={ezGalVelGLonEdgeFrac:0.4f}  Level={ezGalVelGLonEdgeLevel:0.4f}'
        plt.ylabel(ylabelS)
        plt.ylim(-270, 270)

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')

    plotCountdown -= 1


    # since need same velGLonUEdge, merged plotEzGal550galRot() into plotEzGal541velGLonEdges()
    #def plotEzGal550galRot():
    # if ezGalVelGLonEdgeLevel not 0, then ezGalVelGLonEdgeFrac ignored
    if ezGalVelGLonEdgeLevel:
        velGLonEdgeLevel = ezGalVelGLonEdgeLevel
        # create pltNameS with form of 'ezGal541velGLonEdges_nnnnn.png'
        pltNameS = f'ezGal550galRot_{ezGalVelGLonEdgeLevel:0.4f}.png'
    else:
        velGLonEdgeLevel = ezGalVelGLonEdgeFrac * (velGLonP180Max - velGLonP180Min) + velGLonP180Min
        # create pltNameS with form of 'ezGal541velGLonEdges_0.nnnnn.png'
        pltNameS = f'ezGal550galRot_{ezGalVelGLonEdgeFrac:0.4f}.png'
    print()
    print('  ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ================================')
    plotCountdown -= 1

    # If anything in velGLonP180 to plot.
    # This plotEzGal550galRot() requires plotEzGal541velGLonEdges() to run.
    if ezGalPlotRangeL[0] <= 550 and 550 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plt.clf()

        # Status: for Galactic plane crossings, velGLonUEdge are max velocities vs Galactic longitude.
        # Page 46 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/
        #   Radioastro_21cm_2012b.pdf
        #   says for 0 <= gLon <= 90, the max Galactic velocity around Galactic center
        #   = galVelMax
        #   = galGasVelMax + (earth Galactic rotation speed) * sin(gLon)
        #   = galGasVelMax + (218 km/s)                      * sin(gLon)
        galGasVelMax = np.add(velGLonUEdge[180:180 + 91], 218 * np.sin(np.radians(np.arange(91))))   # in km/s

        # Page 46 also
        #   says for 0 <= gLon <= 90, the Galactic gas radius from Galactic center
        #   = galGasRadius
        #   = (Solar radius from Galactic center)      * sin(gLon)
        #   = (2.6e17 km * (Light year / 9.461e+12 km) * sin(gLon)
        #   = 27481 light years                        * sin(gLon)
        #
        #   = (26000 light years says https://en.wikipedia.org/wiki/Galactic_Center) * sin(gLon)
        galGasRadius = 26000 * np.sin(np.radians(np.arange(91)))            # in light years

        plt.plot(galGasRadius, galGasVelMax, 'g.')

        plt.title(titleS)
        plt.grid(ezGalDispGrid)
        plt.xlabel('Gas Radius from Galactic Center (Light Years)')
        plt.xlim(0, 26000)        # radius from 0 to Solar radius from Galactic center (=26000 light years)
        plt.xticks([0,   5000.,   10000.,   15000.,   20000.,   25000.],
                   ['0', '5,000', '10,000', '15,000', '20,000', '25,000'])

        ylabelS = 'Gas Max Velocity around Galactic Center (km/s)\n\n'
        # if ezGalVelGLonEdgeLevel not 0, then ezGalVelGLonEdgeFrac ignored
        if ezGalVelGLonEdgeLevel:
            ylabelS += f'ezGalVelGLonEdgeLevel = {ezGalVelGLonEdgeLevel:0.6f}'
        else:
            ylabelS += f'ezGalVelGLonEdgeFrac = {ezGalVelGLonEdgeFrac:0.6f}\n\n'
            ylabelS += f'velGLonEdgeLevel = {velGLonEdgeLevel:0.6f}'
        plt.ylabel(ylabelS)

        if os.path.exists(pltNameS):    # to force plot file date update, if file exists, delete it
            os.remove(pltNameS)
        plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def plotEzGal690gLonDegP180_nnnByFreqBinAvg():

    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global plotCountdown            # integer
    global elevation                # float array
    global titleS                   # string
    global ezGalDispGrid            # integer
    global byFreqBinX               # float array
    global ezGalPlotRangeL          # integer list

    # if anything in velGLonP180 to plot
    if ezGalPlotRangeL[0] <= 690 and 690 <= ezGalPlotRangeL[1] and velGLonP180CountSum:
        plotCountdown += np.count_nonzero(velGLonP180Count)

        if 1:
            # same ylim for all ezGal690gLonDegP180_nnnByFreqBinAvg plots
            ezGal690yLimMin = 0.95 * velGLonP180.min()
            print(' ezGal690yLimMin =', ezGal690yLimMin)
            # for small antLen, that ezGal690yLimMin may be nan

            ezGal690yLimMax = 1.05 * velGLonP180.max()
            print(' ezGal690yLimMax =', ezGal690yLimMax)
            # for small antLen, that ezGal690yLimMax may be nan

        for gLonP180 in range(361):                 # for every column, RtoL
            if velGLonP180Count[gLonP180]:      # if column used

                # create pltNameS with form of 'ezGal690gLonDegP180_nnnByFreqBinAvg.png'
                pltNameS = f'ezGal690gLonDegP180_{gLonP180:03d}ByFreqBinAvg.png'
                print()
                print('    ' + str(plotCountdown) + ' plotting ' + pltNameS + ' ============')
                print(' gLonP180 =', gLonP180)
                print(' gLonP180 - 180 =', gLonP180 - 180)
                print(' velGLonP180Count[gLonP180] =', velGLonP180Count[gLonP180])
                plotCountdown -= 1
                plt.clf()

                # velGLonP180 stores increasing velocity, but X axis is increasing freq, so use -byFreqBinX
                plt.plot(-byFreqBinX, velGLonP180[:, gLonP180])

                plt.title(titleS)
                plt.grid(ezGalDispGrid)

                plt.xlabel('Doppler (MHz)')
                plt.xlim(-dopplerSpanD2, dopplerSpanD2)

                if 0:
                    # new ylim for each ezGal690gLonDegP180_nnnByFreqBinAvg plot
                    ezGal690yLimMin = 0.95 * velGLonP180[:, gLonP180].min()
                    print(' ezGal690yLimMin =', ezGal690yLimMin)
                    # for small antLen, that ezGal690yLimMin may be nan

                    ezGal690yLimMax = 1.05 * velGLonP180[:, gLonP180].max()
                    print(' ezGal690yLimMax =', ezGal690yLimMax)
                    # for small antLen, that ezGal690yLimMax may be nan

                if not np.isnan(ezGal690yLimMin):
                    if not np.isnan(ezGal690yLimMax):
                        plt.ylim(ezGal690yLimMin, ezGal690yLimMax)

                # create gLonDegS with form of '+nnn' or '-nnn' degrees
                if gLonP180 < 180:
                    gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
                else:
                    gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros

                plt.ylabel('Average AntCBTB Spectrum for Galaxy plane at' \
                    + f'\n\nGalactic Longitude = {gLonDegS} degrees', \
                    rotation=90, verticalalignment='bottom')

                if os.path.exists(pltNameS): # to force plot file date update, if file exists, delete it
                    os.remove(pltNameS)
                plt.savefig(pltNameS, dpi=300, bbox_inches='tight')



def printGoodbye(startTime):

    global programRevision          # string
    global commandString            # string

    # print status
    if 0:
        print()
        print('   ezRAObsName      =', ezRAObsName)
        if 0:
            print('   ezGalUseSamplesRawL      =', ezGalUseSamplesRawL)
            print('   ezGalAddAzDeg            =', ezGalAddAzDeg)
            print('   ezGalAddElDeg            =', ezGalAddElDeg)

            print('   ezGalHideFreqBinL        =', ezGalHideFreqBinL)
            print('   ezGalRfiLim              =', ezGalRfiLim)
            print('   ezGalUseSamplesAntL      =', ezGalUseSamplesAntL)
            print('   ezGalDispGrid            =', ezGalDispGrid)
            print('   ezGalDispFreqBin         =', ezGalDispFreqBin)
            #print('   ezGalDetectLevel         =', ezGalDetectLevel)
        print('   rawLen =', rawLen)
        print('   antLen =', antLen)
        print('   rawLen / antLen =', rawLen / antLen)
        print('   antLen / rawLen =', antLen / rawLen)

    stopTime = time.time()
    stopTimeS = time.ctime()
    print()
    print(' That Python command')
    print('  ', commandString)
    print(' took %d seconds = %1.1F minutes' % ((int(stopTime-startTime)),
        (float(int(stopTime-startTime))/60.))) # xxxxxx.x minutes
    print(' Now = %s' % stopTimeS[:-5])

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



def main():

    #global programRevision          # string
    #global commandString            # string
    #global cmdDirectoryS            # string

    #global fileFreqMin              # float
    #global fileFreqMax              # float
    #global fileFreqBinQty           # integer

    #global fileNameLast             # string
    ##global fileWriteName            # string
    #global fileWrite                # file handle

    #global freqCenter               # float
    #global freqStep                 # float
    #global dopplerSpanD2            # float
    #global titleS                   # string
    #global plotCountdown            # integer
    #global ezGalDispGrid            # integer

    #global ezGalPlotRangeL          # integer list


    startTime = time.time()

    printHello()
    
    ezGalArguments()

    readDataDir()   # creates fileFreqMin, fileFreqMax, fileFreqBinQty, 
                    #   velGLonP180, velGLonP180Count, galDecP90GLonP180Count,
                    #   galDecP90GLonP180Count, fileNameLast

    plotPrep()                       # creates freqStep, dopplerSpanD2, freqCenter,
                                        #   titleS, byFreqBinX

    # velocity plots
    plotEzGal510velGLon()
    plotEzGal511velGLonCount()          # creates ezGal511velGLonCount.txt

    plotEzGal520velGLonPolar()
    plotEzGal521velGLonPolarCount()

    plotEzGal530galDecGLon()

    plotEzGal540velGLonEdgesB()
    plotEzGal541velGLonEdges()
    #plotEzGal550galRot()                # merged with previous plotEzGal541velGLonEdges()

    plotEzGal690gLonDegP180_nnnByFreqBinAvg()

    printGoodbye(startTime)



if __name__== '__main__':
  main()

