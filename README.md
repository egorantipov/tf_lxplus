# Tensorflow + uproot setup for lxplus


## Get the repository:
```bahs
git clone https://github.com/egorantipov/tf_lxplus.git
```

## Setup uproot
Uproot is not available on `cvmfs`, therefore, it needs to be installed. `lxplus` doesn't give permissions to install packages as `sudo`, like `pip install uproot3`. Therefore, virtual envorinment is used. To handle python paths, `uproot3` is installed from target. Run `setup.sh` script just once. It creates a virtual environment, clones uproot3 from git, and installs it locally from the target.
```bash
source setup.sh
```


## Setup environment
Enables `tensorflov` and `uproot3`. Run each time you log-in to lxplus.
```bash
source setup_env.sh
```


## Run the analysis code
The input file is not on `git` for ATLAS data and simulation privacy reasons.
```bash
python classifier.py
```


# Running in Condor

There two files needed to run a job in condor: `myjob.sub` and `myjob.sh`. The first setupts job's parameters, and the second is the actual executalbe. To submit the job simply run:
```bash
condor_submit myjob.sub
```
The output, log and error files will appear in `condor/` directory.


# TODO
Implement simple NN setup. 
