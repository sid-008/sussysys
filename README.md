# SUSSYSYS
## A syscall tracing dashboard
### (Part of PESU I/O slot-14 course material)


before running please activate venv: 
`source venv/bin/activate` 

also mount debugfs using:
`sudo mount -t debugfs none /sys/kernel/debug` 

To run the dashboard, the command is: 
`sudo streamlit run dashboard.py` 

# FOR SLOT-14 STUDENTS
You may also use strace to trace syscalls and use streamlit to make it into a real time tracing dashboard


# strace helpful commands
1. strace -c -p PID 

2. strace -e trace=write -p PID
(The argument for trace can be replaced by whatever kind of call you want to trace)

# General Instructions for PESU I/O kids:
The dashboard does not need to follow any sort of strict rules of sorts, for any clarifications you can contact me.

The bare minimum your project needs to do is either generate a report of the number of syscalls made in a time interval
or it needs to do real time tracing like is done in dashboard.py(preferred) you can choose to either work on the code already given or make a new project
on your own and use this repository as a reference. Do not hesitate to ask for help, however issues related to syntax errors 
will NOT be entertained, thats for you all to debug on your own :) 
