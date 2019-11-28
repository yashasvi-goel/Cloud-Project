# Cloud-Project
Problem Statement:- Design a predictive mechanism where, in case a potential low-
performance of a process is predicted (such as, due to low potential resource availability), then
the process fails over from one cloud to another.

Prior requirements in user's machine:-
Python 3.7 must be installed to run the python scripts.

First Run master.py which keeps a check on all the virtual machines in a timed fashion.
Then run add.py which will add a new machine according to the user requirements.
In case there is a low potential resource detected we add a VM.

machineData.json contains all the details of all the virtual machines which are in use.

We use the bash scripts setup.sh and proj.sh in add.py to install the dependencies and keep a check of the CPU,Memory,Disk reads (resource utilization) to know when to start a new VM.
