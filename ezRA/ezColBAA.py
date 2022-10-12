pgmName = 'ezColBaa220929a.py'
#pgmRev  = pgmName + ' (N0RQV)'
pgmRev  = pgmName

'''
ezColBaa220929a.py, prep for Git
ezColBaaSem220115a02.py, believe dec in file,
https://www.youtube.com/watch?v=_3vkEIYs7gk&ab_channel=britishastronomical
    GNU II Training seminar - Unpacking more mysteries of GNU Radio
    Jan 15, 2022  RAG Zoom Programme - 2022
        https://github.com/ccera-astro/baa_seminar
            fft-0-20220506.csv says
                0	0	9	8	55	52	-39.31	-39.32	-39.32 ...
            tp-20220506.csv says
                INFO:Sum	Corr(R)	Corr(I)	Diff	East	West	DEC=60.000000	FREQ=1420.405000
                    BW=2.560000			
                0	0	10	8	55	53	0.143533939	1.744E-06	1.462E-06	0.136702067	0.140118003	0.003415936
                0	1	10	8	56	53	0.143562054	9.01E-07	4.275E-06	0.136731358	0.140146706	0.003415348
                ...
'''

def main():

    import os                       # used to grab all files in the current directory
    import sys                
    import time
    #import datetime

    from astropy import units as u
    from astropy.time import Time

    import numpy as np

    startTime = time.time()
    #print(' startTime = ', startTime)
    #print(' time.asctime(time.time() = %s ' % time.asctime(time.time()))
    #print(' time.asctime(time.localtime() = %s ' % time.asctime(time.localtime()))
    print(' Local time = %s ' % time.asctime(time.localtime()))

    print(' pgmRev = ' + pgmRev)
    print()

    cmd = ''
    for i in sys.argv:
        #cmd = cmd + i + '  '
        cmd += i + '  '
    print(' This Python command = ' + cmd)



    #print(sys.argv)
    #print(len(sys.argv))

    if len(sys.argv) > 1:
        if sys.argv[1][0] == '-':       # if first character of first argument
            print()
            print()
            print('USAGE:')
            print('  python sdrVelHayA.py [directories]')
            print()
            print('  sdrVelHayA.py will process all the .rad MIT Haystack SRT txt data files in the')
            print('   (optional) directories, and create one .sdre file in the current directory.')
            print()
            print('EXAMPLES:')
            print()
            print('  python sdrVelHayA.py                         (for current directory)')
            print('  python sdrVelHayA.py .                       (for current directory)')
            print('  python sdrVelHayA.py data                    (for data directory)')
            print('  python sdrVelHayA.py data1 data2 data3       (for data1, data2, and data3 ' \
                        'directories)')
            print('  python sdrVelHayA.py aaa1800_0450            (for aaa1800_0450 directory)')
            print()
            print('  sdrVelHayA.py requires these files to be in the same directory as sdreMakeHay.py:')
            print('    sdrInit.txt                               (customized for observatory')
            print()
            print()
            print(' pgmRev = ' + pgmRev)
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

            if 0:           # test python things
                arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
                print('arr')
                print(arr)
                print('np.delete(arr, 1, 0)')
                print(np.delete(arr, 1, 0))
                print('np.delete(arr, [1,3,5], None)')
                print(np.delete(arr, [1,3,5], None))
                print('np.delete(arr, [0,2], 0)')
                print(np.delete(arr, [0,2], 0))
                print('np.delete(arr, [0,2], 1)')
                print(np.delete(arr, [0,2], 1))

                arrNp = np.array([0, 2])
                print('arrNp =')
                print(arrNp)

                print('np.delete(arr, arrNp, 0)')
                print(np.delete(arr, arrNp, 0))
                print('np.delete(arr, arrNp, 1)')
                print(np.delete(arr, arrNp, 1))

            if 0:           # test python things
                # https://numpy.org/doc/stable/reference/generated/numpy.delete.html
                arr = np.arange(12)
                print('arr =')
                print(arr)
                # arr = [ 0  1  2  3  4  5  6  7  8  9 10 11]
                mask = np.ones(len(arr), dtype=bool)
                mask[[0,2,4]] = False
                print('mask =')
                print(mask)
                mask = mask + 0
                print('mask =')
                print(mask)
                #mask = (mask == True)
                #######mask = not not mask
                #######mask = bool(mask.any)
                mask = mask != 0            # into bool
                print('mask =')
                print(mask)
                result = arr[mask,...]
                print('result =')
                print(result)
                #Is equivalent to np.delete(arr, [0,2,4], axis=0), but allows further use of mask.
                # result = [ 1  3  5  6  7  8  9 10 11]
                #including that line ..... mask = mask + 0     
                # result = [0 1 0 1 0 1 1 1 1 1 1 1]
                #then including that line ..... mask = (mask == True)
                #fixes it:
                # result = [ 1  3  5  6  7  8  9 10 11]
                # so bool numpy required ?   ones and zeroes do not work ?

            if 0:           # test python things
                print(' int( 0.5) = ', int( 0.5))
                print(' int(-0.5) = ', int(-0.5))
                print()
                print(' int( 0.5 + 0.5) = ', int( 0.5 + 0.5))
                print(' int(-0.5 - 0.5) = ', int(-0.5 - 0.5))
                print()
                print(' int( 0.4 + 0.5) = ', int( 0.4 + 0.5))
                print(' int(-0.4 - 0.5) = ', int(-0.4 - 0.5))
                print()
                print(' int( 0.9) = ', int( 0.9))
                print(' int(-0.9) = ', int(-0.9))
                print()
                print(' int( 1.1) = ', int( 1.1))
                print(' int(-1.1) = ', int(-1.1))
                print()
                freqBinBrvcOnes = np.array([1.0] * int(50.3 / 2))
                print(freqBinBrvcOnes)
                print()
            exit()



    ###################################################################################

    # Open initialization file and parse individual lines

    # SDR radio astronomy programs INITialization file (sdrInit.txt)

    # Sharp character (#) begins comment.
    # Whitespace (spaces, tabs, new lines) ignored.
    # All assignments are optional.
    # Multiple assignments are allowed, but usually only the last one is used.

    # sdrRA parameter defaults
    sdrQthName      = 'LebanonKS'
    sdrQthLat       =  39.8282    #Geographic Center of USA, near Lebanon, Kansas
    sdrQthLon       = -98.5696
    sdrQthAmsl      = 563.88

    sdrQthName      = 'N0RQV3PH'     # N0RQV 3-foot dish with CalPulser and Haystack capture
    sdrQthName      = 'N0RQV8H'      # N0RQV 8-foot dish with Haystack capture (recent)
    sdrQthName      = 'LTO15HC'      # LTO 15-foot dish with Haystack capture with feed calibration
    sdrQthName      = 'LTO15HCGE'    # LTO15 Haystack, with feed calibration, GalTour, EzRA
    sdrQthName      = 'N0RQV-H'      # N0RQV 8-foot dish with Haystack capture (early)
    sdrQthName      = 'LTO16HE'      # LTO 16-foot dish with Haystack capture, ezRA
    sdrQthLat       =  40.299512
    sdrQthLon       = -105.084491
    sdrQthAmsl      = 1524



    '''
    if len(os.path.dirname(__file__)) < 1:
        sdrInitFileName = '.' + os.path.sep + 'sdrInit.txt'
    else:
        sdrInitFileName = os.path.dirname(__file__) + os.path.sep + 'sdrInit.txt'
    '''
    sdrInitFileName = '.' + os.path.sep + 'ezColBaaSem220115init.txt'
    print()
    print(' ' + sdrInitFileName)



    # https://www.zframez.com/tutorials/python-exception-handling.html
    try:
        fileInit = open(sdrInitFileName, 'r')
        #if fileInit.mode == 'r':

        while 1:
            #print()
            fileLine = fileInit.readline()
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

            #print('=', thisLine[0].lower(), '=')
            #print('=', 'sdrQthName'.lower(), '=')
            elif thisLine[0].lower() == 'sdrQthName'.lower():
                sdrQthName = thisLine[1]
                #sdrQthName = uni.encode(thisLine[1])
                #sdrQthName = str.encode(thisLine[1])

            elif thisLine[0].lower() == 'sdrQthLatLonAmsl'.lower():
                sdrQthLat  = float(thisLine[1])
                sdrQthLon  = float(thisLine[2])
                sdrQthAmsl = float(thisLine[3])

            elif thisLine[0].lower() == 'sdrUtcOffset'.lower():
                sdrUtcOffset = float(thisLine[1])

            elif thisLine[0].lower() == 'sdrAddAzDeg'.lower():
                sdrAddAzDeg = float(thisLine[1])

            elif thisLine[0].lower() == 'sdrAddElDeg'.lower():
                sdrAddElDeg = float(thisLine[1])

            elif thisLine[0].lower() == 'sdrDispGrid'.lower():
                sdrDispGrid = int(sdrDispGrid[1])

            elif thisLine[0].lower() == 'sdreSkyInput'.lower():
                sdreSkyInput = int(thisLine[1])

            # advanced parameters:
            
            elif thisLine[0].lower() == 'sdrDispFreqBin'.lower():
                sdrDispFreqBin = int(thisLine[1])

            #elif thisLine[0].lower() == 'sdrHideFreqBin'.lower():
            #    sdrHideFreqBinL.append(int(thisLine[1]))

            #elif thisLine[0].lower() == 'sdrUseSamplesRaw'.lower():
            #    sdrUseSamplesRawL.append(int(thisLine[1]))
            #    sdrUseSamplesRawL.append(int(thisLine[2]))

            #elif thisLine[0].lower() == 'sdrUseSamplesAnt'.lower():
            #    sdrUseSamplesAntL.append(int(thisLine[1]))
            #    sdrUseSamplesAntL.append(int(thisLine[2]))

            elif thisLine[0].lower() == 'sdrDetectLevel'.lower():
                sdrDetectLevel = float(thisLine[1])

            elif thisLine[0].lower() == 'sdrAntCBTEdgeFraction'.lower():
                sdrAntCBTEdgeFraction = float(thisLine[1])

            elif thisLine[0].lower() == 'sdreMakeRfiLim'.lower():
                sdreMakeRfiLim = float(thisLine[1])

            elif thisLine[0].lower() == 'sdrBaselineLowFreqBin'.lower():
                sdrBaselineLowFreqBin = int(thisLine[1])

            elif thisLine[0].lower() == 'sdrBaselineHighFreqBin'.lower():
                sdrBaselineHighFreqBin = int(thisLine[1])

            elif thisLine[0].lower() == 'sdrFreqBinQtyPre'.lower():
                sdrFreqBinQtyPre = int(thisLine[1])

            elif thisLine[0].lower() == 'sdrFreqBinQty'.lower():
                sdrFreqBinQty = int(thisLine[1])

            elif thisLine[0].lower() == 'sdreMakeSkyMaskGalFile'.lower():
                #sdreMakeSkyMaskGalFile = thisLine[1]
                pass

            elif thisLine[0].lower() == 'sdreMakeMaskDecDegN'.lower():
                #sdreMakeMaskDecDegN = float(thisLine[1])
                pass

            elif thisLine[0].lower() == 'sdreMakeMaskDecDegS'.lower():
                #sdreMakeMaskDecDegS = float(thisLine[1])
                pass

            elif thisLine[0].lower() == 'sdreMakeSkyMaskGalOutWrite'.lower():
                #sdreMakeSkyMaskGalOutWrite = int(thisLine[1])
                pass

            else:
                print()
                print()
                print()
                print()
                print()
                print(' ========== FATAL ERROR:  Initialization file ( ' + sdrInitFileName + ' )')
                print(" has this line's unrecognized first word:")
                print(fileLine)
                print()
                print()
                print()
                print()
                exit()

    except (FileNotFoundError, IOError):
    	print ()
    	print ('Error in opening file or reading ' + sdrInitFileName + ' file.')
    	print ('... Using defaults ...')
    	print ()

    else:
        fileInit.close()       #   then have processed all available lines in this init file

    #finally:


    # print status
    print('   sdrQthName       = ' + sdrQthName)
    print('   sdrQthLat        = ' + str(sdrQthLat))
    print('   sdrQthLon        = ' + str(sdrQthLon))
    print('   sdrQthAmsl       = ' + str(sdrQthAmsl))

    ###################################################################################

    # Open each data file and read individual lines

    samplesQty     = 0              # current number of samples from all files
    refQty         = 0              # current number of reference samples
    fileWriteNamePostS = 'abcdefghijklmnopqrstuvwxyz'

    if len(sys.argv) > 1:
        #directoryList = sorted(sys.argv[1:])
        directoryList = sys.argv[1:]
    else:
        directoryList = ['.']
    #print(directoryList)

   
    directoryListLen = len(directoryList)
    #print(directoryListLen)
    
    '''
    for directoryCtr in range(directoryListLen):
        directory = directoryList[directoryCtr]
        print(directory)
        print(directory.lower())
        print(directory.lower().endswith('.rad'))

        # if arguments are .rad filenames,
        # pass each them through together as a mini directory list of .rad files.
        # Allows one .rad file from a directory of .rad files.
        # Allows .bat batch file control.
        if(directory.lower().endswith('.rad')):
            fileList = [directory]
            directory = '.'
        else:
            fileList = os.listdir(directory)
        #    fileList = sorted(os.listdir(directory))        # each directory is now sorted alphabetically
        print(fileList)
        fileListLen = len(fileList)
        #fileListLen = 1
        print(fileListLen)
        print()
        #for fileCtr in range(fileListLen):
        #fileCtr = 1
        #if 1:
    '''








    if 1:
        #for fileCtr in range(fileListLen):
        if 1:
            #fileReadName = fileList[fileCtr]
            #fileReadName = sys.argv[1]
            fileReadName = 'tp-' + sys.argv[1] + '.csv'
            print(fileReadName)

            #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
            #    + ' in dir ' + str(directoryCtr + 1) + ' of ' + str(directoryListLen) \
            #    + ' = ' + directory + '\\' + fileReadName + \
            #    '                       ', end='')   # allow append to line
            #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
            #    + ' in dir ' + str(directoryCtr + 1) + ' of ' + str(directoryListLen) \
            #    + ' = ' + directory + os.path.sep + fileReadName + \
            #    '                       ', end='')   # allow append to line

            #if(fileReadName.lower().endswith('.rad')):
            if 1:

                samplesQtyFile = 0              # current number of samples from this file
                #fileRead = open(directory + '\\' + fileReadName, 'r')
                #fileRead = open(directory + os.path.sep + fileReadName, 'r')
                fileRead = open(fileReadName, 'r')
                #fileRead = open(sys.argv[1], 'r')
                if fileRead.mode != 'r':
                    print()
                    print()
                    print()
                    print()
                    print()
                    print(' ========== FATAL ERROR:  Unable to open tp- file ( ' + fileReadName + ' ).')
                    print()
                    print()
                    print()
                    print()
                    exit()

                fileReadLine = fileRead.readline()
                #    0          1       2       3       4       5       6               7
                #                                                       01234           012345
                #        8
                #        0123

                # tp-20220506.csv says
                #    INFO:Sum	Corr(R)	Corr(I)	Diff	East	West	DEC=60.000000	FREQ=1420.405000
                #        BW=2.560000			

                thisLine = fileReadLine.split(',')

                freqBinQty  = 2048
                decDeg  = float(thisLine[6][4:])
                freqCtr = float(thisLine[7][5:])
                freqBw  = float(thisLine[8][3:])

                dataFreqMin = freqCtr - (freqBw / 2.)
                dataFreqMax = dataFreqMin + freqBw

                fileRead.close()



                fileReadName = 'fft-0-' + sys.argv[1] + '.csv'
                print(fileReadName)
                fileRead = open(fileReadName, 'r')
                #fileRead = open(sys.argv[1], 'r')
                if fileRead.mode != 'r':
                    print()
                    print()
                    print()
                    print()
                    print()
                    print(' ========== FATAL ERROR:  Unable to open fft-0- file ( ' + fileReadName + ' ).')
                    print()
                    print()
                    print()
                    print()
                    exit()

                if 1:
                    #print(' samplesFileQty =', str(samplesFileQty))

                    #sampleOfRadFile = 0

                    #print('===========================================================')
                    #print()
                    #print()
                    #print()
                    #print()
                    #print(fileReadName)


                    # now process all lines in that file that ends with .rad and allow read
                    feedRefOnThis = 0
                    #fileWriteNameThis = ''      # to avoid closing fileWriteNameThis file
                    #azimuthLast   = 9999        # silly value to force new fileWriteNameThis file
                    #elevationLast = 9999        # silly value
                    while(1):

                        #print('\r file = ' + str(fileCtr + 1) + ' of ' + str(fileListLen) \
                        #    + ' in dir ' + str(directoryCtr + 1) + ' of ' + str(directoryListLen) \
                        #    + ' = ' + directory + os.path.sep + fileReadName + \
                        #    '                       ', end='')   # allow append to line

                        fileReadLine = fileRead.readline()

                        # fft-0-20220506.csv says
                        #    0	0	9	8	55	52	-39.31	-39.32	-39.32	...

                        thisLine = fileReadLine.split(',')

                        # LF always present: 0=EOF  1=LF  2=1Character
                        # get out of loop if blank line or less
                        if len(fileReadLine) < 1:    # if end of file, might be one ending linefeed
                            # syntax error, not a valid file, reject file
                            fileRead.close()        #   then have processed all lines in this data file
                            break                    #   skip to next file ????????????????????????????????

                        # asume this is the start of a valid 4-line data set
                        #print(thisLine)

                        fileUtcYearS   = sys.argv[1][0:4]
                        fileUtcMonthS  = sys.argv[1][4:6]
                        fileUtcDayS    = sys.argv[1][6:8]

                        fileUtcHour   = int(thisLine[0])
                        fileUtcMinute = int(thisLine[1])
                        fileUtcSecond = int(thisLine[2])

                        #timeStampS = dataTimeUtcThis.strftime('%Y-%m-%dT%H:%M:%S ')
                        # timeStampS = '2022-12-22T21:19:49 '
                        timeStampS = fileUtcYearS + '-' + fileUtcMonthS + '-' + fileUtcDayS + 'T' \
                            f'{fileUtcHour:02d}:{fileUtcMinute:02d}:{fileUtcSecond:02d} '


                        # process first line of 4-line data set
                        # DATE 2020:181:00:00:05 obsn 346 az 227.9 el 73.9 freq_MHz  1420.4000
                        #   Tsys 453.943 Tant 1125.553 vlsr   23.16 glat 60.042 glon 201.727 source 
                        # 0    1                 2    3   4  5     6  7    8         9
                        #   10   11      12   13       14     15    16   17     18   19      20
                        # https://docs.astropy.org/en/stable/api/
                        #   astropy.time.TimeYearDayTime.html#astropy.time.TimeYearDayTime
                        # TimeYearDayTime
                        # format='yday'
                        # “YYYY:DOY:HH:MM:SS.sss…"
                        ###dataTimeUtcThis = Time(thisLine[1], format='yday', scale='utc')

                        #azimuthThis   = float(thisLine[5])
                        azimuthThis   = 180.
                        #elevationThis = float(thisLine[7])
                        # dec = el - 90 + lat
                        # dec + 90 - lat = el
                        elevationThis = float(decDeg - sdrQthLat + 90.)





                        elevationThis = 30.





                        '''
                        if 90. < elevationThis:
                            # to allow calculations, simulate rotating dish
                            elevationThis =  180 - elevationThis
                            azimuthThis   -= 180.
                            #print('after adjustment, using dataAzimuth   = ', dataAzimuth)
                            #print('after adjustment, using dataElevation = ', dataElevation)

                        if azimuthThis < 0.:
                            azimuthThis += 360.
                        if 360. <= azimuthThis:
                            azimuthThis -= 360.
                        '''

                        print('azimuthThis   = ', azimuthThis)
                        print('elevationThis = ', elevationThis)



                        '''
                        # read second line of 4-line data set
                        # Fstart 1419.200 fstop 1421.600 spacing 0.009375 bw    2.400 fbw    2.400 MHz
                        #   nfreq 256 nsam 5242880 npoint 256 integ    16 sigma    1.158 bsw 0
                        # 0      1        2     3        4       5        6     7     8      9     10
                        #   11    12  13   14      15     16  17       18 19       20    21  22

                        ####fileReadLine = fileRead.readline()
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
                        '''



                        # if first sample of this file
                        if not samplesQtyFile:
                            # begin a new fileWriteNameThis file with header
                            #fileWriteSamplesQty = 0

                            # if old data file open, close it
                            #if len(fileWriteNameThis):
                            #    fileWrite.close() 

                            #fileWriteName = fileReadName + '.txt'
                            fileWriteName = fileReadName[:-4] + '.txt'
                            print(fileWriteName)

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
                            #fileWrite.write('from ' + pgmRev  \
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
                                'from ' + pgmRev \
                                + '\nlat {:g} long {:g} amsl {:g} name '.format( \
                                sdrQthLat, sdrQthLon, sdrQthAmsl) \
                                + sdrQthName \
                                + '\nfreqMin {:g} freqMax {:g} freqBinQty {:d}'.format( \
                                dataFreqMin, dataFreqMax, freqBinQty) \
                                + '\naz {:g} el {:g}'.format(azimuthThis, elevationThis) \
                                + '\n# times are in UTC\n')

                            azimuthLast   = azimuthThis
                            elevationLast = elevationThis

                        elif azimuthThis != azimuthLast or elevationThis != elevationLast:
                            fileWrite.write('az {:g} el {:g}\n'.format(azimuthThis, elevationThis))
                            azimuthLast   = azimuthThis
                            elevationLast = elevationThis

                        '''
                        if feedRefOnThis:
                            dataFlagsS = ' C\n'
                            refQty += 1
                        else:
                            dataFlagsS = ' \n'
                        '''
                        dataFlagsS = ' \n'

                        # write data line
                        # dataTimeUtcThis = Time(thisLine[1], format='yday', scale='utc')
                        # Time('2000-01-01 02:03:04', out_subfmt='date_hms').iso
                        #   '2000-01-01 02:03:04.000'




                        ####timeStampS = dataTimeUtcThis.strftime('%Y-%m-%dT%H:%M:%S ')
                        # timeStampS = '2022-12-22T21:19:49 '





                        print()
                        #print('time stamp =', timeStampS[:-1])
                        #print('filename =', fileNameS)
                        #print('file sample =', fileSample)
                        #print(timeStampS[:-1], '          ', fileNameS, '         ', fileSample)
                        print(samplesQty, '    ', timeStampS, '    ', fileWriteName, '   ', samplesQtyFile, \
                            dataFlagsS[:-1])


                        #print(' len(thisLine[6:]) =', len(thisLine[6:]))

                        #fileWrite.write(timeStampS + ' '.join('{:.9g}'.format(i) for i in data) + dataFlagsS)
                        ####fileWrite.write(timeStampS + ' '.join(thisLine) + dataFlagsS)
                        #########fileWrite.write(timeStampS + ' '.join(thisLine[6:]) + dataFlagsS)

                        #fileData = np.array(list(map(float, thisLine[6:]))) + 100.
                        #print(' fileData')
                        #print(fileData)
                        #fileDataS = np.array_str(fileData, precision=8, suppress_small=True)
                        #fileDataS = ' '.join(str(x) for x in fileData)
                        fileDataS = ' '.join(str(float(x) + 100.) for x in thisLine[6:])
                        #print(' fileDataS =', fileDataS, '=')
                        #fileWrite.write(timeStampS + fileDataS + ' ' + dataFlagsS)
                        fileWrite.write(timeStampS + fileDataS + '\n')

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
    #for directoryCtr in range(directoryListLen):

    # blank out the last filename
    print('\r                                                                              ' \
        + '                                                                                ')
    #print('\r samplesFileQty =', samplesFileQty, \
    #    '                                                                                              ')

    print(' Total           samples read   =', samplesQty)
    print(' Total reference samples read   =', refQty)
    print()

    if not samplesQty:
        print()
        print()
        print(" ========== FATAL ERROR: no data loaded from files")
        print()
        print()
        print()
        exit()

    ###################################################################################

if __name__ == "__main__":
    main()

