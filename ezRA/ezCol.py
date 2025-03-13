programName = 'ezCol250313a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezCol Data COLlector program,
#   COLlect radio signals into integrated frequency spectrum data ezRA .txt files.
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

# Modified from Victor Boesen's https://github.com/byggemandboesen/H-line-software

# Thanks to Todd Ullery, ezColX.py was an experimental multiple process version of ezCol.py ,
# to improve graphic dashboard responsiveness, 221130 and 221202.


# ezCol250313a, ring bell after errors
# ezCol250228a, -ezColRefAction
# ezCol250219a, -ezColSecMax
# ezCol250212a, -ezColSecMax
# ezCol240716a, helpful config comments for ezSerRelay.py
# ezCol240715b, swapped locations of 'To File' and 'Off' RadioButtons
# ezCol240715a, Python3.12+ SyntaxWarnings
# ezCol240714b, relayQuietS for Linux syntax
# ezCol240714a, removed several os.path.sep,
#   improvements thanks to Richard Cochois
#       ezColGain to float, and sdr.set_gain(), and sdr.get_gain(),
#       sdr.valid_gains_db,
#       ezColBiasTeeOn,
#       relaySudoS and relayQuietS,
#       ezColUsbRelay == 15 on Linux, using new ezSerRelay.py
#       sdr.close()
# ezCol240712a, raw string for -ezDefaultsFile Windows help
# ezCol240706a, use double quotes to allow for spaces in path of Window call of hidusb-relay-cmd.exe
# ezCol240705a, accounting for any spaces in path, '\ ' to r'\ ' to fix the many (Python3.12+ ?)
#       SyntaxWarning: invalid escape sequence '\ ',
#   moved print of sys.version
# ezCol240522a, first sampleNumber and fileSample are now 0
# ezCol240422a, newFileButton should not clear stripchart plots
# ezCol240420a, fixed New File,
#   many improvements near rmsAvgHistoryLenRecent24Hour and rmsAvgHistoryLenRecent1Hour
# ezCol240419b, New File bug
# ezCol240419a, fixes for ezColDashboard 0, stopped at rmsAvgHistoryLenRecentMost,
#   sys.version
# ezCol240418a, stops at 510 ?, if not ezColDashboard: programStateQueue = Queue()
# ezCol240417f, dusting
# ezCol240417e, unlock graphics window autofocus (allows window sizing), dusting
# ezCol240417c, plot trimmed rmsAvgHistory to avoid y-autoScaling on unseen data,
#   unlock graphics window autofocus ?
# ezCol240417b, if "Idle", print red fileNameDashS inside parentheses
# ezCol240417a,
#   0/1/2 = Collect/Idle/Exit to "To File/Idle/Exit"
# ezCol240416a, -ezColSampleMax for environment RFI surveys
#   0/1/2 = Collect/Pause/Exit to Collect/Idle/Exit
#       where Idle still exercises the SDR to keep it warm,
#   removed need for programStatePutLast and ezColIntegQtyPutLast
# ezCol240221b, add RaDec and GLatGLon creation,
#   changed ezRA .txt file format
#       from 'az x.xx el y.yy' to 'azDeg x.xx elDeg y.yy',
#       and from (unposted) 'ra x.xx dec y.yy' to 'raH x.xx decDeg y.yy',
#       and from (unposted) 'glat x.xx glon y.yy' to 'gLatDeg x.xx gLonDeg y.yy',
#       so will need updates to ezCon240219b.py and ezColGNSM240219d.py
# ezCol240221a, add RaDec and GLatGLon creation
# ezCol231211a.py, if ezColUsbRelay, add ' Relay' or ' R' to end of ezColCenterFreqRef display lines
# ezCol231108a.py, ezColAntBtwnRef into ezColArgumentsFile()
# ezCol231004c.py, write commandStringEnd in file header
# ezCol231004b.py, write commandString in file header
# ezCol231004a.py, write commandString in file header
# ezCol230406a.py, -eX
# ezCol230316a.py, help screen edits, -eX
# ezCol230315a.py, no ezColDashboard needed centerFreqRefHz, major ezColUsbRelay improvements
# ezCol230305a.py, boilerplate from ezSky
# ezCol230301a.py, -ezez help wording
# ezCol230228a.py, ezCol230208a.py did programStateQueue.put() and ezColIntegQtyQueue.put() way too often
# ezCol230208a.py, REF should be defined in data collection process,
#   moved REF and relay control into sdrTask, ezColIntegQtyQueue, now better Ref data
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

