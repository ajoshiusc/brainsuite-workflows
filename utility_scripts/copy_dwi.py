#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Anand A Joshi, Divya Varadarajan
"""
import shutil
from os.path import isdir, isfile
import glob
import sys
import ConfigParser

config_file = sys.argv[1]
'''/big_disk/ajoshi/coding_ground/\
brainsuite-workflows/data/sample_data/thickness.cfg'''

Config = ConfigParser.ConfigParser()
Config.read(config_file)
Config.sections()

STUDY_DIR = Config.get('CSESVREG', 'STUDY_DIR')

sublist = lst = glob.glob(STUDY_DIR+'/*')

ind = 0
for sub in sublist:
    dwi_dir = sub + '/dwi'
    t1_dir = sub + '/anat'
    if not isdir(t1_dir):
        continue

    for fname in glob.glob(t1_dir + '/*.dwi.*'):
        shutil.move(fname, dwi_dir)

    for fname in glob.glob(t1_dir + '/*.D_coord.*'):
        shutil.move(fname, dwi_dir)

    for fname in glob.glob(t1_dir + '/FRT'):
        shutil.move(fname, dwi_dir)

    for fname in glob.glob(t1_dir + '/*.bst'):
        shutil.move(fname, dwi_dir)

    for fname in glob.glob(t1_dir + '/*.atlas.FA.nii.gz'):
        shutil.move(fname, dwi_dir)

    shutil.copy(t1_dir + '/t1.bfc.nii.gz', dwi_dir)
    shutil.copy(t1_dir + '/t1.mask.nii.gz', dwi_dir)

    if isfile(t1_dir + '/t1.BDPSummary.txt'):
        shutil.move(t1_dir + '/t1.BDPSummary.txt', dwi_dir)

    ind += 1

    print ind
