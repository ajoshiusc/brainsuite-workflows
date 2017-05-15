#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: Anand A Joshi, Divya Varadarajan
"""
from shutil import copyfile
import csv
from os import mkdir
from os.path import isfile

#mkdir('/big_disk/ajoshi/ABIDEII-SDSU/')
csv_file = '/big_disk/ajoshi/ABIDEII-SDSU_1.csv'

with open(csv_file, 'rU') as csvfile:
    sublist = csv.reader(csvfile)

    ind = 0
    cmdln1 = []
    cmdln2 = []
    cnt = 0
    for sub in sublist:
        subid = ''.join(sub[1])
        img = '/big_disk/dvaradar/ABIDE2/ABIDEII-SDSU\
_1/' + subid + '/session_1/anat_1/anat.nii.gz'
        dwi = '/big_disk/dvaradar/ABIDE2/ABIDEII-SDSU\
_1/' + subid + '/session_1/dti_1/dti.nii.gz'

        bval = '/big_disk/dvaradar/ABIDE2/ABIDEII-SDSU\
_1/bvals'

        bvec = '/big_disk/dvaradar/ABIDE2/ABIDEII-SDSU\
_1/bvecs'

        if not isfile(dwi):
            continue

        if not isfile(img):
            continue

        cnt += 1
        mkdir('/big_disk/ajoshi/ABIDEII-SDSU/'+subid)
        mkdir('/big_disk/ajoshi/ABIDEII-SDSU/'+subid+'/anat')
        mkdir('/big_disk/ajoshi/ABIDEII-SDSU/'+subid+'/dwi')
        copyfile(img, '/big_disk/ajoshi/ABIDEII-SDSU/'+subid+'/anat/t1.nii.gz')
        copyfile(dwi, '/big_disk/ajoshi/ABIDEII-SDSU/'+subid+'/dwi/dwi.nii.gz')
        copyfile(bval, '/big_disk/ajoshi/ABIDEII-SDSU/'+subid+'/dwi/dwi.bval')
        copyfile(bvec, '/big_disk/ajoshi/ABIDEII-SDSU/'+subid+'/dwi/dwi.bvec')

print cnt
