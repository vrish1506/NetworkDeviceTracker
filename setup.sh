#! /bin/bash

# Install python modules.


# TODO check for supported OS versions.
# TODO: add more modules
PYTHON_MODULES="paramiko"

# First install pip

sudo apt-get install python3-pip

for module in ${PYTHON_MODULES}; do 
	sudo python3 -m pip install ${module}



