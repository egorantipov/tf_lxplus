# ML setup reference:
# https://github.com/USATLAS-ML-Training/Intro-BDT-NN/blob/main/HEPML_HandsOn_NN.ipynb

# How to submit it to HTCondor:
# http://oproject.org/pages/CERN%20GPU%20Condor.html

# setupATLAS
# virtualenv -p /usr/bin/python3 venv
# source venv/bin/activate
# git clone --recursive https://github.com/scikit-hep/uproot3.git
# pip install --upgrade --target=uproot3/ uproot3/
# rm -rf uproot3/numpy*
# source /cvmfs/sft.cern.ch/lcg/views/LCG_96py3cu10/x86_64-centos7-gcc7-opt/setup.sh
# export PYTHONPATH=/afs/cern.ch/work/e/eantipov/public/tt_jets_analyses/test/classifier_python/uproot3:$PYTHONPATH
# python classifier.py


import ROOT 
import os 
import uproot3 as ur
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

pd.set_option('display.max_columns', None)
np.random.seed(31415)


print("Tensorflow version: \n", tf.__version__)
print(tf.test.is_gpu_available())


inFileName = "NN_input.root"
inFile = ur.open(inFileName)
print(inFile.classnames())

tree = inFile["Merged"]
print("Tree keys: \n", tree.keys())
print(type(tree))
tree.show()

#dfall = tree.arrays() # argument ` library="pd" ` didn't work
#print(type(dfall))

# Shuffle the events
#dfall = dfall.sample(frac=1).reset_index(drop=True)
