#!/bin/sh

ClusterId=$1
echo "Cluster id: " $ClusterId

rundir=/afs/cern.ch/work/e/eantipov/public/tt_jets_analyses/test/classifier_python
cd $rundir
pwd
ls

export ATLAS_LOCAL_ROOT_BASE=/cvmfs/atlas.cern.ch/repo/ATLASLocalRootBase
alias setupATLAS='source ${ATLAS_LOCAL_ROOT_BASE}/user/atlasLocalSetup.sh'
setupATLAS
source venv/bin/activate
source /cvmfs/sft.cern.ch/lcg/views/LCG_96py3cu10/x86_64-centos7-gcc7-opt/setup.sh
export PYTHONPATH=$rundir/uproot3:$PYTHONPATH

python classifier.py
