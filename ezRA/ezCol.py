programName = 'ezCol230305a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezCol Data COLlector program,
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

# Modified from Victor Boesen's https://github.com/byggemandboesen/H-line-software

# Thanks to Todd Ullery, this ezColX.py was an experimental multiple process version of ezCol.py ,
# to improve graphic dashboard responsiveness.
# Problems ?  Dashboard more responsive ?  Faster ?
# 221202, works on Win7Pro 'Python 3.8.10'
# 221130, works on Ubuntu22 'Python 3.10.6'

# ezCol230305a.py, boilerplate from ezSky
# ezCol230301a.py, -ezez help wording
# ezCol230228a.py, ezCol230208a.py did programStateQueue.put() and ezColIntegQtyQueue.put() way too often
# ezCol230208a.py, REF should be defined in data collection process,
#   moved REF and relay control into sdrTask, ezColIntegQtyQueue
# ezCol230207c.py, marked REF one sample too early, so write with dataFlagsSLast - worked but first REF is second sample, want as first
# ezCol230207b.py, marked REF one sample too early, so write with dataFlagsSLast
# ezCol230207a.py, marked REF one sample too early, ignore first sample - but no effect
# ezCol230206a.py, name change, seems successful, so I now retire experimental ezColX name.
#   Last single-process version was ezCol221110a.py .
#   Now latest ezColX230205c becomes non-experimental ezCol230206a and ezCol.
# ezColX230205c.py, SampleQty and flags show sample currently being created, had serialsend.exe commands reversed
# ezColX230205b.py, cont.
# ezColX230205a.py, name change
# ezColXP230204a.py, more defining detail to -ezColUsbRelay 1 2 and 3,
# ezColXP230203a.py, Pablo code confused by space in dir name, want hidusb-relay-cmd.exe and serialSend.exe found in ezColX directory,
# ezColXP221220a.py, Pablo USB Relay control serialSend.exe experiment
# ezColXP221219a.py, Pablo USB Relay control serialSend.exe experiment
# ezColX221202a.py, renamed for GitHub
# ezCol221110atbb.py, ezColIntegQty needed by sdrTask(), reordered sdrTask() arguments,
#   small fixes, program overview
# ezCol221110atba.py, https://www.youtube.com/watch?v=AZnGRKFUU0c at 0:36
#   says Python multithreading is still one process,
#   so, changed 2 threads to 2 processes, rearranged blocks
# ezCol221110atb.py, second threaded ezCol
# ezCol221110a.py, changed Linux from double SPDT "BITFT" USB Relay to single SPDT "HW348" USB Relay
# ezCol220930a.py, prep for Git
# ezCol220826a.py, dataFlagsS if no REF


#########################################################################################
# ezCol program overview:

# I think this ezCol line to read the SDR hardware is what slows the program:
#    psd = np.abs(np.fft.fft(sdr.read_samples(freqBinQty)))
# I think this command on that line is what slows the program:
#    sdr.read_samples(freqBinQty)
# That leaves too little time to update and read the dashboard graphics window.

# After initialization, that is why 2 processes: main process loop, and sdrTask process loop.
# ezCol program assumes sdrTask process loop takes more time than main process loop.

# main process:
#    initialize: help screen, read in arguments
#    programState = 0 (0: Collect, 1: Pause, 2: Exit)
#    if ezColDashboard:
#        initialize dashboard (including buttons and programState)
#    create new 'data' directory, unless already exists
#    initialize and start the SDR Process 'sdrTask'
#    initialize while loop
#    while programState <= 1: (0: Collect, 1: Pause, 2: Exit)
#        get sdrOutQueue
#        if sdrOutQueue had New Data:
#            initialize timestamp
#            set centerFreq
#            maybe start new data file (if new UTC day, or if newFileButton)
#            maybe write an az line (if az or el changed)
#            write data sample line
#            if ezColVerbose:
#                print status
#            if ezColDashboard:
#                erase dashboard
#                plot top right text section
#                plot 3 stripcharts
#                plot top left frequency spectrum
#            remember timestamp
#        allow time for dashboard interaction

# sdrTask process:
#    initialize feedRef relay, if any
#    while programState <= 1: (0: Collect, 1: Pause, 2: Exit)
#        get the programStateQueue
#        if programState == 2:
#            exit
#        if programState == 0 (not Paused):
#            set feedRef relay
#            set the center frequency
#            create and put tuple with Power Spectral Density (PSD), values averaged
#              from ezColIntegQty datasets
#########################################################################################

#import operator
import os
#from pickle import FALSE
import sys
import time

#import threading
#import queue
# delayed other imports until after possible help screen



def printHello():

    global programRevision          # string
    global commandString            # string

    print()
    print('         For help, run')
    print('            ezCol.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezCol.py [optional arguments]')
    print('  Linux:     python3 ezCol.py [optional arguments]')
    print()
    print('  Easy Radio Astronomy (ezRA) ezCol data Collector')
    print('  to record radio to "data" directory frequency spectrum data ezRA .txt files.')
    print('  ezCol will create a "data" directory if necessary.')
    print()
    print('  Arguments are read first from inside the ezCol program,')
    print("  then in order from the ezDefaults.txt file in the ezCol.py's directory,")
    print('  then in order from the ezDefaults.txt file in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  py ezCol.py -help                         (Print this help)')
    print('  py ezCol.py -h                            (Print this help)')
    print()
    print('  py ezCol.py -ezRAObsLat    40.2           (Observatory Latitude  (degrees))')
    print('  py ezCol.py -ezRAObsLon  -105.1           (Observatory Longitude (degrees))')
    print('  py ezCol.py -ezRAObsAmsl 1524.0           (Observatory Above Mean Sea Level (meters))')
    print('  py ezCol.py -ezRAObsName bigDish8         (Observatory Name)')
    print('  py ezCol.py -ezColFileNamePrefix bigDish8 (Data File Name Prefix)')
    print()
    print('  py ezCol.py -ezColCenterFreqAnt 1420.405  (Signal          Frequency (MHz))')
    print('  py ezCol.py -ezColCenterFreqRef 1423.405  (Dicke Reference Frequency (MHz))')
    print('  py ezCol.py -ezColBandWidth        2.400  (Signal          Bandwidth (MHz))')
    print()
    print('  py ezCol.py -ezColFreqBinQtyBits   8      (For  256 freqBinQty frequencies)')
    print('  py ezCol.py -ezColFreqBinQtyBits  10      (For 1024 freqBinQty frequencies)')
    print()
    print('  py ezCol.py -ezColGain        9999        (Use max gain)')
    print('  py ezCol.py -ezColOffsetPPM   5           (Tuner offset Parts-Per-Million (integer)')
    print('  py ezCol.py -ezColAntBtwnRef  5           (number of Ant samples between Ref samples)')
    print()
    print('  py ezCol.py -ezColAzimuth   180.0         (Azimuth   pointing of antenna (degrees))')
    print('  py ezCol.py -ezColElevation  45.0         (Elevation pointing of antenna (degrees))')
    print()
    print('  py ezCol.py -ezColVerbose     1           (Turn on Verbose mode)')
    print('  py ezCol.py -ezColDashboard   0           (Turn off graphical display)')
    print('  py ezCol.py -ezColDispGrid    1           (Turn on graphical display plot grids)')
    print()
    print('  py ezCol.py -ezColUsbRelay   0            (No relays driving a feed Dicke reference)')
    print('  py ezCol.py -ezColUsbRelay   1            (1 SPST HID relay, driving feedRef ON or OFF)')
    print('  py ezCol.py -ezColUsbRelay   2            (2 SPST HID relays, driving a latching feedRef',
        ' relay with pulses)')
    print('  py ezCol.py -ezColUsbRelay   3            (1 SPST non-HID relay, driving feedRef ON or OFF)')
    print()
    #print('  py ezCol.py -ezColSlowness   0.9          (Define "Slow" data collect, to allow faster',
    #    'Dashboard interaction)')
    print('  py ezCol.py -ezColIntegQty   31000        (Number of readings to be integrated into',
        'one sample)')
    print('  py ezCol.py -ezColTextFontSize   11       (Size of text font)')
    print('  py ezCol.py -ezColYLimL      0.1  0.4     (Fraction of Y Auto Scale, Min and Max)')
    print()
    print('  py ezCol.py -ezDefaultsFile ..\\bigDish8.txt   (Additional file of default arguments)')
    print()
    print('              -ezezIgonoreThisWholeOneWord')
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



def ezColArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezColFileNamePrefix              # string

    global ezColCenterFreqAnt               # float
    global ezColCenterFreqRef               # float
    global ezColBandWidth                   # float

    global ezColFreqBinQtyBits              # integer
    global ezColGain                        # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global ezColUsbRelay                    # integer

    #global ezColSlowness                    # float
    global ezColIntegQty                    # integer
    global ezColTextFontSize                # integer
    global ezColYLim0                       # float
    global ezColYLim1                       # float


    print()
    print('   ezColArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileDefaults = open(ezDefaultsFileNameInput, 'r')

        print('      success opening ' + ezDefaultsFileNameInput)

        while 1:
            fileLine = fileDefaults.readline()

            # LF always present: 0=EOF  1=LF  2=1Character
            if len(fileLine) < 1:         # if end of file
                break                     # get out of while loop

            thisLineSplit = fileLine.split()
            if len(thisLineSplit) < 1:         # if line all whitespace
                continue                  # skip to next line

            if thisLineSplit[0][0] == '#':    # ignoring whitespace, if first character of first word
                continue                  # it is a comment, skip to next line


            # be kind, ignore argument keyword capitalization
            thisLine0Lower = thisLineSplit[0].lower()

            # ezRA family arguments
            if thisLine0Lower == '-ezRAObsName'.lower():
                ezRAObsName = thisLineSplit[1]

            elif thisLine0Lower == '-ezRAObsLat'.lower():
                ezRAObsLat  = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezRAObsLon'.lower():
                ezRAObsLon  = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezRAObsAmsl'.lower():
                ezRAObsAmsl = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColFileNamePrefix'.lower():
                ezColFileNamePrefix = thisLineSplit[1]


            # ezCol arguments
            # integer arguments
            elif thisLine0Lower == '-ezColFreqBinQtyBits'.lower():
                ezColFreqBinQtyBits = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColGain'.lower():
                ezColGain = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColVerbose'.lower():
                ezColVerbose = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColDashboard'.lower():
                ezColDashboard = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColDispGrid'.lower():
                ezColDispGrid = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColUsbRelay'.lower():
                ezColUsbRelay = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColIntegQty'.lower():
                ezColIntegQty = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColTextFontSize'.lower():
                ezColTextFontSize = int(thisLineSplit[1])

            # float arguments
            elif thisLine0Lower == '-ezColCenterFreqAnt'.lower():
                ezColCenterFreqAnt = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColCenterFreqRef'.lower():
                ezColCenterFreqRef = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColBandWidth'.lower():
                ezColBandWidth = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColAzimuth'.lower():
                ezColAzimuth = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColElevation'.lower():
                ezColElevation = float(thisLineSplit[1])

            #elif thisLine0Lower == '-ezColSlowness'.lower():
            #    ezColSlowness = float(thisLineSplit[1])


            # list arguments
            elif thisLine0Lower == '-ezColYLimL'.lower():
                ezColYLim0 = float(thisLineSplit[1])
                ezColYLim1 = float(thisLineSplit[2])

            elif thisLine0Lower[:6] == '-ezCol'.lower():
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
        fileDefaults.close()       #   then have processed all available lines in this defaults file



def ezColArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezColFileNamePrefix              # string

    global ezColCenterFreqAnt               # float
    global ezColCenterFreqRef               # float
    global ezColBandWidth                   # float

    global ezColFreqBinQtyBits              # integer
    global ezColGain                        # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global cmdDirectoryS                    # string            creation

    global ezColUsbRelay                    # integer

    #global ezColSlowness                    # float
    global ezColIntegQty                    # integer
    global ezColTextFontSize                # integer
    global ezColYLim0                       # float
    global ezColYLim1                       # float


    print()
    print('   ezColArgumentsCommandLine ===============')

    cmdLineSplit = commandString.split()
    cmdLineSplitLen = len(cmdLineSplit)

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

            elif cmdLineArgLower == '-ezColFileNamePrefix'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColFileNamePrefix = cmdLineSplit[cmdLineSplitIndex]


            # integer arguments:
            elif cmdLineArgLower == '-ezColFreqBinQtyBits'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColFreqBinQtyBits = int(cmdLineSplit[cmdLineSplitIndex])

            #elif cmdLineArgLower == '-ezColOffsetPPM'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
            #    ezColOffsetPPM = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColGain'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColGain = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColAntBtwnRef'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColAntBtwnRef = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColVerbose'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColVerbose = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColDashboard'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColDashboard = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColDispGrid'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColDispGrid = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColUsbRelay'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColUsbRelay = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColIntegQty'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColIntegQty = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColTextFontSize'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColTextFontSize = int(cmdLineSplit[cmdLineSplitIndex])

            # float arguments:
            elif cmdLineArgLower == '-ezColCenterFreqAnt'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColCenterFreqAnt = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColCenterFreqRef'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColCenterFreqRef = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColBandWidth'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColBandWidth = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColAzimuth'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColAzimuth = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColElevation'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColElevation = float(cmdLineSplit[cmdLineSplitIndex])

            #elif cmdLineArgLower == '-ezColSlowness'.lower():
            #    cmdLineSplitIndex += 1      # point to first argument value
            #    ezColSlowness = float(cmdLineSplit[cmdLineSplitIndex])


            # list arguments:
            elif cmdLineArgLower == '-ezColYLimL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColYLim0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezColYLim1 = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            # ignore silly -ezez* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            elif 4 <= len(cmdLineArgLower) and cmdLineArgLower[:5] == '-ezez':
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

        cmdLineSplitIndex += 1



def ezColArguments():
    # argument: "(Computing) a value or address passed to a procedure or function at the time of call"

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezColFileNamePrefix              # string

    global ezColCenterFreqAnt               # float
    global ezColCenterFreqRef               # float
    global ezColBandWidth                   # float

    global ezColFreqBinQtyBits              # integer
    global ezColGain                        # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global ezColUsbRelay                    # integer

    #global ezColSlowness                    # float         creation
    global ezColIntegQty                    # integer       creation
    global ezColTextFontSize                # integer       creation

    global ezColYLim0                       # float         creation
    global ezColYLim1                       # float         creation


    # defaults
    if 1:
        ezRAObsName = 'defaultKS'           # Geographic Center of USA, near Lebanon, Kansas
        ezRAObsLat  =  39.8282              # Observatory Latitude  (degrees)
        ezRAObsLon  = -98.5696              # Observatory Longitude (degrees)
        ezRAObsAmsl = 563.88                # Observatory Above Mean Sea Level (meters)
        ezColFileNamePrefix = ''

        ezColCenterFreqAnt = 1420.405       # Center Frequency for Antenna signal measurements

        ezColCenterFreqRef = 0              # silly value for Center Frequency for Reference signal measurements

        # Available bandwidths
        #   3200000Hz = 3.2   MHz
        #   2800000Hz = 2.8   MHz
        #   2560000Hz = 2.56  MHz
        #   2400000Hz = 2.4   MHz = default
        #   2048000Hz = 2.048 MHz
        #   1920000Hz = 1.92  MHz
        #   1800000Hz = 1.8   MHz
        #   1400000Hz = 1.4   MHz
        #   1024000Hz = 1.024 MHz
        #    900001Hz = 0.9   MHz
        #    250000Hz = 0.25  MHz
        ezColBandWidth = 2.400              # bandwidth (tuner sample rate) (MHz)

        # Each recorded sample has ezColFreqBinQty Frequency Bin values.
        ezColFreqBinQtyBits  =  8   # means freqBinQty will be 2 to the power of  8 = 2 **  8 =  256
        #ezColFreqBinQtyBits = 10   # means freqBinQty will be 2 to the power of 10 = 2 ** 10 = 1024

        ezColGain = 9999            # silly big number which RtlSdr library will reduce

        ezColAntBtwnRef = 1         # number of Ant samples between REF samples

        ezColAzimuth   = 180.0      # Azimuth   pointing of antenna (degrees)
        ezColElevation =  45.0      # Elevation pointing of antenna (degrees)

        ezColVerbose   = 0
        ezColDashboard = 1
        ezColDispGrid  = 0

        ezColUsbRelay = 0           # no relays driving a feedRef
        #ezColUsbRelay = 1           # 1 SPST HID relay, driving feedRef ON or OFF
        #ezColUsbRelay = 2           # 2 SPST HID relays, driving a latching feedRef relay with pulses
        #ezColUsbRelay = 3           # 1 SPST non-HID relay, driving feedRef ON or OFF

        #ezColSlowness = 0.9         # data collecting pause to allow dashboard interaction
        ezColIntegQty = 31000       # number of samples to be integrated into one recorded sample
        ezColTextFontSize = 10
        ezColYLim0    = 0.0         # fraction of Y Auto Scale, Minimum
        ezColYLim1    = 1.0         # fraction of Y Auto Scale, Maximum

    # Program argument priority:
    #    Start with the argument value defaults inside the programs.
    #    Then replace those values with any arguments from the ezDefaults.txt in the program's directory.
    #    Then replace values with any arguments from the ezDefaults.txt in the current
    #       directory (where you are standing).
    #    Then replace values (in order) with any arguments from the command line (including
    #       any -ezDefaultsFile).
    #    Each last defined value wins.

    # process arguments from ezDefaults.txt file in the same directory as this ezCol program
    ezColArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezColArgumentsFile('ezDefaults.txt')

    # process arguments from command line
    ezColArgumentsCommandLine()

    # print status
    print()
    print('   ezRAObsName =', ezRAObsName)
    print('   ezRAObsLat  =', ezRAObsLat)
    print('   ezRAObsLon  =', ezRAObsLon)
    print('   ezRAObsAmsl =', ezRAObsAmsl)
    print('   ezColFileNamePrefix =', ezColFileNamePrefix)
    print()
    print('   ezColCenterFreqRef  =', ezColCenterFreqRef)
    print('   ezColCenterFreqAnt  =', ezColCenterFreqAnt)
    print('   ezColBandWidth      =', ezColBandWidth)
    print()
    print('   ezColFreqBinQtyBits =', ezColFreqBinQtyBits)
    print('   ezColGain           =', ezColGain)
    print('   ezColAntBtwnRef     =', ezColAntBtwnRef)
    print()
    print('   ezColAzimuth   =', ezColAzimuth)
    print('   ezColElevation =', ezColElevation)
    print()
    print('   ezColVerbose   =', ezColVerbose)
    print('   ezColDashboard =', ezColDashboard)
    print('   ezColDispGrid  =', ezColDispGrid)
    print()
    print('   ezColUsbRelay =', ezColUsbRelay)
    #print('   ezColSlowness =', ezColSlowness)
    print('   ezColIntegQty =', ezColIntegQty)
    print('   ezColTextFontSize =', ezColTextFontSize)
    print('   ezColYLimL    = [', ezColYLim0, ',', ezColYLim1, ']')

    # fix silly arguments
    if not ezColFileNamePrefix:
        ezColFileNamePrefix = ezRAObsName.split()[0]    # first word of ezRAObsName
    if not ezColCenterFreqRef and ezColUsbRelay:
        ezColCenterFreqRef = ezColCenterFreqAnt



#########################################################################################################
def main():

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string
    global ezColFileNamePrefix              # string

    global ezColCenterFreqAnt               # float
    global ezColCenterFreqRef               # float
    global ezColBandWidth                   # float

    global ezColFreqBinQtyBits              # integer
    global ezColGain                        # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzimuth                     # float
    global ezColElevation                   # float

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global dateDayLastS                     # string
    global rmsAvgHistory                    # float array
    global rmsAvgHistoryLen                 # integer
    global programState                     # integer
    global refAction                        # integer
    #global ezColSlowness                    # float
    global ezColIntegQty                    # integer
    global ezColYLim0                       # float
    global ezColYLim1                       # float
    global ezColTextFontSize                # integer

    printHello()

    ezColArguments()


    # delayed these imports until after possible help screen
    #from time import sleep
    from datetime import date, datetime, timezone
    import numpy as np
    import operator
    from multiprocessing import Process, Queue
    #from math import sqrt
    import matplotlib
    #matplotlib.use('agg')
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Button, RadioButtons, TextBox




    freqBinQty = 2 ** ezColFreqBinQtyBits

    rmsAvgHistoryLen = 9999                                 # max length of history, best if just over 24 hours
    # rmsAvgHistory[0] is most recent, and np.nan values will not plot
    rmsAvgHistory = np.full(rmsAvgHistoryLen, np.nan)
    rmsAvgHistoryLenRecentHour = 1500                       # best if just over 60 minutes (100 * 60 / 40 = 150)
    rmsAvgHistoryLenRecentMost = 510

    print()
    # https://docs.python.org/3/library/datetime.html
    # ... the recommended way to create an object representing the current time in UTC is
    #   by calling datetime.now(timezone.utc)
    timeStampUtcZero = datetime.now(timezone.utc)           # relative time zero
    print(' timeStampUtcZero =', timeStampUtcZero)
    print()
    timeStampUtcZeroHours = timeStampUtcZero.hour + timeStampUtcZero.minute / 60. \
        + timeStampUtcZero.second / 3600.

    # http://www.astro.sunysb.edu/metchev/AST443/times.html
    # Julian date on January 1.5, 2000 was 2,451,545.0. This is defined as J2000.0
    # MJD = JD - 2,400,000.5
    # JD = MJD + 2,400,000.5
    # https://en.wikipedia.org/wiki/Julian_day
    # MJD has a starting point of midnight on November 17, 1858
    timeStampUtcZeroMjdTimedelta = timeStampUtcZero - datetime(1858, 11, 17, tzinfo=timezone.utc)
    timeStampUtcZeroMjd = timeStampUtcZeroMjdTimedelta.total_seconds() / 60. / 60. / 24.

    # prepare to calculate Local Mean Sidereal Time (LMST) Hours
    # http://www.setileague.org/askdr/lmst.htm
    # Local Mean Sidereal Time (LMST) Hours = south's Right Ascension
    # Local Mean Sidereal Time = LMST = gmstHour + timeStampUtcZeroHours + geodeticLongitude
    # TU = (JD                - 2451545.0) / 36525 is the number of Julian Centuries since J2000.0
    # TU = (MJD + 2,400,000.5 - 2451545.0) / 36525 is the number of Julian Centuries since J2000.0
    # calculated later with each file opening:
    ### tU = (timeStampUtcZeroMjd + (timeStampUtcHourRelThis / 24.) + 2400000.5 - 2451545.0) / 36525.

    # gmstSec (Greenwich Mean Sidereal Time) at 0h UT
    #    = 24110.54841 + 8640184.812866 TU + 0.093104 TU ^ 2 - 6.2x10-6 TU ^ 3
    # calculated later with each file opening:
    ###gmst0UTCSec = 24110.54841 + (8640184.812866 * tU) + (0.093104 * tU * tU) - (6.2e-6 * tU * tU * tU)
    ###gmst0UTCHour = gmst0UTCSec / 60 / 60

    geodeticLongitude = ezRAObsLon / 15.

    # calculated later with each file opening:
    ###lmstZero = gmst0UTCHour + timeStampUtcZeroHours + geodeticLongitude


    # relative history of timeStampUtc in hours
    # timeStampUtcHourRelHistory[0] is most recent, on the right edge of stripcharts
    timeStampUtcHourRelHistory = np.zeros(rmsAvgHistoryLen)


    freqMinAnt = (ezColCenterFreqAnt - (ezColBandWidth / 2.))   # in MHz
    freqMaxAnt = freqMinAnt + ezColBandWidth                    # in MHz

    centerFreqAntHz = int(ezColCenterFreqAnt * 1e6)             # in integer Hz
    bandWidthHz = ezColBandWidth * 1e6                          # in float Hz

    programState = 0                # 0: Collect, 1: Pause, 2: Exit, in case no ezColDashboard

    # initialize dashboard
    if ezColDashboard:
        fig = plt.figure(figsize=(20, 12))
        fig.suptitle('ezRA - Easy Radio Astronomy Data Collector - ' + programName, fontsize = 22, y = 0.99)
        grid = fig.add_gridspec(4, 2, hspace=1.0)
        details_ax    = fig.add_subplot(grid[0  , 1])
        powerTime_ax1 = fig.add_subplot(grid[1  , 1])     # Recent  n number of samples
        powerTime_ax2 = fig.add_subplot(grid[2  , 1])     # Recent  1 hour   of samples
        powerTime_ax3 = fig.add_subplot(grid[3  , :])     # Recent 24 hours  of samples
        spectrum_ax   = fig.add_subplot(grid[0:3, 0])
        plt.subplots_adjust(left = 0.07, bottom = 0.08, right = 0.97, top = 0.90, wspace = 0.18, hspace = 0.36)

        powerTime_ax2XB = powerTime_ax2.twiny()  # instantiate a second axes that shares the same y-axis
        powerTime_ax3XB = powerTime_ax3.twiny()  # instantiate a second axes that shares the same y-axis
        spectrum_axXB = spectrum_ax.twiny()  # instantiate a second axes that shares the same y-axis
        spectrum_axXB.set_xlabel('Doppler (MHz)')
        spectrum_axYB = spectrum_ax.twinx()  # instantiate a second axes that shares the same x-axis
        spectrum_axYB.set_ylabel('Fraction of Y Auto Scale')
        spectrum_ax.autoscale(enable = True, axis = 'y')

        centerFreqRefHz = int(ezColCenterFreqRef * 1e6)         # in integer Hz

        bandWidthD2 = ezColBandWidth / 2.                       # ezColBandWidth Divided by 2, in MHz

        freqMinRef = (ezColCenterFreqRef - bandWidthD2)         # in MHz
        freqMaxRef = freqMinRef + ezColBandWidth                # in MHz

        freqsAnt = np.linspace(start=freqMinAnt, stop=freqMaxAnt, num=freqBinQty)
        freqsRef = np.linspace(start=freqMinRef, stop=freqMaxRef, num=freqBinQty)

        # dashboard 'NewPlot' button, to clear stripchart plots
        def newPlot(event):
            global rmsAvgHistory
            global rmsAvgHistoryLen
            rmsAvgHistory = np.full(rmsAvgHistoryLen, np.nan)   # clear plot history
        axNewPlot = plt.axes([0.865, 0.95, 0.05, 0.04])
        bNewPlot = Button(axNewPlot, 'New Plot')
        bNewPlot.on_clicked(newPlot)

        # dashboard 'NewFile' button, to start a new data file
        def newFile(event):
            global dateDayLastS
            global rmsAvgHistory
            global rmsAvgHistoryLen
            rmsAvgHistory = np.full(rmsAvgHistoryLen, np.nan)   # clear plot history
            dateDayLastS = 'newFileButton'                      # silly value to force new data file
        axNewFile = plt.axes([0.92, 0.95, 0.05, 0.04])
        bNewFile = Button(axNewFile, 'New File')
        bNewFile.on_clicked(newFile)

        # dashboard 'programState' radio button, control data collecting priority
        # https://blog.finxter.com/matplotlib-widgets-button/
        def programStateEntry(label):
            global programState                 # integer
            global programStatePutLast          # integer
            #if label == 'Fast':
            if label == 'Collect':
                programState = 0
                programStateQueue.put(programState)
                programStatePutLast = programState
            elif label == 'Pause': 
                programState = 1
                programStateQueue.put(programState)
                programStatePutLast = programState
            else:
                # label == 'Exit'
                #exit()
                programState = 2
                programStateQueue.put(programState)
                programStatePutLast = programState
                #sdrProcess.join()               # needed ????????????????????
                sys.exit(0)

            print(' label =', label,'= ')
            print(' programState =', programState)

        radio2_ax = plt.axes([0.865, 0.85, 0.05, 0.09], facecolor='lightgoldenrodyellow')
        #radio2 = RadioButtons(radio2_ax, ('Fast', 'Slow', 'Pause', 'Exit'))
        radio2 = RadioButtons(radio2_ax, ('Collect', 'Pause', 'Exit'))
        radio2.on_clicked(programStateEntry)
        #programState  = 0               # default Fast
        programState  = 0               # default Collect

        # dashboard 'RefDiv' radio button, spectrum divided by (or subtracting) last REF sample
        def refActionFunction(label):
            global refAction
            if label == 'Off':
                refAction = 0
            elif label == 'RefDiv':
                refAction = 1           # plot last Ant spectrum divided by last REF spectrum
            else:
                # 'RefSub'
                refAction = 2           # plot last Ant spectrum after subtracting last REF spectrum
        radio1_ax = plt.axes([0.92, 0.85, 0.05, 0.09], facecolor='lightgoldenrodyellow')
        radio1 = RadioButtons(radio1_ax, ('Off', 'RefDiv', 'RefSub'))
        radio1.on_clicked(refActionFunction)
        refAction = 0                   # default Off

        ## dashboard 'ezColSlowness' number entry, define slowness when programState = 1
        #def ezColSlownessEntry(ezColSlownessEntryS):
        #    global ezColSlowness                    # float
        #    ezColSlownessEntrySplit = ezColSlownessEntryS.split()
        #    if ezColSlownessEntrySplit:
        #        ezColSlowness = float(ezColSlownessEntrySplit[0])
        #ezColSlownessEntry_ax = fig.add_axes([0.92, 0.80, 0.05, 0.04])
        #ezColSlownessEntryBox = TextBox(ezColSlownessEntry_ax, 'ezColSlowness ')
        #ezColSlownessEntryBox.on_submit(ezColSlownessEntry)
        #ezColSlownessEntryBox.set_val(str(ezColSlowness))  # initialize string of ezColSlownessEntryBox

        # dashboard 'ezColIntegQty' number entry, define number of readings per data sample
        def ezColIntegQtyEntry(ezColIntegQtyEntryS):
            global ezColIntegQty                    # integer
            ezColIntegQtyEntrySplit = ezColIntegQtyEntryS.split()
            if ezColIntegQtyEntrySplit:
                ezColIntegQty = int(ezColIntegQtyEntrySplit[0])
        ezColIntegQtyEntry_ax = fig.add_axes([0.92, 0.75, 0.05, 0.04])
        ezColIntegQtyEntryBox = TextBox(ezColIntegQtyEntry_ax, 'ezColIntegQty ')
        ezColIntegQtyEntryBox.on_submit(ezColIntegQtyEntry)
        ezColIntegQtyEntryBox.set_val(str(ezColIntegQty))   # initialize string of ezColIntegQtyEntryBox

        # dashboard 'ezColAzimuth' number entry, change ezColAzimuth live
        def ezColAzEntry(ezColAzEntryS):
            global ezColAzimuth                     # float
            ezColAzEntrySplit = ezColAzEntryS.split()
            if ezColAzEntrySplit:
                ezColAzimuth   = float(ezColAzEntrySplit[0])
        ezColAzEntry_ax = fig.add_axes([0.56, 0.81, 0.04, 0.04])
        ezColAzEntryBox = TextBox(ezColAzEntry_ax, 'Azimuth ')
        ezColAzEntryBox.on_submit(ezColAzEntry)
        ezColAzEntryBox.set_val(str(ezColAzimuth))          # initialize string of ezColAzEntryBox

        # dashboard 'ezColElEntry' number entry, change ezColElevation live
        def ezColElEntry(ezColElEntryS):
            global ezColElevation                   # float
            ezColElEntrySplit = ezColElEntryS.split()
            if ezColElEntrySplit:
                ezColElevation = float(ezColElEntrySplit[0])
        ezColElEntry_ax = fig.add_axes([0.56, 0.77, 0.04, 0.04])
        ezColElEntryBox = TextBox(ezColElEntry_ax, 'Elevation ')
        ezColElEntryBox.on_submit(ezColElEntry)
        ezColElEntryBox.set_val(str(ezColElevation))        # initialize string of ezColElEntryBox

        # dashboard 'ezColYLimEntry' number pair entry, change displayed spectrum y scale live
        def ezColYLimEntry(ezColYLimEntryS):
            global ezColYLim0                       # float
            global ezColYLim1                       # float
            ezColYLimEntrySplit = ezColYLimEntryS.split()
            if ezColYLimEntrySplit:
                ezColYLim0 = float(ezColYLimEntrySplit[0])
                ezColYLim1 = float(ezColYLimEntrySplit[1])
        ezColYLimEntry_ax = fig.add_axes([0.92, 0.70, 0.05, 0.04])
        ezColYLimEntryBox = TextBox(ezColYLimEntry_ax, 'Fraction of     \nY Auto Scale, \nMin and Max ')
        ezColYLimEntryBox.on_submit(ezColYLimEntry)
        # initialize string of ezColYLimEntryBox
        ezColYLimEntryBox.set_val(str(ezColYLim0) + '   ' + str(ezColYLim1))

        #if os.name == 'nt':     # Windows
        #    # maximize plot window
        #    # https://stackoverflow.com/questions/12439588/how-to-maximize-a-plt-show-window-using-python
        #    mng = plt.get_current_fig_manager()
        #    #mng.window.state('zoomed')



    # if does not exist - create new 'data' directory
    if not os.path.exists('data'):
        os.makedirs('data')
        print(' Created new "data" directory')


    #create the SDR Process
    programStateQueue = Queue()
    programStateQueue.put(programState)
    programStatePutLast = programState

    ezColIntegQtyQueue = Queue()
    ezColIntegQtyQueue.put(ezColIntegQty)
    ezColIntegQtyPutLast = ezColIntegQty

    sdrOutQueue = Queue()               #sdr to main communication

    sdrProcess = Process(target=sdrTask, args=(bandWidthHz, ezColGain, freqBinQty, centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, ezColAntBtwnRef,
        programStateQueue, ezColIntegQtyQueue, sdrOutQueue))
    # sdrTask is started once, with arguments bandWidthHz, ezColGain, freqBinQty, centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, and ezColAntBtwnRef.
    #   It will loop and read the latest inputs from programStateQueue and ezColIntegQtyQueue.
    #   At the end of each loop it will output one tuple through sdrOutQueue.
    #   The tuple includes sdrGain, rmsSpectrum, and dataFlagsS.
    # sdrThread.start()
    sdrProcess.start()


    dateDayLastS = ''         # silly value to force new data file
    fileNameS = ''
    fileSample = 0
    fileNamePostS = 'bcdefghijklmnopqrstuvwxyz'
    timeStampUtcSecRelLast = 0
    rmsSpectrumAntLast = np.ones(freqBinQty)
    rmsSpectrumRefLast = np.ones(freqBinQty)
    lmstLabels1to0to0 = \
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '0',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '0']
    firstDraw = 1           # flag to draw the plot the first time without data
    #mainLoop = 0
    while programState <= 1:
        # update inputs to sdrTask
        if programState != programStatePutLast:
            programStateQueue.put(programState)
            programStatePutLast = programState
        if ezColIntegQty != ezColIntegQtyPutLast:
            ezColIntegQtyQueue.put(ezColIntegQty)
            ezColIntegQtyPutLast = ezColIntegQty

        #get the rmsSpectrum from the queue
        #if firstDraw and programState <= 1:
        hasNewData = 1
        if firstDraw:
            sdrOut = sdrOutQueue.get()
            firstDraw = 0
        else:
            try:
                sdrOut = sdrOutQueue.get_nowait()
            except:
                hasNewData = 0
                #plt.pause(0.5)       # waiting for sdrOutQueue anyway

        if hasNewData:
            (sdrGain, rmsSpectrum, dataFlagsS) = sdrOut
            feedRef = 'R' in dataFlagsS

            timeStampUtc  = datetime.now(timezone.utc)      # this sample's timestamp
            timeStampUtcS = timeStampUtc.strftime('%Y-%m-%dT%H:%M:%S ')
            # https://stackoverflow.com/questions/44823073/convert-datetime-time-to-seconds
            # datetime.time objects are meant to represent a time of the day.
            # datetime.timedelta objects are meant to represent a duration, and they have a total_seconds() method
            timeStampUtcSecRelThis = (timeStampUtc - timeStampUtcZero).total_seconds()
            timeStampUtcHourRelThis = timeStampUtcSecRelThis / 3600.

            # timeStampUtcS = '2022-12-22T21:19:49 '
            #                  01234567890123456789
            dateDayThisS = timeStampUtcS[8:10]
            if dateDayLastS != dateDayThisS:
                # start new data file, because of new UTC day, or newFileButton
                # if old data file open, close it
                if len(fileNameS):
                    fileWrite.close()

                # try to not write over existing data files,
                # assumes 'data' directory exists
                # fileNameHourS = 'YYMMDD_HH'
                #                  0123456789
                fileNameHourS = timeStampUtcS[2:4] + timeStampUtcS[5:7] + dateDayThisS + '_' \
                    + timeStampUtcS[11:13]
                fileNameMidS = 'data' + os.path.sep + ezColFileNamePrefix + fileNameHourS
                # first try with no trailing character
                fileNameS = fileNameMidS + '.txt'
                if not os.path.exists(fileNameS):       # if fileNameS is available
                    fileNameDashS = ezColFileNamePrefix + fileNameHourS + '.txt'  # for dashboard
                else:
                    # try with one trailing character
                    for i in range(25):
                        fileNameS = fileNameMidS + fileNamePostS[i] + '.txt'
                        if not os.path.exists(fileNameS):       # if fileNameS is available
                            # for dashboard
                            fileNameDashS = ezColFileNamePrefix + fileNameHourS + fileNamePostS[i] + '.txt'
                            break           # get out of FOR loop
                        fileNameS = ''      # to flag no available filenames
                    if not fileNameS:
                        # no available filenames
                        print()
                        print('ERROR: already too many files with same fileName base on this UTC date')
                        print()
                        programState = 2
                        programStateQueue.put(programState)
                        programStatePutLast = programState
                        #sdrProcess.join()               # needed ????????????????????
                        exit()

                print()
                print('Starting new output file:', fileNameS, '===============')

                # with each new file, update lmstZero (changes about 4 minutes each 24 hours).
                # As described above, calculate Local Mean Sidereal Time (LMST) Hours
                tU = (timeStampUtcZeroMjd + (timeStampUtcHourRelThis / 24.) + 2400000.5 - 2451545.0) \
                    / 36525.
                gmst0UTCSec = 24110.54841 + 8640184.812866 * tU + 0.093104 * tU * tU \
                    - 6.2e-6 * tU * tU * tU
                gmst0UTCHour = gmst0UTCSec / 3600.
                lmstZero = gmst0UTCHour + timeStampUtcZeroHours + geodeticLongitude
                print('lmstZero % 24 =', lmstZero % 24.)

                # open() with 1 to write to file after every '\n'
                fileWrite = open(fileNameS, 'w', 1)
                fileWrite.write('from ' + programRevision + '\n' \
                    + f'lat {ezRAObsLat:g} ' \
                    + f'long {ezRAObsLon:g} ' \
                    + 'amsl ' + str(ezRAObsAmsl) \
                    + ' name ' + ezRAObsName + '\n' \
                    + f'freqMin {freqMinAnt:g} ' \
                    + f'freqMax {freqMaxAnt:g} ' \
                    + 'freqBinQty ' + str(freqBinQty) + '\n' \
                    + f'az {ezColAzimuth:g} ' \
                    + f'el {ezColElevation:g}' \
                    + '\n# times are in UTC\n')
                fileWrite.write('# gain ' + str(sdrGain) + '\n')
                fileWrite.write('# frequency spectrums of RMS power = sqrt(mean of sum of squares)\n')

                # initialize ezColAzimuthLast and ezColElevationLast
                ezColAzimuthLast = ezColAzimuth
                ezColElevationLast = ezColElevation

                dateDayLastS = dateDayThisS
                fileSample = 0

            # not new file, if az or el changed, write an az line
            elif ezColAzimuthLast != ezColAzimuth or ezColElevationLast != ezColElevation:
                ezColAzimuthLast   = ezColAzimuth
                ezColElevationLast = ezColElevation
                fileWrite.write(f'az {ezColAzimuth:g} el {ezColElevation:g}\n')

            # now feedRef, timeStampUtcS, fileNameS, and fileSample are updated
            fileSample += 1

            # timeStampUtcS = '2022-12-22T21:19:49 '
            #                  01234567890123456789
            timeUtcDateS = timeStampUtcS[:10]
            timeUtcTimeS = timeStampUtcS[11:19]
            # https://stackoverflow.com/questions/4563272/how-to-convert-a-utc-datetime-to-a-local-datetime-using-only-standard-library
            timePcS = timeStampUtc.astimezone(tz=None).strftime('%Y-%m-%dT%H:%M:%S ')
            timePcDateS = timePcS[:10]
            timePcTimeS = timePcS[11:19]

            print()
            currentCenterFreq = ezColCenterFreqRef if feedRef else ezColCenterFreqAnt
            print(timeStampUtcS, 'UTC    ', fileNameS, '   ', fileSample, '  ', currentCenterFreq, 'Hz  ', dataFlagsS)
            print('Receiving', ezColIntegQty, 'readings, each with', freqBinQty, 'frequencies ...')

            # write data sample line
            fileWrite.write(timeStampUtcS + ' '.join(f'{i:.9g}' for i in rmsSpectrum) + dataFlagsS + '\n')

            # this sample's Local Mean Sidereal Time (LMST) in hours, value at dashboard stripcharts' right edge
            lmstThis = (lmstZero + timeStampUtcHourRelThis) % 24.

            if ezColVerbose:
                print(ezRAObsName)
                print(f'  Latitude    {ezRAObsLat:0.1f}')
                print(f'  Longitude   {ezRAObsLon:0.1f}')
                print(f'  Amsl        {ezRAObsAmsl:0.0f}')
                print(f'  Azimuth     {ezColAzimuth:0.1f}')
                print(f'  Elevation   {ezColElevation:0.1f}')
                print(f'FreqBinQty    {freqBinQty:d}')
                print(f'Gain          {sdrGain:0.1f}')
                print(f'Integration   {timeStampUtcSecRelThis - timeStampUtcSecRelLast:0.1f}  sec')
                print( 'ezColIntegQty', ezColIntegQty)
                print('---')
                print(f'ezColCenterFreqRef {ezColCenterFreqRef:0.6f}')
                print(f'ezColCenterFreqAnt {ezColCenterFreqAnt:0.6f}')
                print(f'FreqMin            {freqMinAnt:0.6f}')
                print(f'FreqMax            {freqMaxAnt:0.6f}')
                print('---')
                print(fileNameDashS)
                print('SampleQty   ', fileSample, dataFlagsS)
                print('---')
                print(timeUtcDateS + '   ' + timeUtcTimeS + '  UTC')
                print(timePcDateS  + '   ' + timePcTimeS  + '  PC')
                print( \
                    f"approximate Local Mean Sidereal Time (LMST) Hours = south's Right Ascension = {lmstThis:0.1f}")

            if ezColDashboard:
                # erase dashboard
                details_ax.clear()          # top right text section
                powerTime_ax1.clear()       # top    right "Recent Samples"  stripchart
                powerTime_ax2.clear()       # middle right "Recent One Hour" stripchart
                powerTime_ax3.clear()       # bottom       "Recent 24 Hours" stripchart
                spectrum_ax.clear()         # top left frequency spectrum


                # update top right text section
                details_ax.axis('off')

                # erase previous text
                del fig.texts[2:]

                # write column 1 (left)
                fig.text(0.53, 0.95, \
                    ezRAObsName \
                    + '\n  Latitude\n  Longitude\n  Amsl', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                fig.text(0.53, 0.76, \
                    '  FreqBinQty\n  Gain\n  Integration', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)

                # write column 2
                fig.text(0.61, 0.95, \
                    f'\n{ezRAObsLat:0.1f}\n{ezRAObsLon:0.1f}\n{ezRAObsAmsl:0.0f}\n', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                fig.text(0.61, 0.83, \
                    f'{ezColAzimuth:0.1f}\n{ezColElevation:0.1f}', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                fig.text(0.61, 0.76, \
                    f'{freqBinQty:d}\n{sdrGain:0.1f}\n{timeStampUtcSecRelThis - timeStampUtcSecRelLast:0.1f}  sec', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)

                # write column 3
                fig.text(0.68, 0.95, \
                    'FreqCtrRef\nFreqCtr\nFreqMin\nFreqMax\n\n' \
                    + fileNameDashS + '\nSampleQty\n\n' \
                    + timeUtcDateS + '  ' + timeUtcTimeS + '  UTC\n' \
                    + timePcDateS  + '  ' + timePcTimeS  + '  PC', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)

                # write column 4 (right)
                fig.text(0.77, 0.95, \
                    f'{ezColCenterFreqRef:0.6f}\n{ezColCenterFreqAnt:0.6f}\n' \
                        + f'{freqMinAnt:0.6f}\n{freqMaxAnt:0.6f}\n\n\n{fileSample:d}   ' \
                    + dataFlagsS, \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)

                # update stripchart data.
                # trim last of rmsAvgHistory and append this sample's average of rmsSpectrum to first position
                rmsAvgHistory = np.concatenate([ \
                    np.array([sum(rmsSpectrum) / freqBinQty]), rmsAvgHistory[:-1] ])

                # trim last of timeStampUtcHourRelHistory and append this sample's timeStamp to first position
                timeStampUtcHourRelHistory = np.concatenate([ \
                    np.array([timeStampUtcHourRelThis]), \
                    timeStampUtcHourRelHistory[:-1] ])



                # plot top right "Recent Samples" stripchart
                powerTime_ax1.plot(range(rmsAvgHistoryLenRecentMost), \
                    rmsAvgHistory[:rmsAvgHistoryLenRecentMost], \
                    marker = '.', markersize = 2, color = 'b')
                # x axis increases to the left
                powerTime_ax1.set(xlim = [rmsAvgHistoryLenRecentMost, 0], \
                    xlabel = 'Recent Samples', ylabel = 'Relative RMS Power')



                # plot middle right "Recent One Hour" stripchart
                timeStampUtcHourRelHistoryRecent = timeStampUtcHourRelThis - timeStampUtcHourRelHistory

                powerTime_ax2.plot(timeStampUtcHourRelHistoryRecent[:rmsAvgHistoryLenRecentHour], \
                    rmsAvgHistory[:rmsAvgHistoryLenRecentHour], \
                    marker = '.', markersize = 2, color = 'c')
                # x-scale increases to the left
                powerTime_ax2.set(xlim = [1, 0], xticks=np.linspace(1, 0, num=11, endpoint=True),
                    xlabel = 'Recent One Hour', ylabel = 'Relative RMS Power')

                # set top Local Mean Sidereal Time (LMST) x-scale
                lmstThisInTenths = int(lmstThis * 10.) / 10.        # lmstThis with one decimal digit
                powerTime_ax2XBXticks = \
                    [lmstThisInTenths - x for x in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]]
                powerTime_ax2XB.set(xlim=[lmstThis - 1, lmstThis], \
                    xticks=powerTime_ax2XBXticks, \
                    xticklabels=[f'{x:0.1f}' for x in powerTime_ax2XBXticks], \
                    xlabel = "approximate Local Mean Sidereal Time (LMST) Hours = south's Right Ascension")



                # plot bottom "Recent 24 Hours" stripchart
                powerTime_ax3.plot(timeStampUtcHourRelHistoryRecent, \
                    rmsAvgHistory, \
                    marker = '.', markersize = 2, color = 'r')
                # x-scale increases to the left
                powerTime_ax3.set(xlim = [24., 0.], xticks=range(24, -1, -1), \
                    xlabel = 'Recent 24 Hours', ylabel = 'Relative RMS Power')

                # set top Local Mean Sidereal Time (LMST) x-scale
                lmstThisInt = int(lmstThis)
                powerTime_ax3XB.set(xlim=[lmstThis - 24., lmstThis], \
                    xticks=[lmstThisInt - x for x in [23, 22, 21, 20,
                        19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 
                        9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
                    xticklabels=lmstLabels1to0to0[lmstThisInt:lmstThisInt + 24], \
                    xlabel = "Local Mean Sidereal Time (LMST) Hours = south's Right Ascension")


                # plot top left frequency spectrum
                if feedRef:
                    # update as last REF spectrum
                    rmsSpectrumRefLast = rmsSpectrum
                else:
                    # update as last Ant spectrum
                    rmsSpectrumAntLast = rmsSpectrum

                # refAction from radio1 radio button
                if not refAction:           # if not refDiv nor refSub
                    if feedRef:
                        # plot as Ref spectrum, with REF frequencies
                        spectrum_ax.plot(freqsRef, rmsSpectrum, color = 'r')
                        # plot as Ref spectrum, with REF frequency limit values
                        spectrum_ax.set(xlim = [freqMinRef, freqMaxRef],
                            xlabel = 'Reference Frequency (MHz)', ylabel = 'Relative RMS Power')
                        # plot vertical dashed green line on REF center frequency
                        spectrum_ax.axvline(ezColCenterFreqRef, color = 'g', linestyle = ':', linewidth = 2)
                    else:
                        # plot as Ant spectrum, with Ant frequencies
                        spectrum_ax.plot(freqsAnt, rmsSpectrum, color = 'r')
                        # plot as Ant spectrum, with Ant frequency limit values
                        spectrum_ax.set(xlim = [freqMinAnt, freqMaxAnt],
                            xlabel = 'Frequency (MHz)', ylabel = 'Relative RMS Power')
                        # plot vertical dashed green line on Ant center frequency
                        spectrum_ax.axvline(ezColCenterFreqAnt, color = 'g', linestyle = ':', linewidth = 2)

                elif refAction == 1:      # refDiv: plot last Ant spectrum divided by last REF spectrum
                    spectrum_ax.plot(freqsAnt, \
                        tuple(map(operator.truediv, rmsSpectrumAntLast, rmsSpectrumRefLast)), color = 'r')
                    # plot as Ant spectrum, with Ant frequency limit values
                    spectrum_ax.set(xlim = [freqMinAnt, freqMaxAnt],
                        xlabel = 'Frequency (MHz)', ylabel = 'Relative RMS Power')
                    # plot vertical dashed green line on Ant center frequency
                    spectrum_ax.axvline(ezColCenterFreqAnt, color = 'g', linestyle = ':', linewidth = 2)

                else:
                    # refAction == 2:   # refSub: plot last Ant spectrum after subtracting last REF spectrum
                    spectrum_ax.plot(freqsAnt, \
                        tuple(map(operator.__abs__, \
                        map(operator.sub, rmsSpectrumAntLast, rmsSpectrumRefLast))), color = 'r')
                    # plot as Ant spectrum, with Ant frequency limit values
                    spectrum_ax.set(xlim = [freqMinAnt, freqMaxAnt],
                        xlabel = 'Frequency (MHz)', ylabel = 'Relative RMS Power')
                    # plot vertical dashed green line on Ant center frequency
                    spectrum_ax.axvline(ezColCenterFreqAnt, color = 'g', linestyle = ':', linewidth = 2)

                # read autoscaled left-side y-scale limit values
                spectrum_axY0, spectrum_axY1 = spectrum_ax.get_ylim()
                spectrum_axY1MY0 = spectrum_axY1 - spectrum_axY0        # full autoscaled ylim range, Y1 Minus Y0
                # use ezColYLim0 and ezColYLim1 to set fraction of autoscaled left-side y-scale limit values
                spectrum_ax.set(ylim = [(ezColYLim0 * spectrum_axY1MY0) + spectrum_axY0,
                    (ezColYLim1 * spectrum_axY1MY0) + spectrum_axY0])

                # set top x-scale limits
                spectrum_axXB.set_xlim(-bandWidthD2, bandWidthD2)
                # set right-side y-scale limits
                spectrum_axYB.set_ylim(ezColYLim0, ezColYLim1)

                spectrum_ax.grid()      # turn on grid



                plt.draw()
            timeStampUtcSecRelLast = timeStampUtcSecRelThis

        # allow time for dashboard interaction ?
        plt.pause(0.5)
        #if programState:            # if Slow (, Pause, Exit)
        #    plt.pause(ezColSlowness)
        #else:
        #    plt.pause(0.1)          # Fast, allow little time for dashboard interaction
        #firstDraw = 0
        #timeStampUtcSecRelLast = timeStampUtcSecRelThis

        # mainLoop heartbeat indicator, only for testing, dashboard erased only on new spectrum
        #fig.text(0.68, 0.75, (' '*61)[:(mainLoop+mainLoop)%58] \
        #    + '1234567890'[mainLoop%10], \
        #    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
        #mainLoop += 1

        # go to top of while loop, to start next data sample



def sdrTask(bandWidthHz, ezColGain, freqBinQty, centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, ezColAntBtwnRef,
        programStateQueue, ezColIntegQtyQueue, sdrOutQueue):
    # sdrTask is started once, with arguments bandWidthHz, ezColGain, freqBinQty, centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, and ezColAntBtwnRef.
    #   It will loop and read the latest inputs from programStateQueue and ezColIntegQtyQueue.
    #   At the end of each loop it will output one tuple through sdrOutQueue.
    #   The tuple includes sdrGain, rmsSpectrum, and dataFlagsS.

    import numpy as np
    import operator
    from math import sqrt
    from time import sleep

    from rtlsdr import RtlSdr
    #  pip3 install pyrtlsdr   # worked on Ubuntu 18.04.5
    #  https://pypi.org/project/pyrtlsdr/
    #  https://github.com/roger-/pyrtlsdr

    #initialize the SDR
    sdr = RtlSdr()
    sdr.sample_rate = int(bandWidthHz)                          # in integer Hz
    sdr.center_freq = centerFreqAntHz                           # in integer Hz
    sdr.gain = ezColGain        # "set" SDR gain
    sdrGain = sdr.gain          # what the SDR actually set the gain to

    print('sdr.bandwidth =', sdr.bandwidth)
    print('sdr.center_freq =', sdr.center_freq)
    print('sdr.fc =', sdr.fc)
    print('sdr.freq_correction =', sdr.freq_correction)
    print('sdr.gain =', sdr.gain)
    print('sdr.rs =', sdr.rs)

    # by operating system, initialize (reset) feedRef relay system, if any
    if ezColUsbRelay:
        if os.name == 'nt':     # Windows
            # hidusb-relay-cmd.exe or serialSend.exe assumed to be in same Windows directory as ezCol program
            # in case os.path.dirname(__file__) contains space characters
            #relayOff0 = os.path.dirname(__file__).replace(' ', '\ ')
            #print(relayOff0)
            #print()

            if ezColUsbRelay == 1:
                # ezColUsbRelay = 1: 1 SPST HID relay, driving feedRef ON or OFF
                # for USB Relay that talks HID
                # https://github.com/pavel-a/usb-relay-hid
                # https://github.com/pavel-a/usb-relay-hid/releases/tag/usb-relay-lib_v2.1
                # C:\Users\c\Documents\EZRA01\usb-relay-hid_bin-20150330a\bin-Win64> hidusb-relay-cmd.exe on 1
                # define relay command strings
                # the command prompt command line
                #      ..\ezRA\hidusb-relay-cmd.exe enum 
                # returned
                #      Board ID=[HW348] State: R1=OFF
                # because of the "R1" on that last line, I use:
                relayOff0 = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe off 1'
                #relayOff1 = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe off 2'     # ignore error if only single SPDT USB Relay
                relayOff1 = ''
                relayOn0  = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe on 1'
                #relayOn1  = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe on 2'     # ignore error if only single SPDT USB Relay
                relayOn1  = ''
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
                if relayOff1:
                    os.system(relayOff1)
                    sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 2:
                # ezColUsbRelay = 2: 2 SPST HID relays, driving a latching feedRef relay with pulses
                # for USB Relay that talks HID
                # https://github.com/pavel-a/usb-relay-hid
                # https://github.com/pavel-a/usb-relay-hid/releases/tag/usb-relay-lib_v2.1
                # C:\Users\c\Documents\EZRA01\usb-relay-hid_bin-20150330a\bin-Win64> hidusb-relay-cmd.exe on 1
                # define relay command strings
                # the command prompt command line
                #      ..\ezRA\hidusb-relay-cmd.exe enum 
                # returned
                #      Board ID=[BITFT] State: R1=OFF R2=OFF
                # because of the "R1" and "R2" on that last line, I use:
                relayOff0 = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe off 1'
                relayOff1 = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe off 2'
                relayOn0  = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe on 1'
                relayOn1  = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'hidusb-relay-cmd.exe on 2'

                # initialize relays
                # both relays off
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
                os.system(relayOff1)
                sleep(0.5) # Sleep for 0.5 seconds

                # pulse 'off relay' 0 once to latch feedRef OFF
                os.system(relayOn0)
                sleep(0.5) # Sleep for 0.5 seconds
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 3:
                # ezColUsbRelay = 3: 1 SPST non-HID relay with serialSend.exe
                # for USB Relay that talks serial
                # define relay command strings
                # https://www.amazon.com/dp/B01CN7E0RQ
                #   and down below in "Customer questions & answers",
                #   see "How to set for 7sec on, 3sec off, 20sec on, 1 sec off. (5 series repeat)"
                #   talks of
                #     c:\disp\serialsend.exe /baudrate 9600 /hex "\xA0\x01\x01\xA2"
                #   and
                #     c:\disp\serialsend.exe /baudrate 9600 /hex "\xA0\x01\x00\xA1"
                # https://batchloaf.wordpress.com/serialsend/
                # https://batchloaf.wordpress.com/2011/12/05/serialsend-a-windows-program-to-send-a-text-word-via-serial-port/
                relayOff0 = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'serialSend.exe /devnum 11 /noscan /baudrate 9600 /hex "\\xA0\\x01\\x00\\xA1"'
                relayOff1 = ''
                relayOn0  = os.path.dirname(__file__).replace(' ', '\ ') + os.path.sep + 'serialSend.exe /devnum 11 /noscan /baudrate 9600 /hex "\\xA0\\x01\\x01\\xA2"'
                relayOn1  = ''
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
                if relayOff1:
                    os.system(relayOff1)
                    sleep(0.5) # Sleep for 0.5 seconds

        else:                   # (posix) Linux assumed
            # how to define relay command strings
            # https://github.com/darrylb123/usbrelay
            # sudo apt-get update
            # sudo apt-get install usbrelay
            ###os.system('sudo usbrelay BITFT_1=0 BITFT_2=0')
            #####################
            #    Serial: BITFT, Relay: 1 State: ff --- Not Found  <=================== BITFT Not Found !
            #####################
            #    > lsusb -v -d 16c0:05df
            # - output looks just like on https://github.com/darrylb123/usbrelay
            #####################
            #    > sudo usbrelay
            #    Device Found
            #      type: 16c0 05df
            #      path: /dev/hidraw2
            #      serial_number:
            #      Manufacturer: www.dcttech.com
            #      Product:      USBRelay1
            #      Release:      100
            #      Interface:    0
            #      Number of Relays = 1
            #    HW348_1=0  <================================== OK, use HW348_1 not BITFT_1 ==========
            # https://www.npmjs.com/package/node-red-contrib-usb-hid-relay/v/0.2.3
            # says also available are
            #    HW-348
            #    HW-343
            #    HW-341
            #    Models with USB-Relay-1, USB-Relay-2 or USB-Relay-4 printed on the PCB
            #os.system('sudo usbrelay HW348_1=0')        # works !

            # also may be helpful ?:
            #   Human Interface Device (HID)
            #   http://vusb.wikidot.com/project:driver-less-usb-relays-hid-interface
            #       https://github.com/pavel-a/usb-relay-hid
            #       http://vusb.wikidot.com/hosted-projects
            #           http://vusb.wikidot.com/examples
            #               https://www.workinprogress.ca/v-usb-tutorial-software-only-usb-for-mega-tiny/
            #   https://www.giga.co.za/ocart/index.php?route=product/product&product_id=229
            #       - part is out of stock, but has pictures and links to
            #           https://github.com/pavel-a/usb-relay-hid
            #           http://www.giga.co.za/Kit_Drivers/USB_Relay2.zip
            #           https://github.com/darrylb123/usbrelay
            #           and says
            #               Here is an example how to control the relay in command line.
            #               CommandApp_USBRelay.exe [device id] [close / open] [relay nr]
            #                   CommandApp_USBRelay.exe J34EL close 01
            #                   CommandApp_USBRelay.exe J34EL open 01

            if ezColUsbRelay == 1:
                # ezColUsbRelay = 1: 1 SPST HID relay, driving feedRef ON or OFF
                ##os.system('sudo usbrelay BITFT_1=0 BITFT_2=0')
                #os.system('sudo usbrelay HW348_1=0')        # works !
                # define relay command strings
                # the linux command line
                #      sudo usbrelay
                # returned
                #      Device Found
                #        type: 16c0 05df
                #        path: /dev/hidraw3
                #        serial_number: 
                #        Manufacturer: www.dcttech.com
                #        Product:      USBRelay1
                #        Release:      100
                #        Interface:    0
                #        Number of Relays = 1
                #      HW348_1=0
                # because of that last line, I use:
                relayOff0 = 'sudo usbrelay HW348_1=0'
                relayOff1 = ''
                relayOn0  = 'sudo usbrelay HW348_1=1'
                relayOn1  = ''
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
                if relayOff1:
                    os.system(relayOff1)
                    sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 2:
                # ezColUsbRelay = 2: 2 SPST HID relays, driving a latching feedRef relay with pulses
                # define relay command strings
                # the linux command line
                #      sudo usbrelay
                # returned
                #      Device Found
                #        type: 16c0 05df
                #        path: /dev/hidraw3
                #        serial_number: 
                #        Manufacturer: www.dcttech.com
                #        Product:      USBRelay2
                #        Release:      100
                #        Interface:    0
                #        Number of Relays = 2
                #      BITFT_1=0
                #      BITFT_2=0
                # because of those 2 last lines, I use:
                relayOff0 = 'sudo usbrelay BITFT_1=0 BITFT_2=0'
                relayOff1 = 'sudo usbrelay BITFT_1=0 BITFT_2=0'
                relayOn0  = 'sudo usbrelay BITFT_1=1 BITFT_2=0'
                relayOn1  = 'sudo usbrelay BITFT_1=0 BITFT_2=1'

                # initialize relays
                # both relays off
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
                os.system(relayOff1)
                sleep(0.5) # Sleep for 0.5 seconds

                # pulse 'off relay' 0 once to latch feedRef OFF
                os.system(relayOn0)
                sleep(0.5) # Sleep for 0.5 seconds
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 3:
                # ezColUsbRelay = 3: 1 SPST non-HID relay with serialSend.exe
                pass                    # linux: not yet implemented

    sdrProgramState = 0     # to enter While loop
    feedRef = 0             # assume last sample was ANT sample
    antB4Ref = 0            # number of ANT samples before next REF sample
    dataFlagsS = ' '
    while sdrProgramState <= 1:
        #print('Running sdrProcess')
        # update status of 0/1/2 = Collect/Pause/Exit
        if not programStateQueue.empty():
            sdrProgramState = programStateQueue.get_nowait()

        if sdrProgramState == 2: 
            sys.exit(0)

        elif sdrProgramState == 0: 

            if not ezColIntegQtyQueue.empty():
                sdrEzColIntegQty = ezColIntegQtyQueue.get_nowait()

            if centerFreqRefHz:         # if REF samples requested
                if feedRef:
                    # last sample had feedRef ON
                    if ezColUsbRelay:
                        # https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
                        if os.name == 'nt':     # Windows
                            if ezColUsbRelay == 1:
                                # ezColUsbRelay = 1: 1 SPST HID relay, driving feedRef ON or OFF
                                os.system(relayOff0)
                                sleep(0.5) # Sleep for 0.5 seconds
                            elif ezColUsbRelay == 2:
                                # ezColUsbRelay = 2: 2 SPST HID relays, driving a latching feedRef relay with pulses
                                # pulse 'off relay' 0 once to latch feedRef OFF
                                os.system(relayOn0)
                                sleep(0.5) # Sleep for 0.5 seconds
                                os.system(relayOff0)
                                sleep(0.5) # Sleep for 0.5 seconds
                            elif ezColUsbRelay == 3:
                                # ezColUsbRelay = 3: 1 SPST non-HID relay with serialSend.exe
                                os.system(relayOff0)
                                sleep(0.5) # Sleep for 0.5 seconds
                        else:                   # (posix) Linux assumed
                            if ezColUsbRelay == 1:
                                # ezColUsbRelay = 1: 1 SPST relay, driving feedRef ON or OFF
                                os.system(relayOff0)
                                sleep(0.5) # Sleep for 0.5 seconds
                            elif ezColUsbRelay == 2:
                                # ezColUsbRelay = 2: 2 SPST relays, driving a latching feedRef relay with pulses
                                # pulse 'off relay' 0 once to latch feedRef OFF
                                os.system(relayOn0)
                                sleep(0.5) # Sleep for 0.5 seconds
                                os.system(relayOff0)
                                sleep(0.5) # Sleep for 0.5 seconds
                            elif ezColUsbRelay == 3:
                                # ezColUsbRelay = 3: 1 SPST non-HID relay with serialSend.exe
                                pass                    # not implemented

                    antB4Ref = ezColAntBtwnRef - 1  # reset number of Ant samples before next Ref sample
                    sdr.center_freq = centerFreqAntHz                   # in integer Hz
                    feedRef = 0         # this sample will be with feedRef OFF
                    dataFlagsS = ' '
                else:
                    # last sample had feedRef OFF
                    # prepare for REF only if necessary
                    if 0 < antB4Ref:                # if ANT samples before next REF sample
                        antB4Ref -= 1               #   decrement number of ANT samples before next REF sample
                    else:                           # if no ANT samples before next REF sample
                        # Reference sample if enabled
                        if ezColUsbRelay:
                            if os.name == 'nt':     # Windows
                                if ezColUsbRelay == 1:
                                    # ezColUsbRelay = 1: 1 SPST HID relay, driving feedRef ON or OFF
                                    # set Relay1 on for feedRef on
                                    os.system(relayOn0)
                                    sleep(0.5) # Sleep for 0.5 seconds
                                elif ezColUsbRelay == 2:
                                    # ezColUsbRelay = 2: 2 SPST HID relays, driving a latching feedRef relay with pulses
                                    # pulse 'on relay' 1 once to latch feedRef ON
                                    os.system(relayOn1)
                                    sleep(0.5) # Sleep for 0.5 seconds
                                    os.system(relayOff1)
                                    sleep(0.5) # Sleep for 0.5 seconds
                                elif ezColUsbRelay == 3:
                                    # ezColUsbRelay = 3: 1 SPST non-HID relay with serialSend.exe
                                    # set Relay1 on for feedRef on
                                    os.system(relayOn0)
                                    sleep(0.5) # Sleep for 0.5 seconds
                            else:                   # Linux assumed
                                if ezColUsbRelay == 1:
                                    # ezColUsbRelay = 1: 1 SPST HID relay, driving feedRef ON or OFF
                                    # set Relay1 on for feedRef on
                                    os.system(relayOn0)
                                    sleep(0.5) # Sleep for 0.5 seconds
                                elif ezColUsbRelay == 2:
                                    # ezColUsbRelay = 2: 2 SPST HID relays, driving a latching feedRef relay with pulses
                                    # pulse 'on relay' 1 once to latch feedRef ON
                                    os.system(relayOn1)
                                    sleep(0.5) # Sleep for 0.5 seconds
                                    os.system(relayOff1)
                                    sleep(0.5) # Sleep for 0.5 seconds
                                elif ezColUsbRelay == 3:
                                    # ezColUsbRelay = 3: 1 SPST non-HID relay with serialSend.exe
                                    pass                    # not implemented

                        sdr.center_freq = centerFreqRefHz                   # in integer Hz
                        feedRef = 1         # this sample will be with feedRef ON
                        dataFlagsS = ' R'

            # create tuple with Power Spectral Density (PSD), values averaged from sdrEzColIntegQty datasets
            psdSummed = (0, ) * freqBinQty
            for __ in range(sdrEzColIntegQty):
                # for more convenient (and faster) data values,
                #   uncalibrated __relative__ RMS power can ignore FFT gain constants,
                #   and ignore normalizing amplitude
                #psd = np.abs(np.fft.fft(sdr.read_samples(freqBinQty)) / freqBinQty)       # gives small values
                #psd = np.abs(np.fft.fft(sdr.read_samples(freqBinQty)) / bandWidthHz)      # gives tiny values
                psd = np.abs(np.fft.fft(sdr.read_samples(freqBinQty))) # dashboard values displayed using less space
                psdSummed = tuple(map(operator.add, psdSummed, np.fft.fftshift(psd * psd)))     # sum so far

            # create tuple with Root Mean Squared (RMS) power frequency spectrum from those sdrEzColIntegQty readings
            # https://en.wikipedia.org/wiki/Root_mean_square
            #   Root Mean Squared (RMS) power = sqrt((x1*x1 + x2*x2 + x3*x3 + ... + xn*xn) / n)
            rmsSpectrum = tuple(sqrt(i / sdrEzColIntegQty) for i in psdSummed)                # square root

            sdrOut = rmsSpectrum = (sdrGain, rmsSpectrum, dataFlagsS)

            sdrOutQueue.put(sdrOut)

#run the main process
if __name__ == "__main__":
    main()

