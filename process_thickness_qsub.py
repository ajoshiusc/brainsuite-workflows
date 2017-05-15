#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:26 2017

@author: Anand A Joshi, Divya Varadarajan
"""

import sys
from os import system
from os.path import isfile, split
from multiprocessing import Pool
from contextlib import closing
import configparser
import glob
#config_file = '/big_disk/ajoshi/coding_ground/\
#brainsuite-workflows/data/sample_data/thickness.cfg'

config_file = sys.argv[1]
Config = configparser.ConfigParser()
Config.read(config_file)
Config.sections()

STUDY_DIR = Config.get('CSESVREG', 'STUDY_DIR')
NPROC = int(Config.get('CSESVREG', 'NPROC'))
BST_INSTALL = Config.get('CSESVREG', 'BST_INSTALL')
SVREG_ATLAS = Config.get('CSESVREG', 'SVREG_ATLAS')
THICKNESSPVC_EXE = Config.get('THICKNESS', 'THICKNESSPVC_EXE')
GENERATE_STATS_EXE = Config.get('THICKNESS', 'GENERATE_STATS_EXE')
SMOOTHNESS = Config.get('THICKNESS', 'SMOOTHNESS')
SMOOTHNESS_EXE = Config.get('THICKNESS', 'SMOOTHNESS_EXE')

sublist = lst = glob.glob(STUDY_DIR+'/*')


ind = 0
cmdln1 = []
cmdln2 = []
cmdln3 = []
cmdln4 = []

for sub in sublist:

    img = sub + '/anat/t1.nii.gz'

    if not isfile(img):
        continue
# Check if the workflow has already been run
    subpath, filename = split(img)
    fname = subpath + '/atlas.pvc-thickness_0-6mm.right.\
smooth_' + SMOOTHNESS + 'mm.dfs'
    if isfile(fname):
        continue

    surfname = subpath + '/atlas.left.mid.cortex.svreg.dfs'
    if not isfile(surfname): 
        cmdln1.append('qsub -q long.q -l h_vmem=23G -cwd ' + THICKNESSPVC_EXE +
                  ' ' + img[:-7])
    cmdln2.append('qsub -q long.q -l h_vmem=23G -cwd ' + GENERATE_STATS_EXE +
                  ' ' + img[:-7])
    outsurfname = subpath + '/atlas.pvc-thickness_0-6mm.left.\
smooth_' + SMOOTHNESS + 'mm.dfs'

    if not isfile(outsurfname): 
        cmdln3.append('qsub -q long.q -l h_vmem=23G -cwd ' + SMOOTHNESS_EXE +
                      ' ' + surfname + ' ' + surfname + ' \
' + outsurfname)
    surfname = subpath + '/atlas.right.mid.cortex.svreg.dfs'
    outsurfname = subpath + '/atlas.pvc-thickness_0-6mm.right.\
smooth_' + SMOOTHNESS + 'mm.dfs'

    if not isfile(outsurfname): 
        cmdln4.append('qsub -q long.q -l h_vmem=23G -cwd ' +
                      SMOOTHNESS_EXE + ' ' + surfname + ' ' + surfname + ' \
' + outsurfname)

    print(cmdln1)
    ind += 1

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln1)
    p.terminate()

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln2)
    p.terminate()

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln3)
    p.terminate()

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln4)
    p.terminate()

print("Thickness Computations Done")
