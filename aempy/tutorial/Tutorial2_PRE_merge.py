#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: py:light,ipynb
#     main_language: python
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (Spyder)
#     language: python3
#     name: python3
# ---

"""
Created on Thu Apr 18 08:37:28 2024

@author: vrath
"""

import os
import sys
from sys import exit as error
from time import process_time
from datetime import datetime
import warnings
# import pickle

import numpy


# +
AEMPYX_ROOT = os.environ["AEMPYX_ROOT"]
mypath = [AEMPYX_ROOT+"/aempy/modules/", AEMPYX_ROOT+"/aempy/scripts/"]
for pth in mypath:
    if pth not in sys.path:
        sys.path.insert(0,pth)

from version import versionstrg
import util
import aesys
# -

AEMPYX_DATA = os.environ["AEMPYX_DATA"]

version, _ = versionstrg()
titstrng = util.print_title(version=version, fname=__file__, out=False)
print(titstrng+"\n\n")



AEMPYX_DATA = AEMPYX_ROOT+"/data/"
DataType = "models"
FileList = "search"  # "search", "read"


DataType = "models"
InDatDir = AEMPYX_DATA+"/aem05_limerick/dec/results/"
OutDatDir = AEMPYX_DATA+"/aem05_limerick/merged/"
SearchStrng = "*_k2*5*mean.npz"
OutFileName = OutDatDir+"LimShale_k2_dec5_mean_merged"
OutHeader =" Limerick Shale project, k2 dec5 mean merged"

# DataType = "data"
# InDatDir = AEMPYX_ROOT+"/data/"
# OutDatDir = AEMPYX_ROOT+"/limerick/merged/"
# SearchStrng = "*_k2*5*mean.npz"
# OutFileName = OutDatDir+"LimShale_k2_dec5_mean_merged"
# OutHeader =" Limerick Shale project, k2 dec5 mean merged"


print("Data read from dir:  %s" % InDatDir)
print("Data written to dir: %s" % OutDatDir)
print("New flightline Header string: %s" % OutHeader)
print("SearchStrng is %s\n" % SearchStrng)


if not InDatDir.endswith("/"): InDatDir=InDatDir+"/"
if not OutDatDir.endswith("/"): InDatDir=OutDatDir+"/"
if not os.path.isdir(OutDatDir):
    print("File: %s does not exist, but will be created" % OutDatDir)
    os.mkdir(OutDatDir)

if "set" in FileList.lower():
    print("Data files read from dir:  %s" % InDatDir)
    # dat_files = []
    dat_files = [InDatDir+"StGormans_FL11379-0_k3.npz"]
    # numpy.load(AEMPYX_DATA + "/Projects/Compare/BundoranSubsets.npz")["setC"]
    
    dat_files = [os.path.basename(f) for f in dat_files]  
else:
    # how = ["search", SearchStrng, InDatDir]
    # how = ["read", FileList, InDatDir]
    dat_files = util.get_data_list(how=["search", SearchStrng, InDatDir],
                              out= True, sort=True, fullpath=True)
ns = numpy.size(dat_files)
if ns ==0:
    error("No files set!. Exit.")


if "dat" in DataType.lower():  
    _ = util.merge_data_sets(file_list=dat_files, aem_system="aem05",
                                       outfile_name=OutFileName,
                                       out=False)
else:
    _ = util.merge_model_sets(infile_list=dat_files,
                                   outfile_name=OutFileName,
                                   dictout= True, out=False)


