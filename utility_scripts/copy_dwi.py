#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Anand A Joshi, Divya Varadarajan
"""
import shutil
from os.path import isfile

STUDY_DIR = '<path to directory with all subject folders>'

sublist = lst = glob.glob(STUDY_DIR+'/*')

ind = 0
for sub in sublist:
	dwi_dir = sub + '/dwi'
	t1_dir = sub + '/anat'
	
	shutil.move(t1_dir + '/*.dwi.*', dwi_dir)
	shutil.move(t1_dir + '/*.D_coord.*', dwi_dir)
	shutil.move(t1_dir + '/FRT', dwi_dir)
	shutil.move(t1_dir + '/*.bst', dwi_dir)
	shutil.copy(t1_dir + '/t1.bfc.nii.gz',dwi_dir)
	shutil.copy(t1_dir + '/t1.mask.nii.gz',dwi_dir)
	ind += 1

print ind