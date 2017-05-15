#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:16:26 2017

@author: Anand A Joshi, Divya Varadarajan
"""

import glob
from os.path import isfile, split
import configparser

config_file = u'/big_disk/ajoshi/ABIDE2/study.cfg'

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

SMOOTHNESS = '6'
ind = 0
cmdln1 = []
cmdln2 = []
incom = 0
com = 0
for sub in sublist:
    img = sub + '/anat/t1.roiwise.stats.txt'
    subpath, filename = split(img)
    outsurfname = subpath + '/t1.heat_sol_comp.mat'

#    print img
    if not isfile(outsurfname):
        incom += 1
        print outsurfname
        continue


    com += 1
print str(incom) + ' remaining ' + str(com) + ' done'
