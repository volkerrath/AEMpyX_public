#!/usr/bin/env python3
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:light,ipynb
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# !/usr/bin/env python3
# This script is used for the visualization of AEM data along a flightline. 


# +
import os
import sys
from sys import exit as error
from time import process_time
from datetime import datetime
import warnings
from cycler import cycler

import numpy
import matplotlib
import matplotlib.pyplot

AEMPYX_ROOT = os.environ["AEMPYX_ROOT"]
mypath = [AEMPYX_ROOT+"/aempy/modules/", AEMPYX_ROOT+"/aempy/scripts/"]
for pth in mypath:
    if pth not in sys.path:
        sys.path.insert(0,pth)

from version import versionstrg
import util
import prep
import aesys
import viz
# -

version, _ = versionstrg()
fname = "Tutorial1_VIZ_data_flightline.py"
# fname = __file__  # this only works in python, not jupyter notebook
titstrng = util.print_title(version=version, fname=__file__, out=False)
print(titstrng+"\n\n")
Header = titstrng


OutInfo = False
AEMPYX_DATA = os.environ["AEMPYX_DATA"]
rng = numpy.random.default_rng()
nan = numpy.nan 


# The following cell gives values to AEM-system related settings. Data 
# transformation is activated by the variable \textit{DataTrans}. Currently 
# three possible options are allowed:
# \begin{description}
# \item[DataTrans = 0]. No transformation, i.e., the raw data are used.
# \item[DataTrans = 1]. The natural log of data is used, only allowed for 
# strictly positive values.
# \item[DataTrans = 2]. If data scale logarithmically, an asinh transformation 
# introduced by Scholl (2000)is applied. It allows negatives, which may occur 
# in TDEM, when IP effects are present.)
# \end{description}           
# A general additive/multiplicative error model is applied on the raw data
# before transformation, and errors are also transformed.


# +
# AEM_system = "genesis"
AEM_system = "aem05"  # "genesis"
if "aem05" in AEM_system.lower():
    _ ,NN, _, _, _, = aesys.get_system_params(System=AEM_system)
    nD = NN[0]
    ParaTrans = 1
    DataTrans = 0
    DatErr_add =  75.
    DatErr_mult = 0.05
    data_active = numpy.ones(NN[2], dtype="int8")

if "genes" in AEM_system.lower():
    _ , NN, _, _, _, = aesys.get_system_params(System=AEM_system)
    nD = NN[0]
    ParaTrans = 1
    DataTrans = 0
    DatErr_add = 100.
    DatErr_mult = 0.01
    data_active = numpy.ones(NN[2], dtype="int8")
    data_active[0:11]=0  # only vertical component
    # data_active[10:11]=0  # Vertical + 'good' hoizontals'
# -


version, _ = versionstrg()
titstrng = util.print_title(version=version, fname=__file__, out=False)
print(titstrng+"\n\n")

"""
input formats are .npz, .nc4, 'ascii'
"""
InStrng = ""
PlotStrng = " - data "+InStrng


FileList = "search"  
SearchStrng = "*nan*.npz"# "search", "read"


# InDatDir =  AEMPYX_ROOT + "/work/data/raw/"
# PlotDir  =  AEMPYX_ROOT + "/work/data/raw/plots/"
# PlotStrng = " - data raw"

InDatDir =  AEMPYX_ROOT + "/work/data/proc_delete_PLM3s/"
PlotDir  =  AEMPYX_ROOT + "/work/data/proc_delete_PLM3s/plots/"
PlotStrng = " - data proc"



if "set" in FileList.lower():
    print("Data files read from dir:  %s" % InDatDir)
    dat_files = []
    f = numpy.load(AEMPYX_DATA+"/Projects/Compare_systems/BundoranSubsets.npz")

    dat_files = f["setC"][0]
    dat_files = [os.path.basename(d) for d in dat_files]
else:
    # how = ["search", SearchStrng, InDatDir]
    # how = ["read", FileList, InDatDir]
    dat_files = util.get_data_list(how=["search", SearchStrng, InDatDir],
                              out= True, sort=True)
    ns = numpy.size(dat_files)

ns = numpy.size(dat_files)
if ns ==0:
    error("No files set!. Exit.")

print(dat_files)

if not os.path.isdir(PlotDir):
    print("File: %s does not exist, but will be created" % PlotDir)
    os.mkdir(PlotDir)

FilesOnly = False
PlotFmt = [".pdf", ".png", ]
PdfCatalog = True
PdfCatName = PlotDir+"Limerick_shale_raw.pdf"

if ".pdf" in PlotFmt:
    pass
else:
    error(" No pdfs generated. No catalog possible!")
    PdfCatalog = False

if "aem05" in AEM_system.lower():
    IncludePlots = ["alt", "qdata", "idata",]
    IncludePlots = ["qdata", "idata",]
    QLimits = []
    ILimits = []
    PlotSize = [18., 6.]
    PLimits = [0., 10.]
    HLimits = [30., 90.] #[40., 140.]
    LogPlot = False
    LogSym = False
    LinThresh =10.
    if LogPlot == False:
        LogSym = False
    Logparams=[LogPlot, LogSym, LinThresh]

