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


print("imports worked!")
print(tf.test.is_gpu_available()) # tensorflow 2


inFileName = "tt_hf_MVA_input_reco_nominal_lep_pT_28.root"
inFile = ur.open(inFileName)
print(inFile.classnames())

treeSig = inFile["Signal"]
treeBkg = inFile["Background"]

print("Signal tree keys: \n", \
      treeSig.keys(), \
      "\nBackground tree keys: \n", \
      treeBkg.keys())
