programName = 'ezCon250711a.py'
programRevision = programName

# ezRA - Easy Radio Astronomy ezCon Data CONdenser program,
#   CONdense one or more frequency spectrum data .txt files into
#   one .ezb text data file, and perhaps GALaxy *Gal.npz and *GLon.npz data files.
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
#   dataTimeUtcVlsr2000.mjd = 51544.0
#   add antXTVTCmDop to ezCon191 ?

# ezCon250711a, cmdLineSplit ezConGalCrossingGLonCenter can be float
# ezCon250703a, dataFileIdx, plotEzCon201ZantFileIndex(), studyOutString improvements
# ezCon250522a, ezConRawFreqBinHideLDo() hide with freqBin neighbor having lowest average,
#   -ezDefaultsEnd, added 300 to ezConPlotAllL
# ezCon250409a, corrected RaHThis and DecDegThis to raHThis and decDegThis
# ezCon250329a, *Gal.npz file definition from here, ezCon's writeFileGal()
# ezCon250326a, column 9 AntXTVTCmDop Center-of-Mass of the Doppler shift,
#   code from old ezCon220823a,
#   now officially defined in ezbMenu: AzimuthDeg, ElevationDeg, and AntXTVTCmDop as columns 7, 8, and 9
#   plotEzCon198azimuth()   renamed plotEzCon107azimuth()      for azimuthDeg,
#   plotEzCon199elevation() renamed plotEzCon108elevation()    for elevationDeg,
#   new ........................... plotEzCon109antXTVTCmDop() for antXTVTCmDop
# ezCon250323a, Python 3.13 or new Astropy demands locBaseValid flag,
#   dataTimeUtcThis typo in glatdeg
# ezCon250312a, if ezCon087Csv is 2 then downsample antXTVTCsv before ifAvg format files
# ezCon250303a, writeFileGalRaDecNear() remember gLon in RGal.npz,
#   ring bell upon error exit (to alert operator during batch file runs)
# ezCon250302a, -ezConGalRaDecNearNearL for M31 extragalactic study, creates RGal.npz
# ezCon250124b, ezCon087Csv swap X and Y
# ezCon250124a, -ezConAntXTVTSmooth
# ezCon250123b, ezConAntXTVTSmoothDo()
# ezCon250123a, ezConAntXTVTSmoothDo()
# ezCon250122d, -ezCon087Csv 1 ezCon087antRBTVTMsh.csv
# ezCon250122c, -ezCon087Csv 1 ezCon087antRBTVTMsh.csv
# ezCon250122b, -ezCon087Csv 2 dirOut = plotName
# ezCon250122a, average into fewer ifAvg format files
# ezCon250121a, -ezCon087Csv 2 to also write out ezCon087 as one directory of ifAvg format files
# ezCon241024a, writeFileGLon() to before del antXTVT
# ezCon241021a, -ezCon087Csv plot scales
# ezCon241019ax, -ezCon087Csv
#   to see AntRB, to disable TVT, use -ezConAntXTFreqBinsFracL 0 1 -ezConUseVlsr 0 -ezConAntXTVTFreqBinsFracL 0 1
#       python3 ../ezRA/ezCon241019ax.py data/LTO16230416_00.txt -ezConPlotRangeL 87 87  -ezConAntXInput 6
#           -ezConAntXTFreqBinsFracL 0 1  -ezConUseVlsr 0  -ezConAntXTVTFreqBinsFracL 0 1  -ezCon087Csv 1 
#       created 72MB ezCon087antRBTVT.csv file
#   https://www.rinearn.com/en-us/graph3d/guide/launch
#   then in the directory of the 220K RinearnGraph3D.jar file,
#       java -jar RinearnGraph3D.jar
#           and 20 seconds to render 3d plot of 24-hour 3,932 Ant samples
#   sudo cp -r rinearn_graph_3d_5_6_36b_en /usr/local/bin
#   sudo chmod +x /usr/local/bin/rinearn_graph_3d_5_6_36b_en/rinearn_graph_3d_5_6_36b_en/bin/ring3d
#   ls -lh /usr/local/bin/rinearn_graph_3d_5_6_36b_en/rinearn_graph_3d_5_6_36b_en/bin/ring3d
#   nano ~/.bashrc
#       and add
#   export PATH="$PATH:/usr/local/bin/rinearn_graph_3d_5_6_36b_en/rinearn_graph_3d_5_6_36b_en/bin/"
#   log out and log in
#   now command line
#       ring3d --help
#   or command line
#       ring3d --version
#           RINEARN Graph 3D Ver.5.6.36
#   or command line
#       ring3d ezCon087antRBTVT.csv 
#   or command line
#       ring3d ezCon087antRBTVT.csv --overwrite --saveimg ezCon087antRBTVTCsv.png --quit
#   or command line
#       ring3d
# ezCon241018bx, for 3d plots with https://www.rinearn.com/en-us/
#   ezCon087 antXTVT to a .csv file
# ezCon240811a, -ezConAntXTVTFixL to -ezConAntXTVTLevelL
# ezCon240809b, more of "plot if plotNumber not in ezConPlotRequestedL: return(1)"
# ezCon240809a, -ezConAntXTVTFixL hidden in help
#   from ezCon240725a support multiple -ezConPlotRangeL,
#   plot if plotNumber in ezConPlotRequestedL
# ezCon240803a, -ezConAntXTVTFixL
# ezCon240802a, -ezConAntXMult
# ezCon240730a, yTickHeatL and ezCon0* y scale for 10 MHz Airspy
# ezCon240724a, ezCon0* y scale for 10 MHz Airspy
# ezCon240723a, ezCon0* y scale for 10 MHz Airspy
# ezCon240615b, frequency study % warnings also to AntXT
# ezCon240615a, frequency studies to near bottom of ezConStudy file using OutFreqString
# ezCon240613a, dusting
# ezCon240610a, Doppler to Yscale of ezCon382,
#   added to studyOutString for top of ezConStudy file
# ezCon240609b, remove "Bin" from all plot filenames
# ezCon240609a, dusting,
#   ezCon088antBTVTByFreqBinAllFall.png    to ezCon088antBTVTByFreqBinAvgFall.png (name change),
#   ezCon098antBTVTMaxByFreqBinAllFall.png to ezCon098antBTVTByFreqBinMaxFall.png (name change),
#   ezCon388antBTVTByFreqBinAll.png        to ezCon388antBTVTByFreqBinAvgAll.png  (name change),
#   ezCon397antBTVTMaxByFreqBin.png        to ezCon397antBTVTByFreqBinMax.png     (name change),
#   ezCon398antBTVTMaxByFreqBinAll.png     to ezCon398antBTVTByFreqBinMaxAll.png  (name change),
#   ezCon198azimuthDeg.png                 to ezCon198azimuth.png                 (name change),
#   ezCon392antXTVByFreqBinMax.png         to ezCon393antXTVByFreqBinMax.png      (number change),
#   plotCountdown -= 1 in ezCon690,
#   ezCon690GLonDegP180_nnnByFreqBinAvg.png to
#       to 'ezCon690_nnnGLonDegPnnnByFreqBinAvg.png'
#       or 'ezCon690_nnnGLonDegMnnnByFreqBinAvg.png'
#   plotEzCon690gLonDegP180_nnnByFreqBinAvg() to plotEzCon690gLonDegByFreqAvg()
# ezCon240603b, dusting
# ezCon240603a, spectrum fractions to ezCon382
# ezCon240601a, dusting
# ezCon240420a, wallLTO horizon, azDeg bug and capitalization
# ezCon240420a, wallLTO horizon, azDeg bug and capitalization
# ezCon240419a, sys.version
# ezCon240412b, dusting
# ezCon240412a, ezCon088 and antXTVTDLen = min(antLen, antXTVTDLenMax) for less than 100 samples
# ezCon240308a, dusting
# ezCon240225b, support for negative power values,
#   -ezConInputdBm
# ezCon240225a, changed ezRA .txt file format
#       from 'az x.xx el y.yy' also support new 'azDeg x.xx elDeg y.yy',
#       and from (unposted) 'ra x.xx dec y.yy' to 'raH x.xx decDeg y.yy',
#       and from (unposted) 'glat y.yy glon x.xx' to 'gLatDeg y.yy gLonDeg x.xx',
#       so will need updates to ezCon240219b.py and ezColGNSM240219d.py,
#   dropping support for 'c' (Calibration) last data word
# ezCon240219b, support negative power values
# ezCon240219a, with ezColGNSM why AntXTVT inverted ?  Due to negative power values, antXUsedMin,
#   ezConUseSubRef to ezConUseRefSub to match ezCol
# ezCon240204b, explore poor ezSky405 and ezSky505 images
#   data/Skynet_60333_barnard_33-nb_107271_56634.A.cal.txt says in part:
#     #UTC_Time(s)   Ra(deg)  Dec(deg)   Az(deg)   El(deg)        XX1        YY1        XX2        YY2  Cal   Sweeps 
#     11992.000000  83.06220   -4.6685  193.4920   45.8379   136.3469   137.4065   123.8188   148.3731  -1    0  0 
#
#   data/Skynet_60333_barnard_33-nb_107271_56634.A.cal5Az.txt says in part:
#     from ezColGB20m240203a.py
#     lat 38.4368 long -79.8255 amsl 853 name GB20m
#     freqMin 1406.26 freqMax 1421.88 freqBinQty 256
#     #UTC_Time(s)   Ra(deg)  Dec(deg)   Az(deg)   El(deg)        XX1        YY1        XX2        YY2  Cal   Sweeps 
#     az 193.492 el 45.8381
#     2024-01-24T03:19:54.415924 135.4985 135.4985 135.4985 ...
#
#   data/Skynet_60333_barnard_33-nb_107271_56634.A.cal5Ra.txt says in part:
#     from ezColGB20m240203a.py
#     lat 38.4368 long -79.8255 amsl 853 name GB20m
#     freqMin 1406.26 freqMax 1421.88 freqBinQty 256
#     #UTC_Time(s)   Ra(deg)  Dec(deg)   Az(deg)   El(deg)        XX1        YY1        XX2        YY2  Cal   Sweeps 
#     ra 5.53815 dec -4.6683
#     2024-01-24T03:19:54.415924 135.4985 135.4985 135.4985 ...
#
#   Skynet_60333_barnard_33-nb_107271_56634.A.cal5Ra.ezb says in part:
#     #   from ezCon240202a.py
#     #   ../ezRA/ezCon240202a.py  data/Skynet_60333_barnard_33-nb_107271_56634.A.cal5Az.txt  -ezConPlotRangeL  191  191
#     lat 38.4368 long -79.8255 amsl 853.0 name GB20m
#     freqMin 1406.26 freqMax 1421.88 freqBinQty 256
#     ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  Spare1  Spare2  AntXCMDop    AntAvg  AntMax    RefAvg  RefMax    AntBAvg  AntBMax    #   AntRBAvg  AntRBMax    AntBTVTAvg  AntBTVTMax
#     #          0           1    2       3        4        5     6      7       8       9            10      11        12      13        14       15         16        17          18           19
#     60333.13882 5.581 -4.859 -19.223 -151.516 3.494e+01 1 193.5 45.8 0.00000e+00 1.35498e+02 1.35499e+02 1.35498e+02 1.35499e+02 1.00000e+00 1.00000e+00 1.00000e+00 1.00000e+00 1.00000e+00 1.00000e+00
#   ... and yet, even with 5-fractional-digit-precision output from ezColGB20m,
#       Skynet_60333_barnard_33-nb_107271_56634.A.cal.txt gives differing X and Y use limits
#       in ezSky405 plots when using GM20m AzEl vs RaDec coordinate columns !
# ezCon240204a, explore astropy azEl to raDec to azEl to raDec to azEl dithering, = good
# ezCon240203a, "ra" line input to dataRightAscensionH
# ezCon240202a, "ra" line input
# ezCon240131b,
#   azimuth, elevation to azimuthDeg, elevationDeg,
#   ezConAstroMath == 2:
#       "ra"   line input
#       "glat" line input
#   dusting
# ezCon240131a, support .txt files with any sky coordinate type,
#       az 227.9 el 42.7
#       ra 22.9 decl 42.7
#       glat 42.7 glon 227.9
#   dataAzimuth, dataElevation, dataElevationRef to dataAzimuthDeg, dataElevationDeg, dataElevationRefDeg
# ezCon240108a, ezCon191 Ant to AntXTVT top-bottom order reversed
# ezCon240107a, Copyright (c) 2024
# ezCon240106b, fixed some Pluck routines
# ezCon240106a, fixed some Pluck routines
# ezCon240105b.py, ezConAntSamplePluck to ezConAntPluck,
#   fixed some Pluck routines
# ezCon240105a.py, dusting, added HH:MM to studyTime() OutString
# ezCon240104a.py, "Snip" might mean shorten, so replaced almost all "Snip" with "Pluck",
#   like   -ezConAntXTVTMaxPluckQtyL and -ezConAntXTVTAvgPluckQtyL,
#   added  -ezConAntXTVTMaxPluckValL and -ezConAntXTVTAvgPluckValL and -ezConAntXTVTPluck,
#   revised ezConAntXTVTMaxPluckDo() and  ezConAntXTVTAvgPluckDo() and  ezConAntXTVTPluckDo(),
#   removed "rawLen-refQty ="
# ezCon240101a.py, ezConAntXTVTMaxSnipQtyL before ezConAntXTVTAvgSnipQtyL,
#   antLen ?= rawLen-refQty
# ezCon231231a.py, fileRawLen
# ezCon231213b.py, plot antXTV and antXTVT after filtering antXTVT
# ezCon231213a.py, ezCon098 and ezCon398 'Downsampled by Maxing',
#   removed dead ezCon386
# ezCon231212c.py, per Ted's Oct 18, 2023 at 8:14 PM email,
#   ezCon511 renamed to ezCon519, to align with the future ezGal519,
#   ezCon521 renamed to ezCon529, to align with the future ezGal529,
#   ezCon560 renamed to ezCon800, to avoid alignment with the ezGal560 Galactic angular velocity plot,
#   ezCon382 now FreqBin increases down
# ezCon231212b.py, continued,
#   ezCon386 to ezCon088antXTVTByFreqBinAllFall    Spectra, Downsampled by Averaging with Time Increasing Down
#               ezCon098antXTVTMaxByFreqBinAllFall Spectra, Downsampled by Averaging with Time Increasing Down
#   ezCon382 to ezCon383antXTVByFreqBinAvg
#   ezCon388 to ezCon382antXTByFreqBinAvgRfi
#   ezCon389 to ezCon388antXTVTByFreqBinAll    Spectra, Downsampled by Averaging
#   ezCon397 to ezCon397antXTVTMaxByFreqBin
#               ezCon398antXTVTMaxByFreqBinAll Spectra, Downsampled by Averaging
# ezCon231212a.py, continued
# ezCon231211b.py, continued
# ezCon231211a.py, 
#   -ezConAntXTVTAvgSnipQtyL,
#   -ezConAntXTVTMaxSnipQtyL
# ezCon231210a.py, 
#   ezCon386 AntXTVT Spectra, Downsampled by Averaging with Time Increasing Up
#   ezCon389 AntXTVT Spectra, Downsampled by Averaging
# ezCon231209a.py, ezConAstroMath default to 1 (seems to work for me)
#   ezSky200 AntXTVT violet needs      best contrast, use green
#   ezSky200 AntB           needs next best contrast, use red
#       AntXTVT violet   becomes newgreen
#       Ref     red      becomes violet
#       AntB    green    becomes red
#               newgreen becomes green
# ezCon231202a.py, ezCon389 had ezCon398 typo
# ezCon231108a.py, hid help of (unfinished??) -ezConUseSubRef,
#   ezCon389antXTVTByFreqBinAll(),
#   ezCon392antXTVByFreqBinMax()
# ezCon231002a.py, -ezConUseSubRef
# ezCon230824a.py, print ezConPlotRangeL in printGoodbye(),
#   trouble using -ezConAntAvgSnipQtyL so always create xTickLabelsHeatAntL
# ezCon230820a.py, removed 'Galaxy plane' from ezCon520 ezCon521 and ezCon690
# ezCon230817c.py, ezCon337 and ezCon357 filenames from Avg to Max
#   ezCon191 plt.yticks from GLatDeg to GLat
# ezCon230806b.py, ezCon399SignalSampleByFreqBinL
# ezCon230806a.py, ezCon399SignalSampleByFreqBinL
# ezCon230728a.py, extracted ezConAntSampleSnipL from
#   ezConAntSamplesUseLDo() into new last Ant filter ezConAntSampleSnipLDo()
# ezCon230629a.py, removed ezConGalCrossingGLatCenterSnap and ezConGalCrossingGLonCenterSnap,
#   output filenames *Nxx.xGal.npz and *Pxx.xGal.npz,
#   output filenames *Nxxx.xGLon.npz and *Pxxx.xGLon.npz
# ezCon230628a.py,
#   ezConGalCrossingGLatCenterL and ezConGalCrossingGLatNear and
#   ezConGalCrossingGLonCenterL and ezConGalCrossingGLonNear are now all floats,
#   but ezConGalCrossingGLonCenterSnap and ezConGalCrossingGLonCenterSnap are integers
# ezCon230627a.py,
# ezCon230625a.py, ezConGalCrossingGLat duplicated with ezConGalCrossingGLatNear
#   added ezConGalCrossingGLonNear and ezConGalCrossingGLonCenterL
# ezCon230624a.py, ezConGalCrossingGLatCenterL to int degrees
#   output filenames *NxxGal.npz and *PxxGal.npz
# ezCon230623a.py, ezConGalCrossingGLatCenterL internally, and -ezConGalCrossingGLatCenterL,
#   output filenames *Nxx.xGal.npz and *Pxx.xGal.npz
# ezCon230610a.py, ezConGalCrossingGLatCenter help typo
# ezCon230603a.py, 'Doppler MHz from' only with samples from Ant
# ezCon230527a.py, ezConGalCrossingGLatCenter, gLatDegThis now a float,
#   ezCon027 no longer says 'Ref:  Doppler MHz from 1420.400 MHz'
# ezCon230410a.py, ezConVelGLonEdgeLevel, ezConGalCrossingGLat
# ezCon230408a.py, commented ezConVelGLonEdgeLevel
# ezCon230407a.py, ezCon105 "receding Velocity of the Local Standard of Rest (VLSR)"
# ezCon230406a.py, -eX
# ezCon230401a.py, from AntXTV changed to AntXTVT into velGLonP180[,],
#   added antXTVTName=antXNameL[1]+'TVT' to *Gal.npz file
# ezCon230323a.py, more ezCon082antXTV formula comments
# ezCon230316c.py, different gst() to fix ezConAstroMath=1 right ascension, fixed -eX
# ezCon230316b.py, ezConAstroMath=1 right ascension
# ezCon230316a.py, ezCon082antXTV formula comments, -eX
# ezCon230314a.py, more AntX choices and improved names and separate filenames,
#   ezConAntXTFreqBinsFracL and ezConAntXTVTFreqBinsFracL defaults
# ezCon230313c.py, ezConAstroMath=1 right ascension
# ezCon230313b.py, ezConAstroMath=1 right ascension
# ezCon230313a.py, ezConAstroMath=1 right ascension
# ezCon230311a.py, commented VLSR prints
# ezCon230310a.py, ezConAstroMath=2 VLSR
# ezCon230309a.py, ezConAstroMath=2 VLSR was Barycentric radial velocity only,
# ezCon230305a.py, boilerplate from ezSky
# ezCon230304a.py, help: 'remove' to 'ignore'
# ezCon230303a.py, improved ezConAntFreqBinSmooth help and comments
# ezCon230302a.py, freqBin study to plotEzCon307antByFreqBinAvg() and plotEzCon327refByFreqBinAvg(),
#   always plotCountdown-=1, print plotting {plotName} only if intending to plot
# ezCon230301a.py, ezConAntAvgSnipNumL to ezConAntAvgSnipQtyL, ezConRefAvgSnipNumL to ezConRefAvgSnipQtyL, 
#   ezConAntAvgKeepFracL to ezConAntAvgSnipFracL, ezConRefAvgKeepFracL to ezConRefAvgSnipFracL,
#   timeUtcMjdDBetweenAnt to timeUtcMjdDBetweenAntRaw, timeUtcMjdDBetweenRef to timeUtcMjdDBetweenRefRaw
# ezCon230228a.py, ezConAntSamplesUseLDo() now forces new xTickLabelsHeatAntL
# ezCon230226e.py, antLen cleanup, works, need a VLSR
# ezCon230226d.py, ezConAntAvgSnipNumL = [] to disable
# ezCon230226d.py, ezConAntAvgKeepFracL = [] to disable
# ezCon230226c.py, update ezConRefAvgTrimFracL parts to ezConRefAvgKeepFracL
# ezCon230226b.py, update ezConRefAvgTrimFracL parts to ezConRefAvgKeepFracL
# ezCon230226a.py, ezConAntAvgTrimFracL to ezConAntAvgKeepFracL, works with "0 0.9999999",
#   ezConAntSamplesUseLDo() and ezConAntAvgKeepFracLDo() now force new xTickLocsAnt
# ezCon230225a.py, in ezConAntAvgTrimFracLDo antAvgTrimMask trimming 2 extra so change < to <=
# ezCon230223a.py, optional ezCon201GrawAntRef connecting lines for ant and ref
# ezCon230209a.py, for ezCon520velGLonPolar.png and ezCon521velGLonPolarCount.png,
#   "MatplotlibDeprecationWarning: Auto-removal of grids by pcolor() and
#   pcolormesh() is deprecated since 3.5 and will be removed two minor releases later;
#   please call grid(False) first.", so put "plt.grid(0)" in front of each "im = plt.pcolormesh("
# ezCon221202a.py, ezConAstroMath=1 calculates wrong Right Ascension values,
#   default changed to the slower ezConAstroMath=2
# ezCon221126a.py, if not start with '-ezCon', allow unrecognized words on command line
# ezCon221125a.py, to ezCon690gLonDegP180_nnnByFreqBinAvg, and to X axis using -byFreqBinX
# ezCon221122a.py, ezCon560antXTVTMaxIdxGLon
# ezCon221121a.py, avoid div by 0 when creating antRA,
#   create antRA only once
# ezCon221118a.py, "Galaxy Crossing" to "Galaxy Plane"
# ezCon221116a.py, add ezCon317, ezCon337, ezCon357, ezCon377, and ezCon397
# ezCon221112a.py, help typo
# ezCon221111a.py, experimentEzc for AzEl into .ezb Spare1 and Spare2,
#   commented openFileSdre() and writeFileSdre(),
#   fixed 'FATAL ERROR:  ezRAObsLon' typo
# ezCon221027a.py, "ezRAObsLat = -999.0 is silly" testing to later
# ezCon221017a.py, tilted xlabel
# ezCon221016a.py, renamed ezCon5xx to match ezGal5xx, polishing
# ezCon221015b.py, removed many global from main()
#   Required:  -90 <= ezRAObsLat <= +90
#   Required: -180 <= ezRAObsLon <= +180
# ezCon221015a.py, from skipped ezCon220927a.py,
#   ezCon220927a, add a thin black horizontal line at zero Doppler on ezCon082antXTV,
#   print status polishing,
#   ezCon220924a, add (unique?) 5-character column string (' 33333') into ezConStudyxxx.txt for
#   easy section searching,
# ezCon221013a.py, allow division by data1dSpanD100, commas to prints
# ezCon220930a.py, prep for Git
# ezCon220917a, polishing, max of 19 thin black vertical lines to plotEzCon191sigProg,
#  raw sample number to input file map to studyOutString to ezConStudy*.txt


import seaborn as sb    # heatmaps

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from astropy.time import Time

import numpy as np
import math
#import datetime
from datetime import datetime, timezone
import os
import sys
import time



def printUsage():

    print()
    print()
    print('##############################################################################################')
    print()
    print('USAGE:')
    print('  Windows:   py      ezCon.py [optional arguments] radioDataFileDirectories')
    print('  Linux:     python3 ezCon.py [optional arguments] radioDataFileDirectories')
    print()
    print('  Easy Radio Astronomy (ezRA) ezCon data Condenser program')
    print('  to read ezCol format .txt radio data file(s),')
    print('  analyse them, optionally creating many .png plot files,')
    print('  and maybe write one Gal.npz Galaxy crossing velocity data file.')
    print()
    print('  "radioDataFileDirectories" may be one or more .txt radio data files:')
    print('         py  ezCon.py  bigDish220320_05.txt')
    print('         py  ezCon.py  bigDish220320_05.txt bigDish220321_00.txt')
    print('         py  ezCon.py  bigDish22032*.txt')
    print('  "radioDataFileDirectories" may be one or more directories:')
    print('         py  ezCon.py  bigDish2203')
    print('         py  ezCon.py  bigDish2203 bigDish2204')
    print('         py  ezCon.py  bigDish22*')
    print('  "radioDataFileDirectories" may be a mix of .txt radio data files and directories')
    print()
    print('  Arguments and "radioDataFileDirectories" may be in any mixed order.')
    print()
    print('  Arguments are read first from inside the ezCon program,')
    print("  then in order from the ezDefaults.txt in the ezCon.py's directory,")
    print('  then in order from the ezDefaults.txt in current directory,')
    print('  then in order from the command line.  For duplicates, last read wins.')
    print()
    print('EXAMPLES:')
    print()
    print('  py ezCon.py -help                  (print this help)')
    print('  py ezCon.py -h                     (print this help)')
    print()
    print('    -ezRAObsName   Lebanon Kansas    (Observatory Name)')
    print('    -ezRAObsLat    39.8282           (Observatory Latitude  (degrees))')
    print('    -ezRAObsLon    -98.5696          (Observatory Longitude (degrees))')
    print('    -ezRAObsAmsl   563.88            (Observatory Above Mean Sea Level (meters))')
    print()
    print("    -ezConAzimuth         180.4      (simulate data file's recorded Azimuth   (degrees)")
    print("    -ezConElevation       35.7       (simulate data file's recorded Elevation (degrees)")
    print("    -ezConAddAzDeg        9.4        (add to data file's recorded Azimuth   (degrees))")
    print("    -ezConAddElDeg        -2.6       (add to data file's recorded Elevation (degrees))")
    print()
    print('    -ezConInputdBm        1          (interpret power values as dBm (dB of 1 milliwatt)')
    print()
    print('    -ezConRawSamplesUseL  0 100      (first Raw Sample number    last Raw Sample number)')
    #print('    -ezConRawSamplePluck    29        ( Raw Sample number)')
    #print('    -ezConRawAvgTrimFracL  .01  .98')
    #print('         (trim Raw samples with RawAvg values outside low high (as fractions of sorted rawLen))')
    print('    -ezConRawFreqBinHide  129        (hide Raw freqBin 129 by copying from freqBin 128)')
    #print('    -ezConRawFreqBinSmooth 1,1       ',
    #    '(RFI spur limiter: maximum muliplier over 4 neighboring freqBin of same Raw sample)')
    print()
    print('    -ezConRefMode 1                  (Dicke Reference sample creation method, default = 10)')
    print('      -ezConRefMode N < 0: REF = spectrum from -Nth ANT sample')
    print('      -ezConRefMode -1403: REF = spectrum from ANT sample number 1403')
    print('      -ezConRefMode     0: REF = spectrum from first ANT sample, number 0')
    print('      -ezConRefMode     1: REF = 1.0 (no REF, neutral spectrum)')
    print('      -ezConRefMode     2: REF = spectrum from rawByFreqBinAvg spectrum average')
    print('      -ezConRefMode    10: REF = last REF sample marked in data, if none will use sample 0')
    #print('      -ezConRefMode    20: REF detection by ezCon software (for refPulser hardware)')
    print()
    print('    -ezConAntSamplesUseL    25   102  (first Ant Sample number    last Ant Sample number)')
    print('    -ezConAntPluck          29        (Pluck (ignore) Ant Sample number)')
    print('    -ezConAntAvgPluckQtyL    3    5')
    print('         (Pluck (ignore) Ant samples with the 3 Quantity lowest, and 5 highest, sorted AntAvg values)')
    print('    -ezConAntAvgPluckFracL  .02  .03')
    print('         (Pluck (ignore) Ant samples with the lowest 2% and highest 3% AntAvg values (antLen Fractions))')
    #print('    -ezConAntFreqBinHide  129        (hide Ant freqBin 129 by copying from freqBin 128)')
    print('    -ezConAntFreqBinSmooth  1.1       ',
        '(RFI spur limiter: maximum muliplier over 4 neighboring freqBin of same Ant sample)')
    print()
    print('    -ezConRefAvgPluckQtyL    3    5')
    print('         (Pluck (ignore) Ref samples with the 3 Quantity lowest, and 5 highest, sorted RefAvg values)')
    print('    -ezConRefAvgPluckFracL  .02  .03')
    print('         (Pluck (ignore) Ref samples with the lowest 2% and highest 3% RefAvg values (antLen Fractions))')
    #print('    -ezConRefFreqBinHide  129        (hide Ref freqBin 129 by copying from freqBin 128)')
    #print('    -ezConRefFreqBinSmooth 1.1       ',
    #    '(RFI spur limiter: maximum muliplier over 4 neighboring freqBin of same Ref sample)')
    print()
#    print('    -ezConUseRefSub 1                (use Subtraction of last Reference sample, not Division)')
#    print()
    print('    -ezConAntBaselineFreqBinsFracL   0  0.2344  0.7657  1')
    print('         (AntBaseline        FreqBin bands: start stop start stop (as fractions of bandwidth))')
    print()
    print('    -ezConAntRABaselineFreqBinsFracL 0  0.2344  0.7657  1')
    print('         (AntRABaseline      FreqBin bands: start stop start stop (as fractions of bandwidth))')
    print()
    print('    -ezConAntXInput    6             '
        + '(AntX choice: default -1 for Auto, 0/2/4/5/6 for Ant/Ref/AntB/AntRA/AntRB)')
    #print('    -ezConAntXTVTLevelL  1.3  -3.2   (multiply all AntXTVT sample values and add)')
    print()
    print('    -ezConAntXTFreqBinsFracL            0.2344  0.7657')
    print('         (AntXTFreqBinsFrac FreqBin band:  start stop            (as fractions of bandwidth))')
    print()
    print('    -ezConUseVlsr      1             (use VLSR for AntXTV and further processing)')
    print()
    print('    -ezConAntXTVTFreqBinsFracL          0.4     0.6')
    print('         (AntXTVTFreqBinsFrac FreqBin band:  start stop          (as fractions of bandwidth))')
    print()
    print('    -ezConAntXTVTMaxPluckQtyL   3    5')
    print('         (Pluck (ignore) AntXTVTMax samples with the 3 Quantity lowest, and 5 highest, sorted AntXTVTMax)')
    print('    -ezConAntXTVTMaxPluckValL  .01   .03')
    print('         (Pluck (ignore) AntXTVTMax samples with Values below .01 or above .03)')
    print()
    print('    -ezConAntXTVTAvgPluckQtyL   3    5')
    print('         (Pluck (ignore) AntXTVT    samples with the 3 Quantity lowest, and 5 highest, sorted AntXTVT)')
    print('    -ezConAntXTVTAvgPluckValL  .01   .03')
    print('         (Pluck (ignore) AntXTVT    samples with Values below .01 or above .03)')
    print()
    print('    -ezConAntXTVTPluck          33')
    print('         (Pluck (ignore) AntXTVTMax and AntXTVT sample 33)')
    print()
    print('    -ezConAntXTVTSmooth         2')
    print('         (smooth antXTVT heatmap data as an image, with choice of filters)')
    print()
    print('    -ezCon087Csv         1           (create CSV file of ezCon087 for 3d plots with rinearn.com/en-us/graph3d)')
    print('    -ezCon087Csv         2           (... and also write out ezCon087 as one directory of ifAvg format files)')
    print()
    print('    -ezConPlotRangeL     0  300      (save only this range of ezCon plots to file, to save time)')
    print('    -ezConRawDispIndex   1           (also Display the Raw sample Index on x axis)')
    print('    -ezConDispGrid       1           (turn on graphical display plot grids)')
    print('    -ezConDispFreqBin    1           (1 for display FreqBin numbers on Y axis, 2 for 0.0 to 1.0)')
    print('    -ezConHeatVMinMaxL   1.0 1.4     (heat map z scale)')
    print()
    print('    -ezConAstroMath      0           (astroMath choice)')
    print('      -ezConAstroMath  0:    no math (good for faster plots of most signals, but AntXTV is wrong)')
    print('      -ezConAstroMath  1:    using math from MIT Haystack SRT')
    print('      -ezConAstroMath  2:    using math from authoritative slower AstroPy library')
    print()
    print('    -ezConVelGLonEdgeFrac         0.5    ')
    print('         (velGLon level fraction for plotEzCon430velGLonEdges)')
    #print('    -ezConVelGLonEdgeLevel  0.5    ')
    #print('         (velGLon level for plotEzCon430velGLonEdges, if 0 then use only ezConVelGLonEdgeFrac)')
    print()
    print('    -ezConGalCrossingGLatCenter   2.4')
    print('         (add spectra to Gal.npz, the center of GLat crossing, in Galactic Latitude degrees)')
    print('    -ezConGalCrossingGLatCenterL  -5.2  6.3  11')
    print('         (adds centers of GLat crossings in Galactic Latitude degrees, as np.linspace(-5.2, 6.3, num=11))')
    print('    -ezConGalCrossingGLatNear     2.3')
    print('         (defines "close to GLat crossing" in Galactic Latitude degrees)')
    print()
    print('    -ezConGalCrossingGLonCenter   72.4')
    print('         (add spectra to GLon.npz, the center of GLon crossing, in Galactic Longitude degrees)')
    print('    -ezConGalCrossingGLonCenterL  69.6  82.4  13')
    print('         (adds centers of GLon crossings in Galactic Longitude degrees, as np.linspace(69.6,  82.4, num=13))')
    print('    -ezConGalCrossingGLonNear     2.7')
    print('         (defines "close to GLon crossing" in Galactic Longitude degrees)')
    print()
    print('    -ezConGalRaDecNearNearL       0.8  41.3  0.1  0.2')
    print('         (add spectra to RGal.npz, from RaDec span 0.8 +/-0.1 hours, 41.3 +/-0.2 degrees)')
    print()
    print('    -ezCon399SignalSampleByFreqBinL     18  1423')
    print('         (plot antenna sample 1423 spectrum By FreqBin of signal 18 (of ezbMenu columns 10, 12, 14, 16, 18))')
    print()
    print('    -ezDefaultsFile ../bigDish8.txt     (additional file of ezRA arguments)')
    print('    -ezDefaultsEnd                      (ignore the rest of this ezDefaults file')
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

    # pip install requests
    # py -m pip install requests
    import requests
    url = 'url goes here'
    url = 'https://www.wunderground.com/dashboard/pws/KCOBERTH176/table/2025-07-3/2025-07-3/daily'
    r = requests.get(url)
    print(r.text)  

    #with open('/path/to/file.txt', 'w', encoding='utf-8') as f:
    #    f.write('r.text')
    with open('file.txt', 'w', encoding='utf-8') as f:
        f.write(r.text)





    exit()



def printHello():

    global programRevision          # string
    global commandString            # string

    print()
    print('         For help, run')
    print('            ezCon.py -help')

    print()
    print('=================================================')
    print(' Local time =', time.asctime(time.localtime()))
    print(' programRevision =', programRevision)
    print()

    commandString = '  '.join(sys.argv)
    print(' This Python command = ' + commandString)



def ezConArgumentsFile(ezDefaultsFileNameInput):
    # process arguments from file

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezConAzimuth                     # float - force Azimuth   (Degrees)
    global ezConElevation                   # float - force Elevation (Degrees)
    global ezConAddAzDeg                    # float - correction factor, add to file's Azimuth   (Degrees)
    global ezConAddElDeg                    # float - correction factor, add to file's Elevation (Degrees)

    global ezConInputdBm                    # integer
    global ezConUseRefSub                   # integer
    global ezConAntXInput                   # integer
    global ezConUseVlsr                     # integer

    global ezConRawSamplesUseL              # integer list
    global ezConRawFreqBinHideL             # integer list

    global ezConAntSamplesUseL              # integer list
    global ezConAntPluckL                   # integer list
    global ezConAntAvgPluckQtyL             # integer list
    global ezConAntAvgPluckFracL            # float list
    global ezConAntFreqBinSmooth            # float - RFI spur limiter: max muliplier over 4 neighboring freqBin

    global ezConRefAvgPluckQtyL             # integer list
    global ezConRefAvgPluckFracL            # float list
    global ezConRefMode                     # integer

    global ezConAntBaselineFreqBinsFracL    # float list
    global ezConAntRABaselineFreqBinsFracL  # float list
    global ezConAntXTFreqBinsFracL          # float list
    global ezConAntXTVTFreqBinsFracL        # float list

    global ezConAntXTVTMaxPluckQtyL         # integer list
    global ezConAntXTVTMaxPluckValL         # float list
    global ezConAntXTVTAvgPluckQtyL         # integer list
    global ezConAntXTVTAvgPluckValL         # float list
    global ezConAntXTVTPluckL               # integer list
    global ezConAntXTVTSmooth               # integer
    global ezCon087Csv                      # integer
    global ezConAntXTVTLevelL               # float list

    global ezCon399SignalSampleByFreqBinL   # integer list
    global ezConHeatVMinMaxL                # float list

    global ezConAstroMath                   # integer

    global ezConDispGrid                    # integer
    global ezConDispFreqBin                 # integer
    global ezConRawDispIndex                # integer
    global ezConPlotRangeL                  # integer list

    global ezConVelGLonEdgeFrac             # float
    #global ezConVelGLonEdgeLevel            # float

    global ezConGalCrossingGLatCenterL      # float list
    global ezConGalCrossingGLatNear         # float
    global ezConGalCrossingGLonCenterL      # float list
    global ezConGalCrossingGLonNear         # float
    global ezConGalRaDecNearNearL           # float list

    print()
    print('   ezConArgumentsFile(' + ezDefaultsFileNameInput + ') ===============')

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
            elif thisLine0Lower == '-ezConInputdBm'.lower():
                ezConInputdBm = int(thisLine[1])

            elif thisLine0Lower == '-ezConUseRefSub'.lower():
                ezConUseRefSub = int(thisLine[1])

            elif thisLine0Lower == '-ezConAntXInput'.lower():
                ezConAntXInput = int(thisLine[1])

            elif thisLine0Lower == '-ezConUseVlsr'.lower():
                ezConUseVlsr = int(thisLine[1])

            elif thisLine0Lower == '-ezConRawDispIndex'.lower():
                ezConRawDispIndex = int(thisLine[1])

            elif thisLine0Lower == '-ezConDispGrid'.lower():
                ezConDispGrid = int(thisLine[1])

            elif thisLine0Lower == '-ezConDispFreqBin'.lower():
                ezConDispFreqBin = int(thisLine[1])

            elif thisLine0Lower == '-ezConAstroMath'.lower():
                ezConAstroMath = int(thisLine[1])

            elif thisLine0Lower == '-ezConRefMode'.lower():
                ezConRefMode = int(thisLine[1])

            elif thisLine0Lower == '-ezConAntPluck'.lower():
                ezConAntPluckL.append(int(thisLine[1]))


            # float arguments:
            elif thisLine0Lower == '-ezConAzimuth'.lower():
                ezConAzimuth = float(thisLine[1])
            elif thisLine0Lower == '-ezConElevation'.lower():
                ezConElevation = float(thisLine[1])
            elif thisLine0Lower == '-ezConAddAzDeg'.lower():
                ezConAddAzDeg = float(thisLine[1])
            elif thisLine0Lower == '-ezConAddElDeg'.lower():
                ezConAddElDeg = float(thisLine[1])

            elif thisLine0Lower == '-ezConAntFreqBinSmooth'.lower():
                ezConAntFreqBinSmooth = float(thisLine[1])

            elif thisLine0Lower == '-ezConGalCrossingGLatCenter'.lower():
                #ezConGalCrossingGLatCenterL.append(int(thisLine[1]))
                ezConGalCrossingGLatCenterL += [float(thisLine[1])]

            elif thisLine0Lower == '-ezConGalCrossingGLatCenterL'.lower():
                ezConGalCrossingGLatCenterL += np.linspace(float(thisLine[1]), float(thisLine[2]), num=int(thisLine[3])).tolist()
                #ezConGalCrossingGLatCenterL += range(int(thisLine[1]), int(thisLine[2]))

            # grandfather -ezConGalCrossingGLat as -ezConGalCrossingGLatNear
            elif thisLine0Lower == '-ezConGalCrossingGLat'.lower():
                ezConGalCrossingGLatNear = float(thisLine[1])

            elif thisLine0Lower == '-ezConGalCrossingGLatNear'.lower():
                ezConGalCrossingGLatNear = float(thisLine[1])


            elif thisLine0Lower == '-ezConGalCrossingGLonCenter'.lower():
                #ezConGalCrossingGLonCenterL.append(int(thisLine[1]))
                ezConGalCrossingGLonCenterL += [float(thisLine[1])]

            elif thisLine0Lower == '-ezConGalCrossingGLonCenterL'.lower():
                ezConGalCrossingGLonCenterL += np.linspace(float(thisLine[1]), float(thisLine[2]), num=int(thisLine[3])).tolist()
                #ezConGalCrossingGLonCenterL += range(int(thisLine[1]), int(thisLine[2]))

            elif thisLine0Lower == '-ezConGalCrossingGLonNear'.lower():
                ezConGalCrossingGLonNear = float(thisLine[1])


            elif thisLine0Lower == '-ezConVelGLonEdgeFrac'.lower():
                ezConVelGLonEdgeFrac = float(thisLine[1])

            #elif thisLine0Lower == '-ezConVelGLonEdgeLevel'.lower():
            #    ezConVelGLonEdgeLevel = float(thisLine[1])


            # list arguments:
            elif thisLine0Lower == '-ezConRawFreqBinHide'.lower():
                ezConRawFreqBinHideL.append(int(thisLine[1]))

            elif thisLine0Lower == '-ezConRawSamplesUseL'.lower():
                ezConRawSamplesUseL.append(int(thisLine[1]))
                ezConRawSamplesUseL.append(int(thisLine[2]))

            elif thisLine0Lower == '-ezConAntSamplesUseL'.lower():
                ezConAntSamplesUseL.append(int(thisLine[1]))
                ezConAntSamplesUseL.append(int(thisLine[2]))

            elif thisLine0Lower == '-ezConAntAvgPluckQtyL'.lower():
                ezConAntAvgPluckQtyL.append(int(thisLine[1]))
                ezConAntAvgPluckQtyL.append(int(thisLine[2]))

            elif thisLine0Lower == '-ezConAntAvgPluckFracL'.lower():
                ezConAntAvgPluckFracL.append(float(thisLine[1]))
                ezConAntAvgPluckFracL.append(float(thisLine[2]))

            elif thisLine0Lower == '-ezConRefAvgPluckQtyL'.lower():
                ezConRefAvgPluckQtyL.append(int(thisLine[1]))
                ezConRefAvgPluckQtyL.append(int(thisLine[2]))

            elif thisLine0Lower == '-ezConRefAvgPluckFracL'.lower():
                ezConRefAvgPluckFracL.append(float(thisLine[1]))
                ezConRefAvgPluckFracL.append(float(thisLine[2]))

            elif thisLine0Lower == '-ezConAntBaselineFreqBinsFracL'.lower():
                ezConAntBaselineFreqBinsFracL[0] = float(thisLine[1])
                ezConAntBaselineFreqBinsFracL[1] = float(thisLine[2])
                ezConAntBaselineFreqBinsFracL[2] = float(thisLine[3])
                ezConAntBaselineFreqBinsFracL[3] = float(thisLine[4])

            elif thisLine0Lower == '-ezConAntRABaselineFreqBinsFracL'.lower():
                ezConAntRABaselineFreqBinsFracL[0] = float(thisLine[1])
                ezConAntRABaselineFreqBinsFracL[1] = float(thisLine[2])
                ezConAntRABaselineFreqBinsFracL[2] = float(thisLine[3])
                ezConAntRABaselineFreqBinsFracL[3] = float(thisLine[4])

            elif thisLine0Lower == '-ezConAntXTFreqBinsFracL'.lower():
                ezConAntXTFreqBinsFracL[0] = float(thisLine[1])
                ezConAntXTFreqBinsFracL[1] = float(thisLine[2])

            elif thisLine0Lower == '-ezConAntXTVTFreqBinsFracL'.lower():
                ezConAntXTVTFreqBinsFracL[0] = float(thisLine[1])
                ezConAntXTVTFreqBinsFracL[1] = float(thisLine[2])

            elif thisLine0Lower == '-ezConAntXTVTMaxPluckQtyL'.lower():
                ezConAntXTVTMaxPluckQtyL.append(int(thisLine[1]))
                ezConAntXTVTMaxPluckQtyL.append(int(thisLine[2]))

            elif thisLine0Lower == '-ezConAntXTVTMaxPluckValL'.lower():
                ezConAntXTVTMaxPluckValL.append(float(thisLine[1]))
                ezConAntXTVTMaxPluckValL.append(float(thisLine[2]))

            elif thisLine0Lower == '-ezConAntXTVTAvgPluckQtyL'.lower():
                ezConAntXTVTAvgPluckQtyL.append(int(thisLine[1]))
                ezConAntXTVTAvgPluckQtyL.append(int(thisLine[2]))

            elif thisLine0Lower == '-ezConAntXTVTAvgPluckValL'.lower():
                ezConAntXTVTAvgPluckValL.append(float(thisLine[1]))
                ezConAntXTVTAvgPluckValL.append(float(thisLine[2]))

            elif thisLine0Lower == '-ezConAntXTVTPluck'.lower():
                ezConAntXTVTPluckL.append(int(thisLine[1]))

            elif thisLine0Lower == '-ezConAntXTVTSmooth'.lower():
                ezConAntXTVTSmooth = int(thisLine[1])

            elif thisLine0Lower == '-ezCon087Csv'.lower():
                ezCon087Csv = int(thisLine[1])

            elif thisLine0Lower == '-ezConAntXTVTLevelL'.lower():
                ezConAntXTVTLevelL[0] = float(thisLine[1])
                ezConAntXTVTLevelL[1] = float(thisLine[2])

            elif thisLine0Lower == '-ezCon399SignalSampleByFreqBinL'.lower():
                ezCon399SignalSampleByFreqBinL[0] = int(thisLine[1])
                ezCon399SignalSampleByFreqBinL[1] = int(thisLine[2])

            elif thisLine0Lower == '-ezConHeatVMinMaxL'.lower():
                ezConHeatVMinMaxL[0] = float(thisLine[1])
                ezConHeatVMinMaxL[1] = float(thisLine[2])

            elif thisLine0Lower == '-ezConPlotRangeL'.lower():
                #ezConPlotRangeL[0] = int(thisLine[1])
                #ezConPlotRangeL[1] = int(thisLine[2])
                #ezConPlotRangeL0 = int(thisLine[1])
                #ezConPlotRangeL1 = int(thisLine[2])
                #ezConPlotRangeL.append(range(ezConPlotRangeL0, ezConPlotRangeL1 + 1))
                ezConPlotRangeL += [int(thisLine[1]), int(thisLine[2])]

            elif thisLine0Lower == '-ezConGalRaDecNearNearL'.lower():
                ezConGalRaDecNearNearL = []
                ezConGalRaDecNearNearL.append(float(thisLine[1]))
                ezConGalRaDecNearNearL.append(float(thisLine[2]))
                ezConGalRaDecNearNearL.append(float(thisLine[3]))
                ezConGalRaDecNearNearL.append(float(thisLine[4]))


            elif thisLine0Lower[:5] == '-ezCon'.lower():
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

            elif thisLine0Lower == '-ezDefaultsEnd'.lower():
                # ignore the rest of this defaults file
                fileDefaults.close()        #   then have processed all available lines in this defaults file
                return

            else:
                pass    # unrecognized first word, but no error, allows for other ezRA programs

    except (FileNotFoundError, IOError):
    	pass

    else:
        fileDefaults.close()                #   then have processed all available lines in this defaults file



def ezConArgumentsCommandLine():
    # process arguments from command line

    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezConAzimuth                     # float - force Azimuth   (Degrees)
    global ezConElevation                   # float - force Elevation (Degrees)
    global ezConAddAzDeg                    # float - correction factor, add to file's Azimuth   (Degrees)
    global ezConAddElDeg                    # float - correction factor, add to file's Elevation (Degrees)

    global ezConInputdBm                    # integer
    global ezConUseRefSub                   # integer
    global ezConAntXInput                   # integer
    global ezConUseVlsr                     # integer

    global ezConRawSamplesUseL              # integer list
    global ezConRawFreqBinHideL             # integer list

    global ezConAntSamplesUseL              # integer list
    global ezConAntPluckL                   # integer list
    global ezConAntAvgPluckQtyL             # integer list
    global ezConAntAvgPluckFracL            # float list
    global ezConAntFreqBinSmooth            # float - RFI spur limiter: max muliplier over 4 neighboring freqBin

    global ezConRefAvgPluckQtyL             # integer list
    global ezConRefAvgPluckFracL            # float list
    global ezConRefMode                     # integer

    global ezConAntBaselineFreqBinsFracL    # float list
    global ezConAntRABaselineFreqBinsFracL  # float list
    global ezConAntXTFreqBinsFracL          # float list
    global ezConAntXTVTFreqBinsFracL        # float list

    global ezConAntXTVTMaxPluckQtyL         # integer list
    global ezConAntXTVTMaxPluckValL         # float list
    global ezConAntXTVTAvgPluckQtyL         # integer list
    global ezConAntXTVTAvgPluckValL         # float list
    global ezConAntXTVTPluckL               # integer list
    global ezConAntXTVTSmooth               # integer
    global ezCon087Csv                      # integer
    global ezConAntXTVTLevelL               # float list

    global ezCon399SignalSampleByFreqBinL   # integer list
    global ezConHeatVMinMaxL                # float list

    global ezConAstroMath                   # integer

    global ezConDispGrid                    # integer
    global ezConDispFreqBin                 # integer
    global ezConRawDispIndex                # integer
    global ezConPlotRangeL                  # integer list

    global ezConVelGLonEdgeFrac             # float
    #global ezConVelGLonEdgeLevel            # float

    global ezConGalCrossingGLatCenterL      # float list
    global ezConGalCrossingGLatNear         # float
    global ezConGalCrossingGLonCenterL      # float list
    global ezConGalCrossingGLonNear         # float
    global ezConGalRaDecNearNearL           # float list

    global cmdDirectoryS                    # string            creation

    print()
    print('   ezConArgumentsCommandLine ===============')

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
            elif cmdLineArgLower == '-ezConInputdBm'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConInputdBm = int(cmdLineSplit[cmdLineSplitIndex])
            
            elif cmdLineArgLower == '-ezConUseRefSub'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConUseRefSub = int(cmdLineSplit[cmdLineSplitIndex])
            
            elif cmdLineArgLower == '-ezConAntXInput'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXInput = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConUseVlsr'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConUseVlsr = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConRawDispIndex'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConRawDispIndex = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConDispGrid'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConDispGrid = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConDispFreqBin'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConDispFreqBin = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAstroMath'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAstroMath = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConRefMode'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConRefMode = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntPluck'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntPluckL.append(int(cmdLineSplit[cmdLineSplitIndex]))


            # float arguments:
            elif cmdLineArgLower == '-ezConAzimuth'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAzimuth = float(cmdLineSplit[cmdLineSplitIndex])
            elif cmdLineArgLower == '-ezConElevation'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConElevation = float(cmdLineSplit[cmdLineSplitIndex])
            elif cmdLineArgLower == '-ezConAddAzDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAddAzDeg = float(cmdLineSplit[cmdLineSplitIndex])
            elif cmdLineArgLower == '-ezConAddElDeg'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAddElDeg = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntFreqBinSmooth'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntFreqBinSmooth = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConGalCrossingGLatCenter'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLatCenterL += [int(cmdLineSplit[cmdLineSplitIndex])]

            elif cmdLineArgLower == '-ezConGalCrossingGLatCenterL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLatCenterL0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConGalCrossingGLatCenterL1 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConGalCrossingGLatCenterL2 = int(cmdLineSplit[cmdLineSplitIndex])
                ezConGalCrossingGLatCenterL += np.linspace(ezConGalCrossingGLatCenterL0, ezConGalCrossingGLatCenterL1, num=ezConGalCrossingGLatCenterL2).tolist()
                #ezConGalCrossingGLatCenterL += range(ezConGalCrossingGLatCenterL0, ezConGalCrossingGLatCenterL1)

            # grandfather -ezConGalCrossingGLat as -ezConGalCrossingGLatNear
            elif cmdLineArgLower == '-ezConGalCrossingGLat'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLatNear = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConGalCrossingGLatNear'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLatNear = float(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == '-ezConGalCrossingGLonCenter'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLonCenterL += [float(cmdLineSplit[cmdLineSplitIndex])]

            elif cmdLineArgLower == '-ezConGalCrossingGLonCenterL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLonCenterL0 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConGalCrossingGLonCenterL1 = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConGalCrossingGLonCenterL2 = int(cmdLineSplit[cmdLineSplitIndex])
                ezConGalCrossingGLonCenterL += np.linspace(ezConGalCrossingGLonCenterL0, ezConGalCrossingGLonCenterL1, num=ezConGalCrossingGLonCenterL2).tolist()
                #ezConGalCrossingGLatCenterL += range(ezConGalCrossingGLatCenterL0, ezConGalCrossingGLatCenterL1)

            elif cmdLineArgLower == '-ezConGalCrossingGLonNear'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalCrossingGLonNear = float(cmdLineSplit[cmdLineSplitIndex])


            elif cmdLineArgLower == '-ezConVelGLonEdgeFrac'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConVelGLonEdgeFrac = float(cmdLineSplit[cmdLineSplitIndex])

            #elif cmdLineArgLower == '-ezConVelGLonEdgeLevel'.lower():
            #    cmdLineSplitIndex += 1      # point to first argument value
            #    ezConVelGLonEdgeLevel = float(cmdLineSplit[cmdLineSplitIndex])


            # list arguments:
            elif cmdLineArgLower == '-ezConRawFreqBinHide'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConRawFreqBinHideL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConRawSamplesUseL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConRawSamplesUseL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConRawSamplesUseL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntSamplesUseL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntSamplesUseL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntSamplesUseL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntAvgPluckQtyL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntAvgPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntAvgPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntAvgPluckFracL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntAvgPluckFracL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntAvgPluckFracL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConRefAvgPluckQtyL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConRefAvgPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConRefAvgPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConRefAvgPluckFracL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConRefAvgPluckFracL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConRefAvgPluckFracL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntBaselineFreqBinsFracL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntBaselineFreqBinsFracL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntBaselineFreqBinsFracL[1] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntBaselineFreqBinsFracL[2] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntBaselineFreqBinsFracL[3] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntRABaselineFreqBinsFracL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntRABaselineFreqBinsFracL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntRABaselineFreqBinsFracL[1] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntRABaselineFreqBinsFracL[2] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntRABaselineFreqBinsFracL[3] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntXTFreqBinsFracL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTFreqBinsFracL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntXTFreqBinsFracL[1] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntXTVTFreqBinsFracL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTFreqBinsFracL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntXTVTFreqBinsFracL[1] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntXTVTMaxPluckQtyL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTMaxPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntXTVTMaxPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntXTVTMaxPluckValL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTMaxPluckValL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntXTVTMaxPluckValL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntXTVTAvgPluckQtyL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTAvgPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntXTVTAvgPluckQtyL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntXTVTAvgPluckValL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTAvgPluckValL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConAntXTVTAvgPluckValL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntXTVTPluck'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTPluckL.append(int(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezConAntXTVTSmooth'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTSmooth = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezCon087Csv'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezCon087Csv = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConAntXTVTLevelL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConAntXTVTLevelL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConAntXTVTLevelL[1] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezCon399SignalSampleByFreqBinL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezCon399SignalSampleByFreqBinL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezCon399SignalSampleByFreqBinL[1] = int(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConHeatVMinMaxL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConHeatVMinMaxL[0] = float(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConHeatVMinMaxL[1] = float(cmdLineSplit[cmdLineSplitIndex])

            elif cmdLineArgLower == '-ezConPlotRangeL'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                #ezConPlotRangeL[0] = int(cmdLineSplit[cmdLineSplitIndex])
                #cmdLineSplitIndex += 1
                #ezConPlotRangeL[1] = int(cmdLineSplit[cmdLineSplitIndex])
                ezConPlotRangeL0 = int(cmdLineSplit[cmdLineSplitIndex])
                cmdLineSplitIndex += 1
                ezConPlotRangeL1 = int(cmdLineSplit[cmdLineSplitIndex])
                #ezConPlotRangeL.append(range(ezConPlotRangeL0, ezConPlotRangeL1 + 1))
                ezConPlotRangeL += [ezConPlotRangeL0, ezConPlotRangeL1]

            elif cmdLineArgLower == '-ezConGalRaDecNearNearL'.lower():
                ezConGalRaDecNearNearL = []
                cmdLineSplitIndex += 1      # point to first argument value
                ezConGalRaDecNearNearL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConGalRaDecNearNearL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConGalRaDecNearNearL.append(float(cmdLineSplit[cmdLineSplitIndex]))
                cmdLineSplitIndex += 1
                ezConGalRaDecNearNearL.append(float(cmdLineSplit[cmdLineSplitIndex]))

            elif cmdLineArgLower == '-ezDefaultsFile'.lower():
                cmdLineSplitIndex += 1      # point to first argument value
                ezConArgumentsFile(cmdLineSplit[cmdLineSplitIndex])

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

            elif cmdLineArgLower[:6] == '-ezCon'.lower():
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

            else:
                pass    # unrecognized first word, but no error, allows for other ezRA programs

        else:
            # must be a data directory or file, remember it
            cmdDirectoryS = cmdDirectoryS + cmdLineSplit[cmdLineSplitIndex] + ' '

        cmdLineSplitIndex += 1



def ezConArguments():
    # argument: (Computing) a value or address passed to a procedure or function at the time of call

    global programRevision                  # string
    global commandString                    # string

    global ezRAObsLat                       # float
    global ezRAObsLon                       # float
    global ezRAObsAmsl                      # float
    global ezRAObsName                      # string

    global ezConAzimuth                     # float - force Azimuth   (Degrees)
    global ezConElevation                   # float - force Elevation (Degrees)
    global ezConAddAzDeg                    # float - correction factor, add to file's Azimuth   (Degrees)
    global ezConAddElDeg                    # float - correction factor, add to file's Elevation (Degrees)

    global ezConInputdBm                    # integer
    global ezConUseRefSub                   # integer
    global ezConAntXInput                   # integer
    global ezConUseVlsr                     # integer

    global ezConRawSamplesUseL              # integer list
    global ezConRawFreqBinHideL             # integer list

    global ezConAntSamplesUseL              # integer list
    global ezConAntPluckL                   # integer list
    global ezConAntAvgPluckQtyL             # integer list
    global ezConAntAvgPluckFracL            # float list
    global ezConAntFreqBinSmooth            # float - RFI spur limiter: max muliplier over 4 neighboring freqBin

    global ezConRefAvgPluckQtyL             # integer list
    global ezConRefAvgPluckFracL            # float list
    global ezConRefMode                     # integer

    global ezConAntBaselineFreqBinsFracL    # float list
    global ezConAntRABaselineFreqBinsFracL  # float list
    global ezConAntXTFreqBinsFracL          # float list
    global ezConAntXTVTFreqBinsFracL        # float list

    global ezConAntXTVTMaxPluckQtyL         # integer list
    global ezConAntXTVTMaxPluckValL         # float list
    global ezConAntXTVTAvgPluckQtyL         # integer list
    global ezConAntXTVTAvgPluckValL         # float list
    global ezConAntXTVTPluckL               # integer list
    global ezConAntXTVTSmooth               # integer
    global ezCon087Csv                      # integer
    global ezConAntXTVTLevelL               # float list

    global ezCon399SignalSampleByFreqBinL   # integer list
    global ezCon399SignalSampleByFreqBin1d  # float list or numpy

    global ezConHeatVMinMaxL                # float list

    global ezConAstroMath                   # integer

    global fileNameLast                     # string
    global plotCountdown                    # integer

    global ezConDispGrid                    # integer
    global ezConDispFreqBin                 # integer
    global ezConRawDispIndex                # integer
    global ezConPlotRangeL                  # integer list
    global ezConPlotRequestedL              # integer list

    global ezConVelGLonEdgeFrac             # float
    global ezConVelGLonEdgeLevel            # float

    global ezConGalCrossingGLatCenterL      # float list
    global ezConGalCrossingGLatNear         # float
    global ezConGalCrossingGLonCenterL      # float list
    global ezConGalCrossingGLonNear         # float
    global ezConGalRaDecNearNearL           # float list

    # defaults
    if 1:
        ezRAObsLat  = -999.                 # silly number
        ezRAObsLon  = -999.                 # silly number
        ezRAObsAmsl = -999.                 # silly number
        #ezRAObsName = 'LebanonKS'
        ezRAObsName = ''                    # silly name

        ezConInputdBm     =  0
        ezConUseRefSub    =  0
        ezConAntXInput    = -1              # default = -1 for auto choice: AntB, or if 1 < refQty then AntRB
        ezConUseVlsr      =  1
        ezConRawDispIndex =  0

        ezConAzimuth   = -999               # float - silly value for simulate Azimuth (Degrees)
        ezConElevation = -999               # float - silly value for simulate Elevation (Degrees)
        ezConAddAzDeg  = 0.
        ezConAddElDeg  = 0.

        ezConRawSamplesUseL   = []          # empty to disable
        ezConRawFreqBinHideL  = []          # empty to disable

        ezConAntSamplesUseL   = []          # empty to disable
        ezConAntPluckL        = []          # empty to disable
        ezConAntAvgPluckQtyL  = []          # empty to disable
        ezConAntAvgPluckFracL = []          # empty to disable
        ezConAntFreqBinSmooth = 999999.     # RFI spur limiter: max muliplier over 4 neighboring freqBin

        ezConRefAvgPluckQtyL  = []          # empty to disable
        ezConRefAvgPluckFracL = []          # empty to disable

        # to average, specify low and high freqBin of total freqBin,
        # 60 low of 256 freqBin like (60 / 256 = 0.2344) or (150 / 1024 = 0.1465),
        #   and 60 high of 256 like (1 - 0.2344 = 0.7656) or (1 - 0.1465 = 0.8535)
        #   (1 / 256 = 0.00390625) or (1 / 1024 = 0.0009765625)
        ezConAntBaselineFreqBinsFracL   = [0, 0.2344, 0.7656, 1]
        ezConAntRABaselineFreqBinsFracL = [0, 0.2344, 0.7656, 1]

        # for a bandwidth of 2.4 desired Doppler x, try (2.4 / 2 + x) / 2.4
        #   like for Doppler -0.5, (2.4 / 2 + (-0.5 )) / 2.4 = 0.2917,
        #   like for Doppler  4.5, (2.4 / 2 + ( 0.45)) / 2.4 = 0.6888
        ezConAntXTFreqBinsFracL         = [   0.15,   0.85      ]

        ezConAntXTVTFreqBinsFracL       = [   0.25,   0.75      ]

        ezConAntXTVTMaxPluckQtyL = []       # empty to disable
        ezConAntXTVTMaxPluckValL = []       # empty to disable
        ezConAntXTVTAvgPluckQtyL = []       # empty to disable
        ezConAntXTVTAvgPluckValL = []       # empty to disable
        ezConAntXTVTPluckL       = []       # empty to disable
        ezConAntXTVTSmooth       = 0        # to disable
        ezCon087Csv              = 0        # to disable
        ezConAntXTVTLevelL = [1., 0.]       # to disable

        ezCon399SignalSampleByFreqBinL = [10, 0]    # Ant, antenna sample 0
        ezCon399SignalSampleByFreqBin1d = []        # flag as empty

        ezConHeatVMinMaxL = [0., 0.]        # default is to autoscale heatVMin of heatmaps

        ezConDispGrid    = 0
        ezConDispFreqBin = 0

        #ezConAstroMath = 2                  # 2 = astropy math = slow but authoritative
        ezConAstroMath = 1                  # 1 = math from MIT Haystack SRT

        ezConRefMode = 10

        ezConGalCrossingGLatCenterL = []    # empty for default Galactic plane
        # defines 'close to GLat crossing" in Galactic Latitude degrees
        ezConGalCrossingGLatNear    = 5.

        ezConGalCrossingGLonCenterL = []    # empty to disable
        # defines 'close to GLon crossing" in Galactic Longitude degrees
        ezConGalCrossingGLonNear    = 0.5

        ezConGalRaDecNearNearL = []         # empty to disable

        ezConVelGLonEdgeFrac =  0.5     # velGLon level fraction for plotEzCon430velGLonEdges()
        ezConVelGLonEdgeLevel = 0.      # velGLon level for plotEzCon430velGLonEdges(), if not 0 then
                                        #   ezConVelGLonEdgeFrac ignored

        ezConPlotRangeL = []

    plotCountdown = 88                  # number of plots still to print

    # Program argument priority:
    #    Start with the argument value defaults inside the programs.
    #    Then replace those values with any arguments from the ezDefaults.txt in the program's directory.
    #    Then replace values with any arguments from the ezDefaults.txt in the current
    #       directory (where you are standing).
    #    Then replace values (in order) with any arguments from the command line (including
    #       any -ezDefaultsFile).
    #    Each last defined value wins.
    # The top (and bottom ?) of the program printout should list the resultant argument values.
    # Eventually support -ezez argument preface, to allow ignoring.

    # process arguments from ezDefaults.txt file in the same directory as this ezCon program
    ezConArgumentsFile(os.path.dirname(__file__) + os.path.sep + 'ezDefaults.txt')

    # process arguments from ezDefaults.txt file in the current directory
    ezConArgumentsFile('ezDefaults.txt')

    # process arguments from command line
    ezConArgumentsCommandLine()

    # sanity tests

    if ezConAntXInput not in [-1, 0, 2, 4, 5, 6]:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezConAntXInput, 'is an unrecognized value for ezConAntXInput')
        print('                            Allowed values = -1, 0, 2, 4, 5, or 6')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezCon399SignalSampleByFreqBinL[0] not in [10, 12, 14, 16, 18]:
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ', ezCon399SignalSampleByFreqBinL[0], 'is an unrecognized value for ezCon399SignalSampleByFreqBinL[0]')
        print('                            Allowed values = 10, 12, 14, 16, or 18')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezConGalCrossingGLatCenterL == []:
        ezConGalCrossingGLatCenterL = [0.]

    # create ezConPlotAllL list of all possible ezCon plot numbers
    ezConPlotAllL  = [0, 1, 2, 7, 17, 27, 37, 47, 57, 61, 67, 77, 81, 82, 87, 88, 97, 98]
    ezConPlotAllL += [100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 191]
    ezConPlotAllL += [200, 201, 202, 207, 217, 227, 237, 241, 247, 257, 261, 262, 267, 277, 281, 282, 287, 297]
    ezConPlotAllL += [300, 301, 302, 307, 317, 327, 337, 347, 357, 361, 367, 377, 381, 382, 383, 387, 388, 393, 397, 398, 399]
    ezConPlotAllL += [510, 519, 520, 529, 530, 541, 550]
    ezConPlotAllL += [690]
    ezConPlotAllL += [800]
    # create ezConPlotRequestedL list of requested ezCon plot numbers
    print('================== ezConPlotRangeL =', ezConPlotRangeL)
    print('================== len(ezConPlotRangeL) =', len(ezConPlotRangeL))
    if ezConPlotRangeL:
        ezConPlotRequestedL = []
        for i in range(0, len(ezConPlotRangeL), 2):                            # ezConPlotRangeL comes in pairs
            #for j in range(ezConPlotRangeL[i], ezConPlotRangeL[i+1]):
            #    if j in ezConPlotAllL:
            #        ezConPlotRequestedL.append(j)
            ezConPlotRequestedL += list(set(range(ezConPlotRangeL[i], ezConPlotRangeL[i+1]+1)) & set(ezConPlotAllL))
        ezConPlotRequestedL = list(set(ezConPlotRequestedL))                    # in to a unique list
    else:
        ezConPlotRequestedL = ezConPlotAllL
    print('================== ezConPlotRequestedL =', sorted(ezConPlotRequestedL))
    print('================== len(ezConPlotRequestedL) =', len(ezConPlotRequestedL))

    if 1:
        # print status
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezConAzimuth   =', ezConAzimuth)
        print('   ezConElevation =', ezConElevation)
        print('   ezConAddAzDeg  =', ezConAddAzDeg)
        print('   ezConAddElDeg  =', ezConAddElDeg)
        print()
        print('   ezConInputdBm  =', ezConInputdBm)
        print()
        print('   ezConRawSamplesUseL   =', ezConRawSamplesUseL)
        print('   ezConRawFreqBinHideL  =', ezConRawFreqBinHideL)
        print()
        print('   ezConRefMode          =', ezConRefMode)
        print()
        print('   ezConAntSamplesUseL   =', ezConAntSamplesUseL)
        print('   ezConAntPluckL        =', ezConAntPluckL)
        print('   ezConAntAvgPluckQtyL  =', ezConAntAvgPluckQtyL)
        print('   ezConAntAvgPluckFracL =', ezConAntAvgPluckFracL)
        print('   ezConAntFreqBinSmooth =', ezConAntFreqBinSmooth)
        print()
        print('   ezConRefAvgPluckQtyL  =', ezConRefAvgPluckQtyL)
        print('   ezConRefAvgPluckFracL =', ezConRefAvgPluckFracL)
        print()
        print('   ezConUseRefSub        =', ezConUseRefSub)
        print()
        print('   ezConAntBaselineFreqBinsFracL   =', ezConAntBaselineFreqBinsFracL)
        print('   ezConAntRABaselineFreqBinsFracL =', ezConAntRABaselineFreqBinsFracL)
        print()
        print('   ezConAntXInput                  =', ezConAntXInput)
        print('   ezConAntXTVTLevelL              =', ezConAntXTVTLevelL)
        print()
        print('   ezConAntXTFreqBinsFracL         =', ezConAntXTFreqBinsFracL)
        print('   ezConUseVlsr                    =', ezConUseVlsr)
        print('   ezConAntXTVTFreqBinsFracL       =', ezConAntXTVTFreqBinsFracL)
        print()
        print('   ezConAntXTVTMaxPluckQtyL        =', ezConAntXTVTMaxPluckQtyL)
        print('   ezConAntXTVTMaxPluckValL        =', ezConAntXTVTMaxPluckValL)
        print('   ezConAntXTVTAvgPluckQtyL        =', ezConAntXTVTAvgPluckQtyL)
        print('   ezConAntXTVTAvgPluckValL        =', ezConAntXTVTAvgPluckValL)
        print('   ezConAntXTVTPluckL              =', ezConAntXTVTPluckL)
        print('   ezConAntXTVTSmooth              =', ezConAntXTVTSmooth)
        print('   ezCon087Csv                     =', ezCon087Csv)
        print()
        print('   ezCon399SignalSampleByFreqBinL  =', ezCon399SignalSampleByFreqBinL)
        print()
        print('   ezConRawDispIndex     =', ezConRawDispIndex)
        print('   ezConDispGrid         =', ezConDispGrid)
        print('   ezConDispFreqBin      =', ezConDispFreqBin)
        print('   ezConHeatVMinMaxL     =', ezConHeatVMinMaxL)
        print()
        print('   ezConAstroMath        =', ezConAstroMath)
        print()
        print('   ezConGalCrossingGLatCenterL =', ezConGalCrossingGLatCenterL)
        print('   ezConGalCrossingGLatNear    =', ezConGalCrossingGLatNear)
        print()
        print('   ezConGalCrossingGLonCenterL =', ezConGalCrossingGLonCenterL)
        print('   ezConGalCrossingGLonNear    =', ezConGalCrossingGLonNear)
        print()
        print('   ezConGalRaDecNearNearL      =', ezConGalRaDecNearNearL)
        print()
        print('   ezConVelGLonEdgeFrac  =', ezConVelGLonEdgeFrac)
        print('   ezConVelGLonEdgeLevel =', ezConVelGLonEdgeLevel)
        print()
        print('   ezConPlotRangeL       =', ezConPlotRangeL)



def readDataDir():
    # Open each .txt radio file in each directory and read individual lines.
    # Creates ezRAObsLat, ezRAObsLon, ezRAObsAmsl, ezRAObsName,
    #   fileFreqMin, fileFreqMax, fileFreqBinQty,
    #   azimuthDeg, elevationDeg, dataFileIdx, dataTimeUtc, raw, rawLen, fileNameLast

    global cmdDirectoryS            # string

    global ezRAObsLat               # float
    global ezRAObsLon               # float
    global ezRAObsAmsl              # float
    global ezRAObsName              # string
    
    global fileNameLast             # string                                    creation
    global fileFreqMin              # float                                     creation
    global fileFreqMax              # float                                     creation
    global fileFreqBinQty           # integer                                   creation

    global ezConInputdBm            # integer

    global ezConRawSamplesUseL      # integer list
    global ezConRefMode             # integer

    global dataFileIdx              # integer array                             creation
    global dataTimeUtc              # 'astropy.time.core.Time' object array     creation
    global azimuthDeg               # float array                               creation
    global elevationDeg             # float array                               creation
    global ezConAzimuth             # float
    global ezConElevation           # float
    global ezConAddAzDeg            # float
    global ezConAddElDeg            # float
    global raw                      # float 2d array                            creation
    global rawLen                   # integer                                   creation
    global refQty                   # integer                                   creation

    global ezConAntXInput           # integer
    global studyOutString           # string                                    creation
    global commandString            # string

    print()
    print('   readDataDir ===============')

    rawLen  = 0
    refQty  = 0
    feedRefOnThis = 0
    dataFileIdxThis = -1
    pointingLineSplitNew = False    # flag
    locBaseValid = False            # flag locBase as empty (for astropy)

    if ezConRawSamplesUseL:
        # start with first pair of ezConRawSamplesUseL list elements
        useSamplesRawLast  = ezConRawSamplesUseL[-1]
        useSamplesRawStart = ezConRawSamplesUseL[0]
        useSamplesRawStop  = ezConRawSamplesUseL[1]
        useSamplesRawIndex = 2                          # point to next start/stop pair, if any
    else:
        # ezConRawSamplesUseL empty
        useSamplesRawLast  = 99999999999                # silly big number
        useSamplesRawStart = 0
        useSamplesRawStop  = useSamplesRawLast          # silly big number
    sampleCount = 0         # increments whether or not the data line was collected (ezConRawSamplesUseL)


    directoryList = cmdDirectoryS.split()
    directoryListLen = len(directoryList)
    
    ezRAObsNameFile = ''
    studyOutString = '\n'
    studyOutString += f'now = UTC time {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")}\n'
    studyOutString += f'programRevision = {programRevision}\n'
    studyOutString += f'Python sys.version = {sys.version}\n'
    studyOutString += f'matplotlib.__version__ = {matplotlib.__version__}\n\n'
    # record the (complex?) ezCon command line
    studyOutString += f'Python commandString = {commandString}\n\n'
    dataElevationRefDeg = np.array([999.9])             # silly value to mark as a REF sample
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
            fileList = sorted(os.listdir(directory))    # each directory sorted alphabetically
        fileListLen = len(fileList)
        for fileCounter in range(fileListLen):
            fileReadName = fileList[fileCounter]

            if not fileReadName.lower().endswith('.txt'):
                continue            # skip to next file

            if fileReadName[0] == os.path.sep or fileReadName[0] == '.':
                fileReadNameFull = fileReadName
            else:
                fileReadNameFull = directory + os.path.sep + fileReadName
            print()
            print(' inspecting', fileReadNameFull)
            fileRead = open(fileReadNameFull, 'r')
            if fileRead.mode == 'r':

                ## 220301 new format
                ## ezRA ezCol .txt daily data file with 3-line non-comment header and
                ##   1-line samples each with timestamp and 256 values:
                ##
                ## from ezCol04b5ea.py
                ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb
                ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
                ## az 227.9 el 42.7 
                ## # times are in UTC
                ## 2022-02-15T05:30:55 10.523690382 10.570080895 10.535587705 10.527403187 ... C
                ## 2022-02-15T05:30:56 10.558290361 10.551762452 10.545512521 10.539835481 ...
                ## ...



                fileRawLen = 0          # reset with each new file
                
                # read line 1
                ## from ezCol10z05p.py (Jul-13-2022a N0RQV)
                #  01234567890
                # find next non-End-Of-File non-blank non-comment line of .txt file
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
                if not fileLine:                     # if end of file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                         #   skip to next file

                # skip to next data file if fileLine has less than 10 characters
                if len(fileLine) < 10:               # if not a valid data file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                         #   skip to next data file
                # skip to next data file if fileLine not start with 'from ezCol'
                if fileLine[:10] != 'from ezCol':    # if not a valid data file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                         #   skip to next data file

                # now assume a valid ezCol .txt data file

                dataFileIdxThis += 1
                #studyOutString += f'file = {fileCounter:,} = ' \
                #    + directory + os.path.sep + fileReadName + '\n'
                studyOutStringThis = f'data file = {dataFileIdxThis:,} = ' \
                    + directory + os.path.sep + fileReadName
                print(' ' + studyOutStringThis)
                studyOutString += studyOutStringThis + '\n'

                # read line 2
                ## lat 40.299512 long -105.084491 amsl 1524 name N0RQV8 ezb
                # find next non-End-Of-File non-blank non-comment line of .txt file
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
                if not fileLine:                   # if end of file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                            #   skip to next file
                ezRAObsLatFile = float(fileLineSplit[1])
                print('   ezRAObsLatFile  = ', ezRAObsLatFile)
                ezRAObsLonFile = float(fileLineSplit[3])
                print('   ezRAObsLonFile  = ', ezRAObsLonFile)
                ezRAObsAmslFile = float(fileLineSplit[5])
                print('   ezRAObsAmslFile = ', ezRAObsAmslFile)
                if 7 < len(fileLineSplit):
                    # bug: replace with fileLine[qqqq:] (to allow double spaces in name?)
                    ezRAObsNameFile = ' '.join(fileLineSplit[7:])
                print('   ezRAObsNameFile = ', ezRAObsNameFile)



                # read line 3
                ## freqMin 1419.205 freqMax 1421.605 freqBinQty 256
                # find next non-End-Of-File non-blank non-comment line of .txt file
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
                if not fileLine:                   # if end of file
                    fileRead.close()                 #   then have processed all lines in this data file
                    continue                            #   skip to next file
                fileFreqMin    = float(fileLineSplit[1])
                #print('   fileFreqMin    = ', fileFreqMin)
                fileFreqMax    = float(fileLineSplit[3])
                #print('   fileFreqMax    = ', fileFreqMax)
                fileFreqBinQty = int  (fileLineSplit[5])
                #print('   fileFreqBinQty = ', fileFreqBinQty)


                # az line not required
                ## az 227.9 el 42.7 
                # so, until replaced by an az line,
                # add correction factor to file's Azimuth   (Degrees)
                dataAzimuthDeg   = ezConAzimuth   + ezConAddAzDeg
                # add correction factor to file's Elevation (Degrees)
                dataElevationDeg = ezConElevation + ezConAddElDeg
                #print('   dataAzimuthDeg   =', dataAzimuthDeg)
                #print('   dataElevationDeg =', dataElevationDeg)


                # read blank, and comment, az, and data lines
                ## az 227.9 el 42.7 
                ## # times are in UTC
                ## 2022-02-15T05:30:55 10.523690382 10.570080895 10.535587705 10.527403187 ... C
                ## 2022-02-15T05:30:56 10.558290361 10.551762452 10.545512521 10.539835481 ...
                ## ...
                while(fileLine and sampleCount <= useSamplesRawLast):
                    # fetch a new line
                    fileLine = fileRead.readline()
                    # len(fileLine): 0=EOF  1=LFonly  2=1CharacterWithLF
                    if not fileLine:                    # if end of file
                        fileRead.close()                #   then have processed all lines in this data file
                        continue                        #   skip to next file

                    fileLineSplit = fileLine.split()
                    #print('========== fileLineSplit =', fileLineSplit)
                    # len(fileLineSplit): 0=EOF  0=LFonly  1=1CharacterWithLF
                    # ignore blank line
                    if fileLineSplit:               # if not blank line
                        fileLineSplit0Low = fileLineSplit[0].lower()    # to ignore capitalization

                        # ignore comment line
                        if fileLineSplit[0][0] == '#':    # if first non-white character is '#'
                            pass                            #   flow on to fetch next line

                        elif fileLineSplit0Low == 'azdeg' or fileLineSplit0Low == 'az' or fileLineSplit0Low == 'rah' or fileLineSplit0Low == 'glatdeg':
                            ## azDeg 227.9 elDeg 42.7 
                            ## az 227.9 el 42.7 
                            ## raH 22.9 decDeg 42.7
                            ## gLatDeg 42.7 gLonDeg 227.9

                            # assume a valid pointing line
                            # gather split pointing line to use after have a timeStamp
                            pointingLineSplit = fileLineSplit
                            pointingLineSplit0Low = fileLineSplit0Low
                            pointingLineSplitNew = True

                        else:
                            # assume a valid data line
                            print(f'\r file = {fileCounter:,} of {fileListLen:,}' \
                                + f' in dir {directoryCounter + 1:,} of {directoryListLen:,} = ' \
                                + directory + os.path.sep + fileReadName, end='')   # allow append to print line

                            # need to update useSamplesRawStop and useSamplesRawStart ?
                            if useSamplesRawStop < sampleCount:
                                useSamplesRawStart = ezConRawSamplesUseL[useSamplesRawIndex]
                                useSamplesRawStop  = ezConRawSamplesUseL[useSamplesRawIndex + 1]
                                useSamplesRawIndex += 2        # point to next Start/Stop pair, if any

                            # is sampleCount inside a RAW want-to-use section ?
                            if useSamplesRawStart <= sampleCount and sampleCount <= useSamplesRawStop:
                                # use this sample
                                # collect the data line

                                # Bases: astropy.time.TimeString
                                # FITS format: “[±Y]YYYY-MM-DD[THH:MM:SS[.sss]]”.
                                # https://docs.astropy.org/en/stable/time/#id3
                                #print('\n========== fileLineSplit[0] =', fileLineSplit[0])
                                dataTimeUtcThis = Time(fileLineSplit[0], format='fits', scale='utc')

                                # without astropy ???????????????????????????????????
                                # https://gist.github.com/jiffyclub/1294443
                                #timeStampUtc  = datetime.now(timezone.utc)
                                #timeStampUtcS = timeStampUtc.strftime('%Y-%m-%dT%H:%M:%S ')

                                #radDataL = list(map(float, fileLineSplit[1:fileFreqBinQty + 1]))
                                #print('radDataL =')
                                #print(radDataL)
                                #print(len(fileLineSplit))

                                if ezConInputdBm:
                                    # https://www.omnicalculator.com/conversion/dbm-to-watts#formula-for-dbm-to-watts-conversion
                                    # pW = 0.001 * (10. ** (pdBm / 10.))
                                    # https://www.rapidtables.com/convert/power/dBm_to_Watt.html
                                    # P(W) = 0.001 * (10 ** (P(dBm) / 10)) = 10 ** ((P(dBm) - 30) / 10)
                                    radData = 0.001 * (10. ** (0.1 * np.array([list(map(float, fileLineSplit[1:fileFreqBinQty + 1]))])))
                                else:
                                    radData = np.array([list(map(float, fileLineSplit[1:fileFreqBinQty + 1]))])
                                #print('radData =')
                                #print(radData)
                                #print(len(fileLineSplit))

                                if ezConRefMode == 10:
                                    # is there an 'r' or 'c' in last data word ?
                                    # (changed the format from Calibration 'c' to Reference 'r')
                                    dataFlags = fileLineSplit[-1].lower()
                                    #feedRefOnThis = 'r' in dataFlags or 'c' in dataFlags
                                    feedRefOnThis = 'r' in dataFlags

                                if pointingLineSplitNew:
                                    # now have a timeStamp
                                    if pointingLineSplit0Low == 'azdeg' or pointingLineSplit0Low == 'az':
                                        print()
                                        # assume a valid azDeg or az line
                                        ## azDeg 227.9 elDeg 42.7 
                                        ## az 227.9 el 42.7 
                                        dataAzimuthDeg   = float(pointingLineSplit[1])
                                        dataElevationDeg = float(pointingLineSplit[3])

                                    # precision study:
                                    #
                                    #   #UTC_Time(s)   Ra(deg)  Dec(deg)   Az(deg)   El(deg)
                                    #   11992.000000  83.06220   -4.6685  193.4920   45.8379
                                    #   6             5           4       4          4
                                    #
                                    #
                                    # data/Skynet_60333_barnard_33-nb_107271_56634.A.cal5Az.txt says in part:
                                    #   az 193.492 el 45.8381
                                    # ezColGB20m code     says "az {dataAzimuth:g} el {dataElevation:g}"
                                    #   so with maybe fractional digits:
                                    #      3          4
                                    # ezColGB20m code now says "az {dataAzimuth:.5g} el {dataElevation:.5g}"
                                    #      5          5
                                    #
                                    # data/Skynet_60333_barnard_33-nb_107271_56634.A.cal5Ra.txt says in part:
                                    #   ra 5.53815 dec -4.6683
                                    # ezColGB20m code     says "ra {dataRaH:g} dec {dataDecDeg:g}"
                                    #   so with maybe fractional digits:
                                    #      5          4
                                    # ezColGB20m code now says "ra {dataRaH:.5g} dec {dataDecDeg:.5g}"
                                    #      5          5
                                    #
                                    #
                                    # Skynet_60333_barnard_33-nb_107271_56634.A.cal5Ra.ezb says in part:
                                    #   ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  ...
                                    #   60333.13882 5.581 -4.859 -19.223 -151.516 ...
                                    # ezCon code says "'%0.5f %0.3f %0.3f %0.3f %0.3f"
                                    #   so with fractional digits:
                                    #   5           3     3      3       3

                                    elif pointingLineSplit0Low == 'rah':
                                        # assume a valid raH line
                                        ## raH 22.9 decDeg 42.7
                                        print()
                                        dataRightAscensionH = float(pointingLineSplit[1])
                                        dataDeclinationDeg  = float(pointingLineSplit[3])
                                        #if ezConAstroMath == 1:
                                        if 0:
                                            # use math from MIT Haystack SRT
                                            # radec_azel()      from MIT Haystack SRT, geom.c
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print(' ========== FATAL ERROR:  ezConAstroMath == 1 does not yet support "raH" line input.')
                                            print()
                                            print()
                                            print()
                                            print()
                                            print('\a')     # ring bell
                                            exit()
                                        #elif ezConAstroMath == 2:
                                        if 1:
                                            # use math from astropy
                                            if not locBaseValid:
                                                print(' ========== not locBaseValid =======================')
                                                from astropy import units as u
                                                from astropy.coordinates import EarthLocation
                                                from astropy.coordinates import SkyCoord

                                                locBase = EarthLocation(lat = ezRAObsLatFile*u.deg, lon = ezRAObsLonFile*u.deg,
                                                    height = ezRAObsAmslFile*u.m)
                                                locBaseValid = True
                                                
                                            # Coordinate of sky target at the UTC time from the data file
                                            # SkyCoord() wants time = Time('1991-06-06 12:00:00')
                                            pointingTelescope = SkyCoord(ra = dataRightAscensionH*u.hour, dec = dataDeclinationDeg*u.deg,
                                                obstime = dataTimeUtcThis, frame = 'icrs', location = locBase)
                                            # extract AzEl coordinates
                                            dataAzimuthDeg = float(pointingTelescope.altaz.az.degree)
                                            #print(' dataAzimuthDeg =', dataAzimuthDeg, 'degrees')
                                            dataElevationDeg = float(pointingTelescope.altaz.alt.degree)
                                            #print(' dataElevationDeg =', dataElevationDeg, 'degrees')
                                        print('   "raH" line input to dataAzimuthDeg   =', dataAzimuthDeg)
                                        print('                       dataElevationDeg =', dataElevationDeg)

                                    elif pointingLineSplit0Low == 'glatdeg':
                                        # assume a valid gLatDeg line
                                        ## gLatDeg 42.7 gLonDeg 227.9
                                        print()
                                        dataGLatDeg = float(pointingLineSplit[1])
                                        dataGLonDeg = float(pointingLineSplit[3])
                                        #if ezConAstroMath == 1:
                                        if 0:
                                            # use math from MIT Haystack SRT
                                            # radec_azel()      from MIT Haystack SRT, geom.c
                                            print()
                                            print()
                                            print()
                                            print()
                                            print()
                                            print(' ========== FATAL ERROR:  ezConAstroMath == 1 does not yet support "raH" line input.')
                                            print()
                                            print()
                                            print()
                                            print()
                                            print('\a')     # ring bell
                                            exit()
                                        #elif ezConAstroMath == 2:
                                        if 1:
                                            # use math from astropy
                                            if not locBaseValid:
                                                print(' ========== not locBaseValid =======================')
                                                from astropy import units as u
                                                from astropy.coordinates import EarthLocation
                                                from astropy.coordinates import SkyCoord

                                                locBase = EarthLocation(lat = ezRAObsLatFile*u.deg, lon = ezRAObsLonFile*u.deg,
                                                    height = ezRAObsAmslFile*u.m)
                                                locBaseValid = True

                                            # Coordinate of sky target at the UTC time from the data file
                                            # SkyCoord() wants time = Time('1991-06-06 12:00:00')
                                            pointingTelescope = SkyCoord(b = dataGLatDeg*u.deg, l = dataGLonDeg*u.deg,
                                                obstime = dataTimeUtcThis, frame = 'galactic', location = locBase)
                                            # extract AzEl coordinates
                                            dataAzimuthDeg = float(pointingTelescope.altaz.az.degree)
                                            #print(' raHThis =', raHThis, 'Hours')
                                            dataElevationDeg = float(pointingTelescope.altaz.alt.degree)
                                            #print(' decDegThis =', decDegThis, 'degrees')
                                        print()
                                        print('   "gLatDeg" line input to dataAzimuthDeg   =', dataAzimuthDeg)
                                        print('                           dataElevationDeg =', dataElevationDeg)

                                    # add correction factor to file's Azimuth   (Degrees)
                                    dataAzimuthDeg   += ezConAddAzDeg
                                    # add correction factor to file's Elevation (Degrees)
                                    dataElevationDeg += ezConAddElDeg

                                    if 90. < dataElevationDeg:
                                        # to allow calculations, simulate rotating dish
                                        dataElevationDeg =  180. - dataElevationDeg
                                        dataAzimuthDeg   -= 180.
                                        print('   after Azimuth rotation, using dataAzimuthDeg   =', dataAzimuthDeg)
                                        print('   after Azimuth rotation, using dataElevationDeg =', dataElevationDeg)
                                    if dataAzimuthDeg < 0.:
                                        dataAzimuthDeg += 360.
                                    if 360. <= dataAzimuthDeg:
                                        dataAzimuthDeg -= 360.

                                    print('   dataAzimuthDeg   =', dataAzimuthDeg)
                                    print('   dataElevationDeg =', dataElevationDeg)

                                    pointingLineSplitNew = False

                                # create or append to numpys
                                if rawLen:
                                    # append to numpys
                                    dataFileIdx = np.concatenate([dataFileIdx, np.array([dataFileIdxThis])])
                                    dataTimeUtc = np.concatenate([dataTimeUtc, np.array([dataTimeUtcThis])])
                                    azimuthDeg  = np.concatenate([azimuthDeg , np.array([dataAzimuthDeg])])
                                    raw         = np.concatenate([raw        , radData])
                                    if feedRefOnThis:
                                        # mark as a REF sample
                                        elevationDeg = np.concatenate([elevationDeg, dataElevationRefDeg])
                                        refQty += 1
                                    else:
                                        elevationDeg = np.concatenate([elevationDeg, np.array([dataElevationDeg])])
                                else:
                                    # create numpys
                                    dataFileIdx = np.array([dataFileIdxThis])
                                    dataTimeUtc = np.array([dataTimeUtcThis])
                                    azimuthDeg  = np.array([dataAzimuthDeg])
                                    raw         = radData
                                    if feedRefOnThis:
                                        # mark as a REF sample
                                        elevationDeg = dataElevationRefDeg
                                        refQty += 1
                                    else:
                                        elevationDeg = np.array([dataElevationDeg])

                                # increments when the data line was collected (ezConRawSamplesUseL)
                                fileRawLen += 1
                                rawLen += 1

                            # increments whether or not the data line was collected (ezConRawSamplesUseL)
                            sampleCount += 1

                            # allow append to print line
                            #print(f'    number of samples read = {sampleCount:,}',
                            print(f' samplesRead= {sampleCount:,}',
                                f'  fileRawLen= {fileRawLen:,}',
                                f'  rawLen= {rawLen:,}',
                                f'  antLen ?= {rawLen - refQty:,}             ', end='')

                    # flow on to fetch next file line

                #while(sampleCount <= useSamplesRawLast):

                #studyOutString += f'Local time = {time.asctime(time.localtime())}\n'
                #studyOutString += f'UTC time = {datetime.now(timezone.utc).strftime("%Y%m%d")}\n'
                ##studyOutString += f'UTC time = {datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")}\n'
                ##studyOutString += f'Python sys.version = {sys.version}\n'
                ##studyOutString += f'matplotlib.__version__ = {matplotlib.__version__}\n'
                ##studyOutString += f'programRevision = {programRevision}\n\n'
                ## # record the (complex?) ezCon command line
                ##studyOutString += f'Python commandString = {commandString}\n\n'
                ##studyOutString += f'file = {fileCounter:,} = ' \
                ##    + directory + os.path.sep + fileReadName + f' ,  Total raw samples = {rawLen:,}\n'
                studyOutString += '                                         ' \
                    + f'Total raw samples = {rawLen:,}, fileRawLen = {fileRawLen:,}\n'

                fileNameLast = fileReadName

            # now have processed all lines in that file that allows read
            #if fileRead.mode == 'r':
            fileRead.close()
            print()

        # now have processed all files in that directory
        #for fileCounter in range(fileListLen):

    # now have processed all lines in all directories
    #for directoryCounter in range(directoryListLen):

    # blank out the last printed filename
    print('\r                                                                              ' \
        + '                                                                                ')

    if not rawLen:
        print()
        print()
        print(' ========== FATAL ERROR: no data file loaded')
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    ###################################################################################

    print(f'                         Total           samples read   = {rawLen:,}')
    print(f'                         Total Reference samples read   = {refQty:,}')
    print(f'                         Total Antenna   samples read   = {rawLen - refQty:,}')
    print()
    studyOutString += f'\n Total           samples read   = {rawLen:,}'
    studyOutString += f'\n Total Reference samples read   = {refQty:,}'
    studyOutString += f'\n Total Antenna   samples read   = {rawLen - refQty:,}\n'


    # prepare to process data

    if ezRAObsLat  == -999:                         # if still silly program default
        ezRAObsLat  = ezRAObsLatFile                # ezRAObsLatFile is better than nothing
    print('   ezRAObsLat  = ', ezRAObsLat)

    if ezRAObsLon  == -999:                         # if still silly program default
        ezRAObsLon  = ezRAObsLonFile                # ezRAObsLonFile is better than nothing
    print('   ezRAObsLon  = ', ezRAObsLon)

    if ezRAObsAmsl == -999:                         # if still silly program default
        ezRAObsAmsl = ezRAObsAmslFile               # ezRAObsAmslFile is better than nothing
    print('   ezRAObsAmsl = ', ezRAObsAmsl)

    if not ezRAObsName:                             # if still silly program default
        ezRAObsName = ezRAObsNameFile               # ezRAObsNameFile is better than nothing
    print('   ezRAObsName = ', ezRAObsName)
    
    if ezRAObsLat < -90 or 90 < ezRAObsLat:
        print()
        print()
        print()
        print(f' ========== FATAL ERROR:  ezRAObsLat = {ezRAObsLat} is silly')
        print('                            Required: -90 <= ezRAObsLat <= +90')
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezRAObsLon < -180 or 180 < ezRAObsLon:
        print()
        print()
        print()
        print(f' ========== FATAL ERROR:  ezRAObsLon = {ezRAObsLon} is silly')
        print('                            Required: -180 <= ezRAObsLon <= +180')
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()

    if ezConAzimuth != -999:                            # if not silly program default
        print('   ezConAzimuth = ', ezConAzimuth)
        # add correction factor to simulated file's Azimuth   (Degrees)
        dataAzimuthDeg = ezConAzimuth + ezConAddAzDeg
        # force dataAzimuthDeg into every RAW sample
        azimuthDeg.fill(dataAzimuthDeg)

    if ezConElevation != -999:                          # if not silly program default
        print('   ezConElevation = ', ezConElevation)
        # add correction factor to simulated file's Elevation (Degrees)
        dataElevationDeg = ezConElevation + ezConAddElDeg
        # force dataElevationDeg into every non-REF RAW sample
        for n in range(rawLen):
            if elevationDeg[n] != dataElevationRefDeg:  # if not marked as a REF sample
                elevationDeg[n] = dataElevationDeg

    # Status after data files: Now have ezRAObsLat ezRAObsLon ezRAObsAmsl ezRAObsName
    # fileFreqMin fileFreqMax fileFreqBinQty fileNameLast rawLen refQty
    # azimuthDeg[rawLen] elevationDeg[rawLen] dataTimeUtc[rawLen] raw[fileFreqBinQty * rawLen]

    # reshape into raw[n, fileFreqBinQty]
    raw = raw.reshape(-1, fileFreqBinQty)
    #print('raw.shape = ', raw.shape)

    # make into raw[fileFreqBinQty, n] to match what is needed for Seaborn heatmap plots
    raw = raw.T
    #print('raw.shape = ', raw.shape)

    # if automated setting of ezConAntXInput
    if ezConAntXInput == -1:
        if 1 < refQty:
            ezConAntXInput =  6
            print('\n   ezConAntXInput changed to 6 for AntRB')
        else :
            ezConAntXInput =  4
            print('\n   ezConAntXInput changed to 4 for AntB')



def openFileSdre():
    # In case it will eventually error.  Creates fileWriteNameSdre, fileWriteSdre

    global fileNameLast             # string
    global fileWriteNameSdre        # string                creation
    global fileWriteSdre            # file handle           creation

    print()
    print('   openFileSdre ===============')

    ## data/rqv8ezb220218_00a.txt
    #                        4321-
    fileWriteNameSdre = fileNameLast.split(os.path.sep)[-1][:-4] + '.sdre'
    print('   opening', fileWriteNameSdre)

    # before much calculating, get proof can open output file
    fileWriteSdre = open(fileWriteNameSdre, 'w')
    if not (fileWriteSdre.mode == 'w'):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Can not open ')
        print(' ' + fileWriteNameSdre)
        print(' file to write data out')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()



def openFileEzb():
    # In case it will eventually error.  Creates fileWriteNameEzb, fileWriteEzb

    global fileNameLast             # string
    global fileWriteNameEzb         # string                creation
    global fileWriteEzb             # file handle           creation

    print()
    print('   openFileEzb ===============')

    ## data/rqv8ezb220218_00a.txt
    #                        4321-
    fileWriteNameEzb = fileNameLast.split(os.path.sep)[-1][:-4] + '.ezb'
    print('   opening', fileWriteNameEzb)

    # before much calculating, get proof can open output file
    fileWriteEzb = open(fileWriteNameEzb, 'w')
    if not (fileWriteEzb.mode == 'w'):
        print()
        print()
        print()
        print()
        print()
        print(' ========== FATAL ERROR:  Can not open ')
        print(' ' + fileWriteNameEzb)
        print(' file to write data out')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()



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
    fileWriteNameStudy = 'ezConStudy' + fileNameLast.split(os.path.sep)[-1][:-4] + '.txt'
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
        print(' file to write data out')
        print()
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()
        
    fileWriteStudy.write(studyOutString)        # finally have file to write to

    # free studyOutString memory
    studyOutString = []
    studyOutString = None
    del studyOutString



def rawPlotPrep():
    # creates rawLenM1, freqStep, dopplerSpanD2, freqCenter, titleS, yTickHeatL, byFreqBinX

    global rawLen                   # integer
    global rawLenM1                 # integer               creation

    global ezRAObsName              # string
    global fileNameLast             # string
    global fileFreqMin              # float
    global fileFreqMax              # float
    global fileFreqBinQty           # integer

    global freqStep                 # float                 creation
    global dopplerSpanD2            # float                 creation
    global freqCenter               # float                 creation
    global titleS                   # string                creation

    global yTickHeatL               # string list           creation
    global byFreqBinX               # float array           creation

    print()
    print('   rawPlotPrep ===============')

    rawLenM1 = rawLen - 1

    print('                         fileFreqMin =', fileFreqMin)
    print('                         fileFreqMax =', fileFreqMax)

    freqStep = (fileFreqMax - fileFreqMin) / (fileFreqBinQty - 1)
    print('                         freqStep =', freqStep)

    # Doppler spans -dopplerSpanD2 thru +dopplerSpanD2
    dopplerSpanD2 = (fileFreqMax - fileFreqMin) / 2.
    print('                         dopplerSpanD2 =', dopplerSpanD2)

    freqCenter = (fileFreqMin + fileFreqMax) / 2.
    print('                         freqCenter =', freqCenter)

    # plot titles
    titleS = '  ' + fileNameLast.split(os.path.sep)[-1] + '           ' + ezRAObsName \
        + '          (' + programName + ')'

    # heatmap Doppler Y scale labels
    # dopplerSpanD2 = 1.2
    # dopplerSpanD2 = 5.0
    if f'{dopplerSpanD2:0.1f}' == '1.2':
        yTickHeatL = \
            ['-1.2', '', '-1.',
            '',  '', '',  '', '-0.5',
            '',  '',  '',  '',  '0.',
            '',  '', '',  '',  '0.5',
            '',  '',  '',  '',  '1.', '', '1.2', '']
    else:
        yTickHeatL = \
            [f'{-dopplerSpanD2:0.1f}',        f'{-dopplerSpanD2*11./12.:0.1f}',
            f'{-dopplerSpanD2*10./12.:0.1f}', f'{-dopplerSpanD2*9./12.:0.1f}',
            f'{-dopplerSpanD2*8./12.:0.1f}',  f'{-dopplerSpanD2*7./12.:0.1f}',
            f'{-dopplerSpanD2*6./12.:0.1f}',  f'{-dopplerSpanD2*5./12.:0.1f}',
            f'{-dopplerSpanD2*4./12.:0.1f}',  f'{-dopplerSpanD2*3./12.:0.1f}',
            f'{-dopplerSpanD2*2./12.:0.1f}',  f'{-dopplerSpanD2*1./12.:0.1f}',
            f'0.', f'{dopplerSpanD2*1./12.:0.1f}',
            f'{dopplerSpanD2*2./12.:0.1f}',   f'{dopplerSpanD2*3./12.:0.1f}',
            f'{dopplerSpanD2*4./12.:0.1f}',   f'{dopplerSpanD2*5./12.:0.1f}',
            f'{dopplerSpanD2*6./12.:0.1f}',   f'{dopplerSpanD2*7./12.:0.1f}',
            f'{dopplerSpanD2*8./12.:0.1f}',   f'{dopplerSpanD2*9./12.:0.1f}',
            f'{dopplerSpanD2*10./12.:0.1f}',  f'{dopplerSpanD2*11./12.:0.1f}',
            f'{dopplerSpanD2:0.1f}', '']
    #print('========================= dopplerSpanD2 =', dopplerSpanD2)
    #print('========================= yTickHeatL =', yTickHeatL)

    # increasing freq
    byFreqBinX = np.arange(fileFreqBinQty) * freqStep - dopplerSpanD2



def ezConRefAvgPluckQtyLDo():

    #global azimuthDeg               # float array
    #global elevationDeg             # float array
    #global dataTimeUtc              # 'astropy.time.core.Time' object array
    #global ant                      # float 2d array
    global ref                      # float 2d array
    #global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    global antLen                   # integer
    #global refLen                   # integer
    #global refLenM1                 # integer

    global ezConRefAvgPluckQtyL     # float list

    if not ezConRefAvgPluckQtyL:    # if empty, no plucking needed
        return(1)

    #print(f'   before ezConRefAvgPluckQtyL, refLen = ', {refLen:,}')

    print()
    print('   ezConRefAvgPluckQtyLDo ===============')

    print('   np.shape(ref)[0] =', np.shape(ref)[0])
    print('   np.shape(ref)[1] =', np.shape(ref)[1])

    # create refAvg
    refAvg = np.mean(ref, axis=0)
    #print('   refAvg =', refAvg)
    print(f'   len(refAvg) = {len(refAvg):,}')
    print()

    # get indexes of refAvg with increasing values
    refAvgIdxByIncreasing = refAvg.argsort()
    #print('   refAvgIdxByIncreasing =', refAvgIdxByIncreasing)
    print(f'   len(refAvgIdxByIncreasing) = {len(refAvgIdxByIncreasing):,}')
    print()

    print('   ezConRefAvgPluckQtyL =', ezConRefAvgPluckQtyL)
    print()

    # assume want to keep all refAvg samples
    refAvgPluckNumKeepMask = np.ones(antLen, dtype=bool)

    # mask off requested lowest-valued refAvg samples
    for i in range(ezConRefAvgPluckQtyL[0]):                 # i increases up from 0
        refAvgPluckNumKeepMask[refAvgIdxByIncreasing[i]] = False

    # mask off requested highest-valued refAvg samples
    for i in reversed(range(ezConRefAvgPluckQtyL[1])):       # i decreases down to 0
        refAvgPluckNumKeepMask[refAvgIdxByIncreasing[-1-i]] = False

    # replace the Ref of not-kept REF samples
    if not refAvgPluckNumKeepMask[0]:
        # Ref index is 0
        # Matching ANT needs to use next future kept REF sample.
        # Use Ref from lowest index of True in refAvgPluckNumKeepMask.
        indexFirstKept = np.where(refAvgPluckNumKeepMask)[0][0]
        print('   indexFirstKept =', indexFirstKept)
        ref[:, 0] = ref[:, indexFirstKept]
    for i in range(1, len(refAvgPluckNumKeepMask)):          # i increases up from 1
        # Ref index is greater than 0
        if not refAvgPluckNumKeepMask[i]:                    # if Ref not to be kept
            # replace the Ref with next older REF sample
            ref[:, i] = ref[:, i-1]

    #print('   refAvgPluckNumKeepMask =', refAvgPluckNumKeepMask)
    print('   refAvgPluckNumKeepMask.sum() =', refAvgPluckNumKeepMask.sum())
    print(f'   len(refAvgPluckNumKeepMask) = {len(refAvgPluckNumKeepMask):,}')

    #azimuthDeg   = azimuthDeg  [refAvgPluckNumKeepMask]
    #elevationDeg = elevationDeg[refAvgPluckNumKeepMask]
    #dataTimeUtc  = dataTimeUtc [refAvgPluckNumKeepMask]
    ##rawIndex    = rawIndex    [refAvgPluckNumKeepMask]
    #ant          = ant      [:, refAvgPluckNumKeepMask]
    #ref          = ref      [:, refAvgPluckNumKeepMask]
    #antLen   = ant.shape[1]
    #antLenM1 = antLen - 1
    refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    print(f'   refLen = {refLen:,}')



def ezConRefAvgPluckFracLDo():

    #global azimuthDeg               # float array
    #global elevationDeg             # float array
    #global dataTimeUtc              # 'astropy.time.core.Time' object array
    #global ant                      # float 2d array
    global ref                      # float 2d array
    #global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    #global antLen                   # integer
    #global antLenM1                 # integer
    #global refLen                   # integer
    #global refLenM1                 # integer
    global xTickLocsAnt             # float array

    global ezConRefAvgPluckFracL    # float list

    if not ezConRefAvgPluckFracL:   # if empty, no plucking needed
        return(1)

    #print(f'   before ezConRefAvgPluckFracLDo, antLen = ', {antLen:,}')

    print()
    print('   ezConRefAvgPluckFracLDo ===============')

    print('   np.shape(ref)[0] =', np.shape(ref)[0])
    print('   np.shape(ref)[1] =', np.shape(ref)[1])

    refAvg = np.mean(ref, axis=0)
    #print('   refAvg =', refAvg)
    print(f'   len(refAvg) = {len(refAvg):,}')
    print()

    # get indexes of increasing refAvg
    refAvgIdxByIncreasing = refAvg.argsort()
    #print('   refAvgIdxByIncreasing =', refAvgIdxByIncreasing)
    print(f'   len(refAvgIdxByIncreasing) = {len(refAvgIdxByIncreasing):,}')
    print()

    print('   ezConRefAvgPluckFracL =', ezConRefAvgPluckFracL)
    print()

    # snap down to next integer
    refLenM1 = ref.shape[1] - 1
    refAvgPluckFracQty0 = int(refLenM1 * ezConRefAvgPluckFracL[0])
    refAvgPluckFracQty1 = int(refLenM1 * ezConRefAvgPluckFracL[1])

    # assume want to keep all refAvg samples
    refAvgPluckFracKeepMask = np.ones(antLen, dtype=bool)

    # mask off requested lowest-valued refAvg samples
    for i in range(refAvgPluckFracQty0):     # i starts with 0
        refAvgPluckFracKeepMask[refAvgIdxByIncreasing[i]] = False
    # mask off requested highest-valued refAvg samples
    for i in range(refAvgPluckFracQty1):     # i starts with 0
        refAvgPluckFracKeepMask[refAvgIdxByIncreasing[-1-i]] = False

    # replace the Ref of not-kept REF samples
    if not refAvgPluckFracKeepMask[0]:
        # Ref index is 0
        # Matching ANT needs to use next future kept REF sample.
        # Use Ref from lowest index of True in refAvgPluckFracKeepMask.
        indexFirstKept = np.where(refAvgPluckFracKeepMask)[0][0]
        print('   indexFirstKept =', indexFirstKept)
        ref[:, 0] = ref[:, indexFirstKept]
    for i in range(1, len(refAvgPluckFracKeepMask)):          # i increases up from 1
        # Ref index is greater than 0
        if not refAvgPluckFracKeepMask[i]:                    # if Ref not to be kept
            # replace the Ref with next older REF sample
            ref[:, i] = ref[:, i-1]

    print('   refAvgPluckFracKeepMask =', refAvgPluckFracKeepMask)
    print('   refAvgPluckFracKeepMask.sum() =', refAvgPluckFracKeepMask.sum())
    print(f'   len(refAvgPluckFracKeepMask) = {len(refAvgPluckFracKeepMask):,}')

    #azimuthDeg   = azimuthDeg  [refAvgPluckFracKeepMask]
    #elevationDeg = elevationDeg[refAvgPluckFracKeepMask]
    #dataTimeUtc  = dataTimeUtc [refAvgPluckFracKeepMask]
    ##rawIndex    = rawIndex    [refAvgPluckFracKeepMask]
    #ant          = ant      [:, refAvgPluckFracKeepMask]
    #ref          = ref      [:, refAvgPluckFracKeepMask]
    #antLen   = ant.shape[1]
    #antLenM1 = antLen - 1
    refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    print(f'   refLen = {refLen:,}')



def ezConRawFreqBinHideLDo():
    # filter raw freq bins

    global ezConRawFreqBinHideL     # integer list
    global raw                      # float 2d array
    global fileFreqBinQty           # integer

    print()
    print('   ezConRawFreqBinHideLDo ===============')

    # Hide frequency bin numbers in ezConRawFreqBinHideL.
    # If bin > 0, copy from lessor neighbor freq bin.
    print()
    for i in range(len(ezConRawFreqBinHideL)):
        ezConRawFreqBinHide = ezConRawFreqBinHideL[i]

        # 110% increase a frequency bin, to raise as a freqBin marker
        #raw[ezConRawFreqBinHide, :] = 1.1 * raw[ezConRawFreqBinHide, :]

        # find averages of freqBin neighbors
        # give non-existing freqBin neighbors very high averages, to ignore later
        if ezConRawFreqBinHide <= 0:
            freqBinLowerAvg  = 999999.
        else:
            freqBinLowerAvg  = np.mean(raw[ezConRawFreqBinHide - 1, :], axis=0)
        if ezConRawFreqBinHide >= fileFreqBinQty - 1:
            freqBinHigherAvg = 999999.
        else:
            freqBinHigherAvg = np.mean(raw[ezConRawFreqBinHide + 1, :], axis=0)

        # hide with the freqBin neighbor having lowest average
        if freqBinLowerAvg < freqBinHigherAvg:
            #print('   ezConRawFreqBinHideL[' + str(i) + '] = ' + str(ezConRawFreqBinHide))
            print(f'   ezConRawFreqBinHideL[{i:d}] = {ezConRawFreqBinHide:d}, using lower  freqBin neighbor')
            raw[ezConRawFreqBinHide, :] = raw[ezConRawFreqBinHide - 1, :]
        else:
            #print('   ezConRawFreqBinHideL[' + str(i) + '] = ' + str(ezConRawFreqBinHide))
            print(f'   ezConRawFreqBinHideL[{i:d}] = {ezConRawFreqBinHide:d}, using higher freqBin neighbor')
            raw[ezConRawFreqBinHide, :] = raw[ezConRawFreqBinHide + 1, :]

    if ezConRawFreqBinHideL:        # if just printed any in ezConRawFreqBinHideL
        print()



def createRefNeg(ezConRefMode):
    # ezConRefMode < 0: ref = Nth ANT sample spectrum
    # Create maskRawAnt, maskRawRef, ant, ref, antLen, antLenM1 .
    # Data arrays are already thinned to only ANT samples: azimuthDeg, elevationDeg, dataFileIdx, dataTimeUtc, raw .

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    # for ezConRefMode < 0, create maskRawRef and maskRawAnt
    print()
    print('   createRefNeg ===============')

    # creation: ezConRefMode < 0, so all raw samples are ANT samples
    maskRawAnt = np.ones(rawLen, dtype=bool)    # creation

    ant = raw + 0.                              # creation
    antLen = rawLen + 0                         # creation
    print(f' antLen = {antLen:,}')
    antLenM1 = antLen - 1                       # creation

    # remember, ezConRefMode is negative
    refIndex = min(-ezConRefMode, antLen - 1)
    print(f' refIndex = {refIndex:,}')
    maskRawRef = np.zeros(rawLen, dtype=bool)
    maskRawRef[refIndex] = True     # creation: ezConRefMode < 0, so ref = refIndex-th ANT sample spectrum

    ref = np.empty_like(ant)
    refLast = raw[:, refIndex]
    for n in range(antLen):
        ref[:, n] = refLast                     # creation

    # raw plots for ezConRefMode < 0
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt



def createRef00antSampleZero():
    # ezConRefMode == 0: no REF samples, ref = ANT sample spectrum zero
    # Create maskRawAnt, maskRawRef, ant, ref, antLen, antLenM1 .
    # Data arrays are already thinned to only ANT samples: azimuthDeg, elevationDeg, dataFileIdx, dataTimeUtc, raw .

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    # for ezConRefMode == 0, create maskRawRef and maskRawAnt
    print()
    print('   createRef00antSampleZero ===============')

    # creation: ezConRefMode == 0, so all raw samples are ANT samples
    maskRawAnt = np.ones(rawLen, dtype=bool)    # creation
    maskRawRef = np.zeros(rawLen, dtype=bool)
    maskRawRef[0] = True            # creation: ezConRefMode == 0, so only first raw sample is a REF sample

    ant = raw + 0.                              # creation
    antLen = rawLen + 0                         # creation
    print(f' antLen = {antLen:,}')
    antLenM1 = antLen - 1                       # creation

    ref = np.empty_like(ant)
    refLast = raw[:, 0]                         # ezConRefMode == 0, so first raw sample is the REF sample
    for n in range(antLen):
        ref[:, n] = refLast                     # creation

    # raw plots for ezConRefMode == 0
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt
    plotEzCon201JtimeUtcMjdDBetweenRefRaw()     # using raw, dataTimeUtc, and maskRawRef



def createRef01refIsOne():
    # ezConRefMode == 1: no REF samples, ref = neutral ref spectrum, all ones
    # Create maskRawAnt, maskRawRef, ant, ref, antLen, antLenM1 .
    # Data arrays are already thinned to only ANT samples: azimuthDeg, elevationDeg, dataFileIdx, dataTimeUtc, raw .

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    # for ezConRefMode == 1, create maskRawRef and maskRawAnt
    print()
    print('   createRef01refIsOne ===============')

    # creation: ezConRefMode == 1, so all raw samples are ANT samples
    maskRawAnt = np.ones(rawLen, dtype=bool)
    # creation: ezConRefMode == 1, so no  raw samplea are REF samples
    maskRawRef = np.zeros(rawLen, dtype=bool)

    ant = raw + 0.                              # creation
    antLen = rawLen + 0                         # creation
    print(f' antLen = {antLen:,}')
    antLenM1 = antLen - 1                       # creation

    ref = np.ones_like(ant)

    # raw plots for ezConRefMode == 1
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt
    plotEzCon201JtimeUtcMjdDBetweenRefRaw()     # using raw, dataTimeUtc, and maskRawRef



def createRef02rawByFreqBinAvg():
    # ezConRefMode == 2: no REF samples, ref = rawByFreqBinAvg spectrum

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    print()
    print('   createRef02rawByFreqBinAvg ===============')

    ant = raw + 0.                              # creation
    maskRawAnt = np.ones(rawLen, dtype=bool)    # creation
    maskRawRef = np.zeros(rawLen, dtype=bool)   # creation
    antLen = rawLen + 0                         # creation
    print(f' antLen = {antLen:,}')
    antLenM1 = antLen - 1                       # creation

    # create ref
    ref = np.empty_like(raw)
    rawByFreqBinAvg = np.mean(raw, axis=1)
    for n in range(rawLen):
        ref[:, n] = rawByFreqBinAvg

    # raw plots for ezConRefMode == 2
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt



#XXXXXXXXXXXXXXXXXXXXXXXX incomplete XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def createRef04closestQuietRAAnt():
##########################################################################################
# I broke ezConRefMode == 4 with 'sdrVel08g7.py' (no RA available)
##########################################################################################
    # ezConRefMode == 4: no REF samples, ref = ANT spectrum of average of closest (quiet)
    #      RA=refWantedRaDegA or refWantedRaDegB degrees, depending on declination

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawLen                   # integer
    global antLen                   # integer           creation
    #global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    print()
    print('   createRef04closestQuietRAAnt ===============')

    #print('1111111111111111')
    #refWantedRaDeg = 165.     # RA in degrees (11   hours), for ezConRefMode = 2
    refWantedRaDeg  = 172.5      # RA in degrees (11.5 hours), for ezConRefMode = 2
    refWantedRaDegA = 172.5     # RA in degrees (11.5 hours) for -45 <= Dec
    refWantedRaDegB =   0.      # RA in degrees (11.5 hours) for Dec <= 40

    ref = np.empty_like(ant)
    refLast = ant[:, 0]        # in case do not find refWantedRaDeg
    refWantedRaDeg180 = refWantedRaDeg + 180.
    refIndexStart = 0
    while (refIndexStart < antLen):
        #print('2222222222')
        # find first index where refWantedRaDeg<=RA
        refIndex = refIndexStart

        # find first index where RA<=refWantedRaDeg
        while refIndex < antLen:
            #print('7777777777777777')
            if  ezConOut[refIndex, 1] <= refWantedRaDeg:
                break
            refIndex += 1

        #while ezConOut[refIndex, 1] < refWantedRaDeg and refIndex < antLen:
        #    refIndexThis += 1
        # find first index where refWantedRaDeg<=RA
        while refIndex < antLen:
            #print('333333333333')
            if  refWantedRaDeg <= ezConOut[refIndex, 1]:
                break
            refIndex += 1
            
        #if refWantedRaDeg <= ezConOut[refIndex, 1]:
        #print('44444444444444 ezConOut[refIndex, 1]=', ezConOut[refIndex, 1])
        #print('44444444444444  refIndex=', refIndex)
        if refIndex < antLen:
            #print('44444444444444 ezConOut[refIndex, 1]=', ezConOut[refIndex, 1])
            # if found refWantedRaDeg, record ant from (RA=refWantedRaDeg index) as refLast
            # else use the previous refLast
            refLast = ant[:, refIndex]
            
        # find first index where refWantedRaDeg180<=RA
        #while ezConOut[refIndex, 1] < refWantedRaDeg180 and refIndex < antLen:
        #    refIndex += 1
        #print('555555555555555')
        while refIndex < antLen:
            if  refWantedRaDeg180 <= ezConOut[refIndex, 1]:
                break
            refIndex += 1

        # record either refWantedRaDeg180<=RA index or antLen
        refIndexStop = refIndex

        # paint ref section with refLast spectrum
        #print('66666666666666666')
        for n in range(refIndexStart, refIndexStop):
            #print('66666666666666666aaaaaaaaaaaa')
            ref[:, n] = refLast
            
        # prepare for hunt in next section
        refIndexStart = refIndexStop

        #print('888888888888888 refIndexStart=', refIndexStart)
        #print('                antLen=', antLen)
        #print('                refIndexStop=', refIndexStop)
        #print('                refIndex=', refIndex)



#XXXXXXXXXXXXXXXXXXXXXXXX incomplete XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def createRef05MinimumAvgAnt():
##########################################################################################
# Did I break ezConRefMode == 5 with 'sdrVel08g7.py' ????????????
##########################################################################################
    # ezConRefMode == 5: no REF samples, ref = champion list: ant spectrum of
    #   (minimum average of ant in last 0.5 days)
    #   (ezConRefMode=2 was ref within 1.0 days, but want more often.  0.5 days seems achievable)
    
    global ezConBaselineLowFreqBin  # integer
    global ezConBaselineHighFreqBin # integer

    print()
    print('   createRef05MinimumAvgAnt ===============')

    dayFraction       = 10.
    ref = ant + 0.                  # copy ant[:]
    timeUtcMjdLast    = 0.          # silly value
    azimuthDegLast    = 99999.9     # silly value
    elevationDegLast  = 99999.9     # silly value
    #availableScoreMin = 99999.9     # silly value
    for n in range(antLen):
        #print('1111111111111 n =', n)
        timeUtcMjdThis   = ezConOut[n, 0]
        azimuthDegThis   = azimuthDeg[n]
        elevationDegThis = elevationDeg[n]
        # average of center of this spectrum, smaller is better score
        #scoreThis = ant[ezConBaselineLowFreqBin:-ezConBaselineHighFreqBin, n].sum() \
        #    / (samplesQty - ezConBaselineLowFreqBin - ezConBaselineHighFreqBin)
        scoreThis = ant[ezConBaselineLowFreqBin:-ezConBaselineHighFreqBin, n].sum() \
            / (antLen - ezConBaselineLowFreqBin - ezConBaselineHighFreqBin)

        #print('1111111111111 azimuthDegThis =', azimuthDegThis)
        #print('1111111111111 azimuthDegLast =', azimuthDegLast)
        #print('1111111111111111 elevationDegThis  =', elevationDegThis)
        #print('1111111111111111 elevationDegLast  =', elevationDegLast)
        #print('1111111111111111111 timeUtcMjdThis =', timeUtcMjdThis)
        #print('1111111111111111111 timeUtcMjdLast =', timeUtcMjdLast)
        if ((azimuthDegThis == azimuthDegLast) and (elevationDegThis == elevationDegLast) \
            and ((timeUtcMjdThis - timeUtcMjdLast) <= dayFraction)):

            #print('2222222222')
            # repeatedly: if 0.5 days old is < oldest available, remove oldest available
            while dayFraction < timeUtcMjdThis - availableTimeUtcMjd[-1]:
                #print('333333333')
                #availableIndexL   = availableIndexL[:-1]        # ordered new to old
                #availableFavoredL = availableFavoredL[:-1]      # ordered new to old
                #availableScoreL   = availableScoreL[:-1]        # ordered new to old
                del availableTimeUtcMjd[0]  # ordered new to old
                del availableScoreL[0]      # ordered new to old
                del availableIndexL[0]      # ordered new to old

            # is scoreThis better than all in availableScoreL ?
            # improve every ref of availableIndexL ?
            availableScoreMin = min(availableScoreL + [99999.9])     # with silly value for empty list
            if scoreThis < availableScoreMin:
                #print('4444444444')
                #availableScoreMin = scoreThis
                spectrumThis = ant[:, n]
                for i in availableIndexL:
                    #print('55555555555')
                    ref[:, i] = spectrumThis
            else:
                #print('666666666666')
                availableBest = availableScoreL.index(availableScoreMin) # index of first match in list
                ref[:, n] = ant[:, availableIndexL[availableBest]]

            # add new to front of available lists
            #print('77777777777')
            availableTimeUtcMjd = [timeUtcMjdThis] + availableTimeUtcMjd      # ordered new to old
            availableScoreL     = [scoreThis]      + availableScoreL          # ordered new to old
            availableIndexL     = [n]              + availableIndexL          # ordered new to old

        else:
            # reset timeUtcMjdLast, azimuthDegLast, elevationDegLast, and available records
            #print('88888888888')
            timeUtcMjdLast      = timeUtcMjdThis
            azimuthDegLast      = azimuthDegThis
            elevationDegLast    = elevationDegThis
            availableTimeUtcMjd = [timeUtcMjdThis]
            availableScoreL     = [scoreThis]
            availableIndexL     = [n]
            #availableScoreMin   = scoreThis
            #indexReset          = n
            # already ref[:, n]  = ant[:, n]
            #print('8888888888 timeUtcMjdLast =', timeUtcMjdLast)



#XXXXXXXXXXXXXXXXXXXXXXXX incomplete XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def createRef07minimumAntBAvgAnt():
    # ezConRefMode == 7: no REF samples, for each sample, ref is the ant spectrum where
    #   antB is the minimum for all antB in the time window

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    global ezConAntBaselineFreqBinsFracL        # float list

    print()
    print('   createRef07minimumAntBAvgAnt ===============')

    ant = raw + 0.                              # creation
    maskRawAnt = np.ones(rawLen, dtype=bool)    # creation
    antLen = rawLen + 0                         # creation
    print(f' antLen = {antLen:,}')
    antLenM1 = antLen - 1                       # creation

    # Create ref.
    # Problem: antB and antBAvg not made yet.
    # Well, ignore later antFreqBinHide() and antRfiRemoval() and duplicate code and create it now.
    # Code from plotEzCon241antBaseline(), plotEzCon047antB(), and plotEzCon114antBAvg().

    # In each ant sample spectrum, hydrogen appears in the center frequencies,
    # so average the low and high frequency values.
    # Create antBaseline with ant, and ezConAntBaselineFreqBinsFracL .
    print('                         ezConAntBaselineFreqBinsFracL =', ezConAntBaselineFreqBinsFracL)
    ezConAntBaselineFreqBin = np.empty(4, dtype=int)
    for i in range(4):
        ezConAntBaselineFreqBin[i] = int(ezConAntBaselineFreqBinsFracL[i] * (fileFreqBinQty - 1))
    print('                         ezConAntBaselineFreqBin =', ezConAntBaselineFreqBin)
    print('                           of fileFreqBinQty =', fileFreqBinQty)
    # for each sample, average the ant values (from [0] to [1]) and (from [2] to [3])
    antBaseline = (np.sum(ant[ezConAntBaselineFreqBin[0]:ezConAntBaselineFreqBin[1], :], axis=0) \
        + np.sum(ant[ezConAntBaselineFreqBin[2]:ezConAntBaselineFreqBin[3], :], axis=0)) \
        / ((ezConAntBaselineFreqBin[1] - ezConAntBaselineFreqBin[0]) \
        + (ezConAntBaselineFreqBin[3] - ezConAntBaselineFreqBin[2]))
    #print('np.shape(antBaseline) =', np.shape(antBaseline))

    # create antB
    antB = ant / antBaseline
    #print('np.shape(antB) =', np.shape(antB))
    #print('np.sum(antB) =', np.sum(antB))

    antBAvg = np.mean(antB, axis=0)

    # create the array of indices whose samples would sort antB in increasing value order
    antBIncIndx = antBAvg.argsort()
    # create the array of MJD times whose samples would sort antB in increasing value order
    antBIncTimes = dataTimeUtc[antBIncIndx]

    # fill maskRawRef and ref
    maskRawRef = np.zeros(rawLen, dtype=bool)       # most samples are not a source of a ref spectrum
    #print(' maskRawRef + 0 =', maskRawRef + 0)
    ref = np.empty_like(ant)
    timeWindowD2 = 0.5      # 1 day window / 2 = 0.5 days       creation
    indexOfFirstTrueLast = -9999        # silly number
    print()
    for n in range(antLen):                            # for each sample
        print('\r    ', n, '  of', antLenM1, '      ', end='')   # allow append to line
        timeThis = dataTimeUtc[n]               # this sample's time in MJD
        # mark antBIncTimes element True if in time window around sample's time (timeThis)
        #timesLow = antBIncTimes < (timeThis + timeWindowD2)
        #timesHigh = (timeThis - timeWindowD2) <= antBIncTimes
        # what samples are in the timeThis window
        antBIncTimesMaskThis = np.logical_and(antBIncTimes < timeThis + timeWindowD2,
            timeThis - timeWindowD2 <= antBIncTimes)
        # https://www.geeksforgeeks.org/python-first-occurrence-of-true-number/
        indexOfFirstTrue = next((i for i, j in enumerate(antBIncTimesMaskThis) if j), None)
        # ref is the ant spectrum where antB is the minimum for all antB in the time window
        ref[:, n] = ant[:, indexOfFirstTrue]
        maskRawRef[indexOfFirstTrue] = True     # this ant spectrum was used for a ref spectrum
        if indexOfFirstTrue != indexOfFirstTrueLast:
            print('ref used from sample', indexOfFirstTrue, '      \n')
        indexOfFirstTrueLast = indexOfFirstTrue

    # raw plots for ezConRefMode == 7
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt
    plotEzCon201JtimeUtcMjdDBetweenRefRaw()     # using raw, dataTimeUtc, and maskRawRef



def createRef10lastRefMarkedInData():
    # ezConRefMode == 10: REF = last REF marked in data
    # Create maskRawAnt, maskRawRef, ant, ref, antLen, antLenM1 .
    # Thin data arrays to only ANT samples: azimuthDeg, elevationDeg, dataFileIdx, dataTimeUtc, raw .

    global azimuthDeg               # float array
    global elevationDeg             # float array
    global dataFileIdx              # integer array
    global dataTimeUtc              # 'astropy.time.core.Time' object array

    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawIndex                 # integer array
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation
    #global refLen                   # integer
    #global refLenM1                 # integer

    global ezConRefAvgPluckFracL    # float array
    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    # for ezConRefMode == 10, create maskRawRef and maskRawAnt
    print()
    print('   createRef10lastRefMarkedInData ===============')

    maskRawRef = 400. < elevationDeg       # creation: mark true if is a REF raw sample (see dataElevationRefDeg)
    maskRawAnt = np.logical_not(maskRawRef) # creation: ezConRefMode == 10, so otherwise is an ANT raw sample
    antLen = sum((maskRawAnt + 0))              # creation
    print(f' antLen = {antLen:,}')
    antLenM1 = antLen - 1                       # creation

    #if ezConRefAvgKeepFracL:                    # if plucking requested
    if 0:
        # remove those bad raw samples which would be REF samples, using ezConRefAvgKeepFracL
        
        print()
        print(f'   before refAvgKeepFrac, rawLen = {len(elevationDeg):,}')
        refLen = sum((maskRawRef + 0))          # temporary refLen,   ignored later
        refLenM1 = refLen - 1                   # temporary refLenM1, ignored later
        print(f'   before refAvgKeepFrac, refLen = {refLen:,}')

        print()
        print('   === refAvgKeepFrac ===============')

        ref = raw[:, maskRawRef]                # temporary ref array, ignored later
        print('   np.shape(ref)[0] =', np.shape(ref)[0])
        print('   np.shape(ref)[1] =', np.shape(ref)[1])

        # on spectrum of refAvg values, find ezConRefAvgKeepFracL fraction values
        refAvg = np.mean(ref, axis=0)
        print(f'   len(refAvg) = {len(refAvg):,}')
        refAvgSort = np.sort(refAvg)            # sorted by value
        print('   refAvgSort =', refAvgSort)
        print(f'   len(refAvgSort) = {len(refAvgSort):,}')

        refAvgKeepValue0 = refAvgSort[int(antLenM1 * ezConRefAvgKeepFracL[0])]
        refAvgKeepValue1 = refAvgSort[int(antLenM1 * ezConRefAvgKeepFracL[1])]
        print('   refAvgKeepValue0 =', refAvgKeepValue0)
        print('   refAvgKeepValue1 =', refAvgKeepValue1)

        # find RAW samples whose rawAvg is between refAvgKeepValue0 and refAvgKeepValue1
        rawAvg = np.mean(raw, axis=0)
        refAvgKeepMask = np.logical_and(refAvgKeepValue0 < rawAvg, rawAvg < refAvgKeepValue1)
        # and is a REF sample
        refAvgKeepMask = np.logical_and(refAvgKeepMask, maskRawRef)     # but only REF samples
        # but allow all ANT samples
        refAvgKeepMask = np.logical_or(refAvgKeepMask, maskRawAnt)
        print('   refAvgKeepMask =', refAvgKeepMask)
        print(f'   refAvgKeepMask.sum() = {refAvgKeepMask.sum():,}')
        print(f'   len(refAvgKeepMask) = {len(refAvgKeepMask):,}')

        # thin most data arrays to only refAvgKeepMask samples
        azimuthDeg   = azimuthDeg  [refAvgKeepMask]
        elevationDeg = elevationDeg[refAvgKeepMask]
        dataFileIdx  = dataFileIdx [refAvgKeepMask]
        dataTimeUtc  = dataTimeUtc [refAvgKeepMask]
        maskRawAnt   = maskRawAnt  [refAvgKeepMask]
        maskRawRef   = maskRawRef  [refAvgKeepMask]
        raw          = raw      [:, refAvgKeepMask]
        rawLen       = np.shape(raw)[1]
        print(f'   rawLen = {rawLen:,}')

        print()
        print(f'   after  refAvgKeepFrac, rawLen = {len(elevationDeg):,}')
        refLen = sum((maskRawRef + 0))          # temporary refLen, ignored later
        print(f'   after  refAvgKeepFrac, refLen = {refLen:,}')


    # raw plots for ezConRefMode == 10 (before data thinning soon)
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt
    plotEzCon201JtimeUtcMjdDBetweenRefRaw()     # using raw, dataTimeUtc, and maskRawRef

    # create ref: for every ant, the last REF raw spectrum
    ref = np.empty_like(raw)                    # to be thinned soon, to just the ANT samples
    refLast = raw[:, 0]                         # temporary refLast spectrum, backfilled soon
    refIndexFirst = -1                          # silly value, assumes at least one REF
    for n in range(rawLen):
        if maskRawAnt[n]:
            # n is an ANT sample
            ref[:, n] = refLast
        else:
            # ezConRefMode == 10, so n is a REF sample
            refLast = raw[:, n]
            # remember index and spectrum of first REF
            if refIndexFirst < 0:
                refIndexFirst = n
                refFirst = refLast
    # backfill first REF spectrum into ref[0] to ref[refIndexFirst]
    print(f'     refIndexFirst = {refIndexFirst:,}')
    for n in range(refIndexFirst):
        if maskRawAnt[n]:
            ref[:, n] = refFirst

    # done with raw data, thin most data arrays to only ANT samples
    azimuthDeg   = azimuthDeg  [maskRawAnt]
    elevationDeg = elevationDeg[maskRawAnt]
    dataFileIdx  = dataFileIdx [maskRawAnt]
    dataTimeUtc  = dataTimeUtc [maskRawAnt]
    rawIndex     = rawIndex    [maskRawAnt]
    ant          = raw     [:,  maskRawAnt]           # creation
    ref          = ref     [:,  maskRawAnt]           # creation
    #raw    = ant + 0. ######################################################## needed ?
    #rawLen = antLen + 0 ######################################################## needed ?



#XXXXXXXXXXXXXXXXXXXXXXXX incomplete XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
def createRef20refPulser():
    # ezConRefMode == 20: no REF samples, ref = refPulser hardware REF detection by software
    # a@u18-200107a:~/rqv3$   python3 EzRA/ezCon10g4L.py   data/n0rqv3ez220319_00.txt

    global azimuthDeg               # float array
    global elevationDeg             # float array
    global dataFileIdx              # integer array
    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global raw                      # float 2d array
    global ant                      # float 2d array    creation
    global ref                      # float 2d array    creation
    global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    global rawLen                   # integer
    global antLen                   # integer           creation
    global antLenM1                 # integer           creation

    global maskRawAnt               # Boolean array     creation
    global maskRawRef               # Boolean array     creation

    global xLabelSRaw               # string
    global xTickLocsRaw             # float array
    global xTickLabelsRaw           # string list

    print()
    print('   createRef20refPulser ===============')

    refPositive = 1                     # are REF sample values > ANT sample values ?
    rawAvg = np.mean(raw, axis=0)
    #print('rawAvg')
    #print(rawAvg)
    # refPulser hardware tries to REF 1 of every 8 samples

    # define 'recent' as a time duration in days
    #recentDurationDays = 1.1 / 24     # history long enough to span between REFs
    recentDurationDays = 0.3 / 24     # history long enough to span between REFs
    print('recentDurationDays =', recentDurationDays)

    # find recentLen index, recentDurationDays in time into the data file samples
    recentLen = 0
    dataTimeUtcZero = dataTimeUtc[0]
    for i in range(1, min(500, rawLen)):
        #print('   i =', recentLen, '   dataTimeUtc[i] - dataTimeUtcZero =', dataTimeUtc[i] - dataTimeUtcZero)
        if recentDurationDays <= (dataTimeUtc[i] - dataTimeUtcZero):
            recentLen = i
            break
    if not recentLen:
        print()
        print('  *** FATAL ERROR:    recentLen = 0')
        print()
        print('\a')     # ring bell
        exit()
    print('recentLen =', recentLen)

    # For each sample value, express the value as a fraction between its recent min and max.
    rawAvgRecentFrac = np.empty(rawLen)
    rawAvgRecentMinA = np.empty(rawLen)
    rawAvgRecentMaxA = np.empty(rawLen)
    for n in range(1, rawLen):
        # In the last recentLen samples, what is the max value ?
        # Find the max of (history long enough to span between REFs)
        # last recentLen samples of rawAvg
        rawAvgRecent = rawAvg[max(0, n - recentLen):n]
        if refPositive:
            rawAvgRecentMax = rawAvgRecent.max()                    # max of those recent samples
            rawAvgRecentMaxA[n] = rawAvgRecentMax                   # remember those maximums

            # In the last recentLen/3 samples, what is the min value ?
            # Find the min of (history only long enough to span across one REF)
            # last recentLen/3 samples of rawAvg
            rawAvgRecent = rawAvg[max(0, int(n - (recentLen / 3))):n]
            rawAvgRecentMin = rawAvgRecent.min()                    # min of those recent samples
            rawAvgRecentMinA[n] = rawAvgRecentMin                   # remember those minimums

            # How different is the current sample value from its recent past ?
            # For the current sample value, express the value as a fraction between its recent min and max.
            rawAvgRecentMaxMin = rawAvgRecentMax - rawAvgRecentMin      # span between max and min
            # avoid division by zero
            if rawAvgRecentMaxMin <= 0.:
                rawAvgRecentFrac[n] = 0.       # startup case?  Safer to be not a REF
            else:
                # For the current sample value, express the value as a fraction between its recent min and max.
                rawAvgRecentFrac[n] = (rawAvg[n] - rawAvgRecentMin) / rawAvgRecentMaxMin
        else:
            rawAvgRecentMax = rawAvgRecent.min()                    # min of those recent samples
            rawAvgRecentMaxA[n] = rawAvgRecentMax                   # remember those maximums

            # In the last recentLen/3 samples, what is the min value ?
            # Find the min of (history only long enough to span across one REF)
            # last recentLen/3 samples of rawAvg
            rawAvgRecent = rawAvg[max(0, int(n - (recentLen / 3))):n]
            rawAvgRecentMin = rawAvgRecent.max()                    # max of those recent samples
            rawAvgRecentMinA[n] = rawAvgRecentMin                   # remember those minimums

            # How different is the current sample value from its recent past ?
            # For the current sample value, express the value as a fraction between its recent min and max.
            rawAvgRecentMaxMin = rawAvgRecentMin - rawAvgRecentMax      # span between max and min
            # avoid division by zero
            if rawAvgRecentMaxMin <= 0.:
                rawAvgRecentFrac[n] = 0.       # startup case?  Safer to be not a REF
            else:
                # For the current sample value, express the value as a fraction between its recent min and max.
                rawAvgRecentFrac[n] = (rawAvgRecentMin - rawAvg[n]) / rawAvgRecentMaxMin

    # But the for loop skipped the first sample.  Fill in the skipped zero index from neighbor.
    rawAvgRecentFrac[0] = 0.                    # startup case.  Not a REF
    rawAvgRecentMinA[0] = rawAvgRecentMinA[1]
    rawAvgRecentMaxA[0] = rawAvgRecentMaxA[1]



    #def plotEzCon105ArawAvgMinMax():
    if 1:
        # Plot the REF detection progress so far.
        # Plot rawAvg in connected green, rawAvgRecentMinA in blue, and rawAvgRecentMaxA in violet.
        # The green rawAvg should rattle up and down between the recent blue min and the recent violet max.
        plotName = 'ezCon105ArawAvgMinMax.png'     #
        print()
        print('   plotting ' + plotName + ' ================================')

        print('                         rawAvgMaxMax =', rawAvg.max())
        print('                         rawAvgAvg =', np.mean(rawAvg))
        print('                         rawAvgMinMin =', rawAvg.min())

        #if ezConPlotRangeL[0] <= 105 and 105 <= ezConPlotRangeL[1]:
        if 105 in ezConPlotRequestedL:
            plt.clf()

            plt.plot(rawAvg, 'go-')
            #if refPositive:
            #    plt.plot(rawAvgCM10RecentMinA, 'bo')
            #    plt.plot(rawAvgCM10RecentMaxA, 'ro')
            #else:
            #    plt.plot(-rawAvgCM10RecentMinA, 'bo')
            #    plt.plot(-rawAvgCM10RecentMaxA, 'ro')
            plt.plot(rawAvgRecentMinA, 'bo')
            plt.plot(rawAvgRecentMaxA, 'o', c='violet')

            # Also plot each rawAvg sample as a fraction between the recent min and recent max.
            #rawAvgRecentMinAMin = rawAvgRecentMinA.min()
            #plt.plot(np.clip((rawAvgRecentFrac / 1000.) + rawAvgRecentMinAMin - 0.003,
            #    0, 0.99 * rawAvgRecentMinAMin), 'mo-')

            plt.title(titleS)
            plt.grid(ezConDispGrid)

            plt.xlabel(xLabelSRaw)
            plt.xlim(0, rawLenM1)
            plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

            plt.ylabel('Raw Antenna Spectrum Average with Recent Min and Max' \
                + '\n\n ezConRawSamplesUseL = ' + str(ezConRawSamplesUseL))
            #plt.ylim(-90, 90)

            if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')


    # Define the trigger level for a REF.  If above this, the sample is defined as a possible REF sample.
    #rawAvgRecentFracTrig = 0.5
    rawAvgRecentFracTrig = 0.6

    #def plotEzCon201CrawAvgRecentFrac():
    if 1:
        # Plot the REF detection progress so far.
        # Plot horizontal line at rawAvgRecentFracTrig in violet, and rawAvgAvgRecentFrac in connected green.
        # The green rawAvgAvgRecentFrac should rattle up and down above and below violet rawAvgRecentFracTrig.
        plotName = 'ezCon201CrawAvgRecentFrac.png'
        print()
        print('   plotting ' + plotName + ' ================================')

        print('                         rawAvgRecentFracMax =', rawAvgRecentFrac.max())
        print('                         rawAvgRecentFracAvg =', np.mean(rawAvgRecentFrac))
        print('                         rawAvgRecentFracMin =', rawAvgRecentFrac.min())

        #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
        if 201 in ezConPlotRequestedL:
            plt.clf()

            # horizontal line at rawAvgRecentFracTrig in violet
            plt.plot([0, rawLenM1], [rawAvgRecentFracTrig, rawAvgRecentFracTrig], '-', c='violet')

            # rawAvgAvgRecentFrac in connected green
            plt.plot(rawAvgRecentFrac, 'go-')

            plt.title(titleS)
            plt.grid(ezConDispGrid)

            plt.xlabel(xLabelSRaw)
            plt.xlim(0, rawLenM1)
            plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

            plt.ylabel('RawAvg Recent Fraction vs REF Trigger' \
                + '\n ')
            plt.ylim(-0.5, 2)     # clip silly start up values

            if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')



    # rawAvgRecentFrac is an array of fractions.  Which ones are above the trigger value ?
    # If sampleRef[i] == 1 means that i sample is a possible REF sample
    sampleRef = (rawAvgRecentFracTrig <= rawAvgRecentFrac) + 0    # sampleRef = 1 means possible REF sample
    #print(' sampleRef =')
    #print(sampleRef.tolist())
    sampleRefSum = sampleRef.sum()
    print(' sampleRefSum =', sampleRefSum)

    #def plotEzCon201DsampleRef():
    if 1:
        plotName = 'ezCon201DsampleRef.png'
        print()
        print('   plotting ' + plotName + ' ================================')

        #print('                         sampleRefMax =', sampleRef.max())
        sampleRefAvg = np.mean(sampleRef)
        print('                         sampleRefAvg =', sampleRefAvg)
        #print('                         sampleRefMin =', sampleRef.min())

        #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
        if 201 in ezConPlotRequestedL:
            plt.clf()

            # sampleRef in connected green
            plt.plot(sampleRef, 'go-')

            ## plot a blue dot on sampleRef which are 0
            #temp = sampleRef + 0.
            #temp[sampleRef] = np.nan                    # mark True  sampleRef as np.nan, which will not plot
            #plt.plot(temp, 'bo')

            # plot a violet dot on sampleRef which are 1
            temp = sampleRef + 0.
            temp[np.logical_not(sampleRef)] = np.nan    # mark False sampleRef as np.nan, which will not plot
            plt.plot(temp, 'o', c='violet')

            plt.title(titleS)
            plt.grid(ezConDispGrid)

            plt.xlabel(xLabelSRaw)
            plt.xlim(0, rawLenM1)
            plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

            plt.ylabel('Possible REF in Violet\n\nSampleRef = ' + str(sampleRefSum) \
                + ' = ' + str(int(100. * sampleRefAvg)) + ' %')
            #    + '\n\n rawLen = ' + str(rawLen))
            #plt.ylim(-90, 90)
            plt.ylim(-0.5, 2)     # same scale as previous plot
            
            if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')


    # Samples on both sides of a REF transition edge are assumed BAD (corrupted), so find them.

    #      123456
    #   ====CCCC====
    #   000100000000 = sampleBad0
    #   000010000000 = sampleBad1
    # Mark a non-REF BAD if it has a possible REF to its right.
    # non-REF samples on left side of a possible REF are assumed BAD (corrupted), so find them (sampleBad1).
    # REF samples to the right of sampleBad1 are assumed BAD (corrupted), so find them (sampleBad2).
    sampleRefLeft = np.concatenate([sampleRef[1:], [0]])       # shift sampleRef left
    sampleBad1 = np.logical_and(np.logical_not(sampleRef), sampleRefLeft) + 0
    #print(' sampleBad1 =')
    #print(sampleBad1.tolist())
    sampleBad2 = np.concatenate([[0], sampleBad1[:-1]])       # shift sampleBad1 right
    #print(' sampleBad2 =')
    #print(sampleBad2.tolist())

    #      123456
    #   ====CCCC====
    #   000000001000 = sampleBad6
    #   000000010000 = sampleBad5
    # Mark a non-REF BAD if it has a possible REF to its left.
    # non-REF samples on right side of a possible REF are assumed BAD (corrupted), so find them (sampleBad6).
    # REF samples to the left of sampleBad6 are assumed BAD (corrupted), so find them (sampleBad5).
    sampleRefRight = np.concatenate([[0], sampleRef[:-1]])       # shift sampleRef right
    sampleBad6 = np.logical_and(sampleRefRight, np.logical_not(sampleRef)) + 0
    #print(' sampleBad6 =')
    #print(sampleBad6.tolist())
    sampleBad5 = np.concatenate([sampleBad6[1:], [0]])       # shift sampleBad6 left
    #print(' sampleBad5 =')
    #print(sampleBad5.tolist())

    # combine sampleBad1, sampleBad2, sampleBad5, and sampleBad6 into sampleBad
    sampleBad = np.logical_or(sampleBad1, sampleBad2)
    sampleBad = np.logical_or(sampleBad,  sampleBad5)
    sampleBad = np.logical_or(sampleBad,  sampleBad6) + 0


    # But REF which were only 2 long were just both marked as BAD.
    # Of the 2 trailing REF neighbors (sample4 and sample5), mark the one more REFish as non-BAD.
    #      123456
    #   ====CCCC====
    #   000000010000 = sampleBad5 (created above)
    for i in np.nonzero(sampleBad5)[0]:
        if i:                                                       # ignore if sample5 index is 0
            if sampleRef[i-1]:                                      # insure sample4 is a REF
                if rawAvgRecentFrac[i-1] < rawAvgRecentFrac[i]:     # if sample4 is less REFish than sample5
                    sampleBad[i]   = 0                              # mark the more REFish sample5 as non-BAD
                else:
                    sampleBad[i-1] = 0                              # mark the more REFish sample4 as non-BAD


    # insist first recentLen sampleBad are True
    for i in range(recentLen):
        sampleBad[i] = 1
    #print(' sampleBad =')
    #print(sampleBad.tolist())


    #def plotEzCon201FsampleBad():
    if 1:
        plotName = 'ezCon201FsampleBad.png'
        print()
        print('   plotting ' + plotName + ' ================================')

        #print('                         sampleBadMax =', sampleBad.max())
        sampleBadSum = np.sum(sampleBad)
        sampleBadAvg = sampleBadSum / rawLen
        print('                         sampleBadAvg =', sampleBadAvg)
        #print('                         sampleBadMin =', sampleBad.min())

        #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
        if 201 in ezConPlotRequestedL:
            plt.clf()

            # sampleBad in connected green
            plt.plot(sampleBad, 'go-')

            plt.title(titleS)
            plt.grid(ezConDispGrid)

            plt.xlabel(xLabelSRaw)
            plt.xlim(0, rawLenM1)
            plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

            plt.ylabel('Samples Marked Invalid\n\nSampleBad = ' + str(sampleBadSum) \
                + ' = ' + str(int(100. * sampleBadAvg)) + ' %')
            #    + '\n\n rawLen = ' + str(rawLen))
            #plt.ylim(-90, 90)
            plt.ylim(-0.5, 2)     # same scale as previous plot
            
            if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')


    # maskRawRef = sampleRef and not(sampleBad)
    maskRawRef = np.logical_and(sampleRef, np.logical_not(sampleBad))
    #print(' maskRawRef =')
    #print(maskRawRef.tolist())

    # maskRawAnt = not maskRawRef and not(sampleBad)
    maskRawAnt = np.logical_and(np.logical_not(maskRawRef), np.logical_not(sampleBad))
    #print(' maskRawAnt =')
    #print(maskRawAnt.tolist())
    antLen = np.sum(maskRawAnt + 0)
    antLenM1 = antLen - 1

    #print(' maskRawAnt =', maskRawAnt)
    #print(' maskRawAnt + 0 =', maskRawAnt + 0)
    #print(' maskRawRef + 0 =', maskRawRef + 0)

    # raw plots for ezConRefMode == 20 (before data thinning soon)
    plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt
    plotEzCon201JtimeUtcMjdDBetweenRefRaw()     # using raw, dataTimeUtc, and maskRawRef

    #    # for a REF next to a REF, mark the lesser deviation REF as BAD.
    #    # Find REFs that follow a REF
    #    sampleRefAgain = np.concatenate([[0], sampleRef[:-1]])      # shift sampleRef right
    #    print(' sampleRefAgain =')
    #    print(sampleRefAgain.tolist())
    #    sampleRefAgain = np.logical_and(sampleRef, sampleRefAgain) + 0
    #    print(' sampleRefAgain =')
    #    print(sampleRefAgain.tolist())
    #    sampleRefAgainIndex = np.nonzero(sampleRefAgain)
    #    print(' sampleRefAgainIndex[0] =')
    #    print(sampleRefAgainIndex[0])

    #    for i in range(len(sampleRefAgainIndex[0])):
    #        # if the later REF has greater rawAvgAvgRecentFrac than the earlier REF
    #        if    rawAvg[sampleRefAgainIndex[0][i]] \
    #            > rawAvg[sampleRefAgainIndex[0][i] - 1]:
    #                       sampleRef[sampleRefAgainIndex[0][i] - 1] = 0      # mark earlier REF as non-REF
    #        else:
    #                       sampleRef[sampleRefAgainIndex[0][i]    ] = 0      # mark later   REF as non-REF

    #def plotEzCon105ErawAvgMaskRawAnt():
    if 0:
        plotName = 'ezCon105ErawAvgMaskRawAnt.png'
        print()
        print('   plotting ' + plotName + ' ================================')

        #print('                         maskRawAntMax =', maskRawAnt.max())
        maskRawAntSum = np.sum(maskRawAnt)
        maskRawAntAvg = maskRawAntSum / rawLen
        print('                         maskRawAntAvg =', maskRawAntAvg)
        #print('                         maskRawAntMin =', maskRawAnt.min())

        #if ezConPlotRangeL[0] <= 105 and 105 <= ezConPlotRangeL[1]:
        if 105 in ezConPlotRequestedL:
            plt.clf()

            # raw in connected green
            plt.plot(rawAvg, 'go-')

            # plot a blue dot on raw where maskAnt is True
            temp = rawAvg + 0.
            temp[np.logical_not(maskRawAnt)] = np.nan   # mark False maskRawAnt as np.nan, which will not plot
            plt.plot(temp, 'bo')

            # plot a violet dot on raw where maskRef is True
            temp = rawAvg + 0.
            temp[np.logical_not(maskRawRef)] = np.nan   # mark False maskRawRef as np.nan, which will not plot
            plt.plot(temp, 'o', c='violet')

            plt.title(titleS)
            plt.grid(ezConDispGrid)

            plt.xlabel(xLabelSRaw)
            plt.xlim(0, rawLenM1)
            plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

            plt.ylabel('maskRawAnt = ' + str(maskRawAntSum) \
                + ' = ' + str(int(100. * maskRawAntAvg)) + ' %' \
                + '\n\n rawLen = ' + str(rawLen))
            #plt.ylim(-90, 90)
            
            if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')


    # create ref: for every ant, the last REF raw spectrum
    ref = np.empty_like(raw)                    # to be thinned soon, to just the ANT samples
    refLast = raw[:, 0]                         # temporary refLast spectrum, backfilled soon
    refIndexFirst = -1                          # silly value, assumes at least one REF
    for n in range(rawLen):
        #print(' maskRawAnt[n] + 0 =', maskRawAnt[n] + 0)
        if maskRawAnt[n]:
            # n is an ANT sample
            ref[:, n] = refLast
        elif maskRawRef[n]:
            # n is an REF sample
            refLast = raw[:, n]
            #print(' np.shape(refLast) =', np.shape(refLast))
            # remember index and spectrum of first REF
            if refIndexFirst < 0:
                refIndexFirst = n
                #print('     refIndexFirst =', refIndexFirst)
                refFirst = refLast
                #print(' np.shape(refFirst) =', np.shape(refFirst))
    # backfill first REF spectrum into ref[0] to ref[refIndexFirst]
    print('     refIndexFirst =', refIndexFirst)
    for n in range(refIndexFirst):
        if maskRawAnt[n]:
            ref[:, n] = refFirst

    # done with raw data, thin most data arrays to only ANT samples
    azimuthDeg   = azimuthDeg  [maskRawAnt]
    elevationDeg = elevationDeg[maskRawAnt]
    dataFileIdx  = dataFileIdx [maskRawAnt]
    dataTimeUtc  = dataTimeUtc [maskRawAnt]
    rawIndex     = rawIndex    [maskRawAnt]
    ant          = raw     [:,  maskRawAnt]           # creation
    ref          = ref     [:,  maskRawAnt]           # creation
    #print(' np.shape(ant) =', np.shape(ant))

    #raw    = ant + 0. ######################################################## needed ?
    #raw = []                       # free memory
    #raw = None
    #del raw
    #rawLen = antLen + 0 ######################################################## needed ?



def createRef():

    global ezConRawSamplesUseL      # integer list
    global rawIndex                 # integer array       creation
    global rawLen                   # integer    

    # Create ref according to ezConRefMode
    #   ezConRefMode N < 0: REF = spectrum from -Nth ANT sample')
    #   ezConRefMode -1403: REF = spectrum from ANT sample number 1403')
    #
    #   ezConRefMode     0: REF = 1.0 (no REF, neutral spectrum)')
    #   ezConRefMode     1: REF = spectrum from first ANT sample, number 0')
    #   ezConRefMode     2: REF = spectrum from rawByFreqBinAvg')
    #
    #   ezConRefMode xxx 4: REF = ANT spectrum of closest (quiet) RA=refWantedRaDegA or refWantedRaDegB
    #                                   degrees, depending on declination ====== need RA
    #   ezConRefMode xxx 5: REF = ANT spectrum of (minimum average of ANT in last 0.5 days) (champion)
    #                                   ======= need RA
    #   ezConRefMode ??? 7: REF = ANT spectrum where antB is minimum for all antB in the time window
    #
    #   ezConRefMode    10: REF = last REF marked in data')
    #
    #   ezConRefMode ?? 20: REF detection by software (for refPulser hardware)

    print()
    print('   createRef ===============')

    print('   calculating Ref with ezConRefMode =', ezConRefMode)

    if ezConRawSamplesUseL:
        rawIndex = np.array(range(rawLen)) + ezConRawSamplesUseL[0]
    else:
        rawIndex = np.array(range(rawLen))

    if ezConRefMode < 0:
        createRefNeg(ezConRefMode)
    elif ezConRefMode == 0:
        createRef00antSampleZero()
    elif ezConRefMode == 1:
        createRef01refIsOne()
    elif ezConRefMode == 2:
        createRef02rawByFreqBinAvg()

    #elif ezConRefMode == 4:
    #    createRef04closestQuietRAAnt()      # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    #elif ezConRefMode == 5:
    #    createRef05minimumAvgAnt()          # xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    #elif ezConRefMode == 7:
    #    createRef07minimumAntBAvgAnt()      #?????????????????????????????????????

    elif ezConRefMode == 10:                #need REF marked in data, otherwise uses sample 0
        createRef10lastRefMarkedInData()

    #elif ezConRefMode == 20:                #need refPulser hardware
    #    createRef20refPulser()

    else:
        print()
        print()
        print()
        print(' ========== FATAL ERROR: ezConRefMode = ', ezConRefMode, ' not supported')
        print()
        print()
        print()
        print('\a')     # ring bell
        exit()



def ezConAntAvgPluckQtyLDo():

    global azimuthDeg               # float array
    global elevationDeg             # float array
    global dataFileIdx              # integer array
    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global ant                      # float 2d array
    global ref                      # float 2d array
    #global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    global antLen                   # integer
    global antLenM1                 # integer
    #global refLen                   # integer
    #global refLenM1                 # integer
    global xTickLocsAnt             # float array

    global ezConAntAvgPluckQtyL     # float list

    if not ezConAntAvgPluckQtyL:    # if empty, no plucking needed
        return(1)

    #print(f'   before ezConAntAvgPluckQtyL, antLen = ', {antLen:,}')

    print()
    print('   ezConAntAvgPluckQtyLDo ===============')

    print('   np.shape(ant)[0] =', np.shape(ant)[0])
    print('   np.shape(ant)[1] =', np.shape(ant)[1])

    antAvg = np.mean(ant, axis=0)
    #print('   antAvg =', antAvg)
    print(f'   len(antAvg) = {len(antAvg):,}')
    print()

    # get indexes of increasing antAvg
    antAvgIdxByIncreasing = antAvg.argsort()
    #print('   antAvgIdxByIncreasing =', antAvgIdxByIncreasing)
    print(f'   len(antAvgIdxByIncreasing) = {len(antAvgIdxByIncreasing):,}')
    print()

    print('   ezConAntAvgPluckQtyL =', ezConAntAvgPluckQtyL)
    print()

    # assume want to keep all antAvg samples
    antAvgPluckNumKeepMask = np.ones(antLen, dtype=bool)
    # mask off requested lowest-valued antAvg samples
    for i in range(ezConAntAvgPluckQtyL[0]):     # i starts with 0
        antAvgPluckNumKeepMask[antAvgIdxByIncreasing[i]] = False
    # mask off requested highest-valued antAvg samples
    for i in range(ezConAntAvgPluckQtyL[1]):     # i starts with 0
        antAvgPluckNumKeepMask[antAvgIdxByIncreasing[-1-i]] = False

    #print('   antAvgPluckNumKeepMask =', antAvgPluckNumKeepMask)
    print(f'   antAvgPluckNumKeepMask.sum() =', antAvgPluckNumKeepMask.sum())
    print(f'   len(antAvgPluckNumKeepMask) = {len(antAvgPluckNumKeepMask):,}')

    # thin most data arrays to keep only antAvgPluckNumKeepMask samples
    azimuthDeg   = azimuthDeg  [antAvgPluckNumKeepMask]
    elevationDeg = elevationDeg[antAvgPluckNumKeepMask]
    dataFileIdx  = dataFileIdx [antAvgPluckNumKeepMask]
    dataTimeUtc  = dataTimeUtc [antAvgPluckNumKeepMask]
    #rawIndex     = rawIndex    [antAvgPluckNumKeepMask]
    ant          = ant      [:, antAvgPluckNumKeepMask]
    ref          = ref      [:, antAvgPluckNumKeepMask]
    antLen    = ant.shape[1]
    antLenM1  = antLen - 1
    refLen    = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    print(f'   refLen = {refLen:,}')
    xTickLocsAnt = []               # probably just changed antLen, force new xTickLocsAnt



def ezConAntAvgPluckFracLDo():

    global azimuthDeg               # float array
    global elevationDeg             # float array
    global dataFileIdx              # integer array
    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global ant                      # float 2d array
    global ref                      # float 2d array
    #global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    global antLen                   # integer
    global antLenM1                 # integer
    #global refLen                   # integer
    #global refLenM1                 # integer
    global xTickLocsAnt             # float array

    global ezConAntAvgPluckFracL    # float list

    if not ezConAntAvgPluckFracL:   # if empty, no plucking needed
        return(1)

    #print(f'   before ezConAntAvgPluckFracLDo, antLen = ', {antLen:,}')

    print()
    print('   ezConAntAvgPluckFracLDo ===============')

    print('   np.shape(ant)[0] =', np.shape(ant)[0])
    print('   np.shape(ant)[1] =', np.shape(ant)[1])

    antAvg = np.mean(ant, axis=0)
    #print('   antAvg =', antAvg)
    print(f'   len(antAvg) = {len(antAvg):,}')
    print()

    # get indexes of increasing antAvg
    antAvgIdxByIncreasing = antAvg.argsort()
    #print('   antAvgIdxByIncreasing =', antAvgIdxByIncreasing)
    print(f'   len(antAvgIdxByIncreasing) = {len(antAvgIdxByIncreasing):,}')
    print()

    print('   ezConAntAvgPluckFracL =', ezConAntAvgPluckFracL)
    print()

    # snap down to next integer
    antAvgPluckFracQty0 = int(antLenM1 * ezConAntAvgPluckFracL[0])
    antAvgPluckFracQty1 = int(antLenM1 * ezConAntAvgPluckFracL[1])

    # assume want to keep all antAvg samples
    antAvgPluckFracKeepMask = np.ones(antLen, dtype=bool)

    # mask off requested lowest-valued antAvg samples
    for i in range(antAvgPluckFracQty0):     # i starts with 0
        antAvgPluckFracKeepMask[antAvgIdxByIncreasing[i]] = False
    # mask off requested highest-valued antAvg samples
    for i in range(antAvgPluckFracQty1):     # i starts with 0
        antAvgPluckFracKeepMask[antAvgIdxByIncreasing[-1-i]] = False

    #print('   antAvgPluckFracKeepMask =', antAvgPluckFracKeepMask)
    print(f'   antAvgPluckFracKeepMask.sum() =', antAvgPluckFracKeepMask.sum())
    print(f'   len(antAvgPluckFracKeepMask) = {len(antAvgPluckFracKeepMask):,}')

    # thin most data arrays to keep only antAvgPluckFracKeepMask samples
    azimuthDeg   = azimuthDeg  [antAvgPluckFracKeepMask]
    elevationDeg = elevationDeg[antAvgPluckFracKeepMask]
    dataFileIdx  = dataFileIdx [antAvgPluckFracKeepMask]
    dataTimeUtc  = dataTimeUtc [antAvgPluckFracKeepMask]
    #rawIndex     = rawIndex    [antAvgPluckFracKeepMask]
    ant          = ant      [:, antAvgPluckFracKeepMask]
    ref          = ref      [:, antAvgPluckFracKeepMask]
    antLen   = ant.shape[1]
    antLenM1 = antLen - 1
    refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    print(f'   refLen = {refLen:,}')
    xTickLocsAnt = []               # probably just changed antLen, force new xTickLocsAnt



def ezConAntFreqBinSmoothDo():
    # ant RFI spur removal with ezConAntFreqBinSmooth
    # for each Ant sample, no freqBin should be > ezConAntFreqBinSmooth * average of its 4 freqBin neighbor values

    global fileFreqBinQty           # integer
    global ant                      # float 2d array
    global antLen                   # integer
    global ezConAntFreqBinSmooth    # float

    print()
    print('   ezConAntFreqBinSmoothDo ===============')

    antZero = ant + 0.

    # if ezConAntFreqBinSmooth not a silly number
    if ezConAntFreqBinSmooth < 98.:
        print(' hide the RFI spectrum spurs ...')
        for n in range(antLen):
            # process the first 2 freqBin and the last 2 freqBin later, ignore them in this loop
            for f in range(2, fileFreqBinQty - 2):
                freqBinMax = ezConAntFreqBinSmooth \
                    * (antZero[f - 2, n] + antZero[f - 1, n] + antZero[f + 1, n] + antZero[f + 2, n]) / 4.
                if freqBinMax < antZero[f, n]:
                    ant[f, n] = min(antZero[f - 1, n], ant[f - 1, n])
                    print('        freqBinMax =', freqBinMax,
                        '           antZero[', f, ',', n, '] = ', antZero[f, n],
                        '           to ant[', f, ',', n, '] = ', ant[f, n])

        # process first freqBin
        for n in range(antLen):
            freqBinMax = ezConAntFreqBinSmooth * (antZero[1, n] + antZero[2, n]) / 2.
            if freqBinMax < antZero[0, n]:
                ant[0, n] = min(antZero[1, n], ant[1, n])
                print('        freqBinMax =', freqBinMax,
                    '           antZero[0,', n, '] = ', antZero[0, n],
                    '           to ant[0,', n, '] = ', ant[0, n])

        # process second freqBin
        for n in range(antLen):
            freqBinMax = ezConAntFreqBinSmooth \
                * (antZero[0, n] + antZero[2, n] + antZero[3, n] / 3.)
            if freqBinMax < antZero[1, n]:
                ant[1, n] = min(antZero[0, n], ant[0, n])
                print('        freqBinMax =', freqBinMax,
                    '           antZero[1,', n, '] = ', antZero[1, n],
                    '           to ant[1,', n, '] = ', ant[1, n])

        # process next to last freqBin
        for n in range(antLen):
            freqBinMax = ezConAntFreqBinSmooth \
                * (antZero[-4, n] + antZero[-3, n] + antZero[-1, n] / 3.)
            if freqBinMax < antZero[-2, n]:
                ant[-2, n] = min(antZero[-3, n], ant[-3, n])
                print('        freqBinMax =', freqBinMax,
                    '           antZero[-2,', n, '] = ', antZero[-2, n],
                    '           to ant[-2,', n, '] = ', ant[-2, n])

        # process last freqBin
        for n in range(antLen):
            freqBinMax = ezConAntFreqBinSmooth \
                * (antZero[-3, n] + antZero[-2, n] / 2.)
            if freqBinMax < antZero[-1, n]:
                ant[-1, n] = min(antZero[-2, n], ant[-2, n])
                print('        freqBinMax =', freqBinMax,
                    '           antZero[-1,', n, '] = ', antZero[-1, n],
                    '           to ant[-1,', n, '] = ', ant[-1, n])
        print()



def ezConAntSamplesUseLDo():

    global azimuthDeg               # float array
    global elevationDeg             # float array
    global dataFileIdx              # integer array
    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global ant                      # float 2d array
    global ref                      # float 2d array
    #global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    global antLen                   # integer
    global antLenM1                 # integer
    #global refLen                   # integer
    #global refLenM1                 # integer

    global xTickLabelsHeatAntL      # string list
    global xTickLocsAnt             # float array

    global ezConAntSamplesUseL      # integer list
    global ezConAntPluckL           # integer list

    #print(f'   before ezConAntSamplesUseLDo, antLen = ', {antLen:,}')
    
    print()
    print('   ezConAntSamplesUseLDo ===============')

    print('                         np.shape(ant)[1] =', np.shape(ant)[1])

    # ezConAntSamplesUseL allows more than one pair of list elements
    useSamplesAntStart = ezConAntSamplesUseL[0]
    useSamplesAntStop  = ezConAntSamplesUseL[1]
    useSamplesAntIndex = 2                         # point to next start/stop pair, if any
    # assume do  not  want to keep all Ant samples
    useSamplesAntMask = np.zeros([antLen], dtype = bool)
    for n in range(min(ezConAntSamplesUseL[-1] + 1, antLen)):
        # need to update useSamplesAntStop and useSamplesAntStart ?
        if useSamplesAntStop < n:
            useSamplesAntStart = ezConAntSamplesUseL[useSamplesAntIndex]
            useSamplesAntStop  = ezConAntSamplesUseL[useSamplesAntIndex + 1]
            useSamplesAntIndex += 2        # point to next Start/Stop pair, if any

        # is n inside a ANT want-to-use section ?
        if useSamplesAntStart <= n and n <= useSamplesAntStop:
            useSamplesAntMask[n] = True

    #print('                         useSamplesAntMask =', useSamplesAntMask)
    print('                         useSamplesAntMask.sum() =', (useSamplesAntMask + 0).sum())
    print('                         len(useSamplesAntMask) =', len(useSamplesAntMask))

    # thin most data arrays to only antAvgKeepMask samples
    azimuthDeg   = azimuthDeg  [useSamplesAntMask]
    elevationDeg = elevationDeg[useSamplesAntMask]
    dataFileIdx  = dataFileIdx [useSamplesAntMask]
    dataTimeUtc  = dataTimeUtc [useSamplesAntMask]
    #rawIndex     = rawIndex    [useSamplesAntMask]
    ant          = ant      [:, useSamplesAntMask]
    ref          = ref      [:, useSamplesAntMask]
    antLen   = ant.shape[1]
    antLenM1 = antLen - 1
    refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'                         antLen = {antLen:,}')
    print(f'                         refLen = {refLen:,}')
    xTickLabelsHeatAntL = []        # probably just changed antLen, force new xTickLabelsHeatAntL
    xTickLocsAnt        = []        # probably just changed antLen, force new xTickLocsAnt



def ezConAntPluckLDo():

    global azimuthDeg               # float array
    global elevationDeg             # float array
    global dataFileIdx              # integer array
    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global ant                      # float 2d array
    global ref                      # float 2d array
    #global rawIndex                 # integer array     may be thinned ??????????????????????????????????????
    global antLen                   # integer
    global antLenM1                 # integer
    #global refLen                   # integer
    #global refLenM1                 # integer

    global xTickLabelsHeatAntL      # string list
    global xTickLocsAnt             # float array

    global ezConAntSamplesUseL      # integer list
    global ezConAntPluckL           # integer list

    print()
    print('   ezConAntPluckLDo ===============')

    #print('   ant =', ant)
    print('                         np.shape(ant)[0] =', np.shape(ant)[0])
    print('                         np.shape(ant)[1] =', np.shape(ant)[1])
    print()

    # assume want to keep all Ant samples
    antPluckKeepMask = np.ones(antLen, dtype=bool)

    print('   ezConAntPluckL =', ezConAntPluckL)
    print()

    # This ezConAntPluckLDo() starts with the current indices of AntXT.
    # This loop processes the requests in given order.
    # Each pluck changes the index of the higher indexes (all higher samples move left).
    # Like a chain anchored at the left, and removing one link, the total chain is shortened and the right side of the chain moves left by one link.
    # This why it is easier to request ezConAntPluckL values in decreasing order !
    for i in range(len(ezConAntPluckL)):
        ezConAntPluckThis = ezConAntPluckL[i]
        if antLen <= ezConAntPluckThis:
            print()
            print()
            print()
            print(f' ========== FATAL ERROR: ezConAntPluckL[{i}] is too large a number.')
            print(f'                         ezConAntPluckL =', ezConAntPluckL)
            print(f'                         current length of Ant <= ezConAntPluckL[{i}]')
            print(f'                         {antLen} <= {ezConAntPluckThis}')
            print()
            print()
            print()
            print('\a')     # ring bell
            exit()
        else:
            antPluckKeepMask[ezConAntPluckThis] = False
    
    #print('                         antPluckKeepMask =', antPluckKeepMask)
    print('                         antPluckKeepMask.sum() =', (antPluckKeepMask + 0).sum())
    print('                         len(antPluckKeepMask) =', len(antPluckKeepMask))

    # thin most data arrays to only antPluckKeepMask samples
    azimuthDeg   = azimuthDeg  [antPluckKeepMask]
    elevationDeg = elevationDeg[antPluckKeepMask]
    dataFileIdx  = dataFileIdx [antPluckKeepMask]
    dataTimeUtc  = dataTimeUtc [antPluckKeepMask]
    #rawIndex     = rawIndex    [antPluckKeepMask]
    ant          = ant      [:, antPluckKeepMask]
    ref          = ref      [:, antPluckKeepMask]
    antLen   = ant.shape[1]
    antLenM1 = antLen - 1
    refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'                         antLen = {antLen:,}')
    print(f'                         refLen = {refLen:,}')
    xTickLabelsHeatAntL = []        # probably just changed antLen, force new xTickLabelsHeatAntL
    xTickLocsAnt        = []        # probably just changed antLen, force new xTickLocsAnt



def ezConAntXTVTMaxPluckDo():

    global ezConOut                 # float and int 2d array
    global antXTV                   # float 2d array
    global antXTVT                  # float 2d array
    global antLen                   # integer
    global antLenM1                 # integer
    global xTickLocsAnt             # float array

    global ezConAntXTVTMaxPluckQtyL         # integer list
    global ezConAntXTVTMaxPluckValL         # float list

    if not ezConAntXTVTMaxPluckQtyL and not ezConAntXTVTMaxPluckValL:    # if both empty, no plucking needed
        return(1)

    #print(f'   before ezConAntXTVTMaxPluckQtyL, antLen = ', {antLen:,}')

    print()
    print('   ezConAntXTVTMaxPluckDo ===============')

    print('   np.shape(antXTVT)[0] =', np.shape(antXTVT)[0])
    print('   np.shape(antXTVT)[1] =', np.shape(antXTVT)[1])

    antXTVTMax = np.amax(antXTVT, axis=0)
    #print('   antXTVTMax =', antXTVTMax)
    print(f'   len(antXTVTMax) = {len(antXTVTMax):,}')
    print()

    # assume want to keep all antXTVTMax samples
    antXTVTMaxPluckQtyKeepMask = np.ones(antLen, dtype=bool)

    if ezConAntXTVTMaxPluckQtyL:
        # get indexes of increasing antXTVTMax
        antXTVTMaxIdxByIncreasing = antXTVTMax.argsort()
        #print('   antXTVTMaxIdxByIncreasing =', antXTVTMaxIdxByIncreasing)
        print(f'   len(antXTVTMaxIdxByIncreasing) = {len(antXTVTMaxIdxByIncreasing):,}')
        print()

        print('   ezConAntXTVTMaxPluckQtyL =', ezConAntXTVTMaxPluckQtyL)
        print()

        # mask off requested lowest-valued antXTVTMax samples
        for i in range(ezConAntXTVTMaxPluckQtyL[0]):     # i starts with 0
            antXTVTMaxPluckQtyKeepMask[antXTVTMaxIdxByIncreasing[i]] = False
        # mask off requested highest-valued antXTVTMax samples
        for i in range(ezConAntXTVTMaxPluckQtyL[1]):     # i starts with 0
            antXTVTMaxPluckQtyKeepMask[antXTVTMaxIdxByIncreasing[-1-i]] = False

    if ezConAntXTVTMaxPluckValL:
        print('   ezConAntXTVTMaxPluckValL =', ezConAntXTVTMaxPluckValL)
        print()

        # mask off antXTVTMax samples with values equal or less than requested low
        antXTVTMaxPluckQtyKeepMask[antXTVTMax <= ezConAntXTVTMaxPluckValL[0]] = False
        # mask off antXTVTMax samples with values equal or greater than requested high
        antXTVTMaxPluckQtyKeepMask[ezConAntXTVTMaxPluckValL[1] <= antXTVTMax] = False

    #print('   antXTVTMaxPluckQtyKeepMask =', antXTVTMaxPluckQtyKeepMask)
    print(f'   antXTVTMaxPluckQtyKeepMask.sum() =', antXTVTMaxPluckQtyKeepMask.sum())
    print(f'   len(antXTVTMaxPluckQtyKeepMask) = {len(antXTVTMaxPluckQtyKeepMask):,}')

    # thin most data arrays to keep only antXTVTMaxPluckQtyKeepMask samples
    #azimuthDeg   = azimuthDeg  [antXTVTMaxPluckQtyKeepMask]
    #elevationDeg = elevationDeg[antXTVTMaxPluckQtyKeepMask]
    #dataTimeUtc  = dataTimeUtc [antXTVTMaxPluckQtyKeepMask]
    #rawIndex     = rawIndex    [antXTVTMaxPluckQtyKeepMask]
    # thin ezConOut[n, :]
    ezConOut     = ezConOut    [antXTVTMaxPluckQtyKeepMask, :]
    antXTV       = antXTV   [:, antXTVTMaxPluckQtyKeepMask]    # keep antXTV for Galaxy crossing plots
    antXTVT      = antXTVT  [:, antXTVTMaxPluckQtyKeepMask]
    antLen   = antXTVT.shape[1]
    antLenM1 = antLen - 1
    #refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    #print(f'   refLen = {refLen:,}')
    xTickLocsAnt = []               # probably just changed antLen, force new xTickLocsAnt



def ezConAntXTVTAvgPluckDo():

    global ezConOut                 # float and int 2d array
    global antXTV                   # float 2d array
    global antXTVT                  # float 2d array
    global antLen                   # integer
    global antLenM1                 # integer
    global xTickLocsAnt             # float array

    global ezConAntXTVTAvgPluckQtyL         # integer list
    global ezConAntXTVTAvgPluckValL         # float list

    if not ezConAntXTVTAvgPluckQtyL and not ezConAntXTVTAvgPluckValL:    # if both empty, no plucking needed
        return(1)

    #print(f'   before ezConAntXTVTAvgPluckQtyL, antLen = ', {antLen:,}')

    print()
    print('   ezConAntXTVTAvgPluckDo ===============')

    print('   np.shape(antXTVT)[0] =', np.shape(antXTVT)[0])
    print('   np.shape(antXTVT)[1] =', np.shape(antXTVT)[1])

    antXTVTAvg = np.mean(antXTVT, axis=0)
    #print('   antXTVTAvg =', antXTVTAvg)
    print(f'   len(antXTVTAvg) = {len(antXTVTAvg):,}')
    print()

    # assume want to keep all antXTVTAvg samples
    antXTVTAvgPluckQtyKeepMask = np.ones(antLen, dtype=bool)

    if ezConAntXTVTAvgPluckQtyL:
        # get indexes of increasing antXTVTAvg
        antXTVTAvgIdxByIncreasing = antXTVTAvg.argsort()
        #print('   antXTVTAvgIdxByIncreasing =', antXTVTAvgIdxByIncreasing)
        print(f'   len(antXTVTAvgIdxByIncreasing) = {len(antXTVTAvgIdxByIncreasing):,}')
        print()

        print('   ezConAntXTVTAvgPluckQtyL =', ezConAntXTVTAvgPluckQtyL)
        print()

        # mask off requested lowest-valued antXTVTAvg samples
        for i in range(ezConAntXTVTAvgPluckQtyL[0]):     # i starts with 0
            antXTVTAvgPluckQtyKeepMask[antXTVTAvgIdxByIncreasing[i]] = False
        # mask off requested highest-valued antXTVTAvg samples
        for i in range(ezConAntXTVTAvgPluckQtyL[1]):     # i starts with 0
            antXTVTAvgPluckQtyKeepMask[antXTVTAvgIdxByIncreasing[-1-i]] = False

    if ezConAntXTVTAvgPluckValL:
        print('   ezConAntXTVTAvgPluckValL =', ezConAntXTVTAvgPluckValL)
        print()

        # mask off antXTVTAvg samples with values equal or less than requested low
        antXTVTAvgPluckQtyKeepMask[antXTVTAvg <= ezConAntXTVTAvgPluckValL[0]] = False
        # mask off antXTVTAvg samples with values equal or greater than requested high
        antXTVTAvgPluckQtyKeepMask[ezConAntXTVTAvgPluckValL[1] <= antXTVTAvg] = False

    #print('   antXTVTAvgPluckQtyKeepMask =', antXTVTAvgPluckQtyKeepMask)
    print(f'   antXTVTAvgPluckQtyKeepMask.sum() =', antXTVTAvgPluckQtyKeepMask.sum())
    print(f'   len(antXTVTAvgPluckQtyKeepMask) = {len(antXTVTAvgPluckQtyKeepMask):,}')

    # thin most data arrays to keep only antXTVTAvgPluckQtyKeepMask samples
    #azimuthDeg   = azimuthDeg  [antXTVTAvgPluckQtyKeepMask]
    #elevationDeg = elevationDeg[antXTVTAvgPluckQtyKeepMask]
    #dataTimeUtc  = dataTimeUtc [antXTVTAvgPluckQtyKeepMask]
    #rawIndex     = rawIndex    [antXTVTAvgPluckQtyKeepMask]
    # thin ezConOut[n, :]
    ezConOut     = ezConOut    [antXTVTAvgPluckQtyKeepMask, :]
    antXTV       = antXTV   [:, antXTVTAvgPluckQtyKeepMask]    # keep antXTV for Galaxy crossing plots
    antXTVT      = antXTVT  [:, antXTVTAvgPluckQtyKeepMask]
    antLen   = antXTVT.shape[1]
    antLenM1 = antLen - 1
    #refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    #print(f'   refLen = {refLen:,}')
    xTickLocsAnt = []               # probably just changed antLen, force new xTickLocsAnt



def ezConAntXTVTPluckDo():

    global ezConOut                 # float and int 2d array
    global antXTV                   # float 2d array
    global antXTVT                  # float 2d array
    global antLen                   # integer
    global antLenM1                 # integer
    global xTickLocsAnt             # float array

    global ezConAntXTVTPluckL       # integer list

    #print(f'   before ezConAntXTVTPluckDo, antLen = ', {antLen:,}')

    print()
    print('   ezConAntXTVTPluckDo ===============')

    #print('   antXTVT =', antXTVT)
    print('                         np.shape(antXTVT)[0] =', np.shape(antXTVT)[0])
    print('                         np.shape(antXTVT)[1] =', np.shape(antXTVT)[1])
    print()

    # assume want to keep all AntXTVT samples
    antXTVTPluckKeepMask = np.ones(antLen, dtype=bool)

    print('   ezConAntXTVTPluckL =', ezConAntXTVTPluckL)
    print()

    # This ezConAntXTVTPluckLDo() starts with the current indices of AntXT.
    # This loop processes the requests in given order.
    # Each pluck changes the index of the higher indexes (all higher samples move left).
    # Like a chain anchored at the left, and removing one link, the total chain is shortened and the right side of the chain moves left by one link.
    # This why it is easier to request ezConAntXTVTPluckL values in decreasing order !
    for i in range(len(ezConAntXTVTPluckL)):
        ezConAntXTVTPluckThis = ezConAntXTVTPluckL[i]
        if antLen <= ezConAntXTVTPluckThis:
            print()
            print()
            print()
            print(f' ========== FATAL ERROR: ezConAntXTVTPluckL[{i}] is too large a number.')
            print(f'                         ezConAntXTVTPluckL =', ezConAntXTVTPluckL)
            print(f'                         current length of Ant <= ezConAntXTVTPluckL[{i}]')
            print(f'                         {antLen} <= {ezConAntXTVTPluckThis}')
            print()
            print()
            print()
            print('\a')     # ring bell
            exit()
        else:
            antXTVTPluckKeepMask[ezConAntXTVTPluckThis] = False

    #print('                         antXTVTPluckKeepMask =', antXTVTPluckKeepMask)
    print(f'                         len(antXTVTPluckKeepMask) = {len(antXTVTPluckKeepMask):,}')
    print(f'                         antXTVTPluckKeepMask.sum() =', antXTVTPluckKeepMask.sum())

    # thin most data arrays to keep only antXTVTPluckKeepMask samples
    #azimuthDeg   = azimuthDeg  [antXTVTPluckKeepMask]
    #elevationDeg = elevationDeg[antXTVTPluckKeepMask]
    #dataTimeUtc  = dataTimeUtc [antXTVTPluckKeepMask]
    #rawIndex     = rawIndex    [antXTVTPluckKeepMask]
    # thin ezConOut[n, :]
    ezConOut     = ezConOut    [antXTVTPluckKeepMask, :]
    antXTV       = antXTV      [:, antXTVTPluckKeepMask]    # keep antXTV for Galaxy crossing plots
    antXTVT      = antXTVT     [:, antXTVTPluckKeepMask]
    antLen   = antXTVT.shape[1]
    antLenM1 = antLen - 1
    #refLen   = ref.shape[1]
    #refLenM1 = refLen - 1
    print(f'   antLen = {antLen:,}')
    #print(f'   refLen = {refLen:,}')
    xTickLocsAnt = []               # probably just changed antLen, force new xTickLocsAnt



def ezConAntXTVTSmoothDo():
    # smooth antXTVT heatmap image

    global antXTVT                  # float 2d array

    print()
    print('   ezConAntXTVTSmoothDo ===============')

    #print('   antXTVT =', antXTVT)
    print('                         np.shape(antXTVT)[0] =', np.shape(antXTVT)[0])
    print('                         np.shape(antXTVT)[1] =', np.shape(antXTVT)[1])
    print()

    # Ubuntu22 cv2 install:
    #   sudo apt-get install python3-opencv
    # Windows10 cv2 install (may work but not tried):
    #   https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html
    #       https://github.com/opencv/opencv/releases
    #           opencv-4.11.0-windows.exe
    # Windows10 cv2 install (provided too much):
    #   https://docs.opencv.org/4.x/d3/d52/tutorial_windows_install.html
    #       https://sourceforge.net/projects/opencvlibrary/files/
    #       https://sourceforge.net/projects/opencvlibrary/files/4.11.0/
    #       https://sourceforge.net/projects/opencvlibrary/files/latest/download
    #           ran that opencv-4.11.0-windows.exe
    # Windows10 cv2 install (worked on Win10):
    #   https://github.com/opencv/opencv-python?tab=readme-ov-file#supported-python-versions
    #       py -m pip install opencv-python
    #
    # https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

    #img = cv2.imread('opencv_logo.png')

    if ezConAntXTVTSmooth == 1:
        import cv2
        #from cv2 import blur
        antXTVT = cv2.blur(antXTVT,(5,5))

    elif ezConAntXTVTSmooth == 2:
        import cv2
        antXTVT = cv2.GaussianBlur(antXTVT,(5,5),0)

    elif ezConAntXTVTSmooth == 11:
        import cv2
        antXTVT = cv2.blur(antXTVT,(5,5))
        antXTVT = cv2.blur(antXTVT,(5,5))

    elif ezConAntXTVTSmooth == 22:
        import cv2
        antXTVT = cv2.GaussianBlur(antXTVT,(5,5),0)
        antXTVT = cv2.GaussianBlur(antXTVT,(5,5),0)

    elif ezConAntXTVTSmooth == 111:
        import cv2
        antXTVT = cv2.blur(antXTVT,(5,5))
        antXTVT = cv2.blur(antXTVT,(5,5))
        antXTVT = cv2.blur(antXTVT,(5,5))

    elif ezConAntXTVTSmooth == 222:
        import cv2
        antXTVT = cv2.GaussianBlur(antXTVT,(5,5),0)
        antXTVT = cv2.GaussianBlur(antXTVT,(5,5),0)
        antXTVT = cv2.GaussianBlur(antXTVT,(5,5),0)

    #antXTVT = cv2.medianBlur(antXTVT,5)             # Median Filtering 1 === "Unsupported format"

    #antXTVT = cv2.bilateralFilter(antXTVT,9,75,75)  # Bilateral Filtering 1 === "only 8u and 32f images"



def createEzConOutEzb():
    # creates antXTV, and ezConOut[n, 20]
    # deletes antAvg, antMax,   refAvg, refMax,   antBAvg, antBMax,   antRBAvg, antRBMax

    # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  AzimuthDeg  ElevationDeg  AntXTVTCmDop
    #          0           1    2       3        4        5     6      7           8             9
    #   AntAvg  AntMax    RefAvg  RefMax
    #   10      11        12      13
    #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
    #   14       15          16        17         18          19

    global ezRAObsLat               # float
    global ezRAObsLon               # float
    global ezRAObsAmsl              # float

    global dataTimeUtc              # 'astropy.time.core.Time' object array
    global azimuthDeg               # float array
    global elevationDeg             # float array
    global fileFreqBinQty           # integer
    global freqCenter               # float
    global dopplerSpanD2            # float

    global ezConAstroMath           # integer

    global antAvg                   # float array
    global antMax                   # float array
    global refAvg                   # float array
    global refMax                   # float array
    global antBAvg                  # float array
    global antBMax                  # float array
    global antRBAvg                 # float array
    global antRBMax                 # float array
    global antXT                    # float 2d array
    global antXTV                   # float 2d array    creation

    global antLen                   # integer

    global ezConOut                 # float and int 2d array        creation

    global fileNameLast             # string

    print()
    print('   createEzConOutEzb ===============')
    print('                         ezConAstroMath =', ezConAstroMath)

    # for each sample in ant, create and collect .ezb coordinate numbers

    # calculate constants

    if ezConAstroMath == 1:
        # use Python port from MIT Haystack Small Radio Telescope (SRT) from vlsr() in geom.c
        # https://www.haystack.mit.edu/haystack-public-outreach/srt-the-small-radio-telescope-for-education/
        # VLSR = receding Velocity of the Local Standard of Rest
        #   to remove Doppler effects of earth and Sun Galactic movements
        # "/* sun 20km/s towards ra=18h dec=30.0 */"
        # https://en.wikipedia.org/wiki/Solar_apex

        #decc = -(28. + 56. / 60.) * math.pi / 180.
        #print(' decc =', decc)
        #rac = (17. + 45.5 / 60.) * math.pi / 12.
        #print(' rac =', rac)
        #dp = 27.1 * math.pi / 180.
        #print(' dp =', dp)
        #rp = (12. + 51.4 / 60.) * math.pi / 12.
        #print(' rp =', rp)
        #x0 = 20. * math.cos(18. * math.pi / 12.) * math.cos(30. * math.pi / 180.)
        #print(' x0 =', x0)
        #y0 = 20.0 * math.sin(18.0 * math.pi / 12.0) * math.cos(30.0 * math.pi / 180.0)
        #print(' y0 =', y0)
        #z0 = 20.0 * math.sin(30.0 * math.pi / 180.0)        # sun 20km/s towards ra=18h dec=30.
        #print(' z0 =', z0)

        #decc = -0.5049819302436926
        #cosDecc = math.cos(decc)
        #print(' cosDecc =', cosDecc)
        #sinDecc = math.sin(decc)
        #print(' sinDecc =', sinDecc)
        cosDecc = 0.875183216565868
        sinDecc = -0.48379162605549625

        rac = 4.649120794999895

        #dp = 0.4729842272904633
        #sinDp = math.sin(dp)
        #print(' sinDp =', sinDp)
        #cosDp = math.cos(dp)
        #print(' cosDp =', cosDp)
        sinDp = 0.45554490723351554
        cosDp = 0.8902128046111265

        rp = 3.3658674624710643

        #cosRpMRac = math.cos(rp - rac)
        #print(' cosRpMRac =', cosRpMRac)
        #sinRpMRac = math.sin(rp - rac)
        #print(' sinRpMRac =', sinRpMRac)
        cosRpMRac = 0.28359695364827764
        sinRpMRac = -0.958943568663671

        # readclock() from SRT's time.c
        # says
        # t = gmtime(&now);
        # // gmtime Jan 1 is day 0
        # secs = tosecs(t->tm_year + 1900, t->tm_yday + 1, t->tm_hour, t->tm_min, t->tm_sec);

        # FITS format: “[±Y]YYYY-MM-DD[THH:MM:SS[.sss]]”.
        # dataTimeUtcVlsr1900 = Time('1900-01-01T00:00:00', format='fits', scale='utc')
        #   gives a warning: 
        #       WARNING: ErfaWarning: ERFA function "dtf2d" yielded 1 of "dubious year (Note 6)"
        #        [astropy._erfa.core]
        # OK, use year 2000 and add a year of seconds:
        # print(' (dataTimeUtcVlsr2000.mjd - dataTimeUtcVlsr1900.mjd) * 24. * 60. * 60. =',
        #    (dataTimeUtcVlsr2000.mjd - dataTimeUtcVlsr1900.mjd) * 24. * 60. * 60.)
        # gives (dataTimeUtcVlsr2000.mjd - dataTimeUtcVlsr1900.mjd) * 24. * 60. * 60. = 3155673600.0
        # check: 365.25 * 100 * 24. * 60. * 60. = 3155760000 seconds = yup, close
        # diff = 3155760000 - 3155673600.0 = 86400 = 24. * 60. * 60. = 1 day, so use 3155673600. below
        #
        #from astropy.time import Time
        dataTimeUtcVlsr2000 = Time('2000-01-01T00:00:00', format='fits', scale='utc')
        #print(' dataTimeUtcVlsr2000.mjd =', dataTimeUtcVlsr2000.mjd)

    elif ezConAstroMath == 2:
        # use astropy
        from astropy import units as u
        from astropy.coordinates import EarthLocation
        from astropy.coordinates import SkyCoord

        locBase = EarthLocation(lat = ezRAObsLat*u.deg, lon = ezRAObsLon*u.deg, height = ezRAObsAmsl*u.m)
        # for testing:  https://www.gb.nrao.edu/~fghigo/gbt/setups/radvelcalc.html
        #   which assumes location is the Green Bank Telescope at 38.432964328895835, -79.83969457195226,
        #locBase = EarthLocation(lat = 38.432964328895835*u.deg, lon = -79.83969457195226*u.deg, height = 807.43*u.m)

        # By studying the telescope's received frequency information, the telescope can measure the radial (line-of-sight) velocity of Galactic hydrogen,
        #
        #     Telescope <========== moving-relative-to ==========>  Galactic hydrogen
        #
        # The MIT Haystack Small Radio Telescope (SRT) system suggests that ezRA divide that moving-relative-to velocity measurement into 2 parts,
        # both relative to a "Local Standard of Reference (LSR)" in the middle,
        #
        #     Telescope <==== moving-relative-to ====> LSR <==== moving-relative-to ====> Galactic hydrogen
        # 
        # That MIT Haystack system says that "Local Standard of Reference (LSR)"
        # "is the average [motion] for a group of stars that are in the vicinity of our solar system",
        #     http://web.mit.edu/8.13/www/srt_software/vlsr.pdf
        #
        # ezRA should study that velocity part on the right, the radial velocity of the Galactic hydrogen relative to the LSR.
        #
        # ezRA should calculate and subtract that velocity part on the left, the radial velocity of the telescope relative to the LSR.
        # That ezRA telescope is on the moving Earth, with the Earth moving around the Sun, with the Sun moving relative to the Local Standard of Rest.
        # Considering those motions in the opposite order, ezRA could calculate
        #     1. the Sun motion relative to the LSR
        #     2. the Earth motion revolving around the Sun once a year
        #     3. the motion of the telescope location on the Earth which rotates once a day

        # What is the fastest the telescope can move toward a star ?
        # If everything aligns, the notes below say 20.0 + 29.86  + 0.463 = 50.323 km/s
        #
        # 1. The Sun is moving toward a particular star: vStarSunMax = 20 km/s:
        # Direction of motion of the Sun from
        # http://herschel.esac.esa.int/hcss-doc-15.0/load/hifi_um/html/hifi_ref_frame.html#hum_lsr_frame
        # https://en.wikipedia.org/wiki/Solar_apex
        pointingSun = SkyCoord(ra = "18:03:50.29", dec = "+30:00:16.8",frame = "icrs",unit = (u.hourangle,u.deg))
        vStarSunMax = -20.0*u.km/u.s        # toward a direction is negative velocity
        #
        # 2. The Earth is revolving around the Sun once a year: vStarEarthAroundSunMax = 29.86 km/s:
        # Earth is 150e6 km from Sun.
        # Circumference = 2 * pi * r = 2 * pi * 150e6 = 942,477,796 km.
        # Speed to travel that distance in 365.25 days
        # = 942,477,796 / 365.25 / 24 / 60 / 60 = 29.86 km/s
        #
        # 3. The Earth is rotating on its north-south axis: vStarEarthOnAxisMax = 0.463 km/s:
        # At equator, Earth radius is 6371 km.
        # Circumference = 2 * pi * r = 2 * pi * 6371 = 40,030 km.
        # Speed to travel that distance in 24 hours
        # = 40,030 / 24 / 60 / 60 = 0.463 km/s ====== which is relatively so small that ezCol will ignore.

        # https://www.cosmos.esa.int/documents/12133/1028864/HCSS+User%27s+Reference+Manual+Herschel+Data+Processing
        # "The sign of the radial velocity is negative towards the target and positive otherwise (Doppler effect sign convention)"

        # https://gitlab.camras.nl/dijkema/HPIB/blob/185d241ad9bd7507ed90c9fa91fe0a63009d3eee/vlsr.py

        # https://public.nrao.edu/ask/velocity-reference-used-in-radio-astronomy/
        # https://www.atnf.csiro.au/people/Tobias.Westmeier/tools_hihelpers.php#restframes
        # says 'alternative “kinematical definition” (referred to as LSRK) which results in a slightly
        #     higher velocity of about 20 km/s in the direction of (α,δ)=(270∘,30∘) in the B1900 system'.
        # https://science.nrao.edu/facilities/gbt/observing/GBTog.pdf
        # says "‘lsrk’ (Local Standard of Rest kinematical definition, i.e. typical LSR definition)".
        # https://encyclopedia2.thefreedictionary.com/local+standard+of+rest

    ## calculate and fill missing ezConOut[n, 20] signal columns

    samplesQtyProcessed = 0

    for n in range(antLen):

        dataTimeUtcStrThis = dataTimeUtc[n].iso
        # '2023-02-09 00:01:20.000'
        
        if ezConAstroMath == 1:
            # use Python port from MIT Haystack Small Radio Telescope (SRT) geom.c and time.c,
            # derivation comments last in ezCon220825b.py

            # pre-calculations
            pie    = math.pi
            piD180 = pie / 180
            piPPi  = pie + pie
            oneEightZeroDPi = 180 / pie
            secsPerYear = 31536000.0 # 365 * 24 * 60 * 60 = seconds per year

            #print()
            #print()
            #print(' dataTimeUtcStrThis =', dataTimeUtcStrThis)

            azimuthRadThis   = azimuthDeg[n]   * piD180         # to radians
            elevationRadThis = elevationDeg[n] * piD180         # to radians
            cosElRad = math.cos(elevationRadThis)
            north = math.cos(azimuthRadThis) * cosElRad
            west = -math.sin(azimuthRadThis) * cosElRad
            zen = math.sin(elevationRadThis)

            d1lat = ezRAObsLat * piD180                         # to radians
            d1lon = ezRAObsLon * piD180                         # to radians
            #print(' ezRAObsLon =', ezRAObsLon, 'degrees')
            #print(' d1lon =', d1lon, 'radians')

            cosD1lat = math.cos(d1lat)
            sinD1lat = math.sin(d1lat)
            pole = north * cosD1lat + zen * sinD1lat
            rad = zen * cosD1lat - north * sinD1lat
            #print(' rad =', rad, 'radians')                        # right ascension (radians)

            dec = math.atan2(pole, math.sqrt(rad * rad + west * west))
            #print(' dec =', dec, 'radians')                        # declination (radians)
            
            ha = math.atan2(west, rad)
            #print(' ha =', ha, 'radians')                          # hour angle (radians)
            #print(' ha * 24./piPPi =', ha*24./piPPi, 'hours')
            #https://clearskytonight.com/projects/astronomycalculator/coordinate/rightascension_hourangle.html
            
            # try gst() with Haystack code
            if 0:
                # srt's readclock() (which calls tosecs()) to define secs as "Seconds since New Year 1970", 
                #   = seconds since start of 1970
                #
                # https://linux.die.net/man/3/modf
                #   The modf() function returns the fractional part of x
                #
                # gst() from SRT's time.c
                # double gst(double ttime)
                # {
                #     double secs, pdum;
                #     int i;
                # //    secs = (1999 - 1970) * 31536000.0 + 17.0 * 3600.0 + 16.0 * 60.0 + 20.1948;
                # //    secs = (2011 - 1970) * 31536000.0 + 17.0 * 3600.0 + 15.0 * 60.0 + 58.0778;
                #     secs = (2020 - 1970) * 31536000.0 + 17.0 * 3600.0 + 16.0 * 60.0 + 40.5;
                #     for (i = 1970; i < 2020; i++) {
                #         if ((i % 4 == 0 && i % 100 != 0) || i % 400 == 0)
                #             secs += 86400.0;
                #     }
                #
                #     return (modf((ttime - secs) / 86164.09053, &pdum) * TWOPI);
                # /* 17 16 20.1948 UT at 0hr newyear1999 */
                # /* 17 15 58.0778 UT at 0hr newyear2011 */
                # /* 17 16 40.5    UT at 0hr newyear2020 */
                # } 
                #
                # tosecs() from SRT's time.c
                # /* Convert to Seconds since New Year 1970 */
                # double tosecs(int yr, int day, int hr, int min, int sec)
                # {
                #     int i;
                #     double secs;
                #     secs = (yr - 1970) * 31536000.0 + (day - 1) * 86400.0 + hr * 3600.0 + min * 60.0 + sec;
                #     for (i = 1970; i < yr; i++) {
                #         if ((i % 4 == 0 && i % 100 != 0) || i % 400 == 0)
                #             secs += 86400.0;
                #     }
                #     if (secs < 0.0)
                #         secs = 0.0;
                #     return secs;
                # }
                #
                # readclock() from SRT's time.c
                # double readclock(void)
                # {
                #     time_t now;
                #     double secs;
                #     struct tm *t;
                #     now = time(NULL);
                #     t = gmtime(&now);
                # // gmtime Jan 1 is day 0
                #     secs = tosecs(t->tm_year + 1900, t->tm_yday + 1, t->tm_hour, t->tm_min, t->tm_sec);
                #     if (d1.azelsim) {
                #         if (d1.start_time == 0.0)
                #             d1.start_time = secs;
                #         if (d1.start_sec)
                #             secs = d1.start_sec + (secs - d1.start_time) * d1.speed_up;
                #         else {
                #             if (d1.speed_up > 0)
                #                 secs = d1.start_time + (secs - d1.start_time) * d1.speed_up;
                #             else
                #                 secs += -d1.speed_up * 3600.0; // advance by hours
                #         }
                #     }
                #     sprintf(d1.timsource, "PC ");
                #     return (secs);
                # }

                # python version of the gst() above
                #   valid only during 2020 through 2024
                # assuming data not earlier than 2020, start with
                #   latest seed of "17 16 40.5 UT at 0hr newyear2020"
                secsGst2020 = 1577899000.5
                # calculate that number
                if 0:
                    secsGst2020 = (2020 - 1970) * 31536000.0 + 17.0 * 3600.0 + 16.0 * 60.0 + 40.5
                    print()
                    print(' secsGst2020 =', secsGst2020, 'seconds')      # says secsGst2020 = 1576862200.5
                    # add leap year days 1970 through 1999
                    for i in range(1970, 2020):
                        #if ((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):
                        if ((not i % 4 and i % 100) or not i % 400):
                            print(' i =', i)
                            secsGst2020 += 86400.0             # seconds in a non-leap year
                    print(' secsGst2020 =', secsGst2020, 'radians')
                    print()
                    exit()

                # Calculate seconds since 1577899000.5 (start of 1970).
                ttimeSecGst = dataTimeUtc[n].mjd * 86400. - 1577899000.5  # in seconds
                #print(' ttimeSecGst =', ttimeSecGst, 'seconds')

                # Calculate GST fractional sidereal day
                # Sidereal day on Earth is approximately 86164.0905 seconds ?????????????????????????????? why sidereal ?
                ##gstSidVlsr = (ttimeSecVlsr - secsVlsr2020) / 86164.09053 % 1.
                ###print(' gstSidVlsr =', gstSidVlsr, 'seconds')
                ##gstSidVlsrRad = gstSidVlsr * piPPi      # in radians
                ##print(' gstSidVlsrRad =', gstSidVlsrRad, 'radians')
                ##print(' gstSidVlsrRad * 24./piPPi =', gstSidVlsrRad*24./piPPi, 'hours')
                gstDay = (ttimeSecVlsr - secsVlsr2020) / 86164.09053 % 1.
                #print(' gstDay =', gstDay, 'days')
                gstDayRad = gstDay * piPPi      # in radians
                print(' gstDayRad =', gstDayRad, 'radians')
                print(' gstDayRad * 24./piPPi =', gstDayRad*24./piPPi, 'hours')

            # try gst() with https://www.astro.umd.edu/~jph/GST_eqn.pdf
            
            #dataTimeUtcStrThis = '1999-12-31 00:00:00.000'  # gstHoursThis = 6.598809806000002 hours
            #                                                       vs table=6.5988098 yup
            #                                                                 gstHoursThis = 6 35 55.715301600007194
            #                                                     vs table= 2000 * 6.5988098 6 35 55.72 yup

            #dataTimeUtcStrThis = '2000-01-01 00:00:00.000'  # gstHoursThis = 6.6645196304000045 hours
            #                           vs math = 6.5988098 + 0.0657098244 = 6.6645196244 yup ???????????
            #                                                                 gstHoursThis = 6 39 52.270669440016206
            # https://dc.zah.uni-heidelberg.de/apfs/times/q/form says 2000-01-01 00:00:00	06 39 52.2717 yup

            #dataTimeUtcStrThis = '2000-12-31 00:00:00.000'  # gstHoursThis = 6.648605536400005 hours
            #                                                       vs table=6.6486056 yup

            #dataTimeUtcStrThis = '2001-12-31 00:00:00.000'  # gstHoursThis = 6.632691442400002 hours
            #                                                       vs table=6.6326915 yup

            #dataTimeUtcStrThis = '2010-12-31 00:00:00.000'  # gstHoursThis = 6.620884245200045 hours
            #                                                       vs table=6.6208844 yup

            #dataTimeUtcStrThis = '2022-12-31 00:00:00.000'  # gstHoursThis = 6.627044590400033 hours
            #                                                                 gstHoursThis = 6 37 37.36052544011727
            # https://dc.zah.uni-heidelberg.de/apfs/times/q/form says 2022-12-31 00:00:00	06 37 37.3628 yup

            #print(' dataTimeUtcStrThis =', dataTimeUtcStrThis)

            # Calculate GST fractional sidereal day
            # https://www.astro.umd.edu/~jph/GST_eqn.pdf
            # gstHours = G2001 + 0.0657098244 * yearDay + 1.00273791 * hoursThis
            # gstHours = 6.6486056 + 0.0657098244 * yearDay + 1.00273791 * hoursThis

            #dataTimeUtcStrThis = dataTimeUtc[n].iso
            #   '2023-02-09 00:01:20.000'
            #    yyyy mm dd hh mm ssssss
            #    012345678901234567890123
            yearThis = int(dataTimeUtcStrThis[0:4])
            #print(' yearThis =', yearThis)
            monthThis = int(dataTimeUtcStrThis[5:7])
            #print(' monthThis =', monthThis)
            MonthDayThis   = int(dataTimeUtcStrThis[8:10])     # round up: fully count partial days
            #print(' MonthDayThis =', MonthDayThis)

            hoursThis = float(dataTimeUtcStrThis[11:13]) + float(dataTimeUtcStrThis[14:16]) / 60. + float(dataTimeUtcStrThis[17:]) / 3600.
            #print(' hoursThis =', hoursThis, 'hours')

            # round up yearDayThis: yearDayThis fully counts partial days
            if ((not yearThis % 4 and yearThis % 100) or not yearThis % 400):       # if leap year
                yearDayThis = [-1, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335][monthThis] + MonthDayThis   # leap year
            else:
                yearDayThis = [-1, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334][monthThis] + MonthDayThis   # non-leap year
            #print(' yearDayThis =', yearDayThis)

            # round up daysFromStartOf1999: daysFromStartOf1900 fully counts partial days
            daysFromStartOf1999 = (yearThis - 1999) * 365 + yearDayThis
            #print(' daysFromStartOf1999 =', daysFromStartOf1999, 'days')
            # add one day for each leap year Feb-29 since start of 1999, but not yearThis
            for i in range(1999, yearThis):
                #if ((i % 4 == 0 and i % 100 != 0) or (i % 400 == 0)):
                if ((not i % 4 and i % 100) or not i % 400):        # if leap year
                    #print(' i =', i)    
                    daysFromStartOf1999 += 1            # leap year
            #print(' daysFromStartOf1999 =', daysFromStartOf1999, 'days')

            gstHoursThis = 6.6147239 + 0.0657098244 * daysFromStartOf1999 + 1.00273791 * hoursThis
            #print(' gstHoursThis =', gstHoursThis, 'hours')
            gstHoursThis = gstHoursThis % 24.
            #print(' gstHoursThis =', gstHoursThis, 'hours')
            gstMinThis = gstHoursThis %1. * 60.
            gstSecThis = gstMinThis %1. * 60.
            #print('                                 gstHoursThis =', int(gstHoursThis), int(gstMinThis), gstSecThis)
            gstDayRad = gstHoursThis * piPPi / 24.      # in radians
            #print(' gstDayRad =', gstDayRad, 'radians')

            # https://dc.zah.uni-heidelberg.de/apfs/times/q/form
            # https://astronomy.stackexchange.com/questions/21002/how-to-find-greenwich-mean-sideral-time

            #ra = gstDayRad - ha - d1lon                 # in radians
            # Haystack srt.cat file stored Longitude as positive, ezRA stores as negative
            ra = gstDayRad - ha + d1lon                 # in radians
             
            if ra < 0.:
                ra += piPPi
            elif piPPi < ra:
                ra -= piPPi
            #print(' ra =', ra, 'radians')
            raDegThis = ra * oneEightZeroDPi            # in degrees
            #print(' raDegThis =', raDegThis, 'degrees')
            raHThis = raDegThis / 15.       # 24 / 360 = 1 / 15
            #print(' raHThis =', raHThis, 'hours')

            decDegThis = dec * oneEightZeroDPi          # in degrees
            #print(' decDegThis =', decDegThis, 'degrees')

            cosRa = math.cos(ra)
            cosDec = math.cos(dec)
            sinRa = math.sin(ra)
            sinDec = math.sin(dec)
            vsun = 3.1817257161747205e-15 * cosRa * cosDec \
                + 17.320508075688775 * sinRa * cosDec - 9.999999999999998 * sinDec

            x0 = cosRa * cosDec
            y0 = sinRa * cosDec
            z0 = sinDec
            y = y0 * 0.9170600744802925 + z0 * 0.3987490687063738

            z = z0 * 0.9170600744802925 - y0 * 0.3987490687063738
            soulat = math.atan2(z, np.sqrt(x0 * x0 + y * y))
            soulong = math.atan2(y, x0)

            # timeVlsr = for this sample n, seconds since start of 1900
            timeVlsr = (dataTimeUtc[n].mjd - dataTimeUtcVlsr2000.mjd) * 86400. + 3155673600.
            sunlong = (timeVlsr * 0.00001140795 + 280.) * piD180            # long=280 day 1

            vearth = -30. * math.cos(soulat) * math.sin(sunlong - soulong)
            gwest = cosDecc * math.cos(rp - rac)

            grad = cosDecc * math.sin(rp - rac)

            ggwest = gwest * sinDp + 0.43067750027824064

            gpole = gwest * cosDp - 0.22038881141180267

            lon0 = (math.atan2(ggwest, grad)) * oneEightZeroDPi
            gwest = cosDec * math.cos(rp - ra)

            grad = cosDec * math.sin(rp - ra)

            ggwest = gwest * sinDp - sinDec * cosDp

            gpole = gwest * cosDp + sinDec * sinDp

            d1glat = (math.atan2(gpole, math.sqrt(ggwest * ggwest + grad * grad))) * oneEightZeroDPi
            gLatDegThis = d1glat            # in degrees

            d1glon = (math.atan2(ggwest, grad)) * oneEightZeroDPi - lon0

            # map d1glon into (-180 to +180) degrees
            gLonDegThis = d1glon
            if gLonDegThis < -180.:
                gLonDegThis += 360.
            elif 180. < gLonDegThis:        # in degrees (+180 to +540) to (0 to +360)
                gLonDegThis -= 360.

            if ezConUseVlsr:
                vlsrThis = vsun + vearth    # km/s
                #print()
                #print()
                #print(' vsun =', vsun, 'km/s')
                #print(' vearth =', vearth, 'km/s')
                #print(' vlsrThis =', vlsrThis, 'km/s')
            else:
                vlsrThis = 0.               # km/s

            #exit()

        elif ezConAstroMath == 2:
            # use astropy

            # Coordinate of sky target at the UTC time from the data file
            # SkyCoord() wants time = Time('1991-06-06 12:00:00')
            pointingTelescope = SkyCoord(az = azimuthDeg[n]*u.deg, alt = elevationDeg[n]*u.deg,
                obstime = dataTimeUtcStrThis, frame = 'altaz', location = locBase)
            #print()
            #print()
            #print(' dataTimeUtcStrThis =', dataTimeUtcStrThis)

            # extract RaDec coordinates
            raDegThis = float(pointingTelescope.icrs.ra.degree)
            raHThis = raDegThis / 15.       # 24 / 360 = 1 / 15
            #print(' raHThis =', raHThis, 'Hours')
            decDegThis = float(pointingTelescope.icrs.dec.degree)
            #print(' decDegThis =', decDegThis, 'degrees')

            # extract Galactic coordinates
            gLatDegThis = float(pointingTelescope.galactic.b.degree)
            gLonDegThis = float(pointingTelescope.galactic.l.degree)
            if 180. < gLonDegThis:
                gLonDegThis -= 360.

            if ezConUseVlsr:        # astropy
                # https://gitlab.camras.nl/dijkema/HPIB/blob/185d241ad9bd7507ed90c9fa91fe0a63009d3eee/vlsr.py
                # https://astropy-cjhang.readthedocs.io/en/latest/api/
                #   astropy.coordinates.SkyCoord.html#astropy.coordinates.SkyCoord.radial_velocity_correction
                # brvc = barycentric radial velocity correction = velocity of solar system barycenter toward star
                #vStarEarthAroundSun = pointingTelescope.radial_velocity_correction(kind='barycentric')    # in m/sec
                # print(pointingTelescope.radial_velocity_correction(kind='barycentric'))   # says -17469.223186040872 m / s
                vStarEarthAroundSun = -float(pointingTelescope.radial_velocity_correction(kind='barycentric') / (1000. * u.m / u.s))   # into km/s
                #print(' pointingTelescope =', pointingTelescope)
                #print(' vStarEarthAroundSun =', vStarEarthAroundSun, 'km/s')

                # Projection of solar velocity towards the pointingTelescope star
                # https://www.khanacademy.org/math/multivariable-calculus/thinking-about-multivariable-function/x786f2022:vectors-and-matrices/a/dot-products-mvc
                #vsun_proj = psrc.cartesian.dot(psun.cartesian)*vsun

                # pointingTelescope currently contains (az, alt) in deg
                # For dot product, need pointingTelescope also containing (ra, dec) in deg
                pointingTelescope = SkyCoord(ra = raDegThis*u.deg, dec = decDegThis*u.deg,
                    obstime = dataTimeUtcStrThis, frame = 'icrs', location = locBase)
                #print(' pointingTelescope =', pointingTelescope)
                #print(pointingTelescope.cartesian.dot(pointingSun.cartesian) * vStarSunMax)     # says -17.46922318604087  km/s
                vStarSun = -float(pointingTelescope.cartesian.dot(pointingSun.cartesian) * vStarSunMax / (u.km / u.s))  # in km/s
                # and vStarSun has positive max is near ra=18.0567000180526 Hours
                #print(' pointingTelescope.cartesian =', pointingTelescope.cartesian)
                #print(' pointingSun =', pointingSun)    # <SkyCoord (ICRS): (ra, dec) in deg (270.95954167, 30.00466667)>
                #print(' pointingSun.cartesian =', pointingSun.cartesian)
                #vStarSun = 0
                #print(' vStarSun =', vStarSun, 'km/s')

                # VLSR = receding Velocity of the Local Standard of Rest (km/s)
                #vlsrThis = -float((vStarSun - vStarEarthAroundSun) / (1000. * u.m / u.s))   # to extract from units as km/s
                #vlsrThis = vStarSun - vStarEarthAroundSun
                vlsrThis = vStarEarthAroundSun - vStarSun
                #print(' vlsrThis =', vlsrThis, 'km/s')

                # for that last sample of N0RQV-8230209_00.txt,
                #   dataTimeUtcStrThis = 2023-02-09 23:58:56.000
                #   raHThis = 23.405257531500908  Hours
                #   decDegThis = 8.007827205726938  degrees
                #   vStarEarthAroundSun = -17.206217294776792  km/s
                #   vStarSun = -18.037474540029592  km/s
                #   vlsrThis = -0.8312572452528002  km/s
                # HawkRAO VLSR Calculator,
                # http://f4klo.ampr.org/vlsrKLO.php
                #   Radial Velocity Calculator
                #   UTC (DD/MM/YYYY hh:mm:ss):	
                #   09/02/2023 23:58:56
                #   RA (hh.hhhhh):	
                #   23.4052575
                #   DEC (±dd.ddddd):	
                #   8.00782720
                #   Latitude (±dd.ddddd):	
                #   40.299512
                #   Longitude (±dd.ddddd):	
                #   -105.08449
                #   ---
                #   Radial Velocity (±km/s):	
                #   +12.68 ======================================================================================= +12.68
                #   Local Sidereal Time (day):	
                #   0.095736

                # for the first sample of N0RQV-8230209_00.txt,
                #    dataTimeUtcStrThis = 2023-02-09 00:01:20.000
                #    raHThis = 23.379665787029346  Hours
                #    decDegThis = 8.007942475940645  degrees
                #    vStarEarthAroundSun = -17.46922318604087  km/s
                #    vStarSun = 0  km/s
                #    vlsrThis = 17.46922318604087  km/s
                #      data/N0RQV-8230209_00.txt   Total samples processed for signals     = 1 of 908

                # for the first and last samples of N0RQV-8230209_00.txt, with -ezConAstroMath 1
                #    # from ezCon230309a.py
                #    lat 40.299512 long -105.084491 amsl 1524.0 name N0RQV-8
                #    freqMin 1419.2 freqMax 1421.61 freqBinQty 256
                #    ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  ...
                #    #        0           1    2       3        4        5     6      ...
                #    59984.00093 23.415 8.132 -49.006 89.145 1.352e+01 1 ... ======================================= 13.52
                #    59984.99926 23.440 8.132 -49.195 89.649 1.338e+01 1 ... ======================================= 13.38
                #       vsun = -3.9173568308658924
                #       vearth = 17.29853211404944
            else:
                vlsrThis = 0.       # km/s

        else:
            # ezConAstroMath == 0:
            # fill with suspicious harmless values, to be ignored, faster if not needed for plots ?
            raHThis     = 0.        # hours
            decDegThis  = 0.        # degrees
            gLatDegThis = 0.        # degrees
            gLonDegThis = 0.        # degrees
            vlsrThis    = 0.        # km/s


        # store in ezConOut[n, column] coordinate columns (0.0 for unfinished antXTVLdDop and antXTVUdDop)
        # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  AzimuthDeg  ElevationDeg  AntXTVTCmDop
        #          0           1    2       3        4        5     6      7           8             9
        #   AntAvg  AntMax    RefAvg  RefMax
        #   10      11        12      13
        #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
        #   14       15          16        17         18          19
        if not samplesQtyProcessed:
            #    1., 0., 0., 0.,        # before experimentEzc for AzEl into .ezb Spare1 and Spare2
            ezConOut = np.array([
                dataTimeUtc[n].mjd, raHThis, decDegThis, gLatDegThis, gLonDegThis, vlsrThis,
                1., azimuthDeg[n], elevationDeg[n], 0.,
                antAvg[n], antMax[n], refAvg[n], refMax[n],
                antBAvg[n], antBMax[n], antRBAvg[n], antRBMax[n], 0., 0.])
        else:
            #    1., 0., 0., 0.,        # before experimentEzc for AzEl into .ezb Spare1 and Spare2
            ezConOut = np.concatenate([ezConOut, np.array([
                dataTimeUtc[n].mjd, raHThis, decDegThis, gLatDegThis, gLonDegThis, vlsrThis,
                1., azimuthDeg[n], elevationDeg[n], 0.,
                antAvg[n], antMax[n], refAvg[n], refMax[n],
                antBAvg[n], antBMax[n], antRBAvg[n], antRBMax[n], 0., 0.]) ])


        samplesQtyProcessed += 1

        # allow append to line
        print('\r  ', fileNameLast, '  Total samples processed for signals     =',
            f'{samplesQtyProcessed:,} of {antLen:,}', end='')

    print()
    ezConOut = np.reshape(ezConOut, (-1, 20))


    # free antAvg memory
    antAvg = []
    antAvg = None
    del antAvg
    # free antMax memory
    antMax = []
    antMax = None
    del antMax


    # free refAvg memory
    refAvg = []
    refAvg = None
    del refAvg
    # free refMax memory
    refMax = []
    refMax = None
    del refMax


    # free antBAvg memory
    antBAvg = []
    antBAvg = None
    del antBAvg
    # free antBMax memory
    antBMax = []
    antBMax = None
    del antBMax


    # free antRBAvg memory
    antRBAvg = []
    antRBAvg = None
    del antRBAvg
    # free antRBMax memory
    antRBMax = []
    antRBMax = None
    del antRBMax



def writeFileSdre():

    global programRevision          # string
    global commandString            # string
    global ezRAObsName              # string
    global fileWriteSdre            # file handle

    global ezConOut                 # float and int 2d array
    global antLen                   # integer

    print()
    print('   writeFileSdre ===============')

    # record the (complex?) ezCon command line as a comment at the top of .sdre file
    fileWriteSdre.write('\n# from ' + programRevision)
    fileWriteSdre.write('\n# ' + commandString)
    fileWriteSdre.write('\n\ndataFreqMin ' + str(fileFreqMin) + ' dataFreqMax ' + str(fileFreqMax) \
        + ' name ' + ezRAObsName)
    fileWriteSdre.write('\n' \
        + 'sdreMenu: TimeUtcMjd  RaDeg  DecDeg  GLatDeg  GLonDeg  VLSR  Count' \
        + '  AntAvg  RefAvg  AntBAvg  AntXTVTAvg' \
        + '  AntMax  RefMax  AntBMax  AntXTVTMax' \
        + '  AntXTVTCmDop  AntXTVTLdDop  AntXTVTUdDop')
    fileWriteSdre.write('\n' \
        + '#         0           1      2       3        4        5     6    ' \
        + '  7       8       9        10        ' \
        + '  11      12      13       14        ' \
        + '  15            16            17')
    fileWriteSdre.write('\n')

    # save ezConOut[] in columns
    ezConOutFmtS = \
        '%0.5f %0.3f %0.3f %0.3f %0.3f %0.3e %d ' + \
        '%0.5e %0.5e %0.5e %0.5e ' + \
        '%0.5e %0.5e %0.5e %0.5e ' + \
        '%0.3e %0.3e %0.3e'

    # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  AzimuthDeg  ElevationDeg  AntXTVTCmDop
    #          0           1    2       3        4        5     6      7           8             9
    #   AntAvg  AntMax    RefAvg  RefMax
    #   10      11        12      13
    #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
    #   14       15          16        17         18          19

    # to

    # sdreMenu: TimeUtcMjd  RaDeg  DecDeg  GLatDeg  GLonDeg  VLSR  Count  
    #           0           1      2       3        4        5     6      
    #   AntAvg  RefAvg  AntBAvg  AntXTVTAvg  
    #   7       8       9        10          
    #   AntMax  RefMax  AntBMax  AntXTVTMax      AntXTVTCmDop  AntXTVTLdDop  AntXTVTUdDop
    #   11      12      13       14              15            16            17

    # sdre columns <- ezb columns
    # ezb  columns = 0 1 2 3 4 5 6   10 12 14 18   11 13 15 19    0  0  0
    # sdre columns = 0 1 2 3 4 5 6    7  8  9 10   11 12 13 14   15 16 17
    for n in range(antLen):
        ezConOutThisSdre = ezConOut[n, :] + 0                   # copy all 20 ezb columns of one row
        ezConOutThisSdre[ 7] = ezConOutThisSdre[10]
        ezConOutThisSdre[ 8] = ezConOutThisSdre[12]
        ezConOutThisSdre[ 9] = ezConOutThisSdre[14]
        ezConOutThisSdre[10] = ezConOutThisSdre[18]

        #ezConOutThisSdre[11] = ezConOutThisSdre[11]
        ezConOutThisSdre[12] = ezConOutThisSdre[13]
        ezConOutThisSdre[13] = ezConOutThisSdre[15]
        ezConOutThisSdre[14] = ezConOutThisSdre[19]
        
        ezConOutThisSdre[15:18] = 0.

        ezConOutThisSdre = ezConOutThisSdre[:18]                # trim off last 2 columns
        ezConOutThisSdre[1] = ezConOutThisSdre[1] * 15.         # convert: RaDeg  <-  RaH (360 / 24 = 15)

        np.savetxt(fileWriteSdre, [ezConOutThisSdre], fmt = ezConOutFmtS)

    fileWriteSdre.write('\n')
    fileWriteSdre.close()   



def writeFileEzb():

    global programRevision          # string
    global commandString            # string
    global ezRAObsName              # string
    global fileWriteEzb             # file handle

    global ezConOut                 # float and int 2d array
    global antLen                   # integer

    print()
    print('   writeFileEzb ===============')

    # record the (complex?) ezCon command line as a comment at the top of .ezb file
    fileWriteEzb.write(f'\n# from {programRevision}\n')
    fileWriteEzb.write(f'# {commandString}\n\n')
    fileWriteEzb.write(f'lat {ezRAObsLat} long {ezRAObsLon} amsl {ezRAObsAmsl} name {ezRAObsName}\n')
    fileWriteEzb.write(f'freqMin {fileFreqMin} freqMax {fileFreqMax} freqBinQty {fileFreqBinQty}\n')
    fileWriteEzb.write( \
        'ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  AzimuthDeg  ElevationDeg  AntXTVTCmDop' \
        + '    AntAvg  AntMax    RefAvg  RefMax' \
        + '    AntBAvg  AntBMax    AntRBAvg  AntRBMax    '+antXNameL[1]+'TVTAvg  '+antXNameL[1]+'TVTMax\n')
    #    + '    AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax\n')
    fileWriteEzb.write( \
        '#        0           1    2       3        4        5     6      7           8             9           ' \
        + '    10      11        12      13    ' \
        + '    14       15         16        17          18           19\n')

    # save ezConOut[] in columns
    # experimentEzc for AzEl into .ezb Spare1 and Spare2
    #    '%0.5f %0.3f %0.3f %0.3f %0.3f %0.3e %d %d %d %d ' + \
    ezConOutFmtS = \
        '%0.5f %0.3f %0.3f %0.3f %0.3f %0.3e %d %0.1f %0.1f %0.5e ' + \
        '%0.5e %0.5e %0.5e %0.5e ' + \
        '%0.5e %0.5e %0.5e %0.5e %0.5e %0.5e'
    for n in range(antLen):
        np.savetxt(fileWriteEzb, [ezConOut[n, :]], fmt = ezConOutFmtS)
    fileWriteEzb.write('\n')
    fileWriteEzb.close()   



def writeFileStudy():

    global fileWriteStudy           # file handle
    global antXNameL                # list of strings

    fileWriteStudy.write( \
        '\n\n\n============================================================================ ant\n\n\n')
    fileWriteStudy.write(studyTime(10, 'AntAvg'))
    fileWriteStudy.write(studyTime(11, 'AntMax'))

    fileWriteStudy.write( \
        '\n\n\n============================================================================ ref\n\n\n')
    fileWriteStudy.write(studyTime(12, 'RefAvg'))
    fileWriteStudy.write(studyTime(13, 'RefMax'))
    
    fileWriteStudy.write( \
        '\n\n\n============================================================================ antB\n\n\n')
    fileWriteStudy.write(studyTime(14, 'AntBAvg'))
    fileWriteStudy.write(studyTime(15, 'AntBMax'))
    
    fileWriteStudy.write( \
        '\n\n\n============================================================================ antRB\n\n\n')
    fileWriteStudy.write(studyTime(16, 'AntRBAvg'))
    fileWriteStudy.write(studyTime(17, 'AntRBMax'))

    fileWriteStudy.write( \
        '\n\n\n============================================================================ antXTVT\n\n\n')
    fileWriteStudy.write(studyTime(18, antXNameL[1] + 'TVTAvg'))
    fileWriteStudy.write(studyTime(19, antXNameL[1] + 'TVTMax'))
    fileWriteStudy.write( \
        '\n\n\n============================================================================\n')



def writeFileGal():
    # write velocity data arrays to Gal.npz file

    global antXNameL                    # list of strings
    global antXTVT                      # float 2d array
    global antLen                       # integer
    global velGLonP180                  # float 2d array     creation
    global velGLonP180Count             # integer array      creation
    global velGLonP180CountSum          # integer            creation
    global galDecP90GLonP180Count       # integer array      creation

    global fileFreqMin                  # float
    global fileFreqMax                  # float
    global fileFreqBinQty               # integer
    global ezConGalCrossingGLatCenterL  # float list
    global ezConGalCrossingGLatNear     # float
    global fileNameLast                 # string

    # if Galactic Latitude Crossings not wanted, then return
    if ezConGalCrossingGLatNear == 0.:
        return(1)

    print()
    print('   writeFileGal ===============')

    for ezConGalCrossingGLatCenter in ezConGalCrossingGLatCenterL:
        # Velocity by Galactic Longitude (gLon) grid.
        # gLon is -180thru+180, adding 180, gives gLonP180 as 0thru360 which is more convenient.
        velGLonP180 = np.zeros([fileFreqBinQty, 361], dtype = float)    # fileFreqBinQty by 0thru360 gLonP180
        velGLonP180Count = np.zeros([361], dtype = int)                 # count of saved spectrums in velGLonP180
        # Declination (dec) is -90thru+90, adding 90, gives decP90 as 0thru180 which is more convenient.
        # galDecP90GLonP180Count is floats to allow mask replacement with np.nan later.
        galDecP90GLonP180Count = np.zeros([181, 361], dtype = int)      # 0thru180 decP90 by 0thru360 gLonP180

        for n in range(antLen):
            gLatDegThis = ezConOut[n, 3]                        # gLatDeg is -90. thru +90.

            # if n is close enough to Galactic GLat, a Galactic crossing
            if abs(gLatDegThis - ezConGalCrossingGLatCenter) <= ezConGalCrossingGLatNear:
                gLonP180 = int(ezConOut[n, 4]) + 180            # gLonP180 is RtoL from 0 thru 360

                # sum the current antXTVT spectrum to the grid column, and increment the column count
                # but reverse the freqBin elements,
                #   because highest freqBin = highest freq = approaching fastest = most negative "velocity"
                #velGLonP180[:, gLonP180] += antXTV[:, n][::-1]
                velGLonP180[:, gLonP180] += antXTVT[:, n][::-1]
                velGLonP180Count[gLonP180] += 1

                # For each declination, several gLat may be 'close enough' to count as a crossing.
                # Increment at each crossing's dec and gLon.
                galDecP90GLonP180Count[int(ezConOut[n, 2] + 90), gLonP180] += 1     # declination + 90

        #print('velGLonP180 = ')
        #print(velGLonP180)
        #print(velGLonP180.shape)
        #print()

        #print('velGLonP180Count = ')
        #print(velGLonP180Count)
        #print(velGLonP180Count.shape)
        #print()

        print()
        print(f' ezConGalCrossingGLatCenter = {ezConGalCrossingGLatCenter:04.1f}')
        #print(' ezConGalCrossingGLatCenter =', ezConGalCrossingGLatCenter)
        velGLonP180CountSum = velGLonP180Count.sum()
        print(' velGLonP180CountSum =', velGLonP180CountSum)

        if velGLonP180CountSum:       # if anything in velGLonP180 to save or plot
            # for fileNameLast of  data/2021_333_00.rad.txt  create fileGalWriteName as  data/2021_333_00.radGal.npz
            #fileGalWriteName = fileNameLast.split(os.path.sep)[-1].split('.')[-2] + 'Gal.npz'
            #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] + 'Gal.npz'
            if ezConGalCrossingGLatCenter < 0:
                # output filenames *Nxx.xGal.npz (N for Negative)
                fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                    + f'N{-ezConGalCrossingGLatCenter:04.1f}Gal.npz'
                # output filenames *Gal.npz (N for Negative)
                #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                #    + f'N{-ezConGalCrossingGLatCenter:02d}Gal.npz'
            else:
                # output filenames *Pxx.xGal.npz (P for Negative)
                fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                    + f'P{ezConGalCrossingGLatCenter:04.1f}Gal.npz'
                # output filenames *PxxGal.npz (P for Positive)
                #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                #    + f'P{ezConGalCrossingGLatCenter:02d}Gal.npz'
            #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-8] \
            #    + 'GalC.npz'   # ezGal combines .npz
            #print('   ezRAObsName = ', ezRAObsName)

            # *Gal.npz file definition from here, ezCon's writeFileGal()
            #   np.savez_compressed(fileGalWriteName,           # filename
            #       fileObsName=np.array(ezRAObsName),          # string
            #       fileFreqMin=np.array(fileFreqMin),          # float
            #       fileFreqMax=np.array(fileFreqMax),          # float
            #       fileFreqBinQty=np.array(fileFreqBinQty),    # float
            #       velGLonP180=velGLonP180,                    # float: fileFreqBinQty by 0thru360 gLonP180
            #       velGLonP180Count=velGLonP180Count,          # int:                     0thru360 gLonP180
            #       galDecP90GLonP180Count=galDecP90GLonP180Count,  # int: 0thru180 decP90 by 0thru360 gLonP180
            #       antXTVTName=antXNameL[1]+'TVT',                         # string
            #       ezConGalCrossingGLatCenter=ezConGalCrossingGLatCenter,  # float
            #       ezConGalCrossingGLatNear=ezConGalCrossingGLatNear)      # float

            np.savez_compressed(fileGalWriteName,
                fileObsName=np.array(ezRAObsName),
                fileFreqMin=np.array(fileFreqMin), 
                fileFreqMax=np.array(fileFreqMax),
                fileFreqBinQty=np.array(fileFreqBinQty),
                velGLonP180=velGLonP180,
                velGLonP180Count=velGLonP180Count,
                galDecP90GLonP180Count=galDecP90GLonP180Count,
                antXTVTName=antXNameL[1]+'TVT',
                ezConGalCrossingGLatCenter=ezConGalCrossingGLatCenter,
                ezConGalCrossingGLatNear=ezConGalCrossingGLatNear)
            # antXTVTName was added to file definition later, on 230401
            # ezConGalCrossingGLatCenter was added to file definition later, on 230623
            # ezConGalCrossingGLatNear was added to file definition later, on 230625

            #npzfile = np.load(directory + os.path.sep + fileReadName)
            #ezRAObsName = npzfile['ezRAObsName'] 
            #fileFreqMin    = npzfile['fileFreqMin'] 
            #fileFreqMax    = npzfile['fileFreqMax']
            #fileFreqBinQty = npzfile['fileFreqBinQty'] 
            #velGLonP180      = npzfile['velGLonP180']
            #velGLonP180Count = npzfile['velGLonP180Count']
            #galDecP90GLonP180Count = npzfile['galDecP90GLonP180Count']


            # Prepare velGLonP180 for later ezCon plots.
            # velGLonP180 has been filled with sums of samples.
            #   Now for each column, convert to sum's average.
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



def writeFileGalRaDecNear():
    # write velocity data array to Gal.npz file
    # Just like writeFileGal(), but different qualifier question for the samples,
    # and only gLonP180 = 0 is used.

    global antXNameL                    # list of strings
    global antXTVT                      # float 2d array
    global antLen                       # integer
    global velGLonP180                  # float 2d array     creation
    global velGLonP180Count             # integer array      creation
    global velGLonP180CountSum          # integer            creation
    global galDecP90GLonP180Count       # integer array      creation

    global fileFreqMin                  # float
    global fileFreqMax                  # float
    global fileFreqBinQty               # integer
    #global ezConGalCrossingGLatCenterL  # float list
    #global ezConGalCrossingGLatNear     # float
    global ezConGalRaDecNearNearL       # float list
    global fileNameLast                 # string

    # if ezConGalRaDecNearNearL not filled, then return
    if not ezConGalRaDecNearNearL:
        return(1)

    print()
    print('   writeFileGalRaDecNear ===============')

    # Velocity by Galactic Longitude (gLon) grid.
    # gLon is -180thru+180, adding 180, gives gLonP180 as 0thru360 which is more convenient.
    velGLonP180 = np.zeros([fileFreqBinQty, 361], dtype = float)    # fileFreqBinQty by 0thru360 gLonP180
    velGLonP180Count = np.zeros([361], dtype = int)                 # count of saved spectrums in velGLonP180
    # Declination (dec) is -90thru+90, adding 90, gives decP90 as 0thru180 which is more convenient.
    # galDecP90GLonP180Count is floats to allow mask replacement with np.nan later.
    galDecP90GLonP180Count = np.zeros([181, 361], dtype = int)      # 0thru180 decP90 by 0thru360 gLonP180

    # define RaDec span
    spanRaHMin    = ezConGalRaDecNearNearL[0] - ezConGalRaDecNearNearL[2]
    spanRaHMax    = ezConGalRaDecNearNearL[0] + ezConGalRaDecNearNearL[2]
    spanDecDegMin = ezConGalRaDecNearNearL[1] - ezConGalRaDecNearNearL[3]
    spanDecDegMax = ezConGalRaDecNearNearL[1] + ezConGalRaDecNearNearL[3]

    for n in range(antLen):
        raHThis    = ezConOut[n, 1]         # RaH is 0. thru 24.
        decDegThis = ezConOut[n, 2]         # DecDeg is -90. thru +90.

        # if n is within RaDec span, use spectrum
        if spanRaHMin <= raHThis and raHThis <= spanRaHMax \
            and spanDecDegMin <= decDegThis and decDegThis <= spanDecDegMax:
                gLonP180 = int(ezConOut[n, 4]) + 180            # gLonP180 is RtoL from 0 thru 360
                #gLonP180 = 0        # wasteful, but RGal.npz file size is only 6.0K

                # sum the current antXTVT spectrum to the grid column, and increment the column count
                # but reverse the freqBin elements,
                #   because highest freqBin = highest freq = approaching fastest = most negative "velocity"
                #velGLonP180[:, gLonP180] += antXTV[:, n][::-1]
                velGLonP180[:, gLonP180] += antXTVT[:, n][::-1]
                velGLonP180Count[gLonP180] += 1

                # For each declination, several gLat may be 'close enough' to count as a crossing.
                # Increment at each crossing's dec and gLon.
                #galDecP90GLonP180Count[int(ezConOut[n, 2] + 90), gLonP180] += 1     # declination + 90
                galDecP90GLonP180Count[0, gLonP180] += 1

    #print('velGLonP180 = ')
    #print(velGLonP180)
    #print(velGLonP180.shape)
    #print()

    #print('velGLonP180Count = ')
    #print(velGLonP180Count)
    #print(velGLonP180Count.shape)
    #print()

    print()
    #print(f' ezConGalCrossingGLatCenter = {ezConGalCrossingGLatCenter:04.1f}')
    #print(' ezConGalCrossingGLatCenter =', ezConGalCrossingGLatCenter)
    velGLonP180CountSum = velGLonP180Count.sum()
    print(' velGLonP180CountSum =', velGLonP180CountSum)

    if velGLonP180CountSum:       # if anything in velGLonP180 to save or plot
        # for fileNameLast of  data/2021_333_00.rad.txt  create fileGalWriteName as  data/2021_333_00.radGal.npz
        #fileGalWriteName = fileNameLast.split(os.path.sep)[-1].split('.')[-2] + 'Gal.npz'
        #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] + 'Gal.npz'
        #if ezConGalCrossingGLatCenter < 0:
        #    # output filenames *Nxx.xGal.npz (N for Negative)
        #    fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
        #        + f'N{-ezConGalCrossingGLatCenter:04.1f}Gal.npz'
        #    # output filenames *Gal.npz (N for Negative)
        #    #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
        #    #    + f'N{-ezConGalCrossingGLatCenter:02d}Gal.npz'
        #else:
        #    # output filenames *Pxx.xGal.npz (P for Negative)
        #    fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
        #        + f'P{ezConGalCrossingGLatCenter:04.1f}Gal.npz'
        #    # output filenames *PxxGal.npz (P for Positive)
        #    #fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
        #    #    + f'P{ezConGalCrossingGLatCenter:02d}Gal.npz'

        # output filename, 2025_061_00.rad_0.8_41.3_0.1_0.1RGal.npz
        fileGalWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
            + f'_{ezConGalRaDecNearNearL[0]:02.1f}_{ezConGalRaDecNearNearL[1]:02.1f}' \
            + f'_{ezConGalRaDecNearNearL[2]:02.1f}_{ezConGalRaDecNearNearL[3]:02.1f}RGal.npz'

        #print('   ezRAObsName = ', ezRAObsName)
        ezConGalCrossingGLatCenter = 999.   # silly flag for ezConGalRaDecNear
        ezConGalCrossingGLatNear   = 0.
        np.savez_compressed(fileGalWriteName,
            fileObsName=np.array(ezRAObsName),
            fileFreqMin=np.array(fileFreqMin), 
            fileFreqMax=np.array(fileFreqMax),
            fileFreqBinQty=np.array(fileFreqBinQty),
            velGLonP180=velGLonP180,
            velGLonP180Count=velGLonP180Count,
            galDecP90GLonP180Count=galDecP90GLonP180Count,
            antXTVTName=antXNameL[1]+'TVT',
            ezConGalCrossingGLatCenter=ezConGalCrossingGLatCenter,
            ezConGalCrossingGLatNear=ezConGalCrossingGLatNear)
        # antXTVTName was added to file definition later, on 230401
        # ezConGalCrossingGLatCenter was added to file definition later, on 230623
        # ezConGalCrossingGLatNear was added to file definition later, on 230625

        #npzfile = np.load(directory + os.path.sep + fileReadName)
        #ezRAObsName = npzfile['ezRAObsName'] 
        #fileFreqMin    = npzfile['fileFreqMin'] 
        #fileFreqMax    = npzfile['fileFreqMax']
        #fileFreqBinQty = npzfile['fileFreqBinQty'] 
        #velGLonP180      = npzfile['velGLonP180']
        #velGLonP180Count = npzfile['velGLonP180Count']
        #galDecP90GLonP180Count = npzfile['galDecP90GLonP180Count']


        # Prepare velGLonP180 for later ezCon plots.
        # velGLonP180 has been filled with sums of samples.
        #   Now for each column, convert to sum's average.
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



def writeFileGLon():
    # write velocity data arrays to GLon.npz file

    global antXNameL                    # list of strings
    global antXTVT                      # float 2d array
    global antLen                       # integer
    global velGLonP180                  # float 2d array     creation
    global velGLonP180Count             # integer array      creation
    global velGLonP180CountSum          # integer            creation

    global fileFreqMin                  # float
    global fileFreqMax                  # float
    global fileFreqBinQty               # integer
    global ezConGalCrossingGLonCenterL  # float list
    global ezConGalCrossingGLonNear     # float
    global fileNameLast                 # string

    # if Galactic Longitude Crossings not wanted, then return
    if not len(ezConGalCrossingGLonCenterL) or ezConGalCrossingGLonNear == 0.:
        return(1)

    print()
    print('   writeFileGLon ===============')

    # Velocity by Galactic Latitude (gLat) grid.
    # gLat is -90thru+90, adding 90, gives gLatP90 as 0thru180 which is more convenient.
    velGLatP90 = np.zeros([fileFreqBinQty, 181], dtype = float)    # fileFreqBinQty by 0thru180 gLatP90
    velGLatP90Count = np.zeros([181], dtype = int)                 # count of saved spectrums in velGLatP90

    for ezConGalCrossingGLonCenter in ezConGalCrossingGLonCenterL:
        for n in range(antLen):
            gLonDegThis = ezConOut[n, 4]                        # gLonDeg is -180. thru +180.

            # if n is close enough to Galactic Longitude, a GLon crossing
            if abs(gLonDegThis - ezConGalCrossingGLonCenter) <= ezConGalCrossingGLonNear:
                gLatP90 = int(ezConOut[n, 3]) + 90            # gLatP90 is from 0 thru 180

                # sum the current antXTVT spectrum to the grid column, and increment the column count
                # but reverse the freqBin elements,
                #   because highest freqBin = highest freq = approaching fastest = most negative "velocity"
                velGLatP90[:, gLatP90] += antXTVT[:, n][::-1]
                velGLatP90Count[gLatP90] += 1

        #print('velGLatP90 = ')
        #print(velGLatP90)
        #print(velGLonP90.shape)
        #print()

        #print('velGLatP90Count = ')
        #print(velGLatP90Count)
        #print(velGLatP90Count.shape)
        #print()

        print()
        print(' ezConGalCrossingGLonCenter =', ezConGalCrossingGLonCenter)
        velGLatP90CountSum = velGLatP90Count.sum()
        print(' velGLatP90CountSum =', velGLatP90CountSum)

        if velGLatP90CountSum:       # if anything in velGLatP90 to save or plot
            if ezConGalCrossingGLonCenter < 0:
                # output filenames *Nxxx.xGLon.npz (N for Negative)
                fileGLonWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                    + f'N{-ezConGalCrossingGLonCenter:05.1f}GLon.npz'
                # output filenames *NxxxGLon.npz (N for Negative)
                #fileGLonWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                #    + f'N{-ezConGalCrossingGLonCenter:03d}GLon.npz'
            else:
                # output filenames *Pxxx.xGLon.npz (P for Positive)
                fileGLonWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                    + f'P{ezConGalCrossingGLonCenter:05.1f}GLon.npz'
                # output filenames *PxxxGLon.npz (P for Positive)
                #fileGLonWriteName = fileNameLast.split(os.path.sep)[-1][:-4] \
                #    + f'P{ezConGalCrossingGLonCenter:03d}GLon.npz'
            #print('   ezRAObsName = ', ezRAObsName)
            np.savez_compressed(fileGLonWriteName,
                fileObsName=np.array(ezRAObsName),
                fileFreqMin=np.array(fileFreqMin), 
                fileFreqMax=np.array(fileFreqMax),
                fileFreqBinQty=np.array(fileFreqBinQty),
                velGLatP90=velGLatP90,
                velGLatP90Count=velGLatP90Count,
                antXTVTName=antXNameL[1]+'TVT',
                ezConGalCrossingGLonCenter=ezConGalCrossingGLonCenter,
                ezConGalCrossingGLonNear=ezConGalCrossingGLonNear)



def studyTime(column, data1dName):
    # returns long string

    # column                                    # integer
    # data1dName                                # string

    global ezConOut                             # float and int 2d array
    global dataTimeUtc                          # 'astropy.time.core.Time' object array

    # '5 * str(column - 10)' below provides a (unique?) 5-character string.
    #  RefMax is .ezb file column 13, so later, in the large ezConStudyxxx.txt file,
    #  search for ' 33333' to easily find the RefMax section.
    OutString = f'\n  {fileNameLast}  ================================== ' \
        + f'{5 * str(column - 10)} Time study of {data1dName}\n'

    data1d = ezConOut[:, column]
    
    data1dMax = data1d.max()
    data1dMin = data1d.min()
    OutString += f'                         {data1dName}Max = {data1dMax}\n'
    OutString += f'                         {data1dName}Avg = {np.mean(data1d)}\n'
    OutString += f'                         {data1dName}Min = {data1dMin}\n'

    data1dSpanD100 = (data1dMax - data1dMin) / 100.
    # to allow division by data1dSpanD100
    if not data1dSpanD100:
        data1dSpanD100 = 1e-14

    if column == 18 or column == 19:
        pluckArgumentS = 'ezConAntXTVTPluck'
    else:
        pluckArgumentS = 'ezConAntPluck'

    OutString += f'\n Sample numbers of 20 highest-values of {data1dName}:\n'
    data1dIdxbyValueHigh = np.array(data1d).argsort()[::-1][:20]
    for i in range(len(data1dIdxbyValueHigh)):
        data1dIdxbyValueHighThis = data1dIdxbyValueHigh[i]
        #data1dThis = data1d[data1dIdxbyValueHigh[i]]
        data1dThis = data1d[data1dIdxbyValueHighThis]
        data1dThisPercent = (data1dThis - data1dMin) / data1dSpanD100
        # '2023-02-09 00:01:20.000'
        #  012345678901234567890123
        #             00:01
        #             123456
        timeThisS = dataTimeUtc[data1dIdxbyValueHighThis].iso[11:16]
        #OutString += f' i = {i}      sample {data1dIdxbyValueHigh[i]}' \
        #    + f'      {data1dName} = {data1dThis}       {data1dThisPercent} %'
        OutString += f' i = {i}      sample {data1dIdxbyValueHighThis}' \
            + f'   {timeThisS}   {data1dName} = {data1dThis}   {data1dThisPercent} %'
        if data1dThisPercent < 95:
            OutString += '  <=========== < 95%\n'
        else:
            OutString += '\n'
        if i == 4 or i == 9 or i == 14:
            OutString += '\n'
    OutString += f'                 Maybe try arguments like    -{pluckArgumentS} '\
        + f'{data1dIdxbyValueHigh[0]}\n'

    OutString += f'\n Sample numbers of 20 lowest-values of {data1dName}:\n'
    data1dIdxbyValueLow = np.array(data1d).argsort()[:20]
    for i in range(len(data1dIdxbyValueLow)):
        data1dIdxbyValueLowThis = data1dIdxbyValueLow[i]
        data1dThis = data1d[data1dIdxbyValueLowThis]
        data1dThisPercent = (data1dThis - data1dMin) / data1dSpanD100
        timeThisS = dataTimeUtc[data1dIdxbyValueHighThis].iso[11:16]
        OutString += f' i = {i}      sample {data1dIdxbyValueLowThis}' \
            + f'   {timeThisS}   {data1dName} = {data1dThis}   {data1dThisPercent} %'
        if 5 < data1dThisPercent:
            OutString += '  <=========== > 5%\n'
        else:
            OutString += '\n'
        if i == 4 or i == 9 or i == 14:
            OutString += '\n'
    OutString += f'                 Maybe try arguments like    -{pluckArgumentS} '\
        + f'{data1dIdxbyValueLow[0]}\n'

    OutString += f'\n Sample numbers of 20 largest change values of {data1dName}:\n'
    data1dIdxbyValueDeltaHighM1 = np.array(abs(data1d[1:] - data1d[:-1])).argsort()[::-1][:20]
    for i in range(len(data1dIdxbyValueDeltaHighM1)):
        data1dIdxbyValueDeltaHighM1This = data1dIdxbyValueDeltaHighM1[i]
        data1dDeltaThis = \
            data1d[data1dIdxbyValueDeltaHighM1This + 1] - data1d[data1dIdxbyValueDeltaHighM1This]
        timeThisS = dataTimeUtc[data1dIdxbyValueDeltaHighM1This + 1].iso[11:16]
        OutString += f' i = {i}      sample {data1dIdxbyValueDeltaHighM1This + 1}' \
            + f'   {timeThisS}   {data1dName}Delta = {data1dDeltaThis}' \
            + f'   {data1dDeltaThis / data1dSpanD100} %\n'
        if i == 4 or i == 9 or i == 14:
            OutString += '\n'
    OutString += f'                 Maybe try arguments like    -{pluckArgumentS} '\
        + f'{data1dIdxbyValueDeltaHighM1[0] + 1}\n'
        
    return(OutString)



def printGoodbye(startTime):

    global rawLen                   # integer
    global antLen                   # integer
    #global refLen                   # integer
    global refQty                   # integer
    global programRevision          # string
    global commandString            # string
    global ezConPlotRangeL          # integer list
    global OutFreqString            # string

    # print status
    if 0:
        print()
        print('   ezRAObsName =', ezRAObsName)
        print('   ezRAObsLat  =', ezRAObsLat)
        print('   ezRAObsLon  =', ezRAObsLon)
        print('   ezRAObsAmsl =', ezRAObsAmsl)
        print()
        print('   ezConAzimuth   =', ezConAzimuth)
        print('   ezConElevation =', ezConElevation)
        print('   ezConAddAzDeg  =', ezConAddAzDeg)
        print('   ezConAddElDeg  =', ezConAddElDeg)
        print()
        print('   ezConInputdBm  =', ezConInputdBm)
        print()
        print('   ezConRawSamplesUseL   =', ezConRawSamplesUseL)
        print('   ezConRawFreqBinHideL  =', ezConRawFreqBinHideL)
        print()
        print('   ezConRefMode          =', ezConRefMode)
        print()
        print('   ezConAntSamplesUseL   =', ezConAntSamplesUseL)
        print('   ezConAntPluckL        =', ezConAntPluckL)
        print('   ezConAntAvgPluckQtyL  =', ezConAntAvgPluckQtyL)
        print('   ezConAntAvgPluckFracL =', ezConAntAvgPluckFracL)
        print('   ezConAntFreqBinSmooth =', ezConAntFreqBinSmooth)
        print()
        print('   ezConRefAvgPluckQtyL  =', ezConRefAvgPluckQtyL)
        print('   ezConRefAvgPluckFracL =', ezConRefAvgPluckFracL)
        print()
        print('   ezConUseRefSub        =', ezConUseRefSub)
        print()
        print('   ezConAntBaselineFreqBinsFracL   =', ezConAntBaselineFreqBinsFracL)
        print('   ezConAntRABaselineFreqBinsFracL =', ezConAntRABaselineFreqBinsFracL)
        print()
        print('   ezConAntXInput                  =', ezConAntXInput)
        print('   ezConAntXTVTLevelL              =', ezConAntXTVTLevelL)
        print()
        print('   ezConAntXTFreqBinsFracL         =', ezConAntXTFreqBinsFracL)
        print('   ezConUseVlsr                    =', ezConUseVlsr)
        print('   ezConAntXTVTFreqBinsFracL       =', ezConAntXTVTFreqBinsFracL)
        print()
        print('   ezConAntXTVTMaxPluckQtyL        =', ezConAntXTVTMaxPluckQtyL)
        print('   ezConAntXTVTMaxPluckValL        =', ezConAntXTVTMaxPluckValL)
        print('   ezConAntXTVTAvgPluckQtyL        =', ezConAntXTVTAvgPluckQtyL)
        print('   ezConAntXTVTAvgPluckValL        =', ezConAntXTVTAvgPluckValL)
        print('   ezConAntXTVTPluckL              =', ezConAntXTVTPluckL)
        print('   ezConAntXTVTSmooth              =', ezConAntXTVTSmooth)
        print('   ezCon087Csv                     =', ezCon087Csv)
        print()
        print('   ezCon399SignalSampleByFreqBinL  =', ezCon399SignalSampleByFreqBinL)
        print()
        print('   ezConAstroMath        =', ezConAstroMath)
        print()
        print('   ezConGalCrossingGLat  =', ezConGalCrossingGLat)
        print('   ezConVelGLonEdgeFrac  =', ezConVelGLonEdgeFrac)
        print('   ezConVelGLonEdgeLevel =', ezConVelGLonEdgeLevel)
        print()
        print('   ezConHeatVMinMaxL     =', ezConHeatVMinMaxL)
        print('   ezConRawDispIndex     =', ezConRawDispIndex)
        print('   ezConDispGrid         =', ezConDispGrid)
        print('   ezConDispFreqBin      =', ezConDispFreqBin)
        print('   ezConPlotRangeL       =', ezConPlotRangeL)
        print()
        print(f'   rawLen = {rawLen:,}')
        print(f'   antLen = {antLen:,}')
        print(f'   rawLen / antLen = {rawLen / antLen:,}')
        print(f'   antLen / rawLen = {antLen / rawLen:,}')

    print('\n\n\n ezConPlotRangeL =', ezConPlotRangeL)

    fileWriteStudy.write(OutFreqString + '\n\n\n\n')

    stopTime = time.time()
    stopTimeS = time.ctime()
    #OutString = f'\n rawLen = {rawLen:,}\n'
    OutString = f'\n rawLen = {rawLen:,}\n'
    #OutString += f' refLen = {refLen}\n'
    OutString += f' refQty = {refQty:,}\n'
    OutString += f' antLen = {antLen:,}\n'
    OutString += f'\n That Python command,\n'
    OutString += f'   {commandString}\n'
    OutString += f' took {int(stopTime-startTime)} seconds = {(stopTime-startTime)/60.:1.1f} minutes\n'
    OutString += f' Now = {stopTimeS[:-5]}\n'
    OutString += f'\n programRevision = {programRevision}\n'
    print(OutString)
    fileWriteStudy.write(OutString)

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



#A#####################################################################################



def plotEzCon1dByFreqBin(plotName, plotData1d, plotColorS, plotYLabel):

    # plotName                                  # string
    # plotData1d                                # float 1d array
    # plotColorS                                # string
    # plotYLabel                                # string

    global byFreqBinX                           # float array
    global ezConDispGrid                        # integer
    global dopplerSpanD2                        # float

    plt.clf()

    plt.plot(byFreqBinX, plotData1d, plotColorS)

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel('Doppler (MHz)')
    plt.xlim(-dopplerSpanD2, dopplerSpanD2)

    plt.ylabel(plotYLabel)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon1dSamplesAnt(plotName, plotData1d, plotYLimL, plotColorS, plotYLabel):

    # plotName                                  # string
    # plotData1d                                # float 1d array
    # plotYLimL                                 # list
    # plotColorS                                # string
    # plotYLabel                                # string

    global fileNameLast                         # string
    global titleS                               # string
    global ezConDispGrid                        # integer
    global dataTimeUtc                          # 'astropy.time.core.Time' object array
    global ezConRawDispIndex                    # integer
    global antLenM1                             # integer

    global xTickLocsAnt                         # array         creation?
    global xTickLabelsAnt                       # list          creation?
    global xLabelSAnt                           # string        creation?

    plt.clf()

    plt.plot(plotData1d, plotColorS)

    plt.title(titleS)
    plt.grid(ezConDispGrid)
    
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
                if ezConRawDispIndex:
                    xTickLabelsAnt[i] = f'{rawIndex[xTickLocsAntIInt]:,}  {xTickLocsAntIInt:,}  ' \
                        + dataTimeUtc[xTickLocsAntIInt].iso[11:16]
                else:
                    xTickLabelsAnt[i] = f'{xTickLocsAntIInt:,}  ' \
                        + dataTimeUtc[xTickLocsAntIInt].iso[11:16]
            else:       # remove silly values
                xTickLocsAnt = np.delete(xTickLocsAnt, i)
                xTickLabelsAnt = np.delete(xTickLabelsAnt, i)
        # fill xTickLabelsAnt[-1], samplesQtyM1 is usually less than xTickLocsAnt[-1]
        xTickLocsAnt[-1] = antLenM1
        if 0.975 < xTickLocsAnt[-2] / antLenM1:   # if last label overlaps, blank it
            xTickLabelsAnt[-1] = ''
        elif ezConRawDispIndex:
            xTickLabelsAnt[-1] = f'{rawIndex[-1]:,}  {antLenM1:,}  ' + dataTimeUtc[-1].iso[11:16]
        else:
            xTickLabelsAnt[-1] = f'{antLenM1:,}  ' + dataTimeUtc[-1].iso[11:16]
        if ezConRawDispIndex:
            xLabelSAnt = f'Raw Sample Number + Ant Sample Number (last={antLenM1:,}) with UTC Hour:Min (last=' \
                + dataTimeUtc[-1].iso[11:16] + ')'
        else:
            xLabelSAnt = f'Ant Sample Number (last={antLenM1:,}) with UTC Hour:Min (last=' \
                + dataTimeUtc[-1].iso[11:16] + ')'
    plt.xticks(xTickLocsAnt, xTickLabelsAnt, rotation=45, ha='right', rotation_mode='anchor')
    plt.xlabel(xLabelSAnt)
    plt.xlim(0, antLenM1)

    plt.ylabel(plotYLabel)
    if len(plotYLimL):
        plt.ylim(plotYLimL[0], plotYLimL[1])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon2dSamples(plotName, plotData2d, plotXLabel, plotXLast, plotYLabel, plotMax):

    # plotName                                  # string
    # plotData2d                                # float 2d array
    # plotXLabel                                # string
    # plotXLast                                 # integer
    # plotYLabel                                # string
    # plotNumberMax                             # integer

    global ezConHeatVMinMaxL                    # float list
    global titleS                               # string
    global ezConDispGrid                        # integer
    global ezConRawDispIndex                    # integer
    global dataTimeUtc                          # 'astropy.time.core.Time' object array

    global xTickLabelsHeatAntL                  # string list   creation?
    global xLabelSAnt                           # string        creation?
    global yTickHeatL                           # string list   creation?

    global fileFreqBinQty                       # integer
    #global freqCenter                           # float

    # plot heat map of ant
    heatVMin = ezConHeatVMinMaxL[0]             # minimum 3d value (color), <=0 for autoscale
    heatVMax = ezConHeatVMinMaxL[1]             # maximum 3d value (color), <=0 for autoscale

    plt.clf()

    if heatVMin <= 0:              # if should autoscale heatVMin
        if heatVMax <= 0:            # if should autoscale heatVMax
            # autoscale heatVMin and heatVMax
            heat_map = sb.heatmap(plotData2d,                               cmap='gnuplot')
        else:
            # only heatVMax available
            heat_map = sb.heatmap(plotData2d,                vmax=heatVMax, cmap='gnuplot')
    else:
        if heatVMax <= 0:            # if should autoscale heatVMax
            # only heatVMin available
            heat_map = sb.heatmap(plotData2d, vmin=heatVMin,                cmap='gnuplot')
        else:
            # heatVMin and heatVMax available
            heat_map = sb.heatmap(plotData2d, vmin=heatVMin, vmax=heatVMax, cmap='gnuplot')

    heat_map.set_title(titleS)
    if ezConDispGrid:
        heat_map.grid(b=True, which='major', color='black', linewidth=0.075)

    xTickLabelsHeatAntL = []
    #if not len(xTickLabelsHeatAntL):            # create xTickLabelsHeatAntL only if needed
    if 1:
        # create xTickLabelsHeatAntL
        xticklabels = heat_map.get_xticklabels()
        #print(xticklabels)
        for label in xticklabels:
            labelTextInt = int(label.get_text())
            #if 0 <= labelTextInt and labelTextInt < plotXLast:
            dataTimeUtcStrThis = dataTimeUtc[labelTextInt].iso[11:16]
            xTickLabelsHeatAntL.append(f'{labelTextInt:,}  ' + dataTimeUtcStrThis)

    # create xLabelSAnt
    if ezConRawDispIndex and (plotXLabel != 'Raw'):
        xLabelSAnt = f'Raw Sample Number + Ant Sample Number (last={plotXLast:,}) with UTC Hour:Min (last=' \
            + dataTimeUtc[-1].iso[11:16] + ')'
    else:
        xLabelSAnt = f'{plotXLabel} Sample Number (last={plotXLast:,}) with UTC Hour:Min (last=' \
            + dataTimeUtc[-1].iso[11:16] + ')'

    heat_map.set_xticklabels(xTickLabelsHeatAntL, rotation=90)
    heat_map.set_xlabel(xLabelSAnt)

    heat_map.invert_yaxis()
    if ezConDispFreqBin == 1:
        heat_map.set_ylabel(plotYLabel + ':  Frequency Bin',
            rotation=90, verticalalignment='bottom')
        heat_map.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(32))
        antYtickFn = lambda x, pos: f'{x:0.0f}'
    elif ezConDispFreqBin == 2:
        heat_map.set_ylabel(plotYLabel + ':  Frequency Bandwidth Fraction',
            rotation=90, verticalalignment='bottom')
        # 31.9835 gets 991, but not 1023 !!!!
        heat_map.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(32.))
        antYtickFn = lambda x, pos: f'{x / fileFreqBinQty:0.2f}'
    else:
        #heat_map.set_ylabel(plotYLabel + f':  Doppler MHz from {freqCenter:.3f} MHz',
        #    rotation=90, verticalalignment='bottom')
        heat_map.set_ylabel(plotYLabel,
            rotation=90, verticalalignment='bottom')
        #  256 / 24 = 10.666666 freqBin per ytick
        #heat_map.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(10.666666))
        # 1024 / 24 = 42.666666 freqBin per ytick
        #heat_map.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(42.666666))
        heat_map.yaxis.set_major_locator(matplotlib.ticker.MultipleLocator(fileFreqBinQty / 24.))
        antYtickFn = lambda x, pos: yTickHeatL[int(pos) - 1]
    heat_map.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(antYtickFn))

    if plotMax:
         # green dots for each sample's max
        plotData2dMaxY = np.argmax(plotData2d, axis=0)          # Y (=freqBin) for each sample's max
        plt.plot(plotData2dMaxY, 'go', markersize=2)

        #    # big violet dots on plot's max 1% values
        #    plotData2dSort = np.sort(plotData2d, axis=None)[::-1]   # flattened and sorted by decreasing value
        #    for n in range(1, int(0.01 * len(plotData2dSort))):
        #        plotData2dY, plotData2dX = np.where(plotData2d == plotData2dSort[n])
        #        plt.plot(plotData2dX, plotData2dY, 'o', c='violet', markersize=10)

        # big yellow dot on plot's max
        plotData2dMaxMaxY, plotData2dMaxMaxX = np.where(plotData2d == plotData2d.max())
        plt.plot(plotData2dMaxMaxX, plotData2dMaxMaxY, 'yo', markersize=10)
        #    plotData2dY, plotData2dX = np.where(plotData2d == plotData2dSort[0])
        #    plt.plot(plotData2dX, plotData2dY, 'yo', markersize=10)
        
    if plotYLabel[-2:] == 'TV':
        # add a thin black horizontal line at zero Doppler, for comparison
        plt.axhline(y=fileFreqBinQty/2, linewidth=0.5, color='black')
    
    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon000rawRaw():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list
    global xTickLabelsHeatAntL                  # string list

    global raw                                  # float 2d array
    global rawLen                               # integer

    plotName = 'ezCon000rawRaw.png'

    plotCountdown -= 1

    #if 0 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 0:
    if 0 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # force new xTickLabelsHeatAntL before and after plotting
    xTickLabelsHeatAntL = []
    plotEzCon2dSamples(plotName, raw, 'RawRaw', rawLen-1, f'RawRaw:  Doppler MHz', 0)
    xTickLabelsHeatAntL = []



def plotEzCon001raw():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list
    global xTickLabelsHeatAntL                  # string list

    global raw                                  # float 2d array
    global rawLen                               # integer

    plotName = 'ezCon001raw.png'

    plotCountdown -= 1

    #if 1 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 1:
    if 1 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # because Raw data, force new xTickLabelsHeatAntL before and after plotting
    xTickLabelsHeatAntL = []
    plotEzCon2dSamples(plotName, raw, 'Raw', rawLen-1, f'Raw:  Doppler MHz', 0)
    xTickLabelsHeatAntL = []



def plotEzCon002antRaw():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antMax                               # float array       creation
    global antLenM1                             # integer
    global freqCenter                           # float

    plotName = 'ezCon002antRaw.png'

    antMax = np.amax(ant, axis=0)               # creation

    plotCountdown -= 1

    #if 2 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 2:
    if 2 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, ant, 'Ant', antLenM1, f'AntRaw:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def plotEzCon007ant():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antLenM1                             # integer
    global freqCenter                           # float

    plotName = 'ezCon007ant.png'

    plotCountdown -= 1

    #if 7 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 7:
    if 7 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, ant, 'Ant', antLenM1, f'Ant:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def plotEzCon017antMax2d():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antLenM1                             # integer
    global freqCenter                           # float

    plotName = 'ezCon017antMax.png'

    plotCountdown -= 1

    #if 17 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 17:
    if 17 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, ant, 'Ant', antLenM1, f'AntMax:  Doppler MHz from {freqCenter:.3f} MHz', 1)



def plotEzCon022refRaw():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ref                                  # float 2d array
    #global refLenM1                             # integer
    global antLenM1                             # integer

    plotName = 'ezCon022refRaw.png'

    plotCountdown -= 1

    #if 22 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 22:
    if 22 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, ref, 'Ref', antLenM1, 'RefRaw:  Doppler MHz', 0)



def plotEzCon027ref():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ref                                  # float 2d array
    #global refLenM1                             # integer
    global antLenM1                             # integer

    plotName = 'ezCon027ref.png'

    plotCountdown -= 1

    #if 27 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 27:
    if 27 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, ref, 'Ref', antLenM1, 'Ref:  Doppler MHz', 0)



def plotEzCon037refMax2d():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ref                                  # float 2d array
    #global refLenM1                             # integer
    global antLenM1                             # integer

    plotName = 'ezCon037refMax.png'

    plotCountdown -= 1

    #if 37 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 37:
    if 37 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, ref, 'Ref', antLenM1, 'RefMax:  Doppler MHz', 1)



def plotEzCon047antB():

    # creates antB

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antBaseline                          # float array
    global antB                                 # float 2d array        creation
    global antLenM1                             # integer
    global freqCenter                           # float
    global ezConUseRefSub                       # integer

    plotName = 'ezCon047antB.png'

    if ezConUseRefSub:
        antB = ant - antBaseline                    # creation
    else:
        # before division, if any antBaseline is zero, then add tiny number to all antBaseline
        if not antBaseline.all():
            antBaseline += 1e-14
        antB = ant / antBaseline

    plotCountdown -= 1

    #if 47 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 47:
    if 47 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antBAvgMax = ', antB.max())
    print('                         antBAvgAvg =', np.mean(antB))
    print('                         antBAvgMin = ', antB.min())

    plotEzCon2dSamples(plotName, antB, 'Ant', antLenM1, f'AntB:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def plotEzCon057antBMax2d():
    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antB                                 # float 2d array
    global antLenM1                             # integer
    global freqCenter                           # float

    plotName = 'ezCon057antBMax.png'

    plotCountdown -= 1

    #if 57 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 57:
    if 57 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, antB, 'Ant', antLenM1, f'AntBMax:  Doppler MHz from {freqCenter:.3f} MHz', 1)



def plotEzCon061antRA():
    # creates antRA

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global ref                                  # float 2d array
    global antRA                                # float 2d array        creation
    global antLenM1                             # integer
    global freqCenter                           # float
    global ezConUseRefSub                       # integer

    plotName = 'ezCon061antRA.png'

    # create antRA
    if ezConUseRefSub:
        antRA = np.subtract(ant, ref)               # creation
    else:
        # before division, if any ref is zero, then add tiny number to all ref
        if not ref.all():
            ref += 1e-14
        antRA = np.true_divide(ant, ref)        # creation

    plotCountdown -= 1

    #if 61 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 61:
    if 61 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, antRA, 'Ant', antLenM1, f'AntRA:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def plotEzCon067antRB():
    # creates antRB

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antRA                                # float 2d array
    global antRABaseline                        # float array
    global antRB                                # float 2d array        creation
    global antLenM1                             # integer
    global freqCenter                           # float
    global ezConUseRefSub                       # integer

    plotName = 'ezCon067antRB.png'

    if ezConUseRefSub:
        antRB = antRA - antRABaseline           # creation
    else:
        antRB = antRA / antRABaseline           # creation

    plotCountdown -= 1

    #if 67 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 67:
    if 67 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, antRB, 'Ant', antLenM1, f'AntRB:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def plotEzCon077antRBMax2d():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antRB                                # float 2d array
    global antLenM1                             # integer
    global freqCenter                           # float

    plotName = 'ezCon077antRBMax.png'

    plotCountdown -= 1

    #if 77 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 77:
    if 77 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon2dSamples(plotName, antRB, 'Ant', antLenM1, f'AntRBMax:  Doppler MHz from {freqCenter:.3f} MHz', 1)



def plotEzCon081antXT():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antX                                 # float 2d array
    global antXNameL                            # list of strings
    global antXT                                # float 2d array        creation
    global antLen                               # integer
    global antLenM1                             # integer
    global freqCenter                           # float

    #plotName = 'ezCon081antXT.png'
    plotName = 'ezCon081' + antXNameL[0] + 'T.png'

    # Each antX[:, n] is a spectrum, normally from Doppler -1.2 to +1.2 MHz.
    # The low and high frequency extremes, they rise up, and they mislead.
    # Because interested in HI emision, antXT will use only the center of that antXThis spectrum,
    # maybe Doppler -0.6 to +0.6 MHz.
    # Create an antXT spectrum with extremes with values adjusted to 1. .
    # So do not use maybe 1.2 - 0.6 = 0.6 MHz of the outer extremes.
    # So do not use a fraction of the whole, suggest maybe 0.6 of 2.4 MHz, of the outer extremes.
 



    print('==AAA============== antX =', antX)
    print('==AAA============== np.max(antX) =', np.max(antX))
    print('==AAA============== np.min(antX) =', np.min(antX))





    #antXT = np.empty_like(antX)
    antXT = np.ones_like(antX)
 
    # For each individual antX spectrum, fill antXT inside the FOR loop below.
    #   Using an average slope from antXByFreqBinAvg, want to fill antXT
    #   with a corresponding slope-flatten center section of antX.
    #   The center section has antXSlopeQty indicies, starting at index ezConAntXFreqBin0 .
    print('                         ezConAntXTFreqBinsFracL =', ezConAntXTFreqBinsFracL)
    ezConAntXFreqBin0 = int(ezConAntXTFreqBinsFracL[0] * (fileFreqBinQty - 1))
    ezConAntXFreqBin1 = int(ezConAntXTFreqBinsFracL[1] * (fileFreqBinQty - 1))
    ezConAntXFreqBin1P1 = ezConAntXFreqBin1 + 1
    print('                         ezConAntXFreqBin0 =', ezConAntXFreqBin0)
    print('                         ezConAntXFreqBin1 =', ezConAntXFreqBin1)

    antXUsedMin = antX[ezConAntXFreqBin0:ezConAntXFreqBin1P1, :].min()
    print('                         antXUsedMin =', antXUsedMin)

    if antXUsedMin < 1.:
       antX -= antXUsedMin

    antXSlopeQty = ezConAntXFreqBin1P1 - ezConAntXFreqBin0
    antXRange = range(antXSlopeQty)
    antXTThis = np.ones(fileFreqBinQty)        # sets antXT extreme lows and highs to 1.0

    # create a level antX center sloped spectrum
    # set antXSlope from antXByFreqBinAvg
    antXByFreqBinAvg = np.mean(antX + 0., axis=1)
    print('==BBB1============== antXByFreqBinAvg =', antXByFreqBinAvg)
    print('==BBB1============== np.max(antXByFreqBinAvg) =', np.max(antXByFreqBinAvg))
    print('==BBB1============== np.min(antXByFreqBinAvg) =', np.min(antXByFreqBinAvg))
    antXSlopeValueStart = antXByFreqBinAvg[ezConAntXFreqBin0]
    print('==BBB1============== antXSlopeValueStart =', antXSlopeValueStart)
    antXSlopeValueStop  = antXByFreqBinAvg[ezConAntXFreqBin1]
    print('==BBB1============== antXSlopeValueStop =', antXSlopeValueStop)
    antXSlope = (antXSlopeValueStop - antXSlopeValueStart) / antXSlopeQty
    print('==BBB1============== antXSlope =', antXSlope)
    antXTThisDivisor = antXRange * antXSlope + antXSlopeValueStart
    print('==BBB1============== antXTThisDivisor =', antXTThisDivisor)
    # before division, if antXTThisDivisor is zero, then add tiny number to all antXTThisDivisor
    if not antXTThisDivisor.all():
        antXTThisDivisor += 1e-14
    print('==BBB1============== antXTThisDivisor =', antXTThisDivisor)


    print()
    print('==BBB2============== antXT =', antXT)
    print('==BBB2============== np.max(antXT) =', np.max(antXT))
    print('==BBB2============== np.min(antXT) =', np.min(antXT))

    for n in range(antLen):
        # want to slope-flatten the antX center section, which has antXSlopeQty indicies,
        #   inserting at index antXSlopeIndexStart
        antXTThis[ezConAntXFreqBin0:ezConAntXFreqBin1P1] \
            = antX[ezConAntXFreqBin0:ezConAntXFreqBin1P1, n] / antXTThisDivisor
        antXT[:, n] = antXTThis
        #print()
        #print('==BBB1============== antXT =', antXT)
        #print('==BBB1============== np.max(antXT) =', np.max(antXT))
        #print('==BBB1============== np.min(antXT) =', np.min(antXT))
        #print('====BBB2============== antXT =', antXT)
        #print('====BBB2============== np.max(antXT) =', np.max(antXT))
        #print('====BBB2============== np.min(antXT) =', np.min(antXT))

    print()
    print('==BBB3============== antXT =', antXT)
    print('==BBB3============== np.max(antXT) =', np.max(antXT))
    print('==BBB3============== np.min(antXT) =', np.min(antXT))



    # free antX memory
    antX = []
    antX = None
    del antX

    plotCountdown -= 1

    #if 81 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 81:
    if 81 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    #plotEzCon2dSamples(plotName, antXT, 'Ant', antLenM1, 'AntXT', 0)
    plotEzCon2dSamples(plotName, antXT, 'Ant', antLenM1, antXNameL[1]+f'T:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def createAntXTV():                             # creates antXTV and antXTVAvg

    global antXT                                # float 2d array
    global antXTV                               # float 2d array        creation
    global antLen                               # integer
    global freqCenter                           # float

    # create antXTV
    antXTV = np.empty_like(antXT)   # antXTV is like antXT but corrected by Vlsr

    # create array of ones to attach to low or high end of antXT spectrum as needed
    freqBinVlsrOnes = np.ones(int(fileFreqBinQty / 2))

    # speed of light = 299,792,458 meters per second
    # https://minerva.union.edu/marrj/radioastro/Instructions_MWrotationcurve.html
    # (fem - fobs) / fobs = Vrec / c
    # fem is the frequency that the radiation was emitted at, which is 1420.4 MHz, and fobs is the frequency that you observed [min freq value of possible H]
    # This velocity is, now, the Vmax along that line of sight,
    # -OK, but why the "/ fobs" here, vs the "/ fRest" below ?
    # ezCon chooses the astropy formula below

    # https://docs.astropy.org/en/stable/api/astropy.units.equivalencies.doppler_radio.html
    # V = c * (fRest - f) / fRest
    #                     V          = c * (fRest - f        ) / fRest
    #                     V / c      =     (fRest - f        ) / fRest
    #                     V / c      =     (1     - f / fRest) / 1
    #                     V / c      =      1     - f / fRest
    #                     V / c  - 1 =            - f / fRest
    #                 1 - V / c      =              f / fRest
    #        fRest * (1 - V / c)     =              f
    # f    = fRest * (1 - V / c)
    # f(V) = fRest * (1 - V / c)
    # f(VLSR) = fRest * (1 - VLSR / 299,792.458 km per second)
    # f(VLSR) = fRest * (1     -           VLSR          / 299,792.458 km per second)
    # f(VLSR) =          fRest - fRest *   VLSR          / 299,792.458 km per second
    # f(VLSR) =          fRest -           VLSR *  fRest / 299,792.458 km per second
    # f(VLSR) =          fRest -           VLSR * (fRest / 299,792.458 km per second)
    # f(VLSR) =          fRest -           VLSR * freqCenterDivC
    # f(VLSR) =          fRest +         (-VLSR * freqCenterDivC)
    # f(VLSR) = fRest + (-VLSR * freqCenterDivC)
    # f(VLSR) = fRest + freqVlsrThis
    # below, ezCon shifts each fRest spectrum by (-VLSR * freqCenterDivC)
    # below, ezCon shifts each fRest spectrum by (freqVlsrThis)

    #freqVlsrThis = -vlsr km/s * 1420.406 MHz / (299,792,458. m/s / 1000.)       # in MHz
    #freqVlsrThis = -vlsr      * freqCenter   / (299,792,458.     / 1000.)       # in MHz
    #freqVlsrThis = -vlsr      * freqCenterDivC                                  # in MHz
    #freqVlsrThis = -vlsrThis  * freqCenterDivC
    freqCenterDivC = freqCenter / (299792458. / 1000.)

    for n in range(antLen):
        # create antXTVThis
        #freqVlsrThis = -vlsrThis  * freqCenterDivC
        freqVlsrThis = -ezConOut[n, 5] * freqCenterDivC
        if 0. <= freqVlsrThis:
            freqBinVlsrThis = int((freqVlsrThis / freqStep) + 0.5)      # round to closest number of freqBins
            if freqBinVlsrThis == 0:
                # shift antXT[:, n] spectrum by 0 freqBin
                antXTVThis = antXT[:, n] + 0.
            else:
                # shift antXT[:, n] spectrum by -freqBinVlsrThis freqBin
                antXTVThis = np.concatenate([ antXT[freqBinVlsrThis:, n], 
                    freqBinVlsrOnes[:freqBinVlsrThis] ])
        else:
            freqBinVlsrThis = int((freqVlsrThis / freqStep) - 0.5)      # round to closest number of freqBins
            if freqBinVlsrThis == 0:
                # shift antXT[:, n] spectrum by 0 freqBin
                antXTVThis = antXT[:, n] + 0.
            else:
                # shift antXT[:, n] spectrum by +freqBinVlsrThis freqBin
                antXTVThis = np.concatenate([ freqBinVlsrOnes[:-freqBinVlsrThis],
                    antXT[:freqBinVlsrThis, n] ])

        antXTV[:, n] = antXTVThis



def plotEzCon082antXTV():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXTV                               # float 2d array        creation
    global antLenM1                             # integer
    global freqCenter                           # float

    #plotName = 'ezCon082antXTV.png'
    plotName = 'ezCon082' + antXNameL[0] + 'TV.png'

    plotCountdown -= 1

    #if 82 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 82:
    if 82 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    #plotEzCon2dSamples(plotName, antXTV, 'Ant', antLenM1, 'AntXTV', 0)
    plotEzCon2dSamples(plotName, antXTV, 'Ant', antLenM1, antXNameL[1]+f'TV:  Doppler MHz from {freqCenter:.3f} MHz', 0)



def createAntXTVT():                            # creates antXTVT

    global antXTV                               # float 2d array
    global antXTVT                              # float 2d array        creation
    global antLen                               # integer

    # Each antXTV[:, n] is a spectrum, normally from Doppler -1.2 to +1.2 MHz.
    # The low and high frequency extremes, they rise up, and they mislead.
    # Because interested in HI emision, antXTVT will use only the center of that antXTVThis spectrum,
    # maybe Doppler -0.6 to +0.6 MHz.
    # Create an antXTVT spectrum with extremes with values adjusted to 1. .
    # So do not use 1.2 - 0.6 = 0.6 MHz of the outer extremes.
    # So do not use a fraction of the whole, suggest maybe 0.6 of 2.4 MHz, of the outer extremes.
 
    antXTVT = np.empty_like(antXTV)
 
    # For each individual antXTV spectrum, fill antXTVT inside the FOR loop below.
    #   Using an average slope from antXTVByFreqBinAvg, want to fill antXTVT
    #   with a corresponding slope-flatten center section of antXTV.
    #   The center section has antXTVSlopeQty indicies, starting at index ezConAntXTVFreqBin0 .
    print('                         ezConAntXTVTFreqBinsFracL =', ezConAntXTVTFreqBinsFracL)
    ezConAntXTVFreqBin0 = int(ezConAntXTVTFreqBinsFracL[0] * (fileFreqBinQty - 1))
    ezConAntXTVFreqBin1 = int(ezConAntXTVTFreqBinsFracL[1] * (fileFreqBinQty - 1))
    ezConAntXTVFreqBin1P1 = ezConAntXTVFreqBin1 + 1
    print('                         ezConAntXTVFreqBin0 =', ezConAntXTVFreqBin0)
    print('                         ezConAntXTVFreqBin1 =', ezConAntXTVFreqBin1)

    antXTVSlopeQty = ezConAntXTVFreqBin1P1 - ezConAntXTVFreqBin0
    antXTVRange = range(antXTVSlopeQty)
    antXTVTThis = np.ones(fileFreqBinQty)        # sets antXTVT extreme lows and highs to 1.0

    # create a level antXTV center sloped spectrum
    # set antXTVSlope from antXTVByFreqBinAvg
    antXTVByFreqBinAvg = np.mean(antXTV, axis=1)
    antXTVSlopeValueStart = antXTVByFreqBinAvg[ezConAntXTVFreqBin0]
    antXTVSlopeValueStop  = antXTVByFreqBinAvg[ezConAntXTVFreqBin1]
    antXTVSlope = (antXTVSlopeValueStop - antXTVSlopeValueStart) / antXTVSlopeQty
    antXTVTThisDivisor = antXTVRange * antXTVSlope + antXTVSlopeValueStart
    # before division, if antXTVTThisDivisor is zero, then add tiny number to all antXTVTThisDivisor
    if not antXTVTThisDivisor.all():
        antXTVTThisDivisor += 1e-14

    for n in range(antLen):
        ## level antXTV center sloped spectrum
        # want to slope-flatten the antXTV center section, which has antXTVSlopeQty indicies,
        #   inserting at index antXTVSlopeIndexStart
        antXTVTThis[ezConAntXTVFreqBin0:ezConAntXTVFreqBin1P1] \
            = antXTV[ezConAntXTVFreqBin0:ezConAntXTVFreqBin1P1, n] / antXTVTThisDivisor
        antXTVT[:, n] = antXTVTThis



def plotEzCon087antXTVT():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXTVT                              # float 2d array        creation
    global antLenM1                             # integer
    global freqCenter                           # float
    global fileFreqBinQty                       # integer
    global ezCon087Csv                          # integer
    global dopplerSpanD2                        # float
    global fileFreqMin                          # float
    global fileFreqMax                          # float
    global titleS                               # string

    #plotName = 'ezCon087antXTVT.png'
    plotName = 'ezCon087' + antXNameL[0] + 'TVT.png'

    plotCountdown -= 1

    #if 87 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 87:
    if 87 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    #plotEzCon2dSamples(plotName, antXTVT, 'Ant', antLenM1, 'AntXTVT', 0)
    plotEzCon2dSamples(plotName, antXTVT, 'Ant', antLenM1, antXNameL[1]+f'TVT:  Doppler MHz from {freqCenter:.3f} MHz', 0)

    if ezCon087Csv:

        # create independent antXTVTCsv to allow downsampling for smaller CSV files
        antXTVTCsv = antXTVT + 0.

        if 0:
            # create antXTVTCsv to allow small study data
            antXTVTCsv = np.array([
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 10, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 3, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] ])
            print(' ================== antXTVTCsv =', antXTVT)
            print(' ================== antXTVTCsv.shape =', antXTVT.shape)

        if 0:
            # downsample antXTVTCsv ?
            antXTVTCsvLenMax = 500      #######################################################
            if antXTVTCsvLenMax < antLen:
                # downsample antXTVTCsv by averaging groupLen samples together
                #   1999 // 500 = 3, so want groupLen as 4
                #   2000 // 500 = 4, so want groupLen as 5
                #   2001 // 500 = 4, so want groupLen as 5
                groupLen = antLen // antXTVTCsvLenMax + 1
                print(' ================== groupLen =', groupLen)
                antXTVTCsvIdx = 0
                for n in range(0, antLen, groupLen):
                    # downsample antXTVTCsv group by averaging groupLen samples together
                    antXTVTCsv[:,antXTVTCsvIdx] = np.mean(antXTVTCsv[:,n:n+groupLen], axis=1)
                    antXTVTCsvIdx += 1
                # downsample antXTVTCsv remaining group by averaging the samples together
                antXTVTCsv[:,antXTVTCsvIdx] = np.mean(antXTVTCsv[:,n:], axis=1)
                antXTVTCsv = antXTVTCsv[:,:antXTVTCsvIdx+1]     # trim off excess samples

        _, antXTVTCsvLen = antXTVTCsv.shape   # number of samples
        print(' ================== antXTVTCsvLen =', antXTVTCsvLen)
        
            
            
            
            

        if 0:
            # write 3 column CSV with file name like ezCon087antRBTVT.csv
            plotNameCsv = plotName[:-3] + 'csv'
            row_indices, col_indices = np.indices(np.transpose(antXTVTCsv).shape)
            #antXTVTCsv = np.column_stack((row_indices.ravel(), col_indices.ravel(), np.transpose(antXTVT).ravel()))
            fileFreqBinQtyD2 = fileFreqBinQty / 2.
            antXTVTCsv = np.column_stack(( \
                row_indices.ravel(),
                (col_indices.ravel()-fileFreqBinQtyD2) * dopplerSpanD2 / fileFreqBinQtyD2,
                np.transpose(antXTVTCsv).ravel() ))
            np.savetxt(plotNameCsv, antXTVTCsv, delimiter=",")

            # free antXTVTCsv memory
            antXTVTCsv = []
            antXTVTCsv = None
            del antXTVTCsv

            # free col_indices memory
            col_indices = []
            col_indices = None
            del col_indices




        # write mesh CSV with file name like ezCon087antRBTVTMsh.csv
        plotNameCsv = plotName[:-4] + 'Msh.csv'
        print(' ================== writing    ', plotNameCsv)
        fileWrite = open(plotNameCsv, 'w')

        #row_indices, _ = np.indices(np.transpose(antXTVTCsv).shape)
        row_indices, _ = np.indices(antXTVTCsv.shape)
        print(' ================== row_indices.shape =', row_indices.shape)
        # row_indices.shape = (908, 256)

        # write top line of sample number coordinates (X)
        fileOutS = ',' + np.array2string(row_indices[:,0], separator=',',max_line_width=1e9)[1:-1].replace(' ', '')
        #print(' ================== fileOutS =', fileOutS, '=')
        fileWrite.write(fileOutS + '\n')

        # free row_indices memory
        row_indices = []
        row_indices = None
        del row_indices

        #print(' ================== col_indices.shape =', col_indices.shape)
        # col_indices.shape = (908, 256)
        #print(' ================== col_indices[:,0] =', col_indices[:,0])
        #print(' ================== col_indices[0,:] =', col_indices[0,:])

        #freqBin = 0
        #for n in range(antLen):
        #for freqBin in range(4):
        print(' ================== fileFreqBinQty =', fileFreqBinQty)
        # write each line of freqBin coordinate (Y) and all values for each freqBin
        #for freqBin in range(fileFreqBinQty):
        _, xLen = antXTVTCsv.shape
        for n in range(xLen):
            #fileOutS = str(col_indices[n,0]) + ',' + np.array2string(antXTVTCsv[:,n], separator=',',max_line_width=1e9)[1:-1].replace(' ', '')
            fileOutS = str(n) + '.,' + np.array2string(antXTVTCsv[:,n],separator=',',max_line_width=1e9)[1:-1].replace(' ', '')
            #print(' ================== fileOutS =', fileOutS, '=')
            fileWrite.write(fileOutS + '\n')
        fileWrite.write('\n')
        fileWrite.close()

        # free fileOutS memory
        fileOutS = []
        fileOutS = None
        del fileOutS

        if 1 < ezCon087Csv:
            # for each sample, write one file into the output directory, each with fileFreqBinQty+2 lines
            fileOutFreqs = np.linspace(fileFreqMin, fileFreqMax, num=fileFreqBinQty, endpoint=True)
            az_el_S = f'{int(ezConOut[0, 7] * 10.):04d}_{int(ezConOut[0, 8] * 10.):04d}_'

            # create antXTVTCsv
            antXTVTCsv = antXTVT + 0.

            #if 1:
            if 2 < ezCon087Csv:
                # downsample antXTVTCsv ?
                antXTVTCsvLenMax = 500
                if antXTVTCsvLenMax < antLen:
                    # downsample antXTVTCsv by averaging groupLen samples together
                    #   1999 // 500 = 3, so want groupLen as 4
                    #   2000 // 500 = 4, so want groupLen as 5
                    #   2001 // 500 = 4, so want groupLen as 5
                    groupLen = antLen // antXTVTCsvLenMax + 1
                    print(' ================== groupLen =', groupLen)
                    antXTVTCsvIdx = 0
                    for n in range(0, antLen, groupLen):
                        # downsample antXTVTCsv group by averaging groupLen samples together
                        antXTVTCsv[:,antXTVTCsvIdx] = np.mean(antXTVTCsv[:,n:n+groupLen], axis=1)
                        antXTVTCsvIdx += 1
                    # downsample antXTVTCsv remaining group by averaging the samples together
                    antXTVTCsv[:,antXTVTCsvIdx] = np.mean(antXTVTCsv[:,n:], axis=1)
                    antXTVTCsv = antXTVTCsv[:,:antXTVTCsvIdx+1]     # trim off excess samples

            _, antXTVTCsvLen = antXTVTCsv.shape   # number of samples
            print(' ================== antXTVTCsvLen =', antXTVTCsvLen)
            for n in range(antXTVTCsvLen):
                #dataTimeUtcStrThis = ezConOut[n, 0].iso
                dataTimeUtcStrThis = Time(ezConOut[n, 0], format='mjd', scale='utc').iso
                #print(' ================== dataTimeUtcStrThis =', dataTimeUtcStrThis)
                # '2023-02-09 00:01:20.000'
                # '01234567890123456789
                yymmdd_ = dataTimeUtcStrThis[2:4] + dataTimeUtcStrThis[5:7] + dataTimeUtcStrThis[8:10] + '_'
                hhmmss  = dataTimeUtcStrThis[11:13] + dataTimeUtcStrThis[14:16] + dataTimeUtcStrThis[17:19]

                if not n:
                    # use filenameOutBase from first sample to create output directory name
                    filenameOutBase = az_el_S + yymmdd_
                    # use yymmdd_hhmmss from first sample to create output directory name,
                    #   Aaaa_Eeee_YYMMDD_HHMMSS
                    #dirOut = filenameOutBase + hhmmss
                    dirOut = titleS.split()[0][:-4]
                    # if does not exist - create new dirOut directory
                    print('\n   dirOut =', dirOut)
                    if not os.path.exists(dirOut):
                        os.makedirs(dirOut)
                        print('   Created new   ', dirOut, '   output directory')
                    print()

                # for each sample, write one file into the output directory, each with fileFreqBinQty+2 lines
                #   Aaaa_Eeee_YYMMDD_HHMMSS/Aaaa_Eeee_YYMMDD_Nnnn.txt
                # output all freqBin of current sample
                fileWriteName = dirOut + os.path.sep + filenameOutBase + f'{n:04d}.txt'
                print(' ================== writing    ', plotNameCsv)
                fileWrite = open(fileWriteName, 'w')

                # The "IF Average Plugin" .txt output radio spectrum data file looks like,
                #   4/28/2021 6:43:57 AM  Counts:451000
                #   1419.205000000  0.322551440
                #   1419.207343750  0.320824318
                #   1419.209687500  0.318060119
                #   ...
                ######## 123456789    123456789

                # assemble and write out fileOutLineTop first line
                #   5/3/2020 0:00:05 AM  Counts:451000
                # yymmdd_       hhmmss
                # 01234567      0123456
                fileOutLineTop = f'{int(yymmdd_[2:4]):d}/{int(yymmdd_[4:6]):d}/{dataTimeUtcStrThis[0:4]}' \
                    + f' {int(hhmmss[0:2]):d}:{hhmmss[2:4]}:{hhmmss[4:6]}'
                if int(hhmmss[0:2]) <= 12:
                    fileOutLineTop += ' AM  Counts:451000\n'
                else:
                    fileOutLineTop += ' PM  Counts:451000\n'
                fileWrite.write(fileOutLineTop)

                # output all freqBin of current sample
                for freqBin in range(fileFreqBinQty):
                    #fileWrite.write(f'{fileOutFreqs[freqBin]:0.9f}  {float(fileOutPowersS[freqBin])/1e7:0.9f}\n')
                    fileWrite.write(f'{fileOutFreqs[freqBin]:0.9f}  {antXTVTCsv[freqBin, n]/1e7:0.9f}\n')
                fileWrite.write('\n')
                fileWrite.close()



def plotEzCon088antBTVTByFreqBinAvgFall():

    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTVT                  # float 2d array

    global byFreqBinX               # float array
    global ezConDispGrid            # integer
    global dopplerSpanD2            # float

    #plotName = 'ezCon088antBTVTByFreqAvgFall.png'
    plotName = 'ezCon088' + antXNameL[0] + 'TVTByFreqAvgFall.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 88 and 88 <= ezConPlotRangeL[1]:
    if 88 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    #antXTVTDLen = 100                           # maximum quantity of spectra after downsampling
    antXTVTDLenMax = 100                        # maximum quantity of spectra after downsampling
    antXTVTDLen = min(antLen, antXTVTDLenMax)   # quantity of spectra after downsampling
    colorPenSL = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey']

    # true downsampling, using the slicing notation of start:stop:step ("Decimation" ?)
    #antXTVTD = antXTVT[:, ::downsamplingStep]

    # downsampling by averaging
    # (// is floor division)
    downsamplingStep = antLen // antXTVTDLen

    antXTVTD = np.empty_like(antXTVT[:, :antXTVTDLen])
    for n in range(antXTVTDLen):
        downsamplingIndex = n * downsamplingStep
        antXTVTD[:, n] = np.mean(antXTVT[:, downsamplingIndex:downsamplingIndex+downsamplingStep], axis=1)

    for n in range(len(antXTVTD[0, :])):
        plt.plot(byFreqBinX, [y - n * 0.01 for y in antXTVTD[:, n]], colorPenSL[n % 9], linewidth=0.5)

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel('Doppler (MHz)')
    plt.xlim(-dopplerSpanD2, dopplerSpanD2)

    #get current axes
    ax = plt.gca()
    # set the ticks to an empty list:
    ax.get_yaxis().set_ticks([])
    # hide just the axis text keeping the grid lines:
    ax.yaxis.set_ticklabels([])

    #plt.ylabel(antXNameL[1]+'TVT Spectra (time increasing up)')
    plt.ylabel(antXNameL[1]+'TVT Spectra, Downsampled by Averaging\nTime Increasing Down, downsamplingStep=' + str(downsamplingStep))

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon097antXTVTMax2d():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXTVT                              # float 2d array
    global antLenM1                             # integer
    global freqCenter                           # float

    #plotName = 'ezCon097antXTVTMax.png'
    plotName = 'ezCon097' + antXNameL[0] + 'TVTMax.png'

    plotCountdown -= 1

    #if 97 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 97:
    if 97 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    #plotEzCon2dSamples(plotName, antXTVT, 'Ant', antLenM1, 'AntXTVTMax', 1)
    plotEzCon2dSamples(plotName, antXTVT, 'Ant', antLenM1, antXNameL[1]+f'TVTMax:  Doppler MHz from {freqCenter:.3f} MHz', 1)



def plotEzCon098antBTVTByFreqBinMaxFall():

    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTVT                  # float 2d array

    global byFreqBinX               # float array
    global ezConDispGrid            # integer
    global dopplerSpanD2            # float

    #plotName = 'ezCon098antBTVTByFreqMaxFall.png'
    plotName = 'ezCon098' + antXNameL[0] + 'TVTByFreqMaxFall.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 98 and 98 <= ezConPlotRangeL[1]:
    if 98 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    #antXTVTMaxDLen = 100                                # quantity of spectra after downsampling
    antXTVTMaxDLenMax = 100                             # maximum quantity of spectra after downsampling
    antXTVTMaxDLen = min(antLen, antXTVTMaxDLenMax)     # quantity of spectra after downsampling

    colorPenSL = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey']

    # true downsampling, using the slicing notation of start:stop:step ("Decimation" ?)
    #antXTVTD = antXTVT[:, ::downsamplingStep]

    # downsampling by maximizing
    # (// is floor division)
    downsamplingStep = antLen // antXTVTMaxDLen

    antXTVTMaxD = np.empty_like(antXTVT[:, :antXTVTMaxDLen])
    for n in range(antXTVTMaxDLen):
        downsamplingIndex = n * downsamplingStep
        antXTVTMaxD[:, n] = np.amax(antXTVT[:, downsamplingIndex:downsamplingIndex+downsamplingStep], axis=1)

    for n in range(len(antXTVTMaxD[0, :])):
        plt.plot(byFreqBinX, [y - n * 0.01 for y in antXTVTMaxD[:, n]], colorPenSL[n % 9], linewidth=0.5)

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel('Doppler (MHz)')
    plt.xlim(-dopplerSpanD2, dopplerSpanD2)

    #get current axes
    ax = plt.gca()
    # set the ticks to an empty list:
    ax.get_yaxis().set_ticks([])
    # hide just the axis text keeping the grid lines:
    ax.yaxis.set_ticklabels([])

    #plt.ylabel(antXNameL[1]+'TVTMax Spectra (time increasing up)')
    plt.ylabel(antXNameL[1]+'TVTMax Spectra, Downsampled by Maximizing\nTime Increasing Down, downsamplingStep=' + str(downsamplingStep))

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



# one plot for each ezConOut column #########################################################

def plotEzCon100timeUtcMjd():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array
    global antLen                               # integer

    plotName = 'ezCon100timeUtcMjd.png'

    plotCountdown -= 1

    #if 100 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 100:
    if 100 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    timeUtcMjdMax = ezConOut[:, 0].max()
    timeUtcMjdMin = ezConOut[:, 0].min()
    print('                         timeUtcMjdMax =', timeUtcMjdMax)
    print('                         timeUtcMjdAvg =', ezConOut[:, 0].sum() / antLen)
    print('                         timeUtcMjdMin =', timeUtcMjdMin)
    timeUtcMjdMaxS = Time(timeUtcMjdMax, format='mjd', scale='utc').iso
    #'2021-09-19 04:58:48.000'
    # 012345678901234567890123
    timeUtcMjdMaxS = timeUtcMjdMaxS[:10] + '   ' + timeUtcMjdMaxS[11:]
    timeUtcMjdMinS = Time(timeUtcMjdMin, format='mjd', scale='utc').iso
    timeUtcMjdMinS = timeUtcMjdMinS[:10] + '   ' + timeUtcMjdMinS[11:]

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 0] - int(ezConOut[0, 0]), [], 'green',
        'Relative UTC Time in Modified Julian Day' \
            + '\n\nMinimum = ' + timeUtcMjdMinS \
            + '\n\nMaximum = ' + timeUtcMjdMaxS)



def plotEzCon101raH():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon101raH.png'

    plotCountdown -= 1

    #if 101 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 101:
    if 101 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         raHMax =', ezConOut[:, 1].max())
    print('                         raHAvg =', np.mean(ezConOut[:, 1]))
    print('                         raHMin =', ezConOut[:, 1].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 1], [0., 24.], 'green',
        'Right Ascension (hours)')



def plotEzCon102decDeg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon102decDeg.png'

    plotCountdown -= 1

    #if 102 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 102:
    if 102 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         decDegMax =', ezConOut[:, 2].max())
    print('                         decDegAvg =', np.mean(ezConOut[:, 2]))
    print('                         decDegMin =', ezConOut[:, 2].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 2], [-90., 90.], 'green',
        'Declination (degrees)')



def plotEzCon103gLatDeg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon103gLatDeg.png'

    plotCountdown -= 1

    #if 103 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 103:
    if 103 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLatDegMax =', ezConOut[:, 3].max())
    print('                         gLatDegAvg =', np.mean(ezConOut[:, 3]))
    print('                         gLatDegMin =', ezConOut[:, 3].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 3], [-90., 90.], 'green',
        'Galactic Latitude (degrees)')



def plotEzCon104gLonDeg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon104gLonDeg.png'

    plotCountdown -= 1

    #if 104 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 104:
    if 104 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         gLonDegMax =', ezConOut[:, 4].max())
    print('                         gLonDegAvg =', np.mean(ezConOut[:, 4]))
    print('                         gLonDegMin =', ezConOut[:, 4].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 4], [-180., 180.], 'green',
        'Galactic Longitude (degrees)')



def plotEzCon105vlsr():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon105vlsr.png'

    plotCountdown -= 1

    #if 105 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 105:
    if 105 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         vlsrMax =', ezConOut[:, 5].max())
    print('                         vlsrAvg =', np.mean(ezConOut[:, 5]))
    print('                         vlsrMin =', ezConOut[:, 5].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 5], [], 'green',
        'receding Velocity of Local Standard of Rest (VLSR) (km/s)')



def plotEzCon106count():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon106count.png'

    plotCountdown -= 1

    #if 106 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 106:
    if 106 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 6], [], 'green',
        'Count')



def plotEzCon110antAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon110antAvg.png'

    plotCountdown -= 1

    #if 110 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 110:
    if 110 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antAvgMax =', ezConOut[:, 10].max())
    print('                         antAvgAvg =', np.mean(ezConOut[:, 10]))
    print('                         antAvgMin =', ezConOut[:, 10].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 10], [], 'blue',
        'Ant Antenna Spectrum Average')



def plotEzCon112refAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon112refAvg.png'

    plotCountdown -= 1

    #if 112 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 112:
    if 112 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         refAvgMax =', ezConOut[:, 12].max())
    print('                         refAvgAvg =', np.mean(ezConOut[:, 12]))
    print('                         refAvgMin =', ezConOut[:, 12].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 12], [], 'violet',
        'Reference Spectrum Average')



def plotEzCon114antBAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon114antBAvg.png'

    plotCountdown -= 1

    #if 114 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 114:
    if 114 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antBAvgMax =', ezConOut[:, 14].max())
    print('                         antBAvgAvg =', np.mean(ezConOut[:, 14]))
    print('                         antBAvgMin =', ezConOut[:, 14].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 14], [], 'red',
        'AntB Spectrum Average')



def plotEzCon116antRBAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon116antRBAvg.png'

    plotCountdown -= 1

    #if 116 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 116:
    if 116 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antRBAvgMax =', ezConOut[:, 16].max())
    print('                         antRBAvgAvg =', np.mean(ezConOut[:, 16]))
    print('                         antRBAvgMin =', ezConOut[:, 16].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 16], [], 'orange',
        'AntRB Spectrum Average')



def plotEzCon118antXTVTAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    #plotName = 'ezCon118antXTVTAvg.png'
    plotName = 'ezCon118' + antXNameL[0] + 'TVTAvg.png'

    plotCountdown -= 1

    #if 118 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 118:
    if 118 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antXTVTAvgMax =', ezConOut[:, 18].max())
    print('                         antXTVTAvgAvg =', np.mean(ezConOut[:, 18]))
    print('                         antXTVTAvgMin =', ezConOut[:, 18].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 18], [], 'green',
        antXNameL[1]+'TVT Spectrum Average')



def plotEzCon111antMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon111antMax.png'

    plotCountdown -= 1

    #if 111 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 111:
    if 111 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antMaxMax =', ezConOut[:, 11].max())
    print('                         antMaxAvg =', np.mean(ezConOut[:, 11]))
    print('                         antMaxMin =', ezConOut[:, 11].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 11], [], 'blue',
        'Ant Antenna Spectrum Maximum')



def plotEzCon113refMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon113refMax.png'

    plotCountdown -= 1

    #if 113 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 113:
    if 113 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         refMaxMax =', ezConOut[:, 13].max())
    print('                         refMaxAvg =', np.mean(ezConOut[:, 13]))
    print('                         refMaxMin =', ezConOut[:, 13].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 13], [], 'violet',
        'Reference Spectrum Maximum')



def plotEzCon115antBMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon115antBMax.png'

    plotCountdown -= 1

    #if 115 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 115:
    if 115 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antBMaxMax =', ezConOut[:, 15].max())
    print('                         antBMaxAvg =', np.mean(ezConOut[:, 15]))
    print('                         antBMaxMin =', ezConOut[:, 15].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 15], [], 'red',
        'AntB Spectrum Maximum')



def plotEzCon117antRBMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon117antRBMax.png'

    plotCountdown -= 1

    #if 117 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 117:
    if 117 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antBRMaxMax =', ezConOut[:, 17].max())
    print('                         antBRMaxAvg =', np.mean(ezConOut[:, 17]))
    print('                         antBRMaxMin =', ezConOut[:, 17].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 17], [], 'orange',
        'AntRB Spectrum Maximum')



def plotEzCon119antXTVTMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    #plotName = 'ezCon119antXTVTMax.png'
    plotName = 'ezCon119' + antXNameL[0] + 'TVTMax.png'

    plotCountdown -= 1

    #if 119 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 119:
    if 119 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antXTVTMaxMax =', ezConOut[:, 19].max())
    print('                         antXTVTMaxAvg =', np.mean(ezConOut[:, 19]))
    print('                         antXTVTMaxMin =', ezConOut[:, 19].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 19], [], 'green',
        antXNameL[1]+'TVT Spectrum Maximum')



def plotEzCon191sigProg():
    # deletes antRawAvg, antBaseline, refRawAvg, antRAAvg, antRABaseline, antXTVAvg

    global fileNameLast             # string
    global plotCountdown            # integer
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global ezConPlotRequestedL      # integer list
    global titleS                   # string
    global ezConDispGrid            # integer

    global xLabelSAnt               # string
    global xTickLocsAnt
    global xTickLabelsAnt

    global antLenM1                 # integer

    global ezConOut                 # float and int 2d array
    global antRawAvg                # float array
    global antBaseline              # float array
    global refRawAvg                # float array
    global antRAAvg                 # float array
    global antRABaseline            # float array
    global antXTVAvg                # float array       creation
    global antXNameL                # list of strings

    plotName = 'ezCon191sigProg.png'     # Signal Computation Progression

    plotCountdown -= 1

    #if 191 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 191:
    if 191 not in ezConPlotRequestedL:

        # free antRawAvg memory
        antRawAvg = []
        antRawAvg = None
        del antRawAvg
        # free antBaseline memory
        antBaseline = []
        antBaseline = None
        del antBaseline
        # free refRawAvg memory
        refRawAvg = []
        refRawAvg = None
        del refRawAvg
        # free antRAAvg memory
        antRAAvg = []
        antRAAvg = None
        del antRAAvg
        # free antRABaseline memory
        antRABaseline = []
        antRABaseline = None
        del antRABaseline
        # free antXTVAvg memory
        antXTVAvg = []
        antXTVAvg = None
        del antXTVAvg
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()


    # using gLatDeg, calculate a gain to fit it within -100 to +100 of its average
    print()
    gLatDegMax = ezConOut[:, 3].max()
    print('                         gLatDegMax =', gLatDegMax)
    gLatDegAvg = np.mean(ezConOut[:, 3])
    print('                         gLatDegAvg =', gLatDegAvg)
    gLatDegAvg = 0.                                                 # center trace on zero
    gLatDegMin = ezConOut[:, 3].min()
    print('                         gLatDegMin =', gLatDegMin)
    if gLatDegMax == gLatDegMin:            # gLatDeg will not vary when ezConAstroMath == 0
        gLatDegGain = 0.
    elif gLatDegAvg - gLatDegMin < gLatDegMax - gLatDegAvg:
        gLatDegGain = 93. / (gLatDegMax  - gLatDegAvg)
    else:
        gLatDegGain = 93. / (gLatDegAvg - gLatDegMin)

    gLatDegY = gLatDegGain * (ezConOut[:, 3] - gLatDegAvg)

    # thin black horizontal line on center
    plt.axhline(y = 0., linewidth=0.5, color='black')

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
            plt.axvline(x = x, linewidth=0.5, color='black')
            
    #plt.plot(gLatDegY, c='blue')
    plt.plot(gLatDegY, c='red')


    # If Ant samples are pluck filtered (ignored), this unplucked antRawAvg will no longer align vertically on this plot.
    # No good solution, because comparing antRawLen samples to a now shorter antLen.
    # But usually hard to see, because only plucking a few samples compared to a large number of antLen.

    # using antRawAvg, calculate a gain to fit it within -100 to +100 of its average
    antRawAvgMax = antRawAvg.max()
    print('                         antRawAvgMax =', antRawAvgMax)
    antRawAvgAvg = np.mean(antRawAvg)
    print('                         antRawAvgAvg =', antRawAvgAvg)
    antRawAvgMin = antRawAvg.min()
    print('                         antRawAvgMin =', antRawAvgMin)
    if antRawAvgMax == antRawAvgMin:        # antRawAvg may not vary
        antRawAvgGain = 0.
    elif antRawAvgAvg - antRawAvgMin < antRawAvgMax - antRawAvgAvg:
        antRawAvgGain = 93. / (antRawAvgMax  - antRawAvgAvg)
    else:
        antRawAvgGain = 93. / (antRawAvgAvg - antRawAvgMin)
    #plt.plot(antRawAvgGain * (antRawAvg - antRawAvgAvg) + 3200., c='blue')
    plt.plot(antRawAvgGain * (antRawAvg - antRawAvgAvg) + 200., c='blue')
    # free antRawAvg memory
    antRawAvg = []
    antRawAvg = None
    del antRawAvg


    # using antAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antAvgMax = ezConOut[:, 10].max()
    print('                         antAvgMax =', antAvgMax)
    antAvgAvg = np.mean(ezConOut[:, 10])
    print('                         antAvgAvg =', antAvgAvg)
    antAvgMin = ezConOut[:, 10].min()
    print('                         antAvgMin =', antAvgMin)
    if antAvgMax == antAvgMin:              # antAvg may not vary
        antAvgGain = 0.
    elif antAvgAvg - antAvgMin < antAvgMax - antAvgAvg:
        antAvgGain = 93. / (antAvgMax  - antAvgAvg)
    else:
        antAvgGain = 93. / (antAvgAvg - antAvgMin)
    #plt.plot(antAvgGain * (ezConOut[:, 10] - antAvgAvg) + 3000., c='blue')
    plt.plot(antAvgGain * (ezConOut[:, 10] - antAvgAvg) + 400., c='blue')


    # using antMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antMaxMax = ezConOut[:, 11].max()
    print('                         antMaxMax =', antMaxMax)
    antMaxAvg = np.mean(ezConOut[:, 11])
    print('                         antMaxAvg =', antMaxAvg)
    antMaxMin = ezConOut[:, 11].min()
    print('                         antMaxMin =', antMaxMin)
    if antMaxMax == antMaxMin:              # antMax may not vary
        antMaxGain = 0.
    elif antMaxAvg - antMaxMin < antMaxMax - antMaxAvg:
        antMaxGain = 93. / (antMaxMax  - antMaxAvg)
    else:
        antMaxGain = 93. / (antMaxAvg - antMaxMin)
    #plt.plot(antMaxGain * (ezConOut[:, 11] - antMaxAvg) + 2800., c='blue')
    plt.plot(antMaxGain * (ezConOut[:, 11] - antMaxAvg) + 600., c='blue')


    # using antBaseline, calculate a gain to fit it within -100 to +100 of its average
    print()
    antBaselineMax = antBaseline.max()
    print('                         antBaselineMax =', antBaselineMax)
    antBaselineAvg = np.mean(antBaseline)
    print('                         antBaselineAvg =', antBaselineAvg)
    antBaselineMin = antBaseline.min()
    print('                         antBaselineMin =', antBaselineMin)
    if antBaselineMax == antBaselineMin:    # antBaseline may not vary
        antBaselineGain = 0.
    elif antBaselineAvg - antBaselineMin < antBaselineMax - antBaselineAvg:
        antBaselineGain = 93. / (antBaselineMax  - antBaselineAvg)
    else:
        antBaselineGain = 93. / (antBaselineAvg - antBaselineMin)
    #plt.plot(antBaselineGain * (antBaseline - antBaselineAvg) + 2600., c='red')
    plt.plot(antBaselineGain * (antBaseline - antBaselineAvg) + 800., c='red')
    # free antBaseline memory
    antBaseline = []
    antBaseline = None
    del antBaseline


    # using antBAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antBAvgMax = ezConOut[:, 14].max()
    print('                         antBAvgMax =', antBAvgMax)
    antBAvgAvg = np.mean(ezConOut[:, 14])
    print('                         antBAvgAvg =', antBAvgAvg)
    antBAvgMin = ezConOut[:, 14].min()
    print('                         antBAvgMin =', antBAvgMin)
    if antBAvgMax == antBAvgMin:            # antBAvg may not vary
        antBAvgGain = 0.
    elif antBAvgAvg - antBAvgMin < antBAvgMax - antBAvgAvg:
        antBAvgGain = 93. / (antBAvgMax  - antBAvgAvg)
    else:
        antBAvgGain = 93. / (antBAvgAvg - antBAvgMin)
    #plt.plot(antBAvgGain * (ezConOut[:, 14] - antBAvgAvg) + 2400., c='red')
    plt.plot(antBAvgGain * (ezConOut[:, 14] - antBAvgAvg) + 1000., c='red')


    # using antBMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antBMaxMax = ezConOut[:, 15].max()
    print('                         antBMaxMax =', antBMaxMax)
    antBMaxAvg = np.mean(ezConOut[:, 15])
    print('                         antBMaxAvg =', antBMaxAvg)
    antBMaxMin = ezConOut[:, 15].min()
    print('                         antBMaxMin =', antBMaxMin)
    if antBMaxMax == antBMaxMin:            # antBMax may not vary
        antBMaxGain = 0.
    elif antBMaxAvg - antBMaxMin < antBMaxMax - antBMaxAvg:
        antBMaxGain = 93. / (antBMaxMax  - antBMaxAvg)
    else:
        antBMaxGain = 93. / (antBMaxAvg - antBMaxMin)
    #plt.plot(antBMaxGain * (ezConOut[:, 15] - antBMaxAvg) + 2200., c='red')
    plt.plot(antBMaxGain * (ezConOut[:, 15] - antBMaxAvg) + 1200., c='red')


    # using refRawAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    refRawAvgMax = refRawAvg.max()
    print('                         refRawAvgMax =', refRawAvgMax)
    refRawAvgAvg = np.mean(refRawAvg)
    print('                         refRawAvgAvg =', refRawAvgAvg)
    refRawAvgMin = refRawAvg.min()
    print('                         refRawAvgMin =', refRawAvgMin)
    if refRawAvgMax == refRawAvgMin:        # refRawAvg may not vary
        refRawAvgGain = 0.
    elif refRawAvgAvg - refRawAvgMin < refRawAvgMax - refRawAvgAvg:
        refRawAvgGain = 93. / (refRawAvgMax  - refRawAvgAvg)
    else:
        refRawAvgGain = 93. / (refRawAvgAvg - refRawAvgMin)
    #plt.plot(refRawAvgGain * (refRawAvg - refRawAvgAvg) + 2000., c='violet')
    plt.plot(refRawAvgGain * (refRawAvg - refRawAvgAvg) + 1400., c='violet')
    # free refRawAvg memory
    refRawAvg = []
    refRawAvg = None
    del refRawAvg


    # using refAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    refAvgMax = ezConOut[:, 12].max()
    print('                         refAvgMax =', refAvgMax)
    refAvgAvg = np.mean(ezConOut[:, 12])
    print('                         refAvgAvg =', refAvgAvg)
    refAvgMin = ezConOut[:, 12].min()
    print('                         refAvgMin =', refAvgMin)
    if refAvgMax == refAvgMin:              # refAvg may not vary
        refAvgGain = 0.
    elif refAvgAvg - refAvgMin < refAvgMax - refAvgAvg:
        refAvgGain = 93. / (refAvgMax  - refAvgAvg)
    else:
        refAvgGain = 93. / (refAvgAvg - refAvgMin)
    #plt.plot(refAvgGain * (ezConOut[:, 12] - refAvgAvg) + 1800., c='violet')
    plt.plot(refAvgGain * (ezConOut[:, 12] - refAvgAvg) + 1600., c='violet')


    # using refMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    refMaxMax = ezConOut[:, 13].max()
    print('                         refMaxMax =', refMaxMax)
    refMaxAvg = np.mean(ezConOut[:, 13])
    print('                         refMaxAvg =', refMaxAvg)
    refMaxMin = ezConOut[:, 13].min()
    print('                         refMaxMin =', refMaxMin)
    if refMaxMax == refMaxMin:              # refMax may not vary
        refMaxGain = 0.
    elif refMaxAvg - refMaxMin < refMaxMax - refMaxAvg:
        refMaxGain = 93. / (refMaxMax  - refMaxAvg)
    else:
        refMaxGain = 93. / (refMaxAvg - refMaxMin)
    #plt.plot(refMaxGain * (ezConOut[:, 13] - refMaxAvg) + 1600., c='violet')
    plt.plot(refMaxGain * (ezConOut[:, 13] - refMaxAvg) + 1800., c='violet')


    # using antRAAvg, calculate a gain to fit it within -100 to +100 of its average
    antRAAvgMax = max(antRAAvg)
    print('                         antRAAvgMax =', antRAAvgMax)
    antRAAvgAvg = np.mean(antRAAvg)
    print('                         antRAAvgAvg =', antRAAvgAvg)
    antRAAvgMin = min(antRAAvg)
    print('                         antRAAvgMin =', antRAAvgMin)
    if antRAAvgMax == antRAAvgMin:          # antRAAvg may not vary
        antRAAvgGain = 0.
    elif antRAAvgAvg - antRAAvgMin < antRAAvgMax - antRAAvgAvg:
        antRAAvgGain = 93. / (antRAAvgMax  - antRAAvgAvg)
    else:
        antRAAvgGain = 93. / (antRAAvgAvg - antRAAvgMin)
    #plt.plot(antRAAvgGain * (antRAAvg - antRAAvgAvg) + 1400., c='orange')
    plt.plot(antRAAvgGain * (antRAAvg - antRAAvgAvg) + 2000., c='orange')
    # free antRAAvg memory
    antRAAvg = []
    antRAAvg = None
    del antRAAvg


    # using antRABaseline, calculate a gain to fit it within -100 to +100 of its average
    print()
    antRABaselineMax = antRABaseline.max()
    print('                         antRABaselineMax =', antRABaselineMax)
    antRABaselineAvg = np.mean(antRABaseline)
    print('                         antRABaselineAvg =', antRABaselineAvg)
    antRABaselineMin = antRABaseline.min()
    print('                         antRABaselineMin =', antRABaselineMin)
    if antRABaselineMax == antRABaselineMin:    # antRABaseline may not vary
        antRABaselineGain = 0.
    elif antRABaselineAvg - antRABaselineMin < antRABaselineMax - antRABaselineAvg:
        antRABaselineGain = 93. / (antRABaselineMax  - antRABaselineAvg)
    else:
        antRABaselineGain = 93. / (antRABaselineAvg - antRABaselineMin)
    #plt.plot(antRABaselineGain * (antRABaseline - antRABaselineAvg) + 1200., c='orange')
    plt.plot(antRABaselineGain * (antRABaseline - antRABaselineAvg) + 2200., c='orange')
    # free antRABaseline memory
    antRABaseline = []
    antRABaseline = None
    del antRABaseline


    # using antRBAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antRBAvgMax = ezConOut[:, 16].max()
    print('                         antRBAvgMax =', antRBAvgMax)
    antRBAvgAvg = np.mean(ezConOut[:, 16])
    print('                         antRBAvgAvg =', antRBAvgAvg)
    antRBAvgMin = ezConOut[:, 16].min()
    print('                         antRBAvgMin =', antRBAvgMin)
    if antRBAvgMax == antRBAvgMin:          # antRBAvg may not vary
        antRBAvgGain = 0.
    elif antRBAvgAvg - antRBAvgMin < antRBAvgMax - antRBAvgAvg:
        antRBAvgGain = 93. / (antRBAvgMax  - antRBAvgAvg)
    else:
        antRBAvgGain = 93. / (antRBAvgAvg - antRBAvgMin)
    #plt.plot(antRBAvgGain * (ezConOut[:, 16] - antRBAvgAvg) + 1000., c='orange')
    plt.plot(antRBAvgGain * (ezConOut[:, 16] - antRBAvgAvg) + 2400., c='orange')


    # using antRBMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antRBMaxMax = ezConOut[:, 17].max()
    print('                         antRBMaxMax =', antRBMaxMax)
    antRBMaxAvg = np.mean(ezConOut[:, 17])
    print('                         antRBMaxAvg =', antRBMaxAvg)
    antRBMaxMin = ezConOut[:, 17].min()
    print('                         antRBMaxMin =', antRBMaxMin)
    if antRBMaxMax == antRBMaxMin:          # antRBMax may not vary
        antRBMaxGain = 0.
    elif antRBMaxAvg - antRBMaxMin < antRBMaxMax - antRBMaxAvg:
        antRBMaxGain = 93. / (antRBMaxMax  - antRBMaxAvg)
    else:
        antRBMaxGain = 93. / (antRBMaxAvg - antRBMaxMin)
    #plt.plot(antRBMaxGain * (ezConOut[:, 17] - antRBMaxAvg) + 800., c='orange')
    plt.plot(antRBMaxGain * (ezConOut[:, 17] - antRBMaxAvg) + 2600., c='orange')


    # using antXTVAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antXTVAvgMax = antXTVAvg.max()
    print('                         antXTVAvgMax =', antXTVAvgMax)
    antXTVAvgAvg = np.mean(antXTVAvg)
    print('                         antXTVAvgAvg =', antXTVAvgAvg)
    antXTVAvgMin = antXTVAvg.min()
    print('                         antXTVAvgMin =', antXTVAvgMin)
    if antXTVAvgMax == antXTVAvgMin:        # antXTVAvg may not vary
        antXTVAvgGain = 0.
    elif antXTVAvgAvg - antXTVAvgMin < antXTVAvgMax - antXTVAvgAvg:
        antXTVAvgGain = 93. / (antXTVAvgMax  - antXTVAvgAvg)
    else:
        antXTVAvgGain = 93. / (antXTVAvgAvg - antXTVAvgMin)
    #plt.plot(antXTVAvgGain * (antXTVAvg - antXTVAvgAvg) + 600., c='green')
    plt.plot(antXTVAvgGain * (antXTVAvg - antXTVAvgAvg) + 2800., c='green')
    # free antXTVAvg memory
    antXTVAvg = []
    antXTVAvg = None
    del antXTVAvg


    # using antXTVTAvg, calculate a gain to fit it within -100 to +100 of its average
    print()
    antXTVTAvgMax = ezConOut[:, 18].max()
    print('                         antXTVTAvgMax =', antXTVTAvgMax)
    antXTVTAvgAvg = np.mean(ezConOut[:, 18])
    print('                         antXTVTAvgAvg =', antXTVTAvgAvg)
    antXTVTAvgMin = ezConOut[:, 18].min()
    print('                         antXTVTAvgMin =', antXTVTAvgMin)
    if antXTVTAvgMax == antXTVTAvgMin:      # antXTVTAvg may not vary
        antXTVTAvgGain = 0.
    elif antXTVTAvgAvg - antXTVTAvgMin < antXTVTAvgMax - antXTVTAvgAvg:
        antXTVTAvgGain = 93. / (antXTVTAvgMax  - antXTVTAvgAvg)
    else:
        antXTVTAvgGain = 93. / (antXTVTAvgAvg - antXTVTAvgMin)
    #plt.plot(antXTVTAvgGain * (ezConOut[:, 18] - antXTVTAvgAvg) + 400., c='green')
    plt.plot(antXTVTAvgGain * (ezConOut[:, 18] - antXTVTAvgAvg) + 3000., c='green')


    # using antXTVTMax, calculate a gain to fit it within -100 to +100 of its average
    print()
    antXTVTMaxMax = ezConOut[:, 19].max()
    print('                         antXTVTMaxMax =', antXTVTMaxMax)
    antXTVTMaxAvg = np.mean(ezConOut[:, 19])
    print('                         antXTVTMaxAvg =', antXTVTMaxAvg)
    antXTVTMaxMin = ezConOut[:, 19].min()
    print('                         antXTVTMaxMin =', antXTVTMaxMin)
    if antXTVTMaxMax == antXTVTMaxMin:      # antXTVTMax may not vary
        antXTVTMaxGain = 0.
    elif antXTVTMaxAvg - antXTVTMaxMin < antXTVTMaxMax - antXTVTMaxAvg:
        antXTVTMaxGain = 93. / (antXTVTMaxMax  - antXTVTMaxAvg)
    else:
        antXTVTMaxGain = 93. / (antXTVTMaxAvg - antXTVTMaxMin)
    #plt.plot(antXTVTMaxGain * (ezConOut[:, 19] - antXTVTMaxAvg) + 200., c='green')
    plt.plot(antXTVTMaxGain * (ezConOut[:, 19] - antXTVTMaxAvg) + 3200., c='green')


    plt.title(titleS)
    plt.grid(ezConDispGrid)

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
                if ezConRawDispIndex:
                    xTickLabelsAnt[i] = f'{rawIndex[xTickLocsAntIInt]:,}  {xTickLocsAntIInt:,}  ' \
                        + dataTimeUtc[xTickLocsAntIInt].iso[11:16]
                else:
                    xTickLabelsAnt[i] = f'{xTickLocsAntIInt:,}  ' \
                        + dataTimeUtc[xTickLocsAntIInt].iso[11:16]
            else:       # remove silly values
                xTickLocsAnt = np.delete(xTickLocsAnt, i)
                xTickLabelsAnt = np.delete(xTickLabelsAnt, i)
        # fill xTickLabelsAnt[-1], samplesQtyM1 is usually less than xTickLocsAnt[-1]
        xTickLocsAnt[-1] = antLenM1
        if 0.975 < xTickLocsAnt[-2] / antLenM1:   # if last label overlaps, blank it
            xTickLabelsAnt[-1] = ''
        elif ezConRawDispIndex:
            xTickLabelsAnt[-1] = f'{rawIndex[-1]:,}  {antLenM1:,}  ' \
                + dataTimeUtc[-1].iso[11:16]
        else:
            xTickLabelsAnt[-1] = f'{antLenM1:,}  ' + dataTimeUtc[-1].iso[11:16]
        if ezConRawDispIndex:
            xLabelSAnt = \
                f'Raw Sample Number + Ant Sample Number (last={antLenM1:,}) with UTC Hour:Min (last=' \
                + dataTimeUtc[-1].iso[11:16] + ')'
        else:
            xLabelSAnt = f'Ant Sample Number (last={antLenM1:,}) with UTC Hour:Min (last=' \
                + dataTimeUtc[-1].iso[11:16] + ')'
    plt.xticks(xTickLocsAnt, xTickLabelsAnt, rotation=45, ha='right', rotation_mode='anchor')
    plt.xlabel(xLabelSAnt)
    plt.xlim(0, antLenM1)

    plt.ylabel('Signal Computation Progression\nfrom AntRaw to '+antXNameL[1]+'TVTMax')
    plt.ylim(-150, 3350)
    #     3200.,     3000., 2800.,    2600.,    2400.,  2200.,     2000.,    1800., 1600.,
    #     1400.,   1200.,      1000.,   800.,       600.,     400.,      200.,         0.],
    plt.yticks([ \
        200.,      400.,  600.,     800.,     1000.,  1200.,     1400.,    1600., 1800.,
        2000.,   2200.,      2400.,   2600.,      2800.,             3000.,
        3200.,                 0.],
        ['AntRaw', 'Ant', 'AntMax', 'AntBas', 'AntB', 'AntBMax', 'RefRaw', 'Ref', 'RefMax',
        'AntRA', 'AntRABas', 'AntRB', 'AntRBMax', antXNameL[1]+'TV', antXNameL[1]+'TVT',
        antXNameL[1]+'TVTMax', 'GLat'])
    #    'AntRA', 'AntRABas', 'AntRB', 'AntRBMax', 'AntXTV', 'AntXTVT', 'AntXTVTMax', 'GLatDeg'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



#def plotEzCon198azimuth():
def plotEzCon107azimuth():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global azimuthDeg                           # float array

    plotName = 'ezCon107azimuth.png'

    plotCountdown -= 1

    #if 198 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 198:
    if 107 not in ezConPlotRequestedL:
        # free azimuthDeg memory
        azimuthDeg = []
        azimuthDeg = None
        del azimuthDeg
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         azimuthDegMax =', azimuthDeg.max())
    print('                         azimuthDegAvg =', np.mean(azimuthDeg))
    print('                         azimuthDegMin =', azimuthDeg.min())

    plotEzCon1dSamplesAnt(plotName, azimuthDeg, [], 'green',
        'Azimuth (Degrees)')

    # free azimuthDeg memory
    azimuthDeg = []
    azimuthDeg = None
    del azimuthDeg



#def plotEzCon199elevation():
def plotEzCon108elevation():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global elevationDeg                         # float array

    plotName = 'ezCon108elevation.png'

    plotCountdown -= 1

    #if 199 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 199:
    if 108 not in ezConPlotRequestedL:
        # free elevationDeg memory
        elevationDeg = []
        elevationDeg = None
        del elevationDeg
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         elevationDegMax =', elevationDeg.max())
    print('                         elevationDegAvg =', np.mean(elevationDeg))
    print('                         elevationDegMin =', elevationDeg.min())

    plotEzCon1dSamplesAnt(plotName, elevationDeg, [], 'green',
        'Elevation (Degrees)')

    # free elevationDeg memory
    elevationDeg = []
    elevationDeg = None
    del elevationDeg



def plotEzCon109antXTVTCmDop():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ezConOut                             # float and int 2d array

    plotName = 'ezCon109antXTVTCmDop.png'

    plotCountdown -= 1

    if 109 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    antXTVTCmDop = ezConOut[:, 9]

    print('                         antXTVTCmDopMax =', antXTVTCmDop.max())
    print('                         antXTVTCmDopAvg =', np.mean(antXTVTCmDop))
    print('                         antXTVTCmDopMin =', antXTVTCmDop.min())

    plotEzCon1dSamplesAnt(plotName, antXTVTCmDop, [], 'green',
        'AntXTVT Center of Mass of Doppler (MHz)')



def plotEzCon200rawRawAvg():

    global raw                      # float 2d array

    global rawLenM1                 # integer

    global fileNameLast             # string
    global plotCountdown                # integer
    global titleS                   # string
    global ezConDispGrid            # integer
    global dataTimeUtc              # 'astropy.time.core.Time' object array

    global xLabelSRaw               # string        creation
    global xTickLocsRaw             # float array   creation
    global xTickLabelsRaw           # string list   creation
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon200rawRawAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 200 and 200 <= ezConPlotRangeL[1]:
    if 200 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # create rawAvg array: for each raw sample, the average of that sample's spectrum values
    rawAvg = np.mean(raw, axis=0)
    print('                         rawRawAvgMax =', rawAvg.max())
    print('                         rawRawAvgAvg =', np.mean(rawAvg))
    print('                         rawRawAvgMin =', rawAvg.min())

    plt.clf()

    # plot all raw data as connected green dots
    plt.plot(rawAvg, 'go-')

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    if ezConRawSamplesUseL:
        xLabelSRaw = f'RawRaw Sample Number (last={rawLenM1 + ezConRawSamplesUseL[0]:,})' \
            + ' with UTC Hour:Min (last=' + dataTimeUtc[-1].iso[11:16] + ')'
    else:
        xLabelSRaw = f'RawRaw Sample Number (last={rawLenM1:,})' \
            + ' with UTC Hour:Min (last=' + dataTimeUtc[-1].iso[11:16] + ')'
    plt.xlabel(xLabelSRaw)
    plt.xlim(0, rawLenM1)
    xTickLocsRaw, xTickLabelsRaw = plt.xticks()
    # dataTimeUtcStrThis = dataTimeUtc[n].iso
    # https://docs.astropy.org/en/stable/time/#id3
    # iso   TimeISO   ‘2000-01-01 00:00:00.000’
    #                  01234567890123456
    if ezConRawSamplesUseL:
        for i in range(len(xTickLocsRaw) - 1):
            xTickLabelsRaw[i] = f'{int(xTickLocsRaw[i] + ezConRawSamplesUseL[0]):,}  ' + \
                dataTimeUtc[int(xTickLocsRaw[i])].iso[11:16]
    else:
        for i in range(len(xTickLocsRaw) - 1):
            xTickLabelsRaw[i] = f'{int(xTickLocsRaw[i]):,}  ' + \
                dataTimeUtc[int(xTickLocsRaw[i])].iso[11:16]
    xTickLocsRaw[-1] = rawLenM1
    if 0.975 < xTickLocsRaw[-2] / rawLenM1:   # if last label overlaps, blank it
        xTickLabelsRaw[-1] = ''
    elif ezConRawSamplesUseL:
        xTickLabelsRaw[-1] = f'{rawLenM1 + ezConRawSamplesUseL[0]:,}  ' + dataTimeUtc[-1].iso[11:16]
    else:
        xTickLabelsRaw[-1] = f'{rawLenM1:,}  ' + dataTimeUtc[-1].iso[11:16]
    plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

    plt.ylabel('RawRaw Spectrum Average' \
        + '\n\n ezConRawSamplesUseL = ' + str(ezConRawSamplesUseL))

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201ArawAvg():

    global raw                      # float 2d array

    global rawLenM1                 # integer

    global fileNameLast             # string
    global plotCountdown                # integer
    global titleS                   # string
    global ezConDispGrid            # integer
    global dataTimeUtc              # 'astropy.time.core.Time' object array

    global xLabelSRaw               # string        creation
    global xTickLocsRaw             # float array   creation
    global xTickLabelsRaw           # string list   creation
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon201ArawAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # create rawAvg array: for each raw sample, the average of that sample's spectrum values
    rawAvg = np.mean(raw, axis=0)
    print('                         rawAvgMax =', rawAvg.max())
    print('                         rawAvgAvg =', np.mean(rawAvg))
    print('                         rawAvgMin =', rawAvg.min())

    plt.clf()

    # plot all raw data as connected green dots
    plt.plot(rawAvg, 'go-')

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    if ezConRawSamplesUseL:
        xLabelSRaw = f'Raw Sample Number (last={rawLenM1 + ezConRawSamplesUseL[0]:,})' \
            + ' with UTC Hour:Min (last=' + dataTimeUtc[-1].iso[11:16] + ')'
    else:
        xLabelSRaw = f'Raw Sample Number (last={rawLenM1:,})' \
            + ' with UTC Hour:Min (last=' + dataTimeUtc[-1].iso[11:16] + ')'
    plt.xlabel(xLabelSRaw)
    plt.xlim(0, rawLenM1)
    xTickLocsRaw, xTickLabelsRaw = plt.xticks()
    # dataTimeUtcStrThis = dataTimeUtc[n].iso
    # https://docs.astropy.org/en/stable/time/#id3
    # iso   TimeISO   ‘2000-01-01 00:00:00.000’
    #                  01234567890123456
    if ezConRawSamplesUseL:
        for i in range(len(xTickLocsRaw) - 1):
            xTickLabelsRaw[i] = f'{int(xTickLocsRaw[i] + ezConRawSamplesUseL[0]):,}  ' + \
                dataTimeUtc[int(xTickLocsRaw[i])].iso[11:16]
    else:
        for i in range(len(xTickLocsRaw) - 1):
            xTickLabelsRaw[i] = f'{int(xTickLocsRaw[i]):,}  ' + \
                dataTimeUtc[int(xTickLocsRaw[i])].iso[11:16]
    xTickLocsRaw[-1] = rawLenM1
    if 0.975 < xTickLocsRaw[-2] / rawLenM1:   # if last label overlaps, blank it
        xTickLabelsRaw[-1] = ''
    elif ezConRawSamplesUseL:
        xTickLabelsRaw[-1] = f'{rawLenM1 + ezConRawSamplesUseL[0]:,}  ' + dataTimeUtc[-1].iso[11:16]
    else:
        xTickLabelsRaw[-1] = f'{rawLenM1:,}  ' + dataTimeUtc[-1].iso[11:16]
    plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

    plt.ylabel('Raw Spectrum Average' \
        + '\n\n ezConRawSamplesUseL = ' + str(ezConRawSamplesUseL))

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201EsampleRefAgain():

    #global raw                      # float 2d array
    #global raw                      # float 2d array
    #global refRaw                   # float 2d array

    global sampleRefAgain           # float 2d array
    #global maskRawRef               # float 2d array

    global rawLen                   # integer
    #global antLen                   # integer

    global xLabelSRaw               # string
    global xTickLocsRaw             # float array
    global xTickLabelsRaw           # string list

    plotName = 'ezCon201EsampleRefAgain.png'

    #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print('   plotting ' + plotName + ' ================================')

    plt.clf()

    print('                         sampleRefAgainMax =', sampleRefAgain.max())
    #print('                         sampleRefAgain =', sampleRefAgain.sum() / rawLen)
    sampleRefAgainSum = sampleRefAgain.sum()
    print('                         sampleRefAgainAvg =', sampleRefAgainSum / rawLen)
    print('                         sampleRefAgainMin =', sampleRefAgain.min())

    plt.plot(sampleRefAgain, 'bo-')

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel(xLabelSRaw)
    plt.xlim(0, rawLenM1)
    plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

    #plt.ylabel('sampleRefAgain' \
    #    + '\n\n sampleRefAgain = ' + str(int(100. * sampleRefAgain.sum() / rawLen)) + ' %')
    plt.ylabel('sampleRefAgain = ' + str(sampleRefAgainSum) \
        + ' = ' + str(int(100. * sampleRefAgainSum / rawLen)) + ' %' \
        + '\n\n rawLen = ' + str(rawLen))
    #plt.ylim(-90, 90)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201GrawAntRef():
    # plot rawAvg, then color Ant and Ref

    global fileNameLast             # string
    global plotCountdown            # integer
    global raw                      # float 2d array

    global maskRawAnt               # float 2d array
    global maskRawRef               # float 2d array

    global rawLenM1                 # integer
    global antLen                   # integer

    global xLabelSRaw               # string
    global xTickLocsRaw             # float array
    global xTickLabelsRaw           # string list

    plotName = 'ezCon201GrawAntRef.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # create rawAvg array: for each raw sample, the average of that sample's spectrum values
    rawAvg = np.mean(raw, axis=0)
    print('                         rawAvgMax =', rawAvg.max())
    print('                         rawAvgAvg =', np.mean(rawAvg))
    print('                         rawAvgMin =', rawAvg.min())

    # create rawAvgAnt as the raw samples, but only where sample is an ANT
    # start with rawAvg
    rawAvgAnt = rawAvg + 0.
    # so as not to plot, where not an ANT sample, make np.nan
    rawAvgAnt[np.logical_not(maskRawAnt)] = np.nan
    print()
    print('                         rawAvgAntMax =', np.nanmax(rawAvgAnt))
    print('                         rawAvgAntAvg =', np.nansum(rawAvgAnt) / antLen)
    print('                         rawAvgAntMin =', np.nanmin(rawAvgAnt))

    # create rawAvgRef as the raw samples, but only where sample is a REF
    # start with rawAvg
    rawAvgRef = rawAvg + 0.
    # so as not to plot, where not a REF sample, make np.nan
    rawAvgRef[np.logical_not(maskRawRef)] = np.nan
    refQty = sum((maskRawRef + 0))      # might be different than antLen
    print(f'   refQty = {refQty:,}')
    if refQty:      # avoid division by zero
        print('                         rawAvgRefMax =', np.nanmax(rawAvgRef))
        print('                         rawAvgRefAvg =', np.nansum(rawAvgRef) / refQty)
        print('                         rawAvgRefMin =', np.nanmin(rawAvgRef))

    plt.clf()

    # plot all raw data as connected green dots
    plt.plot(rawAvg, 'go-')

    #print('             rawAvgRef =', rawAvgRef)
    # rawAvgRef = [ 1.15663404  nan  1.1568708  ...  1.13110415  nan  1.13264854 ]
    #print('             rawAvgAnt =', rawAvgAnt)
    # rawAvgAnt = [ nan  0.95682753  nan  ...  nan  0.94020758  nan ]
    if 0:
        # ref violet dots unconnected and ant blue dots unconnected
        # plot just ref data as violet dots
        plt.plot(rawAvgRef, 'o', c='violet')

        # plot just ant data as blue dots
        plt.plot(rawAvgAnt, 'bo')

    else:
        # ref violet dots connected and ant blue dots connected
        # create rawAvgRefNoGap like rawAvgRef, but without np.nan values
        rawAvgRefNoGap = rawAvgRef + 0
        if np.isnan(rawAvgRefNoGap[0]):
            # copy from future by 1
            rawAvgRefNoGap[0] = rawAvgRefNoGap[1]
        for i in range(1, rawLen):
            if np.isnan(rawAvgRefNoGap[i]):
                # copy from past by 1
                rawAvgRefNoGap[i] = rawAvgRefNoGap[i-1]
        # plot rawAvgRefNoGap as connected violet dots
        #plt.plot(rawAvgRefNoGap, 'vo-')
        plt.plot(rawAvgRefNoGap, 'o-', c='violet')

        # create rawAvgAntNoGap like rawAvgAnt, but without np.nan values
        rawAvgAntNoGap = rawAvgAnt + 0
        if np.isnan(rawAvgAntNoGap[0]):
            # copy from future by 1
            rawAvgAntNoGap[0] = rawAvgAntNoGap[1]
        for i in range(1, rawLen):
            if np.isnan(rawAvgAntNoGap[i]):
                # copy from past by 1
                rawAvgAntNoGap[i] = rawAvgAntNoGap[i-1]
        # plot rawAvgAntNoGap as connected blue dots
        plt.plot(rawAvgAntNoGap, 'bo-')

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel(xLabelSRaw)
    plt.xlim(0, rawLenM1)
    plt.xticks(xTickLocsRaw, xTickLabelsRaw, rotation=45, ha='right', rotation_mode='anchor')

    plt.ylabel('Last Raw Spectrum Average   (Ant = blue, Ref = violet)'
        + '\n\n ezConRawSamplesUseL = ' + str(ezConRawSamplesUseL))

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201HtimeUtcMjdDBetweenRaw():

    global fileNameLast             # string
    global plotCountdown            # integer
    global dataTimeUtc              # 'astropy.time.core.Time' object array

    global raw                      # float 2d array
    global rawLen                   # integer

    global xLabelSRaw               # string
    global xTickLocsRaw             # float array
    global xTickLabelsRaw           # string list

    plotName = 'ezCon201HtimeUtcMjdDBetweenRaw.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    # 24 * 60 * 60 = 86400 seconds in one MJD Day
    timeUtcMjdDBetweenRaw = np.empty(rawLen)
    for i in range(rawLen):
        timeUtcMjdDBetweenRaw[i] = dataTimeUtc[i].mjd
    timeUtcMjdDBetweenRaw = (timeUtcMjdDBetweenRaw[1:] - timeUtcMjdDBetweenRaw[:-1]) * 86400
    timeUtcMjdDBetweenRawAvg = int(np.mean(timeUtcMjdDBetweenRaw) + 0.5)
    timeUtcMjdDBetweenRawSpan \
        = int((timeUtcMjdDBetweenRaw.max() - timeUtcMjdDBetweenRaw.min()) + 0.5)

    plt.plot(timeUtcMjdDBetweenRaw, 'go-')

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlim(0, rawLenM1 - 1)

    plt.ylabel('Seconds Between ' + str(rawLen) + ' Raw Samples' \
        + '\n\nMedian=' + str(int(np.median(timeUtcMjdDBetweenRaw) + 0.5)) \
        + '  Mean=' + str(timeUtcMjdDBetweenRawAvg) \
        + '  Span=' + str(timeUtcMjdDBetweenRawSpan))
    # truncate y axis if too large
    axes = plt.gca()
    y_min, y_max = axes.get_ylim()
    if 400 < y_max - y_min:
        plt.ylim(0, 400)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201ItimeUtcMjdDBetweenAntRaw():

    global fileNameLast             # string
    global plotCountdown            # integer
    global dataTimeUtc              # 'astropy.time.core.Time' object array

    global rawLen                   # integer
    global antLen                   # integer
    global antLenM1                 # integer

    global maskRawAnt               # Boolean array

    plotName = 'ezCon201ItimeUtcMjdDBetweenAntRaw.png'

    plotCountdown -= 1

    print(f'   rawLen = {rawLen:,}')
    timeUtcMjdRaw = np.empty(rawLen)
    for i in range(rawLen):
        timeUtcMjdRaw[i] = dataTimeUtc[i].mjd       # convert to MJD numbers

    #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    # mask off all but ANT samples
    timeUtcMjdRawAnt = timeUtcMjdRaw[maskRawAnt]

    # seconds per MJD day = 24 * 60 * 60 = 86400
    timeUtcMjdDBetweenRawAnt = (timeUtcMjdRawAnt[1:] - timeUtcMjdRawAnt[:-1]) * 86400.
    timeUtcMjdDBetweenRawAntAvg = int((timeUtcMjdDBetweenRawAnt.sum() / antLenM1) + 0.5)
    timeUtcMjdDBetweenRawAntSpan \
        = int((timeUtcMjdDBetweenRawAnt.max() - timeUtcMjdDBetweenRawAnt.min()) + 0.5)

    plt.plot(timeUtcMjdDBetweenRawAnt, 'bo-')

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlim(0, antLenM1 - 1)

    plt.ylabel('Seconds Between ' + str(antLen) + ' AntRaw Samples' \
        + '\n\nMedian=' + str(int(np.median(timeUtcMjdDBetweenRawAnt) + 0.5)) \
        + '  Mean=' + str(timeUtcMjdDBetweenRawAntAvg) \
        + '  Span=' + str(timeUtcMjdDBetweenRawAntSpan))

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201JtimeUtcMjdDBetweenRefRaw():

    global fileNameLast             # string
    global plotCountdown            # integer
    global dataTimeUtc              # 'astropy.time.core.Time' object array

    global rawLen                   # integer

    global maskRawRef               # Boolean array

    plotName = 'ezCon201JtimeUtcMjdDBetweenRefRaw.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 201 and 201 <= ezConPlotRangeL[1]:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    refQty = np.sum((maskRawRef + 0))          # might be different than antLen
    if refQty < 2:
        print()
        print()
        print()
        print()
        print()
        print(' ========== Warning: Can not create this plot with less than 2 REF samples')
        print()
        print()
        print()
        print()
        print()

        plt.plot([0, 1], [0, 0], 'o-', c='violet')

        plt.xlim(0, 1)
        plt.ylim(0, 1)

        plt.ylabel('Seconds Between ' + str(refQty) + ' RefRaw Samples\n\n')

        plt.text(0, 0.5, '      Warning: Can not create this plot with less than 2 Ref samples')
        
    else:
        timeUtcMjdRaw = np.empty(rawLen)
        for i in range(rawLen):
            timeUtcMjdRaw[i] = dataTimeUtc[i].mjd       # convert to MJD numbers
        # mask off all but REF samples
        timeUtcMjdRawRef = timeUtcMjdRaw[maskRawRef]
        # seconds per MJD day = 24 * 60 * 60 = 86400
        timeUtcMjdDBetweenRawRef = (timeUtcMjdRawRef[1:] - timeUtcMjdRawRef[:-1]) * 86400.
        timeUtcMjdDBetweenRawRefAvg = int(np.mean(timeUtcMjdDBetweenRawRef) + 0.5)
        timeUtcMjdDBetweenRawRefSpan \
            = int((timeUtcMjdDBetweenRawRef.max() - timeUtcMjdDBetweenRawRef.min()) + 0.5)

        plt.plot(timeUtcMjdDBetweenRawRef, 'o-', c='violet')
        plt.xlim(0, refQty - 2)

        plt.ylabel('Seconds Between ' + str(refQty) + ' RefRaw Samples' \
            + '\n\nMedian=' + str(int(np.median(timeUtcMjdDBetweenRawRef) + 0.5)) \
            + '  Mean=' + str(timeUtcMjdDBetweenRawRefAvg) \
            + '  Span=' + str(timeUtcMjdDBetweenRawRefSpan))

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon201ZantFileIndex():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global dataFileIdx                          # integer array

    plotName = 'ezCon201ZantFileIndex.png'

    plotCountdown -= 1

    #if 201 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 201:
    if 201 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    #print('                         dataFileIdx =', dataFileIdx.tolist())
    #print()
    print('                         dataFileIdxMax =', dataFileIdx.max())
    print('                         dataFileIdxMin =', dataFileIdx.min())
    #print('                         len(dataFileIdx) =', len(dataFileIdx))

    plotEzCon1dSamplesAnt(plotName, dataFileIdx, [], 'blue',
        'Ant Antenna Data File Index')



def plotEzCon202antRawAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antRawAvg                            # float array       creation

    plotName = 'ezCon202antRawAvg.png'

    antRawAvg = np.mean(ant, axis=0)            # creation

    plotCountdown -= 1

    #if 202 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 202:
    if 202 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antRawAvgMax =', antRawAvg.max())
    print('                         antRawAvgAvg =', np.mean(antRawAvg))
    print('                         antRawAvgMin =', antRawAvg.min())

    plotEzCon1dSamplesAnt(plotName, antRawAvg, [], 'blue',
        'AntRaw Antenna Spectrum Average')



def plotEzCon207antAvg():
    # same as earlier plotEzCon110antAvg()

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antAvg                               # float array       creation

    plotName = 'ezCon207antAvg.png'

    antAvg = np.mean(ant, axis=0)               # creation

    plotCountdown -= 1

    #if 207 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 207:
    if 207 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antAvgMax =', antAvg.max())
    print('                         antAvgAvg =', np.mean(antAvg))
    print('                         antAvgMin =', antAvg.min())

    plotEzCon1dSamplesAnt(plotName, antAvg, [], 'blue',
        'Ant Antenna Spectrum Average')



def plotEzCon217antMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antMax                               # float array       creation

    plotName = 'ezCon217antMax.png'

    antMax = np.amax(ant, axis=0)               # creation

    plotCountdown -= 1

    #if 217 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 217:
    if 217 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antMaxMax =', antMax.max())
    print('                         antMaxAvg =', np.mean(antMax))
    print('                         antMaxMin =', antMax.min())

    plotEzCon1dSamplesAnt(plotName, antMax, [], 'blue',
        'Ant Antenna Spectrum Maximum')



def plotEzCon222refRawAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ref                                  # float 2d array
    global refRawAvg                            # float array       creation

    plotName = 'ezCon222refRawAvg.png'

    plotCountdown -= 1

    #if 222 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 222:
    if 222 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         refRawAvgMax =', refRawAvg.max())
    print('                         refRawAvgAvg =', np.mean(refRawAvg))
    print('                         refRawAvgMin =', refRawAvg.min())

    plotEzCon1dSamplesAnt(plotName, refRawAvg, [], 'violet',
        'RefRaw Antenna Spectrum Average')



def plotEzCon227refAvg():
    # same as earlier plotEzCon112refAvg()
    
    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ref                                  # float 2d array
    global refAvg                               # float array       creation

    plotName = 'ezCon227refAvg.png'

    refAvg = np.mean(ref, axis=0)               # creation

    plotCountdown -= 1

    #if 227 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 227:
    if 227 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         refAvgMax =', refAvg.max())
    print('                         refAvgAvg =', np.mean(refAvg))
    print('                         refAvgMin =', refAvg.min())

    plotEzCon1dSamplesAnt(plotName, refAvg, [], 'violet',
        'Ref Antenna Spectrum Average')



def plotEzCon237refMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ref                                  # float 2d array
    global refMax                               # float array       creation

    plotName = 'ezCon237refMax.png'

    refMax = np.amax(ref, axis=0)               # creation

    plotCountdown -= 1

    #if 237 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 237:
    if 237 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         refMaxMax =', refMax.max())
    print('                         refMaxAvg =', np.mean(refMax))
    print('                         refMaxMin =', refMax.min())

    plotEzCon1dSamplesAnt(plotName, refMax, [], 'violet',
        'Ref Reference Spectrum Maximum')



def plotEzCon241antBaseline():
    # creates antBaseline

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global ant                                  # float 2d array
    global antBaseline                          # float array       creation
    global ezConAntBaselineFreqBinsFracL        # float list

    plotName = 'ezCon241antBaseline.png'

    # In each ant sample spectrum, hydrogen appears in the center frequencies,
    # so average the low and high frequency values.
    # Create antBaseline with ant, and ezConAntBaselineFreqBinsFracL .
    ezConAntBaselineFreqBin = np.empty(4, dtype=int)
    for i in range(4):
        ezConAntBaselineFreqBin[i] = int(ezConAntBaselineFreqBinsFracL[i] * (fileFreqBinQty - 1))
    # for each sample, average the ant values (from [0] to [1]) and (from [2] to [3])
    antBaseline = (np.sum(ant[ezConAntBaselineFreqBin[0]:ezConAntBaselineFreqBin[1], :], axis=0) \
        + np.sum(ant[ezConAntBaselineFreqBin[2]:ezConAntBaselineFreqBin[3], :], axis=0)) \
        / ((ezConAntBaselineFreqBin[1] - ezConAntBaselineFreqBin[0]) \
        + (ezConAntBaselineFreqBin[3] - ezConAntBaselineFreqBin[2]))

    plotCountdown -= 1

    #if 241 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 241:
    if 241 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antBasMax =', antBaseline.max())
    print('                         antBasAvg =', np.mean(antBaseline))
    print('                         antBasMin =', antBaseline.min())

    plotEzCon1dSamplesAnt(plotName, antBaseline, [], 'red',
        'Ant Baseline')



def plotEzCon247antBAvg():
    # same as earlier plotEzCon114antBAvg()

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antB                                 # float 2d array
    global antBAvg                              # float array       creation

    plotName = 'ezCon247antBAvg.png'

    antBAvg = np.mean(antB, axis=0)             # creation

    plotCountdown -= 1

    #if 247 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 247:
    if 247 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    antBAvgMax = antBAvg.max()
    antBAvgMin = antBAvg.min()
    print('                         antBAvgMax =', antBAvgMax)
    print('                         antBAvgAvg =', np.mean(antBAvg))
    print('                         antBAvgMin =', antBAvgMin)

    plotEzCon1dSamplesAnt(plotName, antBAvg, [], 'red',
        'AntB Antenna Spectrum Average')



def plotEzCon257antBMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antB                                 # float 2d array
    global antBMax                              # float array       creation

    plotName = 'ezCon257antBMax.png'

    antBMax = np.amax(antB, axis=0)             # creation

    plotCountdown -= 1

    #if 257 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 257:
    if 257 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antBMaxMax =', antBMax.max())
    print('                         antBMaxAvg =', np.mean(antBMax))
    print('                         antBMaxMin =', antBMax.min())

    plotEzCon1dSamplesAnt(plotName, antBMax, [], 'red',
        'AntB Spectrum Maximum')



def plotEzCon261antRAAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antRA                                # float 2d array
    global antRAAvg                             # float array       creation

    plotName = 'ezCon261antRAAvg.png'

    antRAAvg = np.mean(antRA, axis=0)           # creation

    plotCountdown -= 1

    #if 261 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 261:
    if 261 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antRAAvgMax =', antRAAvg.max())
    print('                         antRAAvgAvg =', np.mean(antRAAvg))
    print('                         antRAAvgMin =', antRAAvg.min())

    plotEzCon1dSamplesAnt(plotName, antRAAvg, [], 'orange',
        'AntRA Antenna Spectrum Average')



def plotEzCon262antRABaseline():
    # creates antRABaseline

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antRA                                # float 2d array
    global antRABaseline                        # float array       creation
    global ezConAntRABaselineFreqBinsFracL      # float list

    plotName = 'ezCon262antRABasAvg.png'

    # In each antRA sample spectrum, hydrogen appears in the center frequencies,
    # so average the low and high frequency values.
    # Create antRABaseline with antRA, and ezConAntRABaselineFreqBinsFracL .
    ezConAntRABaselineFreqBin = np.empty(4, dtype=int)
    for i in range(4):
        ezConAntRABaselineFreqBin[i] = int(ezConAntRABaselineFreqBinsFracL[i] * (fileFreqBinQty - 1))
    # for each sample, average the antRA values (from [0] to [1]) and (from [2] to [3])
    antRABaseline = (np.sum(antRA[ezConAntRABaselineFreqBin[0]:ezConAntRABaselineFreqBin[1], :], axis=0) \
        + np.sum(antRA[ezConAntRABaselineFreqBin[2]:ezConAntRABaselineFreqBin[3], :], axis=0)) \
        / ((ezConAntRABaselineFreqBin[1] - ezConAntRABaselineFreqBin[0]) \
        + (ezConAntRABaselineFreqBin[3] - ezConAntRABaselineFreqBin[2]))

    plotCountdown -= 1

    #if 262 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 262:
    if 262 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antRABasMax =', antRABaseline.max())
    print('                         antRABasAvg =', np.mean(antRABaseline))
    print('                         antRABasMin =', antRABaseline.min())

    plotEzCon1dSamplesAnt(plotName, antRABaseline, [], 'orange',
        'AntRA Baseline')



def plotEzCon267antRBAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antRB                                # float 2d array
    global antRBAvg                             # float array       creation

    plotName = 'ezCon267antRBAvg.png'

    antRBAvg = np.mean(antRB, axis=0)           # creation

    plotCountdown -= 1

    #if 267 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 267:
    if 267 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antRBAvgMax =', antRBAvg.max())
    print('                         antRBAvgAvg =', np.mean(antRBAvg))
    print('                         antRBAvgMin =', antRBAvg.min())

    plotEzCon1dSamplesAnt(plotName, antRBAvg, [], 'orange',
        'AntRB Antenna Spectrum Average')



def plotEzCon277antRBMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antRB                                # float 2d array
    global antRBMax                             # float array       creation

    plotName = 'ezCon277antRBMax.png'

    antRBMax = np.amax(antRB, axis=0)           # creation

    plotCountdown -= 1

    #if 277 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 277:
    if 277 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antRBMaxMax =', antRBMax.max())
    print('                         antRBMaxAvg =', np.mean(antRBMax))
    print('                         antRBMaxMin =', antRBMax.min())

    plotEzCon1dSamplesAnt(plotName, antRBMax, [], 'orange',
        'AntRB Spectrum Maximum')



def plotEzCon281antXTAvg():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXT                                # float 2d array
    global antXTAvg                             # float array       creation

    #plotName = 'ezCon281antXTAvg.png'
    plotName = 'ezCon281' + antXNameL[0] + 'TAvg.png'


    antXTAvg = np.mean(antXT, axis=0)           # creation

    plotCountdown -= 1

    #if 281 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 281:
    if 281 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antXTAvgMax =', antXTAvg.max())
    print('                         antXTAvgAvg =', np.mean(antXTAvg))
    print('                         antXTAvgMin =', antXTAvg.min())

    plotEzCon1dSamplesAnt(plotName, antXTAvg, [], 'green',
        antXNameL[1]+'T Antenna Spectrum Average')



def plotEzCon282antXTVAvg():
    # same as earlier plotEzCon118antXTVAvg()

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXTV                               # float 2d array
    global antXTVAvg                            # float array       creation

    #plotName = 'ezCon282antXTVAvg.png'
    plotName = 'ezCon282' + antXNameL[0] + 'TVAvg.png'

    antXTVAvg = np.mean(antXTV, axis=0)         # creation

    plotCountdown -= 1

    #if 282 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 282:
    if 282 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antXTVAvgMax =', antXTVAvg.max())
    print('                         antXTVAvgAvg =', np.mean(antXTVAvg))
    print('                         antXTVAvgMin =', antXTVAvg.min())

    plotEzCon1dSamplesAnt(plotName, antXTVAvg, [], 'green',
        antXNameL[1]+'TV Antenna Spectrum Average')



def plotEzCon287antXTVTAvg():
    # creates antXTVTAvg into ezConOut[:, 18], antXTVTCmDop into ezConOut[:, 9]

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXTVT                              # float 2d array
    global antLen                               # integer
    global freqStep                             # float
    global dopplerSpanD2                        # float

    global ezConAntXTVTLevelL                   # float list
    global ezConOut                             # float and int 2d array

    #plotName = 'ezCon287antXTVTAvg.png'
    plotName = 'ezCon287' + antXNameL[0] + 'TVTAvg.png'

    # creation of antXTVTAvg into ezConOut[:, 18]
    ezConOut[:, 18] = ezConAntXTVTLevelL[0] * np.mean(antXTVT, axis=0) + ezConAntXTVTLevelL[1]

    # creation of antXTVTCmDop into ezConOut[:, 9]
    for n in range(antLen):
        # calculate Center of Mass of AntXTVT spectrum
        # https://en.wikipedia.org/wiki/Center_of_mass#Definition
        ######antXTVTCmFreqBinFloat = sum([freqBin * antXTVT[freqBin, n] for freqBin in range(fileFreqBinQty)]) \
        ######    / antXTVTSum
        antXTVTThis = antXTVT[:, n] 
        antXTVTCmFreqBinFloatThis = sum(antXTVTThis * range(fileFreqBinQty)) / antXTVTThis.sum()
        antXTVTCmDopThis = antXTVTCmFreqBinFloatThis * freqStep - dopplerSpanD2
        ezConOut[n, 9] = antXTVTCmDopThis

    plotCountdown -= 1

    #if 287 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 287:
    if 287 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antXTVTAvgMax =', ezConOut[:, 18].max())
    print('                         antXTVTAvgAvg =', np.mean(ezConOut[:, 18]))
    print('                         antXTVTAvgMin =', ezConOut[:, 18].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 18], [], 'green',
        antXNameL[1]+'TVT Antenna Spectrum Average')



def plotEzCon297antXTVTMax():

    global fileNameLast                         # string
    global plotCountdown                        # integer
    #global ezConPlotRangeL                      # integer list
    global ezConPlotRequestedL                  # integer list

    global antXNameL                            # list of strings
    global antXTVT                              # float 2d array
    global ezConAntXTVTLevelL                   # float list
    global ezConOut                             # float and int 2d array

    plotName = 'ezCon297' + antXNameL[0] + 'TVTMax.png'

    # creation of antXTVTMax into ezConOut[:, 19]
    ezConOut[:, 19] = ezConAntXTVTLevelL[0] * np.amax(antXTVT, axis=0) + ezConAntXTVTLevelL[1]

    plotCountdown -= 1

    #if 297 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 297:
    if 297 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    print('                         antXTVTMaxMax =', ezConOut[:, 19].max())
    print('                         antXTVTMaxAvg =', np.mean(ezConOut[:, 19]))
    print('                         antXTVTMaxMin =', ezConOut[:, 19].min())

    plotEzCon1dSamplesAnt(plotName, ezConOut[:, 19], [], 'green',
        antXNameL[1]+'TVT Spectrum Maximum')



def plotEzCon300rawRawByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global raw                      # float 2d array

    plotName = 'ezCon300rawRawByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 300 and 300 <= ezConPlotRangeL[1]:
    if 300 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # calculate average by Freq Bin and plot by Doppler
    plotEzCon1dByFreqBin(plotName, np.mean(raw, axis=1), 'green',
        'RawRaw Average Spectrum')



def plotEzCon301rawByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global raw                      # float 2d array

    plotName = 'ezCon301rawByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 301 and 301 <= ezConPlotRangeL[1]:
    if 301 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    # calculate average by Freq Bin and plot by Doppler
    plotEzCon1dByFreqBin(plotName, np.mean(raw, axis=1), 'green',
        'Raw Average Spectrum')



def plotEzCon302antRawByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global ant                      # float 2d array

    plotName = 'ezCon302antRawByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 302 and 302 <= ezConPlotRangeL[1]:
    if 302 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(ant, axis=1), 'blue',
        'AntRaw Average Spectrum')



def plotEzCon307antByFreqBinAvg():
    # after antRfiRemoval()

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global ant                      # float 2d array
    global OutFreqString            # string

    plotName = 'ezCon307antByFreqAvg.png'

    if 1:
        #print()
        #print(f'  {fileNameLast}  ======================================== Frequency study of Ant')
        OutFreqStringThis = \
            f'\n  {fileNameLast}  ======================================== Frequency study of Ant\n'

        antByFreqBinSumAvg = np.mean(ant, axis=1)
        antByFreqBinSumAvgMin = min(antByFreqBinSumAvg)
        antByFreqBinSumAvgMax = max(antByFreqBinSumAvg)
        antByFreqBinSumAvgSpanD100 \
            = (antByFreqBinSumAvgMax - antByFreqBinSumAvgMin) / 100.
        # to allow division by antByFreqBinSumAvgSpanD100
        if not antByFreqBinSumAvgSpanD100:
            antByFreqBinSumAvgSpanD100 = 1e-14

        #print()
        #print(' FreqBin indexes of 5 highest-values of Ant:')
        OutFreqStringThis += '\n FreqBin indexes of 5 highest-values of Ant:\n'
        antByFreqBinSumAvgIdxbyValueHigh5 = np.array(antByFreqBinSumAvg).argsort()[::-1][:5]
        for i in range(len(antByFreqBinSumAvgIdxbyValueHigh5)):
            antByFreqBinSumAvgThis = \
                antByFreqBinSumAvg[antByFreqBinSumAvgIdxbyValueHigh5[i]]
            antByFreqBinSumAvgThisPercent = \
                (antByFreqBinSumAvgThis - antByFreqBinSumAvgMin) / antByFreqBinSumAvgSpanD100
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antByFreqBinSumAvgIdxbyValueHigh5[i]}' \
                + f'       antByFreqBinSumAvg = {antByFreqBinSumAvgThis}' \
                + f'       {(antByFreqBinSumAvgThis - antByFreqBinSumAvgMin) / antByFreqBinSumAvgSpanD100} %'
            if antByFreqBinSumAvgThisPercent < 95:
                #print(' i =', i,
                #    '      FreqBin =', antByFreqBinSumAvgIdxbyValueHigh5[i],
                #    '      antByFreqBinSumAvg =', antByFreqBinSumAvgThis,
                #    '      ', (antByFreqBinSumAvgThis - antByFreqBinSumAvgMin) \
                #    / antByFreqBinSumAvgSpanD100, '%  <=========== < 95%')
                OutFreqStringThis += '  <=========== < 95%\n'
            else:
                #print(' i =', i,
                #    '      FreqBin =', antByFreqBinSumAvgIdxbyValueHigh5[i],
                #    '      antByFreqBinSumAvg =', antByFreqBinSumAvgThis,
                #    '      ', (antByFreqBinSumAvgThis - antByFreqBinSumAvgMin) \
                #    / antByFreqBinSumAvgSpanD100, '%')
                OutFreqStringThis += '\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antByFreqBinSumAvgIdxbyValueHigh5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 lowest-values of Ant:')
        OutFreqStringThis += '\n FreqBin indexes of 5 lowest-values of Ant:\n'
        antByFreqBinSumAvgIdxbyValueLow5 = np.array(antByFreqBinSumAvg).argsort()[:5]
        for i in range(len(antByFreqBinSumAvgIdxbyValueLow5)):
            antByFreqBinSumAvgThis = \
                antByFreqBinSumAvg[antByFreqBinSumAvgIdxbyValueLow5[i]]
            #print(' i =', i,
            #    '      FreqBin =', antByFreqBinSumAvgIdxbyValueLow5[i],
            #    '      antByFreqBinSumAvg =', antByFreqBinSumAvgThis,
            #    '      ', (antByFreqBinSumAvgThis - antByFreqBinSumAvgMin) \
            #    / antByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antByFreqBinSumAvgIdxbyValueLow5[i]}' \
                + f'       antByFreqBinSumAvg = {antByFreqBinSumAvgThis}' \
                + f'       {(antByFreqBinSumAvgThis - antByFreqBinSumAvgMin) / antByFreqBinSumAvgSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antByFreqBinSumAvgIdxbyValueLow5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antByFreqBinSumAvgIdxbyValueLow5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 largest change values of Ant:')
        OutFreqStringThis += '\n FreqBin indexes of 5 largest change values of Ant:\n'
        antByFreqBinSumAvgIdxbyValueDeltaHigh5m1 \
            = np.array(abs(antByFreqBinSumAvg[1:] - antByFreqBinSumAvg[:-1])).argsort()[::-1][:5]
        for i in range(len(antByFreqBinSumAvgIdxbyValueDeltaHigh5m1)):
            antByFreqBinSumAvgDeltaThis = \
                antByFreqBinSumAvg[antByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1] \
                - antByFreqBinSumAvg[antByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i]]
            #print(' i =', i,
            #    '      FreqBin =', antByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1,
            #    '      antByFreqBinSumAvgDelta =', antByFreqBinSumAvgDeltaThis,
            #    '      ', antByFreqBinSumAvgDeltaThis / antByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1}' \
                + f'       antByFreqBinSumAvgDelta = {antByFreqBinSumAvgDeltaThis}' \
                + f'       {antByFreqBinSumAvgDeltaThis / antByFreqBinSumAvgSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antByFreqBinSumAvgIdxbyValueDeltaHigh5m1[0] + 1)
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antByFreqBinSumAvgIdxbyValueDeltaHigh5m1[0] + 1}'
        print(OutFreqStringThis)
        OutFreqString = '\n\n\n\n' \
            + '============================================================================\n' \
            + '============================================================================\n' \
            + '============================================================================\n' \
            + '\n\n\n' + OutFreqStringThis

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 307 and 307 <= ezConPlotRangeL[1]:
    if 307 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, antByFreqBinSumAvg, 'blue',
        'Ant Average Spectrum')



def plotEzCon317antByFreqBinMax():
    # after antRfiRemoval()

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global ant                      # float 2d array
    global OutFreqString            # string

    plotName = 'ezCon317antByFreqMax.png'

    if 1:
        #print()
        #print(f'  {fileNameLast}  ============================ Frequency study of AntByFreqBinMax')
        OutFreqStringThis = \
            f'\n  {fileNameLast}  ============================ Frequency study of AntByFreqBinMax\n'

        antByFreqBinMax = np.amax(ant, axis=1)
        antByFreqBinMaxMin = min(antByFreqBinMax)
        antByFreqBinMaxMax = max(antByFreqBinMax)
        antByFreqBinMaxSpanD100 \
            = (antByFreqBinMaxMax - antByFreqBinMaxMin) / 100.
        # to allow division by antByFreqBinMaxSpanD100
        if not antByFreqBinMaxSpanD100:
            antByFreqBinMaxSpanD100 = 1e-14

        #print()
        #print(' FreqBin indexes of 5 highest-values of AntByFreqBinMax:')
        OutFreqStringThis += '\n FreqBin indexes of 5 highest-values of AntByFreqBinMax:\n'
        antByFreqBinMaxIdxbyValueHigh5 = np.array(antByFreqBinMax).argsort()[::-1][:5]
        for i in range(len(antByFreqBinMaxIdxbyValueHigh5)):
            antByFreqBinMaxThis = \
                antByFreqBinMax[antByFreqBinMaxIdxbyValueHigh5[i]]
            antByFreqBinMaxThisPercent = \
                (antByFreqBinMaxThis - antByFreqBinMaxMin) / antByFreqBinMaxSpanD100
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antByFreqBinMaxIdxbyValueHigh5[i]}' \
                + f'       antByFreqBinMax = {antByFreqBinMaxThis}' \
                + f'       {(antByFreqBinMaxThis - antByFreqBinMaxMin) / antByFreqBinMaxSpanD100} %'
            if antByFreqBinMaxThisPercent < 95:
                #print(' i =', i,
                #    '      FreqBin =', antByFreqBinMaxIdxbyValueHigh5[i],
                #    '      antByFreqBinMax =', antByFreqBinMaxThis,
                #    '      ', (antByFreqBinMaxThis - antByFreqBinMaxMin) \
                #    / antByFreqBinMaxSpanD100, '%  <=========== < 95%')
                OutFreqStringThis += '  <=========== < 95%\n'
            else:
                #print(' i =', i,
                #    '      FreqBin =', antByFreqBinMaxIdxbyValueHigh5[i],
                #    '      antByFreqBinMax =', antByFreqBinMaxThis,
                #    '      ', (antByFreqBinMaxThis - antByFreqBinMaxMin) \
                #    / antByFreqBinMaxSpanD100, '%')
                OutFreqStringThis += '\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antByFreqBinMaxIdxbyValueHigh5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antByFreqBinMaxIdxbyValueHigh5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 lowest-values of AntByFreqBinMax:')
        OutFreqStringThis += '\n FreqBin indexes of 5 lowest-values of AntByFreqBinMax:\n'
        antByFreqBinMaxIdxbyValueLow5 = np.array(antByFreqBinMax).argsort()[:5]
        for i in range(len(antByFreqBinMaxIdxbyValueLow5)):
            antByFreqBinMaxThis = \
                antByFreqBinMax[antByFreqBinMaxIdxbyValueLow5[i]]
            #print(' i =', i,
            #    '      FreqBin =', antByFreqBinMaxIdxbyValueLow5[i],
            #    '      antByFreqBinMax =', antByFreqBinMaxThis,
            #    '      ', (antByFreqBinMaxThis - antByFreqBinMaxMin) \
            #    / antByFreqBinMaxSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antByFreqBinMaxIdxbyValueLow5[i]}' \
                + f'       antByFreqBinMax = {antByFreqBinMaxThis}' \
                + f'       {(antByFreqBinMaxThis - antByFreqBinMaxMin) / antByFreqBinMaxSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antByFreqBinMaxIdxbyValueLow5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antByFreqBinMaxIdxbyValueLow5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 largest change values of AntByFreqBinMax:')
        OutFreqStringThis += '\n FreqBin indexes of 5 largest change values of AntByFreqBinMax:\n'
        antByFreqBinMaxIdxbyValueDeltaHigh5m1 \
            = np.array(abs(antByFreqBinMax[1:] - antByFreqBinMax[:-1])).argsort()[::-1][:5]
        for i in range(len(antByFreqBinMaxIdxbyValueDeltaHigh5m1)):
            antByFreqBinMaxDeltaThis = \
                antByFreqBinMax[antByFreqBinMaxIdxbyValueDeltaHigh5m1[i] + 1] \
                - antByFreqBinMax[antByFreqBinMaxIdxbyValueDeltaHigh5m1[i]]
            #print(' i =', i,
            #    '      FreqBin =', antByFreqBinMaxIdxbyValueDeltaHigh5m1[i] + 1,
            #    '      antByFreqBinMaxDelta =', antByFreqBinMaxDeltaThis,
            #    '      ', antByFreqBinMaxDeltaThis / antByFreqBinMaxSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antByFreqBinMaxIdxbyValueDeltaHigh5m1[i] + 1}' \
                + f'       antByFreqBinMaxDelta = {antByFreqBinMaxDeltaThis}' \
                + f'       {antByFreqBinMaxDeltaThis / antByFreqBinMaxSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antByFreqBinMaxIdxbyValueDeltaHigh5m1[0] + 1)
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antByFreqBinMaxIdxbyValueDeltaHigh5m1[0] + 1}'
        print(OutFreqStringThis)
        OutFreqString += '\n\n\n\n' + OutFreqStringThis

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 317 and 317 <= ezConPlotRangeL[1]:
    if 317 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, antByFreqBinMax, 'blue',
        'Ant Maximum Spectrum')



def plotEzCon322refRawByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global ref                      # float 2d array

    plotName = 'ezCon322refRawByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 322 and 322 <= ezConPlotRangeL[1]:
    if 322 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(ref, axis=1), 'violet',
        'RefRaw Average Spectrum')



def plotEzCon327refByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global ref                      # float 2d array
    global OutFreqString            # string

    plotName = 'ezCon327refByFreqAvg.png'

    if 1:
        #print()
        #print(f'  {fileNameLast}  ======================================== Frequency study of Ref')
        OutFreqStringThis = \
            f'\n  {fileNameLast}  ======================================== Frequency study of Ref\n'

        refByFreqBinSumAvg = np.mean(ref, axis=1)
        refByFreqBinSumAvgMin = min(refByFreqBinSumAvg)
        refByFreqBinSumAvgMax = max(refByFreqBinSumAvg)
        refByFreqBinSumAvgSpanD100 \
            = (refByFreqBinSumAvgMax - refByFreqBinSumAvgMin) / 100.
        # to allow division by refByFreqBinSumAvgSpanD100
        if not refByFreqBinSumAvgSpanD100:
            refByFreqBinSumAvgSpanD100 = 1e-14

        #print()
        #print(' FreqBin indexes of 5 highest-values of Ref:')
        OutFreqStringThis += '\n FreqBin indexes of 5 highest-values of Ref:\n'
        refByFreqBinSumAvgIdxbyValueHigh5 = np.array(refByFreqBinSumAvg).argsort()[::-1][:5]
        for i in range(len(refByFreqBinSumAvgIdxbyValueHigh5)):
            refByFreqBinSumAvgThis = \
                refByFreqBinSumAvg[refByFreqBinSumAvgIdxbyValueHigh5[i]]
            refByFreqBinSumAvgThisPercent = \
                (refByFreqBinSumAvgThis - refByFreqBinSumAvgMin) / refByFreqBinSumAvgSpanD100
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {refByFreqBinSumAvgIdxbyValueHigh5[i]}' \
                + f'       refByFreqBinSumAvg = {refByFreqBinSumAvgThis}' \
                + f'       {(refByFreqBinSumAvgThis - refByFreqBinSumAvgMin) / refByFreqBinSumAvgSpanD100} %'
            if refByFreqBinSumAvgThisPercent < 95:
                #print(' i =', i,
                #    '      FreqBin =', refByFreqBinSumAvgIdxbyValueHigh5[i],
                #    '      refByFreqBinSumAvg =', refByFreqBinSumAvgThis,
                #    '      ', (refByFreqBinSumAvgThis - refByFreqBinSumAvgMin) \
                #    / refByFreqBinSumAvgSpanD100, '%  <=========== < 95%')
                OutFreqStringThis += '  <=========== < 95%\n'
            else:
                #print(' i =', i,
                #    '      FreqBin =', refByFreqBinSumAvgIdxbyValueHigh5[i],
                #    '      refByFreqBinSumAvg =', refByFreqBinSumAvgThis,
                #    '      ', (refByFreqBinSumAvgThis - refByFreqBinSumAvgMin) \
                #    / refByFreqBinSumAvgSpanD100, '%')
                OutFreqStringThis += '\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    refByFreqBinSumAvgIdxbyValueHigh5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {refByFreqBinSumAvgIdxbyValueHigh5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 lowest-values of Ref:')
        OutFreqStringThis += '\n FreqBin indexes of 5 lowest-values of Ref:\n'
        refByFreqBinSumAvgIdxbyValueLow5 = np.array(refByFreqBinSumAvg).argsort()[:5]
        for i in range(len(refByFreqBinSumAvgIdxbyValueLow5)):
            refByFreqBinSumAvgThis = \
                refByFreqBinSumAvg[refByFreqBinSumAvgIdxbyValueLow5[i]]
            #print(' i =', i,
            #    '      FreqBin =', refByFreqBinSumAvgIdxbyValueLow5[i],
            #    '      refByFreqBinSumAvg =', refByFreqBinSumAvgThis,
            #    '      ', (refByFreqBinSumAvgThis - refByFreqBinSumAvgMin) \
            #    / refByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {refByFreqBinSumAvgIdxbyValueLow5[i]}' \
                + f'       refByFreqBinSumAvg = {refByFreqBinSumAvgThis}' \
                + f'       {(refByFreqBinSumAvgThis - refByFreqBinSumAvgMin) / refByFreqBinSumAvgSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    refByFreqBinSumAvgIdxbyValueLow5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {refByFreqBinSumAvgIdxbyValueLow5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 largest change values of Ref:')
        OutFreqStringThis += '\n FreqBin indexes of 5 largest change values of Ref:\n'
        refByFreqBinSumAvgIdxbyValueDeltaHigh5m1 \
            = np.array(abs(refByFreqBinSumAvg[1:] - refByFreqBinSumAvg[:-1])).argsort()[::-1][:5]
        for i in range(len(refByFreqBinSumAvgIdxbyValueDeltaHigh5m1)):
            refByFreqBinSumAvgDeltaThis = \
                refByFreqBinSumAvg[refByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1] \
                - refByFreqBinSumAvg[refByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i]]
            #print(' i =', i,
            #    '      FreqBin =', refByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1,
            #    '      refByFreqBinSumAvgDelta =', refByFreqBinSumAvgDeltaThis,
            #    '      ', refByFreqBinSumAvgDeltaThis / refByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {refByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1}' \
                + f'       refByFreqBinSumAvgDelta = {refByFreqBinSumAvgDeltaThis}' \
                + f'       {refByFreqBinSumAvgDeltaThis / refByFreqBinSumAvgSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    refByFreqBinSumAvgIdxbyValueDeltaHigh5m1[0] + 1)
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {refByFreqBinSumAvgIdxbyValueDeltaHigh5m1[0] + 1}'
        print(OutFreqStringThis)
        OutFreqString += '\n\n\n\n' + OutFreqStringThis

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 327 and 327 <= ezConPlotRangeL[1]:
    if 327 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, refByFreqBinSumAvg, 'violet',
        'Ref Average Spectrum')



def plotEzCon337refByFreqBinMax():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global ref                      # float 2d array

    plotName = 'ezCon337refByFreqMax.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 337 and 337 <= ezConPlotRangeL[1]:
    if 337 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.amax(ref, axis=1), 'violet',
        'Ref Maximum Spectrum')



def plotEzCon347antBByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antB                     # float 2d array

    plotName = 'ezCon347antBByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 347 and 347 <= ezConPlotRangeL[1]:
    if 347 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(antB, axis=1), 'red',
        'AntB Average Spectrum')



def plotEzCon357antBByFreqBinMax():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antB                     # float 2d array

    plotName = 'ezCon357antBByFreqMax.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 357 and 357 <= ezConPlotRangeL[1]:
    if 357 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.amax(antB, axis=1), 'red',
        'AntB Maximum Spectrum')



def plotEzCon361antRAByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antRA                    # float 2d array

    plotName = 'ezCon361antRAByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 361 and 361 <= ezConPlotRangeL[1]:
    if 361 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(antRA, axis=1), 'orange',
        'AntRA Average Spectrum')



def plotEzCon367antRBByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antRB                    # float 2d array

    plotName = 'ezCon367antRBByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 367 and 367 <= ezConPlotRangeL[1]:
    if 367 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(antRB, axis=1), 'orange',
        'AntRB Average Spectrum')



def plotEzCon377antRBByFreqBinMax():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antRB                    # float 2d array

    plotName = 'ezCon377antRBByFreqMax.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 377 and 377 <= ezConPlotRangeL[1]:
    if 377 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.amax(antRB, axis=1), 'orange',
        'AntRB Maximum Spectrum')



def plotEzCon381antXTByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXT                    # float 2d array

    #plotName = 'ezCon381antXTByFreqAvg.png'
    plotName = 'ezCon381' + antXNameL[0] + 'TByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 381 and 381 <= ezConPlotRangeL[1]:
    if 381 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(antXT, axis=1), 'green',
        antXNameL[1]+'T Average Spectrum')



def plotEzCon382antXTByFreqBinAvgRfi():

    global fileNameLast             # string
    global plotCountdown            # integer
    global titleS                   # string
    global ezConDispGrid            # integer
    global dopplerSpanD2            # float
    global fileFreqMin              # float
    global fileFreqMax              # float
    global fileFreqBinQty           # integer
    global antXNameL                # list of strings
    global antXT                    # float 2d array
    #global antLen                   # integer
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global OutFreqString            # string

    #plotName = 'ezCon382antXTByFreqAvgRfi.png'
    plotName = 'ezCon382' + antXNameL[0] + 'TByFreqAvgRfi.png'
    # for RFI filtering, to help create ezDefaults.txt ezConHideFreqBin arguments, 
    # print freqBin indexes of 5 highest-values of antXTByFreqBinSum

    if 1:
        #print()
        #print(f'  {fileNameLast}  ======================================== Frequency study of AntXT')
        OutFreqStringThis = \
            f'\n  {fileNameLast}  ======================================== Frequency study of AntXT\n'

        antXTByFreqBinSumAvg = np.mean(antXT, axis=1)
        antXTByFreqBinSumAvgMin = min(antXTByFreqBinSumAvg)
        antXTByFreqBinSumAvgMax = max(antXTByFreqBinSumAvg)
        antXTByFreqBinSumAvgSpanD100 \
            = (antXTByFreqBinSumAvgMax - antXTByFreqBinSumAvgMin) / 100.

        #print()
        #print(' FreqBin indexes of 5 highest-values of ' + antXNameL[1] + 'T:')
        OutFreqStringThis += f'\n FreqBin indexes of 5 highest-values of {antXNameL[1]}T:\n'
        antXTByFreqBinSumAvgIdxbyValueHigh5 = np.array(antXTByFreqBinSumAvg).argsort()[::-1][:5]
        for i in range(len(antXTByFreqBinSumAvgIdxbyValueHigh5)):
            antXTByFreqBinSumAvgThis = \
                antXTByFreqBinSumAvg[antXTByFreqBinSumAvgIdxbyValueHigh5[i]]
            antXTByFreqBinSumAvgThisPercent = \
                (antXTByFreqBinSumAvgThis - antXTByFreqBinSumAvgMin) / antXTByFreqBinSumAvgSpanD100
            #print(' i =', i,
            #    '      FreqBin =', antXTByFreqBinSumAvgIdxbyValueHigh5[i],
            #    '      '+antXNameL[1]+'TByFreqBinSumAvg =', antXTByFreqBinSumAvgThis,
            #    '      ', (antXTByFreqBinSumAvgThis - antXTByFreqBinSumAvgMin) \
            #    / antXTByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antXTByFreqBinSumAvgIdxbyValueHigh5[i]}' \
                + f'       {antXNameL[1]}TByFreqBinSumAvg = {antXTByFreqBinSumAvgThis}' \
                + f'       ' \
                + f'{(antXTByFreqBinSumAvgThis - antXTByFreqBinSumAvgMin) / antXTByFreqBinSumAvgSpanD100} %'
            if antXTByFreqBinSumAvgThisPercent < 95:
                OutFreqStringThis += '  <=========== < 95%\n'
            else:
                OutFreqStringThis += '\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antXTByFreqBinSumAvgIdxbyValueHigh5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antXTByFreqBinSumAvgIdxbyValueHigh5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 lowest-values of ' + antXNameL[1] + 'T:')
        OutFreqStringThis += f'\n FreqBin indexes of 5 lowest-values of {antXNameL[1]}T:\n'
        antXTByFreqBinSumAvgIdxbyValueLow5 = np.array(antXTByFreqBinSumAvg).argsort()[:5]
        for i in range(len(antXTByFreqBinSumAvgIdxbyValueLow5)):
            antXTByFreqBinSumAvgThis = \
                antXTByFreqBinSumAvg[antXTByFreqBinSumAvgIdxbyValueLow5[i]]
            #print(' i =', i,
            #    '      FreqBin =', antXTByFreqBinSumAvgIdxbyValueLow5[i],
            #    '      '+antXNameL[1]+'TByFreqBinSumAvg =', antXTByFreqBinSumAvgThis,
            #    '      ', (antXTByFreqBinSumAvgThis - antXTByFreqBinSumAvgMin) \
            #    / antXTByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antXTByFreqBinSumAvgIdxbyValueLow5[i]}' \
                + f'       {antXNameL[1]}TByFreqBinSumAvg = {antXTByFreqBinSumAvgThis}' \
                + f'       ' \
                + f'{(antXTByFreqBinSumAvgThis - antXTByFreqBinSumAvgMin) / antXTByFreqBinSumAvgSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antXTByFreqBinSumAvgIdxbyValueLow5[0])
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antXTByFreqBinSumAvgIdxbyValueLow5[0]}\n'

        #print()
        #print(' FreqBin indexes of 5 largest change values of ' + antXNameL[1] + 'T:')
        OutFreqStringThis += f'\n FreqBin indexes of 5 largest change values of {antXNameL[1]}T:\n'
        antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1 \
            = np.array(abs(antXTByFreqBinSumAvg[1:] - antXTByFreqBinSumAvg[:-1])).argsort()[::-1][:5]
        for i in range(len(antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1)):
            antXTByFreqBinSumAvgDeltaThis = \
                antXTByFreqBinSumAvg[antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1] \
                - antXTByFreqBinSumAvg[antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i]]
            #print(' i =', i,
            #    '      FreqBin =', antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1,
            #    '      '+antXNameL[1]+'TByFreqBinSumAvgDelta =', antXTByFreqBinSumAvgDeltaThis,
            #    '      ', antXTByFreqBinSumAvgDeltaThis / antXTByFreqBinSumAvgSpanD100, '%')
            OutFreqStringThis += f' i = {i}' \
                + f'       FreqBin = {antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1[i] + 1}' \
                + f'       {antXNameL[1]}TByFreqBinSumAvgDelta = {antXTByFreqBinSumAvgDeltaThis}' \
                + f'       {antXTByFreqBinSumAvgDeltaThis / antXTByFreqBinSumAvgSpanD100} %\n'
        #print('                 Maybe try arguments like    -ezConRawFreqBinHide',
        #    antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1[0] + 1)
        OutFreqStringThis += '                 Maybe try arguments like    -ezConRawFreqBinHide' \
            + f' {antXTByFreqBinSumAvgIdxbyValueDeltaHigh5m1[0] + 1}'
        print(OutFreqStringThis)
        OutFreqString += '\n\n\n\n' + OutFreqStringThis

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 382 and 382 <= ezConPlotRangeL[1]:
    if 382 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    # calculate average by Freq Bin and plot by Doppler
    plt.plot(antXTByFreqBinSumAvg, range(fileFreqBinQty), 'green')

    plt.title(titleS)
    plt.grid(1)

    plt.xlabel(antXNameL[1]+'T Average Spectrum')
    # 2% of the data span as a spacing on each end
    plt.xlim(antXTByFreqBinSumAvgMin - 2 * antXTByFreqBinSumAvgSpanD100,
        antXTByFreqBinSumAvgMax + 2 * antXTByFreqBinSumAvgSpanD100)

    yTick382Locs   = []
    yTick382Labels = []
    dopplerSpan = fileFreqMax - fileFreqMin
    dopplerSpanD2 = dopplerSpan / 2.
    for i in range(21):
        yTick382LocsIInt = int(fileFreqBinQty * i / 20.)
        yTick382Locs.append(yTick382LocsIInt)
        # below widths assume dopplerSpan < 20 MHz
        # allow for width of negative Doppler '-' character
        dopplerThis = dopplerSpan * i / 20. - dopplerSpanD2
        if dopplerThis < 0.:
            yTick382Labels.append(f'{yTick382LocsIInt:d}  {i / 20.:0.2f}  {dopplerThis:0.2f}')
        else:
            yTick382Labels.append(f'{yTick382LocsIInt:d}  {i / 20.:0.2f}   {dopplerThis:0.2f}')

    plt.yticks(yTick382Locs, yTick382Labels)
    #plt.ylabel('Frequency Bin and Spectrum Fraction')
    plt.ylabel('Frequency Bin, Spectrum Fraction, and Doppler')
    #plt.ylim(0, fileFreqBinQty)
    plt.ylim(fileFreqBinQty * 1.001, 0)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon383antXTVByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTV                   # float 2d array

    #plotName = 'ezCon383antXTVByFreqAvg.png'
    plotName = 'ezCon383' + antXNameL[0] + 'TVByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 383 and 383 <= ezConPlotRangeL[1]:
    if 383 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(antXTV, axis=1), 'green',
        antXNameL[1]+'TV Average Spectrum')



def plotEzCon387antXTVTByFreqBinAvg():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTVT                  # float 2d array

    #plotName = 'ezCon387antXTVTByFreqAvg.png'
    plotName = 'ezCon387' + antXNameL[0] + 'TVTByFreqAvg.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 387 and 387 <= ezConPlotRangeL[1]:
    if 387 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.mean(antXTVT, axis=1), 'green',
        antXNameL[1]+'TVT Average Spectrum')



def plotEzCon388antBTVTByFreqBinAvgAll():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTVT                  # float 2d array

    global byFreqBinX               # float array
    global ezConDispGrid            # integer
    global dopplerSpanD2            # float

    #plotName = 'ezCon388antBTVTByFreqAvgAll.png'
    plotName = 'ezCon388' + antXNameL[0] + 'TVTByFreqAvgAll.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 388 and 388 <= ezConPlotRangeL[1]:
    if 388 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    #antXTVTDLen = 100                           # maximum quantity of spectra after downsampling
    antXTVTDLenMax = 100                        # maximum quantity of spectra after downsampling
    antXTVTDLen = min(antLen, antXTVTDLenMax)   # quantity of spectra after downsampling
    colorPenSL = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey']

    # no downsampling
    #for n in range(antLen):
    #    plt.plot(byFreqBinX, antXTVT[:, n], colorPenSL[n % 9], linewidth=0.5)

    # true downsampling, using the slicing notation of start:stop:step ("Decimation" ?)
    #antXTVTD = antXTVT[:, ::downsamplingStep]

    # downsampling by averaging
    # (// is floor division)
    downsamplingStep = antLen // antXTVTDLen

    antXTVTD = np.empty_like(antXTVT[:, :antXTVTDLen])
    for n in range(antXTVTDLen):
        downsamplingIndex = n * downsamplingStep
        antXTVTD[:, n] = np.mean(antXTVT[:, downsamplingIndex:downsamplingIndex+downsamplingStep], axis=1)

    for n in range(len(antXTVTD[0, :])):
        plt.plot(byFreqBinX, antXTVTD[:, n], colorPenSL[n % 9], linewidth=0.5)

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel('Doppler (MHz)')
    plt.xlim(-dopplerSpanD2, dopplerSpanD2)

    plt.ylabel(antXNameL[1]+'TVT Spectra')
    plt.ylabel(antXNameL[1]+'TVT Spectra, Downsampled by Averaging')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon393antXTVByFreqBinMax():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTV                   # float 2d array

    #plotName = 'ezCon393antXTVByFreqMax.png'
    plotName = 'ezCon393' + antXNameL[0] + 'TVByFreqMax.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 393 and 393 <= ezConPlotRangeL[1]:
    if 393 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.amax(antXTV, axis=1), 'green',
        antXNameL[1]+'TV Maximum Spectrum')



def plotEzCon397antBTVTByFreqBinMax():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTVT                  # float 2d array

    #plotName = 'ezCon397antBTVTByFreqMax.png'
    plotName = 'ezCon397' + antXNameL[0] + 'TVTByFreqMax.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 397 and 397 <= ezConPlotRangeL[1]:
    if 397 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, np.amax(antXTVT, axis=1), 'green',
        antXNameL[1]+'TVT Maximum Spectrum')



def plotEzCon398antBTVTByFreqBinMaxAll():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast             # string
    global plotCountdown            # integer
    global antXNameL                # list of strings
    global antXTVT                  # float 2d array

    global byFreqBinX               # float array
    global ezConDispGrid            # integer
    global dopplerSpanD2            # float

    #plotName = 'ezCon398antBTVTByFreqMaxAll.png'
    plotName = 'ezCon398' + antXNameL[0] + 'TVTByFreqMaxAll.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 398 and 398 <= ezConPlotRangeL[1]:
    if 398 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    #antXTVTMaxDLen = 100                                # quantity of spectra after downsampling
    antXTVTMaxDLenMax = 100                             # maximum quantity of spectra after downsampling
    antXTVTMaxDLen = min(antLen, antXTVTMaxDLenMax)     # quantity of spectra after downsampling

    colorPenSL = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey']

    # no downsampling
    #for n in range(antLen):
    #    plt.plot(byFreqBinX, antXTVT[:, n], colorPenSL[n % 9], linewidth=0.5)

    # true downsampling, using the slicing notation of start:stop:step ("Decimation" ?)
    #antXTVTD = antXTVT[:, ::downsamplingStep]

    # downsampling by maximizing
    # (// is floor division)
    downsamplingStep = antLen // antXTVTMaxDLen

    antXTVTMaxD = np.empty_like(antXTVT[:, :antXTVTMaxDLen])
    for n in range(antXTVTMaxDLen):
        downsamplingIndex = n * downsamplingStep
        antXTVTMaxD[:, n] = np.amax(antXTVT[:, downsamplingIndex:downsamplingIndex+downsamplingStep], axis=1)

    for n in range(len(antXTVTMaxD[0, :])):
        plt.plot(byFreqBinX, antXTVTMaxD[:, n], colorPenSL[n % 9], linewidth=0.5)

    plt.title(titleS)
    plt.grid(ezConDispGrid)

    plt.xlabel('Doppler (MHz)')
    plt.xlim(-dopplerSpanD2, dopplerSpanD2)

    plt.ylabel(antXNameL[1]+'TVTMax Spectra, Downsampled by Maximizing')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon399SignalSampleByFreqBin():

    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list
    global fileNameLast                     # string
    global plotCountdown                    # integer
    global ezCon399SignalSampleByFreqBinL   # integer list
    global ezCon399SignalSampleByFreqBin1d  # float list or numpy
    global antXNameL                        # list of strings

    plotCountdown -= 1

    #if 399 < ezConPlotRangeL[0] or ezConPlotRangeL[1] < 399:
    if 399 not in ezConPlotRequestedL:
        return(1)

    ezCon399SignalSampleByFreqBinL[1] = min(ezCon399SignalSampleByFreqBinL[1], antLen)
    ezCon399SampleS = str(ezCon399SignalSampleByFreqBinL[1])

    if ezCon399SignalSampleByFreqBinL[0] == 10:
        plotName = 'ezCon399AntByFreq' + ezCon399SampleS + '.png'
        plotColorS = 'blue'
        plotYLabel = 'Ant Spectrum, Sample ' + ezCon399SampleS
    elif ezCon399SignalSampleByFreqBinL[0] == 12:
        plotName = 'ezCon399RefByFreq' + ezCon399SampleS + '.png'
        plotColorS = 'violet'
        plotYLabel = 'Ref Spectrum, Sample ' + ezCon399SampleS
    elif ezCon399SignalSampleByFreqBinL[0] == 14:
        plotName = 'ezCon399AntBByFreq' + ezCon399SampleS + '.png'
        plotColorS = 'red'
        plotYLabel = 'AntB Spectrum, Sample ' + ezCon399SampleS
    elif ezCon399SignalSampleByFreqBinL[0] == 16:
        plotName = 'ezCon399AntRBByFreq' + ezCon399SampleS + '.png'
        plotColorS = 'orange'
        plotYLabel = 'AntRB Spectrum, Sample ' + ezCon399SampleS
    else:
        # ezCon399SignalSampleByFreqBinL[0] == 18
        plotName = 'ezCon399' + antXNameL[1] + 'TVTByFreq' + ezCon399SampleS + '.png'
        plotColorS = 'green'
        plotYLabel = antXNameL[1] + 'TVT Spectrum, Sample ' + ezCon399SampleS

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plotEzCon1dByFreqBin(plotName, ezCon399SignalSampleByFreqBin1d, plotColorS, plotYLabel)

    # free ezCon399SignalSampleByFreqBin1d memory
    ezCon399SignalSampleByFreqBin1d = []
    ezCon399SignalSampleByFreqBin1d = None
    del ezCon399SignalSampleByFreqBin1d



#A#################################################################################################



def plotEzCon510velGLon():

    global fileNameLast             # string
    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezConDispGrid            # integer
    global fileFreqBinQty           # integer
    global freqStep                 # float
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon510velGLon.png'

    plotCountdown -= 1

    # if anything in velGLonP180 to save or plot
    #if ezConPlotRangeL[0] <= 510 and 510 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (510 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

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

    plt.axhline(y = 0, linewidth=0.5, color='black')
    plt.axvline(x =  90, linewidth=0.5, color='black')
    plt.axvline(x =   0, linewidth=0.5, color='black')
    plt.axvline(x = -90, linewidth=0.5, color='black')

    cbar = plt.colorbar(pts, orientation='vertical', pad=0.06)

    plt.title(titleS)
    #plt.grid(ezConDispGrid)
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    plt.xlim(180, -180)        # in degrees
    plt.xticks([  180,   90,   0,   -90,   -180],
               [ '180', '90', '0', '-90', '-180'])

    plt.ylim(-velocitySpanMax, velocitySpanMax)        # in velocity

    plt.ylabel('Interpolated Velocity (km/s) by Galactic Longitude' \
        + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
        + f' Nonzero = {velGLonP180CountNonzero} of {len(velGLonP180Count)}',
        rotation=90, verticalalignment='bottom')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon519velGLonCount():

    global fileNameLast             # string
    global plotCountdown            # integer
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezConDispGrid            # integer
    global fileFreqBinQty           # integer
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon519velGLonCount.png'

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    #if ezConPlotRangeL[0] <= 519 and 519 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (519 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()
    plt.plot(np.arange(-180, +181, 1), velGLonP180Count)

    plt.title(titleS)
    #plt.grid(ezConDispGrid)
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    plt.xlim(180, -180)        # in degrees
    plt.xticks([  180,   90,   0,   -90,   -180],
               [ '180', '90', '0', '-90', '-180'])

    # if any Galactic plane crossings, velGLonP180 has been (partially?) filled with averages
    velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
    print(' velGLonP180CountNonzero =', velGLonP180CountNonzero, 'of', len(velGLonP180Count) )
    print()

    plt.ylabel('Velocity Data Counts by Galactic Longitude' \
        + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
        + f' Nonzero={velGLonP180CountNonzero} of {len(velGLonP180Count)}')
    #    rotation=90, verticalalignment='bottom')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')


    # print out velGLonCount status
    fileWriteGLonName = 'ezCon519velGLonCount.txt'
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
        print('\a')     # ring bell
        exit()


    fileWriteGLonHashS = '########################################' \
        + '########################################'                        # 40 + 40 = 80 '#'

    fileWriteGLon.write('\ngLonDeg   velGLonCount   gLonDegForHaystackSrt.cmd        (RtoL)\n\n')

    for gLonP180 in range(180):                               # for every column, RtoL, 0 thru 179
        fileWriteGLonS = f'{gLonP180 - 180:4d}  {velGLonP180Count[gLonP180]:5d}  {gLonP180 + 180:4d}  ' \
            + fileWriteGLonHashS[:velGLonP180Count[gLonP180]] + '\n'
        fileWriteGLon.write(fileWriteGLonS)

    # for the gLonDeg == 0000 column
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



def plotEzCon520velGLonPolar():

    global fileNameLast             # string
    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezConDispGrid            # integer
    global fileFreqBinQty           # integer
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon520velGLonPolar.png'     # Velocity by Galactic Longitude with pcolormesh

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    #if ezConPlotRangeL[0] <= 520 and 520 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (520 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()
    
    #    # https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_demo.html
    #    # https://matplotlib.org/stable/gallery/pie_and_polar_charts/polar_scatter.html
    # https://stackoverflow.com/questions/36513312/polar-heatmaps-in-python
    fig = plt.figure()
    ax = fig.add_subplot(projection='polar')

    rad = np.arange(0, fileFreqBinQty, 1)        # 0 to fileFreqBinQty in freqBins
    azm = np.linspace(0, np.pi + np.pi, 361, endpoint=True)

    r, theta = np.meshgrid(rad, azm)
    plt.grid(0)
    im = plt.pcolormesh(theta, r, velGLonP180.T, cmap=plt.get_cmap('gnuplot'), shading='auto')

    fig.colorbar(im, ax=ax, pad=0.1)

    polarPlot = plt.plot(azm, r, color='black', linestyle='none')
    plt.grid(1)

    plt.title(titleS)

    ax.set_rgrids((fileFreqBinQty/2.,), ('',))
    ax.set_theta_zero_location('S', offset=0.)
    ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

    ax.set_xlabel('Galactic Longitude (degrees) of Spectra')
    ax.set_ylabel('Radius Is Increasing "Velocity",\n\n' \
        + 'Radius Is Increasing Receding,\n\n' \
        + 'Radius Is Decreasing Doppler\n\n')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon529velGLonPolarCount():

    global fileNameLast             # string
    global plotCountdown            # integer
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global titleS                   # string
    global ezConDispGrid            # integer
    global fileFreqBinQty           # integer
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon529velGLonPolarCount.png'     # Velocity by Galactic Longitude with pcolormesh

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    #if ezConPlotRangeL[0] <= 529 and 529 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (529 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

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

    plt.grid(0)
    im = plt.pcolormesh(theta, r, velGLonP180CountPolar, cmap=plt.get_cmap('gnuplot'), shading='auto')

    fig.colorbar(im, ax=ax, pad=0.1)

    polarPlot = plt.plot(azm, r, color='black', linestyle='none')
    plt.grid(1)

    plt.title(titleS)

    ax.set_rgrids((fileFreqBinQty/2.,), ('',))
    ax.set_theta_zero_location('S', offset=0.)
    ax.set_thetagrids((90, 180, 270, 360), ('-90', '0', '90', '180 and -180'))

    ax.set_xlabel('Galactic Longitude (degrees) of Spectra')
    velGLonP180CountNonzero = np.count_nonzero(velGLonP180Count)
    ax.set_ylabel('Velocity Data Counts by Galactic Longitude' \
        + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
        + f' Nonzero={velGLonP180CountNonzero} of {len(velGLonP180Count)}\n\n')
    #        ax.set_ylabel('Velocity Data Counts by Galactic Longitude' \
    #            + f'\nVelocity Count: Sum={velGLonP180CountSum:,}' \
    #            + f' Nonzero={velGLonP180CountNonzero} of {len(velGLonP180Count)}')
    #        #    rotation=90, verticalalignment='bottom')

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon530galDecGLon():

    global fileNameLast             # string
    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer
    global galDecP90GLonP180Count   # integer array

    global titleS                   # string
    global ezConDispGrid            # integer
    global fileFreqBinQty           # integer
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon530galDecGLon.png'

    plotCountdown -= 1

    # if anything in velGLonP180 to plot
    #if ezConPlotRangeL[0] <= 530 and 530 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (530 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)
    
    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

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
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    plt.xlim(180, -180)        # in degrees
    plt.xticks([  180,   90,   0,   -90,   -180],
               [ '180', '90', '0', '-90', '-180'])

    plt.ylabel('Velocity Counts on Declination by Galactic Longitude' \
        + f'\nVelocity Count Sum = {velGLonP180CountSum:,}',
        rotation=90, verticalalignment='bottom')
    plt.ylim(0, 180)                # in decP90
    plt.yticks([ 0,     30,    60,    90,  120,  150,  180],
               [ '-90', '-60', '-30', '0', '30', '60', '90'])

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon541velGLonEdges():

    global fileNameLast             # string
    global plotCountdown            # integer
    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global ezConVelGLonEdgeFrac     # float
    global ezConVelGLonEdgeLevel    # float

    global titleS                   # string
    global ezConDispGrid            # integer
    global fileFreqBinQty           # integer
    global dopplerSpanD2            # float
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon541velGLonEdges.png'

    plotCountdown -= 1

    # If anything in velGLonP180 to plot.
    #if ezConPlotRangeL[0] <= 541 and 541 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if 541 in ezConPlotRequestedL and velGLonP180CountSum:

        print()
        print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

        plt.clf()

        print(' ezConVelGLonEdgeFrac  =', ezConVelGLonEdgeFrac)
        print(' ezConVelGLonEdgeLevel =', ezConVelGLonEdgeLevel)

        velGLonP180Max = velGLonP180.max()
        velGLonP180Min = velGLonP180.min()
        # if ezConVelGLonEdgeLevel not 0, then ezConVelGLonEdgeFrac ignored
        if ezConVelGLonEdgeLevel:
            velGLonEdgeLevel = ezConVelGLonEdgeLevel
        else:
            velGLonEdgeLevel = ezConVelGLonEdgeFrac * (velGLonP180Max - velGLonP180Min) + velGLonP180Min
        print('                         velGLonP180Max   =', velGLonP180Max)
        print('                         velGLonEdgeLevel =', velGLonEdgeLevel)
        print('                         velGLonP180Min   =', velGLonP180Min)

        velGLonUEdgeFreqBin = np.full(361, np.nan)      # unused nan will not plot
        velGLonLEdgeFreqBin = np.full(361, np.nan)      # unused nan will not plot
        
        # for Galactic plane crossings, velGLonUEdge will be the max velocity vs Galactic Longitude.
        # Page 46 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/
        #   Radioastro_21cm_2012b.pdf
        #   says the max Galactic velocity around Galactic center
        #   = galGalMax
        #   = velGLonUEdge + (earth Galactic rotation speed) * sin(gLon)
        #   = velGLonUEdge + (218 km/s)                      * sin(gLon)
        galGalMax = np.full(361, np.nan)      # unused nan will not plot

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
        plt.grid(0)

        plt.xlabel('Galactic Longitude (degrees)')
        plt.xlim(180, -180)        # in degrees
        plt.xticks([  180,   90,   0,   -90,   -180],
                   [ '180', '90', '0', '-90', '-180'])

        ylabelS = 'Velocity Edge: Upper (Red) and Lower (Blue) (km/s)'
        # if ezConVelGLonEdgeLevel not 0, then ezConVelGLonEdgeFrac ignored
        if ezConVelGLonEdgeLevel:
            ylabelS += f'\nezConVelGLonEdgeLevel = {ezConVelGLonEdgeLevel:0.4f}'
        else:
            ylabelS += f'\nezConVelGLonEdge: Frac={ezConVelGLonEdgeFrac:0.4f}'
            ylabelS += f' Level={velGLonEdgeLevel:0.4f}'

        plt.ylabel(ylabelS)
        plt.ylim(-270, 270)

        if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
            os.remove(plotName)
        plt.savefig(plotName, dpi=300, bbox_inches='tight')


    # since need same velGLonUEdge, merged plotEzCon550galRot() into plotEzCon541velGLonEdges()
    #def plotEzCon550galRot():
    plotName = 'ezCon550galRot.png'

    plotCountdown -= 1

    # If anything in velGLonP180 to plot.
    # This ezCon531galRot.png requires ezCon530velGLonEdges.png to run.
    #if ezConPlotRangeL[0] <= 550 and 550 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (550 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    # Status: for Galactic plane crossings, velGLonUEdge are max velocities vs Galactic longitude.
    # Page 46 of https://f1ehn.pagesperso-orange.fr/pages_radioastro/Images_Docs/
    #   Radioastro_21cm_2012b.pdf
    #   says for 0 <= gLon <= 90, the max Galactic velocity around Galactic center
    #   = galGalMax
    #   = galGasGalMax + (earth Galactic rotation speed) * sin(gLon)
    #   = galGasGalMax + (218 km/s)                      * sin(gLon)
    galGasGalMax = np.add(velGLonUEdge[180:180 + 91], 218 * np.sin(np.radians(np.arange(91))))   # in km/s

    # Page 46 also
    #   says for 0 <= gLon <= 90, the Galactic gas radius from Galactic center
    #   = galGasRadius
    #   = (Solar radius from Galactic center)      * sin(gLon)
    #   = (2.6e17 km * (Light year / 9.461e+12 km) * sin(gLon)
    #   = 27481 light years                        * sin(gLon)
    #
    #   = (26000 light years says https://en.wikipedia.org/wiki/Galactic_Center) * sin(gLon)
    galGasRadius = 26000 * np.sin(np.radians(np.arange(91)))            # in light years

    plt.plot(galGasRadius, galGasGalMax, 'g.')

    plt.title(titleS)
    plt.grid(ezConDispGrid)
    plt.xlabel('Gas Radius from Galactic Center (Light Years)')
    plt.xlim(0, 26000)        # radius from 0 to Solar radius from Galactic center (=26000 light years)
    plt.xticks([0,      5000.,   10000.,   15000.,   20000.,   25000.],
               ['0', '5,000', '10,000', '15,000', '20,000', '25,000'])

    ylabelS = 'Gas Max Velocity around Galactic Center (km/s)'
    # if ezConVelGLonEdgeLevel not 0, then ezConVelGLonEdgeFrac ignored
    if ezConVelGLonEdgeLevel:
        ylabelS += f'\nezConVelGLonEdgeLevel = {ezConVelGLonEdgeLevel:0.4f}'
    else:
        ylabelS += f'\nezConVelGLonEdge: Frac={ezConVelGLonEdgeFrac:0.4f}'
        ylabelS += f' Level={velGLonEdgeLevel:0.4f}'
    plt.ylabel(ylabelS)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon800antXTVTMaxIdxGLon():

    global fileNameLast             # string
    global plotCountdown            # integer
    global antXTVT                  # float 2d array

    global titleS                   # string
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    plotName = 'ezCon800' + antXNameL[0] + 'TVTMaxIdxGLon.png'

    plotCountdown -= 1

    #if ezConPlotRangeL[0] <= 800 and 800 <= ezConPlotRangeL[1]:
    if 800 not in ezConPlotRequestedL:
        return(1)

    print()
    print(f'  {fileNameLast}  {plotCountdown} plotting {plotName} ================================')

    plt.clf()

    #velMaxIndex = np.empty(antLen, dtype=int)
    #for n in range(antLen):
    #    velMaxIndex[n] = np.maximum(antXTVT[:, n] = antXTVTThis)    # index of spectrum's max power

    antXTVTMaxIndex = np.argmax(antXTVT, axis=0)          # freqBin-like for each sample's max
    #velMaxIndexY, velMaxIndexX = np.where(antXTVT == velMax)

    # ezConOut[:, 4] is gLon is RtoL from -180 thru 180
    #pts = plt.scatter(ezConOut[:, 4], velMaxIndex-120,
    #    s=1, marker='|', c='green', cmap=plt.get_cmap('gnuplot'))
    #pts = plt.scatter(ezConOut[:, 4]+360., velMaxIndex-120,
    #    s=1, marker='|', c='violet', cmap=plt.get_cmap('gnuplot'))
    #pts = plt.scatter(ezConOut[:, 4], antXTVTMaxIndex,
    #    s=1, marker='|', c='green', cmap=plt.get_cmap('gnuplot'))
    #pts = plt.scatter(ezConOut[:, 4]+360., antXTVTMaxIndex,
    #    s=1, marker='|', c='violet', cmap=plt.get_cmap('gnuplot'))
    pts = plt.scatter(ezConOut[:, 4], antXTVTMaxIndex,
        s=1, marker='|', c='green')
    pts = plt.scatter(ezConOut[:, 4]+360., antXTVTMaxIndex,
        s=1, marker='|', c='red')

    plt.title(titleS)
    plt.grid(0)

    plt.xlabel('Galactic Longitude (degrees)')
    #plt.xlim(180, -180)        # in degrees
    #plt.xlim(-180, 180)        # in degrees
    #plt.xticks([  180,   90,   0,   -90,   -180],
    #           [ '180', '90', '0', '-90', '-180'])
    plt.xlim(0, 360)        # in degrees

    plt.ylabel('Index of ' + antXNameL[1] + 'TVT Spectrum Maximum (increasing freq)')
    #plt.ylim(-270, 270)
    plt.ylim(0, 400)

    if os.path.exists(plotName):    # to force plot file date update, if file exists, delete it
        os.remove(plotName)
    plt.savefig(plotName, dpi=300, bbox_inches='tight')



def plotEzCon690gLonDegByFreqAvg():

    global velGLonP180              # float 2d array
    global velGLonP180Count         # integer array
    global velGLonP180CountSum      # integer

    global fileNameLast             # string
    global plotCountdown            # integer
    global elevationDeg             # float array
    global titleS                   # string
    global ezConDispGrid            # integer
    global byFreqBinX               # float array
    #global ezConPlotRangeL          # integer list
    global ezConPlotRequestedL      # integer list

    # if anything in velGLonP180 to plot
    #if ezConPlotRangeL[0] <= 690 and 690 <= ezConPlotRangeL[1] and velGLonP180CountSum:
    if not (690 in ezConPlotRequestedL and velGLonP180CountSum):
        return(1)

    plotCountdown += np.count_nonzero(velGLonP180Count)

    print()
    print('   plotEzCon690gLonDegByFreqAvg ===============')

    if 1:
        # same ylim for all ezCon690GLonDegP180_nnnByFreqBinAvg plots
        ezCon690yLimMin = 0.95 * velGLonP180.min()
        print(' ezCon690yLimMin =', ezCon690yLimMin)
        # for small antLen, that ezCon690yLimMin may be nan

        ezCon690yLimMax = 1.05 * velGLonP180.max()
        print(' ezCon690yLimMax =', ezCon690yLimMax)
        # for small antLen, that ezCon690yLimMax may be nan

    for gLonP180 in range(361):                 # for every column, RtoL

        if velGLonP180Count[gLonP180]:      # if column used

            plotCountdown -= 1

            # create gLonDegS with form of '+nnn' or '-nnn' degrees
            ## create plotName with form of 'ezCon690GLonDegP180_nnnByFreqBinAvg.png'
            #plotName = f'ezCon690gLonDegP180_{gLonP180:03d}ByFreqAvg.png'
            # create plotName with form of 'ezCon690_nnnGLonDegPnnnByFreqAvg.png'
            #   or                         'ezCon690_nnnGLonDegMnnnByFreqAvg.png'
            if gLonP180 < 180:
                gLonDegS = f'-{180 - gLonP180:03d}'        # '-nnn' with leading zeros
                plotName = f'ezCon690_{gLonP180:03d}gLonDegM{gLonDegS[1:]}ByFreqAvg.png'
            else:
                gLonDegS = f'+{gLonP180 - 180:03d}'        # '+nnn' with leading zeros
                plotName = f'ezCon690_{gLonP180:03d}gLonDegP{gLonDegS[1:]}ByFreqAvg.png'

            print()
            print(f'  {fileNameLast}  {plotCountdown} plotting {plotName}' \
                + ' ================================')
            print(' gLonP180 =', gLonP180)
            print(' gLonP180 - 180 =', gLonP180 - 180)
            print(' velGLonP180Count[gLonP180] =', velGLonP180Count[gLonP180])
            plt.clf()
            
            # velGLonP180 stores increasing velocity, but X axis is increasing freq, so use -byFreqBinX
            plt.plot(-byFreqBinX, velGLonP180[:, gLonP180])

            plt.title(titleS)
            plt.grid(ezConDispGrid)

            plt.xlabel('Doppler (MHz)')
            plt.xlim(-dopplerSpanD2, dopplerSpanD2)

            if 0:
                # new ylim for each ezCon690GLonDegP180_nnnByFreqBinAvg plot
                ezCon690yLimMin = 0.95 * velGLonP180[:, gLonP180].min()
                print(' ezCon690yLimMin =', ezCon690yLimMin)
                # for small antLen, that ezCon690yLimMin may be nan

                ezCon690yLimMax = 1.05 * velGLonP180[:, gLonP180].max()
                print(' ezCon690yLimMax =', ezCon690yLimMax)
                # for small antLen, that ezCon690yLimMax may be nan

            if not np.isnan(ezCon690yLimMin) and not np.isnan(ezCon690yLimMax):
                plt.ylim(ezCon690yLimMin, ezCon690yLimMax)

            plt.ylabel('Average ' + antXNameL[1] + 'TV Spectrum' \
                + '\n\nGalactic Longitude = ' + gLonDegS + ' degrees', \
                rotation=90, verticalalignment='bottom')

            if os.path.exists(plotName): # to force plot file date update, if file exists, delete it
                os.remove(plotName)
            plt.savefig(plotName, dpi=300, bbox_inches='tight')



#A#################################################################################################



def main():

    global raw                      # float 2d array
    global ant                      # float 2d array
    global antB                     # float 2d array
    global ref                      # float 2d array
    global antRA                    # float 2d array
    global antRB                    # float 2d array
    global antX                     # float 2d array
    global antXT                    # float 2d array
    global antXTV                   # float 2d array
    global antXTVT                  # float 2d array
    global antXNameL                # list of strings
    global ezCon399SignalSampleByFreqBinL   # integer list
    global ezCon399SignalSampleByFreqBin1d  # float list or numpy

    global refRawAvg                # float array

    global ezConAntXInput           # integer

    global ezConRawSamplesUseL      # integer list
    global ezConAntSamplesUseL      # integer list
    global ezConAntPluckL           # integer list
    global ezConRawFreqBinHideL     # integer list
    global ezConAntFreqBinSmooth    # float - RFI spur limiter: max muliplier over 4 neighboring freqBin

    global ezConAntXTVTMaxPluckQtyL         # integer list
    global ezConAntXTVTMaxPluckValL         # float list
    global ezConAntXTVTAvgPluckQtyL         # integer list
    global ezConAntXTVTAvgPluckValL         # float list
    global ezConAntXTVTPluckL               # integer list
    global ezConAntXTVTSmooth               # integer
    global ezCon087Csv                      # integer

    global xTickLabelsHeatAntL      # string list
    global xTickLocsAnt             # float array


    startTime = time.time()
    xTickLocsAnt = []               # force new xTickLocsAnt
    xTickLabelsHeatAntL = []        # force new xTickLabelsHeatAntL

    #################################################################################################
    #
    # Plot number system:
    #
    #   0xx         signal processing spectrum         by sample  = explain sig processing progression
    #   1xx .ezb file column                           by sample  = display .ezb file columns output
    #   2xx         signal processing spectrum average by sample  = display sig processing progression details
    #   3xx average signal processing spectrum         by Doppler = display sig spectrum   progression average
    #   4xx galactic plots                             by galactic longitude (mostly)
    #   5xx galactic longitude spectrum plots          by Doppler
    #
    # Trailing asterix (*) indicates plot displays rawLen samples
    # Numbers is parentheses indicates plot must be requested (default is 0-199).
    # Numbers is brackets    indicates plot is a duplicate of number in brackets.
    #
    #
    #                               2d      1d Column  Making  Signal        G Crossing
    #                      X Axis = Samples Samples    Samples FreqBins GLon FreqBins
    #    Y Axis                     0xx     1xx        2xx     3xx      4xx  5xx
    #    ================           ======= ========== ======= ======== ==== ==========
    #    rawRaw                     000*               200*    300
    #    raw                        001*               201A*   301
    #
    #    if ezConRefMode == 20:
    #      rawAntAvg                                   201B*
    #      rawAvgRecentFrac                            201C*
    #      sampleRef                                   201D*
    #      sampleRefAgain                              201E*
    #      sampleBad                                   201F*
    #
    #    rawAntRef                                     201G*
    #
    #    timeUtcMjdDBetweenRaw                         201H*
    #    timeUtcMjdDBetweenAntRaw                      201I
    #    timeUtcMjdDBetweenRefRaw                      201J
    #
    #    timeUtcMjd                         100
    #    raH                                101
    #    decDeg                             102
    #
    #    gLatDeg                            103
    #    gLonDeg                            104
    #
    #    vlsr                               105
    #
    #    count                             (106)
    #    azimuth                            107
    #    elevationDeg                       108
    #    spare3                            (109)
    #
    #
    #    antRaw                    (002)              (202)    302
    #    ant                        007     110[=207]  207     307
    #
    #    antMax                    (017)    111[=217]  217
    #
    #
    #    refRaw                    (022)              (222)    322
    #    ref                        027     112[=227]  227     327
    #
    #    refMax                    (037)    113[=237]  237
    #
    #
    #    antBas                                        241
    #    antB                       047     114[=247]  247     347
    #
    #    antBMax                   (057)    115[=257]  257
    #
    #
    #    antRA                      061                261     361
    #    antRABas                                      262
    #    antRB                      067     116[=267]  267     367
    #
    #    antRBMax                  (077)    117[=277]  277
    #
    #    antXT                      081                281     381
    #    antXTV                     082                282     382
    #    antXTVT                    087     118[=287]  287     387
    #    antXTRfi                                              388
    #
    #    antXTVTMax                (097)    119[=297]  297
    #
    #    sigProg                            191
    #
    #    velGLon                                                        410
    #    velGLonCount                                                   411
    #    velGLonPolar                                                   412
    #    galDecGLon                                                     420
    #
    #    velGLonEdges                                                   430
    #    galRot                                                         431
    #
    #    gLon_nnnByFreqBinAvg                                                590
    #
    #################################################################################################

    #################################################################################################
    # start with    ant[fileFreqBinQty, n]
    #               ref[fileFreqBinQty, n]
    #
    # end with      ant[fileFreqBinQty, n]     antAvg[n]     antMax[n]   antBaseline[n]
    #              antB[fileFreqBinQty, n]    antBAvg[n]    antBMax[n]
    #               ref[fileFreqBinQty, n]     refAvg[n]     refMax[n]
    #             antRA[fileFreqBinQty, n]   antRAAvg[n]               antRABaseline[n]
    #             antRB[fileFreqBinQty, n]   antRBAvg[n]   antRBMax[n]
    #             antXT[fileFreqBinQty, n]   antXTAvg[n]
    #            antXTV[fileFreqBinQty, n]  antXTVAvg[n]  antXTVMax[n]
    #################################################################################################
    #         antRBAvg[n]  vs   antXTAvg[n] ??????????????
    #################################################################################################
    # Status:
    # Also have dataTimeUtc[n] azimuthDeg[n] elevationDeg[n] 
    #   fileFreqMin fileFreqMax fileNameLast
    #   freqCenter dopplerSpanD2 freqStep ezConOut[n, 18]
    #################################################################################################

    #################################################################################################
    #
    #      Study of Global Data Array Lifetimes, to Reduce Memory Requirements
    #
    #                  ***  ***** * * = plots which display rawLen samples
    # a
    # r               r             t
    # r               e             i
    # a               a    c      r m                                                                      
    # y               d    r      a e                                    a       a e                      
    #                 D    e      w B       a                r           n       n z                       s
    # d               a    a      A e   a   n       a    r   e           t       t C                   a   i
    # i               t    t      n t   n   t       n    e   f       a   Ra   a  X o                   n   g
    # m               a    e      t w   t   H       ta   f   H       n   An   n  T n                   t   P
    # e               Dr   R      R e   R   i   a   Bn   R   i   r   t   Bt   t  R O                   X   r   v
    # n               ia   e      e e   a   d   n   at   a   d   e   R   aR   X  f u                   T   oae e
    # s               rw   f      f n   w   e   t   sB   w   e   f   A   sB   T  i t                   V   gzl l
    # i            {  |012 |11111 1 111 012 012 012 1012 012 012 012 012 1012 0122 |333333333333333333 012 144 |
    # o     plot # {  |000 |00000 0 000 111 111 111 2222 333 333 333 444 4444 4444 |000000000011111111 444 999 |
    # n            {  |111 |55555 8 999 000 111 222 3444 000 111 222 333 4555 6668 |012345678901234567 777 003 |
    # s               |    |ABCDE   ABC                                            |                           |
    #
    # 1 dataTimeUtc   *ooo oooooo o *XX ooo ooo ooo oooo ooo ooo ooo ooo oooo oooo Xoooooooooooooooooo ooo ooo o
    # 1 azimuth       *ooo *ooooo o ooo ooo ooo ooo oooo ooo ooo ooo ooo oooo oooo Xoooooooooooooooooo ooo oX. .
    # 1 elevation     *ooo *ooooo o ooo ooo ooo ooo oooo ooo ooo ooo ooo oooo oooo Xoooooooooooooooooo ooo ooX .
    # 1 rawIndex      .... *ooooo o ooo oX. ... ... .... ... ... ... ... .... .... ................... ... ... .
    #
    # 2 raw           *XXX XXXXXX X XXX ... ... ... .... ... ... ... ... o... .... ................... ... ... .
    # 1 rawAntAvg     .... *ooooo * ooo ooo ooo ooo oooo ooo ooo ooo ooo oooo oooo ooooooooooooooooooo ooo X.. .
    #
    # 1 maskRawAnt    .... *xxxxx X xX. ... ... ... .... ... ... ... ... .... .... ................... ... ... .
    # 1 maskRawRef    .... *xxxxx X xxX ... ... ... .... ... ... ... ... .... .... ................... ... ... .
    #
    # 2 ant           .... *ooooo o ooo *XX *XX *XX Xooo ooo ooo ooo X.. .... .... ................... ... ... .
    # 1 antRawAvg     .... ...... . ... .*o ooo ooo oooo ooo ooo ooo ooo oooo oooo ooooooooooooooooooo ooo X.. .
    # 1 antAvg        .... ...... . ... ... ... .*. .... ... ... ... *oo oooo oooo X.................. ... ... .
    # 1 antMax        .... ...... . ... ... ... ... .... ... ... ... *oo oooo oooo X.................. ... ... .
    # 1 antBaseline   .... ...... . ... ... ... ... *Xoo ooo ooo ooo ooo oooo oooo ooooooooooooooooooo ooo X.. .
    #
    # 2 antB          .... ...... . ... ... ... ... .*XX ... ... ... ... .... .... ................... ... ... .
    # 1 antBAvg       .... ...... . ... ... ... ... ..*o ooo ooo ooo ooo oooo oooo X.................. ... ... .
    # 1 antBMax       .... ...... . ... ... ... ... ...* ooo ooo ooo ooo oooo oooo X.................. ... ... .
    #
    # 2 ref           .... *ooooo o ooo ooo ooo ooo oooo ooo *oo *XX X.. .... .... ................... ... ... .
    # 1 refRawAvg     .... ...... . ... ... ... ... .... *oo ooo ooo ooo oooo oooo ooooooooooooooooooo ooo X.. .
    # 1 refAvg        .... ...... . ... ... ... ... .... .*. ... ... *oo oooo oooo X.................. ... ... .
    # 1 refMax        .... ...... . ... ... ... ... .... ... ... ... *oo oooo oooo X.................. ... ... .
    #
    # 2 antRA         .... ...... . ... ... ... ... .... ... ... ... *XX XX.. .... ................... ... ... .
    # 1 antRAAvg      .... ...... . ... ... ... ... .... ... ... ... ... .*Xo oooo ooooooooooooooooooo ooo X.. .
    #
    # 1 antRABaseline .... ...... . ... ... ... ... .... ... ... ... ... *Xoo oooo ooooooooooooooooooo ooo X.. .
    #
    # 2 antRB         .... ...... . ... ... ... ... .... ... ... ... ... .*XX X... ................... ... ... .
    # 1 antRBAvg      .... ...... . ... ... ... ... .... ... ... ... ... .... *ooo ooooooooooooooooooo ooo X.. .
    #
    # 2 antXT         .... ...... . ... ... ... ... .... ... ... ... ... .... *ooo X.................. ... ... .
    #
    # 2 ezConOut      .... ...... . ... ... ... ... .... ... ... ... ... .... .... *XXXXXXXXXXXXXXXXXX ooo Xoo o
    #
    # 2 antXTV        .... ...... . ... ... ... ... .... ... ... ... ... .... .... *oooooooooooooooooo XXX ooo o
    #
    #################################################################################################


    printHello()
    
    ezConArguments()

    print('\n Python sys.version =', sys.version)
    print('\n matplotlib.__version__ =', matplotlib.__version__)

    readDataDir()   # creates ezRAObsLat, ezRAObsLon, ezRAObsAmsl, ezRAObsName
                    #   fileFreqMin, fileFreqMax, fileFreqBinQty, 
                    #   azimuthDeg, elevationDeg, dataFileIdx, dataTimeUtc, raw, rawLen, fileNameLast

    #openFileSdre()          # In case it will eventually error.  Creates fileWriteNameSdre, fileWriteSdre
    openFileEzb()           # In case it will eventually error.  Creates fileWriteNameEzb, fileWriteEzb
    openFileStudy()         # In case it will eventually error.  Creates fileWriteNameStudy, fileWriteStudy

    rawPlotPrep()                       # creates rawLenM1, freqStep, dopplerSpanD2, freqCenter,
                                        #   titleS, yTickHeatL, byFreqBinX

    # Create signals and plot.
    # Full sized signal histories (used in heatmaps) are large, so delete them promptly.

    # if any raw filtering, plot rawRaw before the filtering
    #if ezConRawSamplesUseL or ezConRawSamplePluckL or ezConRawAvgTrimFracL or ezConRawFreqBinHideL \
    #    or ezConRawFreqBinSmooth:
    if ezConRawFreqBinHideL:
            plotEzCon000rawRaw()                # rawRaw heatmap
            plotEzCon200rawRawAvg()
            plotEzCon300rawRawByFreqBinAvg()

    #if ezConRawSamplesUseL or ezConRawSamplePluckL:
    #    ezConRawSamplesUseLDo()

    #if ezConRawAvgTrimFracL:
    #    ezConRawAvgTrimFracLDo()

    if ezConRawFreqBinHideL:
        ezConRawFreqBinHideLDo()

    #if ezConRawFreqBinSmooth:
    #    ezConRawFreqBinSmoothDo

    plotEzCon001raw()                           # raw heatmap
    plotEzCon201ArawAvg()
    plotEzCon301rawByFreqBinAvg()

    createRef()                         # creates ant, ref, maskRawAnt, maskRawRef
    ####plotEzCon201BrawAntAvg()
    ####plotEzCon201BrawAntAvgRecentFrac()
    ####plotEzCon201DsampleRef()
    ####plotEzCon201EsampleRefAgain()
    ####plotEzCon201FsampleBad()
    ####plotEzCon201GrawAntRef()                    # using raw, maskRawAnt and maskRawRef
    ####plotEzCon201HtimeUtcMjdDBetweenRaw()        # using raw and dataTimeUtc
    ####plotEzCon201ItimeUtcMjdDBetweenAntRaw()     # using raw, dataTimeUtc, and maskRawAnt
    ####plotEzCon201JtimeUtcMjdDBetweenRefRaw()     # using raw, dataTimeUtc, and maskRawRef
    # free raw memory
    raw = []
    raw = None
    del raw


    ####### ant

    # if any ant filtering, plot antRaw before the filtering
    #if ezConAntSamplesUseL or ezConAntPluckL or ezConAntAvgPluckFracL or ezConAntFreqBinHideL \
    #    or ezConAntFreqBinSmooth:
    if ezConAntSamplesUseL or ezConAntPluckL or ezConAntFreqBinSmooth or ezConAntAvgPluckQtyL or ezConAntAvgPluckFracL:
            plotEzCon002antRaw()
            plotEzCon202antRawAvg()
            plotEzCon302antRawByFreqBinAvg()

    #if ezConAntSamplesUseL or ezConAntPluckL:
    if ezConAntSamplesUseL:
        ezConAntSamplesUseLDo()

    if ezConAntAvgPluckQtyL:
        ezConAntAvgPluckQtyLDo()

    if ezConAntAvgPluckFracL:
        ezConAntAvgPluckFracLDo()

    #if ezConAntFreqBinHideL: ???????????????????????
    #    ezConAntFreqBinHideLDo()

    if ezConAntFreqBinSmooth < 999998.:
        ezConAntFreqBinSmoothDo()

    if ezConAntPluckL:
        ezConAntPluckLDo()

    plotEzCon201ZantFileIndex()

    plotEzCon007ant()
    plotEzCon207antAvg()                # creates antAvg
    plotEzCon307antByFreqBinAvg()
    plotEzCon317antByFreqBinMax()

    plotEzCon017antMax2d()
    plotEzCon217antMax()                # creates antMax


    ####### ref

    refRawAvg = np.mean(ref, axis=0)            # creation,  needed for plotEzCon191sigProg()

    # if any ref filtering, plot refRaw before the filtering
    #if ezConRefAvgPluckQtyL or ezConRefAvgPluckFracL or ezConRefFreqBinHideL or ezConRefFreqBinSmooth:
    if ezConRefAvgPluckQtyL or ezConRefAvgPluckFracL:
            plotEzCon022refRaw()
            plotEzCon222refRawAvg()
            plotEzCon322refRawByFreqBinAvg()

    #if ezConRefFreqBinHideL: ?????????????????????
    #    ezConRefFreqBinHideLDo()

    #if ezConRefFreqBinSmooth:
    #    ezConRefFreqBinSmoothDo()

    if ezConRefAvgPluckQtyL:
        ezConRefAvgPluckQtyLDo()

    if ezConRefAvgPluckFracL:
        ezConRefAvgPluckFracLDo()

    plotEzCon027ref()
    plotEzCon227refAvg()                # creates refAvg
    plotEzCon327refByFreqBinAvg()
    plotEzCon337refByFreqBinMax()

    plotEzCon037refMax2d()
    plotEzCon237refMax()                # creates refMax


    ####### antB

    plotEzCon241antBaseline()           # creates antBaseline

    plotEzCon047antB()                  # creates antB
    plotEzCon247antBAvg()               # creates antBAvg
    plotEzCon347antBByFreqBinAvg()
    plotEzCon357antBByFreqBinMax()

    plotEzCon057antBMax2d()
    plotEzCon257antBMax()               # creates antBMax
    # if antB not needed, free antB memory
    if ezConAntXInput != 4:
        if ezCon399SignalSampleByFreqBinL[0] == 14:
            ezCon399SignalSampleByFreqBin1d = antB[:, ezCon399SignalSampleByFreqBinL[1]]
        antB = []
        antB = None
        del antB


    ####### antRB

    plotEzCon061antRA()                 # creates antRA
    # if ant not needed, free ant memory
    if ezConAntXInput != 0:
        if ezCon399SignalSampleByFreqBinL[0] == 10:
            ezCon399SignalSampleByFreqBin1d = ant[:, ezCon399SignalSampleByFreqBinL[1]]
        ant = []
        ant = None
        del ant
    # if ref not needed, free ref memory
    if ezConAntXInput != 2:
        if ezCon399SignalSampleByFreqBinL[0] == 12:
            ezCon399SignalSampleByFreqBin1d = ref[:, ezCon399SignalSampleByFreqBinL[1]]
        ref = []
        ref = None
        del ref
    plotEzCon261antRAAvg()
    plotEzCon361antRAByFreqBinAvg()

    plotEzCon262antRABaseline()         # creates antRABaseline

    plotEzCon067antRB()                 # creates antRB
    # if antRA not needed, free antRA memory
    if ezConAntXInput != 5:
        antRA = []
        antRA = None
        del antRA
    plotEzCon267antRBAvg()              # creates antRBAvg
    plotEzCon367antRBByFreqBinAvg()
    plotEzCon377antRBByFreqBinMax()

    plotEzCon077antRBMax2d()
    plotEzCon277antRBMax()              # creates antRBMax
    # if antRB not needed, free antRB memory
    if ezConAntXInput != 6:
        if ezCon399SignalSampleByFreqBinL[0] == 16:
            ezCon399SignalSampleByFreqBin1d = antRB[:, ezCon399SignalSampleByFreqBinL[1]]
        antRB = []
        antRB = None
        del antRB


    if not len(ezCon399SignalSampleByFreqBin1d):        # if empty
        if ezCon399SignalSampleByFreqBinL[0] == 10:
            ezCon399SignalSampleByFreqBin1d = ant[:, ezCon399SignalSampleByFreqBinL[1]]
        elif ezCon399SignalSampleByFreqBinL[0] == 12:
            ezCon399SignalSampleByFreqBin1d = ref[:, ezCon399SignalSampleByFreqBinL[1]]
        elif ezCon399SignalSampleByFreqBinL[0] == 14:
            ezCon399SignalSampleByFreqBin1d = antB[:, ezCon399SignalSampleByFreqBinL[1]]
        elif ezCon399SignalSampleByFreqBinL[0] == 16:
            ezCon399SignalSampleByFreqBin1d = antRB[:, ezCon399SignalSampleByFreqBinL[1]]
        # antXTVT does not exist yet

    ####### antX

    # create antX
    if ezConAntXInput == 0:             # use Ant
        antX = ant
        # free ant memory
        ant = []
        ant = None
        del ant
        antXNameL = ['ant', 'Ant']
    elif ezConAntXInput == 2:           # use Ref
        antX = ref
        # free ref memory
        ref = []
        ref = None
        del ref
        antXNameL = ['ref', 'Ref']
    elif ezConAntXInput == 4:           # use AntRB
        antX = antB
        # free antB memory
        antB = []
        antB = None
        del antB
        antXNameL = ['antB', 'AntB']
    elif ezConAntXInput == 5:           # use AntRA
        antX = antRA
        # free antRA memory
        antRA = []
        antRA = None
        del antRA
        antXNameL = ['antRA', 'AntRA']
    elif ezConAntXInput == 6:           # use AntRB
        antX = antRB
        # free antRB memory
        antRB = []
        antRB = None
        del antRB
        antXNameL = ['antRB', 'AntRB']

    plotEzCon081antXT()                 # creates antXT, deletes AntX
    plotEzCon281antXTAvg()              # creates antXTAvg
    plotEzCon381antXTByFreqBinAvg()

    plotEzCon382antXTByFreqBinAvgRfi()

    # now need VLSR, so create partial ezConOut in .ezb format
    # ezbMenu: TimeUtcMjd  RaH  DecDeg  GLatDeg  GLonDeg  VLSR  Count  AzimuthDeg  ElevationDeg  AntXTVTCmDop
    #          0           1    2       3        4        5     6      7           8             9
    #   AntAvg  AntMax    RefAvg  RefMax
    #   10      11        12      13
    #   AntBAvg  AntBMax    AntRBAvg  AntRBMax    AntXTVTAvg  AntXTVTMax
    #   14       15          16        17         18          19
    createEzConOutEzb()                 # using ezConAstroMath, creates partial ezConOut,
                                        # deletes antAvg, antMax, refAvg, refMax,
                                        #   antBAvg, antBMax, antRBAvg, antRBMax


    ####### antXTV

    createAntXTV()                      # creates antXTV

    ####### antXTVT

    createAntXTVT()                     # creates antXTVT, keeps antXTV for Galaxy crossing plots
    if ezConAntXTVTMaxPluckQtyL or ezConAntXTVTMaxPluckValL :
        ezConAntXTVTMaxPluckDo()        # thin ezConOut[:, :], antXTV, antXTVT, antLen, and antLenM1
    if ezConAntXTVTAvgPluckQtyL or ezConAntXTVTAvgPluckValL :
        ezConAntXTVTAvgPluckDo()        # thin ezConOut[:, :], antXTV, antXTVT, antLen, and antLenM1
    if ezConAntXTVTPluckL:
        ezConAntXTVTPluckDo()           # thin ezConOut[:, :], antXTV, antXTVT, antLen, and antLenM1

    # antXTV and antXTVT now filtered
    plotEzCon082antXTV()
    plotEzCon282antXTVAvg()             # creates antXTVAvg
    plotEzCon383antXTVByFreqBinAvg()
    plotEzCon393antXTVByFreqBinMax()

    if ezConAntXTVTSmooth:
        ezConAntXTVTSmoothDo()          # smooth antXTVT heatmap image

    plotEzCon087antXTVT()
    plotEzCon088antBTVTByFreqBinAvgFall()
    plotEzCon287antXTVTAvg()    # creates antXTVTAvg into ezConOut[:, 18], antXTVTCmDop into ezConOut[:, 9]
    plotEzCon387antXTVTByFreqBinAvg()
    plotEzCon388antBTVTByFreqBinAvgAll()
    plotEzCon397antBTVTByFreqBinMax()
    plotEzCon398antBTVTByFreqBinMaxAll()
    plotEzCon800antXTVTMaxIdxGLon()

    plotEzCon097antXTVTMax2d()
    plotEzCon098antBTVTByFreqBinMaxFall()
    plotEzCon297antXTVTMax()            # creates antXTVTMax into ezConOut[:, 19]

    if not len(ezCon399SignalSampleByFreqBin1d):        # if not empty
        ezCon399SignalSampleByFreqBin1d = antXTVT[:, ezCon399SignalSampleByFreqBinL[1]]
    plotEzCon399SignalSampleByFreqBin()


    #writeFileSdre()
    writeFileEzb()


    # plot most ezConOut columns
    plotEzCon100timeUtcMjd()
    plotEzCon101raH()
    plotEzCon102decDeg()
    plotEzCon103gLatDeg()
    plotEzCon104gLonDeg()
    plotEzCon105vlsr()
    #plotEzCon106count()
    plotEzCon107azimuth()               # deletes azimuthDeg
    plotEzCon108elevation()             # deletes elevationDeg
    plotEzCon109antXTVTCmDop()

    plotEzCon110antAvg()
    plotEzCon111antMax()

    plotEzCon112refAvg()
    plotEzCon113refMax()

    plotEzCon114antBAvg()
    plotEzCon115antBMax()

    plotEzCon116antRBAvg()
    plotEzCon117antRBMax()

    plotEzCon118antXTVTAvg()
    plotEzCon119antXTVTMax()


    plotEzCon191sigProg()               # deletes antRawAvg, antBaseline, refRawAvg, antRAAvg, antRABaseline,
                                        #    and antXTVAvg

    #plotEzCon198azimuth()               # deletes azimuthDeg
    #plotEzCon199elevation()             # deletes elevationDeg



    # Global arrays remaining: dataTimeUtc, antXTV, ezConOut

    # save frequency spectrum of each qualifing sample
    writeFileGal()      # save qualifing frequency spectra to Gal.npz (parallel to Galactic plane)
                        # creates fileGalWriteName like 2021_333_00.radGal.npz, velGLonP180,
                        #   velGLonP180Count, velGLonP180CountSum, galDecP90GLonP180Count

    writeFileGLon()     # save qualifing frequency spectra to GLon.npz (perpendicular to Galactic plane)

    writeFileGalRaDecNear() # save qualifing frequency spectra to RGal.npz (inside RaDecNearNearL span)

    # free antXTVT memory
    antXTVT = []
    antXTVT = None
    del antXTVT

    plotEzCon510velGLon()
    plotEzCon519velGLonCount()          # creates ezCon519velGLonCount.txt

    plotEzCon520velGLonPolar()
    plotEzCon529velGLonPolarCount()

    plotEzCon530galDecGLon()

    plotEzCon541velGLonEdges()          # and plotEzCon550galRot()

    #plotEzCon550galRot()

    plotEzCon690gLonDegByFreqAvg()
    writeFileStudy()

    printGoodbye(startTime)



if __name__== '__main__':
  main()

# python3 ../ezRA/ezCon230623a.py  ~/aaaEzRABase/lto16h/data/2021_285_00.rad.txt -exzConGalCrossingGLatCenter23.4 -exzConGalCrossingGLatCenter-43.4 -exzConGalCrossingGLatCenterL-5.015.0201 -ezConAstroMath 1 -ezRAObsName  LTO16  -ezRAObsLat  40.3  -ezRAObsLon  -105.1  -ezRAObsAmsl  1524 -ezConPlotRangeL 191 191

# python3 ../ezRA/ezCon230625a.py  ~/aaaEzRABase/lto16h/data/2021_285_00.rad.txt -exzConGalCrossingGLatCenter23 -exzConGalCrossingGLatCenter-43 -ezConGalCrossingGLonCenterL -5 16 -ezConAstroMath 1 -ezRAObsName  LTO16  -ezRAObsLat  40.3  -ezRAObsLon  -105.1  -ezRAObsAmsl  1524 -ezConPlotRangeL 191 191

# ls -lhtr

# python3 ../ezRA/ezCon230629a.py  /home/a/aaaEzRABase/lto16h/data/2021_171_00.rad.txt  -ezConAstroMath  1  -ezRAObsName  LTO16  -ezRAObsLat  40.3  -ezRAObsLon  -105.1  -ezRAObsAmsl  1524  -ezConPlotRangeL  191  191  -ezConRawFreqBinHide  91

# cat  ezCon240613a.py | grep 'def ' > ezConDef.txt

# a@u22-221222a:~/ezRABase/lto16h$
# python3 ../ezRA/ezCon241021a.py  data/2021_200_00.rad.txt  -ezConPlotRangeL 87 87 -ezCon087Csv 1
# ring3d ezCon087antBTVT.csv
# mv graph3d.png ezCon087antBTVTCsv.png

# a@u22-221222a:~/ezRABase/ifAvgEzCon087csv$
# python3  ../ezRA/ezCon250121a.py  data/2020_124_00.rad.txt  -ezConPlotRangeL 87 87  -ezCon087Csv 2
#  rawLen = 4,546
#  antLen = 2,273
#  refQty = 2,273
#  took 19 seconds = 0.3 minutes



# S:\D5\C\Users\B\Documents\Astronomy\Astronomy Radio\SARA\SARA ezRA\_ezRABase\h1SW>
# py  ..\..\ezCon250121a.py  "LRO-H1(Ptarmigan)_ezCol_SAWB_241003_00_El_54-4_Az_163.txt"  -ezConPlotRangeL 87 87  -ezCon087Csv 2  -ezConUseVlsr 0

# a@u22-221222a:~/ezRABase/hL3d$
# python3  ../ezRA/ezCon250123a.py  data/N0RQV-8230209_00.txt  -ezConAntXTFreqBinsFracL 0 1  -ezConUseVlsr 0  -ezConAntXTVTFreqBinsFracL 0 1  -ezConPlotRangeL 87 87  -ezCon087Csv 1
# ring3d  ezCon087antRBTVTMsh.csv


# S:\D5\C\Users\B\Documents\Astronomy\Astronomy Radio\SARA\SARA ezRA\_ezRABase\hL3d>
# CALL C:\Users\b\Downloads\rinearn_graph_3d_5_6_36b_en\rinearn_graph_3d_5_6_36b_en\bin\ring3d.bat  --config rot.ini  --overwrite  --saveimg rot%~1%.png  --quit  ezGLonAll580.csv

# CALL C:\Users\b\Downloads\rinearn_graph_3d_5_6_36b_en\rinearn_graph_3d_5_6_36b_en\bin\ring3d.bat  ezCon087antRBTVTMsh.csv

# py  ..\..\ezCon250124b.py  data\N0RQV-8230209_00.txt  -ezConUseVlsr 0  -exzConAntXTVTFreqBinsFracL01  -ezConAntXTVTSmooth 1  -ezConPlotRangeL 87 87  -ezCon087Csv 1

# CALL C:\Users\b\Downloads\rinearn_graph_3d_5_6_36b_en\rinearn_graph_3d_5_6_36b_en\bin\ring3d.bat  ezCon087antRBTVTMsh.csv  --config RinearnGraph3DSetting.ini

# python3  ../ezRA/ezCon250302a.py  data/2025_061_00.rad.txt -ezConAntXTFreqBinsFracL 0 1  -ezConAntXTVTFreqBinsFracL 0 1  -ezConPlotRangeL 382 999  -ezConGalRaDecNearNearL 0.8 41.3 1. 1.
# python3  ../ezRA/ezCon250302a.py  data/2025_061_00.rad.txt -ezConAntXTFreqBinsFracL 0 1  -ezConAntXTVTFreqBinsFracL 0 1  -ezConPlotRangeL 382 999  -ezConGalRaDecNearNearL 0.8 41.3 0.1 0.2

# python3  ../ezRA/ezGal250301a.py  *RGal.npz -ezGalPlotRangeL 710 710
# python3  ../ezRA/ezGal250301a.py  *RGal.npz -ezGalPlotRangeL 710 710  -ezGal710LimL -650 250 0.95 1.21


# S:\D5\C\Users\B\Documents\Astronomy\Astronomy Radio\SARA\SARA ezRA\_ezRABase\N0RQV-8>
# py  ..\ezRA\ezCon250326a.py  data\N0RQV-8230209_00.txt  -ezConRawFreqBinHide 128  -ezConAntXTVTFreqBinsFracL 0.35 0.65  -ezConAntXTVTSmooth 2  -ezConPlotRangeL 87 109

