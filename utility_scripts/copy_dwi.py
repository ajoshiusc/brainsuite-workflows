#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Anand A Joshi, Divya Varadarajan
"""
import shutil
#from os.path import isfile
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

    shutil.move(t1_dir + '/*.dwi.*', dwi_dir)
    shutil.move(t1_dir + '/*.D_coord.*', dwi_dir)
    shutil.move(t1_dir + '/FRT', dwi_dir)
    shutil.move(t1_dir + '/*.bst', dwi_dir)
    shutil.move(t1_dir + '/*.atlas.FA.nii.gz', dwi_dir)
    shutil.copy(t1_dir + '/t1.bfc.nii.gz', dwi_dir)
    shutil.copy(t1_dir + '/t1.mask.nii.gz', dwi_dir)
    ind += 1

    print ind
