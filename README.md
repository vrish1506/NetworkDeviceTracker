# NetworkDeviceTracker
NetworkDeviceTracker - Track a network machine through other network host. Retrieve the stats, logs and prepare report. 


GOAL #1. SSH to same box and run a DF command. Collect output. 

      Step 1 : SSH to Linux box from the same box and run the DF command. 
      Step 2 : Collect and filter the output to retrieve only relevant data
      Step 3 : Log the filered output in log file
      
      APPROACH #1.
      Step 1:  Configure a Ubuntu 16.0 box and Install Python and other needed modules
      Step 2:  Create a module to SSH to box and run DF command through functions and collect the return result  
      Step 3:  Create a main module which will accept IP, username and password from command line and execute SSH module 
      
        

    
