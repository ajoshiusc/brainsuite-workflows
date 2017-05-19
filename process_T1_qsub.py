#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:26 2017

@author: Anand A Joshi, Divya Varadarajan
"""

import glob
from os import system
from os.path import isfile
from multiprocessing import Pool
from contextlib import closing
import configparser
import sys

config_file = sys.argv[1]
# '/big_disk/ajoshi/ABIDE2/study.cfg'

Config = configparser.ConfigParser()
Config.read(config_file)
Config.sections()

STUDY_DIR = Config.get('CSESVREG', 'STUDY_DIR')
NPROC = int(Config.get('CSESVREG', 'NPROC'))

BST_INSTALL = Config.get('CSESVREG', 'BST_INSTALL')
SVREG_ATLAS = Config.get('CSESVREG', 'SVREG_ATLAS')
SVREG_FLAGS = Config.get('CSESVREG', 'SVREG_FLAGS')

CSE_EXE = Config.get('CSESVREG', 'CSE_EXE')
SVREG_EXE = Config.get('CSESVREG', 'SVREG_EXE')

sublist = lst = glob.glob(STUDY_DIR+'/*')


ind = 0
cmdln1 = []
cmdln2 = []
for sub in sublist:

    img = sub + '/anat/t1.nii.gz'
#    print img
    if not isfile(img):
        continue

# Compose commands for CSE and SVReg

    imgpial = sub + '/anat/t1.right.pial.cortex.dfs'
    imgstats = sub + '/anat/t1.roiwise.stats.txt'

# Check if the workflow has already been run
    if not isfile(imgpial):
        cmdln1.append('qsub -q long.q -l h_vmem=23G -cwd ' + CSE_EXE + ' ' +
                      img)

    if not isfile(imgstats):
        cmdln2.append('qsub -q long.q -l h_vmem=23G -cwd ' + SVREG_EXE + ' ' +
                      img[:-7] + ' ' + SVREG_ATLAS + ' ' +
                      SVREG_FLAGS)
    ind += 1

# Run CSE
with closing(Pool(NPROC)) as p:
    print cmdln1
    p.map(system, cmdln1)
    p.terminate()

# Run SVReg
with closing(Pool(NPROC)) as p:
    p.map(system, cmdln2)
    print cmdln2
    p.terminate()

print("Surface extractions and SVReg done")
