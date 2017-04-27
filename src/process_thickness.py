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
NPROC = Config.get('CSESVREG', 'NPROC')
BST_INSTALL = Config.get('CSESVREG', 'BST_INSTALL')
SVREG_ATLAS = Config.get('CSESVREG', 'SVREG_ATLAS')
THICKNESSPVC_EXE = Config.get('THICKNESS', 'THICKNESSPVC_EXE')
SMOOTHMESS = Config.get('THICKNESS', 'SMOOTHNESS')
SMOOTHMESS_EXE = Config.get('THICKNESS', 'SMOOTHNESS_EXE')


with open(csv_file, 'rb') as csvfile:
    sublist = csv.reader(csvfile)

    ind = 0
    cmdln = []
    for sub in sublist:
        img = ''.join(sub)

        if not isfile(img):
            continue

        subpath, filename = split(sub)

        cmdln.append(THICKNESSPVC_EXE + ' ' + img[:-7] + ' ' + SVREG_ATLAS)
        surfname = subpath + '/atlas.hemi.mid.cortex.svreg.dfs'
        outsurfname = subpath + '/atlas.hemi.mid.cortex.\
smooth' + SMOOTHMESS + '.svreg.dfs'
        cmdln.append(SMOOTHMESS_EXE + ' ' + surfname + ' ' + surfname + ' \
' + outsurfname)

        print cmdln
        ind += 1

    with closing(Pool(NPROC)) as p:
        p.map(system, cmdln)
        p.terminate()

    print "Thickness Computations Done"