import os
import sys
import time
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
    print(' Python sys.version =', sys.version)
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
    print('              -ezRAObsLat    40.2           (Observatory Latitude  (degrees))')
    print('              -ezRAObsLon  -105.1           (Observatory Longitude (degrees))')
    print('              -ezRAObsAmsl 1524.0           (Observatory Above Mean Sea Level (meters))')
    print('              -ezRAObsName bigDish8         (Observatory Name)')
    print('              -ezColFileNamePrefix bigDish8 (Data File Name Prefix)')
    print()
    print('              -ezColCenterFreqAnt 1420.405  (Signal          Frequency (MHz))')
    print('              -ezColCenterFreqRef 1423.405  (Dicke Reference Frequency (MHz))')
    print('              -ezColBandWidth        2.400  (Signal          Bandwidth (MHz))')
    print()
    print('              -ezColFreqBinQtyBits   8      (For  256 freqBinQty frequencies)')
    print('              -ezColFreqBinQtyBits  10      (For 1024 freqBinQty frequencies)')
    print()
    print('              -ezColGain        999.9       (Use max gain)')
    print('              -ezColOffsetPPM   5           (Tuner offset Parts-Per-Million (integer)')
    print('              -ezColAntBtwnRef  5           (number of Ant samples between Ref samples)')
    #print()
    #print('              -ezColBiasTeeOn   -1          (SDR BiasTee voltage no change)')
    #print('              -ezColBiasTeeOn    0          (SDR BiasTee voltage OFF)')
    #print('              -ezColBiasTeeOn    1          (SDR BiasTee voltage ON )')
    print()
    #print('              -ezColAzimuth   180.0         (Azimuth   pointing of antenna (degrees))')
    #print('              -ezColElevation  45.0         (Elevation pointing of antenna (degrees))')
    print('              -ezColAzDeg     180.0         (Azimuth            pointing of antenna (degrees))')
    print('              -ezColElDeg      45.0         (Elevation          pointing of antenna (degrees))')
    print()
    print('              -ezColRaH        20.0         (Right Ascension    pointing of antenna (hours))')
    print('              -ezColDecDeg     40.7         (Declination        pointing of antenna (degrees))')
    print()
    print('              -ezColGLatDeg     0.0         (Galactic Latitude  pointing of antenna (degrees))')
    print('              -ezColGLonDeg    30.0         (Galactic Longitude pointing of antenna (degrees))')
    print()
    print('              -ezColVerbose     1           (Turn on Verbose mode)')
    print('              -ezColDashboard   0           (Turn off graphical display)')
    print('              -ezColDispGrid    1           (Turn on graphical display plot grids)')
    print()
    #print('              -ezColUsbRelay   0            (No relays driving a feed Dicke reference)')
    #print('              -ezColUsbRelay   1            (1 SPST HID relay, driving feedRef ON or OFF)')
    #print('              -ezColUsbRelay   2            (2 SPST HID relays, driving a latching feedRef',
    #    ' relay with pulses)')
    #print('              -ezColUsbRelay   3            (1 SPST non-HID relay, driving feedRef ON or OFF)')
    print('              -ezColUsbRelay    0           (No relays driving a feed Dicke reference)')
    print('              -ezColUsbRelay   11           (1 SPST HID relay,     driving feedRef ON or OFF)')
    print('              -ezColUsbRelay   15           (1 SPST non-HID relay, driving feedRef ON or OFF)')
    print('              -ezColUsbRelay   21           (2 SPST HID relays, #1 driving feedRef ON or OFF)')
    print('              -ezColUsbRelay   22           (2 SPST HID relays, #2 driving feedRef ON or OFF)')
    print('              -ezColUsbRelay   29           (2 SPST HID relays, driving a latching feedRef',
        'relay with pulses)')
    print()
    print('              -ezColIntegQty   31000        (Number of readings to be integrated into',
        'one sample)')
    print('              -ezColTextFontSize   11       (Size of text font)')
    print('              -ezColSampleMax      10       (last sample number before exit)')
    print('              -ezColSecMax         3600.2   (maximum number of seconds before exit)')
    print('              -ezColRefAction      1        (0/1/2 for initial Off/RefDiv/RefSub)')
    print('              -ezColYLimL      0.1  0.4     (Fraction of Y Auto Scale, Min and Max)')
    print()
    print(r'              -ezDefaultsFile ..\bigDish8.txt   (Additional file of default arguments)')
    print()
    print('              -eXXXXXXXXXXXXXXzIgonoreThisWholeOneWord')
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
    global ezColGain                        # float
    global ezColBiasTeeOn                   # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzDeg                       # float
    global ezColElDeg                       # float
    global ezColRaH                         # float
    global ezColDecDeg                      # float
    global ezColGLatDeg                     # float
    global ezColGLonDeg                     # float
    global coordType                        # integer

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global ezColUsbRelay                    # integer

    global ezColIntegQty                    # integer
    global ezColTextFontSize                # integer
    global ezColSampleMax                   # integer
    global ezColSecMax                      # float
    global ezColRefAction                   # integer
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

            elif thisLine0Lower == '-ezColBiasTeeOn'.lower():
                ezColBiasTeeOn = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColAntBtwnRef'.lower():
                ezColAntBtwnRef = int(thisLineSplit[1])

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

            elif thisLine0Lower == '-ezColSampleMax'.lower():
                ezColSampleMax = int(thisLineSplit[1])

            elif thisLine0Lower == '-ezColSecMax'.lower():
                ezColSecMax = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColRefAction'.lower():
                ezColRefAction = int(thisLineSplit[1])


            # float arguments
            elif thisLine0Lower == '-ezColCenterFreqAnt'.lower():
                ezColCenterFreqAnt = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColCenterFreqRef'.lower():
                ezColCenterFreqRef = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColBandWidth'.lower():
                ezColBandWidth = float(thisLineSplit[1])

            elif thisLine0Lower == '-ezColAzimuth'.lower() or thisLine0Lower == '-ezColAzDeg'.lower():
                ezColAzDeg = float(thisLineSplit[1])
                coordType = 0               # AzEl

            elif thisLine0Lower == '-ezColElevation'.lower() or thisLine0Lower == '-ezColElDeg'.lower():
                ezColElDeg = float(thisLineSplit[1])
                coordType = 0               # AzEl

            elif thisLine0Lower == '-ezColRaH'.lower():
                ezColRaH = float(thisLineSplit[1])
                coordType = 1               # RaDec

            elif thisLine0Lower == '-ezColDecDeg'.lower():
                ezColDecDeg = float(thisLineSplit[1])
                coordType = 1               # RaDec

            elif thisLine0Lower == '-ezColGLatDeg'.lower():
                ezColGLatDeg = float(thisLineSplit[1])
                coordType = 2               # GLatGLon

            elif thisLine0Lower == '-ezColGLonDeg'.lower():
                ezColGLonDeg = float(thisLineSplit[1])
                coordType = 2               # GLatGLon

            elif thisLine0Lower == '-ezColGain'.lower():
                ezColGain = float(thisLineSplit[1])


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
                print('\a')     # ring bell
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
    global ezColGain                        # float
    global ezColBiasTeeOn                   # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzDeg                       # float
    global ezColElDeg                       # float
    global ezColRaH                         # float
    global ezColDecDeg                      # float
    global ezColGLatDeg                     # float
    global ezColGLonDeg                     # float
    global coordType                        # integer

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global cmdDirectoryS                    # string            creation

    global ezColUsbRelay                    # integer

    global ezColIntegQty                    # integer
    global ezColTextFontSize                # integer
    global ezColSampleMax                   # integer
    global ezColSecMax                      # float
    global ezColRefAction                   # integer
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
                ezColGain = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColBiasTeeOn'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColBiasTeeOn = int(cmdLineSplit[cmdLineSplitIndex])

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

            elif cmdLineArgLower == '-ezColSampleMax'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColSampleMax = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColSecMax'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColSecMax = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezColRefAction'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColRefAction = int(cmdLineSplit[cmdLineSplitIndex])


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

            elif cmdLineArgLower == '-ezColAzimuth'.lower() or cmdLineArgLower == '-ezColAzDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColAzDeg = float(cmdLineSplit[cmdLineSplitIndex])
                coordType = 0               # AzEl

            elif cmdLineArgLower == '-ezColElevation'.lower() or cmdLineArgLower == '-ezColElDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColElDeg = float(cmdLineSplit[cmdLineSplitIndex])
                coordType = 0               # AzEl

            elif cmdLineArgLower == '-ezColRaH'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColRaH = float(cmdLineSplit[cmdLineSplitIndex])
                coordType = 1               # RaDec

            elif cmdLineArgLower == '-ezColDecDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColDecDeg = float(cmdLineSplit[cmdLineSplitIndex])
                coordType = 1               # RaDec

            elif cmdLineArgLower == '-ezColGLatDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColGLatDeg = float(cmdLineSplit[cmdLineSplitIndex])
                coordType = 2               # GLatGLon

            elif cmdLineArgLower == '-ezColGLonDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColGLonDeg = float(cmdLineSplit[cmdLineSplitIndex])
                coordType = 2               # GLatGLon


            # list arguments:
            elif cmdLineArgLower == '-ezColYLimL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColYLim0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezColYLim1 = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezColArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

            # ignore silly -eX* arguments, for handy neutralization of command line arguments,
            #   but remove spaces before argument numbers
            #   (can not use '-x' which is a preface to a negative hexadecimal number)
            elif 3 <= len(cmdLineArgLower) and cmdLineArgLower[:3] == '-ex':
                pass

            # before -eX, old spelling:
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
                print('\a')     # ring bell
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
    global ezColGain                        # float
    global ezColBiasTeeOn                   # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzDeg                       # float
    global ezColElDeg                       # float
    global ezColRaH                         # float
    global ezColDecDeg                      # float
    global ezColGLatDeg                     # float
    global ezColGLonDeg                     # float
    global coordType                        # integer
    global coord0                           # float
    global coord1                           # float
    global coordMayBeNew                    # integer

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global ezColUsbRelay                    # integer

    global ezColIntegQty                    # integer       creation
    global ezColTextFontSize                # integer       creation
    global ezColSampleMax                   # integer       creation
    global ezColSecMax                      # float         creation

    global ezColRefAction                   # integer
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

        ezColGain = 999.9           # silly big number which RtlSdr library will reduce ?
        ezColBiasTeeOn = -1         # SDR BiasTee voltage no change

        ezColAntBtwnRef = 1         # number of Ant samples between REF samples

        ezColAzDeg   = 180.0        # Azimuth            pointing of antenna (degrees)
        ezColElDeg   =  45.0        # Elevation          pointing of antenna (degrees)
        ezColRaH     =  11.3        # Right Ascension    pointing of antenna (hours)
        ezColDecDeg  =  40.0        # Declination        pointing of antenna (degrees)
        ezColGLatDeg =   0.0        # Galactic Latitude  pointing of antenna (degrees)
        ezColGLonDeg =  30.0        # Galactic Longitude pointing of antenna (degrees)
        coordType    = 0            # AzEl

        ezColVerbose   = 0
        ezColDashboard = 1
        ezColDispGrid  = 0

        ezColUsbRelay = 0           # no relays driving a feedRef

        ezColIntegQty = 31000       # number of samples to be integrated into one recorded sample
        ezColTextFontSize = 10

        ezColSampleMax = sys.maxsize         # last integer sample number before exit
        ezColSecMax    = float(sys.maxsize)  # maximum number of seconds before exit

        ezColRefAction = 0          # default is Off
        ezColYLim0     = 0.0        # fraction of Y Auto Scale, Minimum
        ezColYLim1     = 1.0        # fraction of Y Auto Scale, Maximum

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

    if ezColBiasTeeOn not in [-1, 0, 1]:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezColBiasTeeOn, 'is an unrecognized value for ezColBiasTeeOn')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    # now know coordType, assign coord0, and coord1
    if coordType == 0:
        coord0     = ezColAzDeg
        coord1     = ezColElDeg
    elif coordType == 1:
        coord0     = ezColRaH
        coord1     = ezColDecDeg
    else:
        # 'GLatGLon'
        coord0     = ezColGLatDeg
        coord1     = ezColGLonDeg
    coordMayBeNew = 1

    if ezColUsbRelay not in [0, 11, 15, 21, 22, 29]:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezColUsbRelay, 'is an unrecognized value for ezColUsbRelay')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezColAntBtwnRef < 1:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezColAntBtwnRef, 'is an invalid value for ezColAntBtwnRef')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezColSecMax < 0.:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezColSecMax, 'is an invalid value for ezColSecMax')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezColRefAction not in [0, 1, 2]:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezColRefAction, 'is an unrecognized value for ezColRefAction')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()




    # fix silly arguments
    if not ezColFileNamePrefix:
        ezColFileNamePrefix = ezRAObsName.split()[0]    # first word of ezRAObsName
    if not ezColCenterFreqRef and ezColUsbRelay:
        ezColCenterFreqRef = ezColCenterFreqAnt

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
    print('   ezColBiasTeeOn      =', ezColBiasTeeOn)
    print('   ezColAntBtwnRef     =', ezColAntBtwnRef)
    print()
    print('   ezColAzDeg =', ezColAzDeg)
    print('   ezColElDeg =', ezColElDeg)
    print('   ezColRaH    =', ezColRaH)
    print('   ezColDecDeg =', ezColDecDeg)
    print('   ezColGLatDeg =', ezColGLatDeg)
    print('   ezColGLonDeg =', ezColGLonDeg)
    print('   coordType =', coordType)
    print()
    print('   ezColVerbose   =', ezColVerbose)
    print('   ezColDashboard =', ezColDashboard)
    print('   ezColDispGrid  =', ezColDispGrid)
    print()
    print('   ezColUsbRelay =', ezColUsbRelay)
    print('   ezColIntegQty =', ezColIntegQty)
    print('   ezColTextFontSize =', ezColTextFontSize)
    print('   ezColSampleMax =', ezColSampleMax)
    print('   ezColSecMax    =', ezColSecMax)
    print('   ezColRefAction =', ezColRefAction)
    print('   ezColYLimL     = [', ezColYLim0, ',', ezColYLim1, ']')



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
    global ezColGain                        # float
    global ezColBiasTeeOn                   # integer
    global ezColAntBtwnRef                  # integer

    global ezColAzDeg                       # float
    global ezColElDeg                       # float
    global ezColRaH                         # float
    global ezColDecDeg                      # float
    global ezColGLatDeg                     # float
    global ezColGLonDeg                     # float
    global coordType                        # integer
    global coord0                           # float
    global coord1                           # float
    global coordMayBeNew                    # integer

    global ezColVerbose                     # integer
    global ezColDashboard                   # integer
    global ezColDispGrid                    # integer

    global ezColUsbRelay                    # integer
    global commandString                    # string
    global dateDayLastS                     # string
    global rmsAvgHistory                    # float array
    global rmsAvgHistoryLenRecent24Hour     # integer
    global rmsAvgHistoryLenRecent1Hour      # integer
    global programState                     # integer
    global refAction                        # integer
    global ezColIntegQty                    # integer
    global ezColRefAction                   # integer
    global ezColYLim0                       # float
    global ezColYLim1                       # float
    global ezColTextFontSize                # integer
    global ezColSampleMax                   # integer
    global ezColSecMax                      # float

    printHello()

    ezColArguments()


    # delayed these imports until after possible help screen
    from datetime import date, datetime, timezone
    import numpy as np
    import operator
    from multiprocessing import Process, Queue
    import matplotlib
    #matplotlib.use('Agg')
    # graphics window was always annoyingly grabbing focus
    #   https://stackoverflow.com/questions/44278369/how-to-keep-matplotlib-python-window-in-background
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    # ModuleNotFoundError: No module name 'tkinter'
    #   sudo apt-get install python3-tk
    #   sudo apt-get install python3-pil python3-pil.imagetk 
    from matplotlib.widgets import Button, RadioButtons, TextBox

    print('\n matplotlib.__version__ =', matplotlib.__version__)

    freqBinQty = 2 ** ezColFreqBinQtyBits

    coordName = [[['azDeg', 'elDeg'], ['raH', 'decDeg'], ['gLatDeg', 'gLonDeg']],
                 [['AzDeg', 'ElDeg'], ['RaH', 'DecDeg'], ['GLatDeg', 'GLonDeg']]]
    # print('coordName[capital][coordType][coord])

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
    lmstZero = -1.      # flag lmstZero as not yet calculated

    # relative history of timeStampUtc in hours
    # timeStampUtcHourRelHistory[0] is most recent, on the right edge of stripcharts
    timeStampUtcHourRelHistory = np.zeros(0)
    rmsAvgHistory = np.full(0, np.nan)
    rmsAvgHistoryLenRecent24Hour = 0
    rmsAvgHistoryLenRecent1Hour  = 0
    rmsAvgHistoryLenRecentMost   = 510

    freqMinAnt = (ezColCenterFreqAnt - (ezColBandWidth / 2.))   # in MHz
    freqMaxAnt = freqMinAnt + ezColBandWidth                    # in MHz

    centerFreqAntHz = int(ezColCenterFreqAnt * 1e6)             # in integer Hz
    centerFreqRefHz = int(ezColCenterFreqRef * 1e6)         	# in integer Hz
    bandWidthHz = ezColBandWidth * 1e6                          # in float Hz

    programState = 0                # 0: "To File", 1: Idle, 2: Exit, in case no ezColDashboard
    
    if ezColUsbRelay:
        ezColUsbRelayS = ' Relay'
    else:
        ezColUsbRelayS = ''

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

        bandWidthD2 = ezColBandWidth / 2.                       # ezColBandWidth Divided by 2, in MHz

        freqMinRef = (ezColCenterFreqRef - bandWidthD2)         # in MHz
        freqMaxRef = freqMinRef + ezColBandWidth                # in MHz

        freqsAnt = np.linspace(start=freqMinAnt, stop=freqMaxAnt, num=freqBinQty)
        freqsRef = np.linspace(start=freqMinRef, stop=freqMaxRef, num=freqBinQty)

        # dashboard 'NewPlot' button, to clear stripchart plots
        def newPlot(event):
            global rmsAvgHistory
            global rmsAvgHistoryLenRecent24Hour
            global rmsAvgHistoryLenRecent1Hour
            rmsAvgHistory = np.full(0, np.nan)
            rmsAvgHistoryLenRecent24Hour = 0
            rmsAvgHistoryLenRecent1Hour  = 0
        axNewPlot = plt.axes([0.865, 0.95, 0.05, 0.04])
        bNewPlot = Button(axNewPlot, 'New Plot')
        bNewPlot.on_clicked(newPlot)

        # dashboard 'NewFile' button, to start a new data file, and clear stripchart plots
        def newFile(event):
            global dateDayLastS
            dateDayLastS = 'newFileButton'                      # silly value to force new data file
        axNewFile = plt.axes([0.92, 0.95, 0.05, 0.04])
        bNewFile = Button(axNewFile, 'New File')
        bNewFile.on_clicked(newFile)

        # dashboard 'coord0' number entry, change coord0 value live
        def coord0Entry(coord0EntryS):
            global coord0                           # float
            global coordMayBeNew                    # integer
            coord0EntrySplit = coord0EntryS.split()
            if coord0EntrySplit:
                coord0 = float(coord0EntrySplit[0])
                coordMayBeNew = 1
        coord0Entry_ax = fig.add_axes([0.58, 0.81, 0.04, 0.04])
        coord0EntryBox = TextBox(coord0Entry_ax, '')
        coord0EntryBox.on_submit(coord0Entry)
        coord0EntryBox.set_val(str(coord0))         # initialize string of coord0EntryBox

        # dashboard 'coord1' number entry, change coord1 value live
        def coord1Entry(coord1EntryS):
            global coord1                           # float
            global coordMayBeNew                    # integer
            coord1EntrySplit = coord1EntryS.split()
            if coord1EntrySplit:
                coord1 = float(coord1EntrySplit[0])
                coordMayBeNew = 1
        coord1Entry_ax = fig.add_axes([0.58, 0.77, 0.04, 0.04])
        coord1EntryBox = TextBox(coord1Entry_ax, '')
        coord1EntryBox.on_submit(coord1Entry)
        coord1EntryBox.set_val(str(coord1))         # initialize string of coord1EntryBox

        # dashboard 'coordType' radio buttons (no change of coord0 and coord1)
        def coordTypeEntry(label):
            global coordType            # integer
            global coordMayBeNew        # integer
            if label == 'AzEl':
                coordType  = 0
            elif label == 'RaDec':
                coordType = 1
            else:
                # 'GLatGLon'
                coordType = 2
            coordMayBeNew = 1
        radio3_ax = plt.axes([0.625, 0.77, 0.05, 0.08], facecolor='lightgoldenrodyellow')
        radio3 = RadioButtons(radio3_ax, ('AzEl', 'RaDec', 'GLatGLon'))
        radio3.on_clicked(coordTypeEntry)

        # now that radio3 RadioButtons and coordTypeEntry() exist, initialize radio3
        if coordType == 0:              # AzEl
            coordTypeEntry('AzEl')
        elif coordType == 1:            # RaDec
            coordTypeEntry('RaDec')
        else:                           # GLatGLon
            coordTypeEntry('GLatGLon')

        programState = 0                # default "To File"
        programStateQueue = Queue()
        programStateQueue.put(programState)
        # dashboard 'programState' radio buttons, control data collecting priority
        # https://blog.finxter.com/matplotlib-widgets-button/
        def programStateEntry(label):
            global programState                 # integer
            if label == 'To File':
                programState = 0
                programStateQueue.put(programState)
            elif label == 'Idle': 
                programState = 1
                programStateQueue.put(programState)
            else:
                programState = 2
                programStateQueue.put(programState)
                plt.close("all")
                #sdrProcess.join()               # needed ????????????????????
                print('\n\n\n\n\n =============== Try fully killing this program by repeating many Control-C on keyboard ? ....\n\n\n\n\n')
                exit(0)

            print('\n programState =', programState, '    label =', label)
        #radio2_ax = plt.axes([0.865, 0.85, 0.05, 0.09], facecolor='lightgoldenrodyellow')
        radio2_ax = plt.axes([0.92, 0.85, 0.05, 0.09], facecolor='lightgoldenrodyellow')
        radio2 = RadioButtons(radio2_ax, ('To File', 'Idle', 'Exit'))
        radio2.on_clicked(programStateEntry)

        # dashboard 'RefDiv' radio buttons, spectrum divided by (or subtracting) last REF sample
        def refActionFunction(label):
            global refAction
            if label == 'Off':
                refAction = 0
            elif label == 'RefDiv':
                refAction = 1           # plot last Ant spectrum divided by last REF spectrum
            else:
                # 'RefSub'
                refAction = 2           # plot last Ant spectrum after subtracting last REF spectrum
        #radio1_ax = plt.axes([0.92, 0.85, 0.05, 0.09], facecolor='lightgoldenrodyellow')
        radio1_ax = plt.axes([0.865, 0.85, 0.05, 0.09], facecolor='lightgoldenrodyellow')
        #radio1 = RadioButtons(radio1_ax, ('Off', 'RefDiv', 'RefSub'))
        radio1 = RadioButtons(radio1_ax, ('Off', 'RefDiv', 'RefSub'), active=ezColRefAction)
        radio1.on_clicked(refActionFunction)
        #refAction = 0                   # default Off
        refAction = ezColRefAction

        ezColIntegQtyQueue = Queue()
        # dashboard 'ezColIntegQty' number entry, define number of readings per data sample
        def ezColIntegQtyEntry(ezColIntegQtyEntryS):
            global ezColIntegQty                    # integer
            ezColIntegQtyEntrySplit = ezColIntegQtyEntryS.split()
            if ezColIntegQtyEntrySplit:
                ezColIntegQty = int(ezColIntegQtyEntrySplit[0])
                ezColIntegQtyQueue.put(ezColIntegQty)
        ezColIntegQtyEntry_ax = fig.add_axes([0.92, 0.75, 0.05, 0.04])
        ezColIntegQtyEntryBox = TextBox(ezColIntegQtyEntry_ax, 'ezColIntegQty ')
        ezColIntegQtyEntryBox.on_submit(ezColIntegQtyEntry)
        ezColIntegQtyEntryBox.set_val(str(ezColIntegQty))   # initialize string of ezColIntegQtyEntryBox

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

        fig.show()  # show the window (figure will be in foreground, but the user may move it to background)
        #           # (avoid calling plt.show() and plt.pause() to prevent window popping to foreground)

    else:
        # ezColDashboard is 0
        programState = 0                # default "To File"
        programStateQueue = Queue()
        programStateQueue.put(programState)

        ezColIntegQtyQueue = Queue()
        ezColIntegQtyQueue.put(ezColIntegQty)

    commandStringEnd = ' '.join(commandString.split()[1:])

    # if does not exist - create new 'data' directory
    if not os.path.exists('data'):
        os.makedirs('data')
        print(' Created new "data" directory')

    sdrOutQueue = Queue()               #sdr to main communication

    sdrProcess = Process(target=sdrTask, args=(bandWidthHz, ezColGain, ezColBiasTeeOn, freqBinQty, centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, ezColVerbose, ezColAntBtwnRef,
        programStateQueue, ezColIntegQtyQueue, sdrOutQueue))
    # sdrTask is started once, with arguments bandWidthHz, ezColGain, ezColBiasTeeOn, freqBinQty, centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, ezColVerbose, and ezColAntBtwnRef.
    #   It will loop and read the latest inputs from programStateQueue and ezColIntegQtyQueue.
    #   At the end of each loop it will output one tuple through sdrOutQueue.
    #   The tuple includes sdrGain, rmsSpectrum, and dataFlagsS.
    sdrProcess.start()


    dateDayLastS = ''         # silly value to force new data file
    sampleNumber = 0
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
    timeStampUtcSecRelThis = -1.    # force at least one loop below
    firstDraw = 1           # flag to draw the plot the first time without data
    ###mainLoop = 0
    while sampleNumber < ezColSampleMax and timeStampUtcSecRelThis < ezColSecMax:
        ###print(' =========== mainLoop =', mainLoop)

        #get the rmsSpectrum from the queue
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

            # timeStampUtcS = '2022-12-22T21:19:49 '
            #                  01234567890123456789
            timeUtcDateS = timeStampUtcS[:10]
            timeUtcTimeS = timeStampUtcS[11:19]
            # https://stackoverflow.com/questions/4563272/how-to-convert-a-utc-datetime-to-a-local-datetime-using-only-standard-library
            timePcS = timeStampUtc.astimezone(tz=None).strftime('%Y-%m-%dT%H:%M:%S ')
            timePcDateS = timePcS[:10]
            timePcTimeS = timePcS[11:19]

            if lmstZero < 0.0:       # if lmstZero not yet calculated
                # with each new file, update lmstZero (changes about 4 minutes each 24 hours).
                # As described above, calculate Local Mean Sidereal Time (LMST) Hours
                tU = (timeStampUtcZeroMjd + (timeStampUtcHourRelThis / 24.) + 2400000.5 - 2451545.0) \
                    / 36525.
                gmst0UTCSec = 24110.54841 + 8640184.812866 * tU + 0.093104 * tU * tU \
                    - 6.2e-6 * tU * tU * tU
                gmst0UTCHour = gmst0UTCSec / 3600.
                lmstZero = gmst0UTCHour + timeStampUtcZeroHours + geodeticLongitude
                print('lmstZero % 24 =', lmstZero % 24.)

            # this sample's Local Mean Sidereal Time (LMST) in hours, value at dashboard stripcharts' right edge
            lmstThis = (lmstZero + timeStampUtcHourRelThis) % 24.

            if programState != 1:       # if not "Idle"
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
                    # first try fileNameS with no trailing character
                    fileNameS = fileNameMidS + '.txt'
                    if not os.path.exists(fileNameS):       # if fileNameS is available
                        fileNameDashS = ezColFileNamePrefix + fileNameHourS + '.txt'  # for dashboard
                    else:
                        # try fileNameS with one trailing character
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
                            plt.close("all")
                            #sdrProcess.join()               # needed ????????????????????
                            print('\n\n\n\n\n =============== Try fully killing this program by repeating many Control-C on keyboard ? ....\n\n\n\n\n')
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

                    # write file header
                    fileWrite.write(f'from {programRevision} {commandStringEnd}\n' \
                        + f'lat {ezRAObsLat:g} ' \
                        + f'long {ezRAObsLon:g} ' \
                        + f'amsl {str(ezRAObsAmsl)} ' \
                        + f'name {ezRAObsName}\n' \
                        + f'freqMin {freqMinAnt:g} ' \
                        + f'freqMax {freqMaxAnt:g} ' \
                        + f'freqBinQty {str(freqBinQty)}\n' \
                        + f'{coordName[0][coordType][0]} {coord0:g} ' \
                        + f'{coordName[0][coordType][1]} {coord1:g}\n' \
                        + '# times are in UTC\n'\
                        + f'# gain {str(sdrGain)}\n' \
                        + '# frequency spectrums of RMS power = sqrt(mean of sum of squares)\n')

                    coordMayBeNew = 0

                    dateDayLastS = dateDayThisS
                    fileSample = 0

                # not new file, but if coordType or coord0 or coord1 has changed, write a coord line
                elif coordMayBeNew:
                    fileWrite.write(f'{coordName[0][coordType][0]} {coord0:g} {coordName[0][coordType][1]} {coord1:g}\n')
                    coordMayBeNew = 0

                # now feedRef, timeStampUtcS, fileNameS, and fileSample are updated

                print()
                currentCenterFreq = ezColCenterFreqRef if feedRef else ezColCenterFreqAnt
                print(timeStampUtcS, 'UTC    ', fileNameS, '   ', fileSample, '  ', currentCenterFreq, 'Hz  ', dataFlagsS)
                print('Receiving', ezColIntegQty, 'readings, each with', freqBinQty, 'frequencies ...')

                # write data sample line
                fileWrite.write(timeStampUtcS + ' '.join(f'{i:.9g}' for i in rmsSpectrum) + dataFlagsS + '\n')

                if ezColVerbose:
                    print(ezRAObsName)
                    print(f'  Latitude    {ezRAObsLat:0.1f}')
                    print(f'  Longitude   {ezRAObsLon:0.1f}')
                    print(f'  Amsl        {ezRAObsAmsl:0.0f}')
                    if coordType == 0:              # AzEl
                        print(f'  AzDeg       {coord0:0.1f}')
                        print(f'  ElDeg       {coord1:0.1f}')
                    elif coordType == 1:            # RaDec
                        print(f'  RaH         {coord0:0.1f}')
                        print(f'  DecDeg      {coord1:0.1f}')
                    else:                           # GLatGLon
                        print(f'  GLatDeg     {coord0:0.1f}')
                        print(f'  GLonDeg     {coord1:0.1f}')
                    print(f'FreqBinQty    {freqBinQty:d}')
                    print(f'Gain          {sdrGain:0.1f}')
                    print(f'Integration   {timeStampUtcSecRelThis - timeStampUtcSecRelLast:0.1f}  sec')
                    print( 'ezColIntegQty', ezColIntegQty)
                    print('---')
                    print(f'ezColCenterFreqRef {ezColCenterFreqRef:0.6f}{ezColUsbRelayS}')
                    print(f'ezColCenterFreqAnt {ezColCenterFreqAnt:0.6f}')
                    print(f'FreqMin            {freqMinAnt:0.6f}')
                    print(f'FreqMax            {freqMaxAnt:0.6f}')
                    print('---')
                    print(fileNameDashS)
                    print('File SampleQty   ', fileSample, dataFlagsS)
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
                fig.text(0.51, 0.83, \
                    f'{coordName[1][coordType][0]}\n\n{coordName[1][coordType][1]}', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                fig.text(0.55, 0.83, \
                    f'{coord0:0.1f}\n\n{coord1:0.1f}', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                fig.text(0.61, 0.76, \
                    f'{freqBinQty:d}\n{sdrGain:0.1f}\n{timeStampUtcSecRelThis - timeStampUtcSecRelLast:0.1f}  sec', \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)

                # write column 3
                if programState == 1:       # if "Idle", print red fileNameDashS inside parentheses
                    fig.text(0.68, 0.95, \
                        'FreqCtrRef\nFreqCtr\nFreqMin\nFreqMax\n\n' \
                        + '\nFile SampleQty\n\n' \
                        + timeUtcDateS + '  ' + timeUtcTimeS + '  UTC\n' \
                        + timePcDateS  + '  ' + timePcTimeS  + '  PC', \
                        horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                    fig.text(0.68, 0.95, \
                        '\n\n\n\n\n(' + fileNameDashS + ')', color='red', \
                        horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)
                else:
                    fig.text(0.68, 0.95, \
                        'FreqCtrRef\nFreqCtr\nFreqMin\nFreqMax\n\n' \
                        + fileNameDashS + '\nFile SampleQty\n\n' \
                        + timeUtcDateS + '  ' + timeUtcTimeS + '  UTC\n' \
                        + timePcDateS  + '  ' + timePcTimeS  + '  PC', \
                        horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)

                # write column 4 (right)
                fig.text(0.77, 0.95, \
                    f'{ezColCenterFreqRef:0.6f}{ezColUsbRelayS[:2]}\n{ezColCenterFreqAnt:0.6f}\n' \
                        + f'{freqMinAnt:0.6f}\n{freqMaxAnt:0.6f}\n\n\n{fileSample:d}   ' \
                    + dataFlagsS, \
                    horizontalalignment='left', verticalalignment='top', fontsize=ezColTextFontSize)



                # update stripchart data

                # append this sample's average of rmsSpectrum to first position of rmsAvgHistory
                rmsAvgHistory = np.concatenate([ \
                    np.array([sum(rmsSpectrum) / freqBinQty]), rmsAvgHistory ])
                rmsAvgHistoryLenRecent24Hour += 1
                rmsAvgHistoryLenRecent1Hour  += 1

                # append this sample's timeStamp to first position of timeStampUtcHourRelHistory
                timeStampUtcHourRelHistory = np.concatenate([ \
                    np.array([timeStampUtcHourRelThis]), timeStampUtcHourRelHistory ])

                # reduce rmsAvgHistoryLenRecent24Hour index to 24 hours
                timeStampUtcHourRelHistory24Max = timeStampUtcHourRelThis + 24.
                while timeStampUtcHourRelHistory24Max < timeStampUtcHourRelHistory[rmsAvgHistoryLenRecent24Hour - 1]:
                    rmsAvgHistoryLenRecent24Hour -= 1
                # trim span of rmsAvgHistory and timeStampUtcHourRelHistory to 24 hours
                timeStampUtcHourRelHistory = timeStampUtcHourRelHistory[:rmsAvgHistoryLenRecent24Hour]
                rmsAvgHistory              = rmsAvgHistory[             :rmsAvgHistoryLenRecent24Hour]

                # reduce rmsAvgHistoryLenRecent1Hour index to 1 hour
                timeStampUtcHourRelHistory1Max = timeStampUtcHourRelThis + 1.
                while timeStampUtcHourRelHistory1Max < timeStampUtcHourRelHistory[rmsAvgHistoryLenRecent1Hour - 1]:
                    rmsAvgHistoryLenRecent1Hour -= 1

                # reduce rmsAvgHistoryLenRecent to rmsAvgHistoryLenRecentMost
                rmsAvgHistoryLenRecent = min(rmsAvgHistoryLenRecent24Hour, rmsAvgHistoryLenRecentMost)

                # plot using timeStampUtcHourRelHistoryRecent
                timeStampUtcHourRelHistoryRecent = timeStampUtcHourRelThis - timeStampUtcHourRelHistory



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



                # plot middle right "Recent One Hour" stripchart
                powerTime_ax2.plot(timeStampUtcHourRelHistoryRecent[:rmsAvgHistoryLenRecent1Hour], \
                    rmsAvgHistory[:rmsAvgHistoryLenRecent1Hour], \
                    marker = '.', markersize = 2, color = 'c')
                # x-scale increases to the left
                powerTime_ax2.set(xlim = [1., 0.], xticks=np.linspace(1, 0, num=11, endpoint=True),
                    xlabel = 'Recent One Hour', ylabel = 'Relative RMS Power')

                # set top Local Mean Sidereal Time (LMST) x-scale
                lmstThisInTenths = int(lmstThis * 10.) / 10.        # lmstThis with one decimal digit
                powerTime_ax2XBXticks = \
                    [lmstThisInTenths - x for x in [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]]
                powerTime_ax2XB.set(xlim=[lmstThis - 1, lmstThis], \
                    xticks=powerTime_ax2XBXticks, \
                    xticklabels=[f'{x:0.1f}' for x in powerTime_ax2XBXticks], \
                    xlabel = "approximate Local Mean Sidereal Time (LMST) Hours = south's Right Ascension")



                # plot top right "Recent Samples" stripchart
                powerTime_ax1.plot(range(rmsAvgHistoryLenRecent), \
                    rmsAvgHistory[:rmsAvgHistoryLenRecent], \
                    marker = '.', markersize = 2, color = 'b')
                # x axis increases to the left
                powerTime_ax1.set(xlim = [rmsAvgHistoryLenRecentMost, 0], \
                    xlabel = 'Recent Samples', ylabel = 'Relative RMS Power')



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

                # graphics window was always grabbing focus
                # https://stackoverflow.com/questions/44278369/how-to-keep-matplotlib-python-window-in-background
                #fig.canvas.draw_idle()
                fig.canvas.flush_events()   # update the plot and take care of window events (like resizing etc.)

            timeStampUtcSecRelLast = timeStampUtcSecRelThis

            # not a "sample" if not written to file
            sampleNumber += 1
            fileSample   += 1
            ###mainLoop = 0

        ###mainLoop += 1

        # go to top of while loop, to start next data sample

    # exit ezCol
    #if not sampleNumber < ezColSampleMax:
    #if not timeStampUtcSecRelThis < ezColSecMax:
    programState = 2
    programStateQueue.put(programState)
    plt.close("all")
    #sdrProcess.join()               # needed ????????????????????
    print('\n\n\n\n\n =============== Try fully killing this program by repeating many Control-C on keyboard ? ....\n\n\n\n\n')
    exit(0)



def sdrTask(bandWidthHz, ezColGain, ezColBiasTeeOn, freqBinQty, centerFreqAntHz, centerFreqRefHz,
        ezColUsbRelay, ezColVerbose, ezColAntBtwnRef, programStateQueue, ezColIntegQtyQueue, sdrOutQueue):
    # sdrTask is started once, with arguments bandWidthHz, ezColGain, ezColBiasTeeOn, freqBinQty,
    #    centerFreqAntHz, centerFreqRefHz, ezColUsbRelay, ezColVerbose, and ezColAntBtwnRef.
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
    sdr.sample_rate = int(bandWidthHz)          # in integer Hz
    sdr.center_freq = centerFreqAntHz           # in integer Hz
    #sdr.gain = ezColGain                        # "set" SDR gain
    sdr.set_gain(ezColGain)                     # "set" SDR gain
    #sdrGain = sdr.gain                          # what the SDR actually set the gain to
    sdrGain = sdr.get_gain()                    # what the SDR actually set the gain to

    print('sdr.bandwidth =', sdr.bandwidth)
    print('sdr.center_freq =', sdr.center_freq)
    print('sdr.fc =', sdr.fc)
    print('sdr.freq_correction =', sdr.freq_correction)
    print('sdr.valid_gains_db =', sdr.valid_gains_db)
    #print('sdr.gain =', sdr.gain)
    print('sdr.gain =', sdrGain)
    print('sdr.rs =', sdr.rs)

    # Control SDR BiasTee voltage
    if 0 <= ezColBiasTeeOn:
        # set/unset SDR BiasTee voltage
        if sdr.set_bias_tee(ezColBiasTeeOn) < 0:
            print('============ Could not set SDR BiasTee voltage')
        else:
            if ezColBiasTeeOn:
                print('SDR BiasTee voltage ON')
            else:
                print('SDR BiasTee voltage OFF')
        sleep(0.2)  # Sleep for x seconds

    # by operating system, initialize (reset) feedRef relay system, if any
    # -ezColUsbRelay    0           No relays driving a feed Dicke reference
    # -ezColUsbRelay   11           1 SPST HID relay,     driving feedRef ON or OFF
    # -ezColUsbRelay   15           1 SPST non-HID relay, driving feedRef ON or OFF
    # -ezColUsbRelay   21           2 SPST HID relays, #1 driving feedRef ON or OFF
    # -ezColUsbRelay   22           2 SPST HID relays, #2 driving feedRef ON or OFF
    # -ezColUsbRelay   29           2 SPST HID relays, driving a latching feedRef relay with pulses
    # https://stackoverflow.com/questions/1854/python-what-os-am-i-running-on
    if ezColUsbRelay:
        if os.name == 'nt':     # Windows
            # hidusb-relay-cmd.exe or serialSend.exe assumed to be in same  directory as ezCol program

            if ezColUsbRelay == 11:
                # ezColUsbRelay = 11: 1 SPST HID relay, driving feedRef ON or OFF
                # for USB Relay that talks HID
                # https://github.com/pavel-a/usb-relay-hid
                # https://github.com/pavel-a/usb-relay-hid/releases/tag/usb-relay-lib_v2.1
                # Assumes hidusb-relay-cmd.exe program is in the same directory as this ezCol program.
                # define relay command strings
                # the command prompt command line
                #      ..\ezRA\hidusb-relay-cmd.exe enum 
                # returned
                #      Board ID=[HW348] State: R1=OFF
                # because of the "R1" on that last line, I use:
                # Use double quotes to allow for spaces in path of Window call of hidusb-relay-cmd.exe
                relayOff0 = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" off 1'
                relayOn0  = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" on 1'
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 15:
                # ezColUsbRelay = 15: 1 SPST non-HID relay with serialSend.exe
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
                # Assumes serialSend.exe program is in the same directory as this ezCol program.
                # Use double quotes to allow for spaces in path of Window call of hidusb-relay-cmd.exe
                relayOff0 = '"' + os.path.dirname(__file__) + r'\serialSend.exe" /devnum 11 /noscan /baudrate 9600 /hex "\\xA0\\x01\\x00\\xA1"'
                relayOn0  = '"' + os.path.dirname(__file__) + r'\serialSend.exe" /devnum 11 /noscan /baudrate 9600 /hex "\\xA0\\x01\\x01\\xA2"'
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 21:
                # ezColUsbRelay = 21: 2 SPST HID relays, #1 driving feedRef ON or OFF
                # for USB Relay that talks HID
                # https://github.com/pavel-a/usb-relay-hid
                # https://github.com/pavel-a/usb-relay-hid/releases/tag/usb-relay-lib_v2.1
                # Assumes hidusb-relay-cmd.exe program is in the same directory as this ezCol program.
                # define relay command strings
                # the command prompt command line
                #      ..\ezRA\hidusb-relay-cmd.exe enum 
                # returned
                #      Board ID=[BITFT] State: R1=OFF R2=OFF
                # because of the "R1" and "R2" on that last line, I use:
                # Use double quotes to allow for spaces in path of Window call of hidusb-relay-cmd.exe
                relayOff0 = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" off 1'
                relayOn0  = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" on 1'
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 22:
                # ezColUsbRelay = 22: 2 SPST HID relays, #2 driving feedRef ON or OFF
                # for USB Relay that talks HID
                # https://github.com/pavel-a/usb-relay-hid
                # https://github.com/pavel-a/usb-relay-hid/releases/tag/usb-relay-lib_v2.1
                # Assumes hidusb-relay-cmd.exe program is in the same directory as this ezCol program.
                # define relay command strings
                # the command prompt command line
                #      ..\ezRA\hidusb-relay-cmd.exe enum 
                # returned
                #      Board ID=[BITFT] State: R1=OFF R2=OFF
                # because of the "R1" and "R2" on that last line, I use:
                # Use double quotes to allow for spaces in path of Window call of hidusb-relay-cmd.exe
                relayOff0 = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" off 2'
                relayOn0  = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" on 2'
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 29:
                # ezColUsbRelay = 29: 2 SPST HID relays, driving a latching feedRef relay with pulses
                # for USB Relay that talks HID
                # https://github.com/pavel-a/usb-relay-hid
                # https://github.com/pavel-a/usb-relay-hid/releases/tag/usb-relay-lib_v2.1
                # Assumes hidusb-relay-cmd.exe program is in the same directory as this ezCol program.
                # define relay command strings
                # the command prompt command line
                #      ..\ezRA\hidusb-relay-cmd.exe enum 
                # returned
                #      Board ID=[BITFT] State: R1=OFF R2=OFF
                # because of the "R1" and "R2" on that last line, I use:
                # Use double quotes to allow for spaces in path of Window call of hidusb-relay-cmd.exe
                relayOff0 = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" off 1'
                relayOff1 = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" off 2'
                relayOn0  = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" on 1'
                relayOn1  = '"' + os.path.dirname(__file__) + r'\hidusb-relay-cmd.exe" on 2'
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

            # 'sudo ' may want renewal and cause trouble ?
            relaySudoS = ''
            relaySudoS = 'sudo '

            if ezColVerbose:
                relayQuietS = ''
            else:
                # quiet mode
                relayQuietS = ' -q'

            if ezColUsbRelay == 11:
                # ezColUsbRelay = 11: 1 SPST HID relay, driving feedRef ON or OFF
                # for USB Relay that talks HID
                ##os.system('sudo usbrelay BITFT_1=0 BITFT_2=0')
                #os.system('sudo usbrelay HW348_1=0')        # works !
                # define relay command strings
                # the Linux command line
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
                relayOff0 = relaySudoS + 'usbrelay' + relayQuietS + ' HW348_1=0'
                relayOn0  = relaySudoS + 'usbrelay' + relayQuietS + ' HW348_1=1'
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 15:
                #######################################################
                ################ untested as of 240714 ################
                #######################################################
                # ezColUsbRelay = 15: 1 SPST non-HID relay with serialSend.exe
                # for USB Relay that talks serial
                #relayOff0 = '#'             # Linux: not yet implemented
                #relayOn0  = '#'             # Linux: not yet implemented
                #relayOff0 = 'stty -F /dev/ttyUSB0 9600; sleep 0.1s; echo echo -ne "\\xA0\\x01\\x00\\xA1" > /dev/ttyUSB0' # Working inside batch, Not working inside Python
                #relayOn0  = 'stty -F /dev/ttyUSB0 9600; sleep 0.1s; echo echo -ne "\\xA0\\x01\\x01\\xA2" > /dev/ttyUSB0' # Working inside batch, Not working inside Python
                #relayConf0 = 'sudo chmod 777 /dev/ttyUSB0'     # working
                # Put the user in the dialout group for Serial,
                #   and also in the plugdev group for USB:
                #     sudo usermod -a -G dialout,plugdev <username>
                #   
                # See the group for serial:
                #   ls -l /dev/ttyUSB0
                # gives
                #   crw-rw---- 1 root dialout 188, 0 15 juil. 14:12 /dev/ttyUSB0
                #   
                # See the group for USB:
                #   ls -l /dev/hidraw1
                # gives
                #   crw-rw---- 1 root plugdev 246, 1 15 juil. 14:12 /dev/hidraw1
                relayOff0 = relaySudoS + 'python3 ' + os.path.dirname(__file__) + '/ezSerRelay.py /dev/ttyUSB0 9600 0'
                relayOn0  = relaySudoS + 'python3 ' + os.path.dirname(__file__) + '/ezSerRelay.py /dev/ttyUSB0 9600 1'
                # initialize relays
                os.system(relayOff0)
                sleep(0.5) # Sleep for x seconds
            elif ezColUsbRelay == 21:
                # ezColUsbRelay = 21: 2 SPST HID relays, #1 driving feedRef ON or OFF
                # for USB Relay that talks HID
                relayOff0 = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=0 BITFT_2=0'
                relayOn0  = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=1 BITFT_2=0'
                # initialize relays
                # both relays off
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 22:
                # ezColUsbRelay = 22: 2 SPST HID relays, #2 driving feedRef ON or OFF
                # for USB Relay that talks HID
                relayOff0 = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=0 BITFT_2=0'
                relayOn0  = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=0 BITFT_2=1'
                # initialize relays
                # both relays off
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
            elif ezColUsbRelay == 29:
                # ezColUsbRelay = 29: 2 SPST HID relays, driving a latching feedRef relay with pulses
                # define relay command strings
                # the Linux command line
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
                relayOff0 = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=0 BITFT_2=0'
                relayOff1 = relayOff0
                relayOn0  = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=1 BITFT_2=0'
                relayOn1  = relaySudoS + 'usbrelay' + relayQuietS + ' BITFT_1=0 BITFT_2=1'
                # initialize relays
                # both relays off
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds
                #os.system(relayOff1)
                #sleep(0.5) # Sleep for 0.5 seconds
                # pulse 'off relay' 0 once to latch feedRef OFF
                os.system(relayOn0)
                sleep(0.5) # Sleep for 0.5 seconds
                os.system(relayOff0)
                sleep(0.5) # Sleep for 0.5 seconds

    sdrProgramState = 0     # "To File"
    feedRef = 0             # assume last sample was ANT sample
    antB4Ref = 0            # number of ANT samples before next REF sample
    dataFlagsS = ' '
    while 1:
        # update status of 0/1/2 = "To File/Idle/Exit"
        if not programStateQueue.empty():
            sdrProgramState = programStateQueue.get_nowait()

        if sdrProgramState == 2:
            if 0 <= ezColBiasTeeOn:
                # unset SDR BiasTee voltage
                if sdr.set_bias_tee(False) < 0:
                    print('============ Could not set SDR BiasTee voltage')
                else:
                    print('SDR BiasTee voltage OFF')
                sleep(0.2) # Sleep for x seconds
            sdr.close()
            exit(0)

        else: 
            # take ezColIntegQty readings and create a sample

            if not ezColIntegQtyQueue.empty():
                sdrEzColIntegQty = ezColIntegQtyQueue.get_nowait()

            if centerFreqRefHz:         # if REF samples requested
                if feedRef:
                    # last sample had feedRef ON
                    if ezColUsbRelay:
                        if ezColUsbRelay == 29:
                            # ezColUsbRelay = 29: 2 SPST HID relays, driving a latching feedRef relay with pulses
                            # pulse 'off relay' 0 once to latch feedRef OFF
                            os.system(relayOn0)
                            sleep(0.5) # Sleep for 0.5 seconds
                            os.system(relayOff0)
                            sleep(0.5) # Sleep for 0.5 seconds
                        else:
                            # ezColUsbRelay = 11: 1 SPST HID relay, driving feedRef ON or OFF
                            # ezColUsbRelay = 15: 1 SPST non-HID relay, driving feedRef ON or OFF
                            # ezColUsbRelay = 21: 2 SPST HID relays, #1 driving feedRef ON or OFF
                            # ezColUsbRelay = 22: 2 SPST HID relays, #2 driving feedRef ON or OFF
                            # set Relay off for feedRef off
                            os.system(relayOff0)
                            sleep(0.5) # Sleep for 0.5 seconds

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
                            if ezColUsbRelay == 29:
                                # ezColUsbRelay = 29: 2 SPST HID relays, driving a latching feedRef relay with pulses
                                # pulse 'on relay' 1 once to latch feedRef ON
                                os.system(relayOn1)
                                sleep(0.5) # Sleep for 0.5 seconds
                                os.system(relayOff1)
                                sleep(0.5) # Sleep for 0.5 seconds
                            else:
                                # ezColUsbRelay = 11: 1 SPST HID relay, driving feedRef ON or OFF
                                # ezColUsbRelay = 15: 1 SPST non-HID relay, driving feedRef ON or OFF
                                # ezColUsbRelay = 21: 2 SPST HID relays, #1 driving feedRef ON or OFF
                                # ezColUsbRelay = 22: 2 SPST HID relays, #2 driving feedRef ON or OFF
                                # set Relay on for feedRef on
                                os.system(relayOn0)
                                sleep(0.5) # Sleep for 0.5 seconds

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

