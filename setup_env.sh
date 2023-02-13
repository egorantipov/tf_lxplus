setupATLAS
source venv/bin/activate
scl enable rh-python38 bash
source /cvmfs/sft.cern.ch/lcg/views/LCG_96py3cu10/x86_64-centos7-gcc7-opt/setup.sh
export PYTHONPATH=$(pwd)/uproot3:$PYTHONPATH
