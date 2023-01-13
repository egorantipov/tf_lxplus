mkdir condor
setupATLAS
virtualenv -p /usr/bin/python3 venv
source venv/bin/activate
git clone --recursive https://github.com/scikit-hep/uproot3.git
pip install --upgrade --target=uproot3/ uproot3/
# will be using numpy from cvmfs
rm -rf uproot3/numpy*
