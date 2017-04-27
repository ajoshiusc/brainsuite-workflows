# BrainSuite Workflows

The brainsuite workflows are set of python scripts to carry out studies using BrainSuite programs. They invoke appropriate BrainSuite executables for performing specific studies. 

![enter image description here](https://docs.google.com/drawings/d/1npbk6qKl4GP5pBomLT52FJ_eP1vo6HtlyHKLPLpECQ0/pub?w=641&h=123)

## Cortical Extraction
First, make sure that [BrainSuite](http://brainsuite.org) is installed and working on your computer. Make sure that Python is installed. It is helpful to run through the [tutorials](http://brainsuite.org/tutorials/).
In order to run cortical thickness analysis in BrainSuite please follow following steps:

 1.  Make sure that each subject's T1 is in its own folder 
 2.  Create a csv file with full paths and file names of the T1 images (sample.csv)
 3.  Download brainsuite-workflows from [here](https://github.com/ajoshiusc/brainsuite-workflows)
 4. Arrange your data in directories as follows: 

![enter image description here](https://docs.google.com/drawings/d/1SDnDKRA-YF5I3IvcQrO6NTS84jlTN1HHkv6SlIDE7fE/pub?w=600)

 5. Edit the study.cfg file as required. The config file cobtains location of the csv file that has all the T1 scans. make sure that the locations of executables are correct. Make sure that the number of processors **NPROC** is set correctly for your machine.
 6. Run  `process_t1.py` from the command prompt. This will run cortical surface extraction.

# Cortical Thickness Workflow

1. Check the **Thickness** section in the study.cfg file. Especially, select the SMOOTHNESS parameter as desired.
2. Run `process_thickness.sh`script. This will run cortical thickness computation and smoothing on all of the datasets in the study.
3. BSS [BSS documention here]
 
# Diffusion workflow

1. Check the **BDP** section in the study.cfg file.
2. Run `process_dwi.sh`script. 
3. BSS [BSS documention here]
