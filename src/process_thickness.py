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
import configparser

config_file = '/big_disk/ajoshi/coding_ground/\
brainsuite-workflows/data/sample_data/thickness.cfg'

Config = configparser.ConfigParser()
Config.read(config_file)
Config.sections()

csv_file = Config.get('CSESVREG', 'csv_file')
NPROC = int(Config.get('CSESVREG', 'NPROC'))
BST_INSTALL = Config.get('CSESVREG', 'BST_INSTALL')
SVREG_ATLAS = Config.get('CSESVREG', 'SVREG_ATLAS')
THICKNESSPVC_EXE = Config.get('THICKNESS', 'THICKNESSPVC_EXE')
SMOOTHNESS = Config.get('THICKNESS', 'SMOOTHNESS')
SMOOTHNESS_EXE = Config.get('THICKNESS', 'SMOOTHNESS_EXE')


with open(csv_file, 'rt') as csvfile:
    sublist = csv.reader(csvfile)

    ind = 0
    cmdln1 = []
    cmdln2 = []
    cmdln3 = []

    for sub in sublist:
        img = ''.join(sub[0])

        if not isfile(img):
            continue

        subpath, filename = split(sub[0])

        cmdln1.append(THICKNESSPVC_EXE + ' ' + img[:-7] + ' ' + SVREG_ATLAS)
        surfname = subpath + '/atlas.left.mid.cortex.svreg.dfs'
        outsurfname = subpath + '/atlas.pvc-thickness_0-6mm.left.\
smooth_' + SMOOTHNESS + 'mm.dfs'
        cmdln2.append(SMOOTHNESS_EXE + ' ' + surfname + ' ' + surfname + ' \
' + outsurfname)
        surfname = subpath + '/atlas.right.mid.cortex.svreg.dfs'
        outsurfname = subpath + '/atlas.pvc-thickness_0-6mm.right.\
smooth_' + SMOOTHNESS + 'mm.dfs'
        cmdln3.append(SMOOTHNESS_EXE + ' ' + surfname + ' ' + surfname + ' \
' + outsurfname)

        print(cmdln1)
        ind += 1

#    with closing(Pool(NPROC)) as p:
#        p.map(system, cmdln1)
#        p.terminate()

    with closing(Pool(NPROC)) as p:
        p.map(system, cmdln2)
        p.terminate()

    with closing(Pool(NPROC)) as p:
        p.map(system, cmdln3)
        p.terminate()

    print("Thickness Computations Done")
