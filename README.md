# Cloud-Project
Problem Statement:- 
Design a predictive mechanism where in case of a potential low-
performance of a process is predicted (such as due to low potential resource availability), then the process fails over from one cloud to another.

### Prior requirements in user's machine:-
Python 3.7 must be installed in order to run the python scripts.

First run <b>add.py</b> which will add a new machine according to the user requirements.
Then Run <b>master.py</b> which keeps a check on all the virtual machines in a timed fashion.
In case there is a low potential resource detected we add a VM.

<b>machineData.json</b> contains all the details of all the virtual machines which are in use.

We use the bash scripts <b>setup.sh</b> and <b>proj.sh</b> in add.py to install the dependencies and keep a check of the CPU,Memory,Disk reads (resource utilization) to know when to start a new VM.
