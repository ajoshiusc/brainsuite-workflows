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

csv_file = '/big_disk/ajoshi/coding_ground/brainsuite-workflows/\
data/sample_data/sample_T1.csv'
NPROC = 6
BST_INSTALL = '/home/ajoshi/BrainSuite16a1'
SVREG_ATLAS = '/home/ajoshi/BrainSuite16a1/svreg/BrainSuiteAtlas1/mri'
SVREG_FLAGS = ''
CSE_EXE = BST_INSTALL + '/bin/cortical_extraction.sh'
SVREG_EXE = BST_INSTALL + '/svreg/bin/svreg.sh'


with open(csv_file, 'rb') as csvfile:
    sublist = csv.reader(csvfile)

    ind = 0
    cmdln = []
    for sub in sublist:
        img = ''.join(sub)

        if not isfile(img):
            continue

        cmdln.append(CSE_EXE + ' ' + img)
        cmdln.append(SVREG_EXE + ' ' + img[:-7] + ' ' + SVREG_ATLAS + ' ' +
                     SVREG_FLAGS)
        print cmdln
        ind += 1

    with closing(Pool(NPROC)) as p:
        p.map(system, cmdln)
        p.terminate()

    print "Surface extractions done"
