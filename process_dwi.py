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
import ConfigParser
import sys
from shutil import copyfile

config_file = sys.argv[1]
'''/big_disk/ajoshi/coding_ground/\
brainsuite-workflows/data/sample_data/thickness.cfg'''

Config = ConfigParser.ConfigParser()
Config.read(config_file)
Config.sections()

STUDY_DIR = Config.get('CSESVREG', 'STUDY_DIR')
NPROC = int(Config.get('CSESVREG', 'NPROC'))
BST_INSTALL = Config.get('CSESVREG', 'BST_INSTALL')
SVREG_ATLAS = Config.get('CSESVREG', 'SVREG_ATLAS')

BDP_EXE = Config.get('BDP', 'BDP_EXE')
BDP_FLAGS = Config.get('BDP', 'BDP_FLAGS')
SVREG_MAP_EXE = Config.get('BDP', 'SVREG_MAP_EXE')

sublist = lst = glob.glob(STUDY_DIR+'/*')
ind = 0
cmdln1 = []
cmdln2 = []

for sub in sublist:
    t1_org = sub + '/anat/t1.nii.gz'
    t1 = sub + '/dwi/t1.nii.gz'
    mask_org = sub + '/anat/t1.mask.nii.gz'
    mask = sub + '/dwi/t1.mask.nii.gz'
    bfc_org = sub + '/anat/t1.bfc.nii.gz'
    bfc = sub + '/dwi/t1.bfc.nii.gz'
    dwi = sub + '/dwi/dwi.nii.gz'

    if not isfile(t1_org):
        continue
    if not isfile(dwi):
        continue
    if not isfile(bfc_org):
        continue

    copyfile(t1_org, t1)
    copyfile(bfc_org, bfc)
    if isfile(mask_org):
        copyfile(mask_org, mask)

    cmdln1.append(BDP_EXE + ' ' + t1[:-7] + '.bfc.nii.gz ' + ' --nii ' + dwi +
                  ' --bvec ' + dwi[:-7] + '.bvec' + ' --bval ' + dwi[:-7] +
                  '.bval ' + ' --tensors --frt ' + BDP_FLAGS)
    print(cmdln1)
    cmdln2.append(SVREG_MAP_EXE + ' ' + t1[:-7] + '.svreg.inv.map.nii.gz ' +
                  t1[:-7] + '.dwi.RAS.correct.FA.T1_coord.nii.gz ' +
                  t1[:-7] + '.atlas.FA.nii.gz ' + SVREG_ATLAS + '.bfc.nii.gz')
    print cmdln2

    ind += 1


with closing(Pool(NPROC)) as p:
    p.map(system, cmdln1)
    p.terminate()

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln2)
    p.terminate()

    print("DWI Computations Done")