if "genes" in AEM_system.lower():
    IncludePlots = ["alt", "xdata", "zdata",]
    IncludePlots = ["xdata", "zdata",]
    PlotSize = [18., 6.]
    DataTrans = "asinh"
    XLimits = [3.5, 12.]
    ZLimits = [6., 14.]

    LogPlot = False
    LogSym = False
    LinThresh =100.
    if LogPlot == False:
        LogSym = False
    Logparams=[LogPlot, LogSym, LinThresh]


    HLimits = [80., 320.]
    PLimits = [0., 25.]

PosDegrees = False
if PosDegrees:
    EPSG=32629
PlotThresh =10

ProfType = "distance"
if "dist" in ProfType.lower():
    ProfLabel = "profile distance (m) "
    ProfScale = 1. # 0.001  # m to km
else:
    ProfLabel = "site # (-)"
    ProfScale = 1. # 0.001  # m to km


"""
Determine graphical parameter.
=> print(matplotlib.pyplot.style.available)
"""

matplotlib.pyplot.style.use("seaborn-v0_8-paper")
matplotlib.rcParams["figure.dpi"] = 400
matplotlib.rcParams["axes.linewidth"] = 0.5
matplotlib.rcParams["savefig.facecolor"] = "none"
matplotlib.rcParams["savefig.transparent"] = True
matplotlib.rcParams["savefig.bbox"] = "tight"
Fontsize = 8
Labelsize = Fontsize
Titlesize = 8
Fontsizes = [Fontsize, Labelsize, Titlesize]

Linewidths= [0.6]
Markersize = 4

ncols = 11
Colors = matplotlib.pyplot.cm.jet(numpy.linspace(0,1,ncols))
Grey = 0.7
Lcycle =Lcycle = (cycler("linestyle", ["-", "--", ":", "-."])
          * cycler("color", ["r", "g", "b", "y"]))

"""
For just plotting to files, choose the cairo backend (eps, pdf, ,png, jpg...).
If you need to see the plot. directly (plot. window, or jupyter), simatplotliby
comment out the following line. In this case matplotlib may run into
memory problems after a few hundreds of high-resolution plot..
"""
if FilesOnly:
    matplotlib.use("cairo")

if PdfCatalog:
    pdf_list = []

ifl = 0
for file in dat_files:

    ifl = ifl+1
    
    name, ext = os.path.splitext(file)
    
    filein = InDatDir+file
    Data, Header, _ = aesys.read_aempy(File=filein, 
                                   System=AEM_system, OutInfo=False)
    sD = numpy.shape(Data)
    print("flightline "+name+"  #"
          +str(ifl)+" of "
          +str(numpy.size(dat_files)) +" has shape: "+str(sD))

    if numpy.size(Data)<=nD:
        print("Not enough data! Not plotted")
        continue

    anynan = numpy.argwhere(numpy.isnan(Data))
    nnans = numpy.shape(anynan)[0]
    for ii in anynan:
        Data[ii[0],3:] = numpy.nan

    if numpy.shape(Data)[0]-nnans < PlotThresh:
        print("Not enough data! Not plotted")
        continue


    if PdfCatalog:
        pdf_list.append(PlotDir+name+".pdf")

    fline = Data[:, 0]
    Data[:, 1] = Data[:, 1] * ProfScale
    Data[:, 2] = Data[:, 2] * ProfScale

    if "aem05" in AEM_system.lower():
        viz.plot_flightline_aem05(
            PlotName = name,
            PlotDir = PlotDir,
            PlotFmt=PlotFmt,
            IncludePlots=IncludePlots,
            PlotSize = PlotSize,
            DataObs=Data,
            DataCal=[],
            QLimits =[],
            ILimits =[],
            DLimits = [],
            HLimits = HLimits,
            PLimits = PLimits,
            ProfLabel=ProfLabel,
            Linecolor=Colors,
            Linewidth=Linewidths,
            Fontsizes=Fontsizes,
            Logparams=Logparams,
            PlotStrng=PlotStrng,
            PlotPLM = True)
    if "genes" in AEM_system.lower():
        viz.plot_flightline_genesis(
            PlotName = name,
            PlotDir = PlotDir,
            PlotFmt=PlotFmt,
            IncludePlots=IncludePlots,
            PlotSize = PlotSize,
            DataObs=Data,
            DataCal=[],
            DataTrans = DataTrans,
            DLimits = [],
            XLimits =XLimits,
            ZLimits =ZLimits,
            HLimits =[],
            ProfLabel=ProfLabel,
            Linecolor=Colors,
            Linewidth=Linewidths,
            Fontsizes=Fontsizes,
            Logparams=Logparams,
            PlotStrng=PlotStrng)


if PdfCatalog:
    viz.make_pdf_catalog(PDFList=pdf_list, FileName=PlotDir+PdfCatName)
