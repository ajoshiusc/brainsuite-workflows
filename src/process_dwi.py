#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:26 2017

@author: Anand A Joshi, Divya Varadarajan
"""

import csv
from os import system
from os.path import isfile, split
from multiprocessing import Pool
from contextlib import closing
import ConfigParser

config_file = '/big_disk/ajoshi/coding_ground/\
brainsuite-workflows/data/sample_data/thickness.cfg'

Config = ConfigParser.ConfigParser()
Config.read(config_file)
Config.sections()

csv_file = Config.get('CSESVREG', 'csv_file')
NPROC = int(Config.get('CSESVREG', 'NPROC'))
BST_INSTALL = Config.get('CSESVREG', 'BST_INSTALL')
SVREG_ATLAS = Config.get('CSESVREG', 'SVREG_ATLAS')

BDP_EXE = Config.get('BDP', 'BDP_EXE')
SVREG_MAP_EXE = Config.get('BDP', 'SVREG_MAP_EXE')
csv_file=''.join(csv_file)
f = open(csv_file, 'rU') #open the file in read universal mode
ind = 0;
cmdln1 = []
cmdln2 = []

for line in f:
    cells = line.split( "," )
    t1 = cells[0];
    dwi = cells[1][:-1]

    if not isfile(t1):
        continue
    if not isfile(dwi):
        continue

    cmdln1.append(BDP_EXE + ' ' + t1[:-7] + '.bfc.nii.gz ' + ' --nii ' + dwi + ' --bvec ' + dwi[:-7] + '.bvec' + ' --bval ' +  dwi[:-7] + '.bval ' +  ' --tensors --frt');
    print cmdln1
    cmdln2.append(SVREG_MAP_EXE + ' ' + t1[:-7] + '.svreg.inv.map.nii.gz ' + t1[:-7] + '.dwi.RAS.correct.FA.T1_coord.nii.gz ' +  t1[:-7] + '.atlas.FA.nii.gz ' +  SVREG_ATLAS + '.bfc.nii.gz');
    print cmdln2

    ind += 1

f.close()

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln1)
    p.terminate()

with closing(Pool(NPROC)) as p:
    p.map(system, cmdln2)
    p.terminate()

    print "DWI Computations Done"
