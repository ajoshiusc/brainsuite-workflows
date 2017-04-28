#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:26 2017

@author: Anand A Joshi, Divya Varadarajan
"""

import csv
from os import system
from os.path import isfile
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
SVREG_FLAGS = Config.get('CSESVREG', 'SVREG_FLAGS')

CSE_EXE = Config.get('CSESVREG', 'CSE_EXE')
SVREG_EXE = Config.get('CSESVREG', 'SVREG_EXE')

with open(csv_file, 'rb') as csvfile:
    sublist = csv.reader(csvfile)

    ind = 0
    cmdln1 = []
    cmdln2 = []
    for sub in sublist:
        img = ''.join(sub[0])

        if not isfile(img):
            continue

# compose commands for cse and svreg
        cmdln1.append(CSE_EXE + ' ' + img)
        cmdln2.append(SVREG_EXE + ' ' + img[:-7] + ' ' + SVREG_ATLAS + ' ' +
                      SVREG_FLAGS)
#        print cmdln1, cmdln2
        ind += 1

# Run CSE
    with closing(Pool(NPROC)) as p:
        p.map(system, cmdln1)
        p.terminate()
# run SVReg
    with closing(Pool(NPROC)) as p:
        p.map(system, cmdln2)
        p.terminate()

print "Surface extractions done"

